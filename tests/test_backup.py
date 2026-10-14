import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

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


if __name__ == "__main__":
    unittest.main()
