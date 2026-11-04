# EC_number_0115

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0115.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 7.6.2.2

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MADTAITVDGAEKRYGDKKALDGLDLRVARGTVHGVLGPNGAGKTTLVRVLSTLLRPDAGRIEVSGHDVVREAYAVRLRIGLLGQHAALDEELGGRQNLELFGRLHHLGARRARARADELLERFDLADTGRKTVRQYSGGMRRRLDLAASLITEPEVLFLDEPTTGLDPRGRAEVWDSVRSLVGGGTTVLLTTQYLEEADQLADRISVVDAGRVIAEGTADELKAETGGDRIDVVLREAGQLGAAVALLPLTGVTVDTDRRLLSAPVTDRMEALSGVVRALQEAGIEAEDVALRRPTLDEVFLHLTGDDRRVKEAA

[Multiple Choices]
A. 6.3.5.1
B. 2.4.2.14
C. 2.5.1.160
D. 7.6.2.2
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The matched UniProt record assigns EC 7.6.2.2 and describes ATP-driven daunorubicin efflux, consistent with choice D. The annotation cites a publication, though the supplied evidence does not independently validate that study's experiments.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a P-loop Walker A motif (GPNGAGKTT) and other ABC ATPase features, supporting an ABC transporter ATP-binding component. Among the options, D is the ABC-type transport EC; the other choices are transferase or ligase ECs. This family-level inference distinguishes D among the choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence supports the transporter class, which is enough to select the only transporter option offered. It does not by itself establish daunorubicin as the transported substrate, so the exact four-digit assignment is less certain than the choice-level distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D corresponds to the ABC transporter class indicated by the sequence among the supplied alternatives.


### Important caveats

