# transmembrane_0105

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `transmembrane`  
**Author expected answer:** **B** — 93..113; 163..183; 382..402; 425..445; 764..784

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVDFNDLSVELKKTELIKEDLRNLSHIINNEFSYFCQNENKNVSFNNNISSYYNDDIFSKSTLNNLYTSWKLEDFSHFDFSSILDILKRNQYVMCSIYFLLIFSCIYFLTLLLYTKCIKTTLKKWFCRYCSENINENNSNHNEQRTVLQNVINKSCYFITYSSIICLLLFLLLSGITYMHYFIKTKKGIHSNICNIYTRLDKFLLNKCLDPKKVDTSCYSAEHILNDLSSILEEYKKVKQQAKDDTLLDENTPFPLLERYITTFNKLNVLKNNINKNNTTLENEYFHTYPALKGISETLTTIISEGNKNFGNARNVIKEVKSTIKYSFHTVDETIRNVFKDSVPKITGLITQAGKSIKGINNKYKIKERIPKYTNIILLTNIILLLPPFLILLGIIIFMIFILMGYIQKNNNFFIKLFGHFSAYFGLLTIIILSFGILFLSTSVIGGTSCILSERILKNELRFDILNNTLIDYCIKNESAPLIDDDITTSFVAKINSFDTGHIDHNINEYEKHFTILKESFFHKSLKFMDYIWIVIMKRENNTFLNRIRTEQVKKSLLITGIINENIKYENMEAIGIRSYLTTLNKIIFPENNGKICFNDIICEKENNTYNITENSKTTDQKYRNIRDGMDEHLRNDLDAIVQLFVYKARILKENIFDINDLDSNEKNKIGWSEYTPRNINGTQKKSIINTFLVNVIESINFSEIINFFDKMRDQFNVLKDLILLKIDTLTENTKCNKLVKELINVRKDYCNNVVLNLSTLSVYLIIFSITSFLLWYLFLFLWFYYNIKPS

[Multiple Choices]
A. 93..113; 382..402; 425..445; 764..784
B. 93..113; 163..183; 382..402; 425..445; 764..784
C. 93..113; 163..183; 382..404; 425..445; 764..784
D. 18..38
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

> The sequence-matched UniProt record annotates all five intervals in B as transmembrane helices, including in the historical record. The evidence code ECO:0000255 indicates computational support, not direct experimental validation.

