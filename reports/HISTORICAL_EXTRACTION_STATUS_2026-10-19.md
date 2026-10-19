# Historical output diagnostics

Prepared October 19, 2026, Pacific time. Original scores and benchmark outputs remain unchanged. No model inference occurred.

The requested historical P01 and V01–V05 extraction diagnostics cannot currently be scored: their original raw run folders are absent. The same holds for the original B02 and P42 folders. Four retained publication checkouts, the initial 2,493-file archive manifest and all 24 public releases (19,010 asset records) were checked; none contain a matching original-run asset or archive member. The original `/data/rustfs1/dongweij` mount is unavailable. Exact search evidence and preserved counts are in `historical_availability.json`. This reports unavailable evidence, not zero parser recoveries.

`extraction_rules_v1.py` is a concrete label-blind diagnostic implementation, frozen before any reference comparisons. Twelve synthetic tests pass. It accepts exact binary/ABCD answers or explicit terminal answer declarations, rejects ambiguity and unfinished outputs, and uses only the visible final channel. Arbitrary explanatory prose is not silently converted to a medical answer. Free-text extraction requires an explicit terminal answer field. It never inspects hidden reasoning or references.

`run_visible_extraction.py` implements whole-case-set accounting for those rules. It requires a verified original case set and per-response hashes, checks raw versus saved final content, preserves missing and invalid slots, and computes extraction diagnostics only. Six synthetic integrity tests pass, including tampering, count mismatch, missing slots and hidden-reasoning isolation. No historical benchmark correctness has been recomputed. Restoring the originals and full case-set proofs is the remaining dependency.

P42's preserved aggregate reports 0/200 parsed candidates and 196 output-cap finishes; its frozen generation config used 1,024 output tokens with thinking enabled. B02's preserved aggregate reports 427/520 parsed and 93 output-cap finishes. These are historical metadata checks, not a fresh audit of unavailable raw responses. `p42_synthetic_contract_receipt.json` validates the actual candidate schema using a fabricated ten-residue sequence without biological optimization, assay labels or oracle calls.

[Download frozen rules, checks and availability evidence](benchmark_assets/historical_extraction_tools_2026-10-19.tar.gz) · [Action plan](EVALUATION_REPAIR_PLAN_2026-10-19.md)
