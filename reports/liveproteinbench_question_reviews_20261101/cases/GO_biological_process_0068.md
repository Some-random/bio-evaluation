# GO_biological_process_0068

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **C** — polysaccharide biosynthetic process

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEKEKGEEKMNDSRKITVIGLGYVGLPLAIHFAERGYNVVGLDKDKRKIERIEKGDSYIPDVSSNVLKDLVQNKQLVVYTPHTGIEEFQNSEYVIVTVPTPINKQKEPDLSALIAASHYIKQNLQAGQTFIFESSTYPGTLEEVIIPIIAQSGKEVGKDYYIGYSPERIDPANQQYTVQTIPKVISGQTERCKQQVQKLYSTIFDTVVPVSSPKVAEMCKLFENIQRLVNISLVNELNILCEKLGIDFREALEAAATKPFGFTPYWPGPGIGGHCIPVDPLYFQWKARQLGQSSQLIEVAHMINEKMPQQIVTQVKELSAPPGTVFLIGIAYKKDVNDLRESPALPIIELLVNEGYKVQYHDPYISSAKIGDKIYDSIPLKKKTLEKADCILIVTDHSNIDWNICKGMKHVIDTRGVLKKVSA

[Multiple Choices]
A. cytoplasmic translational elongation
B. zinc ion transport
C. polysaccharide biosynthetic process
D. amino acid metabolic process
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

> The sequence matches a UniProt entry annotated with GO:0000271, polysaccharide biosynthetic process, by IEA:InterPro. The entry also reports experimentally supported UDP-GlcNAc dehydrogenase activity in synthesis of a nucleotide-sugar precursor. The specific GO annotation is computational, not itself experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> No clear sequence feature or task context distinguishes polysaccharide biosynthesis from the other listed processes without identifying the protein’s specific enzymatic function.


**Missing item-specific fact**

> The protein’s identity and its experimentally characterized role converting UDP-GlcNAc toward UDP-XylNAc biosynthesis are not supplied in the question.


**Reason**

> Choosing C depends on the protein-specific substrate, product, and pathway assignment; these are not reliably established by general reasoning from the raw sequence and choices alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C is the only choice supported by the matched entry’s biological-process annotation and reported nucleotide-sugar biosynthetic role; the other options have no comparable support in the evidence.


### Important caveats

