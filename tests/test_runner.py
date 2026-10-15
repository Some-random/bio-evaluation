import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import json

spec = importlib.util.spec_from_file_location("runner",Path(__file__).resolve().parents[1]/"scripts/run_evaluations.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class ResourceAndProtocolTests(unittest.TestCase):
    def test_policy_hold_stops_before_credentials_or_network(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/"configs").mkdir()
            (root/"configs/execution_authorization.json").write_text(json.dumps({"policy_warning_active":True,"inference_authorized":True}))
            with patch.object(runner,"ROOT",root), \
                 patch("sys.argv",["run_evaluations.py","--inputs","unused","--run","test"]), \
                 patch.object(runner,"Client") as client:
                with self.assertRaisesRegex(SystemExit,"Policy warning hold"):
                    runner.main()
                client.assert_not_called()

    def test_reservations_block_overspend_and_persist(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/"ledger.sqlite"
            ledger = runner.Ledger(path,1)
            self.assertTrue(ledger.reserve("first",.8))
            self.assertFalse(ledger.reserve("second",.3))
            ledger.finish("first",.1,"completed")
            self.assertTrue(runner.Ledger(path,1).reserve("second",.3))
            self.assertFalse(ledger.reserve("first",.1))

    def test_usage_includes_reasoning_and_long_context_rates(self):
        self.assertAlmostEqual(runner.usage_cost({"input_tokens":100,"output_tokens":1000,
            "output_tokens_details":{"reasoning_tokens":900}}),.00051)
        self.assertAlmostEqual(runner.usage_cost({"input_tokens":300000,"output_tokens":1000}),.06075)

    def test_unreviewed_and_tool_enabled_protocols_are_rejected(self):
        with self.assertRaises(ValueError):
            runner.payload_for({"variant":"DRAFT", "task":"P30"})
        with self.assertRaises(ValueError):
            runner.payload_for({"variant":"NATIVE", "task":"P18",
                "payload":{"model":runner.MODEL,"tools":[{"type":"web_search"}]}})


if __name__ == "__main__":
    unittest.main()
