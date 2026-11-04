# transmembrane_0023

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0023.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 41..64; 76..96; 108..126; 132..156; 176..195; 201..220; 241..260; 280..300; 312..330; 346..366; 416..437

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIEKSNNIYLSIDPIVERIKKNGEELPLINSEKKGIDYTQIVVYLVGLSDGLIHLASLAIYYLFKDHYRLTPYQVSLILMYPYLPFILKPIIALITDSISIFGMRRKPYLFLFSLFQSLNFLSLALVDLSLIQATLVLFFISLCASFCTTVAEALVVESSIGKTYSQGTNKVTEFIASKAVGSLSVAYFSGYFLEKVSREYIFMATSIFPLIISISCLFLKEKEYVTRKNIFKQMTDLIKFINTPVFIGPFLYIFVYMSGPDYDDAFFFFCTNKLGFRPSFMGTLRLTYGIASLIGIIVYRVFLKNSSLRNTLIFTTLVSFPIYISPIILTEKINKYFGISNELFVLSGGFLIEAITEIQLLPLFILTANICQEGLEASVFATILSVKNLGSLTKKGTSSLLTYLMKIDTYNFDNLSMYILTCGLFLLLSLSLVPLLPSEDQIESLKNKKIQK

[Multiple Choices]
A. 41..64; 108..126; 132..156; 176..195; 201..220; 241..260; 280..300; 312..330; 346..366; 416..437
B. 41..64; 76..96; 108..126; 132..156; 176..195; 201..220; 241..260; 284..304; 312..330; 346..366; 416..437
C. 41..64; 76..96; 108..126; 132..156; 176..195; 201..220; 241..260; 280..300; 312..330; 346..366; 416..437
D. 1..21; 31..51; 56..76; 77..97; 101..121; 128..148; 149..169; 182..202; 206..226; 321..341
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

> The sequence-matched UniProt record annotates the eleven spans listed in C. These are computational helical transmembrane annotations (ECO:0000255), not evidence of experimental determination, but they support the expected answer.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has repeated long hydrophobic stretches characteristic of membrane-spanning helices, including the strongly hydrophobic stretch around 76–96, which distinguishes C and B from A, and the unrelated intervals in D. Around the disputed later span, C's 280–300 interval is a somewhat better hydropathy-based placement than B's shifted 284–304 interval, whose ends include more polar/charged residues. This is a transferable sequence-pattern inference, not proof of exact boundaries.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multipass membrane pattern and most listed spans can be inferred from hydrophobic sequence features. The small boundary shift separating B and C is less certain from sequence alone, but a hydropathy-based preference for C is credible; exact residue boundaries remain approximate.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B and C share the same likely membrane-spanning core in the 280–304 region, with boundaries shifted by only four residues. Because the prompt asks for a segment that crosses the membrane rather than exact annotation boundaries, B's interval could also describe a crossing segment, even though C better matches the cited annotation.


### Important caveats

