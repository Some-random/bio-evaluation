# GO_biological_process_0083: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_biological_process_0083.txt)

**Task:** `GO_biological_process`  
**Author key, unchanged:** **B** — saponin biosynthetic process

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MGSNTEATEIPKMPLKIVFLTLPIAGHMLHIVDTASTFAIHGVECTIITTPANVPFIEKSISATNTTIRQFLSIRLVDFPHEAVGLPPGVENFSAVTCPDMRPKISKGLSIIQKPTEDLIKEISPDCIVSDMFYPWTSDFALEIGVPRVVFRGCGMFPMCCWHSIKSHLPHEKVDRDDEMIVLPTLPDHIEMRKSTLPDWVRKPTGYSYLMKMIDAAELKSYGVIVNSFSDLERDYEEYFKNVTGLKVWTVGPISLHVGRNEELEGSDEWVKWLDGKKLDSVIYVSFGGVAKFPPHQLREIAAGLESSGHDFVWVVRASDENGDQAEADEWSLQKFKEKMKKTNHGLVIESWVPQLMFLEHKAIGGMLTHVGWGTMLEGITAGLPLVTWPLYAEQFYNERLVVDVLKIGVGVGVKEFCGLDDIGKKETIGRENIEASVRLVMGDGEEAAAMRLRVKELSEASMKAVREGGSSKANIHDFLNELSTLRSLRQA

[Multiple Choices]
A. negative regulation of RNA export from nucleus
B. saponin biosynthetic process
C. regulation of protein stability
D. biosynthetic process
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches a soapwort UDP-glucosyltransferase annotated to saponin biosynthesis; its cited function describes a role in that pathway, and the GO annotation has IDA evidence.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with an enzyme involved in biosynthesis, but sequence features alone do not identify its particular substrate or establish a role in saponin biosynthesis rather than another biosynthetic pathway.


**Missing item-specific fact**

> The protein-specific identification and functional evidence that this enzyme glycosylates a saponin-pathway intermediate.


**Reason**

> Distinguishing the specific saponin process from the broad biosynthetic choice requires item-specific functional annotation or experimental knowledge not supplied with the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Saponin biosynthesis is itself a biosynthetic process, so B is the specific choice while D is also true at a broader level. The wording does not require the most specific GO term.


### Important caveats

