# transmembrane_0013

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0013.txt)

**Task:** `transmembrane`  
**Expected answer:** **C** — 29..49; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEVSNMTTVTVFILLGLSNNPQVQALLFVLFLVIYLLTLLGNLLMVLVISTDSHLCTPMYFFLRQLSFLDAFYSSIIVPKLLENLLSKGETISFLECFTQISLVIFSGATEACLLSVMAYDRFQAMCHPLLYVVIINRRVCAGLVGASWAIGMGTGLINTLLLAQQHFCGPNVIHSFACELPPVLLLTCSDPCASIVSILTTMSVLGLGTLVLLLGSYSCIIMTALRINSATGRSKIFSTCSSHFLVVTIFYTSGVLRYMIPASGSALEQVLSVQYSVITPLLNPLIYSLKSQEVKVALRRMLARKSRLPL

[Multiple Choices]
A. 278..286; 308..323
B. 32..52; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290
C. 29..49; 66..86; 98..118; 141..163; 196..216; 237..257; 270..290
D. 29..49; 66..86; 98..118; 196..216; 237..257; 270..290
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

> The sequence-matched UniProt annotations list seven transmembrane helices, including 29..49 and the other regions in choice C. These annotations are computationally evidenced, not experimental confirmation.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has the characteristic pattern of a multi-pass, seven-helix membrane protein: long hydrophobic stretches recur at the regions listed in C, including a particularly hydrophobic stretch around 29..49. This distinguishes C from A, which does not give the set of membrane-spanning regions, and D, which omits a likely helix. C is also favored over B because B shifts the first segment toward more polar residues at its end.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of membrane-protein hydropathy and seven-helix architectures provides a credible basis for selecting C among these choices, although sequence-based inference does not establish exact helix boundaries with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B and C describe nearly the same strongly hydrophobic first helix, shifted by only three residues. C is better supported by the hydropathy pattern, but exact membrane-helix boundaries are approximate, so the sequence alone may not uniquely settle those endpoints.


### Important caveats

