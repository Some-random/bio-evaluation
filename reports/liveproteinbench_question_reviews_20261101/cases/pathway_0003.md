# pathway_0003

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Antibiotic biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTTTSASTTDHLIDQQVIDGQAGYTKSFLNIYDLAVFKGTAPLAWHCSPAVSRQMYDTCLGANHVEIGVGTGYLLDNATFPVADPKITLVDLNPNSLAHTAQRLNRYDVTTVRANVLEPLPLEERAYDSVGMSYLLHCVPGSIKEKGIALKHAAAVVRPGGVVFGATVLSSGVPVSARGRWTMNYLNKRGDFHNQEDNYDDLRDQLAQYFPRFQLTSRGCVGIWRAWTTD

[Multiple Choices]
A. coenzyme A biosynthesis
B. Antibiotic biosynthesis. .
C. Glycolipid biosynthesis
D. LPS O-antigen biosynthesis. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence exactly matches the UniProt sequence annotated as demethylluteothin O-methyltransferase, with the pathway listed as antibiotic biosynthesis. The annotation cites relevant publications, though its pathway evidence code is curator inference rather than a direct experimental evidence code.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme, but no feature in the supplied sequence or context meaningfully distinguishes an antibiotic-biosynthesis role from the other listed pathways without identifying its specific function.


**Missing item-specific fact**

> That this sequence encodes demethylluteothin O-methyltransferase involved in antibiotic biosynthesis.


**Reason**

> The pathway assignment depends on protein-specific functional annotation or recognition of the exact sequence, neither of which is provided. General sequence-based reasoning does not establish the pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the annotated role, antibiotic biosynthesis is the fitting listed choice; the alternatives are not comparably supported.


### Important caveats

- The reviewer-only UniProt records match the submitted sequence, but were not available to the evaluated model.
- The pathway annotation is curator-assigned and cites relevant publications; the supplied evidence does not independently validate those primary studies.
- Polyketide biosynthesis is also annotated for this protein, but is not one of the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but no feature in the supplied sequence or context meaningfully distinguishes an antibiotic-biosynthesis role from the other listed pathways without identifying its specific function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence encodes demethylluteothin O-methyltransferase involved in antibiotic biosynthesis.",
    "reason": "The pathway assignment depends on protein-specific functional annotation or recognition of the exact sequence, neither of which is provided. General sequence-based reasoning does not establish the pathway."
  },
  "case_id": "pathway_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as demethylluteothin O-methyltransferase, with the pathway listed as antibiotic biosynthesis. The annotation cites relevant publications, though its pathway evidence code is curator inference rather than a direct experimental evidence code."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the submitted sequence, but were not available to the evaluated model.",
    "The pathway annotation is curator-assigned and cites relevant publications; the supplied evidence does not independently validate those primary studies.",
    "Polyketide biosynthesis is also annotated for this protein, but is not one of the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the annotated role, antibiotic biosynthesis is the fitting listed choice; the alternatives are not comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt sequence annotated as demethylluteothin O-methyltransferase, with the pathway listed as antibiotic biosynthesis. The annotation cites relevant publications, though its pathway evidence code is curator inference rather than a direct experimental evidence code.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme, but no feature in the supplied sequence or context meaningfully distinguishes an antibiotic-biosynthesis role from the other listed pathways without identifying its specific function.",
    "missing_item_specific_fact": "That this sequence encodes demethylluteothin O-methyltransferase involved in antibiotic biosynthesis.",
    "reason": "The pathway assignment depends on protein-specific functional annotation or recognition of the exact sequence, neither of which is provided. General sequence-based reasoning does not establish the pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the annotated role, antibiotic biosynthesis is the fitting listed choice; the alternatives are not comparably supported."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the submitted sequence, but were not available to the evaluated model.",
    "The pathway annotation is curator-assigned and cites relevant publications; the supplied evidence does not independently validate those primary studies.",
    "Polyketide biosynthesis is also annotated for this protein, but is not one of the choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q70KH3 (AURI_STRTU, Demethylluteothin O-methyltransferase, EC 2.1.1.353) explicitly annotates 'PATHWAY: Antibiotic biosynthesis' with evidence codes ECO:0000305 supported by PubMed:14700630 and PubMed:16292785. The protein catalyzes a late step in aureothin biosynthesis, which is a polyketide antibiotic produced by Streptomyces thioluteus. The sequence matches the benchmark input exactly (230 AA, SHA256 confirmed). Note: 'Polyketide biosynthesis' is also listed as a pathway annotation, but aureothin is specifically an antibiotic, making 'Antibiotic biosynthesis' the more functionally precise pathway label and consistent with the author key.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C4](#evidence-c4), [C3](#evidence-c3), [H4](#evidence-h4), [H5](#evidence-h5), [H1](#evidence-h1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains motifs consistent with a SAM-dependent methyltransferase (e.g., 'VGTGYLL', 'GGVVFGATVL'), but methyltransferases are ubiquitous across all four listed pathways. No sequence-intrinsic feature uniquely identifies this enzyme as participating in antibiotic biosynthesis rather than coenzyme A, glycolipid, or LPS O-antigen biosynthesis. The only reliable discriminator is knowing that this specific 230-residue protein is aurI from Streptomyces thioluteus, functioning in the aureothin polyketide antibiotic gene cluster.


