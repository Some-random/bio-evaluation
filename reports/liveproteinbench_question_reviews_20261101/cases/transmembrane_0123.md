# transmembrane_0123

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 31..51; 112..132; 133..153; 179..199; 212..232; 350..370; 378..398; 406..426; 428..448; 475..495

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTGQSAAVEGSNSALPWYRMGFHTLAEFNTYVTFVLLGMSIMMVTSAVTSAPDFVTKYFIYATGDPDAVAETPLFWNNANTFYNAGTYAMQVVTEIASLTPFMRSIPLGIRLFLGLGIPFVELVVIIAVPAATIPTQNGAIAVIMVVAMMGGLSKALCDSCTNALVGPFPTKFMNGAQWGLTVIALFMSIIQIILQVSMGSTFQDVLTISRIYFGIGIGIQVMAIAALVLLRYNPFAQKYIAEFRAAALRRRGHVEPEESQDSKEPATGDVAEAPKAGEKEVTLDAMEEADEVRAVPSDAFVAKSGAVLQATGDADRMVDLDQTKNITSTEQMLRASVWSVFKRIYPMLLCAFTIFFTTLLVFPGVFFLVPARSGWYMTIIVTLFNAGDFVARVLLMIRVLRPSPKLVIVGTFGRLAVIPLIVLCVRGFIPGVALPYVLIFLFGLTNGYFGTMSCIHCPRTPTLHYAGERSVAAMLAGISLMLGLCFGSNMSLAITLTY

[Multiple Choices]
A. 31..51; 112..132; 133..153; 181..199; 212..232; 350..370; 378..398; 406..426; 428..448; 475..495
B. 31..51; 112..132; 133..153; 179..199; 212..232; 350..370; 378..398; 406..426; 428..448; 475..495
C. 31..51; 133..153; 179..199; 212..232; 350..370; 378..398; 406..426; 428..448; 475..495
D. 4..24; 81..101; 116..136; 158..178; 181..201; 228..248; 271..291; 309..329
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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches the historical UniProt record, whose annotated transmembrane intervals correspond to choice B. These intervals are annotated as helical with evidence code ECO:0000255, indicating computational annotation rather than direct experimental determination of each boundary.

