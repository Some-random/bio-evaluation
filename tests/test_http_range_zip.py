import importlib.util
import io
from pathlib import Path
import unittest
import zipfile

spec = importlib.util.spec_from_file_location("http_range_zip", Path(__file__).resolve().parents[1] / "scripts/http_range_zip.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class Response(io.BytesIO):
    status = 206

    def __init__(self, data, start, end, total):
        super().__init__(data)
        self.headers = {"Content-Range": f"bytes {start}-{end}/{total}"}


class RangeZipTests(unittest.TestCase):
    def source(self, content):
        def opener(request, timeout):
            start, end = map(int, request.get_header("Range").removeprefix("bytes=").split("-"))
            return Response(content[start:end + 1], start, end, len(content))
        return mod.HTTPRangeFile("https://example.invalid/archive.zip", len(content), chunk_size=37, opener=opener)

    def test_selected_nested_member_and_crc_without_whole_archive(self):
        inner = io.BytesIO()
        with zipfile.ZipFile(inner, "w", zipfile.ZIP_DEFLATED) as out:
            out.writestr("test/case.txt", "synthetic full test input")
        outer = io.BytesIO()
        with zipfile.ZipFile(outer, "w", zipfile.ZIP_STORED) as out:
            out.writestr("unused_training.bin", b"x" * 200000)
            out.writestr("test.zip", inner.getvalue())
        source = self.source(outer.getvalue())
        with zipfile.ZipFile(source) as container:
            with zipfile.ZipFile(mod.stored_member_view(source, container.getinfo("test.zip"))) as test:
                self.assertEqual(test.read("test/case.txt"), b"synthetic full test input")
        self.assertLess(sum(row["bytes"] for row in source.acquired_ranges), len(outer.getvalue()))

    def test_ignored_range_and_over_budget_are_rejected(self):
        source = self.source(b"1234")
        source.max_read_bytes = 2
        with self.assertRaises(ValueError):
            source.read()
        class Bad(Response):
            status = 200
        source = mod.HTTPRangeFile("https://example.invalid/a", 4, opener=lambda *args, **kwargs: Bad(b"1234", 0, 3, 4))
        with self.assertRaises(ValueError):
            source.read(1)


if __name__ == "__main__":
    unittest.main()