- The GO:0000271 annotation is IEA:InterPro, so it is a computational annotation rather than direct experimental assignment of that GO process.
- The reviewer-only accession was inferred from dataset metadata and was not provided to the evaluated model; the sequence match is confirmed, but the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "No clear sequence feature or task context distinguishes polysaccharide biosynthesis from the other listed processes without identifying the protein’s specific enzymatic function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein’s identity and its experimentally characterized role converting UDP-GlcNAc toward UDP-XylNAc biosynthesis are not supplied in the question.",
    "reason": "Choosing C depends on the protein-specific substrate, product, and pathway assignment; these are not reliably established by general reasoning from the raw sequence and choices alone."
  },
  "case_id": "GO_biological_process_0068",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches a UniProt entry annotated with GO:0000271, polysaccharide biosynthetic process, by IEA:InterPro. The entry also reports experimentally supported UDP-GlcNAc dehydrogenase activity in synthesis of a nucleotide-sugar precursor. The specific GO annotation is computational, not itself experimental evidence."
  },
  "important_caveats": [
    "The GO:0000271 annotation is IEA:InterPro, so it is a computational annotation rather than direct experimental assignment of that GO process.",
    "The reviewer-only accession was inferred from dataset metadata and was not provided to the evaluated model; the sequence match is confirmed, but the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the only choice supported by the matched entry’s biological-process annotation and reported nucleotide-sugar biosynthetic role; the other options have no comparable support in the evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches a UniProt entry annotated with GO:0000271, polysaccharide biosynthetic process, by IEA:InterPro. The entry also reports experimentally supported UDP-GlcNAc dehydrogenase activity in synthesis of a nucleotide-sugar precursor. The specific GO annotation is computational, not itself experimental evidence.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "No clear sequence feature or task context distinguishes polysaccharide biosynthesis from the other listed processes without identifying the protein’s specific enzymatic function.",
    "missing_item_specific_fact": "The protein’s identity and its experimentally characterized role converting UDP-GlcNAc toward UDP-XylNAc biosynthesis are not supplied in the question.",
    "reason": "Choosing C depends on the protein-specific substrate, product, and pathway assignment; these are not reliably established by general reasoning from the raw sequence and choices alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C is the only choice supported by the matched entry’s biological-process annotation and reported nucleotide-sugar biosynthetic role; the other options have no comparable support in the evidence."
  },
  "important_caveats": [
    "The GO:0000271 annotation is IEA:InterPro, so it is a computational annotation rather than direct experimental assignment of that GO process.",
    "The reviewer-only accession was inferred from dataset metadata and was not provided to the evaluated model; the sequence match is confirmed, but the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (UniProt A7GKX6) is experimentally characterized (PubMed:20529859, ECO:0000269) as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136), which converts UDP-GlcNAc to UDP-GlcNAcA, a nucleotide-sugar intermediate feeding into polysaccharide biosynthesis. The GO annotation GO:0000271 (polysaccharide biosynthetic process) is present in the entry (evidence code IEA:InterPro), and the GO term definition (GO1) covers 'chemical reactions and pathways resulting in the formation of a polysaccharide.' The underlying enzymatic function is experimentally verified; the GO term assignment is computational (IEA) but biologically consistent with the experimentally established role in nucleotide-sugar biosynthesis for polysaccharide assembly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could partially narrow choices by recognizing dehydrogenase-like fold features (e.g., a GxGxxG-type Rossmann motif 'GLGYVGLPL') to rule out A (translational elongation, requiring ribosomal factors) and B (zinc transport, requiring membrane-spanning transporter architecture). However, distinguishing C from D requires knowing that the specific substrate is a UDP-sugar nucleotide (UDP-GlcNAc), not an amino acid, and that its oxidation feeds into polysaccharide biosynthesis rather than amino acid metabolism. This substrate-specificity fact is not reliably extractable from the raw 423-aa sequence without recognizing the specific protein or its database annotation.


**Missing item-specific fact**

> The specific enzymatic substrate identity (UDP-N-acetylglucosamine) and the pathway context (nucleotide-sugar biosynthesis feeding into polysaccharide assembly), which are the decisive facts separating option C from option D.


**Reason**

> While general dehydrogenase recognition eliminates A and B, the C-vs-D distinction hinges on the item-specific substrate identity (a sugar nucleotide vs. an amino acid). The sequence alone does not unambiguously encode 'this enzyme acts on a UDP-sugar'; that requires either protein identification (lookup) or highly specialized motif knowledge of sugar-nucleotide dehydrogenases. The GO annotation itself is IEA:InterPro, confirming the assignment is database-driven rather than derivable from first-principles sequence reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A (cytoplasmic translational elongation) requires ribosomal/translation-factor architecture absent here. B (zinc ion transport) requires a membrane transporter, inconsistent with a soluble dehydrogenase. D (amino acid metabolic process) is incorrect because UDP-GlcNAc is a sugar nucleotide, not an amino acid; the N-acetyl group does not reclassify it under GO:0006520. Only C is consistent with the experimentally verified enzymatic role.


### Important caveats

- The GO:0000271 annotation carries evidence code IEA:InterPro (computational inference), not direct experimental GO curation; however, the underlying enzymatic function is experimentally verified (ECO:0000269, PubMed:20529859).
- The reviewer-only UniProt accession and annotations were absent from the evaluated model input; the model saw only the raw sequence and four options.
- The GO term GO:0000271 is a broad parent term; the protein's most specific role is 'nucleotide-sugar biosynthetic process' (a child of polysaccharide biosynthesis), but the option text matches the annotated parent term exactly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could partially narrow choices by recognizing dehydrogenase-like fold features (e.g., a GxGxxG-type Rossmann motif 'GLGYVGLPL') to rule out A (translational elongation, requiring ribosomal factors) and B (zinc transport, requiring membrane-spanning transporter architecture). However, distinguishing C from D requires knowing that the specific substrate is a UDP-sugar nucleotide (UDP-GlcNAc), not an amino acid, and that its oxidation feeds into polysaccharide biosynthesis rather than amino acid metabolism. This substrate-specificity fact is not reliably extractable from the raw 423-aa sequence without recognizing the specific protein or its database annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific enzymatic substrate identity (UDP-N-acetylglucosamine) and the pathway context (nucleotide-sugar biosynthesis feeding into polysaccharide assembly), which are the decisive facts separating option C from option D.",
    "reason": "While general dehydrogenase recognition eliminates A and B, the C-vs-D distinction hinges on the item-specific substrate identity (a sugar nucleotide vs. an amino acid). The sequence alone does not unambiguously encode 'this enzyme acts on a UDP-sugar'; that requires either protein identification (lookup) or highly specialized motif knowledge of sugar-nucleotide dehydrogenases. The GO annotation itself is IEA:InterPro, confirming the assignment is database-driven rather than derivable from first-principles sequence reasoning."
  },
  "case_id": "GO_biological_process_0068",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein (UniProt A7GKX6) is experimentally characterized (PubMed:20529859, ECO:0000269) as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136), which converts UDP-GlcNAc to UDP-GlcNAcA, a nucleotide-sugar intermediate feeding into polysaccharide biosynthesis. The GO annotation GO:0000271 (polysaccharide biosynthetic process) is present in the entry (evidence code IEA:InterPro), and the GO term definition (GO1) covers 'chemical reactions and pathways resulting in the formation of a polysaccharide.' The underlying enzymatic function is experimentally verified; the GO term assignment is computational (IEA) but biologically consistent with the experimentally established role in nucleotide-sugar biosynthesis for polysaccharide assembly."
  },
  "important_caveats": [
    "The GO:0000271 annotation carries evidence code IEA:InterPro (computational inference), not direct experimental GO curation; however, the underlying enzymatic function is experimentally verified (ECO:0000269, PubMed:20529859).",
    "The reviewer-only UniProt accession and annotations were absent from the evaluated model input; the model saw only the raw sequence and four options.",
    "The GO term GO:0000271 is a broad parent term; the protein's most specific role is 'nucleotide-sugar biosynthetic process' (a child of polysaccharide biosynthesis), but the option text matches the annotated parent term exactly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A (cytoplasmic translational elongation) requires ribosomal/translation-factor architecture absent here. B (zinc ion transport) requires a membrane transporter, inconsistent with a soluble dehydrogenase. D (amino acid metabolic process) is incorrect because UDP-GlcNAc is a sugar nucleotide, not an amino acid; the N-acetyl group does not reclassify it under GO:0006520. Only C is consistent with the experimentally verified enzymatic role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (UniProt A7GKX6) is experimentally characterized (PubMed:20529859, ECO:0000269) as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136), which converts UDP-GlcNAc to UDP-GlcNAcA, a nucleotide-sugar intermediate feeding into polysaccharide biosynthesis. The GO annotation GO:0000271 (polysaccharide biosynthetic process) is present in the entry (evidence code IEA:InterPro), and the GO term definition (GO1) covers 'chemical reactions and pathways resulting in the formation of a polysaccharide.' The underlying enzymatic function is experimentally verified; the GO term assignment is computational (IEA) but biologically consistent with the experimentally established role in nucleotide-sugar biosynthesis for polysaccharide assembly.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could partially narrow choices by recognizing dehydrogenase-like fold features (e.g., a GxGxxG-type Rossmann motif 'GLGYVGLPL') to rule out A (translational elongation, requiring ribosomal factors) and B (zinc transport, requiring membrane-spanning transporter architecture). However, distinguishing C from D requires knowing that the specific substrate is a UDP-sugar nucleotide (UDP-GlcNAc), not an amino acid, and that its oxidation feeds into polysaccharide biosynthesis rather than amino acid metabolism. This substrate-specificity fact is not reliably extractable from the raw 423-aa sequence without recognizing the specific protein or its database annotation.",
    "missing_item_specific_fact": "The specific enzymatic substrate identity (UDP-N-acetylglucosamine) and the pathway context (nucleotide-sugar biosynthesis feeding into polysaccharide assembly), which are the decisive facts separating option C from option D.",
    "reason": "While general dehydrogenase recognition eliminates A and B, the C-vs-D distinction hinges on the item-specific substrate identity (a sugar nucleotide vs. an amino acid). The sequence alone does not unambiguously encode 'this enzyme acts on a UDP-sugar'; that requires either protein identification (lookup) or highly specialized motif knowledge of sugar-nucleotide dehydrogenases. The GO annotation itself is IEA:InterPro, confirming the assignment is database-driven rather than derivable from first-principles sequence reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A (cytoplasmic translational elongation) requires ribosomal/translation-factor architecture absent here. B (zinc ion transport) requires a membrane transporter, inconsistent with a soluble dehydrogenase. D (amino acid metabolic process) is incorrect because UDP-GlcNAc is a sugar nucleotide, not an amino acid; the N-acetyl group does not reclassify it under GO:0006520. Only C is consistent with the experimentally verified enzymatic role."
  },
  "important_caveats": [
    "The GO:0000271 annotation carries evidence code IEA:InterPro (computational inference), not direct experimental GO curation; however, the underlying enzymatic function is experimentally verified (ECO:0000269, PubMed:20529859).",
    "The reviewer-only UniProt accession and annotations were absent from the evaluated model input; the model saw only the raw sequence and four options.",
    "The GO term GO:0000271 is a broad parent term; the protein's most specific role is 'nucleotide-sugar biosynthetic process' (a child of polysaccharide biosynthesis), but the option text matches the annotated parent term exactly."
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

**Accession:** `A7GKX6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 96. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"value":"1.1.1.136"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20529859","source":"PubMed"}],"value":"UDP-N-acetyl-D-glucosamine 6-dehydrogenase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"20529859","source":"PubMed"}],"value":"UDP-GlcNAc 6-dehydrogenase"}]}}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20529859","source":"PubMed"}],"value":"Dehydrogenase involved in the biosynthesis of the nucleotide-sugar UDP-N-acetylxylosamine (UDP-XylNAc) (PubMed:20529859). Catalyzes the conversion of UDP-N-acetylglucosamine (UDP-GlcNAc) to UDP-N-acetylglucosaminuronic acid (UDP-GlcNAcA) (PubMed:20529859). Cannot use UDP-glucose, UDP-galactose and UDP-N-acetylgalactosamine as substrates (PubMed:20529859)"}]}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A7GKX6.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:09.484643+00:00.  

```json
{"database":"GO","id":"GO:0000271","properties":[{"key":"GoTerm","value":"P:polysaccharide biosynthetic process"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `68eff0a78e5c0dadd87ed867729ca5fa907f1022d5a7d7c02ac69e250707cc4f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)  
**Locator:** `lines 34-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:27:11.633421+00:00.  

```text
CC   -!- FUNCTION: Dehydrogenase involved in the biosynthesis of the nucleotide-
CC       sugar UDP-N-acetylxylosamine (UDP-XylNAc) (PubMed:20529859). Catalyzes
CC       the conversion of UDP-N-acetylglucosamine (UDP-GlcNAc) to UDP-N-
CC       acetylglucosaminuronic acid (UDP-GlcNAcA) (PubMed:20529859). Cannot use
CC       UDP-glucose, UDP-galactose and UDP-N-acetylgalactosamine as substrates
CC       (PubMed:20529859). {ECO:0000269|PubMed:20529859}.
```

Source SHA-256: `d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A7GKX6?format=txt&versions=96)  
**Locator:** `lines 68-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 96 / 1.  
**Retrieved:** 2026-11-02T04:27:11.633421+00:00.  

```text
DR   GO; GO:0000271; P:polysaccharide biosynthetic process; IEA:InterPro.
```

Source SHA-256: `d8a31aa88fd823d2c4ea18977d36968e48e5c0bbc7cb1fe4c9e6ca7171435666`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 2936-2950`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0000271
name: polysaccharide biosynthetic process
namespace: biological_process
def: "The chemical reactions and pathways resulting in the formation of a polysaccharide, a polymer of many (typically more than 10) monosaccharide residues linked glycosidically." [GOC:curators]
synonym: "glycan biosynthesis" EXACT []
synonym: "glycan biosynthetic process" EXACT []
synonym: "polysaccharide anabolism" EXACT []
synonym: "polysaccharide biosynthesis" EXACT []
synonym: "polysaccharide formation" EXACT []
synonym: "polysaccharide synthesis" EXACT []
is_a: GO:0005976 ! polysaccharide metabolic process
is_a: GO:0009059 ! macromolecule biosynthetic process
is_a: GO:0016051 ! carbohydrate biosynthetic process

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 68. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
