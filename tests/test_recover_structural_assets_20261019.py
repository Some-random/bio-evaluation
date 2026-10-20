"""Local-only checks for range integrity and resumable source acquisition."""
import hashlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location(
    'structural_recovery', Path(__file__).parents[1] / 'scripts/recover_structural_assets_20261019.py')
RECOVERY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RECOVERY)


class Response(io.BytesIO):
    def __init__(self, body, status=206, content_range='bytes 2-4/7'):
        super().__init__(body)
        self.status = status
        self.headers = {'Content-Range': content_range}


class RecoveryIntegrityTests(unittest.TestCase):
    def test_only_unchanged_cached_chunks_are_reused(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(RECOVERY, 'CHUNK', 3):
            path = Path(folder) / 'partial'
            path.write_bytes(b'abcBADg')
            claimed = {str(i): {'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}
                       for i, b in enumerate([b'abc', b'def', b'g'])}
            self.assertEqual(set(RECOVERY.recheck_chunks(path, 7, claimed)), {'0', '2'})

    def test_missing_partial_cannot_reuse_journal(self):
        self.assertEqual(RECOVERY.recheck_chunks(Path('/nonexistent/recovery-partial'), 7,
                                                {'0': {'bytes': 7, 'sha256': 'fake'}}), {})

    def test_out_of_bounds_or_malformed_cached_ranges_are_rejected(self):
        with tempfile.TemporaryDirectory() as folder, patch.object(RECOVERY, 'CHUNK', 3):
            path = Path(folder) / 'partial'
            path.write_bytes(b'abc')
            bad = {'-1': {}, '01': {}, '1': {'bytes': 3},
                   '0': {'bytes': 2, 'sha256': hashlib.sha256(b'abc').hexdigest()}}
            self.assertEqual(RECOVERY.recheck_chunks(path, 3, bad), {})

    def test_completed_renamed_file_is_verified_without_partial(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'complete'
            path.write_bytes(b'complete')
            item = {'expected_bytes': 8, 'publisher_sha256': hashlib.sha256(b'complete').hexdigest()}
            result = RECOVERY.reuse_complete(path, item)
            self.assertTrue(result['publisher_sha256_verified'])
            self.assertTrue(result['reused_complete_file'])
            self.assertEqual(result['verified_chunk_bytes'], 8)

    def test_corrupt_completed_file_does_not_pass(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'complete'
            path.write_bytes(b'bad')
            with self.assertRaisesRegex(AssertionError, 'SHA256 mismatch'):
                RECOVERY.reuse_complete(path, {'expected_bytes': 3, 'publisher_sha256': '0' * 64})

    def test_exact_range_writes_only_requested_offset(self):
        with tempfile.TemporaryFile() as stream, patch.object(RECOVERY, 'get', return_value=Response(b'abc')):
            stream.write(b'.......')
            stream.flush()
            result = RECOVERY.transfer_range(stream.fileno(), {'url': 'fixture', 'expected_bytes': 7}, 2, 4)
            stream.seek(0)
            self.assertEqual(stream.read(), b'..abc..')
            self.assertEqual(result['sha256'], hashlib.sha256(b'abc').hexdigest())

    def test_ignored_or_wrong_ranges_and_wrong_body_lengths_are_rejected(self):
        for response in [Response(b'abc', status=200),
                         Response(b'abc', content_range='bytes 1-3/7'),
                         Response(b'ab'), Response(b'abcd')]:
            with self.subTest(status=response.status, headers=response.headers), tempfile.TemporaryFile() as stream:
                with patch.object(RECOVERY, 'get', return_value=response), self.assertRaises(AssertionError):
                    RECOVERY.transfer_range(stream.fileno(), {'url': 'fixture', 'expected_bytes': 7}, 2, 4)


if __name__ == '__main__':
    unittest.main()
