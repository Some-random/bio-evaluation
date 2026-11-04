# transmembrane_0033

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0033.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 14..34; 78..98; 114..134; 137..157; 162..182; 193..213; 235..255; 328..348; 380..400; 471..491

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MWSLDPSQKEVLRFAVSCRILTLMLQALFNIIIPDHHADAFSPPRLASSCSVDQLVEGLLGGLSRWDAEHFLFIAEHGYLYEHNFAFFPGFPLALLMGTELLRPLQGLLSQRSCLLVSVALLNFLFSVLAAVTLHDLGCLVLGCPRQAFYAAMLFCLSPANVFLAAGYSEALFAFLTFSAMGQLERGRSWASGLLFALATGVRSNGLVSVGFLLHAQCRGFFSSLVVLNPLKPLFKLMASLCLSVLTVSLPFALFQYYAYTQFCLPGSAHSVPEPLVQLAVDKGYRITGGNEPPWCSWGLPLVYSYIQDVYWNVGFLRYYELRQVPNFLLATPVAVLVVWAAWTYVTTHPWLCLTLGLRRSKDSKKTLEKPHPGFLSPKVFVYLVHAAGLLLFGSLCMHVQVLTRLLCSSTPVVYWFPAHLLQNQEPLLRSVDTVPEKLLEKNSPPGQKAPRNCIMKLLYNWRACSPVTRCILGYFLTYWLLGLLLHCNFLPWT

[Multiple Choices]
A. 14..34; 78..98; 114..134; 137..157; 162..182; 193..213; 235..255; 328..348; 380..400; 471..491
B. 14..34; 78..98; 114..134; 162..182; 193..213; 235..255; 328..348; 380..400; 471..491
C. 41..61
D. 14..34; 78..98; 114..134; 137..157; 158..178; 193..213; 235..255; 328..348; 380..400; 471..491
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

* Protein Sequence: The amino acid sequence of the protein.
* Multiple Choices: Candidate answers for the protein-related question.

Please think step-by-step about this problem:
1. Analyze the protein sequence carefully.
2. Consider the biological context and function.
3. Evaluate each multiple-choice option.
4. Provide your reasoning process.
5. Finally, give your answer.