Citations as saved: [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14), [H15](#evidence-h15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, supporting the general prediction of a multipass membrane protein. But this does not resolve the exact annotated boundaries.


**Missing item-specific fact**

> The specific transmembrane-region coordinates for this protein, particularly whether the fourth listed region begins at 179 or 181.


**Reason**

> Choices A and B differ only by a two-residue boundary shift. Sequence hydrophobicity supports a membrane helix there but does not meaningfully distinguish those precise starts; the keyed coordinate depends on protein-specific annotation or equivalent external evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The 179..199 versus 181..199 alternatives both describe a plausible hydrophobic membrane-spanning segment; the input provides no criterion for choosing the exact boundary.


### Important caveats

- Reviewer-only database evidence supports the key but was not supplied to the evaluated model.
- The cited transmembrane boundary annotations are computational, not direct experimental measurements.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, supporting the general prediction of a multipass membrane protein. But this does not resolve the exact annotated boundaries.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific transmembrane-region coordinates for this protein, particularly whether the fourth listed region begins at 179 or 181.",
    "reason": "Choices A and B differ only by a two-residue boundary shift. Sequence hydrophobicity supports a membrane helix there but does not meaningfully distinguish those precise starts; the keyed coordinate depends on protein-specific annotation or equivalent external evidence."
  },
  "case_id": "transmembrane_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt record, whose annotated transmembrane intervals correspond to choice B. These intervals are annotated as helical with evidence code ECO:0000255, indicating computational annotation rather than direct experimental determination of each boundary."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not supplied to the evaluated model.",
    "The cited transmembrane boundary annotations are computational, not direct experimental measurements."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The 179..199 versus 181..199 alternatives both describe a plausible hydrophobic membrane-spanning segment; the input provides no criterion for choosing the exact boundary."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt record, whose annotated transmembrane intervals correspond to choice B. These intervals are annotated as helical with evidence code ECO:0000255, indicating computational annotation rather than direct experimental determination of each boundary.",
    "evidence_ids": ["H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14", "H15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple hydrophobic stretches consistent with membrane-spanning helices, supporting the general prediction of a multipass membrane protein. But this does not resolve the exact annotated boundaries.",
    "missing_item_specific_fact": "The specific transmembrane-region coordinates for this protein, particularly whether the fourth listed region begins at 179 or 181.",
    "reason": "Choices A and B differ only by a two-residue boundary shift. Sequence hydrophobicity supports a membrane helix there but does not meaningfully distinguish those precise starts; the keyed coordinate depends on protein-specific annotation or equivalent external evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The 179..199 versus 181..199 alternatives both describe a plausible hydrophobic membrane-spanning segment; the input provides no criterion for choosing the exact boundary."
  },
  "important_caveats": [
    "Reviewer-only database evidence supports the key but was not supplied to the evaluated model.",
    "The cited transmembrane boundary annotations are computational, not direct experimental measurements."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9NBV4 (Nucleoside transporter 2, Leishmania donovani) annotates exactly 10 transmembrane helices at 31..51, 112..132, 133..153, 179..199, 212..232, 350..370, 378..398, 406..426, 428..448, and 475..495 (evidence IDs C6-C15, H6-H15). This matches Choice B verbatim. The sequence is confirmed as a 499-aa fragment of LdNT2 (sequence SHA-256 matched). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity/prorule), meaning they are computational predictions rather than experimentally measured boundaries.

