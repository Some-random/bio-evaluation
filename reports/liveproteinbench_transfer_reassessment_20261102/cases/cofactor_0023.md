# cofactor_0023

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0023.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — pyridoxal 5&#x27;-phosphate

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MIAVNSRNSLNADMTSLHPETLMVHGGMKGLTEAGVHVPAIDLSTTNPVNDVATGGDSYEWLATGHTLKDGDSAVYQRLWQPGVARFETALAGLEHAEEAVAFATGMAAMTAALLAAVSAGTPHIVAVRPLYGGSDHLLETGLLGTTVTWAKEADIASAIQDDTGLVIVETPANPSLDLVDLDSVVSAAGNVPVLVDNTFCTPVLQQPISHGAALVLHSATKYLGGHGDAMGGIIATNADWAMRLRQVRAITGALLHPMGAYLLHRGLRTLAVRMRAAQTTAGELAERLDAHPAISVVHYPGLKGQDPRGLLGRQMSGGGAMIAMELAGGFDAARSFVEHCNLVVHAVSLGGADTLIQHPASLTHRPVAATAKPGDGLIRLSVGLEHVDDLADDLIAALDASRAAA

[Multiple Choices]
A. pyridoxal 5'-phosphate
B. Na(+)
C. heme b
D. heme
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates pyridoxal 5′-phosphate as the cofactor and cites experimental evidence for that annotation.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a PLP-dependent amino-acid lyase family: such enzymes use a conserved active-site lysine to bind PLP and catalyze amino-acid transformations. That family-level pattern favors option A over sodium or either heme choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of PLP-dependent lyases provides a meaningful basis to distinguish PLP from the offered alternatives; recalling this exact protein’s database record is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The two heme options are redundant with each other, but neither is a similarly defensible alternative to PLP for this sequence.


### Important caveats

- The reviewer-only annotation supports the answer and cites experimental evidence, but the cited primary studies were not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a PLP-dependent amino-acid lyase family: such enzymes use a conserved active-site lysine to bind PLP and catalyze amino-acid transformations. That family-level pattern favors option A over sodium or either heme choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of PLP-dependent lyases provides a meaningful basis to distinguish PLP from the offered alternatives; recalling this exact protein’s database record is not necessary."
  },
  "case_id": "cofactor_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates pyridoxal 5′-phosphate as the cofactor and cites experimental evidence for that annotation."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the answer and cites experimental evidence, but the cited primary studies were not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The two heme options are redundant with each other, but neither is a similarly defensible alternative to PLP for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates pyridoxal 5′-phosphate as the cofactor and cites experimental evidence for that annotation.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a PLP-dependent amino-acid lyase family: such enzymes use a conserved active-site lysine to bind PLP and catalyze amino-acid transformations. That family-level pattern favors option A over sodium or either heme choice.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of PLP-dependent lyases provides a meaningful basis to distinguish PLP from the offered alternatives; recalling this exact protein’s database record is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The two heme options are redundant with each other, but neither is a similarly defensible alternative to PLP for this sequence."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the answer and cites experimental evidence, but the cited primary studies were not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (A0A2H1K3G9, L-methionine gamma-lyase from Brevibacterium aurantiacum, EC 4.4.1.11) explicitly annotates the cofactor as pyridoxal 5'-phosphate (ChEBI:CHEBI:597326), supported by experimental evidence codes ECO:0000269 from two independent PubMed studies (9726878 and 30940696). The answer is directly and experimentally confirmed.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C6](#evidence-c6), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple transferable lines of reasoning distinguish PLP from the other options. (1) Family/fold recognition: The sequence contains the conserved 'HG' dipeptide motif near the N-terminus (HGGMKGL, position ~17-18), which is the hallmark of PLP-dependent fold-type I enzymes, where the PLP is covalently bound via a Schiff base to the lysine in this motif. Additional HG motifs (HGVHVPAIDL, HGAALVLHS, HYPGLKG) further support this fold. (2) EC-class biochemistry: The enzyme catalyzes a gamma-elimination from an amino acid (EC 4.4.1.11). All known amino acid gamma-lyases (cystathionine beta-lyase, methionine gamma-lyase, cystathionine gamma-synthase) are PLP-dependent; this is a well-established family-level regularity. The PLP-stabilized carbanion mechanism is the canonical route for such eliminations. (3) Elimination of distractors: Heme (C, D) is the prosthetic group of peroxidases, cytochromes, and oxidases—none of which perform amino acid elimination. Na+ (B) is a cofactor for ion transporters and certain hydrolases, not lyases. Thus, general knowledge of PLP-dependent enzyme families and the biochemistry of amino acid elimination reactions meaningfully and confidently selects A over B, C, and D without needing to look up this specific protein's record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the PLP-binding HG motif, recognize the enzyme as belonging to the PLP-dependent amino acid lyase superfamily, and apply the well-established rule that all gamma-lyases acting on amino acids require PLP. The distractors (heme, heme b, Na+) are implausible for any amino acid elimination enzyme based on general biochemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (heme b) and D (heme) are somewhat redundant since heme b is a subtype of heme, but both are clearly incorrect for an amino acid lyase. Option B (Na+) is also clearly implausible. Only PLP (A) is consistent with the enzyme's catalytic mechanism and fold.


