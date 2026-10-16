"""Read ZIP metadata or selected members using strictly checked HTTP ranges.

This verifies exact response bounds and records SHA-256 per acquired range.
It cannot verify the hash of an entire remote archive that was not downloaded.
It never starts SSH connections or invokes inference. Use zipfile.ZipFile over
HTTPRangeFile, optionally over stored_member_view for nested uncompressed ZIPs.
"""
import hashlib
import io
import struct
import urllib.parse
import urllib.request


class HTTPRangeFile(io.RawIOBase):
    def __init__(self, url, total_size, *, chunk_size=8 * 1024 * 1024,
                 max_read_bytes=64 * 1024 * 1024, cache_bust_parameter=None,
                 timeout=180, opener=None):
        self.url = url
        self.total_size = int(total_size)
        self.chunk_size = int(chunk_size)
        self.max_read_bytes = int(max_read_bytes)
        self.cache_bust_parameter = cache_bust_parameter
        self.timeout = timeout
        self.opener = opener or urllib.request.urlopen
        self.position = 0
        self.acquired_ranges = []

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self.position

    def seek(self, offset, whence=io.SEEK_SET):
        target = offset if whence == io.SEEK_SET else self.position + offset if whence == io.SEEK_CUR else self.total_size + offset if whence == io.SEEK_END else None
        if target is None or target < 0:
            raise ValueError("Invalid seek")
        self.position = target
        return target

    def read(self, size=-1):
        count = max(0, min(self.total_size - self.position, self.total_size if size is None or size < 0 else size))
        if count > self.max_read_bytes:
            raise ValueError("Read exceeds explicit range budget; stream the selected member in chunks")
        chunks = []
        while count:
            amount = min(count, self.chunk_size)
            start, end = self.position, self.position + amount - 1
            url = self.url
            if self.cache_bust_parameter:
                delimiter = "&" if urllib.parse.urlsplit(url).query else "?"
                url += delimiter + urllib.parse.urlencode({self.cache_bust_parameter: f"{start}-{end}"})
            request = urllib.request.Request(url, headers={"Range": f"bytes={start}-{end}"})
            with self.opener(request, timeout=self.timeout) as response:
                if response.status != 206 or response.headers.get("Content-Range") != f"bytes {start}-{end}/{self.total_size}":
                    raise ValueError("Server did not honor the exact requested range")
                data = response.read(amount + 1)
                if len(data) != amount:
                    raise ValueError("Range response length mismatch")
            self.acquired_ranges.append({"start": start, "end": end, "bytes": amount, "sha256": hashlib.sha256(data).hexdigest()})
            chunks.append(data)
            self.position += amount
            count -= amount
        return b"".join(chunks)

    def readinto(self, buffer):
        data = self.read(len(buffer))
        buffer[:len(data)] = data
        return len(data)


class StoredMemberView(io.RawIOBase):
    def __init__(self, parent, offset, size):
        self.parent, self.offset, self.total_size = parent, offset, size
        self.position = 0

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self.position

    def seek(self, offset, whence=io.SEEK_SET):
        target = offset if whence == io.SEEK_SET else self.position + offset if whence == io.SEEK_CUR else self.total_size + offset if whence == io.SEEK_END else None
        if target is None or target < 0:
            raise ValueError("Invalid seek")
        self.position = target
        return target

    def read(self, size=-1):
        count = max(0, min(self.total_size - self.position, self.total_size if size is None or size < 0 else size))
        self.parent.seek(self.offset + self.position)
        data = self.parent.read(count)
        self.position += len(data)
        return data


def stored_member_view(parent, zip_info):
    """Return a seekable view of a ZIP_STORED member for nested ZipFile use."""
    if zip_info.compress_type != 0 or zip_info.compress_size != zip_info.file_size:
        raise ValueError("Nested random access requires an uncompressed outer member")
    parent.seek(zip_info.header_offset)
    fields = struct.unpack("<4s5H3L2H", parent.read(30))
    if fields[0] != b"PK\x03\x04" or fields[3] != 0:
        raise ValueError("Stored local header mismatch")
    return StoredMemberView(parent, zip_info.header_offset + 30 + fields[-2] + fields[-1], zip_info.file_size)
