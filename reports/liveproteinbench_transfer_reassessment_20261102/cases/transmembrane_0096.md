# transmembrane_0096

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0096.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 510..528

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTFNGRFRATLRGINIRNASMTSLSLTGSHAQKQTVLGSTPGALGTIPTVALNGVNPLPRYRHNLLFGTLSFGDRWDRIQRRLAVLGRASTGNVVVPFSDSADAFRRMWESVDSASDSVLWQTYICKDDFVGQKTVKKLEEAHRRGCKTELLYDCGGNITGRRRLVGDLKKSGANVIEHRPMWEHFFPYFLRGMKWELSPGIRNHRKILIVDNKLGFCGGLNIGDEYCGTSEGGNGRFRDTHCVVMGPAVMHMREVYEDTKAPKPWKWSLARWRQIASATMNLRYLEGMNVKHDYLEPTTTFVRQGGGVYLRRQMERAERSTVRMMERMRWKRQRERLNRCLLTLAKNLREGQGLVFKAATGKGDDVATTDAGSKRNNEVSHGQWKLMKRRIDEYRQRAIKNAEESFFRRLRVVNPSMRLLEDTSPVAEAEAYGQAHAAVTQVLSCNPHSRDWSIPYAFWQVSKFVHQRLWVTTPYYMPHRKLMRALQLAARRGVDVRILAGSNRTTDPWFMWYASNYITGMLMASGVRVYEYKGGQVMHAKTVVADSIWTSIGSYNWDMMSNKNMEICVCHLDHNLALTMEKQFLDDMNVSEEVNYEEYQRRSLWLRFSSWFFYTALRIAEKFTFRTFWDPDLSSEID

[Multiple Choices]
A. 514..533
B. 1250..1269
C. 510..528; 680..699
D. 510..528
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

> The sequence-matched historical UniProt record annotates residues 510–528 as a helical transmembrane region. Its ECO:0000255 evidence indicates a computational annotation, not direct experimental confirmation.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence hydropathy can point to the putative membrane helix and distinguish its location from the out-of-range alternatives, but options A and D overlap substantially and describe the same candidate helix.


**Missing item-specific fact**

> The exact annotated boundary of the transmembrane segment—whether it is 510–528 rather than 514–533—is not established by the original input.


**Reason**

> Transferable sequence-based reasoning supports a membrane-spanning region in this vicinity, but does not meaningfully resolve the precise boundaries between A and D. Selecting the keyed interval requires the target-specific boundary annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both intervals overlap most of the same putative helix, and the task asks for a segment that crosses the membrane rather than a database's exact annotated boundaries. The supplied sequence does not clearly rule out the shifted interval.


### Important caveats

