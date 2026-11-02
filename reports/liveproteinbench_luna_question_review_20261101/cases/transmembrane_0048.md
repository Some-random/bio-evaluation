# transmembrane_0048

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 15..33

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MDVAMRVEWLATPRVILGIGAGWVAYALCLDPLRHIPGPRLNAVSMIPYARHLLAGTTVQNSVSLHQQYGEVVRIAPNEVSLICGETAFPDIYGRLFITSQTMGQIRANSAVCRVSDGKDERASKYVQGRRVLAHAFSDKALMGQEPLVQRYVDQLIDRLKEVTSANDEPVDMVKWYNWTTFDVIADLLFGEPFGCLQDLSTHQYVALLFQSLKSLRMIYILAYYPWLRFLGNLIVDKGLIQKRKEYATWVSTQVTKRINTATPRPDFMSHILANNNNRGVKLTRAEIDSNATLMTTAGSETTATLLSGATYLLLTHPRVLRTLQDEIHSEFPTYESITLEAVAKRTPYLNAVISEALRFFPPIPVGFIRRVPKGGETVSGYWIPEGTILSVSHYAAYHSERNFRDPDSWVPERWLGDERYVNDKRAAFQPFSFGPRSCLGRNLAYAEMRLILAKMVWSFEMELDEGLSRDWLQRCRVMRLWQKPELEVRVRPRVVA

[Multiple Choices]
A. 5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 261..281; 302..322; 330..350; 385..405
B. 16..32
C. 15..33; 258..281
D. 15..33
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

> The matched UniProt record annotates residues 15–33 as a helical transmembrane region, agreeing with D. The annotation carries ECO:0000255, so this is computational annotation, not evidence of experimental validation.

Cited evidence: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal stretch is strongly hydrophobic and supports predicting a membrane-spanning helix there, distinguishing it from the many unrelated intervals in A and the additional proposed interval in C. But sequence-level reasoning does not reliably resolve the one-residue endpoint differences between B and D.

**Missing item-specific fact**

> The specific annotated boundaries, 15–33 rather than 16–32, are absent from the input.

**Reason**

> General sequence reasoning supports the location of a likely N-terminal membrane helix, but choosing the keyed exact endpoints over the near-identical alternative depends on an item-specific boundary annotation or equivalent evidence.

### Question ambiguity

**Multiple defensible options named by Luna:** B, D.

> Both options describe essentially the same strongly hydrophobic N-terminal segment; the sequence alone does not robustly establish which one-residue boundary difference is correct.

### Important caveats

- The reviewer-only record exactly matches the supplied sequence; the historical annotation is computational and does not establish experimental confirmation.
- The source snapshot used by the author is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt record annotates residues 15–33 as a helical transmembrane region, agreeing with D. The annotation carries ECO:0000255, so this is computational annotation, not evidence of experimental validation.",
    "evidence_ids": [
      "C5",
      "H3"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal stretch is strongly hydrophobic and supports predicting a membrane-spanning helix there, distinguishing it from the many unrelated intervals in A and the additional proposed interval in C. But sequence-level reasoning does not reliably resolve the one-residue endpoint differences between B and D.",
    "missing_item_specific_fact": "The specific annotated boundaries, 15–33 rather than 16–32, are absent from the input.",
    "reason": "General sequence reasoning supports the location of a likely N-terminal membrane helix, but choosing the keyed exact endpoints over the near-identical alternative depends on an item-specific boundary annotation or equivalent evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both options describe essentially the same strongly hydrophobic N-terminal segment; the sequence alone does not robustly establish which one-residue boundary difference is correct."
  },
  "important_caveats": [
    "The reviewer-only record exactly matches the supplied sequence; the historical annotation is computational and does not establish experimental confirmation.",
    "The source snapshot used by the author is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A2QQU9`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 87. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU9.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:57.143489+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":33},"start":{"modifier":"EXACT","value":15}},"type":"Transmembrane"}
```

Source SHA-256: `da743c57c89b0ab786ac3a1103de54e0cfdcba8a2bc83d6afcffbb82b38db7a1`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2QQU9?format=txt&versions=87)  
**Locator:** `lines 99-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 87 / 1.  
**Retrieved:** 2026-11-01T06:27:45.219435+00:00.  

```text
FT   TRANSMEM        15..33
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `7a9ce4cdb7446a207fbe542c309e101b336add0fcb1eacdc0748a053d0baa66d`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 48). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