### Important caveats

- The reviewer-only UniProt evidence confirms PLP as the cofactor with experimental evidence (ECO:0000269), but this annotation was not available to the evaluated model.
- The HG motif at the N-terminus is a strong but not absolutely universal PLP-binding indicator; however, combined with the gamma-lyase activity inference, it provides a robust argument.
- Options C and D (heme b vs. heme) are nearly synonymous, which is a minor question-design issue but does not affect the correct answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple transferable lines of reasoning distinguish PLP from the other options. (1) Family/fold recognition: The sequence contains the conserved 'HG' dipeptide motif near the N-terminus (HGGMKGL, position ~17-18), which is the hallmark of PLP-dependent fold-type I enzymes, where the PLP is covalently bound via a Schiff base to the lysine in this motif. Additional HG motifs (HGVHVPAIDL, HGAALVLHS, HYPGLKG) further support this fold. (2) EC-class biochemistry: The enzyme catalyzes a gamma-elimination from an amino acid (EC 4.4.1.11). All known amino acid gamma-lyases (cystathionine beta-lyase, methionine gamma-lyase, cystathionine gamma-synthase) are PLP-dependent; this is a well-established family-level regularity. The PLP-stabilized carbanion mechanism is the canonical route for such eliminations. (3) Elimination of distractors: Heme (C, D) is the prosthetic group of peroxidases, cytochromes, and oxidases—none of which perform amino acid elimination. Na+ (B) is a cofactor for ion transporters and certain hydrolases, not lyases. Thus, general knowledge of PLP-dependent enzyme families and the biochemistry of amino acid elimination reactions meaningfully and confidently selects A over B, C, and D without needing to look up this specific protein's record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the PLP-binding HG motif, recognize the enzyme as belonging to the PLP-dependent amino acid lyase superfamily, and apply the well-established rule that all gamma-lyases acting on amino acids require PLP. The distractors (heme, heme b, Na+) are implausible for any amino acid elimination enzyme based on general biochemistry."
  },
  "case_id": "cofactor_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C6",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0A2H1K3G9, L-methionine gamma-lyase from Brevibacterium aurantiacum, EC 4.4.1.11) explicitly annotates the cofactor as pyridoxal 5'-phosphate (ChEBI:CHEBI:597326), supported by experimental evidence codes ECO:0000269 from two independent PubMed studies (9726878 and 30940696). The answer is directly and experimentally confirmed."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence confirms PLP as the cofactor with experimental evidence (ECO:0000269), but this annotation was not available to the evaluated model.",
    "The HG motif at the N-terminus is a strong but not absolutely universal PLP-binding indicator; however, combined with the gamma-lyase activity inference, it provides a robust argument.",
    "Options C and D (heme b vs. heme) are nearly synonymous, which is a minor question-design issue but does not affect the correct answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (heme b) and D (heme) are somewhat redundant since heme b is a subtype of heme, but both are clearly incorrect for an amino acid lyase. Option B (Na+) is also clearly implausible. Only PLP (A) is consistent with the enzyme's catalytic mechanism and fold."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0A2H1K3G9, L-methionine gamma-lyase from Brevibacterium aurantiacum, EC 4.4.1.11) explicitly annotates the cofactor as pyridoxal 5'-phosphate (ChEBI:CHEBI:597326), supported by experimental evidence codes ECO:0000269 from two independent PubMed studies (9726878 and 30940696). The answer is directly and experimentally confirmed.",
    "evidence_ids": ["C5", "H5", "C6", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple transferable lines of reasoning distinguish PLP from the other options. (1) Family/fold recognition: The sequence contains the conserved 'HG' dipeptide motif near the N-terminus (HGGMKGL, position ~17-18), which is the hallmark of PLP-dependent fold-type I enzymes, where the PLP is covalently bound via a Schiff base to the lysine in this motif. Additional HG motifs (HGVHVPAIDL, HGAALVLHS, HYPGLKG) further support this fold. (2) EC-class biochemistry: The enzyme catalyzes a gamma-elimination from an amino acid (EC 4.4.1.11). All known amino acid gamma-lyases (cystathionine beta-lyase, methionine gamma-lyase, cystathionine gamma-synthase) are PLP-dependent; this is a well-established family-level regularity. The PLP-stabilized carbanion mechanism is the canonical route for such eliminations. (3) Elimination of distractors: Heme (C, D) is the prosthetic group of peroxidases, cytochromes, and oxidases—none of which perform amino acid elimination. Na+ (B) is a cofactor for ion transporters and certain hydrolases, not lyases. Thus, general knowledge of PLP-dependent enzyme families and the biochemistry of amino acid elimination reactions meaningfully and confidently selects A over B, C, and D without needing to look up this specific protein's record.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the PLP-binding HG motif, recognize the enzyme as belonging to the PLP-dependent amino acid lyase superfamily, and apply the well-established rule that all gamma-lyases acting on amino acids require PLP. The distractors (heme, heme b, Na+) are implausible for any amino acid elimination enzyme based on general biochemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (heme b) and D (heme) are somewhat redundant since heme b is a subtype of heme, but both are clearly incorrect for an amino acid lyase. Option B (Na+) is also clearly implausible. Only PLP (A) is consistent with the enzyme's catalytic mechanism and fold."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence confirms PLP as the cofactor with experimental evidence (ECO:0000269), but this annotation was not available to the evaluated model.",
    "The HG motif at the N-terminus is a strong but not absolutely universal PLP-binding indicator; however, combined with the gamma-lyase activity inference, it provides a robust argument.",
    "Options C and D (heme b vs. heme) are nearly synonymous, which is a minor question-design issue but does not affect the correct answer."
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
  "benchmark_sequence_length": 406,
  "benchmark_sequence_sha256": "435ffd3b8e0f97253809f6299a192824acbc91b3f9ba8e80c96d087a48e0a9a8",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-01-31",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 406,
  "current_source_sequence_sha256": "435ffd3b8e0f97253809f6299a192824acbc91b3f9ba8e80c96d087a48e0a9a8",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A2H1K3G9",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "selected_historical_source_sequence_length": 406,
  "selected_historical_source_sequence_sha256": "435ffd3b8e0f97253809f6299a192824acbc91b3f9ba8e80c96d087a48e0a9a8",
  "selected_historical_version": {
    "accession": "A0A2H1K3G9",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MEGL_BREAU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A2H1K3G9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-01-31\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Micrococcales\",\"Brevibacteriaceae\",\"Brevibacterium\"],\"scientificName\":\"Brevibacterium aurantiacum\",\"taxonId\":273384}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"value\":\"4.4.1.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"value\":\"Homocysteine desulfhydrase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"}],\"value\":\"MGL-BL929\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"4.4.1.11\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"L-methionine gamma-lyase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"value\":\"MGL\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:597326\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30940696\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9726878\",\"source\":\"PubMed\"}],\"name\":\"pyridoxal 5'-phosphate\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Dias B.\",\"Weimer B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9726878\"},{\"database\":\"DOI\",\"id\":\"10.1128/aem.64.9.3327-3331.1998\"}],\"citationType\":\"journal article\",\"firstPage\":\"3327\",\"id\":\"9726878\",\"journal\":\"Appl. Environ. Microbiol.\",\"lastPage\":\"3331\",\"publicationDate\":\"1998\",\"title\":\"Purification and characterization of L-methionine gamma-lyase from brevibacterium linens BL2.\",\"volume\":\"64\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"BL2\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBSTRATE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Machover D.\",\"Rossi L.\",\"Hamelin J.\",\"Desterke C.\",\"Goldschmidt E.\",\"Chadefaux-Vekemans B.\",\"Bonnarme P.\",\"Briozzo P.\",\"Kopecny D.\",\"Pierige F.\",\"Magnani M.\",\"Mollicone R.\",\"Haghighi-Rad F.\",\"Gaston-Mathe Y.\",\"Dairou J.\",\"Boucheix C.\",\"Saffroy R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30940696\"},{\"database\":\"DOI\",\"id\":\"10.1124/jpet.119.256537\"}],\"citationType\":\"journal article\",\"firstPage\":\"489\",\"id\":\"30940696\",\"journal\":\"J. Pharmacol. Exp. Ther.\",\"lastPage\":\"502\",\"publicationDate\":\"2019\",\"title\":\"Effects in Cancer Cells of the Recombinant L-Methionine Gamma-Lyase from Brevibacterium aurantiacum. Encapsulation in Human Erythrocytes for Sustained L-Methionine Elimination.\",\"volume\":\"369\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 9175 / DSM 20426 / JCM 2590 / NBRC 12171 / NCDO 739 / NCIMB 8546 / KC\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBSTRATE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:44.554855+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a920c3d8a2606b869b1968d0c8b2153e5ed89fbf0c4578d7222ed95845d1c3a6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2H1K3G9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   MEGL_BREAU              Reviewed;         406 AA.\nAC   A0A2H1K3G9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   31-JAN-2018, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=L-methionine gamma-lyase {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};\nDE            Short=MGL {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};\nDE            EC=4.4.1.11 {ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};\nDE   AltName: Full=Homocysteine desulfhydrase {ECO:0000303|PubMed:30940696};\nDE            EC=4.4.1.2 {ECO:0000269|PubMed:30940696};\nDE   AltName: Full=MGL-BL929 {ECO:0000303|PubMed:30940696};\nGN   ORFNames=BAUR9175_03070 {ECO:0000312|EMBL:SMX94104.1},\nGN   BAUR920_03040 {ECO:0000312|EMBL:SMX97377.1},\nGN   BAURA63_02933 {ECO:0000312|EMBL:SMX94451.1},\nGN   BAURA86_00394 {ECO:0000312|EMBL:SMX72154.1};\nOS   Brevibacterium aurantiacum.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Micrococcales;\nOC   Brevibacteriaceae; Brevibacterium.\nOX   NCBI_TaxID=273384;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=L-methionine gamma-lyase {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};\nDE            Short=MGL {ECO:0000303|PubMed:30940696, ECO:0000303|PubMed:9726878};\nDE            EC=4.4.1.11 {ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};\nDE   AltName: Full=Homocysteine desulfhydrase {ECO:0000303|PubMed:30940696};\nDE            EC=4.4.1.2 {ECO:0000269|PubMed:30940696};\nDE   AltName: Full=MGL-BL929 {ECO:0000303|PubMed:30940696};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBSTRATE SPECIFICITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, ACTIVITY REGULATION, AND SUBUNIT.\nRC   STRAIN=BL2;\nRX   PubMed=9726878; DOI=10.1128/aem.64.9.3327-3331.1998;\nRA   Dias B., Weimer B.;\nRT   \"Purification and characterization of L-methionine gamma-lyase from\nRT   brevibacterium linens BL2.\";\nRL   Appl. Environ. Microbiol. 64:3327-3331(1998).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBSTRATE SPECIFICITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND BIOTECHNOLOGY.\nRC   STRAIN=ATCC 9175 / DSM 20426 / JCM 2590 / NBRC 12171 / NCDO 739 / NCIMB\nRC   8546 / KC;\nRX   PubMed=30940696; DOI=10.1124/jpet.119.256537;\nRA   Machover D., Rossi L., Hamelin J., Desterke C., Goldschmidt E.,\nRA   Chadefaux-Vekemans B., Bonnarme P., Briozzo P., Kopecny D., Pierige F.,\nRA   Magnani M., Mollicone R., Haghighi-Rad F., Gaston-Mathe Y., Dairou J.,\nRA   Boucheix C., Saffroy R.;\nRT   \"Effects in Cancer Cells of the Recombinant L-Methionine Gamma-Lyase from\nRT   Brevibacterium aurantiacum. Encapsulation in Human Erythrocytes for\nRT   Sustained L-Methionine Elimination.\";\nRL   J. Pharmacol. Exp. Ther. 369:489-502(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=pyridoxal 5'-phosphate; Xref=ChEBI:CHEBI:597326;\nCC         Evidence={ECO:0000269|PubMed:30940696, ECO:0000269|PubMed:9726878};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:25.782043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 75-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9f8f2097c25cd1b2756007ac83a5f1a172b3bde4aa3f977e22144a88c5ee6f0b",
  "url": "https://rest.uniprot.org/unisave/A0A2H1K3G9?format=txt&versions=32"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 23. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
