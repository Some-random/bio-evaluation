import importlib.util
import json
from pathlib import Path
import tarfile
from types import SimpleNamespace
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/prepare_p40_structure_metadata_20261020.py"
SPEC = importlib.util.spec_from_file_location("p40_prep", SCRIPT)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def chain(name="H", insert=False):
    residues = [M.Residue(i, "", {23: "CYS", 41: "TRP", 104: "CYS"}.get(i, "ALA"), (float(i), 0.0, 0.0)) for i in range(1, 130)]
    if insert:
        residues.insert(110, M.Residue(110, "A", "ALA", (110.5, 0.0, 0.0)))
    return M.Chain(name, residues)


class Numbering(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = SCRIPT.parents[1]
        with tarfile.open(root / ".local/source_recovery_round2_2026-10-19/structural/source_archives/THUNLP-MT__MEAN.tar.gz") as tf:
            cls.source = tf.extractfile(next(n for n in tf.getnames() if n.endswith("/data/pdb_utils.py"))).read()
        cls.native = staticmethod(M.native_mask_function(cls.source))

    def test_insertion_codes_retained_and_mask_bounded(self):
        h, l = chain(insert=True), chain("L")
        selected, bounds = self.native(SimpleNamespace(heavy_chain="H", light_chain="L"), {"H": h, "L": l}, "imgt")
        data = M.masked_metadata(selected["H"], bounds["CDR-H3"])
        self.assertEqual(data["cdrh3_residue_count"], 14)
        self.assertEqual(sum(data["target_mask"]), 14)
        self.assertIn({"number": 110, "insertion_code": "A"}, data["fv_numbering"])
        self.assertEqual(data["cdrh3_zero_based_inclusive"], [104, 117])

    def test_wrong_conserved_number_fails(self):
        h = chain()
        h.residues[22].name = "ALA"
        with self.assertRaises(AssertionError):
            self.native(SimpleNamespace(heavy_chain="H", light_chain="L"), {"H": h, "L": chain("L")}, "imgt")

    def test_source_mutation_is_rejected(self):
        with self.assertRaises(ValueError):
            M.native_mask_function(self.source + b"\n# changed\n")

    def test_missing_cdr_is_rejected(self):
        h = chain()
        h.residues = [r for r in h.residues if not 105 <= r.number <= 117]
        with self.assertRaises(ValueError):
            self.native(SimpleNamespace(heavy_chain="H", light_chain="L"), {"H": h, "L": chain("L")}, "imgt")

    def test_duplicate_numbering_rejected(self):
        h = chain()
        h.residues.insert(105, h.residues[104])
        with self.assertRaises(ValueError):
            M.masked_metadata(h, (104, 117))

    def test_no_reference_identity_or_coordinates_emitted(self):
        data = M.masked_metadata(chain(), (104, 116))
        serial = json.dumps(data)
        for prohibited in ["ALA", "CYS", "TRP", "point", "coord", '"name"']:
            self.assertNotIn(prohibited, serial)


class ChainMapping(unittest.TestCase):
    def test_direct_contract(self):
        original = {"pdb": "fake", "heavy_chain": "H", "light_chain": "L", "antigen_chains": ["A"]}
        result = M.resolve_chains(original, [], {"H", "L", "A"})
        self.assertEqual(result[:3], ("H", "L", ["A"]))

    def test_declared_split_contract(self):
        original = {"pdb": "fake", "heavy_chain": "B", "light_chain": "B", "antigen_chains": ["A"]}
        row = {"INSTANCE": "fake-B2-B1", "Hchain": "B2", "Lchain": "B1", "antigen_chain": "A|Z", "chainsharing_construct": "SCFV"}
        result = M.resolve_chains(original, [row], {"B2", "B1", "A"})
        self.assertEqual(result[:3], ("B2", "B1", ["A"]))

    def test_split_ambiguity_not_guessed(self):
        original = {"pdb": "fake", "heavy_chain": "B", "light_chain": "B", "antigen_chains": ["A"]}
        row = {"INSTANCE": "fake", "Hchain": "B2", "Lchain": "B1", "antigen_chain": "A", "chainsharing_construct": "SCFV"}
        with self.assertRaises(ValueError):
            M.resolve_chains(original, [row, row], {"B2", "B1", "A"})

    def test_missing_original_antigen_is_not_substituted(self):
        original = {"pdb": "fake", "heavy_chain": "B", "light_chain": "B", "antigen_chains": ["A"]}
        row = {"INSTANCE": "fake", "Hchain": "B2", "Lchain": "B1", "antigen_chain": "Z", "chainsharing_construct": "SCFV"}
        with self.assertRaises(ValueError):
            M.resolve_chains(original, [row], {"B2", "B1", "A", "Z"})


class ContextGeometry(unittest.TestCase):
    def test_global48_closest_and_original_indices(self):
        import numpy
        antigen = M.Chain("A", [M.Residue(i, "", "ALA", (float(i), 0., 0.)) for i in range(70)])
        ab = M.Chain("H", [M.Residue(1, "", "ALA", (0., 0., 0.))])
        result = M.native_interface_indices([antigen], [ab], numpy)
        self.assertEqual(set(result["A"]), set(range(48)))

    def test_short_context_retained_whole(self):
        import numpy
        antigen = M.Chain("A", [M.Residue(i, "", "ALA", (float(i), 0., 0.)) for i in range(5)])
        ab = M.Chain("H", [M.Residue(1, "", "ALA", (0., 0., 0.))])
        self.assertEqual(set(M.native_interface_indices([antigen], [ab], numpy)["A"]), set(range(5)))

    def test_matches_pinned_native_interface_method_including_order(self):
        import numpy
        root = SCRIPT.parents[1]
        with tarfile.open(root / ".local/source_recovery_round2_2026-10-19/structural/source_archives/THUNLP-MT__MEAN.tar.gz") as tf:
            source = tf.extractfile(next(n for n in tf.getnames() if n.endswith("/data/pdb_utils.py"))).read()
        fn = M.native_method(source, "_cal_interface", {"np": numpy, "print_log": lambda *args: None})
        ag = [M.Chain(name, [M.Residue(i, "", "ALA", (float(i), shift, 0.)) for i in range(35)]) for name, shift in [("A", 0.), ("B", 1.)]]
        ab = [M.Chain("H", [M.Residue(1, "", "ALA", (0., 0., 0.))]), M.Chain("L", [M.Residue(1, "", "ALA", (3., 2., 0.))])]
        context = SimpleNamespace(get_antigen_chains=lambda: ag, get_heavy_chain=lambda: ab[0], get_light_chain=lambda: ab[1], num_interface_residue=48)
        fn(context)
        self.assertEqual(M.native_interface_indices(ag, ab, numpy), context.antigen_interface)


if __name__ == "__main__":
    unittest.main()
