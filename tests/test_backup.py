import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile
from unittest.mock import patch
from types import SimpleNamespace

spec = importlib.util.spec_from_file_location(
    "daily_backup", Path(__file__).resolve().parents[1] / "scripts/daily_backup.py"
)
backup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(backup)


class CredentialProtectionTests(unittest.TestCase):
    def test_credential_across_read_boundary_is_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "notes.txt"
            file.write_bytes(b"x" * (1024 * 1024 - 2) + b"\nsk-" + b"Q" * 48)
            with self.assertRaises(backup.BackupError):
                backup.scan_file(file)

    def test_credential_inside_zip_is_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "bundle.zip"
            with zipfile.ZipFile(file, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.writestr("notes.txt", b"sk-" + b"Q" * 48)
            with self.assertRaises(backup.BackupError):
                backup.scan_file(file)

    def test_zip_cannot_hide_credential_filename_or_escape(self):
        for name in ["../escape.txt", "/absolute.txt", "openai_key_bio"]:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as directory:
                file = Path(directory) / "bundle.zip"
                with zipfile.ZipFile(file, "w") as archive:
                    archive.writestr(name, "synthetic")
                with self.assertRaises(backup.BackupError):
                    backup.scan_file(file)

    def test_public_remote_stops_before_push(self):
        settings = {"owner":"example", "repo_name":"bio-evaluation", "visibility":"private"}
        responses = [
            SimpleNamespace(returncode=0, stdout="example\n"),
            SimpleNamespace(returncode=0, stdout="https://github.com/example/bio-evaluation.git\n"),
        ]
        with patch.object(backup, "run", side_effect=responses), \
             patch.object(backup, "checked", return_value='{"private":false}'), \
             patch.object(backup, "push") as push:
            with self.assertRaises(backup.BackupError):
                backup.private_remote(settings)
            push.assert_not_called()


if __name__ == "__main__":
    unittest.main()