- The sequence-level argument supports ABC transport but does not independently resolve substrate specificity.
- The reviewer-only annotation is linked to a publication; that primary evidence was not independently assessed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a P-loop Walker A motif (GPNGAGKTT) and other ABC ATPase features, supporting an ABC transporter ATP-binding component. Among the options, D is the ABC-type transport EC; the other choices are transferase or ligase ECs. This family-level inference distinguishes D among the choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence supports the transporter class, which is enough to select the only transporter option offered. It does not by itself establish daunorubicin as the transported substrate, so the exact four-digit assignment is less certain than the choice-level distinction."
  },
  "case_id": "EC_number_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt record assigns EC 7.6.2.2 and describes ATP-driven daunorubicin efflux, consistent with choice D. The annotation cites a publication, though the supplied evidence does not independently validate that study's experiments."
  },
  "important_caveats": [
    "The sequence-level argument supports ABC transport but does not independently resolve substrate specificity.",
    "The reviewer-only annotation is linked to a publication; that primary evidence was not independently assessed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D corresponds to the ABC transporter class indicated by the sequence among the supplied alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt record assigns EC 7.6.2.2 and describes ATP-driven daunorubicin efflux, consistent with choice D. The annotation cites a publication, though the supplied evidence does not independently validate that study's experiments.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a P-loop Walker A motif (GPNGAGKTT) and other ABC ATPase features, supporting an ABC transporter ATP-binding component. Among the options, D is the ABC-type transport EC; the other choices are transferase or ligase ECs. This family-level inference distinguishes D among the choices.",
    "missing_item_specific_fact": "",
    "reason": "The sequence supports the transporter class, which is enough to select the only transporter option offered. It does not by itself establish daunorubicin as the transported substrate, so the exact four-digit assignment is less certain than the choice-level distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D corresponds to the ABC transporter class indicated by the sequence among the supplied alternatives."
  },
  "important_caveats": [
    "The sequence-level argument supports ABC transport but does not independently resolve substrate specificity.",
    "The reviewer-only annotation is linked to a publication; that primary evidence was not independently assessed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXU7 (DRRA3_STRC4) annotates this protein as 'Daunorubicin resistance ATP-binding protein DrrA3' with EC 7.6.2.2, supported by experimental evidence (ECO:0000305, PubMed:39375957). The catalytic reaction is daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+), consistent with EC 7.6.2.2 (ABC-type drug efflux transporter). The sequence matches exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical ABC transporter NBD (nucleotide-binding domain) motifs: a Walker A motif 'G-P-N-G-A-G-K-T' (GxxGxGKS/T pattern) in 'GPNGAGKTTLVRV', a Walker B motif with the conserved 'D-E' in 'LDEPTTGLDPRG', and a variant ABC signature region in 'VGGGTTVLL'. These P-loop/ABC signatures are well-known transferable features of ABC-type ATPases. Among the four choices, only 7.6.2.2 belongs to EC class 7 (translocases), which is the class containing all ABC transporters. Options A (6.3.5.1, ligase), B (2.4.2.14, transferase), and C (2.5.1.160, transferase) belong to entirely different EC classes whose catalytic mechanisms (peptide bond formation, glycosyl transfer, alkyl transfer) are incompatible with the observed ABC ATP-binding architecture. Recognizing the ABC signature and knowing that ABC transporters are classified under EC 7 is sufficient to select D over the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Walker A motif (GAGKT) and Walker B motif (DE) are textbook ABC transporter signatures. EC class 7 encompasses translocases including all ABC transporters, while classes 2 and 6 are transferases and ligases respectively. Identifying the ABC signature eliminates A, B, and C, leaving D as the only viable choice. This is standard transferable knowledge about protein families and EC classification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only one option (D, 7.6.2.2) falls within EC class 7 (translocases), which is the correct class for ABC-type ATP-binding proteins. The other three options belong to unrelated EC classes (6 and 2) and are clearly incompatible with the observed ABC signature motifs.


### Important caveats

- The specific sub-classification within EC 7 (7.6 vs 7.1, 7.2, etc.) would require additional knowledge about drug efflux specificity, but since only one EC 7 option is offered, identifying the ABC signature is sufficient to select D.
- The UniProt annotation uses ECO:0000305 (inferred from sequence or biological characteristics of related sequence), which is a computational/inference-level evidence code rather than direct experimental characterization of this exact protein.
- The entry was first released in 2025, so this is a relatively new annotation; the historical availability at the time of benchmark construction is uncertain.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical ABC transporter NBD (nucleotide-binding domain) motifs: a Walker A motif 'G-P-N-G-A-G-K-T' (GxxGxGKS/T pattern) in 'GPNGAGKTTLVRV', a Walker B motif with the conserved 'D-E' in 'LDEPTTGLDPRG', and a variant ABC signature region in 'VGGGTTVLL'. These P-loop/ABC signatures are well-known transferable features of ABC-type ATPases. Among the four choices, only 7.6.2.2 belongs to EC class 7 (translocases), which is the class containing all ABC transporters. Options A (6.3.5.1, ligase), B (2.4.2.14, transferase), and C (2.5.1.160, transferase) belong to entirely different EC classes whose catalytic mechanisms (peptide bond formation, glycosyl transfer, alkyl transfer) are incompatible with the observed ABC ATP-binding architecture. Recognizing the ABC signature and knowing that ABC transporters are classified under EC 7 is sufficient to select D over the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Walker A motif (GAGKT) and Walker B motif (DE) are textbook ABC transporter signatures. EC class 7 encompasses translocases including all ABC transporters, while classes 2 and 6 are transferases and ligases respectively. Identifying the ABC signature eliminates A, B, and C, leaving D as the only viable choice. This is standard transferable knowledge about protein families and EC classification."
  },
  "case_id": "EC_number_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU7 (DRRA3_STRC4) annotates this protein as 'Daunorubicin resistance ATP-binding protein DrrA3' with EC 7.6.2.2, supported by experimental evidence (ECO:0000305, PubMed:39375957). The catalytic reaction is daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+), consistent with EC 7.6.2.2 (ABC-type drug efflux transporter). The sequence matches exactly."
  },
  "important_caveats": [
    "The specific sub-classification within EC 7 (7.6 vs 7.1, 7.2, etc.) would require additional knowledge about drug efflux specificity, but since only one EC 7 option is offered, identifying the ABC signature is sufficient to select D.",
    "The UniProt annotation uses ECO:0000305 (inferred from sequence or biological characteristics of related sequence), which is a computational/inference-level evidence code rather than direct experimental characterization of this exact protein.",
    "The entry was first released in 2025, so this is a relatively new annotation; the historical availability at the time of benchmark construction is uncertain."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (D, 7.6.2.2) falls within EC class 7 (translocases), which is the correct class for ABC-type ATP-binding proteins. The other three options belong to unrelated EC classes (6 and 2) and are clearly incompatible with the observed ABC signature motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU7 (DRRA3_STRC4) annotates this protein as 'Daunorubicin resistance ATP-binding protein DrrA3' with EC 7.6.2.2, supported by experimental evidence (ECO:0000305, PubMed:39375957). The catalytic reaction is daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+), consistent with EC 7.6.2.2 (ABC-type drug efflux transporter). The sequence matches exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical ABC transporter NBD (nucleotide-binding domain) motifs: a Walker A motif 'G-P-N-G-A-G-K-T' (GxxGxGKS/T pattern) in 'GPNGAGKTTLVRV', a Walker B motif with the conserved 'D-E' in 'LDEPTTGLDPRG', and a variant ABC signature region in 'VGGGTTVLL'. These P-loop/ABC signatures are well-known transferable features of ABC-type ATPases. Among the four choices, only 7.6.2.2 belongs to EC class 7 (translocases), which is the class containing all ABC transporters. Options A (6.3.5.1, ligase), B (2.4.2.14, transferase), and C (2.5.1.160, transferase) belong to entirely different EC classes whose catalytic mechanisms (peptide bond formation, glycosyl transfer, alkyl transfer) are incompatible with the observed ABC ATP-binding architecture. Recognizing the ABC signature and knowing that ABC transporters are classified under EC 7 is sufficient to select D over the other three options.",
    "missing_item_specific_fact": "",
    "reason": "The Walker A motif (GAGKT) and Walker B motif (DE) are textbook ABC transporter signatures. EC class 7 encompasses translocases including all ABC transporters, while classes 2 and 6 are transferases and ligases respectively. Identifying the ABC signature eliminates A, B, and C, leaving D as the only viable choice. This is standard transferable knowledge about protein families and EC classification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only one option (D, 7.6.2.2) falls within EC class 7 (translocases), which is the correct class for ABC-type ATP-binding proteins. The other three options belong to unrelated EC classes (6 and 2) and are clearly incompatible with the observed ABC signature motifs."
  },
  "important_caveats": [
    "The specific sub-classification within EC 7 (7.6 vs 7.1, 7.2, etc.) would require additional knowledge about drug efflux specificity, but since only one EC 7 option is offered, identifying the ABC signature is sufficient to select D.",
    "The UniProt annotation uses ECO:0000305 (inferred from sequence or biological characteristics of related sequence), which is a computational/inference-level evidence code rather than direct experimental characterization of this exact protein.",
    "The entry was first released in 2025, so this is a relatively new annotation; the historical availability at the time of benchmark construction is uncertain."
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
  "benchmark_sequence_length": 316,
  "benchmark_sequence_sha256": "bfff69d1d7d031108e1c50bbb606696118d87057cab6e04b802323f2c0487534",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 316,
  "current_source_sequence_sha256": "bfff69d1d7d031108e1c50bbb606696118d87057cab6e04b802323f2c0487534",
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
  "requested_accession": "P0DXU7",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9",
  "selected_historical_source_sequence_length": 316,
  "selected_historical_source_sequence_sha256": "bfff69d1d7d031108e1c50bbb606696118d87057cab6e04b802323f2c0487534",
  "selected_historical_version": {
    "accession": "P0DXU7",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DRRA3_STRC4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXU7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:39.757107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:39.757107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces coeruleorubidus\",\"taxonId\":116188}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:39.757107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"value\":\"7.6.2.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Daunorubicin resistance ATP-binding protein DrrA3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:39.757107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:33148\"}}],\"reaction\":{\"ecNumber\":\"7.6.2.2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"name\":\"daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:33147\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64677\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:39.757107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Dong J.\",\"Ning J.\",\"Tian Y.\",\"Li H.\",\"Chen H.\",\"Guan W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39375957\"},{\"database\":\"DOI\",\"id\":\"10.1111/1751-7915.70023\"}],\"citationType\":\"journal article\",\"firstPage\":\"e70023\",\"id\":\"39375957\",\"journal\":\"Microb. Biotechnol.\",\"lastPage\":\"e70023\",\"publicationDate\":\"2024\",\"title\":\"The involvement of multiple ABC transporters in daunorubicin efflux in Streptomyces coeruleorubidus.\",\"volume\":\"17\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION IN DAUNORUBICIN EFFLUX\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:39.757107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   DRRA3_STRC4             Reviewed;         316 AA.\nAC   P0DXU7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA3 {ECO:0000305};\nDE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};\nGN   Name=drrA3 {ECO:0000303|PubMed:39375957};\nGN   ORFNames=R5U08_20725 {ECO:0000312|EMBL:WOT36399.1};\nOS   Streptomyces coeruleorubidus.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=116188;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:44.049376+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9",
  "url": "https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA3 {ECO:0000305};\nDE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:44.049376+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9",
  "url": "https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39375957; DOI=10.1111/1751-7915.70023;\nRA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;\nRT   \"The involvement of multiple ABC transporters in daunorubicin efflux in\nRT   Streptomyces coeruleorubidus.\";\nRL   Microb. Biotechnol. 17:e70023-e70023(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:44.049376+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9",
  "url": "https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP +\nCC         phosphate + H(+); Xref=Rhea:RHEA:33147, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:30616, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:64677, ChEBI:CHEBI:456216; EC=7.6.2.2;\nCC         Evidence={ECO:0000305|PubMed:39375957};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33148;\nCC         Evidence={ECO:0000305|PubMed:39375957};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:44.049376+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9",
  "url": "https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 115. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
