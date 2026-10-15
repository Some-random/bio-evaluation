import base64
import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from prepare_local_labbench_run import native_messages
from score_local_labbench_suite import metrics_for


class LocalLabSuiteTests(unittest.TestCase):
    def test_native_context_is_preserved_and_source_answers_are_not_copied(self):
        text = "Synthetic complete protocol and sequence\n" * 200
        row = {"payload": {"tools": [], "input": [{"role": "user", "content": [
            {"type": "input_text", "text": text}]}]}, "fields": {}, "ideal": "SCORER_ONLY"}
        messages = native_messages(row)
        self.assertEqual(messages, [{"role": "user", "content": text}])
        self.assertNotIn(row["ideal"], json.dumps(messages))

    def test_inline_image_bytes_and_native_detail_are_preserved(self):
        raw = b"synthetic-image-transport-fixture"
        url = "data:image/png;base64," + base64.b64encode(raw).decode()
        row = {"payload": {"tools": [], "input": [{"role": "user", "content": [
            {"type": "input_text", "text": "Synthetic question"},
            {"type": "input_image", "image_url": url, "detail": "high"}]}]},
            "fields": {"images_sha256": [hashlib.sha256(raw).hexdigest()]}}
        result = native_messages(row)
        self.assertEqual(result[0]["content"][1], {"type": "image_url", "image_url": {"url": url, "detail": "high"}})
        bad = copy.deepcopy(row)
        bad["fields"]["images_sha256"] = ["different"]
        with self.assertRaises(ValueError):
            native_messages(bad)
        bad = copy.deepcopy(row)
        bad["payload"]["input"][0]["content"][1]["image_url"] = "https://example.invalid/gold.png"
        with self.assertRaises(ValueError):
            native_messages(bad)

    def test_native_invalid_answers_count_as_incorrect_and_non_abstaining(self):
        rows = [{"correct": True, "sure": True}, {"correct": False, "sure": False},
                {"correct": False, "sure": True}]
        metrics = metrics_for(rows)
        self.assertEqual(metrics["accuracy"], 1 / 3)
        self.assertEqual(metrics["precision"], 1 / 2)
        self.assertEqual(metrics["coverage"], 2 / 3)


if __name__ == "__main__":
    unittest.main()
