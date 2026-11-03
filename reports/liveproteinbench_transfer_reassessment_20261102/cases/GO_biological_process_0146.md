# GO_biological_process_0146: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_biological_process_0146.txt)

**Task:** `GO_biological_process`  
**Author key, unchanged:** **D** — steroid catabolic process

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | contradicted | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | contradicted | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | contradicted | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MAAVGRYSGKVVVVTGGSRGIGAAIVRAFVDSGAQVVFCDKDEAGGRAVEQELLGTVFIPGDVTQEGDLQTLISETVSRFGHLDCVVNNAGYHPPAQLPEETSAQGFRQLLEENLLGAYTLIKLALPHLRKSKGNIINISSLVGAIGQSQALTYVATKGAVTAMTKALALDESRYGVRVNCISPGNIWTPLWQELAAATSDPRATILEGTLAQPLGRMGQPAEVGAAAVFLASEATFCTGLELFMTGGAELGYGRKASSSTLVEVPILPP

[Multiple Choices]
A. nuclear pore complex assembly
B. response to corticosterone
C. negative regulation of axon extension involved in axon guidance
D. steroid catabolic process
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

### Expected-answer support: contradicted

> The sequence-matched rat protein has experimentally supported NAD(+)-dependent L-fucose oxidation, and its GO annotation assigns L-fucose catabolic process. This supports sugar catabolism, not steroid catabolism as the primary process asked for.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence suggests a soluble enzyme with a nucleotide-binding oxidoreductase-like motif, but that does not identify its substrate or distinguish steroid catabolism from other specific processes.


**Missing item-specific fact**

> The protein-specific substrate and pathway assignment—experimentally, L-fucose oxidation and participation in L-fucose degradation—is absent from the question input.


**Reason**

> Selecting a specific biological process requires knowing this protein's substrate and characterized function; generic sequence features do not establish that pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports L-fucose catabolism, which is not listed. It does not establish another listed option as a defensible primary process.


### Important caveats

