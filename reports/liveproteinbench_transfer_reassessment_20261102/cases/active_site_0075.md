# active_site_0075

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0075.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 254 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
METVESSSSAELLRAQTHFSRQVFSFQNFAALKCALQLGIPDAIKQHGKPMNLSELTSALPINPSKAPCIHRLMRLLVNAGYFAQENECFALTSLGRLLLKDDPLHIRALVLSEFHTALVMPWFALSEWFKNDDVAPFATAHGKSFWDYTSCDPELRNVFDGAMACDSHLIAKALVTEFKYLFEGLKSLVDVGGGNGTLARSIAKAFTNLKCTVCDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKSILHDWSDENCVKILKNCKRAISGKDKGGKVIVIDGVVELQKKAGNDDPGLDNMDMQMLVLFNSKERNEKEWAKLFSDAGFSDYGIVRTFGWWCIMELSP

[Multiple Choices]
A. Position 215 (1)
B. Position 2886 (For beta-ketoacyl synthase 2 activity)
C. Position 254 (Proton acceptor)
D. Position 116 (Charge relay)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies residue 254 as the active-site proton acceptor. This is computational support from a PROSITE rule, not direct experimental validation in the supplied evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a SAM-dependent methyltransferase, including a glycine-rich region around positions 191–200. In this enzyme-family context, a conserved catalytic histidine can act as the proton-accepting base; position 254 is histidine, matching option C. This family-level pattern distinguishes it from the other offered positions, including the out-of-range position 2886.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable methyltransferase-family inference meaningfully favors the histidine at position 254 as the proton acceptor; recalling this exact protein's database record is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the choices, only position 254 is supported as the proton-accepting catalytic residue by the family-level sequence inference.


### Important caveats

