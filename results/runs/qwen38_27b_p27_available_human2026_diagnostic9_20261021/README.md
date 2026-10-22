# Protein function description: nine-case diagnostic

Qwen3.8-27B produced nine descriptions from full human protein sequences in a frozen UniProt2026_03 snapshot. All nine responses were delivered and scored once with ROUGE-L: **0.0462**. The declared query returned twelve candidates; three lacked function comments and were excluded before generation. Exact sequence overlap with the four completed Mol-Instructions description cohorts is zero.

This small available-source diagnostic does not reproduce NatureLM’s unreleased temporal NCBI evaluation and cannot be compared directly with its paper score. UniProt creation dates do not prove first sequence publication, first functional annotation or absence from model pretraining. ROUGE measures lexical agreement, not factual correctness.

Complete questions and saved responses accompany this result; reference annotations remain outside the public trajectory package.

[UniProt API](https://rest.uniprot.org/uniprotkb/search) · [NatureLM paper (2025)](https://arxiv.org/abs/2502.07527)