Citations as saved: [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [C10](#evidence-c10), [C11](#evidence-c11), [C12](#evidence-c12), [C13](#evidence-c13), [C14](#evidence-c14), [C15](#evidence-c15), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [H9](#evidence-h9), [H10](#evidence-h10), [H11](#evidence-h11), [H12](#evidence-h12), [H13](#evidence-h13), [H14](#evidence-h14), [H15](#evidence-h15).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> General reasoning can partially narrow the field: Choice D places TMs at positions (4..24, 81..101, etc.) that do not correspond to the hydrophobic stretches visible in the sequence and yields only 8 TMs, inconsistent with the 10-TM ENT-family topology; Choice C omits the clearly hydrophobic segment at 112..132, making it incomplete. Thus a model can plausibly eliminate C and D by recognizing hydrophobicity patterns and the expected number of TMs for an equilibrative nucleoside transporter.


**Missing item-specific fact**

> The critical distinction between A (TM4 at 181..199) and B (TM4 at 179..199) is a 2-residue boundary shift within a hydrophobic helix. This is well within the ±2–3 residue uncertainty of any hydrophobicity-window or HMM-based TM predictor. No sequence feature at positions 179–181 provides a principled reason to prefer one start over the other; the exact boundary reflects the specific computational annotation algorithm (ECO:0000255) used by the UniProt curators, not an experimentally resolved helix terminus.


**Reason**

> While general biological knowledge (ENT-family topology, hydrophobicity scanning) can eliminate D and C, the final A-vs-B choice hinges on a 2-residue boundary that is indistinguishable by sequence reasoning and depends on the exact database annotation. This makes the question primarily lookup-dependent for selecting the single correct option.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Choices A and B differ only in the start position of TM4 (181 vs 179). Both boundaries fall within the same hydrophobic stretch, and neither is experimentally validated (ECO:0000255). A competent hydrophobicity analysis would not reliably distinguish a 2-residue shift in this context, making both A and B defensible from pure sequence reasoning.


### Important caveats

- All 10 TM annotations carry ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental determination of helix boundaries.
- The UniProt entry is flagged as a Fragment (499 aa), so the full-length protein may have additional TMs not represented here.
- The topological domain (1..30, cytoplasmic) is the only feature with experimental evidence (ECO:0000269, PubMed:12807872); TM boundaries themselves are not experimentally resolved.
- The accession Q9NBV4 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model sees only the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "General reasoning can partially narrow the field: Choice D places TMs at positions (4..24, 81..101, etc.) that do not correspond to the hydrophobic stretches visible in the sequence and yields only 8 TMs, inconsistent with the 10-TM ENT-family topology; Choice C omits the clearly hydrophobic segment at 112..132, making it incomplete. Thus a model can plausibly eliminate C and D by recognizing hydrophobicity patterns and the expected number of TMs for an equilibrative nucleoside transporter.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The critical distinction between A (TM4 at 181..199) and B (TM4 at 179..199) is a 2-residue boundary shift within a hydrophobic helix. This is well within the ±2–3 residue uncertainty of any hydrophobicity-window or HMM-based TM predictor. No sequence feature at positions 179–181 provides a principled reason to prefer one start over the other; the exact boundary reflects the specific computational annotation algorithm (ECO:0000255) used by the UniProt curators, not an experimentally resolved helix terminus.",
    "reason": "While general biological knowledge (ENT-family topology, hydrophobicity scanning) can eliminate D and C, the final A-vs-B choice hinges on a 2-residue boundary that is indistinguishable by sequence reasoning and depends on the exact database annotation. This makes the question primarily lookup-dependent for selecting the single correct option."
  },
  "case_id": "transmembrane_0123",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C7",
      "C8",
      "C9",
      "C10",
      "C11",
      "C12",
      "C13",
      "C14",
      "C15",
      "H6",
      "H7",
      "H8",
      "H9",
      "H10",
      "H11",
      "H12",
      "H13",
      "H14",
      "H15"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9NBV4 (Nucleoside transporter 2, Leishmania donovani) annotates exactly 10 transmembrane helices at 31..51, 112..132, 133..153, 179..199, 212..232, 350..370, 378..398, 406..426, 428..448, and 475..495 (evidence IDs C6-C15, H6-H15). This matches Choice B verbatim. The sequence is confirmed as a 499-aa fragment of LdNT2 (sequence SHA-256 matched). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity/prorule), meaning they are computational predictions rather than experimentally measured boundaries."
  },
  "important_caveats": [
    "All 10 TM annotations carry ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental determination of helix boundaries.",
    "The UniProt entry is flagged as a Fragment (499 aa), so the full-length protein may have additional TMs not represented here.",
    "The topological domain (1..30, cytoplasmic) is the only feature with experimental evidence (ECO:0000269, PubMed:12807872); TM boundaries themselves are not experimentally resolved.",
    "The accession Q9NBV4 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model sees only the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Choices A and B differ only in the start position of TM4 (181 vs 179). Both boundaries fall within the same hydrophobic stretch, and neither is experimentally validated (ECO:0000255). A competent hydrophobicity analysis would not reliably distinguish a 2-residue shift in this context, making both A and B defensible from pure sequence reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0123",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9NBV4 (Nucleoside transporter 2, Leishmania donovani) annotates exactly 10 transmembrane helices at 31..51, 112..132, 133..153, 179..199, 212..232, 350..370, 378..398, 406..426, 428..448, and 475..495 (evidence IDs C6-C15, H6-H15). This matches Choice B verbatim. The sequence is confirmed as a 499-aa fragment of LdNT2 (sequence SHA-256 matched). However, all TM annotations carry evidence code ECO:0000255 (inferred by similarity/prorule), meaning they are computational predictions rather than experimentally measured boundaries.",
    "evidence_ids": ["C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15", "H6", "H7", "H8", "H9", "H10", "H11", "H12", "H13", "H14", "H15"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "General reasoning can partially narrow the field: Choice D places TMs at positions (4..24, 81..101, etc.) that do not correspond to the hydrophobic stretches visible in the sequence and yields only 8 TMs, inconsistent with the 10-TM ENT-family topology; Choice C omits the clearly hydrophobic segment at 112..132, making it incomplete. Thus a model can plausibly eliminate C and D by recognizing hydrophobicity patterns and the expected number of TMs for an equilibrative nucleoside transporter.",
    "missing_item_specific_fact": "The critical distinction between A (TM4 at 181..199) and B (TM4 at 179..199) is a 2-residue boundary shift within a hydrophobic helix. This is well within the ±2–3 residue uncertainty of any hydrophobicity-window or HMM-based TM predictor. No sequence feature at positions 179–181 provides a principled reason to prefer one start over the other; the exact boundary reflects the specific computational annotation algorithm (ECO:0000255) used by the UniProt curators, not an experimentally resolved helix terminus.",
    "reason": "While general biological knowledge (ENT-family topology, hydrophobicity scanning) can eliminate D and C, the final A-vs-B choice hinges on a 2-residue boundary that is indistinguishable by sequence reasoning and depends on the exact database annotation. This makes the question primarily lookup-dependent for selecting the single correct option."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Choices A and B differ only in the start position of TM4 (181 vs 179). Both boundaries fall within the same hydrophobic stretch, and neither is experimentally validated (ECO:0000255). A competent hydrophobicity analysis would not reliably distinguish a 2-residue shift in this context, making both A and B defensible from pure sequence reasoning."
  },
  "important_caveats": [
    "All 10 TM annotations carry ECO:0000255 (inferred by similarity), indicating computational prediction rather than experimental determination of helix boundaries.",
    "The UniProt entry is flagged as a Fragment (499 aa), so the full-length protein may have additional TMs not represented here.",
    "The topological domain (1..30, cytoplasmic) is the only feature with experimental evidence (ECO:0000269, PubMed:12807872); TM boundaries themselves are not experimentally resolved.",
    "The accession Q9NBV4 was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; the model sees only the raw sequence."
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

**Accession:** `Q9NBV4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 62. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":51},"start":{"modifier":"EXACT","value":31}},"type":"Transmembrane"}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":132},"start":{"modifier":"EXACT","value":112}},"type":"Transmembrane"}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":153},"start":{"modifier":"EXACT","value":133}},"type":"Transmembrane"}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":199},"start":{"modifier":"EXACT","value":179}},"type":"Transmembrane"}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/features/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":232},"start":{"modifier":"EXACT","value":212}},"type":"Transmembrane"}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/features/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":370},"start":{"modifier":"EXACT","value":350}},"type":"Transmembrane"}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/features/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":398},"start":{"modifier":"EXACT","value":378}},"type":"Transmembrane"}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/features/9`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":426},"start":{"modifier":"EXACT","value":406}},"type":"Transmembrane"}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/features/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":448},"start":{"modifier":"EXACT","value":428}},"type":"Transmembrane"}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9NBV4.json)  
**Locator:** `/features/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:10.554926+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":495},"start":{"modifier":"EXACT","value":475}},"type":"Transmembrane"}
```

Source SHA-256: `c697205f4abb5ea257a73dd7fa21fb4c3b73a4a657a46f316a07d193e5c8a325`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 145-147`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        31..51
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 148-150`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        112..132
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 151-153`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        133..153
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 154-156`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        179..199
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 157-159`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        212..232
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 160-162`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        350..370
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 163-165`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        378..398
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 166-168`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        406..426
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 169-171`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        428..448
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9NBV4?format=txt&versions=62)  
**Locator:** `lines 172-174`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 1.  
**Retrieved:** 2026-11-02T04:33:13.069958+00:00.  

```text
FT   TRANSMEM        475..495
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `c6f3ea767f28b291172d1bff1e34f97db01c5d476a90a59f7196e827ba0e0fa9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 123. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