- The reviewer-only annotation supports D but is computational and does not establish experimental membrane topology.
- Choice B is outside the supplied sequence length; choice C includes an out-of-range segment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence hydropathy can point to the putative membrane helix and distinguish its location from the out-of-range alternatives, but options A and D overlap substantially and describe the same candidate helix.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated boundary of the transmembrane segment—whether it is 510–528 rather than 514–533—is not established by the original input.",
    "reason": "Transferable sequence-based reasoning supports a membrane-spanning region in this vicinity, but does not meaningfully resolve the precise boundaries between A and D. Selecting the keyed interval requires the target-specific boundary annotation."
  },
  "case_id": "transmembrane_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates residues 510–528 as a helical transmembrane region. Its ECO:0000255 evidence indicates a computational annotation, not direct experimental confirmation."
  },
  "important_caveats": [
    "The reviewer-only annotation supports D but is computational and does not establish experimental membrane topology.",
    "Choice B is outside the supplied sequence length; choice C includes an out-of-range segment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both intervals overlap most of the same putative helix, and the task asks for a segment that crosses the membrane rather than a database's exact annotated boundaries. The supplied sequence does not clearly rule out the shifted interval."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates residues 510–528 as a helical transmembrane region. Its ECO:0000255 evidence indicates a computational annotation, not direct experimental confirmation.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence hydropathy can point to the putative membrane helix and distinguish its location from the out-of-range alternatives, but options A and D overlap substantially and describe the same candidate helix.",
    "missing_item_specific_fact": "The exact annotated boundary of the transmembrane segment—whether it is 510–528 rather than 514–533—is not established by the original input.",
    "reason": "Transferable sequence-based reasoning supports a membrane-spanning region in this vicinity, but does not meaningfully resolve the precise boundaries between A and D. Selecting the keyed interval requires the target-specific boundary annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both intervals overlap most of the same putative helix, and the task asks for a segment that crosses the membrane rather than a database's exact annotated boundaries. The supplied sequence does not clearly rule out the shifted interval."
  },
  "important_caveats": [
    "The reviewer-only annotation supports D but is computational and does not establish experimental membrane topology.",
    "Choice B is outside the supplied sequence length; choice C includes an out-of-range segment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for Q584D1 (Trypanosoma brucei cardiolipin synthetase, 639 AA) annotates a single transmembrane helical region at 510..528 (evidence C5, H3). The evidence code is ECO:0000255 (inferred by similarity), indicating a computational prediction rather than direct experimental determination, but the annotation directly matches the expected answer D. The sequence length of 639 AA confirms that options B (1250..1269) and C (680..699) reference positions beyond the protein, and the annotated region 510..528 matches D exactly.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Options B (1250..1269) and C (510..528; 680..699) can be eliminated immediately because the protein is only 639 residues long, making positions 1250 and 680 impossible. The remaining choice is between A (514..533) and D (510..528). Extracting the actual residues: D (510-528) = WFMWYASNYITGMLMASGV, which begins with the strongly hydrophobic W-F-M-W motif, a classic transmembrane helix anchor. A (514-533) = YASNYITGMLMASGVRVYEYK, which begins with polar residues (Y-A-S-N-Y) and ends with charged residues (E-Y-K), features highly inconsistent with a lipid-embedded alpha-helix. General knowledge of TM helix composition (hydrophobic core of ~19-25 residues, avoidance of charged residues within the bilayer) and the recognition that W, F, M, W form a canonical hydrophobic anchor at the membrane interface favor D. The protein is annotated as a cardiolipin synthase (EC 2.7.8.-), a membrane-associated enzyme, consistent with a single TM anchor.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate B and C by simple length check (639 AA), then use hydrophobicity analysis and general TM helix composition principles to distinguish D from A. The WFMWY motif at position 510-513 is a well-known hydrophobic anchor pattern, while option A's terminal charged residues (E, K) are incompatible with a transmembrane segment. This is a defensible transferable inference from general membrane-protein biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are unambiguously invalid because they reference residue positions beyond the 639-residue protein. Between A and D, the hydrophobicity profile clearly favors D: the WFMWY start and absence of terminal charges make D a more plausible TM helix than A, which starts with polar residues and ends with charged residues. While both regions have some mixed hydrophobicity, the charged-residue content at the boundaries of A is a strong disqualifier for a TM segment.


### Important caveats

- The UniProt TM annotation (510..528) carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational prediction rather than an experimentally determined boundary. The exact start/end positions may differ by a few residues in reality.
- The protein is a bacterial-type cardiolipin synthase in a eukaryotic organism (Trypanosoma brucei), which is an unusual evolutionary context. The single TM region is consistent with the membrane-anchoring role of this enzyme.
- The distinction between options A and D, while reasonable, involves a borderline hydrophobicity assessment; the WFMWY motif strongly favors D, but a model without careful hydrophobicity analysis might hesitate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Options B (1250..1269) and C (510..528; 680..699) can be eliminated immediately because the protein is only 639 residues long, making positions 1250 and 680 impossible. The remaining choice is between A (514..533) and D (510..528). Extracting the actual residues: D (510-528) = WFMWYASNYITGMLMASGV, which begins with the strongly hydrophobic W-F-M-W motif, a classic transmembrane helix anchor. A (514-533) = YASNYITGMLMASGVRVYEYK, which begins with polar residues (Y-A-S-N-Y) and ends with charged residues (E-Y-K), features highly inconsistent with a lipid-embedded alpha-helix. General knowledge of TM helix composition (hydrophobic core of ~19-25 residues, avoidance of charged residues within the bilayer) and the recognition that W, F, M, W form a canonical hydrophobic anchor at the membrane interface favor D. The protein is annotated as a cardiolipin synthase (EC 2.7.8.-), a membrane-associated enzyme, consistent with a single TM anchor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B and C by simple length check (639 AA), then use hydrophobicity analysis and general TM helix composition principles to distinguish D from A. The WFMWY motif at position 510-513 is a well-known hydrophobic anchor pattern, while option A's terminal charged residues (E, K) are incompatible with a transmembrane segment. This is a defensible transferable inference from general membrane-protein biology."
  },
  "case_id": "transmembrane_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for Q584D1 (Trypanosoma brucei cardiolipin synthetase, 639 AA) annotates a single transmembrane helical region at 510..528 (evidence C5, H3). The evidence code is ECO:0000255 (inferred by similarity), indicating a computational prediction rather than direct experimental determination, but the annotation directly matches the expected answer D. The sequence length of 639 AA confirms that options B (1250..1269) and C (680..699) reference positions beyond the protein, and the annotated region 510..528 matches D exactly."
  },
  "important_caveats": [
    "The UniProt TM annotation (510..528) carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational prediction rather than an experimentally determined boundary. The exact start/end positions may differ by a few residues in reality.",
    "The protein is a bacterial-type cardiolipin synthase in a eukaryotic organism (Trypanosoma brucei), which is an unusual evolutionary context. The single TM region is consistent with the membrane-anchoring role of this enzyme.",
    "The distinction between options A and D, while reasonable, involves a borderline hydrophobicity assessment; the WFMWY motif strongly favors D, but a model without careful hydrophobicity analysis might hesitate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are unambiguously invalid because they reference residue positions beyond the 639-residue protein. Between A and D, the hydrophobicity profile clearly favors D: the WFMWY start and absence of terminal charges make D a more plausible TM helix than A, which starts with polar residues and ends with charged residues. While both regions have some mixed hydrophobicity, the charged-residue content at the boundaries of A is a strong disqualifier for a TM segment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for Q584D1 (Trypanosoma brucei cardiolipin synthetase, 639 AA) annotates a single transmembrane helical region at 510..528 (evidence C5, H3). The evidence code is ECO:0000255 (inferred by similarity), indicating a computational prediction rather than direct experimental determination, but the annotation directly matches the expected answer D. The sequence length of 639 AA confirms that options B (1250..1269) and C (680..699) reference positions beyond the protein, and the annotated region 510..528 matches D exactly.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Options B (1250..1269) and C (510..528; 680..699) can be eliminated immediately because the protein is only 639 residues long, making positions 1250 and 680 impossible. The remaining choice is between A (514..533) and D (510..528). Extracting the actual residues: D (510-528) = WFMWYASNYITGMLMASGV, which begins with the strongly hydrophobic W-F-M-W motif, a classic transmembrane helix anchor. A (514-533) = YASNYITGMLMASGVRVYEYK, which begins with polar residues (Y-A-S-N-Y) and ends with charged residues (E-Y-K), features highly inconsistent with a lipid-embedded alpha-helix. General knowledge of TM helix composition (hydrophobic core of ~19-25 residues, avoidance of charged residues within the bilayer) and the recognition that W, F, M, W form a canonical hydrophobic anchor at the membrane interface favor D. The protein is annotated as a cardiolipin synthase (EC 2.7.8.-), a membrane-associated enzyme, consistent with a single TM anchor.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B and C by simple length check (639 AA), then use hydrophobicity analysis and general TM helix composition principles to distinguish D from A. The WFMWY motif at position 510-513 is a well-known hydrophobic anchor pattern, while option A's terminal charged residues (E, K) are incompatible with a transmembrane segment. This is a defensible transferable inference from general membrane-protein biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are unambiguously invalid because they reference residue positions beyond the 639-residue protein. Between A and D, the hydrophobicity profile clearly favors D: the WFMWY start and absence of terminal charges make D a more plausible TM helix than A, which starts with polar residues and ends with charged residues. While both regions have some mixed hydrophobicity, the charged-residue content at the boundaries of A is a strong disqualifier for a TM segment."
  },
  "important_caveats": [
    "The UniProt TM annotation (510..528) carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational prediction rather than an experimentally determined boundary. The exact start/end positions may differ by a few residues in reality.",
    "The protein is a bacterial-type cardiolipin synthase in a eukaryotic organism (Trypanosoma brucei), which is an unusual evolutionary context. The single TM region is consistent with the membrane-anchoring role of this enzyme.",
    "The distinction between options A and D, while reasonable, involves a borderline hydrophobicity assessment; the WFMWY motif strongly favors D, but a model without careful hydrophobicity analysis might hesitate."
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
  "benchmark_sequence_length": 639,
  "benchmark_sequence_sha256": "d1770a01906c887a932e40fe30f046ec16ec07c879d4a17024149479b46e4405",
  "current_entry_audit": {
    "entryVersion": 104,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-05-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 639,
  "current_source_sequence_sha256": "d1770a01906c887a932e40fe30f046ec16ec07c879d4a17024149479b46e4405",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 102,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q584D1",
  "selected_historical_entry_version": 102,
  "selected_historical_record_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "selected_historical_source_sequence_length": 639,
  "selected_historical_source_sequence_sha256": "d1770a01906c887a932e40fe30f046ec16ec07c879d4a17024149479b46e4405",
  "selected_historical_version": {
    "accession": "Q584D1",
    "database": "Swiss-Prot",
    "entryVersion": 102,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CLS_TRYB2",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q584D1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":104,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-05-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008524\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Discoba\",\"Euglenozoa\",\"Kinetoplastea\",\"Metakinetoplastina\",\"Trypanosomatida\",\"Trypanosomatidae\",\"Trypanosoma\"],\"scientificName\":\"Trypanosoma brucei brucei (strain 927/4 GUTat10.1)\",\"taxonId\":185431}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"22451910\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Cardiolipin synthetase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"CL synthase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":528},\"start\":{\"modifier\":\"EXACT\",\"value\":510}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q584D1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Serricchio M.\",\"Buetikofer P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22451910\"},{\"database\":\"DOI\",\"id\":\"10.1073/pnas.1121528109\"}],\"citationType\":\"journal article\",\"firstPage\":\"E954\",\"id\":\"22451910\",\"journal\":\"Proc. Natl. Acad. Sci. U.S.A.\",\"lastPage\":\"E961\",\"publicationDate\":\"2012\",\"title\":\"An essential bacterial-type cardiolipin synthase mediates cardiolipin formation in a eukaryote.\",\"volume\":\"109\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:31:01.049114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "06023be9a8f72ee85cb75383e10f4d8299d2a2508914f86a1650f4b851ae4215",
  "url": "https://rest.uniprot.org/uniprotkb/Q584D1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)

```json
{
  "entry_version": 102,
  "evidence_id": "H1",
  "excerpt": "ID   CLS_TRYB2               Reviewed;         639 AA.\nAC   Q584D1; D6XFJ2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-MAY-2005, sequence version 1.\nDT   28-JAN-2026, entry version 102.\nDE   RecName: Full=Cardiolipin synthetase {ECO:0000305};\nDE            Short=CL synthase {ECO:0000305};\nDE            EC=2.7.8.- {ECO:0000305|PubMed:22451910};\nDE   Flags: Precursor;\nGN   Name=CLS {ECO:0000303|PubMed:22451910};\nGN   ORFNames=Tb04.1H19.1130 {ECO:0000312|EMBL:AAZ10847.1},\nGN   Tb927.4.2560 {ECO:0000312|EMBL:AAX79074.1};\nOS   Trypanosoma brucei brucei (strain 927/4 GUTat10.1).\nOC   Eukaryota; Discoba; Euglenozoa; Kinetoplastea; Metakinetoplastina;\nOC   Trypanosomatida; Trypanosomatidae; Trypanosoma.\nOX   NCBI_TaxID=185431 {ECO:0000312|Proteomes:UP000008524};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:03.966233+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "url": "https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)

```json
{
  "entry_version": 102,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBUNIT, SUBCELLULAR LOCATION, AND DISRUPTION\nRP   PHENOTYPE.\nRX   PubMed=22451910; DOI=10.1073/pnas.1121528109;\nRA   Serricchio M., Buetikofer P.;\nRT   \"An essential bacterial-type cardiolipin synthase mediates cardiolipin\nRT   formation in a eukaryote.\";\nRL   Proc. Natl. Acad. Sci. U.S.A. 109:E954-E961(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:03.966233+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 65-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "url": "https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102)

```json
{
  "entry_version": 102,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        510..528\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:03.966233+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 162-164",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "88350d8820a0e6e2b3dbf458c2c3fbc779b40be576a352499efaf57465c08841",
  "url": "https://rest.uniprot.org/unisave/Q584D1?format=txt&versions=102"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 96. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
