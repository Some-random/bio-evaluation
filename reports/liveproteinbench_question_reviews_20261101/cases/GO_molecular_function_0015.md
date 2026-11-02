# GO_molecular_function_0015

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — exo-alpha-sialidase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MEPSKLFTISDNATFAPGPVINVADKKTFRTCFRILVLSVQAVTLILVIVNLGELVRMINDQGLSNQLSSITDKIRESANMIASAVGVMNQVIHGVTVSLPLQIEGNQNQLLSTLATICTSKKQVSNCSTNIPLVNDLRFINGINKFIIEDYATHDFSIGHPLNMPSFIPTATSPNGCTRIPSFSLGKTHWCYTHNVINANCKDHTSSNQYVSMGILVQTASGYPMFKTLKIQYLSDGLNRKSCSIATVPDGCAMYCYISTQLETDDYAGSSPPTQKLTLLFYNDTVTERTISPSGLEGNWATLVPGVGSGIYFENKLIFPAYGGVLPNSTLGVKSAREFFRPVNPYNPCSGPQQDLDQRALRSYFPSYFSNRRVQSAFLVCAWNQILVTNCELVVPSNNQTLMGAEGRVLLINNRLLYYQRSTSWWPYELLYEISFTFTNSGQSSVNMSWIPIYSFTRPGSGNCSGENVCPTACVSGVYLDPWPLTPYSHQSGINRNFYFTGALLNSSTTRVNPTLYVSALNNLKVLAPYGTQGLFASYTTTTCFQDTGDASVYCVYIMELASNIVGEFQILPVLTRLTIT

[Multiple Choices]
A. exo-alpha-sialidase activity
B. ribosome binding
C. zinc ion transmembrane transporter activity
D. misfolded protein binding
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence matches the UniProt entry for mumps virus hemagglutinin-neuraminidase, whose annotated catalytic activity is hydrolysis of terminal sialic acid linkages (EC 3.2.1.18), corresponding to exo-alpha-sialidase activity. The cited UniProt functional and catalytic annotations are transferred by similarity, not direct experimental evidence for this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment and overall sequence are consistent with a membrane-associated viral glycoprotein, making ribosome binding and zinc transport less plausible. But those broad features do not specifically establish sialidase catalysis over other membrane-protein functions.


**Missing item-specific fact**

> The specific assignment of this sequence to a hemagglutinin-neuraminidase with sialidase activity, or equivalent protein-specific functional/domain annotation, is absent from the prompt.


**Reason**

> Choosing A requires the specific functional identity or a reliable recognition of its protein-specific catalytic features; general sequence and biological reasoning alone do not establish that activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, exo-alpha-sialidase activity is supported for this protein. Its additional receptor-binding role is not one of the options.


### Important caveats