- The source and sequence match are established by reviewer-only evidence, not information provided to the evaluated model.
- The cited functional annotation is linked to experimental evidence (IDA), but the underlying primary study was not independently reviewed here.
- The exact author annotation snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with an enzyme involved in biosynthesis, but sequence features alone do not identify its particular substrate or establish a role in saponin biosynthesis rather than another biosynthetic pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification and functional evidence that this enzyme glycosylates a saponin-pathway intermediate.",
    "reason": "Distinguishing the specific saponin process from the broad biosynthetic choice requires item-specific functional annotation or experimental knowledge not supplied with the sequence."
  },
  "case_id": "GO_biological_process_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a soapwort UDP-glucosyltransferase annotated to saponin biosynthesis; its cited function describes a role in that pathway, and the GO annotation has IDA evidence."
  },
  "important_caveats": [
    "The source and sequence match are established by reviewer-only evidence, not information provided to the evaluated model.",
    "The cited functional annotation is linked to experimental evidence (IDA), but the underlying primary study was not independently reviewed here.",
    "The exact author annotation snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Saponin biosynthesis is itself a biosynthetic process, so B is the specific choice while D is also true at a broader level. The wording does not require the most specific GO term."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a soapwort UDP-glucosyltransferase annotated to saponin biosynthesis; its cited function describes a role in that pathway, and the GO annotation has IDA evidence.",
    "evidence_ids": ["C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with an enzyme involved in biosynthesis, but sequence features alone do not identify its particular substrate or establish a role in saponin biosynthesis rather than another biosynthetic pathway.",
    "missing_item_specific_fact": "The protein-specific identification and functional evidence that this enzyme glycosylates a saponin-pathway intermediate.",
    "reason": "Distinguishing the specific saponin process from the broad biosynthetic choice requires item-specific functional annotation or experimental knowledge not supplied with the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Saponin biosynthesis is itself a biosynthetic process, so B is the specific choice while D is also true at a broader level. The wording does not require the most specific GO term."
  },
  "important_caveats": [
    "The source and sequence match are established by reviewer-only evidence, not information provided to the evaluated model.",
    "The cited functional annotation is linked to experimental evidence (IDA), but the underlying primary study was not independently reviewed here.",
    "The exact author annotation snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0AAW1K8I9 (SoUGT73DL1, Saponaria officinalis) is annotated with GO:0016135 (P:saponin biosynthetic process) with IDA evidence from PubMed:39043959 (Nat. Chem. Biol. 2025). The FUNCTION comment explicitly states it is a 'Component of the oleanane-type triterpene saponins biosynthetic pathway' mediating galactosylation of the C-3 sugar chain. The sequence matches the UniProt record exactly (SHA-256 confirmed).

Citations as saved: [C7](#evidence-c7), [C5](#evidence-c5), [H5](#evidence-h5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General reasoning from the sequence can identify this as a plant UDP-glycosyltransferase (PSPG motif, ~492 aa, plant UGT architecture), which eliminates A (RNA export) and C (protein stability regulation) as mechanistically incompatible. It also supports involvement in some biosynthetic process (favoring D over A/C). However, distinguishing the specific GO term 'saponin biosynthetic process' (B) from the generic ancestor 'biosynthetic process' (D) requires knowing this particular UGT's substrate specificity—namely, that it glycosylates triterpenoid (oleanane-type) aglycones rather than flavonoids, phenolics, or other acceptors common to the broad UGT superfamily.


**Missing item-specific fact**

> The experimental demonstration (PubMed:39043959) that SoUGT73DL1 specifically catalyzes QA-mono to QA-di galactosylation in the oleanane-type saponin pathway. Without this protein-specific substrate assignment, the sequence alone cannot distinguish saponin biosynthesis from other glycosyltransferase-dependent biosynthetic routes (flavonoid, phenolic, or steroid glycosylation) that would also fall under 'biosynthetic process.'


**Reason**

> While the glycosyltransferase identity and plant origin are inferable from sequence features, the precise GO term 'saponin biosynthetic process' depends on the experimentally determined substrate (triterpenoid aglycone) documented in a 2025 publication. A model could reason to 'biosynthetic process' (D) from the UGT activity but cannot uniquely arrive at 'saponin' without memorizing this specific UGT's characterization or recognizing the exact sequence as a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> GO:0016135 (saponin biosynthetic process) is an is_a descendant of GO:0009058 (biosynthetic process) via the path GO:0016135→GO:0016138→GO:1901659→GO:1901137→GO:0009058. Thus D is technically true as a broader ancestor. In standard GO annotation practice the most specific term is preferred, and the question asks for the 'primary biological process,' which favors B. However, without the specific substrate information, a model reasoning only from sequence features (glycosyltransferase → biosynthesis) could defensibly select D. GO:0009058 is flagged 'gocheck_do_not_annotate' in the ontology, which in practice disqualifies it as a primary annotation, but this convention is not stated in the question prompt.


### Important caveats

- The GO annotation for this entry was first published in 2025 (PubMed:39043959); the benchmark author's source snapshot date is unknown. If the benchmark was constructed before this entry existed in UniProt, the annotation may have been derived from a different source or pipeline.
- The protein is also annotated with GO:0016104 (triterpenoid biosynthetic process, IDA), which is a sibling of GO:0016135 under GO:0016114 (terpenoid biosynthetic process). Neither appears as a distractor, so this does not affect the B-vs-D distinction.
- The 'gocheck_do_not_annotate' subset flag on GO:0009058 is an internal curation convention; a model unaware of this convention might still consider D a valid broader answer.
- Sequence identity to UniProt A0AAW1K8I9 is confirmed (SHA-256 match), so the annotation applies directly to the supplied sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General reasoning from the sequence can identify this as a plant UDP-glycosyltransferase (PSPG motif, ~492 aa, plant UGT architecture), which eliminates A (RNA export) and C (protein stability regulation) as mechanistically incompatible. It also supports involvement in some biosynthetic process (favoring D over A/C). However, distinguishing the specific GO term 'saponin biosynthetic process' (B) from the generic ancestor 'biosynthetic process' (D) requires knowing this particular UGT's substrate specificity—namely, that it glycosylates triterpenoid (oleanane-type) aglycones rather than flavonoids, phenolics, or other acceptors common to the broad UGT superfamily.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimental demonstration (PubMed:39043959) that SoUGT73DL1 specifically catalyzes QA-mono to QA-di galactosylation in the oleanane-type saponin pathway. Without this protein-specific substrate assignment, the sequence alone cannot distinguish saponin biosynthesis from other glycosyltransferase-dependent biosynthetic routes (flavonoid, phenolic, or steroid glycosylation) that would also fall under 'biosynthetic process.'",
    "reason": "While the glycosyltransferase identity and plant origin are inferable from sequence features, the precise GO term 'saponin biosynthetic process' depends on the experimentally determined substrate (triterpenoid aglycone) documented in a 2025 publication. A model could reason to 'biosynthetic process' (D) from the UGT activity but cannot uniquely arrive at 'saponin' without memorizing this specific UGT's characterization or recognizing the exact sequence as a database entry."
  },
  "case_id": "GO_biological_process_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C5",
      "H5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1K8I9 (SoUGT73DL1, Saponaria officinalis) is annotated with GO:0016135 (P:saponin biosynthetic process) with IDA evidence from PubMed:39043959 (Nat. Chem. Biol. 2025). The FUNCTION comment explicitly states it is a 'Component of the oleanane-type triterpene saponins biosynthetic pathway' mediating galactosylation of the C-3 sugar chain. The sequence matches the UniProt record exactly (SHA-256 confirmed)."
  },
  "important_caveats": [
    "The GO annotation for this entry was first published in 2025 (PubMed:39043959); the benchmark author's source snapshot date is unknown. If the benchmark was constructed before this entry existed in UniProt, the annotation may have been derived from a different source or pipeline.",
    "The protein is also annotated with GO:0016104 (triterpenoid biosynthetic process, IDA), which is a sibling of GO:0016135 under GO:0016114 (terpenoid biosynthetic process). Neither appears as a distractor, so this does not affect the B-vs-D distinction.",
    "The 'gocheck_do_not_annotate' subset flag on GO:0009058 is an internal curation convention; a model unaware of this convention might still consider D a valid broader answer.",
    "Sequence identity to UniProt A0AAW1K8I9 is confirmed (SHA-256 match), so the annotation applies directly to the supplied sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "GO:0016135 (saponin biosynthetic process) is an is_a descendant of GO:0009058 (biosynthetic process) via the path GO:0016135→GO:0016138→GO:1901659→GO:1901137→GO:0009058. Thus D is technically true as a broader ancestor. In standard GO annotation practice the most specific term is preferred, and the question asks for the 'primary biological process,' which favors B. However, without the specific substrate information, a model reasoning only from sequence features (glycosyltransferase → biosynthesis) could defensibly select D. GO:0009058 is flagged 'gocheck_do_not_annotate' in the ontology, which in practice disqualifies it as a primary annotation, but this convention is not stated in the question prompt."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0AAW1K8I9 (SoUGT73DL1, Saponaria officinalis) is annotated with GO:0016135 (P:saponin biosynthetic process) with IDA evidence from PubMed:39043959 (Nat. Chem. Biol. 2025). The FUNCTION comment explicitly states it is a 'Component of the oleanane-type triterpene saponins biosynthetic pathway' mediating galactosylation of the C-3 sugar chain. The sequence matches the UniProt record exactly (SHA-256 confirmed).",
    "evidence_ids": ["C7", "C5", "H5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General reasoning from the sequence can identify this as a plant UDP-glycosyltransferase (PSPG motif, ~492 aa, plant UGT architecture), which eliminates A (RNA export) and C (protein stability regulation) as mechanistically incompatible. It also supports involvement in some biosynthetic process (favoring D over A/C). However, distinguishing the specific GO term 'saponin biosynthetic process' (B) from the generic ancestor 'biosynthetic process' (D) requires knowing this particular UGT's substrate specificity—namely, that it glycosylates triterpenoid (oleanane-type) aglycones rather than flavonoids, phenolics, or other acceptors common to the broad UGT superfamily.",
    "missing_item_specific_fact": "The experimental demonstration (PubMed:39043959) that SoUGT73DL1 specifically catalyzes QA-mono to QA-di galactosylation in the oleanane-type saponin pathway. Without this protein-specific substrate assignment, the sequence alone cannot distinguish saponin biosynthesis from other glycosyltransferase-dependent biosynthetic routes (flavonoid, phenolic, or steroid glycosylation) that would also fall under 'biosynthetic process.'",
    "reason": "While the glycosyltransferase identity and plant origin are inferable from sequence features, the precise GO term 'saponin biosynthetic process' depends on the experimentally determined substrate (triterpenoid aglycone) documented in a 2025 publication. A model could reason to 'biosynthetic process' (D) from the UGT activity but cannot uniquely arrive at 'saponin' without memorizing this specific UGT's characterization or recognizing the exact sequence as a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "GO:0016135 (saponin biosynthetic process) is an is_a descendant of GO:0009058 (biosynthetic process) via the path GO:0016135→GO:0016138→GO:1901659→GO:1901137→GO:0009058. Thus D is technically true as a broader ancestor. In standard GO annotation practice the most specific term is preferred, and the question asks for the 'primary biological process,' which favors B. However, without the specific substrate information, a model reasoning only from sequence features (glycosyltransferase → biosynthesis) could defensibly select D. GO:0009058 is flagged 'gocheck_do_not_annotate' in the ontology, which in practice disqualifies it as a primary annotation, but this convention is not stated in the question prompt."
  },
  "important_caveats": [
    "The GO annotation for this entry was first published in 2025 (PubMed:39043959); the benchmark author's source snapshot date is unknown. If the benchmark was constructed before this entry existed in UniProt, the annotation may have been derived from a different source or pipeline.",
    "The protein is also annotated with GO:0016104 (triterpenoid biosynthetic process, IDA), which is a sibling of GO:0016135 under GO:0016114 (terpenoid biosynthetic process). Neither appears as a distractor, so this does not affect the B-vs-D distinction.",
    "The 'gocheck_do_not_annotate' subset flag on GO:0009058 is an internal curation convention; a model unaware of this convention might still consider D a valid broader answer.",
    "Sequence identity to UniProt A0AAW1K8I9 is confirmed (SHA-256 match), so the annotation applies directly to the supplied sequence."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched record reports this protein in saponin biosynthesis and describes experimental evidence for its role as a glycosyltransferase in that pathway. This supports B; D is a broader parent process.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The particular substrate and pathway specificity of this enzyme—specifically, that it catalyzes a glycosylation step in saponin biosynthesis—is not established by the sequence’s general glycosyltransferase features.


**Reason**

> A plant UDP-dependent glycosyltransferase sequence can support a broad inference of glycosylation and biosynthesis, making B more plausible than the unrelated choices A and C. But such enzymes act on diverse substrates, so transferable family knowledge alone does not meaningfully distinguish saponin biosynthesis (B) from the broader biosynthetic process (D).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D broadly encompasses B, but the wording asks for the best description of the overall process, for which the more specific saponin biosynthetic process is preferable.


### Important caveats

- The supplied sequence does not itself identify the protein’s organism or its experimentally established substrate specificity.
- The reviewer-only source evidence supports the key but was not available as input for the answerability judgment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The particular substrate and pathway specificity of this enzyme—specifically, that it catalyzes a glycosylation step in saponin biosynthesis—is not established by the sequence’s general glycosyltransferase features.",
    "reason": "A plant UDP-dependent glycosyltransferase sequence can support a broad inference of glycosylation and biosynthesis, making B more plausible than the unrelated choices A and C. But such enzymes act on diverse substrates, so transferable family knowledge alone does not meaningfully distinguish saponin biosynthesis (B) from the broader biosynthetic process (D)."
  },
  "case_id": "GO_biological_process_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record reports this protein in saponin biosynthesis and describes experimental evidence for its role as a glycosyltransferase in that pathway. This supports B; D is a broader parent process."
  },
  "important_caveats": [
    "The supplied sequence does not itself identify the protein’s organism or its experimentally established substrate specificity.",
    "The reviewer-only source evidence supports the key but was not available as input for the answerability judgment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D broadly encompasses B, but the wording asks for the best description of the overall process, for which the more specific saponin biosynthetic process is preferable."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record reports this protein in saponin biosynthesis and describes experimental evidence for its role as a glycosyltransferase in that pathway. This supports B; D is a broader parent process.",
    "evidence_ids": ["C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The particular substrate and pathway specificity of this enzyme—specifically, that it catalyzes a glycosylation step in saponin biosynthesis—is not established by the sequence’s general glycosyltransferase features.",
    "reason": "A plant UDP-dependent glycosyltransferase sequence can support a broad inference of glycosylation and biosynthesis, making B more plausible than the unrelated choices A and C. But such enzymes act on diverse substrates, so transferable family knowledge alone does not meaningfully distinguish saponin biosynthesis (B) from the broader biosynthetic process (D)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D broadly encompasses B, but the wording asks for the best description of the overall process, for which the more specific saponin biosynthetic process is preferable."
  },
  "important_caveats": [
    "The supplied sequence does not itself identify the protein’s organism or its experimentally established substrate specificity.",
    "The reviewer-only source evidence supports the key but was not available as input for the answerability judgment."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1K8I9 annotates this protein with GO:0016135 'saponin biosynthetic process' with IDA evidence (Inferred from Direct Assay, PubMed:39043959). The function comment explicitly states it is a 'Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway' and a glycosyltransferase mediating QA-mono to QA-di conversion. The pathway comment confirms 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' The experimental evidence (ECO:0000269) from the Osbourn group's Nat. Chem. Biol. 2025 paper directly supports the saponin biosynthetic role.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 492-aa sequence contains the characteristic C-terminal PSPG (Plant Secondary Product Glycosyltransferase) motif region (visible in the 'GTMLEGITAGLPLVTWPLYAEQFYNERLVVDVLKIGVGVGVKEFCGLDDIG' stretch) and the overall architecture of a plant UDP-glycosyltransferase. This immediately eliminates A (RNA export regulation) and C (protein stability regulation), as glycosyltransferases are not involved in nucleocytoplasmic transport or proteostasis. Between B and D: D ('biosynthetic process') is the GO ancestor of B (saponin biosynthetic process → glycoside biosynthetic process → glycosyl compound biosynthetic process → carbohydrate derivative biosynthetic process → biosynthetic process). The question asks for the 'primary biological process' and 'overall biological objective,' which in GO convention means the most specific applicable term. Transferable family knowledge: UGT73 sub-family members in Caryophyllales and related lineages (e.g., Medicago UGT73C6 for triterpene saponins, Quinoa UGT73 members for quillaic-acid saponins) are predominantly saponin/triterpenoid glycosyltransferases. A knowledgeable model recognizing the UGT73-like architecture can infer saponin/triterpenoid glycosylation as the likely specific biological objective rather than generic 'biosynthesis,' especially since the UGT73 family's best-characterized members in this taxonomic context are saponin biosynthetic enzymes. The specific '73DL1' sub-family designation and sequence length (492 aa) are consistent with known saponin UGTs.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can identify the protein as a plant UGT from the PSPG motif and architecture, eliminate A and C as incompatible with glycosyltransferase function, and use UGT73-family knowledge (learned from homologs in Medicago, Quinoa, and other Caryophyllales) to infer saponin/triterpenoid glycosylation as the specific biological objective. The B-vs-D distinction is resolved by the question's phrasing ('primary biological process,' 'overall biological objective') which calls for the most specific applicable GO term rather than its ancestor.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While D (biosynthetic process) is a GO ancestor of B (saponin biosynthetic process) and is technically true, the question explicitly asks for the 'primary biological process' and 'overall biological objective,' which in GO annotation convention selects the most specific applicable term. A and C are clearly incompatible with a glycosyltransferase. No genuine ambiguity remains among the offered choices.


### Important caveats

- The specific identification of 'saponin' (rather than flavonoid, phenolic, or other glycosylated secondary metabolite) relies on UGT73-family-level knowledge rather than a unique sequence signature exclusive to saponin UGTs. Plant UGTs glycosylate diverse substrates, and the UGT73 family is not exclusively saponin-specific across all plant lineages.
- The entry was first publicly released in June 2025; the benchmark construction date is unknown. If the benchmark predates the UniProt entry, the annotation source may differ.
- The GO annotation uses IDA (Inferred from Direct Assay) evidence, indicating experimental validation of saponin biosynthetic function, not merely computational prediction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 492-aa sequence contains the characteristic C-terminal PSPG (Plant Secondary Product Glycosyltransferase) motif region (visible in the 'GTMLEGITAGLPLVTWPLYAEQFYNERLVVDVLKIGVGVGVKEFCGLDDIG' stretch) and the overall architecture of a plant UDP-glycosyltransferase. This immediately eliminates A (RNA export regulation) and C (protein stability regulation), as glycosyltransferases are not involved in nucleocytoplasmic transport or proteostasis. Between B and D: D ('biosynthetic process') is the GO ancestor of B (saponin biosynthetic process → glycoside biosynthetic process → glycosyl compound biosynthetic process → carbohydrate derivative biosynthetic process → biosynthetic process). The question asks for the 'primary biological process' and 'overall biological objective,' which in GO convention means the most specific applicable term. Transferable family knowledge: UGT73 sub-family members in Caryophyllales and related lineages (e.g., Medicago UGT73C6 for triterpene saponins, Quinoa UGT73 members for quillaic-acid saponins) are predominantly saponin/triterpenoid glycosyltransferases. A knowledgeable model recognizing the UGT73-like architecture can infer saponin/triterpenoid glycosylation as the likely specific biological objective rather than generic 'biosynthesis,' especially since the UGT73 family's best-characterized members in this taxonomic context are saponin biosynthetic enzymes. The specific '73DL1' sub-family designation and sequence length (492 aa) are consistent with known saponin UGTs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can identify the protein as a plant UGT from the PSPG motif and architecture, eliminate A and C as incompatible with glycosyltransferase function, and use UGT73-family knowledge (learned from homologs in Medicago, Quinoa, and other Caryophyllales) to infer saponin/triterpenoid glycosylation as the specific biological objective. The B-vs-D distinction is resolved by the question's phrasing ('primary biological process,' 'overall biological objective') which calls for the most specific applicable GO term rather than its ancestor."
  },
  "case_id": "GO_biological_process_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1K8I9 annotates this protein with GO:0016135 'saponin biosynthetic process' with IDA evidence (Inferred from Direct Assay, PubMed:39043959). The function comment explicitly states it is a 'Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway' and a glycosyltransferase mediating QA-mono to QA-di conversion. The pathway comment confirms 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' The experimental evidence (ECO:0000269) from the Osbourn group's Nat. Chem. Biol. 2025 paper directly supports the saponin biosynthetic role."
  },
  "important_caveats": [
    "The specific identification of 'saponin' (rather than flavonoid, phenolic, or other glycosylated secondary metabolite) relies on UGT73-family-level knowledge rather than a unique sequence signature exclusive to saponin UGTs. Plant UGTs glycosylate diverse substrates, and the UGT73 family is not exclusively saponin-specific across all plant lineages.",
    "The entry was first publicly released in June 2025; the benchmark construction date is unknown. If the benchmark predates the UniProt entry, the annotation source may differ.",
    "The GO annotation uses IDA (Inferred from Direct Assay) evidence, indicating experimental validation of saponin biosynthetic function, not merely computational prediction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While D (biosynthetic process) is a GO ancestor of B (saponin biosynthetic process) and is technically true, the question explicitly asks for the 'primary biological process' and 'overall biological objective,' which in GO annotation convention selects the most specific applicable term. A and C are clearly incompatible with a glycosyltransferase. No genuine ambiguity remains among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1K8I9 annotates this protein with GO:0016135 'saponin biosynthetic process' with IDA evidence (Inferred from Direct Assay, PubMed:39043959). The function comment explicitly states it is a 'Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway' and a glycosyltransferase mediating QA-mono to QA-di conversion. The pathway comment confirms 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' The experimental evidence (ECO:0000269) from the Osbourn group's Nat. Chem. Biol. 2025 paper directly supports the saponin biosynthetic role.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 492-aa sequence contains the characteristic C-terminal PSPG (Plant Secondary Product Glycosyltransferase) motif region (visible in the 'GTMLEGITAGLPLVTWPLYAEQFYNERLVVDVLKIGVGVGVKEFCGLDDIG' stretch) and the overall architecture of a plant UDP-glycosyltransferase. This immediately eliminates A (RNA export regulation) and C (protein stability regulation), as glycosyltransferases are not involved in nucleocytoplasmic transport or proteostasis. Between B and D: D ('biosynthetic process') is the GO ancestor of B (saponin biosynthetic process → glycoside biosynthetic process → glycosyl compound biosynthetic process → carbohydrate derivative biosynthetic process → biosynthetic process). The question asks for the 'primary biological process' and 'overall biological objective,' which in GO convention means the most specific applicable term. Transferable family knowledge: UGT73 sub-family members in Caryophyllales and related lineages (e.g., Medicago UGT73C6 for triterpene saponins, Quinoa UGT73 members for quillaic-acid saponins) are predominantly saponin/triterpenoid glycosyltransferases. A knowledgeable model recognizing the UGT73-like architecture can infer saponin/triterpenoid glycosylation as the likely specific biological objective rather than generic 'biosynthesis,' especially since the UGT73 family's best-characterized members in this taxonomic context are saponin biosynthetic enzymes. The specific '73DL1' sub-family designation and sequence length (492 aa) are consistent with known saponin UGTs.",
    "missing_item_specific_fact": "",
    "reason": "A model can identify the protein as a plant UGT from the PSPG motif and architecture, eliminate A and C as incompatible with glycosyltransferase function, and use UGT73-family knowledge (learned from homologs in Medicago, Quinoa, and other Caryophyllales) to infer saponin/triterpenoid glycosylation as the specific biological objective. The B-vs-D distinction is resolved by the question's phrasing ('primary biological process,' 'overall biological objective') which calls for the most specific applicable GO term rather than its ancestor."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While D (biosynthetic process) is a GO ancestor of B (saponin biosynthetic process) and is technically true, the question explicitly asks for the 'primary biological process' and 'overall biological objective,' which in GO annotation convention selects the most specific applicable term. A and C are clearly incompatible with a glycosyltransferase. No genuine ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "The specific identification of 'saponin' (rather than flavonoid, phenolic, or other glycosylated secondary metabolite) relies on UGT73-family-level knowledge rather than a unique sequence signature exclusive to saponin UGTs. Plant UGTs glycosylate diverse substrates, and the UGT73 family is not exclusively saponin-specific across all plant lineages.",
    "The entry was first publicly released in June 2025; the benchmark construction date is unknown. If the benchmark predates the UniProt entry, the annotation source may differ.",
    "The GO annotation uses IDA (Inferred from Direct Assay) evidence, indicating experimental validation of saponin biosynthetic function, not merely computational prediction."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "A0AAW1K8I9",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "d01f6d4dbabab508bd73d7aac406c04cbfe1649f32055ff6cc318b8c504ba6c3",
  "benchmark_sequence_length": 492,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "current_source_sequence_sha256": "d01f6d4dbabab508bd73d7aac406c04cbfe1649f32055ff6cc318b8c504ba6c3",
  "current_source_sequence_length": 492,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 5,
  "selected_historical_version": {
    "accession": "A0AAW1K8I9",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GT731_SAPOF",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "selected_historical_source_sequence_sha256": "d01f6d4dbabab508bd73d7aac406c04cbfe1649f32055ff6cc318b8c504ba6c3",
  "selected_historical_source_sequence_length": 492,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0AAW1K8I9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"UDP-glucosyl transferase 73DL1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoUGT73DL1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). A glycosyltransferase that mediates the conversion of QA-mono to QA-di via the elongation of the C-3 sugar chain with a D-galactose (PubMed:39043959)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "json_pointer": "/uniProtKBCrossReferences/8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"id\":\"GO:0016135\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:saponin biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"id\":\"GO:0016104\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:triterpenoid biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1K8I9.json",
  "source_sha256": "ff1d8de511ec47cbdc506fa8efe725b56c63c42715b9a2962823c3dd7244ffa7",
  "retrieved_utc": "2026-11-02T04:26:36.683131+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48158.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   GT731_SAPOF             Reviewed;         492 AA.\nAC   A0AAW1K8I9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=UDP-glucosyl transferase 73DL1 {ECO:0000303|PubMed:39043959};\nDE            Short=SoUGT73DL1 {ECO:0000303|PubMed:39043959};\nDE            EC=2.4.1.- {ECO:0000269|PubMed:39043959};\nGN   Name=UGT73DL1 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11029895m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_06G065500 {ECO:0000312|EMBL:KAK9714013.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "source_locator": "lines 17-26",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48158.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "source_locator": "lines 34-40",
  "excerpt": "CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.\nCC       saponarioside A and saponarioside B) biosynthetic pathway, leading to\nCC       the production of natural products with detergent properties used as\nCC       traditional sources of soap (PubMed:39043959). A glycosyltransferase\nCC       that mediates the conversion of QA-mono to QA-di via the elongation of\nCC       the C-3 sugar chain with a D-galactose (PubMed:39043959).\nCC       {ECO:0000269|PubMed:39043959}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "source_locator": "lines 49-50",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\nCC       {ECO:0000269|PubMed:39043959}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "source_locator": "lines 70-70",
  "excerpt": "DR   GO; GO:0016135; P:saponin biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0AAW1K8I9?format=txt&versions=5",
  "source_sha256": "46eff2d1174436813e2d0276cab6804ed02e27cf24990709a857ea963a1c34bb",
  "retrieved_utc": "2026-11-02T04:26:40.747220+00:00",
  "source_locator": "lines 71-71",
  "excerpt": "DR   GO; GO:0016104; P:triterpenoid biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 5,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 81762-81782",
  "excerpt": "[Term]\nid: GO:0008299\nname: isoprenoid biosynthetic process\nnamespace: biological_process\nalt_id: GO:0009241\ndef: \"The chemical reactions and pathways resulting in the formation of an isoprenoid compound, isoprene (2-methylbuta-1,3-diene) or compounds containing or derived from linked isoprene (3-methyl-2-butenylene) residues.\" [ISBN:0198506732]\nsynonym: \"isoprenoid anabolism\" EXACT []\nsynonym: \"isoprenoid biosynthesis\" EXACT []\nsynonym: \"isoprenoid formation\" EXACT []\nsynonym: \"isoprenoid synthesis\" EXACT []\nsynonym: \"polyisoprenoid anabolism\" NARROW []\nsynonym: \"polyisoprenoid biosynthesis\" NARROW []\nsynonym: \"polyisoprenoid biosynthetic process\" NARROW []\nsynonym: \"polyisoprenoid formation\" NARROW []\nsynonym: \"polyisoprenoid synthesis\" NARROW []\nsynonym: \"polyterpene biosynthesis\" NARROW []\nsynonym: \"polyterpene biosynthetic process\" NARROW []\nxref: MetaCyc:POLYISOPRENSYN-PWY\nis_a: GO:0006720 ! isoprenoid metabolic process\nis_a: GO:0008610 ! lipid biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0008299"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 85448-85460",
  "excerpt": "[Term]\nid: GO:0008610\nname: lipid biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of lipids, compounds soluble in an organic solvent but not, or sparingly, in an aqueous solvent.\" [GOC:curators]\nsynonym: \"lipid anabolism\" EXACT []\nsynonym: \"lipid biosynthesis\" EXACT []\nsynonym: \"lipid formation\" EXACT []\nsynonym: \"lipid synthesis\" EXACT []\nsynonym: \"lipogenesis\" EXACT [GOC:sl]\nis_a: GO:0006629 ! lipid metabolic process\nis_a: GO:0009058 ! biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0008610"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 92248-92268",
  "excerpt": "[Term]\nid: GO:0009058\nname: biosynthetic process\nnamespace: biological_process\nalt_id: GO:0044274\nalt_id: GO:0044711\ndef: \"A cellular process consisting of the biochemical pathways by which a living organism synthesizes chemical substances. This typically represents the energy-requiring part of metabolism in which simpler substances are transformed into more complex ones.\" [GOC:curators, ISBN:0198547684]\nsubset: gocheck_do_not_annotate\nsubset: goslim_chembl\nsubset: goslim_metagenomics\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsynonym: \"anabolism\" EXACT []\nsynonym: \"biosynthesis\" EXACT []\nsynonym: \"formation\" BROAD []\nsynonym: \"multicellular organismal biosynthetic process\" NARROW []\nsynonym: \"single-organism biosynthetic process\" RELATED []\nsynonym: \"synthesis\" EXACT []\nxref: Wikipedia:Anabolism\nis_a: GO:0008152 ! metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0009058"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 123487-123500",
  "excerpt": "[Term]\nid: GO:0016104\nname: triterpenoid biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of triterpenoid compounds, terpenoids with six isoprene units.\" [GOC:curators]\nsynonym: \"triterpene biosynthesis\" NARROW []\nsynonym: \"triterpene biosynthetic process\" NARROW []\nsynonym: \"triterpenoid anabolism\" EXACT []\nsynonym: \"triterpenoid biosynthesis\" EXACT []\nsynonym: \"triterpenoid formation\" EXACT []\nsynonym: \"triterpenoid synthesis\" EXACT []\nis_a: GO:0006722 ! triterpenoid metabolic process\nis_a: GO:0016114 ! terpenoid biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0016104"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 123609-123621",
  "excerpt": "[Term]\nid: GO:0016114\nname: terpenoid biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of terpenoids, any member of a class of compounds characterized by an isoprenoid chemical structure.\" [GOC:ai]\nsynonym: \"terpenoid anabolism\" EXACT []\nsynonym: \"terpenoid biosynthesis\" EXACT []\nsynonym: \"terpenoid formation\" EXACT []\nsynonym: \"terpenoid synthesis\" EXACT []\nxref: Wikipedia:Terpenoid\nis_a: GO:0006721 ! terpenoid metabolic process\nis_a: GO:0008299 ! isoprenoid biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0016114"
}
```

### Evidence GO6

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO6",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 123836-123847",
  "excerpt": "[Term]\nid: GO:0016135\nname: saponin biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of saponins, glycosides of plants in which the aglycan (sapogenin) group is a terpene or steroid and the sugar group is a glucose, a galactose, a pentose, a methylpentose or an oligosaccharide. Saponins are powerful surfactant agents and membrane active; they are, hence, toxic to animals on injection.\" [GOC:curators]\nsynonym: \"saponin anabolism\" EXACT []\nsynonym: \"saponin biosynthesis\" EXACT []\nsynonym: \"saponin formation\" EXACT []\nsynonym: \"saponin synthesis\" EXACT []\nis_a: GO:0016134 ! saponin metabolic process\nis_a: GO:0016138 ! glycoside biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0016135"
}
```

### Evidence GO7

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO7",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 123870-123887",
  "excerpt": "[Term]\nid: GO:0016138\nname: glycoside biosynthetic process\nnamespace: biological_process\nalt_id: GO:0016141\ndef: \"The chemical reactions and pathways resulting in the formation of glycosides, compounds in which a glycosyl group is substituted into a hydroxyl, thiol or selenol group in another compound.\" [GOC:curators]\nsynonym: \"glycoside anabolism\" EXACT []\nsynonym: \"glycoside biosynthesis\" EXACT []\nsynonym: \"glycoside formation\" EXACT []\nsynonym: \"glycoside synthesis\" EXACT []\nsynonym: \"O-glycoside anabolism\" EXACT []\nsynonym: \"O-glycoside biosynthesis\" EXACT []\nsynonym: \"O-glycoside biosynthetic process\" EXACT []\nsynonym: \"O-glycoside formation\" EXACT []\nsynonym: \"O-glycoside synthesis\" EXACT []\nis_a: GO:0016137 ! glycoside metabolic process\nis_a: GO:1901659 ! glycosyl compound biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0016138"
}
```

### Evidence GO8

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO8",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 178643-178650",
  "excerpt": "[Term]\nid: GO:0031647\nname: regulation of protein stability\nnamespace: biological_process\ndef: \"Any process that affects the structure and integrity of a protein, altering the likelihood of its degradation or aggregation.\" [GOC:dph, GOC:mah, GOC:tb]\nsubset: goslim_pir\nis_a: GO:0065008 ! regulation of biological quality\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0031647"
}
```

### Evidence GO9

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO9",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 280910-280927",
  "excerpt": "[Term]\nid: GO:0046832\nname: negative regulation of RNA export from nucleus\nnamespace: biological_process\ndef: \"Any process that stops, prevents, or reduces the frequency, rate or extent of the directed movement of RNA from the nucleus into the cytoplasm.\" [GOC:bf]\nsynonym: \"down regulation of RNA export from nucleus\" EXACT []\nsynonym: \"down-regulation of RNA export from nucleus\" EXACT []\nsynonym: \"downregulation of RNA export from nucleus\" EXACT []\nsynonym: \"inhibition of RNA export from nucleus\" NARROW []\nsynonym: \"negative regulation of RNA export from cell nucleus\" EXACT []\nsynonym: \"negative regulation of RNA export out of nucleus\" EXACT []\nsynonym: \"negative regulation of RNA transport from nucleus to cytoplasm\" EXACT []\nsynonym: \"negative regulation of RNA-nucleus export\" EXACT []\nis_a: GO:0032240 ! negative regulation of nucleobase-containing compound transport\nis_a: GO:0046823 ! negative regulation of nucleocytoplasmic transport\nis_a: GO:0046831 ! regulation of RNA export from nucleus\nrelationship: negatively_regulates GO:0006405 ! RNA export from nucleus\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0046832"
}
```

### Evidence GO10

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO10",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 471797-471808",
  "excerpt": "[Term]\nid: GO:1901137\nname: carbohydrate derivative biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of carbohydrate derivative.\" [GOC:TermGenie]\nsynonym: \"carbohydrate derivative anabolism\" EXACT [GOC:TermGenie]\nsynonym: \"carbohydrate derivative biosynthesis\" EXACT [GOC:TermGenie]\nsynonym: \"carbohydrate derivative formation\" EXACT [GOC:TermGenie]\nsynonym: \"carbohydrate derivative synthesis\" EXACT [GOC:TermGenie]\nis_a: GO:0009058 ! biosynthetic process\nis_a: GO:1901135 ! carbohydrate derivative metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:1901137"
}
```

### Evidence GO11

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO11",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 479374-479384",
  "excerpt": "[Term]\nid: GO:1901659\nname: glycosyl compound biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of glycosyl compound.\" [GOC:pr, GOC:TermGenie]\nsynonym: \"glycosyl compound anabolism\" EXACT [GOC:TermGenie]\nsynonym: \"glycosyl compound biosynthesis\" EXACT [GOC:TermGenie]\nsynonym: \"glycosyl compound formation\" EXACT [GOC:TermGenie]\nsynonym: \"glycosyl compound synthesis\" EXACT [GOC:TermGenie]\nis_a: GO:1901137 ! carbohydrate derivative biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:1901659"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 83. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
