# transmembrane_0105: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0105.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 93..113; 163..183; 382..402; 425..445; 764..784

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

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
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> Choice B matches the five transmembrane regions annotated for the sequence in the historical UniProt record. The annotations are computational (ECO:0000255), so they support the key as a prediction, not as independently verified experimental boundaries.

Citations as saved: [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains several strongly hydrophobic stretches consistent with membrane-spanning helices, including the stretch around 163–183. Transferable knowledge of transmembrane helices can meaningfully favor the five-region choices over A or D, but it does not establish whether the final boundary of the 382-region should be 402 or 404.


**Missing item-specific fact**

> The exact annotated endpoint at residue 402, rather than 404, is needed to distinguish B from C.


**Reason**

> B and C describe the same likely membrane-spanning segments except for a two-residue difference at one boundary. Hydrophobicity and general membrane-helix knowledge support the region but do not meaningfully resolve that precise cutoff; the recorded annotation supplies it.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The 382–404 interval in C extends the corresponding 382–402 interval in B by only two residues. The sequence context is compatible with a membrane-spanning stretch, and the prompt gives no boundary convention that makes the shorter interval uniquely correct.


### Important caveats

- The reviewer evidence matches the supplied sequence, but the author's exact source snapshot is unknown.
- The cited transmembrane annotations are computational rather than experimental; their precise boundaries should not be treated as experimentally established.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains several strongly hydrophobic stretches consistent with membrane-spanning helices, including the stretch around 163–183. Transferable knowledge of transmembrane helices can meaningfully favor the five-region choices over A or D, but it does not establish whether the final boundary of the 382-region should be 402 or 404.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact annotated endpoint at residue 402, rather than 404, is needed to distinguish B from C.",
    "reason": "B and C describe the same likely membrane-spanning segments except for a two-residue difference at one boundary. Hydrophobicity and general membrane-helix knowledge support the region but do not meaningfully resolve that precise cutoff; the recorded annotation supplies it."
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
    "reason": "Choice B matches the five transmembrane regions annotated for the sequence in the historical UniProt record. The annotations are computational (ECO:0000255), so they support the key as a prediction, not as independently verified experimental boundaries."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited transmembrane annotations are computational rather than experimental; their precise boundaries should not be treated as experimentally established."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The 382–404 interval in C extends the corresponding 382–402 interval in B by only two residues. The sequence context is compatible with a membrane-spanning stretch, and the prompt gives no boundary convention that makes the shorter interval uniquely correct."
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
    "reason": "Choice B matches the five transmembrane regions annotated for the sequence in the historical UniProt record. The annotations are computational (ECO:0000255), so they support the key as a prediction, not as independently verified experimental boundaries.",
    "evidence_ids": ["H2", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains several strongly hydrophobic stretches consistent with membrane-spanning helices, including the stretch around 163–183. Transferable knowledge of transmembrane helices can meaningfully favor the five-region choices over A or D, but it does not establish whether the final boundary of the 382-region should be 402 or 404.",
    "missing_item_specific_fact": "The exact annotated endpoint at residue 402, rather than 404, is needed to distinguish B from C.",
    "reason": "B and C describe the same likely membrane-spanning segments except for a two-residue difference at one boundary. Hydrophobicity and general membrane-helix knowledge support the region but do not meaningfully resolve that precise cutoff; the recorded annotation supplies it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The 382–404 interval in C extends the corresponding 382–402 interval in B by only two residues. The sequence context is compatible with a membrane-spanning stretch, and the prompt gives no boundary convention that makes the shorter interval uniquely correct."
  },
  "important_caveats": [
    "The reviewer evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The cited transmembrane annotations are computational rather than experimental; their precise boundaries should not be treated as experimentally established."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8I299 (E140_PLAF7, Plasmodium falciparum) annotates exactly five transmembrane helical regions: 93..113, 163..183, 382..402, 425..445, and 764..784, matching choice B precisely. All annotations carry evidence code ECO:0000255 (similarity-based computational prediction), not experimental data, but they are the recorded database annotations that match the expected answer.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choice D (18..38) is trivially eliminated as it contains charged/polar residues. The A-vs-B distinction (whether 163..183 is a TM) is arguable from hydrophobicity: the region SIICLLLFLLLSGITYMHYFI is moderately hydrophobic (21 residues, mostly L/I/F) and a model could include it. However, the critical B-vs-C distinction is a 2-residue boundary difference (382..402 vs 382..404). Positions 403 (I) and 404 (L) are clearly hydrophobic, and the TM region around 382-406 is a continuous hydrophobic stretch (IILLPPFLILLGIIIFMIFILMGY). No general TM-prediction principle reliably places the boundary at F(402) rather than L(404); this 2-residue difference falls within the resolution of any hydrophobicity-window or HMM-based TM predictor. The annotations themselves are computational (ECO:0000255, similarity), meaning the exact endpoints are algorithm-dependent. Distinguishing B from C requires knowing the specific recorded annotation for this protein.


**Missing item-specific fact**

> The exact TM boundary at the C-terminal end of the third transmembrane segment: whether the UniProt/similarity-based annotation ends at residue 402 (F) or 404 (L), given that both I(403) and L(404) are hydrophobic and the hydrophobic stretch continues through M(405). No general TM biology principle resolves this 2-residue ambiguity.


**Reason**

> While a model can eliminate D and potentially argue for including 163..183 (distinguishing A from B), the decisive B-vs-C choice hinges on a 2-residue boundary within a continuous hydrophobic stretch. This is within the uncertainty of any TM prediction method and cannot be resolved by general knowledge of transmembrane helix biology, family-level inference, or hydrophobicity principles. The specific annotation boundary is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The only difference between B and C is whether the third TM region ends at 402 or 404. Residues 403 (I) and 404 (L) are both strongly hydrophobic and part of the same hydrophobic stretch as the annotated TM region. A knowledgeable model applying standard hydrophobicity criteria might reasonably extend the TM boundary to include these residues, making C defensible. The 2-residue difference is within the typical uncertainty of TM boundary prediction.


### Important caveats

- All five TM annotations carry ECO:0000255 (similarity), indicating computational prediction by homology, not experimental determination. Exact boundaries are algorithm-dependent.
- The PP residues at positions 388-389 within the third TM region are unusual for an alpha-helix and may indicate a kink or boundary uncertainty, further complicating precise endpoint assignment.
- The protein is from Plasmodium falciparum, which has extremely AT-rich coding sequences and atypical amino acid composition, potentially affecting TM prediction accuracy.
- The sequence matches the UniProt entry exactly (791 AA, SHA256 confirmed), so numbering is consistent with the annotations.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice D (18..38) is trivially eliminated as it contains charged/polar residues. The A-vs-B distinction (whether 163..183 is a TM) is arguable from hydrophobicity: the region SIICLLLFLLLSGITYMHYFI is moderately hydrophobic (21 residues, mostly L/I/F) and a model could include it. However, the critical B-vs-C distinction is a 2-residue boundary difference (382..402 vs 382..404). Positions 403 (I) and 404 (L) are clearly hydrophobic, and the TM region around 382-406 is a continuous hydrophobic stretch (IILLPPFLILLGIIIFMIFILMGY). No general TM-prediction principle reliably places the boundary at F(402) rather than L(404); this 2-residue difference falls within the resolution of any hydrophobicity-window or HMM-based TM predictor. The annotations themselves are computational (ECO:0000255, similarity), meaning the exact endpoints are algorithm-dependent. Distinguishing B from C requires knowing the specific recorded annotation for this protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact TM boundary at the C-terminal end of the third transmembrane segment: whether the UniProt/similarity-based annotation ends at residue 402 (F) or 404 (L), given that both I(403) and L(404) are hydrophobic and the hydrophobic stretch continues through M(405). No general TM biology principle resolves this 2-residue ambiguity.",
    "reason": "While a model can eliminate D and potentially argue for including 163..183 (distinguishing A from B), the decisive B-vs-C choice hinges on a 2-residue boundary within a continuous hydrophobic stretch. This is within the uncertainty of any TM prediction method and cannot be resolved by general knowledge of transmembrane helix biology, family-level inference, or hydrophobicity principles. The specific annotation boundary is required."
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
    "reason": "The UniProt entry Q8I299 (E140_PLAF7, Plasmodium falciparum) annotates exactly five transmembrane helical regions: 93..113, 163..183, 382..402, 425..445, and 764..784, matching choice B precisely. All annotations carry evidence code ECO:0000255 (similarity-based computational prediction), not experimental data, but they are the recorded database annotations that match the expected answer."
  },
  "important_caveats": [
    "All five TM annotations carry ECO:0000255 (similarity), indicating computational prediction by homology, not experimental determination. Exact boundaries are algorithm-dependent.",
    "The PP residues at positions 388-389 within the third TM region are unusual for an alpha-helix and may indicate a kink or boundary uncertainty, further complicating precise endpoint assignment.",
    "The protein is from Plasmodium falciparum, which has extremely AT-rich coding sequences and atypical amino acid composition, potentially affecting TM prediction accuracy.",
    "The sequence matches the UniProt entry exactly (791 AA, SHA256 confirmed), so numbering is consistent with the annotations."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The only difference between B and C is whether the third TM region ends at 402 or 404. Residues 403 (I) and 404 (L) are both strongly hydrophobic and part of the same hydrophobic stretch as the annotated TM region. A knowledgeable model applying standard hydrophobicity criteria might reasonably extend the TM boundary to include these residues, making C defensible. The 2-residue difference is within the typical uncertainty of TM boundary prediction."
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
    "reason": "The UniProt entry Q8I299 (E140_PLAF7, Plasmodium falciparum) annotates exactly five transmembrane helical regions: 93..113, 163..183, 382..402, 425..445, and 764..784, matching choice B precisely. All annotations carry evidence code ECO:0000255 (similarity-based computational prediction), not experimental data, but they are the recorded database annotations that match the expected answer.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "C9", "H2", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choice D (18..38) is trivially eliminated as it contains charged/polar residues. The A-vs-B distinction (whether 163..183 is a TM) is arguable from hydrophobicity: the region SIICLLLFLLLSGITYMHYFI is moderately hydrophobic (21 residues, mostly L/I/F) and a model could include it. However, the critical B-vs-C distinction is a 2-residue boundary difference (382..402 vs 382..404). Positions 403 (I) and 404 (L) are clearly hydrophobic, and the TM region around 382-406 is a continuous hydrophobic stretch (IILLPPFLILLGIIIFMIFILMGY). No general TM-prediction principle reliably places the boundary at F(402) rather than L(404); this 2-residue difference falls within the resolution of any hydrophobicity-window or HMM-based TM predictor. The annotations themselves are computational (ECO:0000255, similarity), meaning the exact endpoints are algorithm-dependent. Distinguishing B from C requires knowing the specific recorded annotation for this protein.",
    "missing_item_specific_fact": "The exact TM boundary at the C-terminal end of the third transmembrane segment: whether the UniProt/similarity-based annotation ends at residue 402 (F) or 404 (L), given that both I(403) and L(404) are hydrophobic and the hydrophobic stretch continues through M(405). No general TM biology principle resolves this 2-residue ambiguity.",
    "reason": "While a model can eliminate D and potentially argue for including 163..183 (distinguishing A from B), the decisive B-vs-C choice hinges on a 2-residue boundary within a continuous hydrophobic stretch. This is within the uncertainty of any TM prediction method and cannot be resolved by general knowledge of transmembrane helix biology, family-level inference, or hydrophobicity principles. The specific annotation boundary is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The only difference between B and C is whether the third TM region ends at 402 or 404. Residues 403 (I) and 404 (L) are both strongly hydrophobic and part of the same hydrophobic stretch as the annotated TM region. A knowledgeable model applying standard hydrophobicity criteria might reasonably extend the TM boundary to include these residues, making C defensible. The 2-residue difference is within the typical uncertainty of TM boundary prediction."
  },
  "important_caveats": [
    "All five TM annotations carry ECO:0000255 (similarity), indicating computational prediction by homology, not experimental determination. Exact boundaries are algorithm-dependent.",
    "The PP residues at positions 388-389 within the third TM region are unusual for an alpha-helix and may indicate a kink or boundary uncertainty, further complicating precise endpoint assignment.",
    "The protein is from Plasmodium falciparum, which has extremely AT-rich coding sequences and atypical amino acid composition, potentially affecting TM prediction accuracy.",
    "The sequence matches the UniProt entry exactly (791 AA, SHA256 confirmed), so numbering is consistent with the annotations."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "Q8I299",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "22675bf4cd7112b6120f3639628647369ab18e74bb4d810869b1c3a66db09b8a",
  "benchmark_sequence_length": 791,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 93,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-03-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05",
  "current_source_sequence_sha256": "22675bf4cd7112b6120f3639628647369ab18e74bb4d810869b1c3a66db09b8a",
  "current_source_sequence_length": 791,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 91,
  "selected_historical_version": {
    "accession": "Q8I299",
    "database": "Swiss-Prot",
    "entryVersion": 91,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "E140_PLAF7",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "cca2a043dce4e751bf852a9fc0ce91753d2fa135b97f33f83920f2fd70a67170",
  "selected_historical_source_sequence_sha256": "22675bf4cd7112b6120f3639628647369ab18e74bb4d810869b1c3a66db09b8a",
  "selected_historical_source_sequence_length": 791,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 91,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I299.json",
  "source_sha256": "8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05",
  "retrieved_utc": "2026-11-02T04:32:03.092776+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q8I299\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I299.json",
  "source_sha256": "8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05",
  "retrieved_utc": "2026-11-02T04:32:03.092776+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":93,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I299.json",
  "source_sha256": "8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05",
  "retrieved_utc": "2026-11-02T04:32:03.092776+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I299.json",
  "source_sha256": "8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05",
  "retrieved_utc": "2026-11-02T04:32:03.092776+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Putative iron transporter\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I299.json",
  "source_sha256": "8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05",
  "retrieved_utc": "2026-11-02T04:32:03.092776+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":113},\"start\":{\"modifier\":\"EXACT\",\"value\":93}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I299.json",
  "source_sha256": "8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05",
  "retrieved_utc": "2026-11-02T04:32:03.092776+00:00",
  "json_pointer": "/features/2",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":183},\"start\":{\"modifier\":\"EXACT\",\"value\":163}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I299.json",
  "source_sha256": "8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05",
  "retrieved_utc": "2026-11-02T04:32:03.092776+00:00",
  "json_pointer": "/features/3",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":402},\"start\":{\"modifier\":\"EXACT\",\"value\":382}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I299.json",
  "source_sha256": "8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05",
  "retrieved_utc": "2026-11-02T04:32:03.092776+00:00",
  "json_pointer": "/features/4",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":445},\"start\":{\"modifier\":\"EXACT\",\"value\":425}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8I299.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q8I299.json",
  "source_sha256": "8d838a59ae59c0c1ceba8db6210cb2a811487804bc7a0c01cea9d7fe6eeb2a05",
  "retrieved_utc": "2026-11-02T04:32:03.092776+00:00",
  "json_pointer": "/features/5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":784},\"start\":{\"modifier\":\"EXACT\",\"value\":764}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91",
  "source_sha256": "cca2a043dce4e751bf852a9fc0ce91753d2fa135b97f33f83920f2fd70a67170",
  "retrieved_utc": "2026-11-02T04:32:05.436203+00:00",
  "source_locator": "lines 1-11",
  "excerpt": "ID   E140_PLAF7              Reviewed;         791 AA.\nAC   Q8I299;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2003, sequence version 1.\nDT   28-JAN-2026, entry version 91.\nDE   RecName: Full=Putative iron transporter {ECO:0000305};\nGN   ORFNames=PF3D7_0104100 {ECO:0000312|EMBL:CAD49001.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91",
  "source_sha256": "cca2a043dce4e751bf852a9fc0ce91753d2fa135b97f33f83920f2fd70a67170",
  "retrieved_utc": "2026-11-02T04:32:05.436203+00:00",
  "source_locator": "lines 94-96",
  "excerpt": "FT   TRANSMEM        93..113\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91",
  "source_sha256": "cca2a043dce4e751bf852a9fc0ce91753d2fa135b97f33f83920f2fd70a67170",
  "retrieved_utc": "2026-11-02T04:32:05.436203+00:00",
  "source_locator": "lines 97-99",
  "excerpt": "FT   TRANSMEM        163..183\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91",
  "source_sha256": "cca2a043dce4e751bf852a9fc0ce91753d2fa135b97f33f83920f2fd70a67170",
  "retrieved_utc": "2026-11-02T04:32:05.436203+00:00",
  "source_locator": "lines 100-102",
  "excerpt": "FT   TRANSMEM        382..402\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91",
  "source_sha256": "cca2a043dce4e751bf852a9fc0ce91753d2fa135b97f33f83920f2fd70a67170",
  "retrieved_utc": "2026-11-02T04:32:05.436203+00:00",
  "source_locator": "lines 103-105",
  "excerpt": "FT   TRANSMEM        425..445\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q8I299?format=txt&versions=91",
  "source_sha256": "cca2a043dce4e751bf852a9fc0ce91753d2fa135b97f33f83920f2fd70a67170",
  "retrieved_utc": "2026-11-02T04:32:05.436203+00:00",
  "source_locator": "lines 106-108",
  "excerpt": "FT   TRANSMEM        764..784\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 91,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 105. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