- The supporting database features are computational annotations and should not be presented as experimental measurements.
- Transmembrane segment boundaries are approximate; the sequence alone does not sharply resolve the small B/C boundary shift.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has repeated long hydrophobic stretches characteristic of membrane-spanning helices, including the strongly hydrophobic stretch around 76–96, which distinguishes C and B from A, and the unrelated intervals in D. Around the disputed later span, C's 280–300 interval is a somewhat better hydropathy-based placement than B's shifted 284–304 interval, whose ends include more polar/charged residues. This is a transferable sequence-pattern inference, not proof of exact boundaries.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multipass membrane pattern and most listed spans can be inferred from hydrophobic sequence features. The small boundary shift separating B and C is less certain from sequence alone, but a hydropathy-based preference for C is credible; exact residue boundaries remain approximate."
  },
  "case_id": "transmembrane_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "C15"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the eleven spans listed in C. These are computational helical transmembrane annotations (ECO:0000255), not evidence of experimental determination, but they support the expected answer."
  },
  "important_caveats": [
    "The supporting database features are computational annotations and should not be presented as experimental measurements.",
    "Transmembrane segment boundaries are approximate; the sequence alone does not sharply resolve the small B/C boundary shift."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B and C share the same likely membrane-spanning core in the 280–304 region, with boundaries shifted by only four residues. Because the prompt asks for a segment that crosses the membrane rather than exact annotation boundaries, B's interval could also describe a crossing segment, even though C better matches the cited annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the eleven spans listed in C. These are computational helical transmembrane annotations (ECO:0000255), not evidence of experimental determination, but they support the expected answer.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has repeated long hydrophobic stretches characteristic of membrane-spanning helices, including the strongly hydrophobic stretch around 76–96, which distinguishes C and B from A, and the unrelated intervals in D. Around the disputed later span, C's 280–300 interval is a somewhat better hydropathy-based placement than B's shifted 284–304 interval, whose ends include more polar/charged residues. This is a transferable sequence-pattern inference, not proof of exact boundaries.",
    "missing_item_specific_fact": "",
    "reason": "The multipass membrane pattern and most listed spans can be inferred from hydrophobic sequence features. The small boundary shift separating B and C is less certain from sequence alone, but a hydropathy-based preference for C is credible; exact residue boundaries remain approximate."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B and C share the same likely membrane-spanning core in the 280–304 region, with boundaries shifted by only four residues. Because the prompt asks for a segment that crosses the membrane rather than exact annotation boundaries, B's interval could also describe a crossing segment, even though C better matches the cited annotation."
  },
  "important_caveats": [
    "The supporting database features are computational annotations and should not be presented as experimental measurements.",
    "Transmembrane segment boundaries are approximate; the sequence alone does not sharply resolve the small B/C boundary shift."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence code ECO:0000255, 'inferred by similarity') lists exactly 11 transmembrane helical segments at 41..64, 76..96, 108..126, 132..156, 176..195, 201..220, 241..260, 280..300, 312..330, 346..366, and 416..437, which matches choice C exactly. The sequence match is confirmed (SHA-256 identical). Note that ECO:0000255 indicates computational prediction by similarity, not experimental validation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can eliminate D (positions like 1..21, 31..51 do not correspond to hydrophobic stretches in the sequence) and eliminate A (the region 76..96, encoding VSLILMYPYLPFILKPIIALI, is clearly hydrophobic and should be a TM segment). However, distinguishing B from C requires resolving a 4-residue shift in one TM boundary (280..300 vs 284..304). This is within the resolution noise of any hydrophobicity-based prediction algorithm. No general biological principle, family-level conserved feature, or structural argument reliably favors one 4-residue boundary over the other for this specific segment. The exact boundary is an artifact of the specific prediction tool used (ECO:0000255, by similarity).


**Missing item-specific fact**

> The exact start/end coordinates of the 8th transmembrane segment (280..300 vs 284..304) as output by the specific prediction algorithm used to annotate this protein. A 4-residue boundary shift in a hydrophobic helix cannot be resolved by general hydrophobicity principles or family-level knowledge.


**Reason**

> While choices A and D can be eliminated by hydrophobicity analysis and pattern recognition (transferable knowledge), the critical B-vs-C distinction hinges on a 4-residue boundary shift in one TM segment. This is at the precision limit of prediction algorithms and does not correspond to a meaningful biological distinction (e.g., a conserved motif, a charged residue marking the boundary, or a family-level structural constraint). Determining the 'correct' boundary requires knowing the specific annotation output for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The only difference between B and C is whether the 8th TM is annotated as 280..300 or 284..304. Both represent plausible boundaries for a hydrophobic helical segment of ~20 residues. Without running the exact prediction algorithm or knowing the specific annotation, a model cannot reliably distinguish these two options using general biological reasoning.


### Important caveats

