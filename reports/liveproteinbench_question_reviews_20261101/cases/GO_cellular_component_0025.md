# GO_cellular_component_0025

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — nucleoid

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASRGVNKVILVGNLGQDPEVRYMPSGGAVANFTLATSESWRDKQTGEMKEQTEWHRVVLFGKLAEVAGEYLRKGSQVYIEGQLRTRKWTDQSGQDKYTTEVVVNVGGTMQMLGGRQGGGAPAGGGQQQGGWGQPQQPQGGNQFSGGAQSRPQQQAPAAPSNEPPMDFDDDIPF

[Multiple Choices]
A. acrosomal membrane
B. symbiont-containing vacuole
C. mannosyltransferase complex
D. nucleoid
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence matches a bacterial single-stranded DNA-binding protein, and the matched UniProt record annotates it to the nucleoid (IEA:TreeGrafter). This is computational annotation, not direct experimental evidence, but it supports choice D.

Citations as saved: [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a bacterial SSB protein: its conserved N-terminal DNA-binding region and glycine-rich C-terminal tail support a role in binding single-stranded DNA. A bacterial DNA-binding protein is plausibly associated with the nucleoid; the other options describe eukaryotic structures or complexes.


**Missing item-specific fact**

> No essential item-specific fact is needed to distinguish these choices, although exact protein-family identification strengthens the inference.


**Reason**

> The sequence and biological role provide a defensible distinction for the nucleoid over the listed alternatives; this is not merely recognition of a database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, nucleoid is the biologically coherent location for a bacterial single-stranded DNA-binding protein.


### Important caveats

- The cited GO annotation is computational (IEA:TreeGrafter), not evidence of direct experimental localization.
- The sequence match is established for the cited record, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a bacterial SSB protein: its conserved N-terminal DNA-binding region and glycine-rich C-terminal tail support a role in binding single-stranded DNA. A bacterial DNA-binding protein is plausibly associated with the nucleoid; the other options describe eukaryotic structures or complexes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No essential item-specific fact is needed to distinguish these choices, although exact protein-family identification strengthens the inference.",
    "reason": "The sequence and biological role provide a defensible distinction for the nucleoid over the listed alternatives; this is not merely recognition of a database entry."
  },
  "case_id": "GO_cellular_component_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C3",
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches a bacterial single-stranded DNA-binding protein, and the matched UniProt record annotates it to the nucleoid (IEA:TreeGrafter). This is computational annotation, not direct experimental evidence, but it supports choice D."
  },
  "important_caveats": [
    "The cited GO annotation is computational (IEA:TreeGrafter), not evidence of direct experimental localization.",
    "The sequence match is established for the cited record, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, nucleoid is the biologically coherent location for a bacterial single-stranded DNA-binding protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches a bacterial single-stranded DNA-binding protein, and the matched UniProt record annotates it to the nucleoid (IEA:TreeGrafter). This is computational annotation, not direct experimental evidence, but it supports choice D.",
    "evidence_ids": ["C3", "C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a bacterial SSB protein: its conserved N-terminal DNA-binding region and glycine-rich C-terminal tail support a role in binding single-stranded DNA. A bacterial DNA-binding protein is plausibly associated with the nucleoid; the other options describe eukaryotic structures or complexes.",
    "missing_item_specific_fact": "No essential item-specific fact is needed to distinguish these choices, although exact protein-family identification strengthens the inference.",
    "reason": "The sequence and biological role provide a defensible distinction for the nucleoid over the listed alternatives; this is not merely recognition of a database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, nucleoid is the biologically coherent location for a bacterial single-stranded DNA-binding protein."
  },
  "important_caveats": [
    "The cited GO annotation is computational (IEA:TreeGrafter), not evidence of direct experimental localization.",
    "The sequence match is established for the cited record, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry A6TGW7 (SSB1_KLEP7), annotated as Single-stranded DNA-binding protein 1 from Klebsiella pneumoniae. The GO annotation GO:0009295 (C:nucleoid) is present, albeit via IEA:TreeGrafter (computational transfer). Biologically, SSB proteins bind single-stranded DNA during replication/repair/recombination; in a bacterium, DNA resides in the nucleoid. The protein name, domain architecture (OB-fold), and C-terminal acidic tail (DDDDIPF) are all consistent with an SSB protein functioning at DNA in the nucleoid. The annotation is computationally derived rather than experimentally validated, but the functional reasoning strongly supports the assignment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal ~120 residues exhibit the OB-fold (oligonucleotide/oligosaccharide-binding) β-barrel topology characteristic of nucleic-acid-binding proteins. The C-terminal region contains a glycine/glutamine-rich linker followed by a short acidic tail (DDDDIPF), a hallmark of bacterial SSB proteins that mediates protein-protein interactions with replication/repair machinery. Recognizing these features allows inference: (1) the protein binds DNA, (2) in a prokaryotic context (no signal peptide, no eukaryotic targeting motifs, bacterial-type OB-fold + acidic tail), DNA is in the nucleoid. The distractors are eliminable by general reasoning: no transmembrane helices or signal peptide rules out acrosomal membrane (A); no vacuolar targeting signals rule out symbiont-containing vacuole (B); no mannosyltransferase catalytic motifs rule out mannosyltransferase complex (C).


**Missing item-specific fact**

> None strictly required. The OB-fold and SSB-specific acidic C-terminal tail are recognizable sequence features, and the logical chain (DNA-binding protein → DNA-containing compartment → nucleoid in bacteria) is general biology. The organism identity (bacterium) can be inferred from the absence of eukaryotic features and the SSB-specific C-terminal architecture.


**Reason**

> A model with knowledge of the OB-fold motif and SSB protein architecture can reason from sequence features to DNA-binding function, then to the nucleoid as the bacterial DNA compartment. The distractors are eliminable without item-specific lookup. This does not require memorizing the exact UniProt entry for A6TGW7.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent highly distinct cellular compartments (sperm-specific membrane, host-cell vacuole, enzymatic complex, bacterial DNA region). A DNA-binding protein with no membrane or enzymatic-complex features is unambiguously placed in the nucleoid among these choices.


### Important caveats

- The GO nucleoid annotation carries evidence code IEA:TreeGrafter (computational transfer by similarity), not direct experimental localization data.
- The UniProt entry was first public in April 2025; the author's source snapshot date is unknown, though the sequence has been stable since 2007.
- The question does not explicitly state the organism is bacterial; the model must infer prokaryotic context from sequence features (no signal peptide, SSB-type acidic tail, OB-fold topology).
- Recognizing the OB-fold from raw sequence is specialized protein-structure knowledge but falls within the scope of general biological reasoning for a protein-science task.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal ~120 residues exhibit the OB-fold (oligonucleotide/oligosaccharide-binding) β-barrel topology characteristic of nucleic-acid-binding proteins. The C-terminal region contains a glycine/glutamine-rich linker followed by a short acidic tail (DDDDIPF), a hallmark of bacterial SSB proteins that mediates protein-protein interactions with replication/repair machinery. Recognizing these features allows inference: (1) the protein binds DNA, (2) in a prokaryotic context (no signal peptide, no eukaryotic targeting motifs, bacterial-type OB-fold + acidic tail), DNA is in the nucleoid. The distractors are eliminable by general reasoning: no transmembrane helices or signal peptide rules out acrosomal membrane (A); no vacuolar targeting signals rule out symbiont-containing vacuole (B); no mannosyltransferase catalytic motifs rule out mannosyltransferase complex (C).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The OB-fold and SSB-specific acidic C-terminal tail are recognizable sequence features, and the logical chain (DNA-binding protein → DNA-containing compartment → nucleoid in bacteria) is general biology. The organism identity (bacterium) can be inferred from the absence of eukaryotic features and the SSB-specific C-terminal architecture.",
    "reason": "A model with knowledge of the OB-fold motif and SSB protein architecture can reason from sequence features to DNA-binding function, then to the nucleoid as the bacterial DNA compartment. The distractors are eliminable without item-specific lookup. This does not require memorizing the exact UniProt entry for A6TGW7."
  },
  "case_id": "GO_cellular_component_0025",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A6TGW7 (SSB1_KLEP7), annotated as Single-stranded DNA-binding protein 1 from Klebsiella pneumoniae. The GO annotation GO:0009295 (C:nucleoid) is present, albeit via IEA:TreeGrafter (computational transfer). Biologically, SSB proteins bind single-stranded DNA during replication/repair/recombination; in a bacterium, DNA resides in the nucleoid. The protein name, domain architecture (OB-fold), and C-terminal acidic tail (DDDDIPF) are all consistent with an SSB protein functioning at DNA in the nucleoid. The annotation is computationally derived rather than experimentally validated, but the functional reasoning strongly supports the assignment."
  },
  "important_caveats": [
    "The GO nucleoid annotation carries evidence code IEA:TreeGrafter (computational transfer by similarity), not direct experimental localization data.",
    "The UniProt entry was first public in April 2025; the author's source snapshot date is unknown, though the sequence has been stable since 2007.",
    "The question does not explicitly state the organism is bacterial; the model must infer prokaryotic context from sequence features (no signal peptide, SSB-type acidic tail, OB-fold topology).",
    "Recognizing the OB-fold from raw sequence is specialized protein-structure knowledge but falls within the scope of general biological reasoning for a protein-science task."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct cellular compartments (sperm-specific membrane, host-cell vacuole, enzymatic complex, bacterial DNA region). A DNA-binding protein with no membrane or enzymatic-complex features is unambiguously placed in the nucleoid among these choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0025",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A6TGW7 (SSB1_KLEP7), annotated as Single-stranded DNA-binding protein 1 from Klebsiella pneumoniae. The GO annotation GO:0009295 (C:nucleoid) is present, albeit via IEA:TreeGrafter (computational transfer). Biologically, SSB proteins bind single-stranded DNA during replication/repair/recombination; in a bacterium, DNA resides in the nucleoid. The protein name, domain architecture (OB-fold), and C-terminal acidic tail (DDDDIPF) are all consistent with an SSB protein functioning at DNA in the nucleoid. The annotation is computationally derived rather than experimentally validated, but the functional reasoning strongly supports the assignment.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal ~120 residues exhibit the OB-fold (oligonucleotide/oligosaccharide-binding) β-barrel topology characteristic of nucleic-acid-binding proteins. The C-terminal region contains a glycine/glutamine-rich linker followed by a short acidic tail (DDDDIPF), a hallmark of bacterial SSB proteins that mediates protein-protein interactions with replication/repair machinery. Recognizing these features allows inference: (1) the protein binds DNA, (2) in a prokaryotic context (no signal peptide, no eukaryotic targeting motifs, bacterial-type OB-fold + acidic tail), DNA is in the nucleoid. The distractors are eliminable by general reasoning: no transmembrane helices or signal peptide rules out acrosomal membrane (A); no vacuolar targeting signals rule out symbiont-containing vacuole (B); no mannosyltransferase catalytic motifs rule out mannosyltransferase complex (C).",
    "missing_item_specific_fact": "None strictly required. The OB-fold and SSB-specific acidic C-terminal tail are recognizable sequence features, and the logical chain (DNA-binding protein → DNA-containing compartment → nucleoid in bacteria) is general biology. The organism identity (bacterium) can be inferred from the absence of eukaryotic features and the SSB-specific C-terminal architecture.",
    "reason": "A model with knowledge of the OB-fold motif and SSB protein architecture can reason from sequence features to DNA-binding function, then to the nucleoid as the bacterial DNA compartment. The distractors are eliminable without item-specific lookup. This does not require memorizing the exact UniProt entry for A6TGW7."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct cellular compartments (sperm-specific membrane, host-cell vacuole, enzymatic complex, bacterial DNA region). A DNA-binding protein with no membrane or enzymatic-complex features is unambiguously placed in the nucleoid among these choices."
  },
  "important_caveats": [
    "The GO nucleoid annotation carries evidence code IEA:TreeGrafter (computational transfer by similarity), not direct experimental localization data.",
    "The UniProt entry was first public in April 2025; the author's source snapshot date is unknown, though the sequence has been stable since 2007.",
    "The question does not explicitly state the organism is bacterial; the model must infer prokaryotic context from sequence features (no signal peptide, SSB-type acidic tail, OB-fold topology).",
    "Recognizing the OB-fold from raw sequence is specialized protein-structure knowledge but falls within the scope of general biological reasoning for a protein-science task."
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

**Accession:** `A6TGW7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 103. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGW7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.478301+00:00.  

```json
"A6TGW7"
```

Source SHA-256: `13bb1cd1c52711f4e7ccb9f8f81197919784539d90306c06e23f06f5f8aa042d`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGW7.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.478301+00:00.  

```json
{"lineage":["Bacteria","Pseudomonadati","Pseudomonadota","Gammaproteobacteria","Enterobacterales","Enterobacteriaceae","Klebsiella","Klebsiella pneumoniae complex"],"scientificName":"Klebsiella pneumoniae subsp. pneumoniae (strain ATCC 700721 / MGH 78578)","taxonId":272620}
```

Source SHA-256: `13bb1cd1c52711f4e7ccb9f8f81197919784539d90306c06e23f06f5f8aa042d`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGW7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.478301+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00984","source":"HAMAP-Rule"}],"value":"Single-stranded DNA-binding protein 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00984","source":"HAMAP-Rule"}],"value":"SSB 1"}]}}
```

Source SHA-256: `13bb1cd1c52711f4e7ccb9f8f81197919784539d90306c06e23f06f5f8aa042d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6TGW7.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.478301+00:00.  

```json
{"database":"GO","id":"GO:0009295","properties":[{"key":"GoTerm","value":"C:nucleoid"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `13bb1cd1c52711f4e7ccb9f8f81197919784539d90306c06e23f06f5f8aa042d`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6TGW7?format=txt&versions=103)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 103 / 1.  
**Retrieved:** 2026-11-01T06:27:46.242288+00:00.  

```text
ID   SSB1_KLEP7              Reviewed;         174 AA.
AC   A6TGW7;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   21-AUG-2007, sequence version 1.
DT   18-JUN-2025, entry version 103.
DE   RecName: Full=Single-stranded DNA-binding protein 1 {ECO:0000255|HAMAP-Rule:MF_00984};
DE            Short=SSB 1 {ECO:0000255|HAMAP-Rule:MF_00984};
GN   Name=ssb1 {ECO:0000312|EMBL:ABR79801.1};
GN   ORFNames=KPN_04446 {ECO:0000312|EMBL:ABR79801.1};
OS   Klebsiella pneumoniae subsp. pneumoniae (strain ATCC 700721 / MGH 78578).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Enterobacterales; Enterobacteriaceae; Klebsiella/Raoultella group;
OC   Klebsiella; Klebsiella pneumoniae complex.
OX   NCBI_TaxID=272620;
```

Source SHA-256: `797e2b883602726281d628ce75c121e420e501b33f7fa4c6c43ae907abdfb0d8`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6TGW7?format=txt&versions=103)  
**Locator:** `lines 66-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 103 / 1.  
**Retrieved:** 2026-11-01T06:27:46.242288+00:00.  

```text
DR   GO; GO:0009295; C:nucleoid; IEA:TreeGrafter.
```

Source SHA-256: `797e2b883602726281d628ce75c121e420e501b33f7fa4c6c43ae907abdfb0d8`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 94886-94893`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0009295
name: nucleoid
namespace: cellular_component
def: "The region of a virus, bacterial cell, mitochondrion or chloroplast to which the nucleic acid is confined." [GOC:bm, GOC:ma, ISBN:3540076689]
xref: Wikipedia:Nucleoid
is_a: GO:0110165 ! cellular anatomical structure

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 25. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
