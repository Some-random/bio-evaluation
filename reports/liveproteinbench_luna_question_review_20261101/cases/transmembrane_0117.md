# transmembrane_0117

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 31..51; 82..102; 112..132; 138..158; 179..199; 211..231; 353..373; 381..401; 409..429; 437..457; 478..498

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MTTSSDSAMVNHTPSPWYKFGFKSFAEFNTYVTFVFLGMSIMMVASAVTSAPDFLTRYYVYATGDPDAVAETPLFWNNANTFYNAGTYVLQVLTELFSLTPFMRRIPLSVRLFVGLGIPFAELLLIIIVPAATIKSQHGAIAVIMVVACVGGFSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALLMSIIQIILKVSMGTSFHDILTMSRIYFGICIGIQLFAIFELAILRFNPFAQKYIAEYRAGAQRNAQNNESTLEETAPSMNEPAAGDIADLPATVDDKERALNEEEGDEVRAVTSEEFHVKRGAVLTATGDADKMVDLDQTGNITSTEQLLRASAASVFKRVYPMLVCVFLIYFTSLLTFPGVFFLVSTTSGWYMTVIVTLFNAGDFISRMVLMFRPLRPSPKVVVAGTLGRLIIIPFLVLCVRGIIRGEALPYVLITLLGLTNGYFGCMACIHCPRTTTLRYAGERSLAAMLSGISIMLGLCFGSNLSLAITLTH

[Multiple Choices]
A. 61..81; 91..111; 169..189; 192..212; 276..296; 317..337; 789..809; 830..850; 908..928; 929..949; 1033..1053; 1058..1078
B. 31..51; 82..102; 112..132; 138..158; 179..199; 211..231; 353..373; 381..401; 409..429; 437..457; 478..498
C. 31..51; 82..102; 112..132; 138..158; 179..199; 211..231; 353..373; 381..401; 409..429; 437..457
D. 31..51; 82..102; 112..132; 138..158; 179..199; 211..231; 353..373; 384..405; 409..429; 437..457; 478..498
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

> The sequence matches the UniProt entry, whose annotated transmembrane regions match all 11 intervals in B. These span annotations are primarily computational (ECO:0000255), so they support the key as an annotation-based answer but are not, by themselves, experimental validation of every boundary.

Cited evidence: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has multiple strongly hydrophobic stretches consistent with a multi-pass membrane protein, including the C-terminal region omitted by C. This supports the broad pattern of transmembrane helices, but does not reliably establish the exact listed boundaries.

**Missing item-specific fact**

> The precise annotated boundaries for this particular protein, especially the distinction between 381..401 and the closely overlapping 384..405 interval, are not supplied in the question.

**Reason**

> General sequence reasoning can identify likely membrane-spanning stretches, but the options require exact residue intervals. Choosing the keyed set depends on protein-specific boundary annotations or a sufficiently calibrated predictor, not merely on broad hydrophobicity reasoning.

### Question ambiguity

**Multiple defensible options named by Luna:** B, D.

> B matches the cited annotation. However, B's 381..401 and D's 384..405 intervals substantially overlap the same hydrophobic segment, and the question gives no boundary convention that would make such a small shift biologically unambiguous.

### Important caveats

- The reviewer-only database identity and annotations were not supplied to the evaluated model.
- Database transmembrane features here are computational annotations; the cited topology evidence does not independently establish every helix boundary experimentally.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, whose annotated transmembrane regions match all 11 intervals in B. These span annotations are primarily computational (ECO:0000255), so they support the key as an annotation-based answer but are not, by themselves, experimental validation of every boundary.",
    "evidence_ids": [
      "C6",
      "C8",
      "C10",
      "C12",
      "C14",
      "C16",
      "C18",
      "C20",
      "C22",
      "C24",
      "C26"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has multiple strongly hydrophobic stretches consistent with a multi-pass membrane protein, including the C-terminal region omitted by C. This supports the broad pattern of transmembrane helices, but does not reliably establish the exact listed boundaries.",
    "missing_item_specific_fact": "The precise annotated boundaries for this particular protein, especially the distinction between 381..401 and the closely overlapping 384..405 interval, are not supplied in the question.",
    "reason": "General sequence reasoning can identify likely membrane-spanning stretches, but the options require exact residue intervals. Choosing the keyed set depends on protein-specific boundary annotations or a sufficiently calibrated predictor, not merely on broad hydrophobicity reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "B matches the cited annotation. However, B's 381..401 and D's 384..405 intervals substantially overlap the same hydrophobic segment, and the question gives no boundary convention that would make such a small shift biologically unambiguous."
  },
  "important_caveats": [
    "The reviewer-only database identity and annotations were not supplied to the evaluated model.",
    "Database transmembrane features here are computational annotations; the cited topology evidence does not independently establish every helix boundary experimentally."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `boundary_alternative_not_independently_validated`.

> Cited computational Transmembrane features match keyB381..401; original optionD substitutes384..405, as the model states.

**Remaining uncertainty:** These annotations establish the database interval but do not demonstrate that the alternative interval is equally valid under the wording.

Evidence checked: [C6](#evidence-c6), [C8](#evidence-c8), [C10](#evidence-c10), [C12](#evidence-c12), [C14](#evidence-c14), [C16](#evidence-c16), [C18](#evidence-c18), [C20](#evidence-c20), [C22](#evidence-c22), [C24](#evidence-c24), [C26](#evidence-c26).

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q9GTP4`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 55. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":51},"start":{"modifier":"EXACT","value":31}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":102},"start":{"modifier":"EXACT","value":82}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":132},"start":{"modifier":"EXACT","value":112}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":158},"start":{"modifier":"EXACT","value":138}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":199},"start":{"modifier":"EXACT","value":179}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":231},"start":{"modifier":"EXACT","value":211}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":373},"start":{"modifier":"EXACT","value":353}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C20

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":401},"start":{"modifier":"EXACT","value":381}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C22

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":429},"start":{"modifier":"EXACT","value":409}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C24

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/20`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":457},"start":{"modifier":"EXACT","value":437}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9GTP4.json)  
**Locator:** `/features/22`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:48.296419+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":498},"start":{"modifier":"EXACT","value":478}},"type":"Transmembrane"}
```

Source SHA-256: `3c9982e101acb399e2361c4884d826caa6e853175a76e749eee018234bb47b73`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 117). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
