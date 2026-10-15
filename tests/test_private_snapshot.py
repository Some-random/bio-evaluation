import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import daily_backup as backup
import publish_private_snapshot as snapshot


class PrivateSnapshotTests(unittest.TestCase):
    def test_split_archive_rejoins_exactly_across_multiple_boundaries(self):
        raw = bytes(range(100))
        with tempfile.TemporaryDirectory() as folder:
            writer = snapshot.PartsWriter(Path(folder), limit=17)
            writer.write(raw[:11]);writer.write(raw[11:73]);writer.write(raw[73:]);writer.close()
            joined = b"".join((Path(folder) / p["name"]).read_bytes() for p in writer.parts)
            self.assertEqual(joined, raw)
            self.assertEqual(writer.total_hash.hexdigest(), hashlib.sha256(raw).hexdigest())
            for p in writer.parts:
                self.assertLessEqual(p["bytes"], 17)
                self.assertEqual(p["sha256"], hashlib.sha256((Path(folder) / p["name"]).read_bytes()).hexdigest())

    def test_public_wrong_owner_or_read_only_repositories_are_rejected(self):
        good = {"private": True, "full_name": "example/evaluation", "permissions": {"push": True}}
        snapshot.verify_private(good, "example/evaluation")
        for changed in [{**good, "private": False}, {**good, "full_name": "other/evaluation"},
                        {**good, "permissions": {"push": False}}]:
            with self.assertRaises(backup.BackupError):
                snapshot.verify_private(changed, "example/evaluation")

    def test_uploaded_size_without_matching_digest_is_not_accepted(self):
        item = {"bytes": 42, "sha256": "abc"}
        good = {"state": "uploaded", "size": 42, "digest": "sha256:abc"}
        self.assertTrue(snapshot.asset_matches(good, item))
        for changed in [{**good, "state": "starter"}, {**good, "size": 0},
                        {**good, "digest": None}, {**good, "digest": "sha256:other"}]:
            self.assertFalse(snapshot.asset_matches(changed, item))

    def test_credentials_and_environment_paths_are_excluded(self):
        for path in [".env", ".local/backup_environment.json", ".venv-vllm/bin/python",
                     ".cache/huggingface/token", "openai_key_bio"]:
            self.assertTrue(backup.secret_filename(path))
        with self.assertRaises(backup.BackupError):
            backup.scan_bytes(b"hf_" + b"z" * 40)


if __name__ == "__main__":
    unittest.main()