- The cited functional characterization and GO annotation are reviewer-only evidence, not information supplied to the evaluated model.
- The evidence supports L-fucose catabolism as the characterized function but does not prove the protein has no additional activities.
- The matched historical UniProt record supports the protein identity and annotation, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence suggests a soluble enzyme with a nucleotide-binding oxidoreductase-like motif, but that does not identify its substrate or distinguish steroid catabolism from other specific processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific substrate and pathway assignment—experimentally, L-fucose oxidation and participation in L-fucose degradation—is absent from the question input.",
    "reason": "Selecting a specific biological process requires knowing this protein's substrate and characterized function; generic sequence features do not establish that pathway."
  },
  "case_id": "GO_biological_process_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "C5",
      "C6"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched rat protein has experimentally supported NAD(+)-dependent L-fucose oxidation, and its GO annotation assigns L-fucose catabolic process. This supports sugar catabolism, not steroid catabolism as the primary process asked for."
  },
  "important_caveats": [
    "The cited functional characterization and GO annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The evidence supports L-fucose catabolism as the characterized function but does not prove the protein has no additional activities.",
    "The matched historical UniProt record supports the protein identity and annotation, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports L-fucose catabolism, which is not listed. It does not establish another listed option as a defensible primary process."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0146",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched rat protein has experimentally supported NAD(+)-dependent L-fucose oxidation, and its GO annotation assigns L-fucose catabolic process. This supports sugar catabolism, not steroid catabolism as the primary process asked for.",
    "evidence_ids": ["H3", "H4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence suggests a soluble enzyme with a nucleotide-binding oxidoreductase-like motif, but that does not identify its substrate or distinguish steroid catabolism from other specific processes.",
    "missing_item_specific_fact": "The protein-specific substrate and pathway assignment—experimentally, L-fucose oxidation and participation in L-fucose degradation—is absent from the question input.",
    "reason": "Selecting a specific biological process requires knowing this protein's substrate and characterized function; generic sequence features do not establish that pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports L-fucose catabolism, which is not listed. It does not establish another listed option as a defensible primary process."
  },
  "important_caveats": [
    "The cited functional characterization and GO annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The evidence supports L-fucose catabolism as the characterized function but does not prove the protein has no additional activities.",
    "The matched historical UniProt record supports the protein identity and annotation, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> The protein (UniProt A0A8I6GJ95, DHB14_RAT, HSD17B14) is experimentally characterized (PubMed:38944119, 2024) as L-fucose dehydrogenase (EC 1.1.1.122), catalyzing NAD+-dependent oxidation of L-fucose. Its annotated GO biological process is 'L-fucose catabolic process' (GO:0042355, evidence ISS:UniProtKB), NOT 'steroid catabolic process' (GO:0006706). L-fucose is a sugar, not a steroid. The 'Hydroxysteroid 17-beta dehydrogenase 14' name reflects SDR-family sequence similarity, not demonstrated steroid-catabolic activity. No evidence supports steroid catabolic involvement for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a Rossmann-fold/NAD-binding motif (VVVVTGGSRGIGAAIVRAF) characteristic of the SDR (Short-chain Dehydrogenase/Reductase) superfamily. This fold is shared by steroid dehydrogenases, sugar dehydrogenases, and many other oxidoreductases. Recognizing the SDR fold alone cannot distinguish steroid catabolism from L-fucose catabolism or other substrate-specific processes.


**Missing item-specific fact**

> The specific substrate of this particular SDR member (L-fucose rather than a steroid) was determined experimentally in 2024 (PubMed:38944119). Before that characterization, the protein's name 'Hydroxysteroid 17-beta dehydrogenase 14' might have led to steroid-related annotations by family inference, but no such annotation is present in the evidence. Distinguishing the correct process requires knowing the experimentally validated substrate, which is not inferable from the 270-aa sequence alone.


**Reason**

> The SDR fold motif is necessary but insufficient to identify the specific biological process. The protein's actual function (L-fucose oxidation) is not predictable from general SDR-family knowledge. Furthermore, the expected answer 'steroid catabolic process' is contradicted by the evidence, making the question doubly problematic: even a well-reasoned model recognizing the SDR fold would be led toward an incorrect answer, while the true answer (L-fucose catabolic process) is absent from the options.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> None of the four options matches the protein's actual GO annotation (L-fucose catabolic process, GO:0042355). Option D (steroid catabolic process) is contradicted by experimental evidence. Options A, B, and C are unrelated to any SDR dehydrogenase activity. The question has no scientifically correct answer among the choices as presented, though the benchmark key selects D.


### Important caveats

- The protein's family name 'Hydroxysteroid 17-beta dehydrogenase 14' is misleading; it reflects sequence-similarity-based naming within the SDR superfamily, not confirmed steroid-catabolic activity.
- The functional characterization as L-fucose dehydrogenase was published in 2024 (PubMed:38944119); the benchmark may have been constructed from earlier annotations or family-based inference, but the supplied evidence (both current and historical entry version 19) shows only 'L-fucose catabolic process' as the GO annotation.
- The GO evidence code for the L-fucose catabolic process annotation is ISS (Inferred from Sequence Similarity), meaning even the 'correct' annotation is computational, though the underlying function is experimentally supported (ECO:0000269).
- The expected answer 'steroid catabolic process' (GO:0006706) has no supporting annotation in any provided evidence source for this protein.
- Sequence identity is confirmed (SHA-256 match) between the benchmark input and UniProt A0A8I6GJ95.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold/NAD-binding motif (VVVVTGGSRGIGAAIVRAF) characteristic of the SDR (Short-chain Dehydrogenase/Reductase) superfamily. This fold is shared by steroid dehydrogenases, sugar dehydrogenases, and many other oxidoreductases. Recognizing the SDR fold alone cannot distinguish steroid catabolism from L-fucose catabolism or other substrate-specific processes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate of this particular SDR member (L-fucose rather than a steroid) was determined experimentally in 2024 (PubMed:38944119). Before that characterization, the protein's name 'Hydroxysteroid 17-beta dehydrogenase 14' might have led to steroid-related annotations by family inference, but no such annotation is present in the evidence. Distinguishing the correct process requires knowing the experimentally validated substrate, which is not inferable from the 270-aa sequence alone.",
    "reason": "The SDR fold motif is necessary but insufficient to identify the specific biological process. The protein's actual function (L-fucose oxidation) is not predictable from general SDR-family knowledge. Furthermore, the expected answer 'steroid catabolic process' is contradicted by the evidence, making the question doubly problematic: even a well-reasoned model recognizing the SDR fold would be led toward an incorrect answer, while the true answer (L-fucose catabolic process) is absent from the options."
  },
  "case_id": "GO_biological_process_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "contradicted",
    "reason": "The protein (UniProt A0A8I6GJ95, DHB14_RAT, HSD17B14) is experimentally characterized (PubMed:38944119, 2024) as L-fucose dehydrogenase (EC 1.1.1.122), catalyzing NAD+-dependent oxidation of L-fucose. Its annotated GO biological process is 'L-fucose catabolic process' (GO:0042355, evidence ISS:UniProtKB), NOT 'steroid catabolic process' (GO:0006706). L-fucose is a sugar, not a steroid. The 'Hydroxysteroid 17-beta dehydrogenase 14' name reflects SDR-family sequence similarity, not demonstrated steroid-catabolic activity. No evidence supports steroid catabolic involvement for this protein."
  },
  "important_caveats": [
    "The protein's family name 'Hydroxysteroid 17-beta dehydrogenase 14' is misleading; it reflects sequence-similarity-based naming within the SDR superfamily, not confirmed steroid-catabolic activity.",
    "The functional characterization as L-fucose dehydrogenase was published in 2024 (PubMed:38944119); the benchmark may have been constructed from earlier annotations or family-based inference, but the supplied evidence (both current and historical entry version 19) shows only 'L-fucose catabolic process' as the GO annotation.",
    "The GO evidence code for the L-fucose catabolic process annotation is ISS (Inferred from Sequence Similarity), meaning even the 'correct' annotation is computational, though the underlying function is experimentally supported (ECO:0000269).",
    "The expected answer 'steroid catabolic process' (GO:0006706) has no supporting annotation in any provided evidence source for this protein.",
    "Sequence identity is confirmed (SHA-256 match) between the benchmark input and UniProt A0A8I6GJ95."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options matches the protein's actual GO annotation (L-fucose catabolic process, GO:0042355). Option D (steroid catabolic process) is contradicted by experimental evidence. Options A, B, and C are unrelated to any SDR dehydrogenase activity. The question has no scientifically correct answer among the choices as presented, though the benchmark key selects D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0146",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The protein (UniProt A0A8I6GJ95, DHB14_RAT, HSD17B14) is experimentally characterized (PubMed:38944119, 2024) as L-fucose dehydrogenase (EC 1.1.1.122), catalyzing NAD+-dependent oxidation of L-fucose. Its annotated GO biological process is 'L-fucose catabolic process' (GO:0042355, evidence ISS:UniProtKB), NOT 'steroid catabolic process' (GO:0006706). L-fucose is a sugar, not a steroid. The 'Hydroxysteroid 17-beta dehydrogenase 14' name reflects SDR-family sequence similarity, not demonstrated steroid-catabolic activity. No evidence supports steroid catabolic involvement for this protein.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold/NAD-binding motif (VVVVTGGSRGIGAAIVRAF) characteristic of the SDR (Short-chain Dehydrogenase/Reductase) superfamily. This fold is shared by steroid dehydrogenases, sugar dehydrogenases, and many other oxidoreductases. Recognizing the SDR fold alone cannot distinguish steroid catabolism from L-fucose catabolism or other substrate-specific processes.",
    "missing_item_specific_fact": "The specific substrate of this particular SDR member (L-fucose rather than a steroid) was determined experimentally in 2024 (PubMed:38944119). Before that characterization, the protein's name 'Hydroxysteroid 17-beta dehydrogenase 14' might have led to steroid-related annotations by family inference, but no such annotation is present in the evidence. Distinguishing the correct process requires knowing the experimentally validated substrate, which is not inferable from the 270-aa sequence alone.",
    "reason": "The SDR fold motif is necessary but insufficient to identify the specific biological process. The protein's actual function (L-fucose oxidation) is not predictable from general SDR-family knowledge. Furthermore, the expected answer 'steroid catabolic process' is contradicted by the evidence, making the question doubly problematic: even a well-reasoned model recognizing the SDR fold would be led toward an incorrect answer, while the true answer (L-fucose catabolic process) is absent from the options."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options matches the protein's actual GO annotation (L-fucose catabolic process, GO:0042355). Option D (steroid catabolic process) is contradicted by experimental evidence. Options A, B, and C are unrelated to any SDR dehydrogenase activity. The question has no scientifically correct answer among the choices as presented, though the benchmark key selects D."
  },
  "important_caveats": [
    "The protein's family name 'Hydroxysteroid 17-beta dehydrogenase 14' is misleading; it reflects sequence-similarity-based naming within the SDR superfamily, not confirmed steroid-catabolic activity.",
    "The functional characterization as L-fucose dehydrogenase was published in 2024 (PubMed:38944119); the benchmark may have been constructed from earlier annotations or family-based inference, but the supplied evidence (both current and historical entry version 19) shows only 'L-fucose catabolic process' as the GO annotation.",
    "The GO evidence code for the L-fucose catabolic process annotation is ISS (Inferred from Sequence Similarity), meaning even the 'correct' annotation is computational, though the underlying function is experimentally supported (ECO:0000269).",
    "The expected answer 'steroid catabolic process' (GO:0006706) has no supporting annotation in any provided evidence source for this protein.",
    "Sequence identity is confirmed (SHA-256 match) between the benchmark input and UniProt A0A8I6GJ95."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> Evidence matched to this sequence reports experimentally supported NAD(+)-dependent L-fucose oxidation and identifies the enzyme as an initial enzyme in L-fucose degradation, which conflicts with steroid catabolism as the protein's primary process. This does not prove the protein has no steroid-related activity, but the supplied evidence does not support D as the primary process.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal glycine-rich Rossmann-like dinucleotide-binding motif and a YxxxK-like catalytic motif, consistent with a soluble NAD-dependent short-chain dehydrogenase/reductase. Transferable knowledge that hydroxysteroid dehydrogenases are oxidoreductases makes steroid catabolism a plausible choice over nuclear pore assembly, axon-guidance regulation, or a cellular response to corticosterone. This is a family-level, probabilistic inference, not proof of steroid substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The motifs and enzyme-family analogy provide a meaningful basis for selecting D among these choices without recalling this exact protein's record. However, the family-level inference is not reliable for establishing the target's actual primary substrate or process; the reviewer-only evidence identifies a different process.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No two listed options are comparably supported as the actual primary process by the supplied sequence-level clues. The experimentally indicated L-fucose catabolic process is not offered; D is a plausible family-based distractor, not evidence that multiple options are correct.


### Important caveats

- The sequence motifs support an oxidoreductase-family inference but do not establish steroid specificity.
- The supplied experimental evidence supports L-fucose oxidation; it does not explicitly rule out every possible secondary steroid-related activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich Rossmann-like dinucleotide-binding motif and a YxxxK-like catalytic motif, consistent with a soluble NAD-dependent short-chain dehydrogenase/reductase. Transferable knowledge that hydroxysteroid dehydrogenases are oxidoreductases makes steroid catabolism a plausible choice over nuclear pore assembly, axon-guidance regulation, or a cellular response to corticosterone. This is a family-level, probabilistic inference, not proof of steroid substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The motifs and enzyme-family analogy provide a meaningful basis for selecting D among these choices without recalling this exact protein's record. However, the family-level inference is not reliable for establishing the target's actual primary substrate or process; the reviewer-only evidence identifies a different process."
  },
  "case_id": "GO_biological_process_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3"
    ],
    "judgment": "contradicted",
    "reason": "Evidence matched to this sequence reports experimentally supported NAD(+)-dependent L-fucose oxidation and identifies the enzyme as an initial enzyme in L-fucose degradation, which conflicts with steroid catabolism as the protein's primary process. This does not prove the protein has no steroid-related activity, but the supplied evidence does not support D as the primary process."
  },
  "important_caveats": [
    "The sequence motifs support an oxidoreductase-family inference but do not establish steroid specificity.",
    "The supplied experimental evidence supports L-fucose oxidation; it does not explicitly rule out every possible secondary steroid-related activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No two listed options are comparably supported as the actual primary process by the supplied sequence-level clues. The experimentally indicated L-fucose catabolic process is not offered; D is a plausible family-based distractor, not evidence that multiple options are correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0146",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "Evidence matched to this sequence reports experimentally supported NAD(+)-dependent L-fucose oxidation and identifies the enzyme as an initial enzyme in L-fucose degradation, which conflicts with steroid catabolism as the protein's primary process. This does not prove the protein has no steroid-related activity, but the supplied evidence does not support D as the primary process.",
    "evidence_ids": ["C5", "C7", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal glycine-rich Rossmann-like dinucleotide-binding motif and a YxxxK-like catalytic motif, consistent with a soluble NAD-dependent short-chain dehydrogenase/reductase. Transferable knowledge that hydroxysteroid dehydrogenases are oxidoreductases makes steroid catabolism a plausible choice over nuclear pore assembly, axon-guidance regulation, or a cellular response to corticosterone. This is a family-level, probabilistic inference, not proof of steroid substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "The motifs and enzyme-family analogy provide a meaningful basis for selecting D among these choices without recalling this exact protein's record. However, the family-level inference is not reliable for establishing the target's actual primary substrate or process; the reviewer-only evidence identifies a different process."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No two listed options are comparably supported as the actual primary process by the supplied sequence-level clues. The experimentally indicated L-fucose catabolic process is not offered; D is a plausible family-based distractor, not evidence that multiple options are correct."
  },
  "important_caveats": [
    "The sequence motifs support an oxidoreductase-family inference but do not establish steroid specificity.",
    "The supplied experimental evidence supports L-fucose oxidation; it does not explicitly rule out every possible secondary steroid-related activity."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> The UniProt annotation for this sequence (A0A8I6GJ95, HSD17B14 in Rattus norvegicus) assigns GO:0042355 'L-fucose catabolic process' (ISS:UniProtKB) as the sole biological process annotation. Experimental evidence (PubMed:38944119, ECO:0000269) demonstrates the protein catalyzes NAD(+)-dependent oxidation of L-fucose to L-fucono-1,5-lactone, the initial step of L-fucose degradation. The recommended name is 'L-fucose dehydrogenase' (EC 1.1.1.122); 'Hydroxysteroid 17-beta dehydrogenase 14' is listed only as an alternative name reflecting historical family naming. 'Steroid catabolic process' (GO:0006706) does not appear in the annotation, and the experimental function is inconsistent with steroid metabolism.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Rossmann-fold motif (VVVVTGGSRGIGAAIVRA) indicating an NAD(P)-dependent oxidoreductase. At ~270 aa with SDR-family catalytic architecture, it matches the short-chain dehydrogenase/reductase (SDR) superfamily. Within SDR, the size and specific motif arrangement are consistent with the hydroxysteroid 17-beta dehydrogenase (HSD17B) subfamily, which is classically and overwhelmingly associated with steroid metabolism. Among the four offered choices, only D ('steroid catabolic process') describes an enzymatic metabolic process compatible with an SDR oxidoreductase. Options A (nuclear pore assembly) and C (axon guidance regulation) involve structural/signaling proteins with no sequence similarity to dehydrogenases. Option B ('response to corticosterone') is a signaling-response GO term, not an enzymatic process, and would not be assigned to a catabolic enzyme. Thus family-level inference from SDR/HSD17B → steroid metabolism meaningfully selects D over the other three choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing the Rossmann fold and SDR/HSD17B family architecture can eliminate A, B, and C as incompatible with an oxidoreductase enzyme, and select D based on the well-established association of the HSD17B subfamily with steroid metabolism. This is legitimate family-level transfer knowledge, even though the true function of this specific member (L-fucose catabolism) differs from the family stereotype.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only D is consistent with an SDR-family oxidoreductase. The true GO annotation (L-fucose catabolic process, GO:0042355) is not offered, but no other option is defensible for a dehydrogenase enzyme. Options A, B, and C describe processes (structural assembly, signaling response, axon guidance) with no mechanistic connection to an NAD-dependent oxidoreductase.


### Important caveats

- The expected answer 'steroid catabolic process' is contradicted by the current UniProt annotation and experimental evidence, which assign 'L-fucose catabolic process' (GO:0042355). The 2024 paper (PubMed:38944119) reclassified HSD17B14 from a presumed steroid-metabolizing enzyme to an L-fucose dehydrogenase.
- The question is still answerable toward D through family-level SDR/HSD17B reasoning, making it a valid benchmark item in terms of model discriminability, but the key itself is factually incorrect.
- The UniProt entry was first public in April 2025, after the 2024 paper established L-fucose dehydrogenase activity, so no historical steroid-metabolism annotation is expected in this record.
- The GO annotation for L-fucose catabolic process uses evidence code ISS (inferred by sequence similarity), while the catalytic activity is experimentally verified (ECO:0000269, PubMed:38944119).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold motif (VVVVTGGSRGIGAAIVRA) indicating an NAD(P)-dependent oxidoreductase. At ~270 aa with SDR-family catalytic architecture, it matches the short-chain dehydrogenase/reductase (SDR) superfamily. Within SDR, the size and specific motif arrangement are consistent with the hydroxysteroid 17-beta dehydrogenase (HSD17B) subfamily, which is classically and overwhelmingly associated with steroid metabolism. Among the four offered choices, only D ('steroid catabolic process') describes an enzymatic metabolic process compatible with an SDR oxidoreductase. Options A (nuclear pore assembly) and C (axon guidance regulation) involve structural/signaling proteins with no sequence similarity to dehydrogenases. Option B ('response to corticosterone') is a signaling-response GO term, not an enzymatic process, and would not be assigned to a catabolic enzyme. Thus family-level inference from SDR/HSD17B → steroid metabolism meaningfully selects D over the other three choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the Rossmann fold and SDR/HSD17B family architecture can eliminate A, B, and C as incompatible with an oxidoreductase enzyme, and select D based on the well-established association of the HSD17B subfamily with steroid metabolism. This is legitimate family-level transfer knowledge, even though the true function of this specific member (L-fucose catabolism) differs from the family stereotype."
  },
  "case_id": "GO_biological_process_0146",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "contradicted",
    "reason": "The UniProt annotation for this sequence (A0A8I6GJ95, HSD17B14 in Rattus norvegicus) assigns GO:0042355 'L-fucose catabolic process' (ISS:UniProtKB) as the sole biological process annotation. Experimental evidence (PubMed:38944119, ECO:0000269) demonstrates the protein catalyzes NAD(+)-dependent oxidation of L-fucose to L-fucono-1,5-lactone, the initial step of L-fucose degradation. The recommended name is 'L-fucose dehydrogenase' (EC 1.1.1.122); 'Hydroxysteroid 17-beta dehydrogenase 14' is listed only as an alternative name reflecting historical family naming. 'Steroid catabolic process' (GO:0006706) does not appear in the annotation, and the experimental function is inconsistent with steroid metabolism."
  },
  "important_caveats": [
    "The expected answer 'steroid catabolic process' is contradicted by the current UniProt annotation and experimental evidence, which assign 'L-fucose catabolic process' (GO:0042355). The 2024 paper (PubMed:38944119) reclassified HSD17B14 from a presumed steroid-metabolizing enzyme to an L-fucose dehydrogenase.",
    "The question is still answerable toward D through family-level SDR/HSD17B reasoning, making it a valid benchmark item in terms of model discriminability, but the key itself is factually incorrect.",
    "The UniProt entry was first public in April 2025, after the 2024 paper established L-fucose dehydrogenase activity, so no historical steroid-metabolism annotation is expected in this record.",
    "The GO annotation for L-fucose catabolic process uses evidence code ISS (inferred by sequence similarity), while the catalytic activity is experimentally verified (ECO:0000269, PubMed:38944119)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only D is consistent with an SDR-family oxidoreductase. The true GO annotation (L-fucose catabolic process, GO:0042355) is not offered, but no other option is defensible for a dehydrogenase enzyme. Options A, B, and C describe processes (structural assembly, signaling response, axon guidance) with no mechanistic connection to an NAD-dependent oxidoreductase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0146",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The UniProt annotation for this sequence (A0A8I6GJ95, HSD17B14 in Rattus norvegicus) assigns GO:0042355 'L-fucose catabolic process' (ISS:UniProtKB) as the sole biological process annotation. Experimental evidence (PubMed:38944119, ECO:0000269) demonstrates the protein catalyzes NAD(+)-dependent oxidation of L-fucose to L-fucono-1,5-lactone, the initial step of L-fucose degradation. The recommended name is 'L-fucose dehydrogenase' (EC 1.1.1.122); 'Hydroxysteroid 17-beta dehydrogenase 14' is listed only as an alternative name reflecting historical family naming. 'Steroid catabolic process' (GO:0006706) does not appear in the annotation, and the experimental function is inconsistent with steroid metabolism.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Rossmann-fold motif (VVVVTGGSRGIGAAIVRA) indicating an NAD(P)-dependent oxidoreductase. At ~270 aa with SDR-family catalytic architecture, it matches the short-chain dehydrogenase/reductase (SDR) superfamily. Within SDR, the size and specific motif arrangement are consistent with the hydroxysteroid 17-beta dehydrogenase (HSD17B) subfamily, which is classically and overwhelmingly associated with steroid metabolism. Among the four offered choices, only D ('steroid catabolic process') describes an enzymatic metabolic process compatible with an SDR oxidoreductase. Options A (nuclear pore assembly) and C (axon guidance regulation) involve structural/signaling proteins with no sequence similarity to dehydrogenases. Option B ('response to corticosterone') is a signaling-response GO term, not an enzymatic process, and would not be assigned to a catabolic enzyme. Thus family-level inference from SDR/HSD17B → steroid metabolism meaningfully selects D over the other three choices.",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the Rossmann fold and SDR/HSD17B family architecture can eliminate A, B, and C as incompatible with an oxidoreductase enzyme, and select D based on the well-established association of the HSD17B subfamily with steroid metabolism. This is legitimate family-level transfer knowledge, even though the true function of this specific member (L-fucose catabolism) differs from the family stereotype."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only D is consistent with an SDR-family oxidoreductase. The true GO annotation (L-fucose catabolic process, GO:0042355) is not offered, but no other option is defensible for a dehydrogenase enzyme. Options A, B, and C describe processes (structural assembly, signaling response, axon guidance) with no mechanistic connection to an NAD-dependent oxidoreductase."
  },
  "important_caveats": [
    "The expected answer 'steroid catabolic process' is contradicted by the current UniProt annotation and experimental evidence, which assign 'L-fucose catabolic process' (GO:0042355). The 2024 paper (PubMed:38944119) reclassified HSD17B14 from a presumed steroid-metabolizing enzyme to an L-fucose dehydrogenase.",
    "The question is still answerable toward D through family-level SDR/HSD17B reasoning, making it a valid benchmark item in terms of model discriminability, but the key itself is factually incorrect.",
    "The UniProt entry was first public in April 2025, after the 2024 paper established L-fucose dehydrogenase activity, so no historical steroid-metabolism annotation is expected in this record.",
    "The GO annotation for L-fucose catabolic process uses evidence code ISS (inferred by sequence similarity), while the catalytic activity is experimentally verified (ECO:0000269, PubMed:38944119)."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `annotated_process_differs_from_key`.

> C5/H3 report L-fucose oxidation with ECO:0000269; C6/H4 list L-fucose catabolic process with ISS. These differ from the steroid-catabolism key.

**Remaining uncertainty:** The supplied excerpt contains no direct negative steroid-activity assay; a characterized function is not exhaustive proof against additional roles.

Evidence checked: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5), [C6](#evidence-c6).

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "A0A8I6GJ95",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "bd37d1d516e73777e155d3437157c555ba99078fd50abfd1f3899c2c20580fad",
  "benchmark_sequence_length": 270,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-05-25",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "current_source_sequence_sha256": "bd37d1d516e73777e155d3437157c555ba99078fd50abfd1f3899c2c20580fad",
  "current_source_sequence_length": 270,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 19,
  "selected_historical_version": {
    "accession": "A0A8I6GJ95",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHB14_RAT",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "selected_historical_source_sequence_sha256": "bd37d1d516e73777e155d3437157c555ba99078fd50abfd1f3899c2c20580fad",
  "selected_historical_source_sequence_length": 270,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A8I6GJ95\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-05-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Rat\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Hydroxysteroid 17-beta dehydrogenase 14\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.122\"}],\"fullName\":{\"value\":\"L-fucose dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"value\":\"Catalyzes the NAD(+)-dependent oxidation of L-fucose, yielding L-fucono-1,5-lactone, which rapidly converts spontaneously to L-fucone-1,4-lactone. Does not use NADPH (PubMed:38944119). Displays low activity on L-fucose, D-arabinose and L-galactose compared with rabbit and human (PubMed:38944119). This is consitent with the low L-fucose metabolism observed in this species (PubMed:38944119)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/uniProtKBCrossReferences/26",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0042355\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:L-fucose catabolic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json",
  "source_sha256": "b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca",
  "retrieved_utc": "2026-11-01T06:25:12.152365+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Witecka A.\",\"Kazak V.\",\"Kwiatkowski S.\",\"Kiersztan A.\",\"Jagielski A.K.\",\"Kozminski W.\",\"Augustyniak R.\",\"Drozak J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38944119\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107501\"}],\"citationType\":\"journal article\",\"firstPage\":\"107501\",\"id\":\"38944119\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107501\",\"publicationDate\":\"2024\",\"title\":\"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose dehydrogenase, the initial enzyme of the L-fucose degradation pathway.\",\"volume\":\"300\"},\"referenceNumber\":2,\"referencePositions\":[\"CATALYTIC ACTIVITY\",\"FUNCTION\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   DHB14_RAT               Reviewed;         270 AA.\nAC   A0A8I6GJ95;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-MAY-2022, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000269|PubMed:38944119};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\nGN   Name=Hsd17b14;\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "source_locator": "lines 62-69",
  "excerpt": "RN   [2]\nRP   CATALYTIC ACTIVITY, FUNCTION, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=38944119; DOI=10.1016/j.jbc.2024.107501;\nRA   Witecka A., Kazak V., Kwiatkowski S., Kiersztan A., Jagielski A.K.,\nRA   Kozminski W., Augustyniak R., Drozak J.;\nRT   \"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose\nRT   dehydrogenase, the initial enzyme of the L-fucose degradation pathway.\";\nRL   J. Biol. Chem. 300:107501-107501(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "source_locator": "lines 70-76",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the NAD(+)-dependent oxidation of L-fucose,\nCC       yielding L-fucono-1,5-lactone, which rapidly converts spontaneously to\nCC       L-fucone-1,4-lactone. Does not use NADPH (PubMed:38944119). Displays\nCC       low activity on L-fucose, D-arabinose and L-galactose compared with\nCC       rabbit and human (PubMed:38944119). This is consitent with the low L-\nCC       fucose metabolism observed in this species (PubMed:38944119).\nCC       {ECO:0000269|PubMed:38944119}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19",
  "source_sha256": "254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898",
  "retrieved_utc": "2026-11-01T06:42:06.511227+00:00",
  "source_locator": "lines 137-137",
  "excerpt": "DR   GO; GO:0042355; P:L-fucose catabolic process; ISS:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 19,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 69404-69414",
  "excerpt": "[Term]\nid: GO:0006706\nname: steroid catabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the breakdown of steroids, compounds with a 1,2,cyclopentanoperhydrophenanthrene nucleus.\" [GOC:curators]\nsynonym: \"steroid breakdown\" EXACT []\nsynonym: \"steroid catabolism\" EXACT []\nsynonym: \"steroid degradation\" EXACT []\nis_a: GO:0008202 ! steroid metabolic process\nis_a: GO:0016042 ! lipid catabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0006706"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 307051-307064",
  "excerpt": "[Term]\nid: GO:0048843\nname: negative regulation of axon extension involved in axon guidance\nnamespace: biological_process\ndef: \"Any process that stops, prevents, or reduces the frequency, rate or extent of axon extension involved in axon guidance.\" [GOC:devbiol]\nsynonym: \"down regulation of axon extension involved in axon guidance\" EXACT []\nsynonym: \"down-regulation of axon extension involved in axon guidance\" EXACT []\nsynonym: \"downregulation of axon extension involved in axon guidance\" EXACT []\nsynonym: \"inhibition of axon extension involved in axon guidance\" NARROW []\nis_a: GO:0030517 ! negative regulation of axon extension\nis_a: GO:0048841 ! regulation of axon extension involved in axon guidance\nis_a: GO:0050922 ! negative regulation of chemotaxis\nrelationship: negatively_regulates GO:0048846 ! axon extension involved in axon guidance\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0048843"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 325170-325185",
  "excerpt": "[Term]\nid: GO:0051292\nname: nuclear pore complex assembly\nnamespace: biological_process\ndef: \"The aggregation, arrangement and bonding together of a set of components to form a nuclear pore complex.\" [GOC:ai, GOC:mah]\nsynonym: \"NPC assembly\" EXACT []\nsynonym: \"nuclear pore assembly\" EXACT []\nsynonym: \"nuclear pore biogenesis\" EXACT []\nsynonym: \"nuclear pore biosynthesis\" EXACT []\nsynonym: \"nuclear pore complex biogenesis\" EXACT []\nsynonym: \"nuclear pore complex biosynthesis\" EXACT []\nsynonym: \"nuclear pore complex formation\" EXACT []\nsynonym: \"nuclear pore formation\" EXACT []\nis_a: GO:0006999 ! nuclear pore organization\nis_a: GO:0046931 ! pore complex assembly\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0051292"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 326480-326490",
  "excerpt": "[Term]\nid: GO:0051412\nname: response to corticosterone\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell or an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a corticosterone stimulus. Corticosterone is a 21 carbon steroid hormone of the corticosteroid type, produced in the cortex of the adrenal glands. In many species, corticosterone is the principal glucocorticoid, involved in regulation of fuel metabolism, immune reactions, and stress responses.\" [PMID:15240347]\nsynonym: \"response to corticosterone stimulus\" EXACT [GOC:dos]\nis_a: GO:0051384 ! response to glucocorticoid\nis_a: GO:0051385 ! response to mineralocorticoid\nis_a: GO:0097305 ! response to alcohol\nis_a: GO:1901654 ! response to ketone\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0051412"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 146. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
