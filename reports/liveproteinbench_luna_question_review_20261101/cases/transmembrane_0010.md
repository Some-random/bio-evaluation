# transmembrane_0010

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 3..23

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MDLLQILLAIAGLLAILLLQKQWRTKTSPGAKAGRKLPPEPAGAWPVIGHLHKLGGPNPIYRNLAEWSDKYGPVMTLKLGMQNAVVVSDREAIKECFTTNDKALADRPPSSIGLHLGFNYAAIGAAPYGPYWRDMRKLVLLEVLSSRRLEMLRNVRISEIGTSIKELYSNIIRSSGGSGPAKVVISHWIEQLTLNYILRTIAGRRFSDDSSKDAQYVKGVINDFMYFAGQFVVSDVIPIPLLRWLDPQGHLKGMKRVAKEVDTMCEAWIQEHVQRRMREKPGPGQEQDFIDVLLNNRDVMRKAQEEIDNHVGKERWVDETDLKHLVYLQAIVKEGLRLYPPGPLGAPHRAIEDCQVGGYFIPKGTQLLVNVWKLHRDPRVWSEPEKFMPERFLTRQAEVDVFGHHFELLPFGSGRRACPGITFAVQVMHLTVARLLQGFDMTTPSNLPVDMTEGPGVTMPKAHPVEVLMMPRLPSALYEP

[Multiple Choices]
A. 3..23; 353..377
B. 28..48; 59..79; 106..126
C. -2..22
D. 3..23
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

> The sequence-matched UniProt entry annotates residues 3–23 as a helical transmembrane region. The annotation is computational (ECO:0000255), not direct experimental evidence.

Cited evidence: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Residues 3–23 form a long, strongly hydrophobic stretch rich in leucine and isoleucine, consistent with a membrane-spanning helix. The other listed ranges do not fit that pattern; the offset option also extends beyond the sequence's N-terminus.

**Missing item-specific fact**

> No protein-specific annotation is required to distinguish the choices from the supplied sequence, although exact boundaries remain predictions rather than experimentally established here.

**Reason**

> A conspicuous N-terminal hydrophobic helix supports the 3–23 choice, and the alternatives are meaningfully distinguishable by sequence inspection.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> Only D gives the clearly supported N-terminal segment without adding another unsupported transmembrane region.

### Important caveats

- The supporting database feature is computationally annotated; it should not be described as experimentally measured.
- The current and archived records match the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0010",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates residues 3–23 as a helical transmembrane region. The annotation is computational (ECO:0000255), not direct experimental evidence.",
    "evidence_ids": [
      "C5",
      "H4"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Residues 3–23 form a long, strongly hydrophobic stretch rich in leucine and isoleucine, consistent with a membrane-spanning helix. The other listed ranges do not fit that pattern; the offset option also extends beyond the sequence's N-terminus.",
    "missing_item_specific_fact": "No protein-specific annotation is required to distinguish the choices from the supplied sequence, although exact boundaries remain predictions rather than experimentally established here.",
    "reason": "A conspicuous N-terminal hydrophobic helix supports the 3–23 choice, and the alternatives are meaningfully distinguishable by sequence inspection."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D gives the clearly supported N-terminal segment without adding another unsupported transmembrane region."
  },
  "important_caveats": [
    "The supporting database feature is computationally annotated; it should not be described as experimentally measured.",
    "The current and archived records match the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `A0A218NGS0`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 26. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:42.234878+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":23},"start":{"modifier":"EXACT","value":3}},"type":"Transmembrane"}
```

Source SHA-256: `3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)  
**Locator:** `lines 132-134`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-01T06:27:24.367833+00:00.  

```text
FT   TRANSMEM        3..23
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 10). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
