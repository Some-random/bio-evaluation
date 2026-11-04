# transmembrane_0073

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0073.txt)

**Task:** `transmembrane`  
**Expected answer:** **A** — 3..23

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSILWIVAYALLAFAASIALNLVYQFLYRTFNKSRPPLVFHWVPFIGSTIHYGMDPYNFFFSCREKYGDIFTFILLGRPTTVYLGTQGNEFILNGKLKDVNAEEVYSPLTTPVFGSDVVYDCPNSKLIEQKKFIKFGLSQAALEAHVPLIEKEVIDYLAQSPNFNGTAGTVDIASAMAEITIFTAGSTLQGEEVRSKLTTEFAVLYHDLDKGFTPINFMLPWAPLPHNKKRDAAHARMRAIYIDIINKRRKAGNAATGKPDMIENLMQCTYKNGQPLPDKEIAHIMITLLMAGQHSSSSIGSWIMLRLASQPAIVEELYQEQLANLERTANGSLPPLQFKDIENLPLHQNVIRETLRLHGSIHSLLRKVKNPLPVPGTPYIIPTSHVLLSAPGVTALSDEYFPNAMAWDPHRWETQAPEESKEDIVDYGYGAMSKGTSSPYLPFGAGRHRCIGEKFAYLNLTVIVATLVRHLRFHNLDGKKGVPGTDYTSLFSGPLKPTRVGWERRAAKSA

[Multiple Choices]
A. 3..23
B. 2..28
C. 3..23; 126..145
D. 6..26; 300..320; 337..357; 373..393; 416..436; 439..459
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

> The sequence has a strongly hydrophobic N-terminal segment consistent with a membrane-spanning helix. The sequence-matched UniProt record annotates residues 3–23 as a helical transmembrane region, but its ECO:0000255 evidence code indicates computational annotation rather than direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus contains an extended, strongly hydrophobic stretch, which is characteristic of a membrane-spanning helix. Its approximately 21-residue core makes A a better fit than the longer 2–28 span in B; the remaining options propose extra or multiple transmembrane regions unsupported by comparable hydrophobic segments. Family-level knowledge that many cytochrome P450 enzymes have a single N-terminal membrane anchor is also consistent with this pattern, though the sequence alone does not fix helix boundaries precisely.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable sequence-pattern and protein-family knowledge meaningfully favors the N-terminal region and makes A the best choice among the alternatives. Exact boundaries are less certain from sequence inspection alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> A and B identify the same hydrophobic N-terminal helix with different boundaries. A is the more typical-length core, but the sequence does not definitively rule out a longer membrane-spanning segment as in B.


### Important caveats