- The supplied annotation is computationally assigned by PROSITE; the excerpts do not establish direct experimental validation of residue 254.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a SAM-dependent methyltransferase, including a glycine-rich region around positions 191–200. In this enzyme-family context, a conserved catalytic histidine can act as the proton-accepting base; position 254 is histidine, matching option C. This family-level pattern distinguishes it from the other offered positions, including the out-of-range position 2886.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable methyltransferase-family inference meaningfully favors the histidine at position 254 as the proton acceptor; recalling this exact protein's database record is not necessary."
  },
  "case_id": "active_site_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 254 as the active-site proton acceptor. This is computational support from a PROSITE rule, not direct experimental validation in the supplied evidence."
  },
  "important_caveats": [
    "The supplied annotation is computationally assigned by PROSITE; the excerpts do not establish direct experimental validation of residue 254."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, only position 254 is supported as the proton-accepting catalytic residue by the family-level sequence inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies residue 254 as the active-site proton acceptor. This is computational support from a PROSITE rule, not direct experimental validation in the supplied evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a SAM-dependent methyltransferase, including a glycine-rich region around positions 191–200. In this enzyme-family context, a conserved catalytic histidine can act as the proton-accepting base; position 254 is histidine, matching option C. This family-level pattern distinguishes it from the other offered positions, including the out-of-range position 2886.",
    "missing_item_specific_fact": "",
    "reason": "A transferable methyltransferase-family inference meaningfully favors the histidine at position 254 as the proton acceptor; recalling this exact protein's database record is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, only position 254 is supported as the proton-accepting catalytic residue by the family-level sequence inference."
  },
  "important_caveats": [
    "The supplied annotation is computationally assigned by PROSITE; the excerpts do not establish direct experimental validation of residue 254."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (D3KY98) annotates position 254 as 'Active site' with description 'Proton acceptor' (evidence: ECO:0000255|PROSITE-ProRule:PRU01020). The sequence at position 254 is indeed His (H), and it is followed by Asp at 255 and Asp at 258, forming the H-D-D catalytic triad characteristic of type I plant O-methyltransferases. The protein was experimentally characterized as an O-methyltransferase (PubMed:20061395), confirming the family assignment. The annotation is computational (PROSITE-ProRule pattern matching to the type I plant OMT family) rather than a direct experimental measurement of H254's catalytic role in this specific protein, but the family-level catalytic mechanism is well-established. The expected answer C is supported by the database annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C11](#evidence-c11).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can distinguish the answer through family-level inference from other plant type I O-methyltransferases (e.g., COMT, CCoAOMT). Key steps: (1) The GGGNG motif at positions 193-197 is the canonical SAM-binding motif of methyltransferases, and the ~350 AA length is typical of plant type I OMTs, identifying the family. (2) Type I plant OMTs (COMT, etc.) use a His-Asp-Asp catalytic triad where His acts as a general base (proton acceptor) to deprotonate the substrate hydroxyl. (3) Scanning the sequence reveals H254-D255-D258, matching this triad exactly. (4) 'Proton acceptor' is the precise mechanistic role of the His in this triad. The distractors are eliminable: B (position 2886) exceeds the 350-residue sequence length; A (position 215, a Cys with vague label '(1)') does not match any known OMT catalytic mechanism; D (position 116, also a His, labeled 'Charge relay') is not part of an H-D-D triad and 'charge relay' describes serine-protease-type mechanisms, not OMT catalysis. This inference relies on transferable knowledge of the type I plant OMT family and its catalytic mechanism, not on recalling this specific protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The answer is reachable through recognized sequence motifs (GGGNG SAM-binding motif), family-level catalytic mechanism knowledge (His-Asp-Asp triad in type I plant OMTs), and elimination of obviously wrong choices (out-of-range position, wrong amino acid type, wrong mechanistic description). No target-specific annotation beyond family-level knowledge is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B is trivially wrong (position 2886 exceeds the 350-residue sequence). Option A (Cys at 215, label '(1)') has no mechanistic basis in OMT catalysis. Option D (His at 116, 'Charge relay') is not part of the H-D-D triad and the 'charge relay' description does not match OMT mechanism. Only C (His at 254, 'Proton acceptor') matches the well-established type I plant OMT catalytic triad and its mechanistic role.


### Important caveats

- The UniProt active-site annotation at position 254 is based on PROSITE-ProRule pattern matching (ECO:0000255), a computational/family-level annotation, not a direct experimental measurement of H254's proton-acceptor role in this specific protein. The protein's OMT function was experimentally confirmed (PubMed:20061395), but the specific residue assignment is by analogy to characterized family members like COMT.
- Option D's His at position 116 is also a histidine, which could cause momentary confusion, but it lacks the adjacent Asp-Asp partners and the 'charge relay' label is mechanistically inappropriate for OMT catalysis.
- The sequence-match confirms the benchmark sequence corresponds to UniProt D3KY98 (OMT1_CARIP, 350 AA), so the annotation coordinates are directly applicable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can distinguish the answer through family-level inference from other plant type I O-methyltransferases (e.g., COMT, CCoAOMT). Key steps: (1) The GGGNG motif at positions 193-197 is the canonical SAM-binding motif of methyltransferases, and the ~350 AA length is typical of plant type I OMTs, identifying the family. (2) Type I plant OMTs (COMT, etc.) use a His-Asp-Asp catalytic triad where His acts as a general base (proton acceptor) to deprotonate the substrate hydroxyl. (3) Scanning the sequence reveals H254-D255-D258, matching this triad exactly. (4) 'Proton acceptor' is the precise mechanistic role of the His in this triad. The distractors are eliminable: B (position 2886) exceeds the 350-residue sequence length; A (position 215, a Cys with vague label '(1)') does not match any known OMT catalytic mechanism; D (position 116, also a His, labeled 'Charge relay') is not part of an H-D-D triad and 'charge relay' describes serine-protease-type mechanisms, not OMT catalysis. This inference relies on transferable knowledge of the type I plant OMT family and its catalytic mechanism, not on recalling this specific protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The answer is reachable through recognized sequence motifs (GGGNG SAM-binding motif), family-level catalytic mechanism knowledge (His-Asp-Asp triad in type I plant OMTs), and elimination of obviously wrong choices (out-of-range position, wrong amino acid type, wrong mechanistic description). No target-specific annotation beyond family-level knowledge is required."
  },
  "case_id": "active_site_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C11"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (D3KY98) annotates position 254 as 'Active site' with description 'Proton acceptor' (evidence: ECO:0000255|PROSITE-ProRule:PRU01020). The sequence at position 254 is indeed His (H), and it is followed by Asp at 255 and Asp at 258, forming the H-D-D catalytic triad characteristic of type I plant O-methyltransferases. The protein was experimentally characterized as an O-methyltransferase (PubMed:20061395), confirming the family assignment. The annotation is computational (PROSITE-ProRule pattern matching to the type I plant OMT family) rather than a direct experimental measurement of H254's catalytic role in this specific protein, but the family-level catalytic mechanism is well-established. The expected answer C is supported by the database annotation."
  },
  "important_caveats": [
    "The UniProt active-site annotation at position 254 is based on PROSITE-ProRule pattern matching (ECO:0000255), a computational/family-level annotation, not a direct experimental measurement of H254's proton-acceptor role in this specific protein. The protein's OMT function was experimentally confirmed (PubMed:20061395), but the specific residue assignment is by analogy to characterized family members like COMT.",
    "Option D's His at position 116 is also a histidine, which could cause momentary confusion, but it lacks the adjacent Asp-Asp partners and the 'charge relay' label is mechanistically inappropriate for OMT catalysis.",
    "The sequence-match confirms the benchmark sequence corresponds to UniProt D3KY98 (OMT1_CARIP, 350 AA), so the annotation coordinates are directly applicable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is trivially wrong (position 2886 exceeds the 350-residue sequence). Option A (Cys at 215, label '(1)') has no mechanistic basis in OMT catalysis. Option D (His at 116, 'Charge relay') is not part of the H-D-D triad and the 'charge relay' description does not match OMT mechanism. Only C (His at 254, 'Proton acceptor') matches the well-established type I plant OMT catalytic triad and its mechanistic role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (D3KY98) annotates position 254 as 'Active site' with description 'Proton acceptor' (evidence: ECO:0000255|PROSITE-ProRule:PRU01020). The sequence at position 254 is indeed His (H), and it is followed by Asp at 255 and Asp at 258, forming the H-D-D catalytic triad characteristic of type I plant O-methyltransferases. The protein was experimentally characterized as an O-methyltransferase (PubMed:20061395), confirming the family assignment. The annotation is computational (PROSITE-ProRule pattern matching to the type I plant OMT family) rather than a direct experimental measurement of H254's catalytic role in this specific protein, but the family-level catalytic mechanism is well-established. The expected answer C is supported by the database annotation.",
    "evidence_ids": ["C5", "H3", "C11"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can distinguish the answer through family-level inference from other plant type I O-methyltransferases (e.g., COMT, CCoAOMT). Key steps: (1) The GGGNG motif at positions 193-197 is the canonical SAM-binding motif of methyltransferases, and the ~350 AA length is typical of plant type I OMTs, identifying the family. (2) Type I plant OMTs (COMT, etc.) use a His-Asp-Asp catalytic triad where His acts as a general base (proton acceptor) to deprotonate the substrate hydroxyl. (3) Scanning the sequence reveals H254-D255-D258, matching this triad exactly. (4) 'Proton acceptor' is the precise mechanistic role of the His in this triad. The distractors are eliminable: B (position 2886) exceeds the 350-residue sequence length; A (position 215, a Cys with vague label '(1)') does not match any known OMT catalytic mechanism; D (position 116, also a His, labeled 'Charge relay') is not part of an H-D-D triad and 'charge relay' describes serine-protease-type mechanisms, not OMT catalysis. This inference relies on transferable knowledge of the type I plant OMT family and its catalytic mechanism, not on recalling this specific protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "The answer is reachable through recognized sequence motifs (GGGNG SAM-binding motif), family-level catalytic mechanism knowledge (His-Asp-Asp triad in type I plant OMTs), and elimination of obviously wrong choices (out-of-range position, wrong amino acid type, wrong mechanistic description). No target-specific annotation beyond family-level knowledge is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B is trivially wrong (position 2886 exceeds the 350-residue sequence). Option A (Cys at 215, label '(1)') has no mechanistic basis in OMT catalysis. Option D (His at 116, 'Charge relay') is not part of the H-D-D triad and the 'charge relay' description does not match OMT mechanism. Only C (His at 254, 'Proton acceptor') matches the well-established type I plant OMT catalytic triad and its mechanistic role."
  },
  "important_caveats": [
    "The UniProt active-site annotation at position 254 is based on PROSITE-ProRule pattern matching (ECO:0000255), a computational/family-level annotation, not a direct experimental measurement of H254's proton-acceptor role in this specific protein. The protein's OMT function was experimentally confirmed (PubMed:20061395), but the specific residue assignment is by analogy to characterized family members like COMT.",
    "Option D's His at position 116 is also a histidine, which could cause momentary confusion, but it lacks the adjacent Asp-Asp partners and the 'charge relay' label is mechanistically inappropriate for OMT catalysis.",
    "The sequence-match confirms the benchmark sequence corresponds to UniProt D3KY98 (OMT1_CARIP, 350 AA), so the annotation coordinates are directly applicable."
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
  "benchmark_sequence_length": 350,
  "benchmark_sequence_sha256": "ab6b8f525c4405adcc9e2f43d65d1e3b7ba98c49c094274d62c7598adf3167f9",
  "current_entry_audit": {
    "entryVersion": 58,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2010-04-20",
    "sequenceVersion": 1
  },
  "current_record_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 350,
  "current_source_sequence_sha256": "ab6b8f525c4405adcc9e2f43d65d1e3b7ba98c49c094274d62c7598adf3167f9",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 56,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "D3KY98",
  "selected_historical_entry_version": 56,
  "selected_historical_record_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "selected_historical_source_sequence_length": 350,
  "selected_historical_source_sequence_sha256": "ab6b8f525c4405adcc9e2f43d65d1e3b7ba98c49c094274d62c7598adf3167f9",
  "selected_historical_version": {
    "accession": "D3KY98",
    "database": "Swiss-Prot",
    "entryVersion": 56,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "OMT1_CARIP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D3KY98\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":58,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2010-04-20\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ipecac\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Rubiaceae\",\"Rubioideae\",\"Palicoureeae\",\"Carapichea\"],\"scientificName\":\"Carapichea ipecacuanha\",\"synonyms\":[\"Callicocca ipecacuanha\"],\"taxonId\":77880}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.128\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"(R,S)-norcoclaurine 6-O-methyltransferase IpeOMT1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"Coclaurine synthase IpeOMT1\"}]},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"(R,S)-norprotosinomenine 6-O-methyltransferase IpeOMT1\"}},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"7-O-methyl-N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1\"}},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"Ipecac/benzylisoquinoline alkaloid O-methyltransferase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAI79243.1\",\"source\":\"EMBL\"}],\"value\":\"IpeOMT1\"}]},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"Isococlaurine 6-O-methyltransferase IpeOMT1\"}},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.396\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"Cephaeline 6'-O-methyltransferase IpeOMT1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20061395\",\"source\":\"PubMed\"}],\"value\":\"Emetine synthase IpeOMT1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":254},\"start\":{\"modifier\":\"EXACT\",\"value\":254}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":193},\"start\":{\"modifier\":\"EXACT\",\"value\":193}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":216},\"start\":{\"modifier\":\"EXACT\",\"value\":216}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":236},\"start\":{\"modifier\":\"EXACT\",\"value\":236}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":237},\"start\":{\"modifier\":\"EXACT\",\"value\":237}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":250},\"start\":{\"modifier\":\"EXACT\",\"value\":250}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Nomura T.\",\"Kutchan T.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20061395\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m109.086157\"}],\"citationType\":\"journal article\",\"firstPage\":\"7722\",\"id\":\"20061395\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"7738\",\"publicationDate\":\"2010\",\"title\":\"Three new O-methyltransferases are sufficient for all O-methylation reactions of ipecac alkaloid biosynthesis in root culture of Psychotria ipecacuanha.\",\"volume\":\"285\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAI79243.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Root\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"PATHWAY\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:02.422509+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb",
  "url": "https://rest.uniprot.org/uniprotkb/D3KY98.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H1",
  "excerpt": "ID   OMT1_CARIP              Reviewed;         350 AA.\nAC   D3KY98;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   20-APR-2010, sequence version 1.\nDT   28-JAN-2026, entry version 56.\nDE   RecName: Full=Cephaeline 6'-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            Short=Emetine synthase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.396 {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=(R,S)-norcoclaurine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            Short=Coclaurine synthase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.128 {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=(R,S)-norprotosinomenine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=7-O-methyl-N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=Ipecac/benzylisoquinoline alkaloid O-methyltransferase 1 {ECO:0000303|PubMed:20061395};\nDE            Short=IpeOMT1 {ECO:0000303|PubMed:20061395, ECO:0000312|EMBL:BAI79243.1};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=Isococlaurine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nDE   AltName: Full=N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};\nGN   Name=OMT1 {ECO:0000303|PubMed:20061395};\nOS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;\nOC   Carapichea.\nOX   NCBI_TaxID=77880;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAI79243.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR LOCATION, PATHWAY, AND TISSUE\nRP   SPECIFICITY.\nRC   TISSUE=Root;\nRX   PubMed=20061395; DOI=10.1074/jbc.m109.086157;\nRA   Nomura T., Kutchan T.M.;\nRT   \"Three new O-methyltransferases are sufficient for all O-methylation\nRT   reactions of ipecac alkaloid biosynthesis in root culture of Psychotria\nRT   ipecacuanha.\";\nRL   J. Biol. Chem. 285:7722-7738(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        254\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 173-175",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         193\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 176-179",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         216\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 180-183",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         236\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 184-187",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         237\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 188-191",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)

```json
{
  "entry_version": 56,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         250\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:56.372657+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 192-195",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb",
  "url": "https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 75. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
