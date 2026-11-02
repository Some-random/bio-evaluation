# GO_biological_process_0084

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **A** — alpha-amino acid metabolic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKIDESLNVHSSLLQLIGNTPLLELHKITKGLKGRYFAKLEAFNVGHSAKDRVAKYIVEDAERKGLLKPGSTIVETSSGNTGYSLAMISALRGYRCIIAISDKSSHDKVEMLQALGAEVHLCPANVAPDDPRSYYEVAKRIHNETPNSIYVNQYFNPLNPESHYQTGREIWEQTQGEITHVVVCSGTGGTISGIAHYLKEQNPRVQVLGVDAYGSAIKKYHETREFDPAEVYPYKIEGIGKNLIPTATDFDVIDEFIKVTDKDAALMARKLARTEGLFMGYTSGAAIQAVKQYAEAGKFDENSIVVVLFADHGSRYMNKIYSDDWMKKQGFID

[Multiple Choices]
A. alpha-amino acid metabolic process
B. vesicle fusion to plasma membrane
C. negative regulation of gene expression, epigenetic
D. response to mechanical stimulus
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

### Expected-answer support: supported

> The sequence-matched protein is experimentally characterized as cysteate synthase, catalyzing formation of cysteate from O-phospho-L-serine and sulfite. This supports an amino-acid metabolic process, though the enzyme’s broader role is capnine biosynthesis and lipid metabolism; the exact option is broader than the annotation evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a soluble enzyme, which makes a metabolic role more plausible than vesicle fusion or epigenetic regulation. But that general clue does not establish its substrate, reaction, or biological pathway, nor does it reliably distinguish the metabolic choice from the mechanical-stimulus choice.


**Missing item-specific fact**

> The protein-specific cysteate-synthase activity—formation of cysteate from O-phospho-L-serine and sulfite—and its role in capnine biosynthesis.


**Reason**

> Choosing A requires identifying the particular enzyme activity or relying on a protein-specific functional annotation. Neither that activity nor the pathway is provided in the question; recognizing the sequence or consulting an external annotation would supply the needed fact.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is supported by the amino-acid substrate and product of the characterized reaction. The other choices are not supported by the supplied sequence or the protein-specific evidence; the principal capnine/lipid pathway is not offered as an option.


### Important caveats

