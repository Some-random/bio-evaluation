# transmembrane_0049

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 35..55; 68..88; 99..119; 139..159

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MADFPGKVSTQTSSQEPQRSFAISSSVDMGFIKSIPGILLIAEIVVGLLVWTLIASTPHYLIPALGWVLFVSITLWLLSIALLVILLLSLHQRLPSVPWPLVLLVFYSVAALLYLTAFLANAATVPGGYYQGHLGASAFFGIVETLLYTASSYFAYLGWRGEGQNAAGSTVPV

[Multiple Choices]
A. 35..55; 99..119; 139..159
B. 35..55; 68..88; 99..119; 139..159
C. 35..55
D. 35..55; 63..83; 99..119; 139..159
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## Luna’s full visible review

### Expected-answer support: supported

> The sequence exactly matches the historical UniProt record, which annotates transmembrane helices at 35–55, 68–88, 99–119, and 139–159—the intervals in B. The helix annotations carry computational evidence code ECO:0000255, so this supports the key as a database annotation, not as independently established experimental evidence.

Cited evidence: [H3](#evidence-h3), [H5](#evidence-h5), [H7](#evidence-h7), [H9](#evidence-h9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains long hydrophobic stretches consistent with multiple membrane-spanning helices, including a particularly hydrophobic region around residues 63–88. That supports identifying the general region, but does not reliably establish its exact annotated boundaries.

**Missing item-specific fact**

> The protein-specific annotation locating the second helix at 68–88 rather than the also-hydrophobic 63–83 interval is not supplied in the question.

**Reason**

> The sequence permits broad transmembrane-region inference, but the choices test exact boundaries within a continuous hydrophobic stretch. General sequence reasoning does not clearly distinguish B from D.

### Question ambiguity

**Multiple defensible options named by Luna:** B, D.

> Both choices include the same strongly hydrophobic second region but give different boundaries. The sequence alone does not unambiguously determine those precise endpoints.

### Important caveats

- Reviewer-only database evidence was not available to the evaluated model.
- The cited transmembrane annotations are computational; the supplied evidence does not independently verify the boundaries experimentally.
- The source record sequence matches the input, but the author's exact source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt record, which annotates transmembrane helices at 35–55, 68–88, 99–119, and 139–159—the intervals in B. The helix annotations carry computational evidence code ECO:0000255, so this supports the key as a database annotation, not as independently established experimental evidence.",
    "evidence_ids": [
      "H3",
      "H5",
      "H7",
      "H9"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains long hydrophobic stretches consistent with multiple membrane-spanning helices, including a particularly hydrophobic region around residues 63–88. That supports identifying the general region, but does not reliably establish its exact annotated boundaries.",
    "missing_item_specific_fact": "The protein-specific annotation locating the second helix at 68–88 rather than the also-hydrophobic 63–83 interval is not supplied in the question.",
    "reason": "The sequence permits broad transmembrane-region inference, but the choices test exact boundaries within a continuous hydrophobic stretch. General sequence reasoning does not clearly distinguish B from D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both choices include the same strongly hydrophobic second region but give different boundaries. The sequence alone does not unambiguously determine those precise endpoints."
  },
  "important_caveats": [
    "Reviewer-only database evidence was not available to the evaluated model.",
    "The cited transmembrane annotations are computational; the supplied evidence does not independently verify the boundaries experimentally.",
    "The source record sequence matches the input, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A3KQ86`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 121. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)  
**Locator:** `lines 153-155`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:26:58.657829+00:00.  

```text
FT   TRANSMEM        35..55
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)  
**Locator:** `lines 159-161`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:26:58.657829+00:00.  

```text
FT   TRANSMEM        68..88
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)  
**Locator:** `lines 165-167`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:26:58.657829+00:00.  

```text
FT   TRANSMEM        99..119
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3KQ86?format=txt&versions=121)  
**Locator:** `lines 171-173`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:26:58.657829+00:00.  

```text
FT   TRANSMEM        139..159
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `a6866759886a22c2e64aae8941e7fe997c98c66a52079a88daaa7c18d3ddd601`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 49). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