- The cited source annotations are computationally evidenced; they should not be represented as experimental measurements.
- The reviewer-only source identity and annotations were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has the characteristic pattern of a multi-pass, seven-helix membrane protein: long hydrophobic stretches recur at the regions listed in C, including a particularly hydrophobic stretch around 29..49. This distinguishes C from A, which does not give the set of membrane-spanning regions, and D, which omits a likely helix. C is also favored over B because B shifts the first segment toward more polar residues at its end.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of membrane-protein hydropathy and seven-helix architectures provides a credible basis for selecting C among these choices, although sequence-based inference does not establish exact helix boundaries with certainty."
  },
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotations list seven transmembrane helices, including 29..49 and the other regions in choice C. These annotations are computationally evidenced, not experimental confirmation."
  },
  "important_caveats": [
    "The cited source annotations are computationally evidenced; they should not be represented as experimental measurements.",
    "The reviewer-only source identity and annotations were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B and C describe nearly the same strongly hydrophobic first helix, shifted by only three residues. C is better supported by the hydropathy pattern, but exact membrane-helix boundaries are approximate, so the sequence alone may not uniquely settle those endpoints."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotations list seven transmembrane helices, including 29..49 and the other regions in choice C. These annotations are computationally evidenced, not experimental confirmation.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has the characteristic pattern of a multi-pass, seven-helix membrane protein: long hydrophobic stretches recur at the regions listed in C, including a particularly hydrophobic stretch around 29..49. This distinguishes C from A, which does not give the set of membrane-spanning regions, and D, which omits a likely helix. C is also favored over B because B shifts the first segment toward more polar residues at its end.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of membrane-protein hydropathy and seven-helix architectures provides a credible basis for selecting C among these choices, although sequence-based inference does not establish exact helix boundaries with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B and C describe nearly the same strongly hydrophobic first helix, shifted by only three residues. C is better supported by the hydropathy pattern, but exact membrane-helix boundaries are approximate, so the sequence alone may not uniquely settle those endpoints."
  },
  "important_caveats": [
    "The cited source annotations are computationally evidenced; they should not be represented as experimental measurements.",
    "The reviewer-only source identity and annotations were not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (A0A2R8YED5, Olfactory receptor 5BS1) lists exactly 7 transmembrane helices at positions 29..49, 66..86, 98..118, 141..163, 196..216, 237..257, and 270..290, matching option C precisely. The evidence code ECO:0000255 indicates inference by similarity (computational annotation), not experimental determination, but the annotation is consistent with the hydrophobicity profile of the sequence. The topological domain assignments (Extracellular 1-28, Cytoplasmic 50-65, Extracellular 87-97, etc.) are internally consistent with the 7TM topology.

Citations as saved: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9), [H11](#evidence-h11), [H13](#evidence-h13), [H15](#evidence-h15).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three transferable inference steps distinguish C from the alternatives: (1) The protein is 311 residues with multiple long hydrophobic stretches, consistent with a 7TM GPCR (olfactory receptor family). This eliminates A (only 2 segments of 9 and 16 residues—far too short to span a ~30 Å bilayer) and D (only 6 TM regions, missing the clearly hydrophobic 141-163 segment: CAGLVGASWAIGMGTGLINTLLL). (2) Between B and C, the first TM boundary differs: 32..52 vs 29..49. Positions 50-52 are S-T-D (polar), making 32-52 an unnatural TM terminus that includes polar residues in the helix. Positions 29-49 (VLFVLVIYLLTLLGNLLMVLVI) form a clean hydrophobic helix ending at Ile-49. (3) The N-terminal region (1-28) contains many polar residues (MEVSNMTTV, SNNPQVQ) typical of an extracellular domain in GPCRs, placing the TM1 start at ~29 rather than 32. These are standard hydrophobicity-based TM prediction arguments applicable to any membrane protein, not specific to this exact protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of GPCR 7TM topology, standard hydrophobicity windows (~20-25 hydrophobic residues for a TM helix), and the requirement that TM helices terminate at hydrophobic boundaries can eliminate A (too few/too short), D (missing a clearly hydrophobic TM4), and B (TM1 boundary includes polar STD at positions 50-52). The remaining choice C is selected by standard hydropathy analysis without needing to recall this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While the exact boundary between 29 and 32 for TM1 start could be debated by a few residues, option B's inclusion of polar S-T-D at positions 50-52 within the TM helix is a clear disqualifier under standard TM prediction criteria. Option D is eliminated by the GPCR 7TM requirement. Option A is eliminated by the absurdly short segments. Only C satisfies all constraints simultaneously.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundaries are computationally predicted, not experimentally determined.
- The exact TM1 start position (29 vs 32) is a matter of a few residues and could vary slightly among different prediction algorithms; however, the inclusion of polar residues in option B's boundary makes it clearly less appropriate.
- The protein identity (olfactory receptor) was not provided in the original input; the 7TM inference relies on recognizing the sequence as a GPCR-family protein from its hydrophobic pattern and length.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three transferable inference steps distinguish C from the alternatives: (1) The protein is 311 residues with multiple long hydrophobic stretches, consistent with a 7TM GPCR (olfactory receptor family). This eliminates A (only 2 segments of 9 and 16 residues—far too short to span a ~30 Å bilayer) and D (only 6 TM regions, missing the clearly hydrophobic 141-163 segment: CAGLVGASWAIGMGTGLINTLLL). (2) Between B and C, the first TM boundary differs: 32..52 vs 29..49. Positions 50-52 are S-T-D (polar), making 32-52 an unnatural TM terminus that includes polar residues in the helix. Positions 29-49 (VLFVLVIYLLTLLGNLLMVLVI) form a clean hydrophobic helix ending at Ile-49. (3) The N-terminal region (1-28) contains many polar residues (MEVSNMTTV, SNNPQVQ) typical of an extracellular domain in GPCRs, placing the TM1 start at ~29 rather than 32. These are standard hydrophobicity-based TM prediction arguments applicable to any membrane protein, not specific to this exact protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of GPCR 7TM topology, standard hydrophobicity windows (~20-25 hydrophobic residues for a TM helix), and the requirement that TM helices terminate at hydrophobic boundaries can eliminate A (too few/too short), D (missing a clearly hydrophobic TM4), and B (TM1 boundary includes polar STD at positions 50-52). The remaining choice C is selected by standard hydropathy analysis without needing to recall this specific protein's database annotation."
  },
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "H3",
      "H5",
      "H7",
      "H9",
      "H11",
      "H13",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A2R8YED5, Olfactory receptor 5BS1) lists exactly 7 transmembrane helices at positions 29..49, 66..86, 98..118, 141..163, 196..216, 237..257, and 270..290, matching option C precisely. The evidence code ECO:0000255 indicates inference by similarity (computational annotation), not experimental determination, but the annotation is consistent with the hydrophobicity profile of the sequence. The topological domain assignments (Extracellular 1-28, Cytoplasmic 50-65, Extracellular 87-97, etc.) are internally consistent with the 7TM topology."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundaries are computationally predicted, not experimentally determined.",
    "The exact TM1 start position (29 vs 32) is a matter of a few residues and could vary slightly among different prediction algorithms; however, the inclusion of polar residues in option B's boundary makes it clearly less appropriate.",
    "The protein identity (olfactory receptor) was not provided in the original input; the 7TM inference relies on recognizing the sequence as a GPCR-family protein from its hydrophobic pattern and length."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the exact boundary between 29 and 32 for TM1 start could be debated by a few residues, option B's inclusion of polar S-T-D at positions 50-52 within the TM helix is a clear disqualifier under standard TM prediction criteria. Option D is eliminated by the GPCR 7TM requirement. Option A is eliminated by the absurdly short segments. Only C satisfies all constraints simultaneously."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0013",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (A0A2R8YED5, Olfactory receptor 5BS1) lists exactly 7 transmembrane helices at positions 29..49, 66..86, 98..118, 141..163, 196..216, 237..257, and 270..290, matching option C precisely. The evidence code ECO:0000255 indicates inference by similarity (computational annotation), not experimental determination, but the annotation is consistent with the hydrophobicity profile of the sequence. The topological domain assignments (Extracellular 1-28, Cytoplasmic 50-65, Extracellular 87-97, etc.) are internally consistent with the 7TM topology.",
    "evidence_ids": ["C6", "C8", "C10", "C12", "C14", "C16", "C18", "H3", "H5", "H7", "H9", "H11", "H13", "H15"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three transferable inference steps distinguish C from the alternatives: (1) The protein is 311 residues with multiple long hydrophobic stretches, consistent with a 7TM GPCR (olfactory receptor family). This eliminates A (only 2 segments of 9 and 16 residues—far too short to span a ~30 Å bilayer) and D (only 6 TM regions, missing the clearly hydrophobic 141-163 segment: CAGLVGASWAIGMGTGLINTLLL). (2) Between B and C, the first TM boundary differs: 32..52 vs 29..49. Positions 50-52 are S-T-D (polar), making 32-52 an unnatural TM terminus that includes polar residues in the helix. Positions 29-49 (VLFVLVIYLLTLLGNLLMVLVI) form a clean hydrophobic helix ending at Ile-49. (3) The N-terminal region (1-28) contains many polar residues (MEVSNMTTV, SNNPQVQ) typical of an extracellular domain in GPCRs, placing the TM1 start at ~29 rather than 32. These are standard hydrophobicity-based TM prediction arguments applicable to any membrane protein, not specific to this exact protein.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of GPCR 7TM topology, standard hydrophobicity windows (~20-25 hydrophobic residues for a TM helix), and the requirement that TM helices terminate at hydrophobic boundaries can eliminate A (too few/too short), D (missing a clearly hydrophobic TM4), and B (TM1 boundary includes polar STD at positions 50-52). The remaining choice C is selected by standard hydropathy analysis without needing to recall this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While the exact boundary between 29 and 32 for TM1 start could be debated by a few residues, option B's inclusion of polar S-T-D at positions 50-52 within the TM helix is a clear disqualifier under standard TM prediction criteria. Option D is eliminated by the GPCR 7TM requirement. Option A is eliminated by the absurdly short segments. Only C satisfies all constraints simultaneously."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000255 (inferred by similarity), meaning the TM boundaries are computationally predicted, not experimentally determined.",
    "The exact TM1 start position (29 vs 32) is a matter of a few residues and could vary slightly among different prediction algorithms; however, the inclusion of polar residues in option B's boundary makes it clearly less appropriate.",
    "The protein identity (olfactory receptor) was not provided in the original input; the 7TM inference relies on recognizing the sequence as a GPCR-family protein from its hydrophobic pattern and length."
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
  "benchmark_sequence_length": 311,
  "benchmark_sequence_sha256": "ff6310a4b4f4740c74bc69549e735efa3d99058c3339ad175a562e376a5b2703",
  "current_entry_audit": {
    "entryVersion": 30,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-06-20",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 311,
  "current_source_sequence_sha256": "ff6310a4b4f4740c74bc69549e735efa3d99058c3339ad175a562e376a5b2703",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 28,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2R8YED5",
  "selected_historical_entry_version": 28,
  "selected_historical_record_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "selected_historical_source_sequence_length": 311,
  "selected_historical_source_sequence_sha256": "ff6310a4b4f4740c74bc69549e735efa3d99058c3339ad175a562e376a5b2703",
  "selected_historical_version": {
    "accession": "A0A2R8YED5",
    "database": "Swiss-Prot",
    "entryVersion": 28,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "O5BS1_HUMAN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2R8YED5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":30,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-06-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Human\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Primates\",\"Haplorrhini\",\"Catarrhini\",\"Hominidae\",\"Homo\"],\"scientificName\":\"Homo sapiens\",\"taxonId\":9606}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"HGNC:19627\",\"source\":\"HGNC\"}],\"value\":\"Olfactory receptor family 5 subfamily BS member 1\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Olfactory receptor 5BS1\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":28},\"start\":{\"modifier\":\"EXACT\",\"value\":1}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Helical; Name=1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":49},\"start\":{\"modifier\":\"EXACT\",\"value\":29}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":65},\"start\":{\"modifier\":\"EXACT\",\"value\":50}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"Helical; Name=2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":86},\"start\":{\"modifier\":\"EXACT\",\"value\":66}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":97},\"start\":{\"modifier\":\"EXACT\",\"value\":87}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"Helical; Name=3\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":118},\"start\":{\"modifier\":\"EXACT\",\"value\":98}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":140},\"start\":{\"modifier\":\"EXACT\",\"value\":119}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"Helical; Name=4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":163},\"start\":{\"modifier\":\"EXACT\",\"value\":141}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":195},\"start\":{\"modifier\":\"EXACT\",\"value\":164}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"Helical; Name=5\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":216},\"start\":{\"modifier\":\"EXACT\",\"value\":196}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":236},\"start\":{\"modifier\":\"EXACT\",\"value\":217}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"Helical; Name=6\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":257},\"start\":{\"modifier\":\"EXACT\",\"value\":237}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"Extracellular\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":269},\"start\":{\"modifier\":\"EXACT\",\"value\":258}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"Helical; Name=7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":290},\"start\":{\"modifier\":\"EXACT\",\"value\":270}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence C19

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json)

