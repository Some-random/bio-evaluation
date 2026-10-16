import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location("prepare_deepfri_sequence_contract", Path(__file__).resolve().parents[1] / "scripts/prepare_deepfri_sequence_contract.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class Info:
    def __init__(self, number, name, chain="A", insertion=" "):
        self.number, self.name, self.chain, self.insertion = number, name, chain, insertion
    def GetResidueNumber(self): return self.number
    def GetResidueName(self): return self.name
    def GetChainId(self): return self.chain
    def GetInsertionCode(self): return self.insertion


class Atom:
    def __init__(self, info): self.info = info
    def GetPDBResidueInfo(self): return self.info


class Molecule:
    def __init__(self, residues): self.atoms = [Atom(Info(*row)) for row in residues]
    def GetAtoms(self): return self.atoms
    def GetBonds(self): return []


class DeepFRIContractTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_full_fasta_preserves_source_ids_sequences_and_extra_split_entry(self):
        path = self.root / "test.fasta"
        path.write_text(">OLD-A source\nMX\nAC\n>RENAMED-A source\nSSG\n>EXTRA-B\nTTT\n")
        records = mod.read_fasta(path)
        self.assertEqual(list(records), ["OLD-A", "RENAMED-A", "EXTRA-B"])
        self.assertEqual(records["OLD-A"], "MXAC")
        path = self.root / "test.csv"
        path.write_text("PDB-chain,<30%,<40%,<50%,<70%,<95%\nOLD-A,0,0,0,1,1\nDROP-B,0,0,0,0,0\n")
        self.assertEqual(mod.read_split(path), (["OLD-A"], ["DROP-B"]))

    def test_global_vocabulary_is_header_order_and_references_stay_separate(self):
        annotation = self.root / "zenodo__GeneOntology__nrPDB-GO_annot.tsv"
        annotation.write_text("\n".join([
            "### MF", "GO:0000002\tGO:0000001", "### Names", "second\tfirst",
            "### BP", "GO:0000004", "### Names", "fourth",
            "### CC", "GO:0000003", "### Names", "third",
            "### Case\tMF\tBP\tCC", "CASE-A\tGO:0000001\tGO:0000004\tGO:0000003",
        ]) + "\n")
        vocabulary = mod.vocabulary(self.root, "GO_2019.06.18", "MF", 0)
        self.assertEqual([row["class_id"] for row in vocabulary["classes"]], ["GO:0000002", "GO:0000001"])
        self.assertNotIn("CASE-A", json.dumps(vocabulary))
        refs = mod.read_references(annotation, 0, {"CASE-A"}, {"GO:0000002": 0, "GO:0000001": 1})
        self.assertTrue(refs["CASE-A"]["scorer_only"])
        self.assertEqual(refs["CASE-A"]["positive_class_indices"], [1])

    def test_modeled_residues_do_not_fabricate_missing_fasta_residues(self):
        result = mod.modeled_sequence(Molecule([(3, "MSE"), (4, "SER")]))
        self.assertEqual(result["full_modeled_residue_sequence"], "GS")
        self.assertEqual(result["native_to_sequence_reconstruction"], "G.S")
        self.assertEqual(result["unknown_residue_names_mapped_to_glycine"], {"MSE": 1})
        self.assertEqual(result["modeled_residue_count"], 2)

    def test_source_boundary_collision_and_invalid_chain_remain_qualified(self):
        self.assertEqual(mod.modeled_sequence(Molecule([(1, "GLY")]))["status"], "native_dummy_residue_boundary_collision_requires_full_loader")
        self.assertEqual(mod.modeled_sequence(Molecule([(2, "ALA", "!")]))["status"], "invalid_chain_id")


if __name__ == "__main__":
    unittest.main()
