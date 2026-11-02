# GO_biological_process_0146

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — steroid catabolic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

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
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

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

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

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

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `annotated_process_differs_from_key`.

> C5/H3 report L-fucose oxidation with ECO:0000269; C6/H4 list L-fucose catabolic process with ISS. These differ from the steroid-catabolism key.

**Remaining uncertainty:** The supplied excerpt contains no direct negative steroid-activity assay; a characterized function is not exhaustive proof against additional roles.

Evidence checked: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5), [C6](#evidence-c6).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A8I6GJ95` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.152365+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Hydroxysteroid 17-beta dehydrogenase 14"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"value":"1.1.1.122"}],"fullName":{"value":"L-fucose dehydrogenase"}}}
```

Source SHA-256: `b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.152365+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38944119","source":"PubMed"}],"value":"Catalyzes the NAD(+)-dependent oxidation of L-fucose, yielding L-fucono-1,5-lactone, which rapidly converts spontaneously to L-fucone-1,4-lactone. Does not use NADPH (PubMed:38944119). Displays low activity on L-fucose, D-arabinose and L-galactose compared with rabbit and human (PubMed:38944119). This is consitent with the low L-fucose metabolism observed in this species (PubMed:38944119)"}]}
```

Source SHA-256: `b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8I6GJ95.json)  
**Locator:** `/uniProtKBCrossReferences/26`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:12.152365+00:00.  

```json
{"database":"GO","id":"GO:0042355","properties":[{"key":"GoTerm","value":"P:L-fucose catabolic process"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `b771d75ec68fe3fe40ec9ce4a7c5be09aba6ba685a4b44078776bc6814ffb3ca`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)  
**Locator:** `lines 70-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:42:06.511227+00:00.  

```text
CC   -!- FUNCTION: Catalyzes the NAD(+)-dependent oxidation of L-fucose,
CC       yielding L-fucono-1,5-lactone, which rapidly converts spontaneously to
CC       L-fucone-1,4-lactone. Does not use NADPH (PubMed:38944119). Displays
CC       low activity on L-fucose, D-arabinose and L-galactose compared with
CC       rabbit and human (PubMed:38944119). This is consitent with the low L-
CC       fucose metabolism observed in this species (PubMed:38944119).
CC       {ECO:0000269|PubMed:38944119}.
```

Source SHA-256: `254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8I6GJ95?format=txt&versions=19)  
**Locator:** `lines 137-137`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-01T06:42:06.511227+00:00.  

```text
DR   GO; GO:0042355; P:L-fucose catabolic process; ISS:UniProtKB.
```

Source SHA-256: `254b3aaa13d8772a07a9fba560b88aee21dbd339669de4833af8d223c7eed898`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 69404-69414`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0006706
name: steroid catabolic process
namespace: biological_process
def: "The chemical reactions and pathways resulting in the breakdown of steroids, compounds with a 1,2,cyclopentanoperhydrophenanthrene nucleus." [GOC:curators]
synonym: "steroid breakdown" EXACT []
synonym: "steroid catabolism" EXACT []
synonym: "steroid degradation" EXACT []
is_a: GO:0008202 ! steroid metabolic process
is_a: GO:0016042 ! lipid catabolic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 146. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