- The sequence match is exact, but the retrieved functional evidence is primarily similarity-based rather than direct experimental evidence for this sequence.
- The exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and overall sequence are consistent with a membrane-associated viral glycoprotein, making ribosome binding and zinc transport less plausible. But those broad features do not specifically establish sialidase catalysis over other membrane-protein functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific assignment of this sequence to a hemagglutinin-neuraminidase with sialidase activity, or equivalent protein-specific functional/domain annotation, is absent from the prompt.",
    "reason": "Choosing A requires the specific functional identity or a reliable recognition of its protein-specific catalytic features; general sequence and biological reasoning alone do not establish that activity."
  },
  "case_id": "GO_molecular_function_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C7",
      "C8",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for mumps virus hemagglutinin-neuraminidase, whose annotated catalytic activity is hydrolysis of terminal sialic acid linkages (EC 3.2.1.18), corresponding to exo-alpha-sialidase activity. The cited UniProt functional and catalytic annotations are transferred by similarity, not direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The sequence match is exact, but the retrieved functional evidence is primarily similarity-based rather than direct experimental evidence for this sequence.",
    "The exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, exo-alpha-sialidase activity is supported for this protein. Its additional receptor-binding role is not one of the options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for mumps virus hemagglutinin-neuraminidase, whose annotated catalytic activity is hydrolysis of terminal sialic acid linkages (EC 3.2.1.18), corresponding to exo-alpha-sialidase activity. The cited UniProt functional and catalytic annotations are transferred by similarity, not direct experimental evidence for this exact protein.",
    "evidence_ids": ["C1", "C4", "C7", "C8", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and overall sequence are consistent with a membrane-associated viral glycoprotein, making ribosome binding and zinc transport less plausible. But those broad features do not specifically establish sialidase catalysis over other membrane-protein functions.",
    "missing_item_specific_fact": "The specific assignment of this sequence to a hemagglutinin-neuraminidase with sialidase activity, or equivalent protein-specific functional/domain annotation, is absent from the prompt.",
    "reason": "Choosing A requires the specific functional identity or a reliable recognition of its protein-specific catalytic features; general sequence and biological reasoning alone do not establish that activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, exo-alpha-sialidase activity is supported for this protein. Its additional receptor-binding role is not one of the options."
  },
  "important_caveats": [
    "The sequence match is exact, but the retrieved functional evidence is primarily similarity-based rather than direct experimental evidence for this sequence.",
    "The exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q5SC51 (Mumps virus Hemagglutinin-neuraminidase, HN protein, 582 aa). UniProt assigns EC 3.2.1.18 and GO:0004308 (exo-alpha-sialidase activity) with ISS evidence from related paramyxovirus HN proteins. The catalytic activity comment explicitly describes hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)-glycosidic linkages of terminal sialic acid residues, which is the definition of GO:0004308. The GO term text matches option A exactly.

Citations as saved: [C4](#evidence-c4), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence encodes a type II viral surface glycoprotein: it has an N-terminal signal peptide, a single transmembrane anchor, and a large C-terminal ectodomain (~582 aa total). This architecture is incompatible with ribosomal proteins (B), zinc-ion transmembrane transporters (C, which require specific Zn-binding motifs and multi-TM topology), and molecular chaperones/misfolded-protein binders (D, which have characteristic ATPase or substrate-binding domains). Among the four options, only exo-alpha-sialidase activity (A) is consistent with a viral attachment glycoprotein possessing an enzymatic ectodomain. Paramyxovirus HN proteins are well-known to combine receptor-binding with neuraminidase (sialidase) activity for viral spread. The conserved neuraminidase motifs (e.g., the R-Y-R and R-E-S catalytic motifs visible in the ectodomain) further support an exo-alpha-sialidase assignment over the other three options.


**Missing item-specific fact**

> None strictly required. While confirming the exact GO term benefits from recognizing the sequence as a paramyxovirus HN protein, the three distractors are eliminated by basic architectural and functional incompatibility arguments available from general biology.


**Reason**

> The distractors (ribosome binding, zinc transporter, misfolded protein binding) are all clearly incompatible with the observed sequence architecture (viral type II membrane glycoprotein with enzymatic ectodomain). Elimination reasoning grounded in protein architecture and viral biology distinguishes A from B, C, D without requiring a database lookup of this specific entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors are structurally and functionally incompatible with the sequence. Ribosome binding requires ribosomal protein folds; zinc transport requires specific multi-TM transporter architecture with Zn-coordinating residues; misfolded protein binding requires chaperone domains. None of these features are present. Only exo-alpha-sialidase activity is consistent with a paramyxovirus HN-type viral glycoprotein.


### Important caveats

- The UniProt annotation for Q5SC51 is primarily inferred by sequence similarity (ECO:0000250, ISS) from related paramyxovirus HN proteins (Q9WAF5, Q786F2, Q91UL0) rather than direct experimental characterization of this specific mumps strain.
- The GO:0004308 annotation carries evidence code ISS:UniProtKB (or IEA:UniProtKB-EC in the archived flat file), meaning it is propagated from the EC assignment rather than from direct enzyme assays on this protein.
- The reviewer-only evidence was not available to the evaluated model; the reasoning assessment considers only what a model could derive from the sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence encodes a type II viral surface glycoprotein: it has an N-terminal signal peptide, a single transmembrane anchor, and a large C-terminal ectodomain (~582 aa total). This architecture is incompatible with ribosomal proteins (B), zinc-ion transmembrane transporters (C, which require specific Zn-binding motifs and multi-TM topology), and molecular chaperones/misfolded-protein binders (D, which have characteristic ATPase or substrate-binding domains). Among the four options, only exo-alpha-sialidase activity (A) is consistent with a viral attachment glycoprotein possessing an enzymatic ectodomain. Paramyxovirus HN proteins are well-known to combine receptor-binding with neuraminidase (sialidase) activity for viral spread. The conserved neuraminidase motifs (e.g., the R-Y-R and R-E-S catalytic motifs visible in the ectodomain) further support an exo-alpha-sialidase assignment over the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. While confirming the exact GO term benefits from recognizing the sequence as a paramyxovirus HN protein, the three distractors are eliminated by basic architectural and functional incompatibility arguments available from general biology.",
    "reason": "The distractors (ribosome binding, zinc transporter, misfolded protein binding) are all clearly incompatible with the observed sequence architecture (viral type II membrane glycoprotein with enzymatic ectodomain). Elimination reasoning grounded in protein architecture and viral biology distinguishes A from B, C, D without requiring a database lookup of this specific entry."
  },
  "case_id": "GO_molecular_function_0015",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C7",
      "C8",
      "H4",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q5SC51 (Mumps virus Hemagglutinin-neuraminidase, HN protein, 582 aa). UniProt assigns EC 3.2.1.18 and GO:0004308 (exo-alpha-sialidase activity) with ISS evidence from related paramyxovirus HN proteins. The catalytic activity comment explicitly describes hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)-glycosidic linkages of terminal sialic acid residues, which is the definition of GO:0004308. The GO term text matches option A exactly."
  },
  "important_caveats": [
    "The UniProt annotation for Q5SC51 is primarily inferred by sequence similarity (ECO:0000250, ISS) from related paramyxovirus HN proteins (Q9WAF5, Q786F2, Q91UL0) rather than direct experimental characterization of this specific mumps strain.",
    "The GO:0004308 annotation carries evidence code ISS:UniProtKB (or IEA:UniProtKB-EC in the archived flat file), meaning it is propagated from the EC assignment rather than from direct enzyme assays on this protein.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment considers only what a model could derive from the sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are structurally and functionally incompatible with the sequence. Ribosome binding requires ribosomal protein folds; zinc transport requires specific multi-TM transporter architecture with Zn-coordinating residues; misfolded protein binding requires chaperone domains. None of these features are present. Only exo-alpha-sialidase activity is consistent with a paramyxovirus HN-type viral glycoprotein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0015",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q5SC51 (Mumps virus Hemagglutinin-neuraminidase, HN protein, 582 aa). UniProt assigns EC 3.2.1.18 and GO:0004308 (exo-alpha-sialidase activity) with ISS evidence from related paramyxovirus HN proteins. The catalytic activity comment explicitly describes hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)-glycosidic linkages of terminal sialic acid residues, which is the definition of GO:0004308. The GO term text matches option A exactly.",
    "evidence_ids": ["C4", "C7", "C8", "H4", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence encodes a type II viral surface glycoprotein: it has an N-terminal signal peptide, a single transmembrane anchor, and a large C-terminal ectodomain (~582 aa total). This architecture is incompatible with ribosomal proteins (B), zinc-ion transmembrane transporters (C, which require specific Zn-binding motifs and multi-TM topology), and molecular chaperones/misfolded-protein binders (D, which have characteristic ATPase or substrate-binding domains). Among the four options, only exo-alpha-sialidase activity (A) is consistent with a viral attachment glycoprotein possessing an enzymatic ectodomain. Paramyxovirus HN proteins are well-known to combine receptor-binding with neuraminidase (sialidase) activity for viral spread. The conserved neuraminidase motifs (e.g., the R-Y-R and R-E-S catalytic motifs visible in the ectodomain) further support an exo-alpha-sialidase assignment over the other three options.",
    "missing_item_specific_fact": "None strictly required. While confirming the exact GO term benefits from recognizing the sequence as a paramyxovirus HN protein, the three distractors are eliminated by basic architectural and functional incompatibility arguments available from general biology.",
    "reason": "The distractors (ribosome binding, zinc transporter, misfolded protein binding) are all clearly incompatible with the observed sequence architecture (viral type II membrane glycoprotein with enzymatic ectodomain). Elimination reasoning grounded in protein architecture and viral biology distinguishes A from B, C, D without requiring a database lookup of this specific entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are structurally and functionally incompatible with the sequence. Ribosome binding requires ribosomal protein folds; zinc transport requires specific multi-TM transporter architecture with Zn-coordinating residues; misfolded protein binding requires chaperone domains. None of these features are present. Only exo-alpha-sialidase activity is consistent with a paramyxovirus HN-type viral glycoprotein."
  },
  "important_caveats": [
    "The UniProt annotation for Q5SC51 is primarily inferred by sequence similarity (ECO:0000250, ISS) from related paramyxovirus HN proteins (Q9WAF5, Q786F2, Q91UL0) rather than direct experimental characterization of this specific mumps strain.",
    "The GO:0004308 annotation carries evidence code ISS:UniProtKB (or IEA:UniProtKB-EC in the archived flat file), meaning it is propagated from the EC assignment rather than from direct enzyme assays on this protein.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment considers only what a model could derive from the sequence and general biological knowledge."
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

**Accession:** `Q5SC51` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 105. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
"Q5SC51"
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9WAF5","source":"UniProtKB"}],"value":"3.2.1.18"}],"fullName":{"value":"Hemagglutinin-neuraminidase"}}}
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.18","evidences":[{"evidenceCode":"ECO:0000250","id":"Q9WAF5","source":"UniProtKB"}],"name":"Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)- glycosidic linkages of terminal sialic acid residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates."}}
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC51.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:29.846842+00:00.  