Citations as saved: [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple strongly hydrophobic stretches consistent with membrane-spanning helices, which helps distinguish these choices from D and supports including the 163..183 region absent from A.


**Missing item-specific fact**

> Choosing B over C requires the specific predicted boundary at residue 402 rather than 404; that fine-grained boundary is not reliably determined by general sequence reasoning.


**Reason**

> Broad sequence hydrophobicity supports the set of candidate helices, but the near-identical B and C options differ by only two residues in one predicted helix. The supplied sequence alone does not securely resolve that annotation-level endpoint.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both choices include the same strongly hydrophobic candidate helix and differ only by extending its endpoint from 402 to 404, a small boundary shift that is not clearly distinguished by the sequence as a membrane-spanning segment.


### Important caveats

- The supporting UniProt transmembrane annotations are computational, not evidence of experimental measurement.
- The reviewer-only database evidence was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches consistent with membrane-spanning helices, which helps distinguish these choices from D and supports including the 163..183 region absent from A.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Choosing B over C requires the specific predicted boundary at residue 402 rather than 404; that fine-grained boundary is not reliably determined by general sequence reasoning.",
    "reason": "Broad sequence hydrophobicity supports the set of candidate helices, but the near-identical B and C options differ by only two residues in one predicted helix. The supplied sequence alone does not securely resolve that annotation-level endpoint."
  },
  "case_id": "transmembrane_0105",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all five intervals in B as transmembrane helices, including in the historical record. The evidence code ECO:0000255 indicates computational support, not direct experimental validation."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane annotations are computational, not evidence of experimental measurement.",
    "The reviewer-only database evidence was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both choices include the same strongly hydrophobic candidate helix and differ only by extending its endpoint from 402 to 404, a small boundary shift that is not clearly distinguished by the sequence as a membrane-spanning segment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates all five intervals in B as transmembrane helices, including in the historical record. The evidence code ECO:0000255 indicates computational support, not direct experimental validation.",
    "evidence_ids": ["H2", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple strongly hydrophobic stretches consistent with membrane-spanning helices, which helps distinguish these choices from D and supports including the 163..183 region absent from A.",
    "missing_item_specific_fact": "Choosing B over C requires the specific predicted boundary at residue 402 rather than 404; that fine-grained boundary is not reliably determined by general sequence reasoning.",
    "reason": "Broad sequence hydrophobicity supports the set of candidate helices, but the near-identical B and C options differ by only two residues in one predicted helix. The supplied sequence alone does not securely resolve that annotation-level endpoint."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both choices include the same strongly hydrophobic candidate helix and differ only by extending its endpoint from 402 to 404, a small boundary shift that is not clearly distinguished by the sequence as a membrane-spanning segment."
  },
  "important_caveats": [
    "The supporting UniProt transmembrane annotations are computational, not evidence of experimental measurement.",
    "The reviewer-only database evidence was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8I299 (E140_PLAF7, putative iron transporter, Plasmodium falciparum 3D7) annotates exactly five transmembrane helical regions at 93-113, 163-183, 382-402, 425-445, and 764-784, matching option B precisely. The sequence SHA256 matches the benchmark sequence (791 AA). However, all five annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational/similarity-based predictions rather than experimental determinations.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A hydrophobicity analysis (e.g., Kyte-Doolittle sliding window) could plausibly identify the 163-183 segment (IICLLLFLLLSGITYMHYFIK) as a hydrophobic TM candidate, distinguishing option B/A (five regions) from option A (four regions). Option D (18..38) is trivially eliminable. However, the critical B-vs-C distinction—whether the third TM helix ends at residue 402 or 404—cannot be resolved by any general biological argument. Two-residue boundary precision falls well within the uncertainty of every standard TM predictor (TMHMM, Phobius, etc.) and of hydrophobicity-based reasoning.


**Missing item-specific fact**

> The exact C-terminal boundary of the third transmembrane helix (402 vs 404) as recorded in the specific database annotation used by the question author. No general principle of membrane biophysics or hydrophobicity scale can determine a 2-residue helix boundary with this precision.


**Reason**

> While identifying the number of TM regions (five vs four) has a modest reasoning component via hydrophobicity profiling, the question ultimately requires selecting B over C based on a 2-residue boundary difference at position 382-402/404. This level of boundary precision is not derivable from sequence by general biological reasoning; it depends on the specific output of the annotation pipeline (here, similarity-based inference, ECO:0000255) that produced the UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Options B and C differ only in the end position of the third TM helix (402 vs 404). TM helix boundaries are inherently ambiguous to ±2-3 residues in computational prediction, and no hydrophobicity or structural argument from the supplied sequence can definitively exclude a 2-residue extension. A model using a different predictor or a slightly different hydrophobicity threshold could reasonably produce 382-404. Options A and D are more clearly eliminable (missing region / implausible single region).


### Important caveats

- All five TM annotations carry ECO:0000255 (inferred by similarity), not experimental evidence. The 'correct' boundaries reflect a computational prediction pipeline, not a structural or experimental determination.
- The UniProt entry was first publicly released 2025-06-18; the author's exact source snapshot is unknown, though historical entry version 91 (released 2026-01-28) already contains the same five TM annotations.
- The question format requires exact boundary agreement with a single annotation source, which penalizes defensible ±1-2 residue variation inherent to TM prediction.
- The protein is annotated as a 'Putative iron transporter' (ECO:0000305), a functional label also based on inference, adding context but not independently confirming TM topology.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A hydrophobicity analysis (e.g., Kyte-Doolittle sliding window) could plausibly identify the 163-183 segment (IICLLLFLLLSGITYMHYFIK) as a hydrophobic TM candidate, distinguishing option B/A (five regions) from option A (four regions). Option D (18..38) is trivially eliminable. However, the critical B-vs-C distinction—whether the third TM helix ends at residue 402 or 404—cannot be resolved by any general biological argument. Two-residue boundary precision falls well within the uncertainty of every standard TM predictor (TMHMM, Phobius, etc.) and of hydrophobicity-based reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact C-terminal boundary of the third transmembrane helix (402 vs 404) as recorded in the specific database annotation used by the question author. No general principle of membrane biophysics or hydrophobicity scale can determine a 2-residue helix boundary with this precision.",
    "reason": "While identifying the number of TM regions (five vs four) has a modest reasoning component via hydrophobicity profiling, the question ultimately requires selecting B over C based on a 2-residue boundary difference at position 382-402/404. This level of boundary precision is not derivable from sequence by general biological reasoning; it depends on the specific output of the annotation pipeline (here, similarity-based inference, ECO:0000255) that produced the UniProt entry."
  },
  "case_id": "transmembrane_0105",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H2",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8I299 (E140_PLAF7, putative iron transporter, Plasmodium falciparum 3D7) annotates exactly five transmembrane helical regions at 93-113, 163-183, 382-402, 425-445, and 764-784, matching option B precisely. The sequence SHA256 matches the benchmark sequence (791 AA). However, all five annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational/similarity-based predictions rather than experimental determinations."
  },
  "important_caveats": [
    "All five TM annotations carry ECO:0000255 (inferred by similarity), not experimental evidence. The 'correct' boundaries reflect a computational prediction pipeline, not a structural or experimental determination.",
    "The UniProt entry was first publicly released 2025-06-18; the author's exact source snapshot is unknown, though historical entry version 91 (released 2026-01-28) already contains the same five TM annotations.",
    "The question format requires exact boundary agreement with a single annotation source, which penalizes defensible ±1-2 residue variation inherent to TM prediction.",
    "The protein is annotated as a 'Putative iron transporter' (ECO:0000305), a functional label also based on inference, adding context but not independently confirming TM topology."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Options B and C differ only in the end position of the third TM helix (402 vs 404). TM helix boundaries are inherently ambiguous to ±2-3 residues in computational prediction, and no hydrophobicity or structural argument from the supplied sequence can definitively exclude a 2-residue extension. A model using a different predictor or a slightly different hydrophobicity threshold could reasonably produce 382-404. Options A and D are more clearly eliminable (missing region / implausible single region)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0105",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8I299 (E140_PLAF7, putative iron transporter, Plasmodium falciparum 3D7) annotates exactly five transmembrane helical regions at 93-113, 163-183, 382-402, 425-445, and 764-784, matching option B precisely. The sequence SHA256 matches the benchmark sequence (791 AA). However, all five annotations carry evidence code ECO:0000255 (inferred by similarity), meaning they are computational/similarity-based predictions rather than experimental determinations.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H2", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A hydrophobicity analysis (e.g., Kyte-Doolittle sliding window) could plausibly identify the 163-183 segment (IICLLLFLLLSGITYMHYFIK) as a hydrophobic TM candidate, distinguishing option B/A (five regions) from option A (four regions). Option D (18..38) is trivially eliminable. However, the critical B-vs-C distinction—whether the third TM helix ends at residue 402 or 404—cannot be resolved by any general biological argument. Two-residue boundary precision falls well within the uncertainty of every standard TM predictor (TMHMM, Phobius, etc.) and of hydrophobicity-based reasoning.",
    "missing_item_specific_fact": "The exact C-terminal boundary of the third transmembrane helix (402 vs 404) as recorded in the specific database annotation used by the question author. No general principle of membrane biophysics or hydrophobicity scale can determine a 2-residue helix boundary with this precision.",
    "reason": "While identifying the number of TM regions (five vs four) has a modest reasoning component via hydrophobicity profiling, the question ultimately requires selecting B over C based on a 2-residue boundary difference at position 382-402/404. This level of boundary precision is not derivable from sequence by general biological reasoning; it depends on the specific output of the annotation pipeline (here, similarity-based inference, ECO:0000255) that produced the UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Options B and C differ only in the end position of the third TM helix (402 vs 404). TM helix boundaries are inherently ambiguous to ±2-3 residues in computational prediction, and no hydrophobicity or structural argument from the supplied sequence can definitively exclude a 2-residue extension. A model using a different predictor or a slightly different hydrophobicity threshold could reasonably produce 382-404. Options A and D are more clearly eliminable (missing region / implausible single region)."
  },
  "important_caveats": [
    "All five TM annotations carry ECO:0000255 (inferred by similarity), not experimental evidence. The 'correct' boundaries reflect a computational prediction pipeline, not a structural or experimental determination.",
    "The UniProt entry was first publicly released 2025-06-18; the author's exact source snapshot is unknown, though historical entry version 91 (released 2026-01-28) already contains the same five TM annotations.",
    "The question format requires exact boundary agreement with a single annotation source, which penalizes defensible ±1-2 residue variation inherent to TM prediction.",
    "The protein is annotated as a 'Putative iron transporter' (ECO:0000305), a functional label also based on inference, adding context but not independently confirming TM topology."
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

**Accession:** `Q8I299` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 91. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)  
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.092776+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":113},"start":{"modifier":"EXACT","value":93}},"type":"Transmembrane"}
```

Source SHA-256: `8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.092776+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":183},"start":{"modifier":"EXACT","value":163}},"type":"Transmembrane"}
```

Source SHA-256: `8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)  
**Locator:** `/features/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.092776+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":402},"start":{"modifier":"EXACT","value":382}},"type":"Transmembrane"}
```