```json
{
  "evidence_id": "C19",
  "excerpt": "{\"description\":\"Cytoplasmic\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":311},\"start\":{\"modifier\":\"EXACT\",\"value\":291}},\"type\":\"Topological domain\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-01T06:24:45.255114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d0a68a9d870084d5a8a25b212bcab1f8fc22e1d9dc23ed81cdab2f3f4f4889f2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2R8YED5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H1",
  "excerpt": "ID   O5BS1_HUMAN             Reviewed;         311 AA.\nAC   A0A2R8YED5; Q8NH44;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-JUN-2018, sequence version 1.\nDT   28-JAN-2026, entry version 28.\nDE   RecName: Full=Olfactory receptor 5BS1 {ECO:0000305};\nDE   AltName: Full=Olfactory receptor family 5 subfamily BS member 1 {ECO:0000312|HGNC:HGNC:19627};\nGN   Name=OR5BS1 {ECO:0000312|HGNC:HGNC:19627};\nGN   Synonyms=OR5BS1P {ECO:0000312|HGNC:HGNC:19627};\nOS   Homo sapiens (Human).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Primates; Haplorrhini; Catarrhini; Hominidae;\nOC   Homo.\nOX   NCBI_TaxID=9606;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H2",
  "excerpt": "FT   TOPO_DOM        1..28\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 135-137",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        29..49\nFT                   /note=\"Helical; Name=1\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 138-140",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H4",
  "excerpt": "FT   TOPO_DOM        50..65\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 141-143",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H5",
  "excerpt": "FT   TRANSMEM        66..86\nFT                   /note=\"Helical; Name=2\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 144-146",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H6",
  "excerpt": "FT   TOPO_DOM        87..97\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 147-149",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H7",
  "excerpt": "FT   TRANSMEM        98..118\nFT                   /note=\"Helical; Name=3\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 150-152",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H8",
  "excerpt": "FT   TOPO_DOM        119..140\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-155",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H9",
  "excerpt": "FT   TRANSMEM        141..163\nFT                   /note=\"Helical; Name=4\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 156-158",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H10",
  "excerpt": "FT   TOPO_DOM        164..195\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 159-161",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H11",
  "excerpt": "FT   TRANSMEM        196..216\nFT                   /note=\"Helical; Name=5\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 162-164",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H12",
  "excerpt": "FT   TOPO_DOM        217..236\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 165-167",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H13",
  "excerpt": "FT   TRANSMEM        237..257\nFT                   /note=\"Helical; Name=6\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 168-170",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H14",
  "excerpt": "FT   TOPO_DOM        258..269\nFT                   /note=\"Extracellular\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 171-173",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H15",
  "excerpt": "FT   TRANSMEM        270..290\nFT                   /note=\"Helical; Name=7\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 174-176",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28)

```json
{
  "entry_version": 28,
  "evidence_id": "H16",
  "excerpt": "FT   TOPO_DOM        291..311\nFT                   /note=\"Cytoplasmic\"\nFT                   /evidence=\"ECO:0000305\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:26.314292+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 177-179",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cca1844e232709cdf49594e55779c1f7550585001e53d4c1927ed8cbc4f14327",
  "url": "https://rest.uniprot.org/unisave/A0A2R8YED5?format=txt&versions=28"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 13. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