```json
{"database":"GO","id":"GO:0004308","properties":[{"key":"GoTerm","value":"F:exo-alpha-sialidase activity"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `84cb4071f2488c26b98cb3a00a95cf7fafbb3f15b4205e39b2029f487b04b1c3`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)  
**Locator:** `lines 51-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:31:32.054381+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-
CC         (2->8)- glycosidic linkages of terminal sialic acid residues in
CC         oligosaccharides, glycoproteins, glycolipids, colominic acid and
CC         synthetic substrates.; EC=3.2.1.18;
CC         Evidence={ECO:0000250|UniProtKB:Q9WAF5};
```

Source SHA-256: `8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC51?format=txt&versions=105)  
**Locator:** `lines 82-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 105 / 1.  
**Retrieved:** 2026-11-02T04:31:32.054381+00:00.  

```text
DR   GO; GO:0004308; F:exo-alpha-sialidase activity; IEA:UniProtKB-EC.
```

Source SHA-256: `8bf1ba1afc5634387cc3311f78ac6fc61cefd51f3d1e338d340ea041cd46beeb`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 39493-39517`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004308
name: exo-alpha-sialidase activity
namespace: molecular_function
def: "Catalysis of the hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)-glycosidic linkages of terminal sialic residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates." [EC:3.2.1.18]
synonym: "acetylneuraminidase activity" RELATED [EC:3.2.1.18]
synonym: "acetylneuraminyl hydrolase activity" RELATED [EC:3.2.1.18]
synonym: "alpha-neuraminidase activity" RELATED [EC:3.2.1.18]
synonym: "N-acylneuraminate glycohydrolase activity" RELATED [EC:3.2.1.18]
synonym: "neuraminidase activity" RELATED [EC:3.2.1.18]
synonym: "sialidase activity" RELATED [EC:3.2.1.18]
xref: EC:3.2.1.18
xref: MetaCyc:3.2.1.18-RXN
xref: Reactome:R-HSA-1605723 "NEU2 cleaves GM3 to form LacCer (cytosol)"
xref: Reactome:R-HSA-1605724 "NEU1,4 hydrolyze PSAP(195-273):GM3:PE"
xref: Reactome:R-HSA-1605768 "NEU3 cleaves GM3 to form LacCer (plasma membrane)"
xref: Reactome:R-HSA-168870 "Neuraminidase enzymatic release from sialic acid"
xref: Reactome:R-HSA-4084994 "NEU3 hydrolyzes Neu5Ac from glycoconjugates"
xref: Reactome:R-HSA-4084999 "NEU1 hydrolyses Neu5Ac from glycoconjugates"
xref: Reactome:R-HSA-4085029 "NEU2 hydrolyzes Neu5Ac from glycoconjugates"
xref: Reactome:R-HSA-4341669 "Defective NEU1 does not hydrolyse Neu5Ac from glycoconjugates"
xref: Reactome:R-HSA-9638120 "NEU4 hydrolyses Neu5Ac from glycoconjugates"
is_a: GO:0016997 ! alpha-sialidase activity
property_value: skos:exactMatch EC:3.2.1.18

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 15. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
