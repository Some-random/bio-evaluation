# temperature_0037

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `temperature`  
**Author expected answer:** **B** — 37-42

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MKDLKVAVVGLGYVGLPLAVEFGKKRTVVGFDINQGRIAELRQGIDSTLEVDAAELKEASELSFTFNLQDLQKCNVFIVTVPTPIDEHKQPDLTPLVKASESIGKVLKKGDIVIYESTVYPGATEEDCVPVLEKFSGLRFNEDFFAGYSPERINPGDKEHRVSSIKKVTSGSTPEIAELVDSLYREIITAGTHKASSIKVAEAAKVIENTQRDLNIALINELAIIFNRMGIDTEAVLKAAGTKWNFMPFRPGLVGGHCIGVDPYYLTHKAQSIGYHPEIILAGRRLNDGMGAYVVSQLVKAMLKRRIHVDGARVLLMGLTFKENCPDLRNTKVVDIVRELAEYNIQVDVFDPWVSAEDAMHEYGITPVGTPSHGAYDGIILAVAHSEFKNMGAENIRKLGKAEHVLYDLKYLLDEDKSDLRL

[Multiple Choices]
A. 26-37
B. 37-42
C. 22-33
D. 40-54
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Thermal Adaptation Prediction, which is to predict the thermal adaptation category of a protein. This relates to the optimal temperature range in which the protein is stable and functional (e.g., cold-adapted, moderate temperature-adapted, or heat-adapted). This property is encoded by subtle patterns in the amino acid sequence that affect the protein's structural stability, such as amino acid composition and the potential for internal bonds. Based on the provided sequence, you must classify the protein into its most likely thermal category.. The inputs provided by the user for this task include:

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

> The sequence matches the UniProt entry, whose experimentally supported temperature annotation reports an optimum between 37 and 42 °C, matching choice B. The entry also reports relatively constant activity from 37 to 56 °C, which is distinct from the stated optimum.

Cited evidence: [C1](#evidence-c1), [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The protein’s temperature range cannot be read directly from its sequence. General biological knowledge might suggest a mesophilic context, but the original input supplies neither organism nor experimental temperature data and does not distinguish these precise ranges.

**Missing item-specific fact**

> The experimentally reported optimum temperature range for this specific protein.

**Reason**

> Selecting B requires a protein-specific measurement or annotation absent from the input; generic sequence-based thermal-adaptation heuristics do not justify this precise interval.

### Question ambiguity

**Multiple defensible options named by Luna:** B, D.

> The reported optimum range, 37–42 °C, matches B, but overlaps D at 40–42 °C. Without a single optimum value or a rule for choosing among overlapping ranges, a value within that overlap fits both.

### Important caveats

- The experimental annotation applies to the sequence-matched protein; the exact author source snapshot is unknown.
- The annotation also reports relatively constant activity over a broader range, which should not be conflated with the optimum.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "temperature_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, whose experimentally supported temperature annotation reports an optimum between 37 and 42 °C, matching choice B. The entry also reports relatively constant activity from 37 to 56 °C, which is distinct from the stated optimum.",
    "evidence_ids": [
      "C1",
      "C5",
      "H6"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The protein’s temperature range cannot be read directly from its sequence. General biological knowledge might suggest a mesophilic context, but the original input supplies neither organism nor experimental temperature data and does not distinguish these precise ranges.",
    "missing_item_specific_fact": "The experimentally reported optimum temperature range for this specific protein.",
    "reason": "Selecting B requires a protein-specific measurement or annotation absent from the input; generic sequence-based thermal-adaptation heuristics do not justify this precise interval."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The reported optimum range, 37–42 °C, matches B, but overlaps D at 40–42 °C. Without a single optimum value or a rule for choosing among overlapping ranges, a value within that overlap fits both."
  },
  "important_caveats": [
    "The experimental annotation applies to the sequence-matched protein; the exact author source snapshot is unknown.",
    "The annotation also reports relatively constant activity over a broader range, which should not be conflated with the optimum."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q9RHD7`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 111. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
"Q9RHD7"
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:27.130209+00:00.  

```json
{"commentType":"BIOPHYSICOCHEMICAL PROPERTIES","kineticParameters":{"michaelisConstants":[{"constant":0.047,"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"substrate":"UDP-GlcNAc","unit":"mM"},{"constant":22.2,"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"}],"substrate":"UDP-GlcNAc (refolded enzyme, in the presence of NAD(+))","unit":"mM"},{"constant":0.27,"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"substrate":"UDP-GalNAc","unit":"mM"},{"constant":7.79,"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"}],"substrate":"UDP-GalNAc (refolded enzyme, in the presence of NAD(+))","unit":"mM"},{"constant":0.23,"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"substrate":"NAD(+)","unit":"mM"},{"constant":0.65,"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"}],"substrate":"NAD(+) (refolded enzyme)","unit":"mM"},{"constant":3.7,"evidences":[{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"substrate":"NADP(+)","unit":"mM"},{"constant":0.44,"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"}],"substrate":"NADP(+) (refolded enzyme)","unit":"mM"}],"note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"kcat is 110 min(-1) with UDP-GlcNAc as substrate. kcat is 0.69 min(-1) with UDP-GalNAc as substrate. kcat is 110 min(-1) with NAD(+) as substrate. kcat is 0.71 min(-1) with NADP(+) as substrate (PubMed:18065759). kcat is 5.5 min(-1) with UDP-GlcNAc as substrate (refolded enzyme, in the presence of NAD(+)). kcat is 47.8 min(-1) with UDP-GalNAc as substrate (refolded enzyme, in the presence of NAD(+)). kcat is 26.8 min(-1) with NAD(+) as substrate (refolded enzyme). kcat is 16.9 min(-1) with NADP(+) as substrate (refolded enzyme) (PubMed:10931835)."}]}},"phDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"Optimum pH is 8.5."}]},"temperatureDependence":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"10931835","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"18065759","source":"PubMed"}],"value":"Activity is relatively constant over a wide temperature range from 37 to 56 degrees Celsius (PubMed:10931835). Optimum temperature is between 37 and 42 degrees Celsius (PubMed:18065759)."}]}}
```

Source SHA-256: `9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)  
**Locator:** `lines 78-109`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 111 / 1.  
**Retrieved:** 2026-11-01T06:28:50.339116+00:00.  