- The UniProt annotation uses ECO:0000255 (inferred by similarity), meaning these are computational predictions, not experimentally determined boundaries.
- The 4-residue difference between B and C is within the typical uncertainty range of TM prediction tools (±3-5 residues).
- The sequence is from Plasmodium berghei (Vinckeia subgenus), a malaria parasite, and the protein is annotated as a putative folate transporter with 11 TM segments, consistent with MFS-family or similar multi-pass membrane transporters.
- The annotation evidence code and exact boundaries depend on the specific prediction pipeline used at the time of annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can eliminate D (positions like 1..21, 31..51 do not correspond to hydrophobic stretches in the sequence) and eliminate A (the region 76..96, encoding VSLILMYPYLPFILKPIIALI, is clearly hydrophobic and should be a TM segment). However, distinguishing B from C requires resolving a 4-residue shift in one TM boundary (280..300 vs 284..304). This is within the resolution noise of any hydrophobicity-based prediction algorithm. No general biological principle, family-level conserved feature, or structural argument reliably favors one 4-residue boundary over the other for this specific segment. The exact boundary is an artifact of the specific prediction tool used (ECO:0000255, by similarity).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact start/end coordinates of the 8th transmembrane segment (280..300 vs 284..304) as output by the specific prediction algorithm used to annotate this protein. A 4-residue boundary shift in a hydrophobic helix cannot be resolved by general hydrophobicity principles or family-level knowledge.",
    "reason": "While choices A and D can be eliminated by hydrophobicity analysis and pattern recognition (transferable knowledge), the critical B-vs-C distinction hinges on a 4-residue boundary shift in one TM segment. This is at the precision limit of prediction algorithms and does not correspond to a meaningful biological distinction (e.g., a conserved motif, a charged residue marking the boundary, or a family-level structural constraint). Determining the 'correct' boundary requires knowing the specific annotation output for this protein."
  },
  "case_id": "transmembrane_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "C15"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, 'inferred by similarity') lists exactly 11 transmembrane helical segments at 41..64, 76..96, 108..126, 132..156, 176..195, 201..220, 241..260, 280..300, 312..330, 346..366, and 416..437, which matches choice C exactly. The sequence match is confirmed (SHA-256 identical). Note that ECO:0000255 indicates computational prediction by similarity, not experimental validation."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000255 (inferred by similarity), meaning these are computational predictions, not experimentally determined boundaries.",
    "The 4-residue difference between B and C is within the typical uncertainty range of TM prediction tools (±3-5 residues).",
    "The sequence is from Plasmodium berghei (Vinckeia subgenus), a malaria parasite, and the protein is annotated as a putative folate transporter with 11 TM segments, consistent with MFS-family or similar multi-pass membrane transporters.",
    "The annotation evidence code and exact boundaries depend on the specific prediction pipeline used at the time of annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The only difference between B and C is whether the 8th TM is annotated as 280..300 or 284..304. Both represent plausible boundaries for a hydrophobic helical segment of ~20 residues. Without running the exact prediction algorithm or knowing the specific annotation, a model cannot reliably distinguish these two options using general biological reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, 'inferred by similarity') lists exactly 11 transmembrane helical segments at 41..64, 76..96, 108..126, 132..156, 176..195, 201..220, 241..260, 280..300, 312..330, 346..366, and 416..437, which matches choice C exactly. The sequence match is confirmed (SHA-256 identical). Note that ECO:0000255 indicates computational prediction by similarity, not experimental validation.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model can eliminate D (positions like 1..21, 31..51 do not correspond to hydrophobic stretches in the sequence) and eliminate A (the region 76..96, encoding VSLILMYPYLPFILKPIIALI, is clearly hydrophobic and should be a TM segment). However, distinguishing B from C requires resolving a 4-residue shift in one TM boundary (280..300 vs 284..304). This is within the resolution noise of any hydrophobicity-based prediction algorithm. No general biological principle, family-level conserved feature, or structural argument reliably favors one 4-residue boundary over the other for this specific segment. The exact boundary is an artifact of the specific prediction tool used (ECO:0000255, by similarity).",
    "missing_item_specific_fact": "The exact start/end coordinates of the 8th transmembrane segment (280..300 vs 284..304) as output by the specific prediction algorithm used to annotate this protein. A 4-residue boundary shift in a hydrophobic helix cannot be resolved by general hydrophobicity principles or family-level knowledge.",
    "reason": "While choices A and D can be eliminated by hydrophobicity analysis and pattern recognition (transferable knowledge), the critical B-vs-C distinction hinges on a 4-residue boundary shift in one TM segment. This is at the precision limit of prediction algorithms and does not correspond to a meaningful biological distinction (e.g., a conserved motif, a charged residue marking the boundary, or a family-level structural constraint). Determining the 'correct' boundary requires knowing the specific annotation output for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The only difference between B and C is whether the 8th TM is annotated as 280..300 or 284..304. Both represent plausible boundaries for a hydrophobic helical segment of ~20 residues. Without running the exact prediction algorithm or knowing the specific annotation, a model cannot reliably distinguish these two options using general biological reasoning."
  },
  "important_caveats": [
    "The UniProt annotation uses ECO:0000255 (inferred by similarity), meaning these are computational predictions, not experimentally determined boundaries.",
    "The 4-residue difference between B and C is within the typical uncertainty range of TM prediction tools (±3-5 residues).",
    "The sequence is from Plasmodium berghei (Vinckeia subgenus), a malaria parasite, and the protein is annotated as a putative folate transporter with 11 TM segments, consistent with MFS-family or similar multi-pass membrane transporters.",
    "The annotation evidence code and exact boundaries depend on the specific prediction pipeline used at the time of annotation."
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
  "benchmark_sequence_length": 453,
  "benchmark_sequence_sha256": "d184fbffe61ab6b5d535314bdc55c6bcf173c905437e47d12879217fb9e78f89",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-09-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 453,
  "current_source_sequence_sha256": "d184fbffe61ab6b5d535314bdc55c6bcf173c905437e47d12879217fb9e78f89",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 20,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A509AM18",
  "selected_historical_entry_version": 20,
  "selected_historical_record_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "selected_historical_source_sequence_length": 453,
  "selected_historical_source_sequence_sha256": "d184fbffe61ab6b5d535314bdc55c6bcf173c905437e47d12879217fb9e78f89",
  "selected_historical_version": {
    "accession": "A0A509AM18",
    "database": "Swiss-Prot",
    "entryVersion": 20,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "FT2_PLABA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A509AM18\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-09-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000074855\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Vinckeia\"],\"scientificName\":\"Plasmodium berghei (strain Anka)\",\"taxonId\":5823}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32975363\",\"source\":\"PubMed\"}],\"value\":\"Apicoplast-resident folate transporter\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Putative folate transporter 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32975363\",\"source\":\"PubMed\"}],\"value\":\"PbFT2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":64},\"start\":{\"modifier\":\"EXACT\",\"value\":41}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":96},\"start\":{\"modifier\":\"EXACT\",\"value\":76}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":126},\"start\":{\"modifier\":\"EXACT\",\"value\":108}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":156},\"start\":{\"modifier\":\"EXACT\",\"value\":132}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":195},\"start\":{\"modifier\":\"EXACT\",\"value\":176}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":220},\"start\":{\"modifier\":\"EXACT\",\"value\":201}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":260},\"start\":{\"modifier\":\"EXACT\",\"value\":241}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":300},\"start\":{\"modifier\":\"EXACT\",\"value\":280}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":330},\"start\":{\"modifier\":\"EXACT\",\"value\":312}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":366},\"start\":{\"modifier\":\"EXACT\",\"value\":346}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":437},\"start\":{\"modifier\":\"EXACT\",\"value\":416}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AM18.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"citation\":{\"authors\":[\"Korbmacher F.\",\"Drepper B.\",\"Sanderson T.\",\"Martin P.\",\"Stach T.\",\"Maier A.G.\",\"Matuschewski K.\",\"Matz J.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32975363\"},{\"database\":\"DOI\",\"id\":\"10.1111/cmi.13266\"}],\"citationType\":\"journal article\",\"firstPage\":\"e13266\",\"id\":\"32975363\",\"journal\":\"Cell. Microbiol.\",\"lastPage\":\"e13266\",\"publicationDate\":\"2021\",\"title\":\"An apicoplast-resident folate transporter is essential for sporogony of malaria parasites.\",\"volume\":\"23\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32975363\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"ANKA\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:24.632626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f983917de53c311063e3ec0dde4869d4a7e4fd767ac8b680a2f2cb01fe9b92e9",
  "url": "https://rest.uniprot.org/uniprotkb/A0A509AM18.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H1",
  "excerpt": "ID   FT2_PLABA               Reviewed;         453 AA.\nAC   A0A509AM18;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-SEP-2019, sequence version 1.\nDT   28-JAN-2026, entry version 20.\nDE   RecName: Full=Putative folate transporter 2 {ECO:0000305};\nDE            Short=PbFT2 {ECO:0000303|PubMed:32975363};\nDE   AltName: Full=Apicoplast-resident folate transporter {ECO:0000303|PubMed:32975363};\nGN   ORFNames=PBANKA_0931500 {ECO:0000312|EMBL:VUC55855.1};\nOS   Plasmodium berghei (strain Anka).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Vinckeia).\nOX   NCBI_TaxID=5823 {ECO:0000312|Proteomes:UP000074855};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:29.319637+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "url": "https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H2",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=ANKA {ECO:0000303|PubMed:32975363};\nRX   PubMed=32975363; DOI=10.1111/cmi.13266;\nRA   Korbmacher F., Drepper B., Sanderson T., Martin P., Stach T., Maier A.G.,\nRA   Matuschewski K., Matz J.M.;\nRT   \"An apicoplast-resident folate transporter is essential for sporogony of\nRT   malaria parasites.\";\nRL   Cell. Microbiol. 23:e13266-e13266(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:29.319637+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "url": "https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        41..64\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:29.319637+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "url": "https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H4",
  "excerpt": "FT   TRANSMEM        76..96\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:29.319637+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "url": "https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        108..126\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:29.319637+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-97",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "url": "https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H6",
  "excerpt": "FT   TRANSMEM        132..156\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:29.319637+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "url": "https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        176..195\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:29.319637+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "url": "https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H8",
  "excerpt": "FT   TRANSMEM        201..220\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:29.319637+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "url": "https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        241..260\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:29.319637+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "url": "https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H10",
  "excerpt": "FT   TRANSMEM        280..300\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:29.319637+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "url": "https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        312..330\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:29.319637+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-115",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "url": "https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H12",
  "excerpt": "FT   TRANSMEM        346..366\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:29.319637+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 116-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "url": "https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20)

```json
{
  "entry_version": 20,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        416..437\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:29.319637+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "52278aa5726b2473aad0488c2c3da3b14115e3dd0f2c2903d4b27b3d1cb87749",
  "url": "https://rest.uniprot.org/unisave/A0A509AM18?format=txt&versions=20"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 23. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