- The supporting database annotation is computational, not experimental.
- Membrane-helix boundary estimates can vary; the sequence supports the region more strongly than its exact endpoints.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus contains an extended, strongly hydrophobic stretch, which is characteristic of a membrane-spanning helix. Its approximately 21-residue core makes A a better fit than the longer 2–28 span in B; the remaining options propose extra or multiple transmembrane regions unsupported by comparable hydrophobic segments. Family-level knowledge that many cytochrome P450 enzymes have a single N-terminal membrane anchor is also consistent with this pattern, though the sequence alone does not fix helix boundaries precisely.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence-pattern and protein-family knowledge meaningfully favors the N-terminal region and makes A the best choice among the alternatives. Exact boundaries are less certain from sequence inspection alone."
  },
  "case_id": "transmembrane_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence has a strongly hydrophobic N-terminal segment consistent with a membrane-spanning helix. The sequence-matched UniProt record annotates residues 3–23 as a helical transmembrane region, but its ECO:0000255 evidence code indicates computational annotation rather than direct experimental confirmation."
  },
  "important_caveats": [
    "The supporting database annotation is computational, not experimental.",
    "Membrane-helix boundary estimates can vary; the sequence supports the region more strongly than its exact endpoints."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "A and B identify the same hydrophobic N-terminal helix with different boundaries. A is the more typical-length core, but the sequence does not definitively rule out a longer membrane-spanning segment as in B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence has a strongly hydrophobic N-terminal segment consistent with a membrane-spanning helix. The sequence-matched UniProt record annotates residues 3–23 as a helical transmembrane region, but its ECO:0000255 evidence code indicates computational annotation rather than direct experimental confirmation.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus contains an extended, strongly hydrophobic stretch, which is characteristic of a membrane-spanning helix. Its approximately 21-residue core makes A a better fit than the longer 2–28 span in B; the remaining options propose extra or multiple transmembrane regions unsupported by comparable hydrophobic segments. Family-level knowledge that many cytochrome P450 enzymes have a single N-terminal membrane anchor is also consistent with this pattern, though the sequence alone does not fix helix boundaries precisely.",
    "missing_item_specific_fact": "",
    "reason": "Transferable sequence-pattern and protein-family knowledge meaningfully favors the N-terminal region and makes A the best choice among the alternatives. Exact boundaries are less certain from sequence inspection alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "A and B identify the same hydrophobic N-terminal helix with different boundaries. A is the more typical-length core, but the sequence does not definitively rule out a longer membrane-spanning segment as in B."
  },
  "important_caveats": [
    "The supporting database annotation is computational, not experimental.",
    "Membrane-helix boundary estimates can vary; the sequence supports the region more strongly than its exact endpoints."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXU9 annotates a transmembrane helix at positions 3..23 (evidence C5, H3). The sequence at positions 3-23 (ILWIVAYALLAFAASIALNLV) is a strongly hydrophobic 21-residue stretch consistent with a single-pass TM helix. The annotation evidence code is ECO:0000255 (by similarity/computational), not experimental, but it is consistent with the sequence properties and with the well-established single N-terminal TM anchor of microsomal cytochrome P450 enzymes.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein contains the canonical P450 heme-binding motif (FxxGxxxCxG, visible as 'GAGRHRCIGEKF' near the C-terminus) and overall architecture of a cytochrome P450 monooxygenase. Across the entire P450 superfamily, microsomal P450s (including sterol 14α-demethylases) are anchored to the ER membrane by a single N-terminal transmembrane helix, while the catalytic domain is soluble. This well-established family-level fact eliminates options C (adds a TM region at 126-145 within the catalytic domain) and D (adds five additional TM regions within the soluble catalytic domain). Between A (3-23) and B (2-28), hydrophobicity analysis of the actual sequence distinguishes them: position 2 is Ser (polar) and positions 24-28 are YQFLY (containing polar Gln), diluting the hydrophobic core. The 21-residue window 3-23 is the strongly hydrophobic core (average Kyte-Doolittle ~2.0), while extending to 2-28 lowers the mean hydrophobicity. A knowledgeable model recognizing P450 single-TM architecture and applying standard hydrophobicity criteria to the sequence can select A over B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The distinction between A and C/D relies on transferable P450-family knowledge (single N-terminal TM anchor, soluble catalytic domain). The distinction between A and B relies on hydrophobicity analysis of the provided sequence itself (S at position 2, Q at position 25 reduce hydrophobicity). No fact specific to this exact protein beyond what is inferable from the sequence and P450 family biology is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The boundary between A (3-23) and B (2-28) is somewhat subtle. While hydrophobicity clearly favors 3-23 as the core TM segment, some prediction tools might extend boundaries by a few residues. However, the presence of polar Ser at position 2 and polar Gln within 24-28 makes A the more defensible choice. This is a minor boundary ambiguity rather than a fundamental ambiguity, as the hydrophobicity gradient clearly supports 3-23.


### Important caveats

- The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), indicating computational transfer from related proteins rather than direct experimental measurement.
- The protein was identified as P0DXU9 (RESB_ASPSL, sterol 14α-demethylase) only through reviewer-only metadata; the evaluated model saw only the raw sequence.
- The sequence is 511 residues, matching the UniProt entry exactly (SHA256 confirmed).
- The heme-binding motif (CIGEK) is clearly visible near position 451, confirming P450 identity from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein contains the canonical P450 heme-binding motif (FxxGxxxCxG, visible as 'GAGRHRCIGEKF' near the C-terminus) and overall architecture of a cytochrome P450 monooxygenase. Across the entire P450 superfamily, microsomal P450s (including sterol 14α-demethylases) are anchored to the ER membrane by a single N-terminal transmembrane helix, while the catalytic domain is soluble. This well-established family-level fact eliminates options C (adds a TM region at 126-145 within the catalytic domain) and D (adds five additional TM regions within the soluble catalytic domain). Between A (3-23) and B (2-28), hydrophobicity analysis of the actual sequence distinguishes them: position 2 is Ser (polar) and positions 24-28 are YQFLY (containing polar Gln), diluting the hydrophobic core. The 21-residue window 3-23 is the strongly hydrophobic core (average Kyte-Doolittle ~2.0), while extending to 2-28 lowers the mean hydrophobicity. A knowledgeable model recognizing P450 single-TM architecture and applying standard hydrophobicity criteria to the sequence can select A over B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The distinction between A and C/D relies on transferable P450-family knowledge (single N-terminal TM anchor, soluble catalytic domain). The distinction between A and B relies on hydrophobicity analysis of the provided sequence itself (S at position 2, Q at position 25 reduce hydrophobicity). No fact specific to this exact protein beyond what is inferable from the sequence and P450 family biology is needed."
  },
  "case_id": "transmembrane_0073",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU9 annotates a transmembrane helix at positions 3..23 (evidence C5, H3). The sequence at positions 3-23 (ILWIVAYALLAFAASIALNLV) is a strongly hydrophobic 21-residue stretch consistent with a single-pass TM helix. The annotation evidence code is ECO:0000255 (by similarity/computational), not experimental, but it is consistent with the sequence properties and with the well-established single N-terminal TM anchor of microsomal cytochrome P450 enzymes."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), indicating computational transfer from related proteins rather than direct experimental measurement.",
    "The protein was identified as P0DXU9 (RESB_ASPSL, sterol 14α-demethylase) only through reviewer-only metadata; the evaluated model saw only the raw sequence.",
    "The sequence is 511 residues, matching the UniProt entry exactly (SHA256 confirmed).",
    "The heme-binding motif (CIGEK) is clearly visible near position 451, confirming P450 identity from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The boundary between A (3-23) and B (2-28) is somewhat subtle. While hydrophobicity clearly favors 3-23 as the core TM segment, some prediction tools might extend boundaries by a few residues. However, the presence of polar Ser at position 2 and polar Gln within 24-28 makes A the more defensible choice. This is a minor boundary ambiguity rather than a fundamental ambiguity, as the hydrophobicity gradient clearly supports 3-23."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0073",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU9 annotates a transmembrane helix at positions 3..23 (evidence C5, H3). The sequence at positions 3-23 (ILWIVAYALLAFAASIALNLV) is a strongly hydrophobic 21-residue stretch consistent with a single-pass TM helix. The annotation evidence code is ECO:0000255 (by similarity/computational), not experimental, but it is consistent with the sequence properties and with the well-established single N-terminal TM anchor of microsomal cytochrome P450 enzymes.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein contains the canonical P450 heme-binding motif (FxxGxxxCxG, visible as 'GAGRHRCIGEKF' near the C-terminus) and overall architecture of a cytochrome P450 monooxygenase. Across the entire P450 superfamily, microsomal P450s (including sterol 14α-demethylases) are anchored to the ER membrane by a single N-terminal transmembrane helix, while the catalytic domain is soluble. This well-established family-level fact eliminates options C (adds a TM region at 126-145 within the catalytic domain) and D (adds five additional TM regions within the soluble catalytic domain). Between A (3-23) and B (2-28), hydrophobicity analysis of the actual sequence distinguishes them: position 2 is Ser (polar) and positions 24-28 are YQFLY (containing polar Gln), diluting the hydrophobic core. The 21-residue window 3-23 is the strongly hydrophobic core (average Kyte-Doolittle ~2.0), while extending to 2-28 lowers the mean hydrophobicity. A knowledgeable model recognizing P450 single-TM architecture and applying standard hydrophobicity criteria to the sequence can select A over B.",
    "missing_item_specific_fact": "",
    "reason": "The distinction between A and C/D relies on transferable P450-family knowledge (single N-terminal TM anchor, soluble catalytic domain). The distinction between A and B relies on hydrophobicity analysis of the provided sequence itself (S at position 2, Q at position 25 reduce hydrophobicity). No fact specific to this exact protein beyond what is inferable from the sequence and P450 family biology is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The boundary between A (3-23) and B (2-28) is somewhat subtle. While hydrophobicity clearly favors 3-23 as the core TM segment, some prediction tools might extend boundaries by a few residues. However, the presence of polar Ser at position 2 and polar Gln within 24-28 makes A the more defensible choice. This is a minor boundary ambiguity rather than a fundamental ambiguity, as the hydrophobicity gradient clearly supports 3-23."
  },
  "important_caveats": [
    "The UniProt TM annotation uses evidence code ECO:0000255 (by similarity), indicating computational transfer from related proteins rather than direct experimental measurement.",
    "The protein was identified as P0DXU9 (RESB_ASPSL, sterol 14α-demethylase) only through reviewer-only metadata; the evaluated model saw only the raw sequence.",
    "The sequence is 511 residues, matching the UniProt entry exactly (SHA256 confirmed).",
    "The heme-binding motif (CIGEK) is clearly visible near position 451, confirming P450 identity from sequence alone."
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
  "benchmark_sequence_length": 511,
  "benchmark_sequence_sha256": "a64d471b7671e38c6cea7bce97558a2ede1a3a938dacb056f2034f73583fb71d",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 511,
  "current_source_sequence_sha256": "a64d471b7671e38c6cea7bce97558a2ede1a3a938dacb056f2034f73583fb71d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXU9",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "selected_historical_source_sequence_length": 511,
  "selected_historical_source_sequence_sha256": "a64d471b7671e38c6cea7bce97558a2ede1a3a938dacb056f2034f73583fb71d",
  "selected_historical_version": {
    "accession": "P0DXU9",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RESB_ASPSL",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXU9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus sclerotiorum\",\"taxonId\":138282}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase resB\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Ergosterol biosynthesis protein resB\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Restricticin biosynthesis cluster protein B\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0L1JEW4\",\"source\":\"UniProtKB\"}],\"value\":\"1.14.14.154\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39105744\",\"source\":\"PubMed\"}],\"value\":\"Sterol 14-alpha demethylase resB\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":23},\"start\":{\"modifier\":\"EXACT\",\"value\":3}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Lu Y.\",\"Li Y.\",\"Dou M.\",\"Liu D.\",\"Lin W.\",\"Fan A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39105744\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.jafc.4c04244\"}],\"citationType\":\"journal article\",\"firstPage\":\"18520\",\"id\":\"39105744\",\"journal\":\"J. Agric. Food Chem.\",\"lastPage\":\"18527\",\"publicationDate\":\"2024\",\"title\":\"Discovery of a hybrid molecule with phytotoxic activity by genome mining, heterologous expression, and OSMAC strategy.\",\"volume\":\"72\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:42.593366+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "40d813fd632571e8a780769b1d88199517ade98bc5effc2ac4fd6b84277b29e0",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   RESB_ASPSL              Reviewed;         511 AA.\nAC   P0DXU9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Sterol 14-alpha demethylase resB {ECO:0000303|PubMed:39105744};\nDE            EC=1.14.14.154 {ECO:0000250|UniProtKB:A0A0L1JEW4};\nDE   AltName: Full=Cytochrome P450 monooxygenase resB {ECO:0000303|PubMed:39105744};\nDE   AltName: Full=Ergosterol biosynthesis protein resB {ECO:0000303|PubMed:39105744};\nDE   AltName: Full=Restricticin biosynthesis cluster protein B {ECO:0000303|PubMed:39105744};\nGN   Name=resB {ECO:0000303|PubMed:39105744};\nOS   Aspergillus sclerotiorum.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=138282;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRX   PubMed=39105744; DOI=10.1021/acs.jafc.4c04244;\nRA   Lu Y., Li Y., Dou M., Liu D., Lin W., Fan A.;\nRT   \"Discovery of a hybrid molecule with phytotoxic activity by genome mining,\nRT   heterologous expression, and OSMAC strategy.\";\nRL   J. Agric. Food Chem. 72:18520-18527(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        3..23\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:47.314530+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 193-195",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2a6568f1e723fcdca7476452cdc9b1cfa3524cc0d46266999459913d20ccaeb0",
  "url": "https://rest.uniprot.org/unisave/P0DXU9?format=txt&versions=4"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 73. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