Provide your response in the following format:
1. reasoning: [Your detailed reasoning here]
2. answer: Your final answer, which should be "A", "B", "C" or "D".
```

</details>

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched archived UniProt entry annotates all ten segments in A as transmembrane helices. These are computational annotations (ECO:0000255), not direct experimental demonstrations of each boundary.

Citations as saved: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains repeated hydrophobic stretches of roughly membrane-helix length, supporting the listed multipass topology. In particular, residues 137–157 are largely hydrophobic despite a few helix-disfavoring or polar residues, providing a sequence-based reason to prefer A over B. The hydrophobic run beginning around 162 also fits better than D’s proposed interval, which starts with SPAN and truncates the hydrophobic stretch at its other end.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The options differ at regions whose hydrophobicity can be assessed directly from the supplied sequence. Family-level knowledge about multipass membrane proteins supports interpreting these stretches as membrane helices; exact boundaries remain less certain than the broad helix calls.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is the most defensible offered set. Membrane-helix boundaries can be uncertain by a few residues, but the shifted interval in D includes a less hydrophobic N-terminal segment and omits part of the stronger hydrophobic run; that uncertainty does not make it as defensible as A here.


### Important caveats

- The matching source annotations are computational, and the exact boundaries should not be treated as experimentally established.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains repeated hydrophobic stretches of roughly membrane-helix length, supporting the listed multipass topology. In particular, residues 137–157 are largely hydrophobic despite a few helix-disfavoring or polar residues, providing a sequence-based reason to prefer A over B. The hydrophobic run beginning around 162 also fits better than D’s proposed interval, which starts with SPAN and truncates the hydrophobic stretch at its other end.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The options differ at regions whose hydrophobicity can be assessed directly from the supplied sequence. Family-level knowledge about multipass membrane proteins supports interpreting these stretches as membrane helices; exact boundaries remain less certain than the broad helix calls."
  },
  "case_id": "transmembrane_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched archived UniProt entry annotates all ten segments in A as transmembrane helices. These are computational annotations (ECO:0000255), not direct experimental demonstrations of each boundary."
  },
  "important_caveats": [
    "The matching source annotations are computational, and the exact boundaries should not be treated as experimentally established."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the most defensible offered set. Membrane-helix boundaries can be uncertain by a few residues, but the shifted interval in D includes a less hydrophobic N-terminal segment and omits part of the stronger hydrophobic run; that uncertainty does not make it as defensible as A here."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched archived UniProt entry annotates all ten segments in A as transmembrane helices. These are computational annotations (ECO:0000255), not direct experimental demonstrations of each boundary.",
    "evidence_ids": ["H4", "H6", "H8", "H10", "H12", "H14", "H16", "H18", "H20", "H22"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains repeated hydrophobic stretches of roughly membrane-helix length, supporting the listed multipass topology. In particular, residues 137–157 are largely hydrophobic despite a few helix-disfavoring or polar residues, providing a sequence-based reason to prefer A over B. The hydrophobic run beginning around 162 also fits better than D’s proposed interval, which starts with SPAN and truncates the hydrophobic stretch at its other end.",
    "missing_item_specific_fact": "",
    "reason": "The options differ at regions whose hydrophobicity can be assessed directly from the supplied sequence. Family-level knowledge about multipass membrane proteins supports interpreting these stretches as membrane helices; exact boundaries remain less certain than the broad helix calls."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the most defensible offered set. Membrane-helix boundaries can be uncertain by a few residues, but the shifted interval in D includes a less hydrophobic N-terminal segment and omits part of the stronger hydrophobic run; that uncertainty does not make it as defensible as A here."
  },
  "important_caveats": [
    "The matching source annotations are computational, and the exact boundaries should not be treated as experimentally established."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (A0A8C2M425, PIGV_CRIGR, 494 AA) lists exactly 10 transmembrane helical regions at 14..34, 78..98, 114..134, 137..157, 162..182, 193..213, 235..255, 328..348, 380..400, and 471..491, matching option A precisely. The TM annotations carry evidence code ECO:0000255 (similarity to other proteins, specifically Q9NUD9), indicating computational/transferred annotation rather than direct experimental determination. The topological domain assignments (cytoplasmic/lumenal) are also by similarity (ECO:0000250). The sequence match is confirmed.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can apply hydrophobicity-based TM prediction principles to distinguish the options. (1) Option C (single 20-residue region at 41..61) is trivially eliminated: the sequence contains numerous extended hydrophobic stretches across 494 residues, characteristic of a multi-pass membrane protein, not a single-pass protein. (2) Option D vs A: Option D places a TM at 158..178, which would include S(158), P(159), A(160), N(161) at its N-terminus. Serine, proline, and asparagine are strongly polar/helix-disrupting residues that are highly unusual within a TM alpha-helix. Transferable knowledge from TM helix composition (e.g., the 'positive-inside' rule, polar residue exclusion in TM cores) clearly argues the TM boundary should begin after these polar residues, at V(162), favoring A over D. (3) Option B vs A: Option B omits the 137..157 TM. A Kyte-Doolittle hydrophobicity scan of residues 137-157 (L G C L V L G C P R Q A F Y A A M L F C L; mean KD ≈ +1.4) shows moderate but above-threshold hydrophobicity. While this region contains some polar residues (R, Q, P, G, C), it is still within the range typically called a TM helix by standard predictors. The very short inter-TM loop (only H-D at 135-136) is unusual but occurs in densely packed multi-pass proteins. A model applying sliding-window hydrophobicity analysis would likely identify ~10 TM segments including 137..157, distinguishing A from B. The overall count of ~10 TM regions is also consistent with the pattern of alternating hydrophobic and hydrophilic stretches visible across the full sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The key distinctions between options rely on transferable TM-prediction principles: (a) polar/helix-disrupting residues (S, P, N) at 158-161 clearly mark the boundary between options A and D; (b) hydrophobicity of the 137-157 segment, while moderate, exceeds standard TM thresholds and supports its inclusion, distinguishing A from B; (c) the multi-pass pattern eliminates C. These are general biophysical and sequence-analysis arguments applicable to any membrane protein, not requiring recall of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the 137..157 region (A vs B) is the most borderline distinction, its hydrophobicity is still above typical TM thresholds, and the overall pattern of ~10 TM segments is identifiable. The A vs D distinction is clear-cut due to polar residues at 158-161. No two options are equally defensible given standard hydrophobicity-based reasoning.


### Important caveats

- The UniProt TM annotations use evidence code ECO:0000255 (similarity to Q9NUD9, human PIGV), meaning they are computationally transferred rather than experimentally determined. The exact boundaries could differ in a de novo prediction.
- The 137..157 TM region is the most ambiguous: it contains charged residues (R, Q) and helix-disrupting proline, making its classification as TM borderline. A model using a stricter hydrophobicity threshold might reasonably exclude it, producing option B.
- The protein is annotated as PIGV (GPI alpha-1,6-mannosyltransferase 2) from Cricetulus griseus, but this identity is not provided to the evaluated model and should not be used as an original input.
- All topological domain assignments (cytoplasmic/lumenal) are by similarity to the human ortholog Q9NUD9, not from direct experimental topology determination of this specific protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can apply hydrophobicity-based TM prediction principles to distinguish the options. (1) Option C (single 20-residue region at 41..61) is trivially eliminated: the sequence contains numerous extended hydrophobic stretches across 494 residues, characteristic of a multi-pass membrane protein, not a single-pass protein. (2) Option D vs A: Option D places a TM at 158..178, which would include S(158), P(159), A(160), N(161) at its N-terminus. Serine, proline, and asparagine are strongly polar/helix-disrupting residues that are highly unusual within a TM alpha-helix. Transferable knowledge from TM helix composition (e.g., the 'positive-inside' rule, polar residue exclusion in TM cores) clearly argues the TM boundary should begin after these polar residues, at V(162), favoring A over D. (3) Option B vs A: Option B omits the 137..157 TM. A Kyte-Doolittle hydrophobicity scan of residues 137-157 (L G C L V L G C P R Q A F Y A A M L F C L; mean KD ≈ +1.4) shows moderate but above-threshold hydrophobicity. While this region contains some polar residues (R, Q, P, G, C), it is still within the range typically called a TM helix by standard predictors. The very short inter-TM loop (only H-D at 135-136) is unusual but occurs in densely packed multi-pass proteins. A model applying sliding-window hydrophobicity analysis would likely identify ~10 TM segments including 137..157, distinguishing A from B. The overall count of ~10 TM regions is also consistent with the pattern of alternating hydrophobic and hydrophilic stretches visible across the full sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The key distinctions between options rely on transferable TM-prediction principles: (a) polar/helix-disrupting residues (S, P, N) at 158-161 clearly mark the boundary between options A and D; (b) hydrophobicity of the 137-157 segment, while moderate, exceeds standard TM thresholds and supports its inclusion, distinguishing A from B; (c) the multi-pass pattern eliminates C. These are general biophysical and sequence-analysis arguments applicable to any membrane protein, not requiring recall of this specific protein's database entry."
  },
  "case_id": "transmembrane_0033",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C24"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A8C2M425, PIGV_CRIGR, 494 AA) lists exactly 10 transmembrane helical regions at 14..34, 78..98, 114..134, 137..157, 162..182, 193..213, 235..255, 328..348, 380..400, and 471..491, matching option A precisely. The TM annotations carry evidence code ECO:0000255 (similarity to other proteins, specifically Q9NUD9), indicating computational/transferred annotation rather than direct experimental determination. The topological domain assignments (cytoplasmic/lumenal) are also by similarity (ECO:0000250). The sequence match is confirmed."
  },
  "important_caveats": [
    "The UniProt TM annotations use evidence code ECO:0000255 (similarity to Q9NUD9, human PIGV), meaning they are computationally transferred rather than experimentally determined. The exact boundaries could differ in a de novo prediction.",
    "The 137..157 TM region is the most ambiguous: it contains charged residues (R, Q) and helix-disrupting proline, making its classification as TM borderline. A model using a stricter hydrophobicity threshold might reasonably exclude it, producing option B.",
    "The protein is annotated as PIGV (GPI alpha-1,6-mannosyltransferase 2) from Cricetulus griseus, but this identity is not provided to the evaluated model and should not be used as an original input.",
    "All topological domain assignments (cytoplasmic/lumenal) are by similarity to the human ortholog Q9NUD9, not from direct experimental topology determination of this specific protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the 137..157 region (A vs B) is the most borderline distinction, its hydrophobicity is still above typical TM thresholds, and the overall pattern of ~10 TM segments is identifiable. The A vs D distinction is clear-cut due to polar residues at 158-161. No two options are equally defensible given standard hydrophobicity-based reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0033",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A8C2M425, PIGV_CRIGR, 494 AA) lists exactly 10 transmembrane helical regions at 14..34, 78..98, 114..134, 137..157, 162..182, 193..213, 235..255, 328..348, 380..400, and 471..491, matching option A precisely. The TM annotations carry evidence code ECO:0000255 (similarity to other proteins, specifically Q9NUD9), indicating computational/transferred annotation rather than direct experimental determination. The topological domain assignments (cytoplasmic/lumenal) are also by similarity (ECO:0000250). The sequence match is confirmed.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "C20", "C22", "C24"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can apply hydrophobicity-based TM prediction principles to distinguish the options. (1) Option C (single 20-residue region at 41..61) is trivially eliminated: the sequence contains numerous extended hydrophobic stretches across 494 residues, characteristic of a multi-pass membrane protein, not a single-pass protein. (2) Option D vs A: Option D places a TM at 158..178, which would include S(158), P(159), A(160), N(161) at its N-terminus. Serine, proline, and asparagine are strongly polar/helix-disrupting residues that are highly unusual within a TM alpha-helix. Transferable knowledge from TM helix composition (e.g., the 'positive-inside' rule, polar residue exclusion in TM cores) clearly argues the TM boundary should begin after these polar residues, at V(162), favoring A over D. (3) Option B vs A: Option B omits the 137..157 TM. A Kyte-Doolittle hydrophobicity scan of residues 137-157 (L G C L V L G C P R Q A F Y A A M L F C L; mean KD ≈ +1.4) shows moderate but above-threshold hydrophobicity. While this region contains some polar residues (R, Q, P, G, C), it is still within the range typically called a TM helix by standard predictors. The very short inter-TM loop (only H-D at 135-136) is unusual but occurs in densely packed multi-pass proteins. A model applying sliding-window hydrophobicity analysis would likely identify ~10 TM segments including 137..157, distinguishing A from B. The overall count of ~10 TM regions is also consistent with the pattern of alternating hydrophobic and hydrophilic stretches visible across the full sequence.",
    "missing_item_specific_fact": "",
    "reason": "The key distinctions between options rely on transferable TM-prediction principles: (a) polar/helix-disrupting residues (S, P, N) at 158-161 clearly mark the boundary between options A and D; (b) hydrophobicity of the 137-157 segment, while moderate, exceeds standard TM thresholds and supports its inclusion, distinguishing A from B; (c) the multi-pass pattern eliminates C. These are general biophysical and sequence-analysis arguments applicable to any membrane protein, not requiring recall of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the 137..157 region (A vs B) is the most borderline distinction, its hydrophobicity is still above typical TM thresholds, and the overall pattern of ~10 TM segments is identifiable. The A vs D distinction is clear-cut due to polar residues at 158-161. No two options are equally defensible given standard hydrophobicity-based reasoning."
  },
  "important_caveats": [
    "The UniProt TM annotations use evidence code ECO:0000255 (similarity to Q9NUD9, human PIGV), meaning they are computationally transferred rather than experimentally determined. The exact boundaries could differ in a de novo prediction.",
    "The 137..157 TM region is the most ambiguous: it contains charged residues (R, Q) and helix-disrupting proline, making its classification as TM borderline. A model using a stricter hydrophobicity threshold might reasonably exclude it, producing option B.",
    "The protein is annotated as PIGV (GPI alpha-1,6-mannosyltransferase 2) from Cricetulus griseus, but this identity is not provided to the evaluated model and should not be used as an original input.",
    "All topological domain assignments (cytoplasmic/lumenal) are by similarity to the human ortholog Q9NUD9, not from direct experimental topology determination of this specific protein."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 494,
  "benchmark_sequence_sha256": "9d3f46ba22c4115b7a8c603ef5a943e2972a8c829daba3e4cf44f5137f9c98a1",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-01-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 494,
  "current_source_sequence_sha256": "9d3f46ba22c4115b7a8c603ef5a943e2972a8c829daba3e4cf44f5137f9c98a1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A8C2M425",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "selected_historical_source_sequence_length": 494,
  "selected_historical_source_sequence_sha256": "9d3f46ba22c4115b7a8c603ef5a943e2972a8c829daba3e4cf44f5137f9c98a1",
  "selected_historical_version": {
    "accession": "A0A8C2M425",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PIGV_CRIGR",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A8C2M425\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-01-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Chinese hamster\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Cricetidae\",\"Cricetinae\",\"Cricetulus\"],\"scientificName\":\"Cricetulus griseus\",\"synonyms\":[\"Cricetulus barabensis griseus\"],\"taxonId\":10029}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"GPI mannosyltransferase II\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"GPI-MT-II\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"Phosphatidylinositol-glycan biosynthesis class V protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"PIG-V\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"GPI alpha-1,6-mannosyltransferase 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":13},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":34},\"start\":{\"modifier\":\"EXACT\",\"value\":14}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Lumenal\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":77},\"start\":{\"modifier\":\"EXACT\",\"value\":35}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":98},\"start\":{\"modifier\":\"EXACT\",\"value\":78}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":113},\"start\":{\"modifier\":\"EXACT\",\"value\":99}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":134},\"start\":{\"modifier\":\"EXACT\",\"value\":114}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Lumenal\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":136},\"start\":{\"modifier\":\"EXACT\",\"value\":135}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":157},\"start\":{\"modifier\":\"EXACT\",\"value\":137}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":161},\"start\":{\"modifier\":\"EXACT\",\"value\":158}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":182},\"start\":{\"modifier\":\"EXACT\",\"value\":162}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Lumenal\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":192},\"start\":{\"modifier\":\"EXACT\",\"value\":183}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":213},\"start\":{\"modifier\":\"EXACT\",\"value\":193}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":234},\"start\":{\"modifier\":\"EXACT\",\"value\":214}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":255},\"start\":{\"modifier\":\"EXACT\",\"value\":235}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Lumenal\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":327},\"start\":{\"modifier\":\"EXACT\",\"value\":256}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C20",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":348},\"start\":{\"modifier\":\"EXACT\",\"value\":328}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C21

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C21",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":379},\"start\":{\"modifier\":\"EXACT\",\"value\":349}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/17",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C22",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":400},\"start\":{\"modifier\":\"EXACT\",\"value\":380}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/18",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C23

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C23",
  "excerpt": "{\"description\":\"Lumenal\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":470},\"start\":{\"modifier\":\"EXACT\",\"value\":401}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/19",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C24",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":491},\"start\":{\"modifier\":\"EXACT\",\"value\":471}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/20",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C25

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C25",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":494},\"start\":{\"modifier\":\"EXACT\",\"value\":492}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/21",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C26",
  "excerpt": "{\"citation\":{\"authors\":[\"Hirata T.\",\"Fujita M.\",\"Kanzawa N.\",\"Murakami Y.\",\"Maeda Y.\",\"Kinoshita T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23694781\"},{\"database\":\"DOI\",\"id\":\"10.1093/jb/mvt045\"}],\"citationType\":\"journal article\",\"firstPage\":\"257\",\"id\":\"23694781\",\"journal\":\"J. Biochem.\",\"lastPage\":\"264\",\"publicationDate\":\"2013\",\"title\":\"Glycosylphosphatidylinositol mannosyltransferase II is the rate-limiting enzyme in glycosylphosphatidylinositol biosynthesis under limited dolichol-phosphate mannose availability.\",\"volume\":\"154\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   PIGV_CRIGR              Reviewed;         494 AA.\nAC   A0A8C2M425;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-JAN-2022, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=GPI alpha-1,6-mannosyltransferase 2 {ECO:0000250|UniProtKB:Q9NUD9};\nDE            EC=2.4.1.- {ECO:0000269|PubMed:23694781};\nDE   AltName: Full=GPI mannosyltransferase II;\nDE            Short=GPI-MT-II {ECO:0000250|UniProtKB:Q9NUD9};\nDE   AltName: Full=Phosphatidylinositol-glycan biosynthesis class V protein {ECO:0000250|UniProtKB:Q9NUD9};\nDE            Short=PIG-V {ECO:0000250|UniProtKB:Q9NUD9};\nGN   Name=PIGV {ECO:0000303|PubMed:23694781};\nOS   Cricetulus griseus (Chinese hamster) (Cricetulus barabensis griseus).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea;\nOC   Cricetidae; Cricetinae; Cricetulus.\nOX   NCBI_TaxID=10029;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=23694781; DOI=10.1093/jb/mvt045;\nRA   Hirata T., Fujita M., Kanzawa N., Murakami Y., Maeda Y., Kinoshita T.;\nRT   \"Glycosylphosphatidylinositol mannosyltransferase II is the rate-limiting\nRT   enzyme in glycosylphosphatidylinositol biosynthesis under limited dolichol-\nRT   phosphate mannose availability.\";\nRL   J. Biochem. 154:257-264(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "FT   TOPO_DOM        1..13\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9NUD9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 121-123",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        14..34\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-126",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H5",
  "excerpt": "FT   TOPO_DOM        35..77\nFT                   /note=\"Lumenal\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9NUD9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 127-129",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        78..98\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-132",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H7",
  "excerpt": "FT   TOPO_DOM        99..113\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9NUD9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 133-135",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        114..134\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 136-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H9",
  "excerpt": "FT   TOPO_DOM        135..136\nFT                   /note=\"Lumenal\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9NUD9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 139-141",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        137..157\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 142-144",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H11",
  "excerpt": "FT   TOPO_DOM        158..161\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9NUD9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 145-147",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        162..182\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 148-150",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H13",
  "excerpt": "FT   TOPO_DOM        183..192\nFT                   /note=\"Lumenal\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9NUD9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 151-153",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H14",
  "excerpt": "FT   TRANSMEM        193..213\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 154-156",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H15",
  "excerpt": "FT   TOPO_DOM        214..234\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9NUD9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 157-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H16",
  "excerpt": "FT   TRANSMEM        235..255\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-162",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H17

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H17",
  "excerpt": "FT   TOPO_DOM        256..327\nFT                   /note=\"Lumenal\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9NUD9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 163-165",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H18",
  "excerpt": "FT   TRANSMEM        328..348\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 166-168",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H19

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H19",
  "excerpt": "FT   TOPO_DOM        349..379\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9NUD9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 169-171",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H20",
  "excerpt": "FT   TRANSMEM        380..400\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 172-174",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H21

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H21",
  "excerpt": "FT   TOPO_DOM        401..470\nFT                   /note=\"Lumenal\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9NUD9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 175-177",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H22",
  "excerpt": "FT   TRANSMEM        471..491\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 178-180",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H23

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H23",
  "excerpt": "FT   TOPO_DOM        492..494\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9NUD9\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 181-183",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 33. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