- The reviewed annotation reports experimental evidence for the enzyme function, while the serine-family amino-acid GO annotation is computationally assigned.
- The evidence supports amino-acid metabolism but identifies capnine biosynthesis and lipid metabolism as the broader biological role; the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme, which makes a metabolic role more plausible than vesicle fusion or epigenetic regulation. But that general clue does not establish its substrate, reaction, or biological pathway, nor does it reliably distinguish the metabolic choice from the mechanical-stimulus choice.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific cysteate-synthase activity—formation of cysteate from O-phospho-L-serine and sulfite—and its role in capnine biosynthesis.",
    "reason": "Choosing A requires identifying the particular enzyme activity or relying on a protein-specific functional annotation. Neither that activity nor the pathway is provided in the question; recognizing the sequence or consulting an external annotation would supply the needed fact."
  },
  "case_id": "GO_biological_process_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched protein is experimentally characterized as cysteate synthase, catalyzing formation of cysteate from O-phospho-L-serine and sulfite. This supports an amino-acid metabolic process, though the enzyme’s broader role is capnine biosynthesis and lipid metabolism; the exact option is broader than the annotation evidence."
  },
  "important_caveats": [
    "The reviewed annotation reports experimental evidence for the enzyme function, while the serine-family amino-acid GO annotation is computationally assigned.",
    "The evidence supports amino-acid metabolism but identifies capnine biosynthesis and lipid metabolism as the broader biological role; the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is supported by the amino-acid substrate and product of the characterized reaction. The other choices are not supported by the supplied sequence or the protein-specific evidence; the principal capnine/lipid pathway is not offered as an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched protein is experimentally characterized as cysteate synthase, catalyzing formation of cysteate from O-phospho-L-serine and sulfite. This supports an amino-acid metabolic process, though the enzyme’s broader role is capnine biosynthesis and lipid metabolism; the exact option is broader than the annotation evidence.",
    "evidence_ids": ["C4", "C5", "H3", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme, which makes a metabolic role more plausible than vesicle fusion or epigenetic regulation. But that general clue does not establish its substrate, reaction, or biological pathway, nor does it reliably distinguish the metabolic choice from the mechanical-stimulus choice.",
    "missing_item_specific_fact": "The protein-specific cysteate-synthase activity—formation of cysteate from O-phospho-L-serine and sulfite—and its role in capnine biosynthesis.",
    "reason": "Choosing A requires identifying the particular enzyme activity or relying on a protein-specific functional annotation. Neither that activity nor the pathway is provided in the question; recognizing the sequence or consulting an external annotation would supply the needed fact."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is supported by the amino-acid substrate and product of the characterized reaction. The other choices are not supported by the supplied sequence or the protein-specific evidence; the principal capnine/lipid pathway is not offered as an option."
  },
  "important_caveats": [
    "The reviewed annotation reports experimental evidence for the enzyme function, while the serine-family amino-acid GO annotation is computationally assigned.",
    "The evidence supports amino-acid metabolism but identifies capnine biosynthesis and lipid metabolism as the broader biological role; the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is Cysteate synthase (EC 2.5.1.76), catalyzing O-phospho-L-serine + sulfite → cysteate. GO annotations include GO:0006534 (cysteine metabolic process) and GO:0009069 (serine family amino acid metabolic process), both children of alpha-amino acid metabolic process. The reaction chemistry is an amino acid metabolic transformation. While the broader biological context is sulfonolipid (capnine) biosynthesis (pathway: Lipid metabolism, GO:0006629), 'lipid metabolic process' is not among the options. Among the four choices, A is the only one consistent with the protein's enzymatic activity; B, C, D describe eukaryotic-specific processes incompatible with this bacterial enzyme. Note: the amino acid metabolic GO terms are IEA:UniProtKB-ARBA (computational inference), while the experimental evidence (PubMed:35414181) emphasizes the lipid biosynthesis context.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the motif 'VVVCSGTGGTISG' (~positions 155-170), characteristic of PLP (pyridoxal-5'-phosphate) fold-type I enzymes. PLP-dependent enzymes are overwhelmingly involved in amino acid metabolism (transamination, decarboxylation, racemization, β-replacement). Additionally, options B (vesicle fusion to plasma membrane), C (negative regulation of gene expression, epigenetic), and D (response to mechanical stimulus) describe eukaryotic-specific processes (SNARE-mediated exocytosis, chromatin remodeling, mechanotransduction signaling) that are incompatible with a ~333-residue bacterial enzyme lacking any eukaryotic signaling or membrane-trafficking domains. By identifying the PLP-binding motif and eliminating eukaryotic-specific processes, a knowledgeable biologist can reason toward amino acid metabolic process.


**Missing item-specific fact**

> None strictly required. Precise identification of this enzyme as 'Cysteate synthase' requires database lookup, but the PLP-motif recognition and elimination of eukaryotic-specific options provide a defensible reasoning pathway to option A.


**Reason**

> The PLP-binding motif is identifiable from the sequence and strongly implicates amino acid metabolism. The three distractors are eukaryotic-specific processes, making elimination straightforward for any biologist familiar with basic cell biology and enzyme cofactor chemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D describe processes (vesicle fusion, epigenetic gene silencing, mechanical stimulus response) that are fundamentally incompatible with a small bacterial enzyme bearing a PLP-binding motif. Only A is biologically plausible for this protein. No ambiguity exists among the choices.


### Important caveats

- The primary biological objective of this enzyme is sulfonolipid (capnine) biosynthesis (lipid metabolism), not amino acid metabolism per se. The amino acid metabolic GO terms (cysteine metabolic process, serine family amino acid metabolic process) are IEA:UniProtKB-ARBA computational annotations reflecting reaction chemistry, not the enzyme's primary biological role. However, since 'lipid metabolic process' is not an option, A remains the best available answer.
- The PLP-binding motif identification is a reasonable inference but not definitive proof of amino acid metabolism; some PLP enzymes participate in other pathways. The reasoning is strengthened by elimination of the three eukaryotic-specific distractors.
- The GO annotations supporting option A are all IEA (Inferred from Electronic Annotation), not experimental. The experimental evidence (PubMed:35414181) characterizes the enzyme in the context of capnine/sulfonolipid biosynthesis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the motif 'VVVCSGTGGTISG' (~positions 155-170), characteristic of PLP (pyridoxal-5'-phosphate) fold-type I enzymes. PLP-dependent enzymes are overwhelmingly involved in amino acid metabolism (transamination, decarboxylation, racemization, β-replacement). Additionally, options B (vesicle fusion to plasma membrane), C (negative regulation of gene expression, epigenetic), and D (response to mechanical stimulus) describe eukaryotic-specific processes (SNARE-mediated exocytosis, chromatin remodeling, mechanotransduction signaling) that are incompatible with a ~333-residue bacterial enzyme lacking any eukaryotic signaling or membrane-trafficking domains. By identifying the PLP-binding motif and eliminating eukaryotic-specific processes, a knowledgeable biologist can reason toward amino acid metabolic process.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Precise identification of this enzyme as 'Cysteate synthase' requires database lookup, but the PLP-motif recognition and elimination of eukaryotic-specific options provide a defensible reasoning pathway to option A.",
    "reason": "The PLP-binding motif is identifiable from the sequence and strongly implicates amino acid metabolism. The three distractors are eukaryotic-specific processes, making elimination straightforward for any biologist familiar with basic cell biology and enzyme cofactor chemistry."
  },
  "case_id": "GO_biological_process_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5",
      "H6",
      "H7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The protein is Cysteate synthase (EC 2.5.1.76), catalyzing O-phospho-L-serine + sulfite → cysteate. GO annotations include GO:0006534 (cysteine metabolic process) and GO:0009069 (serine family amino acid metabolic process), both children of alpha-amino acid metabolic process. The reaction chemistry is an amino acid metabolic transformation. While the broader biological context is sulfonolipid (capnine) biosynthesis (pathway: Lipid metabolism, GO:0006629), 'lipid metabolic process' is not among the options. Among the four choices, A is the only one consistent with the protein's enzymatic activity; B, C, D describe eukaryotic-specific processes incompatible with this bacterial enzyme. Note: the amino acid metabolic GO terms are IEA:UniProtKB-ARBA (computational inference), while the experimental evidence (PubMed:35414181) emphasizes the lipid biosynthesis context."
  },
  "important_caveats": [
    "The primary biological objective of this enzyme is sulfonolipid (capnine) biosynthesis (lipid metabolism), not amino acid metabolism per se. The amino acid metabolic GO terms (cysteine metabolic process, serine family amino acid metabolic process) are IEA:UniProtKB-ARBA computational annotations reflecting reaction chemistry, not the enzyme's primary biological role. However, since 'lipid metabolic process' is not an option, A remains the best available answer.",
    "The PLP-binding motif identification is a reasonable inference but not definitive proof of amino acid metabolism; some PLP enzymes participate in other pathways. The reasoning is strengthened by elimination of the three eukaryotic-specific distractors.",
    "The GO annotations supporting option A are all IEA (Inferred from Electronic Annotation), not experimental. The experimental evidence (PubMed:35414181) characterizes the enzyme in the context of capnine/sulfonolipid biosynthesis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D describe processes (vesicle fusion, epigenetic gene silencing, mechanical stimulus response) that are fundamentally incompatible with a small bacterial enzyme bearing a PLP-binding motif. Only A is biologically plausible for this protein. No ambiguity exists among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is Cysteate synthase (EC 2.5.1.76), catalyzing O-phospho-L-serine + sulfite → cysteate. GO annotations include GO:0006534 (cysteine metabolic process) and GO:0009069 (serine family amino acid metabolic process), both children of alpha-amino acid metabolic process. The reaction chemistry is an amino acid metabolic transformation. While the broader biological context is sulfonolipid (capnine) biosynthesis (pathway: Lipid metabolism, GO:0006629), 'lipid metabolic process' is not among the options. Among the four choices, A is the only one consistent with the protein's enzymatic activity; B, C, D describe eukaryotic-specific processes incompatible with this bacterial enzyme. Note: the amino acid metabolic GO terms are IEA:UniProtKB-ARBA (computational inference), while the experimental evidence (PubMed:35414181) emphasizes the lipid biosynthesis context.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5", "H6", "H7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the motif 'VVVCSGTGGTISG' (~positions 155-170), characteristic of PLP (pyridoxal-5'-phosphate) fold-type I enzymes. PLP-dependent enzymes are overwhelmingly involved in amino acid metabolism (transamination, decarboxylation, racemization, β-replacement). Additionally, options B (vesicle fusion to plasma membrane), C (negative regulation of gene expression, epigenetic), and D (response to mechanical stimulus) describe eukaryotic-specific processes (SNARE-mediated exocytosis, chromatin remodeling, mechanotransduction signaling) that are incompatible with a ~333-residue bacterial enzyme lacking any eukaryotic signaling or membrane-trafficking domains. By identifying the PLP-binding motif and eliminating eukaryotic-specific processes, a knowledgeable biologist can reason toward amino acid metabolic process.",
    "missing_item_specific_fact": "None strictly required. Precise identification of this enzyme as 'Cysteate synthase' requires database lookup, but the PLP-motif recognition and elimination of eukaryotic-specific options provide a defensible reasoning pathway to option A.",
    "reason": "The PLP-binding motif is identifiable from the sequence and strongly implicates amino acid metabolism. The three distractors are eukaryotic-specific processes, making elimination straightforward for any biologist familiar with basic cell biology and enzyme cofactor chemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D describe processes (vesicle fusion, epigenetic gene silencing, mechanical stimulus response) that are fundamentally incompatible with a small bacterial enzyme bearing a PLP-binding motif. Only A is biologically plausible for this protein. No ambiguity exists among the choices."
  },
  "important_caveats": [
    "The primary biological objective of this enzyme is sulfonolipid (capnine) biosynthesis (lipid metabolism), not amino acid metabolism per se. The amino acid metabolic GO terms (cysteine metabolic process, serine family amino acid metabolic process) are IEA:UniProtKB-ARBA computational annotations reflecting reaction chemistry, not the enzyme's primary biological role. However, since 'lipid metabolic process' is not an option, A remains the best available answer.",
    "The PLP-binding motif identification is a reasonable inference but not definitive proof of amino acid metabolism; some PLP enzymes participate in other pathways. The reasoning is strengthened by elimination of the three eukaryotic-specific distractors.",
    "The GO annotations supporting option A are all IEA (Inferred from Electronic Annotation), not experimental. The experimental evidence (PubMed:35414181) characterizes the enzyme in the context of capnine/sulfonolipid biosynthesis."
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

**Accession:** `C7M8J5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 65. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.457032+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35414181","source":"PubMed"}],"value":"2.5.1.76"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35414181","source":"PubMed"}],"value":"Cysteate synthase"}}}
```

Source SHA-256: `74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.457032+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35414181","source":"PubMed"}],"value":"Transferase involved in the biosynthesis of capnine, a sulfonolipid present in the outer membrane of gliding Bacteroidetes and essential for gliding motility (PubMed:35414181). Catalyzes the formation of cysteate from O-phospho-L-serine and sulfite (PubMed:35414181)"}]}
```

Source SHA-256: `74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.457032+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"35414181","source":"PubMed"}],"value":"Lipid metabolism"}]}
```

Source SHA-256: `74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C7M8J5.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:35.457032+00:00.  

```json
{"database":"GO","id":"GO:0044272","properties":[{"key":"GoTerm","value":"P:sulfur compound biosynthetic process"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-ARBA"}]}
```

Source SHA-256: `74833a2e933a644627806a5f2995e746ea7942dff28f119bca547cefbc71d5d6`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)  
**Locator:** `lines 38-42`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-02T04:27:40.735965+00:00.  

```text
CC   -!- FUNCTION: Transferase involved in the biosynthesis of capnine, a
CC       sulfonolipid present in the outer membrane of gliding Bacteroidetes and
CC       essential for gliding motility (PubMed:35414181). Catalyzes the
CC       formation of cysteate from O-phospho-L-serine and sulfite
CC       (PubMed:35414181). {ECO:0000269|PubMed:35414181}.
```

Source SHA-256: `b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)  
**Locator:** `lines 62-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-02T04:27:40.735965+00:00.  

```text
CC   -!- PATHWAY: Lipid metabolism. {ECO:0000305|PubMed:35414181}.
```

Source SHA-256: `b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)  
**Locator:** `lines 80-80`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-02T04:27:40.735965+00:00.  

```text
DR   GO; GO:0006534; P:cysteine metabolic process; IEA:UniProtKB-ARBA.
```

Source SHA-256: `b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)  
**Locator:** `lines 81-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-02T04:27:40.735965+00:00.  

```text
DR   GO; GO:0006629; P:lipid metabolic process; IEA:UniProtKB-KW.
```

Source SHA-256: `b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)  
**Locator:** `lines 82-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-02T04:27:40.735965+00:00.  

```text
DR   GO; GO:0009069; P:serine family amino acid metabolic process; IEA:UniProtKB-ARBA.
```

Source SHA-256: `b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110`.

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C7M8J5?format=txt&versions=65)  
**Locator:** `lines 83-83`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 65 / 1.  
**Retrieved:** 2026-11-02T04:27:40.735965+00:00.  

```text
DR   GO; GO:0044272; P:sulfur compound biosynthetic process; IEA:UniProtKB-ARBA.
```

Source SHA-256: `b41db9ab6487840f3f81fafe34e6a0dbd98dcbb452a2aaa98446e01f78448110`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 84. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
