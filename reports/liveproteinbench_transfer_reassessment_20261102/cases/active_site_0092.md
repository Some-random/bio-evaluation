# active_site_0092

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0092.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 154 (Proton donor/acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSGVTTVEYRGRVAVITICNERKLNALDLHGYYELSERMREVATHDEVYVTLLTAKGRFFSAGADVSTIRDPPTTGEDDSGIADGGRRQWLQSFVAFNLNITQAFYSHPKILVVGLNGPVVGLSAALVSFADFIYATPSTFLLTPFSSLGLVAEGGASRALVQRLGVSKANEALLMSRRVPADELLQTGFVNKVFTELKGAKDDDVRFKELVLAEIDDKLGDHLVGDSLIGIKELIRRPEIDVLEGQNAREVFAGLGRFMSGVPQREFLKLASGEKRHKL

[Multiple Choices]
A. Position 154 (Proton donor/acceptor)
B. Position 6761 (Proton donor; for dehydratase activity)
C. Position 959 (Proton acceptor; for dehydratase activity)
D. Position 340 (For beta-ketoacyl synthase activity)
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

> The matched-sequence UniProt annotation identifies position 154 as the proton donor/acceptor active site. Its evidence code indicates transfer by similarity, so this supports the key as a computational annotation, not as independently established experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence is 280 residues long. Options B, C, and D give positions 6761, 959, and 340, all outside the sequence; A is the only offered position that can refer to a residue in this protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The choices are distinguishable from the original input by sequence length alone. This does not independently establish that position 154 has the stated catalytic role, but no fact specific to this protein is needed to select among these alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A gives a position within the supplied sequence.


### Important caveats

- The active-site annotation is similarity-transferred rather than shown here to be experimentally validated.
- The out-of-range distractor positions make the answer identifiable without substantive active-site prediction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence is 280 residues long. Options B, C, and D give positions 6761, 959, and 340, all outside the sequence; A is the only offered position that can refer to a residue in this protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The choices are distinguishable from the original input by sequence length alone. This does not independently establish that position 154 has the stated catalytic role, but no fact specific to this protein is needed to select among these alternatives."
  },
  "case_id": "active_site_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies position 154 as the proton donor/acceptor active site. Its evidence code indicates transfer by similarity, so this supports the key as a computational annotation, not as independently established experimental evidence."
  },
  "important_caveats": [
    "The active-site annotation is similarity-transferred rather than shown here to be experimentally validated.",
    "The out-of-range distractor positions make the answer identifiable without substantive active-site prediction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A gives a position within the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies position 154 as the proton donor/acceptor active site. Its evidence code indicates transfer by similarity, so this supports the key as a computational annotation, not as independently established experimental evidence.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence is 280 residues long. Options B, C, and D give positions 6761, 959, and 340, all outside the sequence; A is the only offered position that can refer to a residue in this protein.",
    "missing_item_specific_fact": "",
    "reason": "The choices are distinguishable from the original input by sequence length alone. This does not independently establish that position 154 has the stated catalytic role, but no fact specific to this protein is needed to select among these alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A gives a position within the supplied sequence."
  },
  "important_caveats": [
    "The active-site annotation is similarity-transferred rather than shown here to be experimentally validated.",
    "The out-of-range distractor positions make the answer identifiable without substantive active-site prediction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G4NCP4 (DCI1_PYRO7, 280 residues) explicitly annotates position 154 as 'Proton donor/acceptor' active site (evidence ECO:0000250|UniProtKB:Q05871, transferred by similarity). This matches option A exactly. The residue at position 154 is Glu (E), consistent with a proton donor/acceptor role in a dienoyl-CoA isomerase. The annotation is computational (by similarity to yeast DCI1, Q05871), not experimentally validated for this specific protein, but it is the recorded annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The provided protein sequence is 280 amino acids long. Options B (position 6761), C (position 959), and D (position 340) all reference residue positions far exceeding the sequence length, making them physically impossible for this protein. Only option A (position 154) falls within the valid range of 1–280. A model can eliminate B, C, and D purely by checking that the cited positions exceed the sequence length, without any prior knowledge of this specific protein's active site. Additionally, position 154 corresponds to a Glutamate (E) in the sequence, which is chemically plausible as a proton donor/acceptor in an isomerase mechanism (EC 5.3.3.21), further supporting A over the nonsensical alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question is answerable by simple arithmetic elimination: three of four options cite positions (6761, 959, 340) that are impossible for a 280-residue protein. This requires only counting/estimating sequence length from the original input. No specific knowledge of this protein's active site is needed. The remaining option (A, position 154) is within range and the residue (Glu) is chemically consistent with a proton donor/acceptor role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A references a position within the 280-residue sequence. Options B, C, and D are unambiguously impossible. There is no ambiguity in selecting A.


### Important caveats

- The question is trivially easy: the distractors are eliminated by a simple sequence-length check, requiring no biological reasoning about active sites, enzyme families, or catalytic mechanisms.
- The UniProt annotation for position 154 is transferred by similarity (ECO:0000250 from Q05871, yeast DCI1), not experimentally determined for this specific fungal protein.
- The distractors appear to be drawn from entirely different proteins (e.g., beta-ketoacyl synthase activity, dehydratase activity), making them irrelevant to any isomerase.
- The reviewer-only accession G4NCP4 and organism identity were not available to the evaluated model; the answer was determinable from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The provided protein sequence is 280 amino acids long. Options B (position 6761), C (position 959), and D (position 340) all reference residue positions far exceeding the sequence length, making them physically impossible for this protein. Only option A (position 154) falls within the valid range of 1–280. A model can eliminate B, C, and D purely by checking that the cited positions exceed the sequence length, without any prior knowledge of this specific protein's active site. Additionally, position 154 corresponds to a Glutamate (E) in the sequence, which is chemically plausible as a proton donor/acceptor in an isomerase mechanism (EC 5.3.3.21), further supporting A over the nonsensical alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable by simple arithmetic elimination: three of four options cite positions (6761, 959, 340) that are impossible for a 280-residue protein. This requires only counting/estimating sequence length from the original input. No specific knowledge of this protein's active site is needed. The remaining option (A, position 154) is within range and the residue (Glu) is chemically consistent with a proton donor/acceptor role."
  },
  "case_id": "active_site_0092",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G4NCP4 (DCI1_PYRO7, 280 residues) explicitly annotates position 154 as 'Proton donor/acceptor' active site (evidence ECO:0000250|UniProtKB:Q05871, transferred by similarity). This matches option A exactly. The residue at position 154 is Glu (E), consistent with a proton donor/acceptor role in a dienoyl-CoA isomerase. The annotation is computational (by similarity to yeast DCI1, Q05871), not experimentally validated for this specific protein, but it is the recorded annotation."
  },
  "important_caveats": [
    "The question is trivially easy: the distractors are eliminated by a simple sequence-length check, requiring no biological reasoning about active sites, enzyme families, or catalytic mechanisms.",
    "The UniProt annotation for position 154 is transferred by similarity (ECO:0000250 from Q05871, yeast DCI1), not experimentally determined for this specific fungal protein.",
    "The distractors appear to be drawn from entirely different proteins (e.g., beta-ketoacyl synthase activity, dehydratase activity), making them irrelevant to any isomerase.",
    "The reviewer-only accession G4NCP4 and organism identity were not available to the evaluated model; the answer was determinable from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A references a position within the 280-residue sequence. Options B, C, and D are unambiguously impossible. There is no ambiguity in selecting A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0092",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G4NCP4 (DCI1_PYRO7, 280 residues) explicitly annotates position 154 as 'Proton donor/acceptor' active site (evidence ECO:0000250|UniProtKB:Q05871, transferred by similarity). This matches option A exactly. The residue at position 154 is Glu (E), consistent with a proton donor/acceptor role in a dienoyl-CoA isomerase. The annotation is computational (by similarity to yeast DCI1, Q05871), not experimentally validated for this specific protein, but it is the recorded annotation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The provided protein sequence is 280 amino acids long. Options B (position 6761), C (position 959), and D (position 340) all reference residue positions far exceeding the sequence length, making them physically impossible for this protein. Only option A (position 154) falls within the valid range of 1–280. A model can eliminate B, C, and D purely by checking that the cited positions exceed the sequence length, without any prior knowledge of this specific protein's active site. Additionally, position 154 corresponds to a Glutamate (E) in the sequence, which is chemically plausible as a proton donor/acceptor in an isomerase mechanism (EC 5.3.3.21), further supporting A over the nonsensical alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable by simple arithmetic elimination: three of four options cite positions (6761, 959, 340) that are impossible for a 280-residue protein. This requires only counting/estimating sequence length from the original input. No specific knowledge of this protein's active site is needed. The remaining option (A, position 154) is within range and the residue (Glu) is chemically consistent with a proton donor/acceptor role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A references a position within the 280-residue sequence. Options B, C, and D are unambiguously impossible. There is no ambiguity in selecting A."
  },
  "important_caveats": [
    "The question is trivially easy: the distractors are eliminated by a simple sequence-length check, requiring no biological reasoning about active sites, enzyme families, or catalytic mechanisms.",
    "The UniProt annotation for position 154 is transferred by similarity (ECO:0000250 from Q05871, yeast DCI1), not experimentally determined for this specific fungal protein.",
    "The distractors appear to be drawn from entirely different proteins (e.g., beta-ketoacyl synthase activity, dehydratase activity), making them irrelevant to any isomerase.",
    "The reviewer-only accession G4NCP4 and organism identity were not available to the evaluated model; the answer was determinable from the sequence alone."
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
  "benchmark_sequence_length": 280,
  "benchmark_sequence_sha256": "81fa542cb1b4c3a9e1fd804427dce8d4e5449793e000d48268cf7974ef114ef0",
  "current_entry_audit": {
    "entryVersion": 51,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-12-14",
    "sequenceVersion": 1
  },
  "current_record_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 280,
  "current_source_sequence_sha256": "81fa542cb1b4c3a9e1fd804427dce8d4e5449793e000d48268cf7974ef114ef0",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 50,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G4NCP4",
  "selected_historical_entry_version": 50,
  "selected_historical_record_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "selected_historical_source_sequence_length": 280,
  "selected_historical_source_sequence_sha256": "81fa542cb1b4c3a9e1fd804427dce8d4e5449793e000d48268cf7974ef114ef0",
  "selected_historical_version": {
    "accession": "G4NCP4",
    "database": "Swiss-Prot",
    "entryVersion": 50,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "DCI1_PYRO7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G4NCP4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":51,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-12-14\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rice blast fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Sordariomycetidae\",\"Magnaporthales\",\"Pyriculariaceae\",\"Pyricularia\"],\"scientificName\":\"Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958)\",\"synonyms\":[\"Magnaporthe oryzae\"],\"taxonId\":242507}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q08558\",\"source\":\"UniProtKB\"}],\"value\":\"Peroxisomal di-isomerase DCI1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"36774535\",\"source\":\"PubMed\"}],\"value\":\"5.3.3.21\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36774535\",\"source\":\"PubMed\"}],\"value\":\"Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton donor/acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q05871\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":154},\"start\":{\"modifier\":\"EXACT\",\"value\":154}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4NCP4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang T.\",\"Wang X.\",\"Li X.\",\"Li Y.N.\",\"Li Y.\",\"Wu S.\",\"Xu L.\",\"Zhou R.\",\"Yang J.\",\"Li G.\",\"Liu X.\",\"Zheng X.\",\"Zhang Z.\",\"Zhang H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36774535\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.xplc.2023.100561\"}],\"citationType\":\"journal article\",\"firstPage\":\"100561\",\"id\":\"36774535\",\"journal\":\"Plant Commun.\",\"lastPage\":\"100561\",\"publicationDate\":\"2023\",\"title\":\"MoLrp1-mediated signaling induces nuclear accumulation of MoMsn2 to facilitate fatty acid oxidation for infectious growth of the rice blast fungus.\",\"volume\":\"4\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:09.351845+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "18e48cf8abf1a98581d94e658f5c733af10a67b9ab523abb9b4c1242569dd85d",
  "url": "https://rest.uniprot.org/uniprotkb/G4NCP4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H1",
  "excerpt": "ID   DCI1_PYRO7              Reviewed;         280 AA.\nAC   G4NCP4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   14-DEC-2011, sequence version 1.\nDT   28-JAN-2026, entry version 50.\nDE   RecName: Full=Delta(3,5)-Delta(2,4)-dienoyl-CoA isomerase {ECO:0000303|PubMed:36774535};\nDE            EC=5.3.3.21 {ECO:0000305|PubMed:36774535};\nDE   AltName: Full=Peroxisomal di-isomerase DCI1 {ECO:0000250|UniProtKB:Q08558};\nGN   Name=DCI1 {ECO:0000303|PubMed:36774535}; ORFNames=MGG_00359;\nOS   Pyricularia oryzae (strain 70-15 / ATCC MYA-4617 / FGSC 8958) (Rice blast\nOS   fungus) (Magnaporthe oryzae).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Sordariomycetidae; Magnaporthales; Pyriculariaceae; Pyricularia.\nOX   NCBI_TaxID=242507;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.213875+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "url": "https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, INDUCTION, DISRUPTION PHENOTYPE, AND SUBCELLULAR LOCATION.\nRX   PubMed=36774535; DOI=10.1016/j.xplc.2023.100561;\nRA   Zhang T., Wang X., Li X., Li Y.N., Li Y., Wu S., Xu L., Zhou R., Yang J.,\nRA   Li G., Liu X., Zheng X., Zhang Z., Zhang H.;\nRT   \"MoLrp1-mediated signaling induces nuclear accumulation of MoMsn2 to\nRT   facilitate fatty acid oxidation for infectious growth of the rice blast\nRT   fungus.\";\nRL   Plant Commun. 4:100561-100561(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.213875+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "url": "https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50)

```json
{
  "entry_version": 50,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        154\nFT                   /note=\"Proton donor/acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q05871\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:06.213875+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "b3af8253bb3b622f3d6088c53ac0e4fee82efbfd91d58cde994f260c9162d6d7",
  "url": "https://rest.uniprot.org/unisave/G4NCP4?format=txt&versions=50"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 92. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
