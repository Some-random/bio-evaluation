"""Pure metadata policy tests; no credentials, network, or publication."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/publication_destination.py"
spec = importlib.util.spec_from_file_location("publication_destination", SCRIPT)
policy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(policy)


class DestinationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.path = self.root / policy.POLICY_PATH
        self.path.parent.mkdir()
        self.config = {"repository": policy.REPOSITORY, "visibility": "public", "publication_authorized": True,
            "user_authorization": {"quote": "prepare everytying publicly", "recorded_at_utc": "2026-10-16T19:23:37+00:00"}}
        self.repo = {"full_name": policy.REPOSITORY, "private": False, "permissions": {"push": True}}
        self.write()

    def tearDown(self):
        self.temp.cleanup()

    def write(self):
        self.path.write_text(json.dumps(self.config))

    def test_authorized_public_destination_keeps_real_visibility(self):
        result = policy.verify_repository_metadata(self.repo, self.root)
        self.assertFalse(result["private"])
        self.assertEqual(result["visibility"], "public")
        self.assertTrue(result["publication_authorized"])
        self.assertEqual(result["repository"], policy.REPOSITORY)
        self.assertEqual(len(result["destination_policy_sha256"]), 64)

    def test_identity_visibility_permission_and_authorization_fail_closed(self):
        for changes in [{"full_name": "another/repo"}, {"private": True}, {"permissions": {"push": False}}]:
            with self.subTest(changes=changes), self.assertRaises(RuntimeError):
                policy.verify_repository_metadata({**self.repo, **changes}, self.root)
        for key, value in [("publication_authorized", False), ("repository", "another/repo"), ("user_authorization", {})]:
            with self.subTest(key=key):
                self.config[key] = value
                self.write()
                with self.assertRaises(RuntimeError):
                    policy.verify_repository_metadata(self.repo, self.root)
                self.setUpConfig()

    def setUpConfig(self):
        self.config.update(repository=policy.REPOSITORY, visibility="public", publication_authorized=True,
            user_authorization={"quote": "prepare everytying publicly", "recorded_at_utc": "2026-10-16T19:23:37+00:00"})
        self.write()


if __name__ == "__main__":
    unittest.main()
