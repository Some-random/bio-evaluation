# transmembrane_0107

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **D** — 229..247; 276..299; 320..345; 351..370; 382..404; 424..445; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | lookup-dependent | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MEKDFTERSTKGQRKLANGVVENIESKLKNHLDNNNVINKSVNYEDVMCSNVKLSVHDDEYDIKNIKKDVCNLSKLSEERLSNNISLKDNNKVVKNPEIDTKTARQQYKKRLNSTQSTMNIEGNINNEKDDIIEDYDDGLIRNMDYEMSIVKNKRNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNSNNVDNRKRNKNEECYDESYCISDNLDEITSYRNKLSLYNKLRMCFNYFGPGWIVAIAYLDPGNLCSNLNVGLIRSPDPTLEKDYSGYYLLWIMVYGHMLGFIFQVLSMRLGHVTGLDLASLCSKEFDRTTSTIIYVLVQIAIWGAHIQAIIGTFIALNLIFGISVKVAIFYTLFEAIIYSFLENKSLGLLENVLSFLVGILAVSFFVNVFMTPINFKELAISILYPRIPKGKEIDALALLGSIISAHIFYLHTNLTAKKKSVICNDLSLRRYNTLGTIESGGSLFLSCLTNCIIVLTFAEVNLKSFERRDQYNLFTAYEVMRKSFGKISMYIWSFGLLSSGNNSSFMCEYASKSVVEGFLNKKINTFVRVFTFRLMLFSLLYMFLTLNKYTLDQLTNFINVIQVLLLPMATIPLYRFSIHENVLGEFRLKKFPKFAVFLIIIAIIISNVLLTFLDFVHKETSLITIFFLVIFSFLYFGFIIYFFNIPIKKNYIQRN

[Multiple Choices]
A. 13..35
B. 229..247; 276..299; 320..345; 351..370; 382..404; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673
C. 229..247; 272..299; 320..345; 351..370; 382..404; 424..445; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673
D. 229..247; 276..299; 320..345; 351..370; 382..404; 424..445; 466..487; 516..534; 555..573; 585..603; 623..645; 651..673
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

> The sequence matches the historical UniProt record, whose annotated transmembrane regions match Choice D exactly. These regions are marked helical with evidence code ECO:0000255, indicating computational annotation rather than direct experimental determination of each boundary.

Cited evidence: [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24), [H26](#evidence-h26), [H28](#evidence-h28).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a series of strongly hydrophobic stretches consistent with a multi-pass membrane protein, distinguishing the transmembrane-region choices from Choice A and supporting inclusion of the 424..445 segment absent from Choice B. But the sequence alone does not reliably establish all exact boundaries.

**Missing item-specific fact**

> The exact transmembrane-region coordinates, especially the 272 versus 276 start in Choices C and D, require a particular boundary annotation or prediction that is not supplied in the question.

**Reason**

> Hydropathy supports the general membrane topology, but predicted helix boundaries can vary. The GYYL residues immediately before the annotated 276 start make sequence-only exclusion of the earlier boundary uncertain.

### Question ambiguity

**Multiple defensible options named by Luna:** C, D.

> The choices differ at the start of one predicted helix: Choice C includes four additional residues, GYYL, which are hydrophobic or aromatic and could plausibly lie at a membrane interface. The exact coordinate convention is not specified; the supplied sequence alone does not conclusively distinguish that boundary.

### Important caveats

- The reviewer-only UniProt evidence supports D for the matched sequence, but the actual source snapshot used by the author is unknown.
- The cited transmembrane annotations are computational, not experimental confirmation of exact boundaries.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the historical UniProt record, whose annotated transmembrane regions match Choice D exactly. These regions are marked helical with evidence code ECO:0000255, indicating computational annotation rather than direct experimental determination of each boundary.",
    "evidence_ids": [
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16",
      "H18",
      "H20",
      "H22",
      "H24",
      "H26",
      "H28"
    ]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a series of strongly hydrophobic stretches consistent with a multi-pass membrane protein, distinguishing the transmembrane-region choices from Choice A and supporting inclusion of the 424..445 segment absent from Choice B. But the sequence alone does not reliably establish all exact boundaries.",
    "missing_item_specific_fact": "The exact transmembrane-region coordinates, especially the 272 versus 276 start in Choices C and D, require a particular boundary annotation or prediction that is not supplied in the question.",
    "reason": "Hydropathy supports the general membrane topology, but predicted helix boundaries can vary. The GYYL residues immediately before the annotated 276 start make sequence-only exclusion of the earlier boundary uncertain."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The choices differ at the start of one predicted helix: Choice C includes four additional residues, GYYL, which are hydrophobic or aromatic and could plausibly lie at a membrane interface. The exact coordinate convention is not specified; the supplied sequence alone does not conclusively distinguish that boundary."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence supports D for the matched sequence, but the actual source snapshot used by the author is unknown.",
    "The cited transmembrane annotations are computational, not experimental confirmation of exact boundaries."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `model_residue_identity_error_in_ambiguity_reason`.

> OptionC extends the second interval from keyD276..299 to272..299. Original1-based residues272..275 are YSGY, not the model claimed GYYL. The historical annotations match D and use ECO:0000255.

**Remaining uncertainty:** The incorrect four-residue string invalidates that literal premise only. Whether the shifted span remains biologically plausible is unresolved here; no ambiguity or key verdict is changed.

**Direct check of the original sequence:**

```json
{
  "inclusive_range": [
    272,
    275
  ],
  "indexing": "1-based",
  "residues": "YSGY",
  "sequence_sha256": "ad3e4f51961e13a279b7a2c9a8d92d3b0cb723ff3f0b8baf5ac09b89a6e02c7c"
}
```

Evidence checked: [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16), [H18](#evidence-h18), [H20](#evidence-h20), [H22](#evidence-h22), [H24](#evidence-h24), [H26](#evidence-h26), [H28](#evidence-h28).

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `Q8I3M7`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 117. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 153-155`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        229..247
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 159-161`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        276..299
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 165-167`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        320..345
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 171-173`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        351..370
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 177-179`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        382..404
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 183-185`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        424..445
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H18

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 189-191`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        466..487
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H20

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 195-197`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        516..534
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H22

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 201-203`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        555..573
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H24

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 207-209`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        585..603
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H26

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 213-215`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        623..645
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

### Evidence H28

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I3M7?format=txt&versions=117)  
**Locator:** `lines 219-221`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 117 / 1.  
**Retrieved:** 2026-11-02T04:32:12.059738+00:00.  

```text
FT   TRANSMEM        651..673
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `75db2a237303bdcca1e3dff1a43527aaee7cf8b65d99a684cef3447701a84319`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 107). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