**Missing item-specific fact**

> The specific identity of this protein as aurI (Demethylluteothin O-methyltransferase) within the aureothin biosynthetic gene cluster of Streptomyces thioluteus, and its role in the late steps of aureothin (antibiotic) biosynthesis. Without this protein-specific annotation, the methyltransferase fold alone cannot distinguish among the four pathway options.


**Reason**

> While one might weakly infer 'antibiotic biosynthesis' from general knowledge that Streptomyces are prolific antibiotic producers, this is a taxon-level heuristic, not a sequence-level argument. The specific pathway assignment (antibiotic vs. polyketide vs. other biosynthetic routes) requires knowing the exact gene cluster context of this particular methyltransferase. The sequence alone does not encode organism identity or gene-cluster membership.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only 'Antibiotic biosynthesis' is supported by the UniProt annotation. 'Polyketide biosynthesis' is also annotated but is not offered as an option. Option D (LPS O-antigen biosynthesis) can be eliminated on the basis that Streptomyces are Gram-positive and lack LPS. Options A and C have no supporting annotation. The author key is unambiguous within the given choices.


### Important caveats

- The UniProt entry also lists 'Polyketide biosynthesis' as a pathway (C6, H5). Since aureothin is both a polyketide and an antibiotic, both annotations are valid. The question's choice of 'Antibiotic biosynthesis' as the answer is defensible but 'Polyketide biosynthesis' would also be correct if offered.
- The pathway annotation uses ECO:0000305 (curator inference), meaning it is derived from literature interpretation rather than a single direct experimental assay of pathway membership.
- The identity of the protein (accession Q70KH3) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model. The model sees only the raw sequence and four pathway labels.
- The protein was first integrated into Swiss-Prot on 2025-02-05; the original dataset construction date is unknown, so the author may have relied on TrEMBL or direct literature rather than a Swiss-Prot annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs consistent with a SAM-dependent methyltransferase (e.g., 'VGTGYLL', 'GGVVFGATVL'), but methyltransferases are ubiquitous across all four listed pathways. No sequence-intrinsic feature uniquely identifies this enzyme as participating in antibiotic biosynthesis rather than coenzyme A, glycolipid, or LPS O-antigen biosynthesis. The only reliable discriminator is knowing that this specific 230-residue protein is aurI from Streptomyces thioluteus, functioning in the aureothin polyketide antibiotic gene cluster.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as aurI (Demethylluteothin O-methyltransferase) within the aureothin biosynthetic gene cluster of Streptomyces thioluteus, and its role in the late steps of aureothin (antibiotic) biosynthesis. Without this protein-specific annotation, the methyltransferase fold alone cannot distinguish among the four pathway options.",
    "reason": "While one might weakly infer 'antibiotic biosynthesis' from general knowledge that Streptomyces are prolific antibiotic producers, this is a taxon-level heuristic, not a sequence-level argument. The specific pathway assignment (antibiotic vs. polyketide vs. other biosynthetic routes) requires knowing the exact gene cluster context of this particular methyltransferase. The sequence alone does not encode organism identity or gene-cluster membership."
  },
  "case_id": "pathway_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C4",
      "C3",
      "H4",
      "H5",
      "H1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q70KH3 (AURI_STRTU, Demethylluteothin O-methyltransferase, EC 2.1.1.353) explicitly annotates 'PATHWAY: Antibiotic biosynthesis' with evidence codes ECO:0000305 supported by PubMed:14700630 and PubMed:16292785. The protein catalyzes a late step in aureothin biosynthesis, which is a polyketide antibiotic produced by Streptomyces thioluteus. The sequence matches the benchmark input exactly (230 AA, SHA256 confirmed). Note: 'Polyketide biosynthesis' is also listed as a pathway annotation, but aureothin is specifically an antibiotic, making 'Antibiotic biosynthesis' the more functionally precise pathway label and consistent with the author key."
  },
  "important_caveats": [
    "The UniProt entry also lists 'Polyketide biosynthesis' as a pathway (C6, H5). Since aureothin is both a polyketide and an antibiotic, both annotations are valid. The question's choice of 'Antibiotic biosynthesis' as the answer is defensible but 'Polyketide biosynthesis' would also be correct if offered.",
    "The pathway annotation uses ECO:0000305 (curator inference), meaning it is derived from literature interpretation rather than a single direct experimental assay of pathway membership.",
    "The identity of the protein (accession Q70KH3) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model. The model sees only the raw sequence and four pathway labels.",
    "The protein was first integrated into Swiss-Prot on 2025-02-05; the original dataset construction date is unknown, so the author may have relied on TrEMBL or direct literature rather than a Swiss-Prot annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only 'Antibiotic biosynthesis' is supported by the UniProt annotation. 'Polyketide biosynthesis' is also annotated but is not offered as an option. Option D (LPS O-antigen biosynthesis) can be eliminated on the basis that Streptomyces are Gram-positive and lack LPS. Options A and C have no supporting annotation. The author key is unambiguous within the given choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q70KH3 (AURI_STRTU, Demethylluteothin O-methyltransferase, EC 2.1.1.353) explicitly annotates 'PATHWAY: Antibiotic biosynthesis' with evidence codes ECO:0000305 supported by PubMed:14700630 and PubMed:16292785. The protein catalyzes a late step in aureothin biosynthesis, which is a polyketide antibiotic produced by Streptomyces thioluteus. The sequence matches the benchmark input exactly (230 AA, SHA256 confirmed). Note: 'Polyketide biosynthesis' is also listed as a pathway annotation, but aureothin is specifically an antibiotic, making 'Antibiotic biosynthesis' the more functionally precise pathway label and consistent with the author key.",
    "evidence_ids": ["C5", "C6", "C4", "C3", "H4", "H5", "H1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains motifs consistent with a SAM-dependent methyltransferase (e.g., 'VGTGYLL', 'GGVVFGATVL'), but methyltransferases are ubiquitous across all four listed pathways. No sequence-intrinsic feature uniquely identifies this enzyme as participating in antibiotic biosynthesis rather than coenzyme A, glycolipid, or LPS O-antigen biosynthesis. The only reliable discriminator is knowing that this specific 230-residue protein is aurI from Streptomyces thioluteus, functioning in the aureothin polyketide antibiotic gene cluster.",
    "missing_item_specific_fact": "The specific identity of this protein as aurI (Demethylluteothin O-methyltransferase) within the aureothin biosynthetic gene cluster of Streptomyces thioluteus, and its role in the late steps of aureothin (antibiotic) biosynthesis. Without this protein-specific annotation, the methyltransferase fold alone cannot distinguish among the four pathway options.",
    "reason": "While one might weakly infer 'antibiotic biosynthesis' from general knowledge that Streptomyces are prolific antibiotic producers, this is a taxon-level heuristic, not a sequence-level argument. The specific pathway assignment (antibiotic vs. polyketide vs. other biosynthetic routes) requires knowing the exact gene cluster context of this particular methyltransferase. The sequence alone does not encode organism identity or gene-cluster membership."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only 'Antibiotic biosynthesis' is supported by the UniProt annotation. 'Polyketide biosynthesis' is also annotated but is not offered as an option. Option D (LPS O-antigen biosynthesis) can be eliminated on the basis that Streptomyces are Gram-positive and lack LPS. Options A and C have no supporting annotation. The author key is unambiguous within the given choices."
  },
  "important_caveats": [
    "The UniProt entry also lists 'Polyketide biosynthesis' as a pathway (C6, H5). Since aureothin is both a polyketide and an antibiotic, both annotations are valid. The question's choice of 'Antibiotic biosynthesis' as the answer is defensible but 'Polyketide biosynthesis' would also be correct if offered.",
    "The pathway annotation uses ECO:0000305 (curator inference), meaning it is derived from literature interpretation rather than a single direct experimental assay of pathway membership.",
    "The identity of the protein (accession Q70KH3) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model. The model sees only the raw sequence and four pathway labels.",
    "The protein was first integrated into Swiss-Prot on 2025-02-05; the original dataset construction date is unknown, so the author may have relied on TrEMBL or direct literature rather than a Swiss-Prot annotation."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q70KH3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 58. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:46.995748+00:00.  

```json
"Q70KH3"
```

Source SHA-256: `31716edcac38405ac53b5851941888070e610d9716c8cadb344cc4e1bc18ba1e`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH3.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:46.995748+00:00.  

```json
{"lineage":["Bacteria","Bacillati","Actinomycetota","Actinomycetes","Kitasatosporales","Streptomycetaceae","Streptomyces"],"scientificName":"Streptomyces thioluteus","taxonId":66431}
```

Source SHA-256: `31716edcac38405ac53b5851941888070e610d9716c8cadb344cc4e1bc18ba1e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:46.995748+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16292785","source":"PubMed"}],"value":"Gamma-pyrone methyltransferase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16292785","source":"PubMed"}],"value":"SAM-dependent pyrone methyltransferase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"16292785","source":"PubMed"}],"value":"2.1.1.353"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Demethylluteothin O-methyltransferase"}}}
```

Source SHA-256: `31716edcac38405ac53b5851941888070e610d9716c8cadb344cc4e1bc18ba1e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:46.995748+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"14700630","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"16292785","source":"PubMed"}],"value":"Antibiotic biosynthesis"}]}
```

Source SHA-256: `31716edcac38405ac53b5851941888070e610d9716c8cadb344cc4e1bc18ba1e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q70KH3.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:46.995748+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"14700630","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"16292785","source":"PubMed"}],"value":"Polyketide biosynthesis"}]}
```

Source SHA-256: `31716edcac38405ac53b5851941888070e610d9716c8cadb344cc4e1bc18ba1e`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q70KH3?format=txt&versions=58)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 58 / 1.  
**Retrieved:** 2026-11-02T04:31:49.122851+00:00.  

```text
ID   AURI_STRTU              Reviewed;         230 AA.
AC   Q70KH3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUL-2004, sequence version 1.
DT   09-APR-2025, entry version 58.
DE   RecName: Full=Demethylluteothin O-methyltransferase {ECO:0000305};
DE            EC=2.1.1.353 {ECO:0000269|PubMed:16292785};
DE   AltName: Full=Gamma-pyrone methyltransferase {ECO:0000303|PubMed:16292785};
DE   AltName: Full=SAM-dependent pyrone methyltransferase {ECO:0000303|PubMed:16292785};
GN   Name=aurI {ECO:0000303|PubMed:14700630};
OS   Streptomyces thioluteus.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=66431;
```

Source SHA-256: `ecdac3ea83c9b526b46a0656f9bc8ad6168658ba01edaa0f5f3f90bf6b40cc09`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q70KH3?format=txt&versions=58)  
**Locator:** `lines 50-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 58 / 1.  
**Retrieved:** 2026-11-02T04:31:49.122851+00:00.  

```text
CC   -!- PATHWAY: Antibiotic biosynthesis. {ECO:0000305|PubMed:14700630,
CC       ECO:0000305|PubMed:16292785}.
```

Source SHA-256: `ecdac3ea83c9b526b46a0656f9bc8ad6168658ba01edaa0f5f3f90bf6b40cc09`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q70KH3?format=txt&versions=58)  
**Locator:** `lines 52-53`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 58 / 1.  
**Retrieved:** 2026-11-02T04:31:49.122851+00:00.  

```text
CC   -!- PATHWAY: Polyketide biosynthesis. {ECO:0000305|PubMed:14700630,
CC       ECO:0000305|PubMed:16292785}.
```

Source SHA-256: `ecdac3ea83c9b526b46a0656f9bc8ad6168658ba01edaa0f5f3f90bf6b40cc09`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 3. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