Source SHA-256: `8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)  
**Locator:** `/features/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.092776+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":445},"start":{"modifier":"EXACT","value":425}},"type":"Transmembrane"}
```

Source SHA-256: `8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)  
**Locator:** `/features/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:03.092776+00:00.  

```json
{"description":"Helical","evidences":[{"evidenceCode":"ECO:0000255"}],"location":{"end":{"modifier":"EXACT","value":784},"start":{"modifier":"EXACT","value":764}},"type":"Transmembrane"}
```

Source SHA-256: `8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91)  
**Locator:** `lines 94-96`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-02T04:32:05.436203+00:00.  

```text
FT   TRANSMEM        93..113
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `cca2a043dce4e751bf852a9fc0ce91753d2fa135b97f33f83920f2fd70a67170`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91)  
**Locator:** `lines 97-99`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-02T04:32:05.436203+00:00.  

```text
FT   TRANSMEM        163..183
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `cca2a043dce4e751bf852a9fc0ce91753d2fa135b97f33f83920f2fd70a67170`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91)  
**Locator:** `lines 100-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-02T04:32:05.436203+00:00.  

```text
FT   TRANSMEM        382..402
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `cca2a043dce4e751bf852a9fc0ce91753d2fa135b97f33f83920f2fd70a67170`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91)  
**Locator:** `lines 103-105`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-02T04:32:05.436203+00:00.  

```text
FT   TRANSMEM        425..445
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `cca2a043dce4e751bf852a9fc0ce91753d2fa135b97f33f83920f2fd70a67170`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91)  
**Locator:** `lines 106-108`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 91 / 1.  
**Retrieved:** 2026-11-02T04:32:05.436203+00:00.  

```text
FT   TRANSMEM        764..784
FT                   /note="Helical"
FT                   /evidence="ECO:0000255"
```

Source SHA-256: `cca2a043dce4e751bf852a9fc0ce91753d2fa135b97f33f83920f2fd70a67170`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 105. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
