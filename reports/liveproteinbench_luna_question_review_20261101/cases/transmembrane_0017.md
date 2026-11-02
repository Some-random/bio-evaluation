# transmembrane_0017

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **C** — 305..325

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MQFNSLVLLAGATILSPFVQAQTWTTCNPLNETCPNDPALGTNHTFVFNTSSTVTDYYNITAGSLTYGDDGAEFTIAKQGQSPTIQSKFYIFFGQVSVIMKAATGVGIVSSIVLESDDLDEIDWEFIGGNDTHAETNYFGKGNTTSYDRAIWYPTPSDPTANFHNYTVDWTAERVQWWIDDSLVRTLAYADAVDGKNFPQTPMTVRLGIWSGGDPKGNSQGTIEWAGGETDFTKVPFTMYVKSAAVQDYSTGSEYEWTDKTGDWTSIKVISGNSTVAETITKNETPTLSLGEKWDNLPKTTKLAVYCGGGAAVAALVSAFLFTFLRQRRNGRLEREAYNQLIEKQQQDAYKDQMELHNKGIGGFDNNSYATQGDDALGGWGSNQGTGYVGPSGSASAMASGSPMVQAGQHGPMSPTMVMRNGEMSPHSAEFPQPQQPMFGGSANGGSYMKM

[Multiple Choices]
A. 305..325; 704..727
B. 301..328
C. 305..325
D. 483..503
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

> The exact supplied sequence matches a UniProt record annotating residues 305–325 as a helical transmembrane region. The annotation is computationally supported (ECO:0000255), not evidence of an experimental measurement.

Cited evidence: [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a strongly hydrophobic stretch around residues 305–325, making a membrane-spanning helix plausible and distinguishing this region from the out-of-range choices. But sequence composition alone does not establish the precise endpoints or decide between C and the broader B interval.

**Missing item-specific fact**

> The protein-specific transmembrane-region annotation or an equivalent prediction specifying its boundaries.

**Reason**

> The sequence supports a likely membrane-spanning helix, but selecting the exact annotated boundaries requires a protein-specific boundary assignment absent from the input.

### Question ambiguity

**Multiple defensible options named by Luna:** B, C.

> C matches the annotated 305–325 boundaries. B is a broader interval that includes the same hydrophobic segment; the wording asks for a segment that crosses the membrane without specifying how tightly its endpoints must match the helix.

### Important caveats

- Reviewer-only database evidence supports the key but was not available to the evaluated model.
- The cited transmembrane annotation is computational, not established here as experimentally determined.
- The source record sequence matches the supplied sequence; the author's exact source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches a UniProt record annotating residues 305–325 as a helical transmembrane region. The annotation is computationally supported (ECO:0000255), not evidence of an experimental measurement.",
    "evidence_ids": [
      "H3",
      "C5"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a strongly hydrophobic stretch around residues 305–325, making a membrane-spanning helix plausible and distinguishing this region from the out-of-range choices. But sequence composition alone does not establish the precise endpoints or decide between C and the broader B interval.",
    "missing_item_specific_fact": "The protein-specific transmembrane-region annotation or an equivalent prediction specifying its boundaries.",
    "reason": "The sequence supports a likely membrane-spanning helix, but selecting the exact annotated boundaries requires a protein-specific boundary assignment absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "C matches the annotated 305–325 boundaries. B is a broader interval that includes the same hydrophobic segment; the wording asks for a segment that crosses the membrane without specifying how tightly its endpoints must match the helix."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not available to the evaluated model.",
    "The cited transmembrane annotation is computational, not established here as experimentally determined.",
    "The source record sequence matches the supplied sequence; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A384K4T0`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 27. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K4T0.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:45.289455+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":325},"start":{"modifier":"EXACT","value":305}},"type":"Transmembrane"}
```

Source SHA-256: `ccbb380e256059eeeb55997de0484dc23c7a7b08194e043b85b0646b3597c6ca`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K4T0?format=txt&versions=27)  
**Locator:** `lines 126-128`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 27 / 1.  
**Retrieved:** 2026-11-01T06:27:27.918229+00:00.  

```text
FT   TRANSMEM        305..325
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `864962b6ce782011bc655e0c92c700e0cffaca889a096636085006100fd06a2f`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 17). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