```text
CC   -!- BIOPHYSICOCHEMICAL PROPERTIES:
CC       Kinetic parameters:
CC         KM=0.047 mM for UDP-GlcNAc {ECO:0000269|PubMed:18065759};
CC         KM=22.2 mM for UDP-GlcNAc (refolded enzyme, in the presence of
CC         NAD(+)) {ECO:0000269|PubMed:10931835};
CC         KM=0.27 mM for UDP-GalNAc {ECO:0000269|PubMed:18065759};
CC         KM=7.79 mM for UDP-GalNAc (refolded enzyme, in the presence of
CC         NAD(+)) {ECO:0000269|PubMed:10931835};
CC         KM=0.23 mM for NAD(+) {ECO:0000269|PubMed:18065759};
CC         KM=0.65 mM for NAD(+) (refolded enzyme)
CC         {ECO:0000269|PubMed:10931835};
CC         KM=3.7 mM for NADP(+) {ECO:0000269|PubMed:18065759};
CC         KM=0.44 mM for NADP(+) (refolded enzyme)
CC         {ECO:0000269|PubMed:10931835};
CC         Note=kcat is 110 min(-1) with UDP-GlcNAc as substrate. kcat is 0.69
CC         min(-1) with UDP-GalNAc as substrate. kcat is 110 min(-1) with NAD(+)
CC         as substrate. kcat is 0.71 min(-1) with NADP(+) as substrate
CC         (PubMed:18065759). kcat is 5.5 min(-1) with UDP-GlcNAc as substrate
CC         (refolded enzyme, in the presence of NAD(+)). kcat is 47.8 min(-1)
CC         with UDP-GalNAc as substrate (refolded enzyme, in the presence of
CC         NAD(+)). kcat is 26.8 min(-1) with NAD(+) as substrate (refolded
CC         enzyme). kcat is 16.9 min(-1) with NADP(+) as substrate (refolded
CC         enzyme) (PubMed:10931835). {ECO:0000269|PubMed:10931835,
CC         ECO:0000269|PubMed:18065759};
CC       pH dependence:
CC         Optimum pH is 8.5. {ECO:0000269|PubMed:10931835,
CC         ECO:0000269|PubMed:18065759};
CC       Temperature dependence:
CC         Activity is relatively constant over a wide temperature range from 37
CC         to 56 degrees Celsius (PubMed:10931835). Optimum temperature is
CC         between 37 and 42 degrees Celsius (PubMed:18065759).
CC         {ECO:0000269|PubMed:10931835, ECO:0000269|PubMed:18065759};
```

Source SHA-256: `f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/temperature.json) (zero-based source row 37). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
