# transmembrane_0059

[All 1,736 questions](../README.md) · [Method and limits](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 17..37; 48..68; 94..114; 129..149; 176..196; 295..315; 322..342

| Expected-answer support | Reasoning versus lookup | Review status |
|---|---|---|
| supported | reasoning-supported | format-valid AI review |

These labels are Luna’s original judgments. Source support and reasoning from the original input are separate questions. The benchmark key and original score are unchanged.

## Complete original question

The sequence and choices below are the complete original user message, in their original order.

```text
[Protein Sequence]
MQPFGDAWSQRHLAGVVLAGSVLSIVGSLYMILGFFFLRECRSFRHKLILGLAVSDLLLALNFFIPSLSMVTGREISSPWNEGFCSANGFLMQLFFAQIDVWQISIALITLLMLSGPSMVLKWIRENVWAVWLFPWLVSLIAAFFAFGFWDYANVGGFCWLGSRNIRLYFNYIPRWIIILVCLVIYIAVYRLILHARRRANIQKTYRGRASDRAPPQPVTTTAPATNPESEKVNPDEISSGNGSSSLDTSRSGSSTGFTQTVHDPAVAGQIQTAAERAQEEAEQQKQVRKIAIQMISYPLAYAVLWAIPTIVMIIQVARGGEGVSIHVEGLAKMLLVFNGFVDAHVYGFNERTAMGWRQRIRPAAQEDDEEAAGTSGGVHEVVSRPEPTLKNPNVWQQNMV

[Multiple Choices]
A. 17..37; 48..68; 94..114; 134..154; 176..196; 295..315; 322..342
B. 17..37; 48..68; 94..114; 129..149; 176..196; 295..315; 322..342
C. 28..48; 59..79; 106..126
D. 48..68; 94..114; 129..149; 176..196; 295..315; 322..342
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

> The sequence exactly matches the UniProt record, whose historical and current annotations include all seven transmembrane spans listed in B, including 129..149. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement.

Cited evidence: [H4](#evidence-h4), [H6](#evidence-h6), [H8](#evidence-h8), [H10](#evidence-h10), [H12](#evidence-h12), [H14](#evidence-h14), [H16](#evidence-h16).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains successive strongly hydrophobic stretches separated by more polar or charged regions, consistent with a multi-pass membrane protein. The candidate set’s seven-span pattern fits this sequence; around the disputed span, 129..149 better captures the hydrophobic segment than the shifted 134..154 option, which extends into more polar residues.

**Missing item-specific fact**

> The exact curated transmembrane coordinates are not given, but sequence hydropathy and the pattern of separated hydrophobic segments provide meaningful grounds to distinguish the choices. The database annotation is useful confirmation, not information supplied to the model.

**Reason**

> This is a sequence-based prediction task with a recognizable multi-pass hydrophobic pattern. The evidence supports an inference from the input rather than requiring recognition of the exact protein or recall of its database entry.

### Question ambiguity

**Multiple defensible options named by Luna:** none.

> The alternatives omit or shift spans in ways that fit the sequence less well; no competing option is comparably supported by the supplied sequence.

### Important caveats

- The supporting database transmembrane features are computationally annotated, not established here as experimental measurements.
- The historical record sequence matches the supplied sequence, but the author’s exact source snapshot is unknown.

<details>
<summary>Saved visible review as JSON</summary>

```json
{
  "case_id": "transmembrane_0059",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the UniProt record, whose historical and current annotations include all seven transmembrane spans listed in B, including 129..149. These are computational annotations (ECO:0000255), not evidence of direct experimental measurement.",
    "evidence_ids": [
      "H4",
      "H6",
      "H8",
      "H10",
      "H12",
      "H14",
      "H16"
    ]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains successive strongly hydrophobic stretches separated by more polar or charged regions, consistent with a multi-pass membrane protein. The candidate set’s seven-span pattern fits this sequence; around the disputed span, 129..149 better captures the hydrophobic segment than the shifted 134..154 option, which extends into more polar residues.",
    "missing_item_specific_fact": "The exact curated transmembrane coordinates are not given, but sequence hydropathy and the pattern of separated hydrophobic segments provide meaningful grounds to distinguish the choices. The database annotation is useful confirmation, not information supplied to the model.",
    "reason": "This is a sequence-based prediction task with a recognizable multi-pass hydrophobic pattern. The evidence supports an inference from the input rather than requiring recognition of the exact protein or recall of its database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives omit or shift spans in ways that fit the sequence less well; no competing option is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "The supporting database transmembrane features are computationally annotated, not established here as experimental measurements.",
    "The historical record sequence matches the supplied sequence, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**This source material was supplied only to the reviewer. It was absent from the original evaluated question.** An exact-sequence database match can support a key without establishing that the question can be answered by reasoning from its original input.

**Accession:** `G1XJN1`; identity was recovered from dataset image-path metadata and was absent from the evaluated model input.  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; selected entry version 46. The exact author source snapshot remains unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 99-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        17..37
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 105-107`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        48..68
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 111-113`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        94..114
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 117-119`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        129..149
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 123-125`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        176..196
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 129-131`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        295..315
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

### Evidence H16

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 135-137`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
FT   TRANSMEM        322..342
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

---

Question and key: [LiveProteinBench source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json) (zero-based source row 59). Benchmark content © 2026 LiveProteinBench contributors, [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). Cited UniProt / Gene Ontology excerpts retain their own attribution; see [source credits](../THIRD_PARTY_NOTICES.md).
