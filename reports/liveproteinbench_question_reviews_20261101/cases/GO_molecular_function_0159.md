# GO_molecular_function_0159

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — single-stranded DNA binding

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTNRLELSGIICRTPLRKVSPSGIPHCQFVLEHRSVQEEAGFHRQAWCQMPVIISGHENQAITHSITVGSAVTVRGFISCHKAKNGLSKMVLHAEQIELIDSGD

[Multiple Choices]
A. flavin adenine dinucleotide binding
B. single-stranded DNA binding
C. isomerase activity
D. oxidoreductase activity, acting on NAD(P)H, oxygen as acceptor
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

> The supplied sequence exactly matches the cited PriB protein. Its UniProt annotation reports ssDNA binding with experimental evidence (ECO:0000269), and the matched record also carries the single-stranded DNA-binding GO annotation. This supports choice B.

Citations as saved: [C1](#evidence-c1), [C6](#evidence-c6), [C7](#evidence-c7), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The 104-residue sequence alone does not provide a sufficiently specific, reliable basis to distinguish ssDNA binding from the listed alternatives.


**Missing item-specific fact**

> The protein's identity as PriB and its experimentally reported DNA-binding activity are not supplied in the question; these protein-specific facts distinguish B.


**Reason**

> The key is supported by reviewer-only annotation and experimental evidence, but those facts were absent from the evaluated input. Generic sequence-based reasoning does not establish this precise molecular function.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched protein has evidence for ssDNA binding, while the other choices are not supported by the supplied sequence or reviewer-only evidence.


### Important caveats

- The evidence includes both computational UniProt annotations and an experimentally evidenced ssDNA-binding annotation; these evidence types should not be conflated.
- The protein is also reported to bind dsDNA, but that does not undermine the specifically supported ssDNA-binding choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 104-residue sequence alone does not provide a sufficiently specific, reliable basis to distinguish ssDNA binding from the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity as PriB and its experimentally reported DNA-binding activity are not supplied in the question; these protein-specific facts distinguish B.",
    "reason": "The key is supported by reviewer-only annotation and experimental evidence, but those facts were absent from the evaluated input. Generic sequence-based reasoning does not establish this precise molecular function."
  },
  "case_id": "GO_molecular_function_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C6",
      "C7",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited PriB protein. Its UniProt annotation reports ssDNA binding with experimental evidence (ECO:0000269), and the matched record also carries the single-stranded DNA-binding GO annotation. This supports choice B."
  },
  "important_caveats": [
    "The evidence includes both computational UniProt annotations and an experimentally evidenced ssDNA-binding annotation; these evidence types should not be conflated.",
    "The protein is also reported to bind dsDNA, but that does not undermine the specifically supported ssDNA-binding choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein has evidence for ssDNA binding, while the other choices are not supported by the supplied sequence or reviewer-only evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the cited PriB protein. Its UniProt annotation reports ssDNA binding with experimental evidence (ECO:0000269), and the matched record also carries the single-stranded DNA-binding GO annotation. This supports choice B.",
    "evidence_ids": ["C1", "C6", "C7", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The 104-residue sequence alone does not provide a sufficiently specific, reliable basis to distinguish ssDNA binding from the listed alternatives.",
    "missing_item_specific_fact": "The protein's identity as PriB and its experimentally reported DNA-binding activity are not supplied in the question; these protein-specific facts distinguish B.",
    "reason": "The key is supported by reviewer-only annotation and experimental evidence, but those facts were absent from the evaluated input. Generic sequence-based reasoning does not establish this precise molecular function."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched protein has evidence for ssDNA binding, while the other choices are not supported by the supplied sequence or reviewer-only evidence."
  },
  "important_caveats": [
    "The evidence includes both computational UniProt annotations and an experimentally evidenced ssDNA-binding annotation; these evidence types should not be conflated.",
    "The protein is also reported to bind dsDNA, but that does not undermine the specifically supported ssDNA-binding choice."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is UniProt A6THB2 (PriB, replication restart protein from Klebsiella pneumoniae). UniProt C6/H5 states 'Binds single-stranded (ss)DNA at the primosome assembly site (PAS)' with experimental evidence code ECO:0000269 (direct assay) from PubMed:22938024, corroborated by crystal structure PDB:4APV (C8/H3). The GO annotation GO:0003697 (single-stranded DNA binding) is assigned via IEA:UniProtKB-UniRule (C7/H6). The other options (FAD binding, isomerase activity, oxidoreductase activity) are not supported by any annotation for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H5](#evidence-h5), [H6](#evidence-h6), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Elimination of options A, C, and D is partially feasible from general knowledge: FAD binding requires a Rossmann fold (GxGxxG motif absent), isomerase and oxidoreductase activities require catalytic residues and cofactor-binding motifs absent from this 104-aa protein. This narrows the field to B. However, positively identifying 'single-stranded DNA binding' specifically (rather than protein-protein binding, dsDNA binding, or other binding activities) requires recognizing the OB-fold or knowing that PriB is a replication restart protein that binds ssDNA at the primosome assembly site. The sequence alone does not provide a clear, unambiguous OB-fold signature recognizable without structural prediction or prior knowledge of PriB.


**Missing item-specific fact**

> Knowledge that this specific 104-aa sequence corresponds to PriB, a replication restart protein whose characterized molecular function is binding single-stranded DNA at the primosome assembly site (PAS), supported by crystal structure PDB:4APV and biochemical assays.


**Reason**

> While the three enzymatic/cofactor-binding distractors can be eliminated by noting the absence of catalytic and cofactor-binding motifs (general biological reasoning), the positive assignment to 'single-stranded DNA binding' rather than other binding activities requires item-specific knowledge of PriB's function or confident OB-fold recognition from sequence alone, which is not reliably achievable without structural prediction tools or database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D describe enzymatic or cofactor-binding activities that require structural motifs (Rossmann fold, catalytic residues) clearly absent from this small non-enzymatic protein. Option B is the only binding activity and is the sole defensible choice. The distractors are sufficiently distinct that no ambiguity arises among them.


### Important caveats

- The GO:0003697 annotation carries evidence code IEA (Inferred from Electronic Annotation via UniProtKB-UniRule), meaning the GO term assignment is computational. However, the underlying function comment is supported by direct experimental evidence (ECO:0000269, crystal structure PDB:4APV, and biochemical binding assays).
- The sequence is 104 amino acids; OB-fold recognition from sequence alone without structural prediction is unreliable, limiting the reasoning pathway to elimination rather than positive fold identification.
- The source accession (A6THB2) was inferred from dataset metadata and was not available to the evaluated model; the model sees only the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Elimination of options A, C, and D is partially feasible from general knowledge: FAD binding requires a Rossmann fold (GxGxxG motif absent), isomerase and oxidoreductase activities require catalytic residues and cofactor-binding motifs absent from this 104-aa protein. This narrows the field to B. However, positively identifying 'single-stranded DNA binding' specifically (rather than protein-protein binding, dsDNA binding, or other binding activities) requires recognizing the OB-fold or knowing that PriB is a replication restart protein that binds ssDNA at the primosome assembly site. The sequence alone does not provide a clear, unambiguous OB-fold signature recognizable without structural prediction or prior knowledge of PriB.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Knowledge that this specific 104-aa sequence corresponds to PriB, a replication restart protein whose characterized molecular function is binding single-stranded DNA at the primosome assembly site (PAS), supported by crystal structure PDB:4APV and biochemical assays.",
    "reason": "While the three enzymatic/cofactor-binding distractors can be eliminated by noting the absence of catalytic and cofactor-binding motifs (general biological reasoning), the positive assignment to 'single-stranded DNA binding' rather than other binding activities requires item-specific knowledge of PriB's function or confident OB-fold recognition from sequence alone, which is not reliably achievable without structural prediction tools or database lookup."
  },
  "case_id": "GO_molecular_function_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H5",
      "H6",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein is UniProt A6THB2 (PriB, replication restart protein from Klebsiella pneumoniae). UniProt C6/H5 states 'Binds single-stranded (ss)DNA at the primosome assembly site (PAS)' with experimental evidence code ECO:0000269 (direct assay) from PubMed:22938024, corroborated by crystal structure PDB:4APV (C8/H3). The GO annotation GO:0003697 (single-stranded DNA binding) is assigned via IEA:UniProtKB-UniRule (C7/H6). The other options (FAD binding, isomerase activity, oxidoreductase activity) are not supported by any annotation for this protein."
  },
  "important_caveats": [
    "The GO:0003697 annotation carries evidence code IEA (Inferred from Electronic Annotation via UniProtKB-UniRule), meaning the GO term assignment is computational. However, the underlying function comment is supported by direct experimental evidence (ECO:0000269, crystal structure PDB:4APV, and biochemical binding assays).",
    "The sequence is 104 amino acids; OB-fold recognition from sequence alone without structural prediction is unreliable, limiting the reasoning pathway to elimination rather than positive fold identification.",
    "The source accession (A6THB2) was inferred from dataset metadata and was not available to the evaluated model; the model sees only the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D describe enzymatic or cofactor-binding activities that require structural motifs (Rossmann fold, catalytic residues) clearly absent from this small non-enzymatic protein. Option B is the only binding activity and is the sole defensible choice. The distractors are sufficiently distinct that no ambiguity arises among them."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is UniProt A6THB2 (PriB, replication restart protein from Klebsiella pneumoniae). UniProt C6/H5 states 'Binds single-stranded (ss)DNA at the primosome assembly site (PAS)' with experimental evidence code ECO:0000269 (direct assay) from PubMed:22938024, corroborated by crystal structure PDB:4APV (C8/H3). The GO annotation GO:0003697 (single-stranded DNA binding) is assigned via IEA:UniProtKB-UniRule (C7/H6). The other options (FAD binding, isomerase activity, oxidoreductase activity) are not supported by any annotation for this protein.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H5", "H6", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Elimination of options A, C, and D is partially feasible from general knowledge: FAD binding requires a Rossmann fold (GxGxxG motif absent), isomerase and oxidoreductase activities require catalytic residues and cofactor-binding motifs absent from this 104-aa protein. This narrows the field to B. However, positively identifying 'single-stranded DNA binding' specifically (rather than protein-protein binding, dsDNA binding, or other binding activities) requires recognizing the OB-fold or knowing that PriB is a replication restart protein that binds ssDNA at the primosome assembly site. The sequence alone does not provide a clear, unambiguous OB-fold signature recognizable without structural prediction or prior knowledge of PriB.",
    "missing_item_specific_fact": "Knowledge that this specific 104-aa sequence corresponds to PriB, a replication restart protein whose characterized molecular function is binding single-stranded DNA at the primosome assembly site (PAS), supported by crystal structure PDB:4APV and biochemical assays.",
    "reason": "While the three enzymatic/cofactor-binding distractors can be eliminated by noting the absence of catalytic and cofactor-binding motifs (general biological reasoning), the positive assignment to 'single-stranded DNA binding' rather than other binding activities requires item-specific knowledge of PriB's function or confident OB-fold recognition from sequence alone, which is not reliably achievable without structural prediction tools or database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D describe enzymatic or cofactor-binding activities that require structural motifs (Rossmann fold, catalytic residues) clearly absent from this small non-enzymatic protein. Option B is the only binding activity and is the sole defensible choice. The distractors are sufficiently distinct that no ambiguity arises among them."
  },
  "important_caveats": [
    "The GO:0003697 annotation carries evidence code IEA (Inferred from Electronic Annotation via UniProtKB-UniRule), meaning the GO term assignment is computational. However, the underlying function comment is supported by direct experimental evidence (ECO:0000269, crystal structure PDB:4APV, and biochemical binding assays).",
    "The sequence is 104 amino acids; OB-fold recognition from sequence alone without structural prediction is unreliable, limiting the reasoning pathway to elimination rather than positive fold identification.",
    "The source accession (A6THB2) was inferred from dataset metadata and was not available to the evaluated model; the model sees only the raw sequence."
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

**Accession:** `A6THB2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 62. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6THB2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.676093+00:00.  

```json
"A6THB2"
```

Source SHA-256: `112d26e808dc1fd38595dddb8c79bc1f7daa2f798cbd64dd9e82faff5c780e1c`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6THB2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.676093+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00720","source":"HAMAP-Rule"}],"value":"Replication restart protein PriB"}}}
```

Source SHA-256: `112d26e808dc1fd38595dddb8c79bc1f7daa2f798cbd64dd9e82faff5c780e1c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6THB2.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.676093+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_00720","source":"HAMAP-Rule"}],"value":"Involved in the restart of stalled replication forks, which reloads the replicative helicase on sites far from the origin of replication; the PriA-PriB pathway is the major replication restart pathway. During primosome assembly it facilitates complex formation between PriA and DnaT on DNA; stabilizes PriA on DNA. Stimulates the DNA unwinding activity of PriA helicase"}]}
```

Source SHA-256: `112d26e808dc1fd38595dddb8c79bc1f7daa2f798cbd64dd9e82faff5c780e1c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6THB2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.676093+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22938024","source":"PubMed"}],"value":"Binds single-stranded (ss)DNA at the primosome assembly site (PAS). One study finds it binds 15 nucleotide (nt) ssDNA (PubMed:21931731). Another study finds the minimal ssDNA length for binding to PriB is 25 nt; prefers dT(30) over dA(30) (PubMed:22938024). Also binds 22 nt dsDNA (PubMed:22938024)"}]}
```

Source SHA-256: `112d26e808dc1fd38595dddb8c79bc1f7daa2f798cbd64dd9e82faff5c780e1c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6THB2.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.676093+00:00.  

```json
{"database":"GO","id":"GO:0003697","properties":[{"key":"GoTerm","value":"F:single-stranded DNA binding"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-UniRule"}]}
```

Source SHA-256: `112d26e808dc1fd38595dddb8c79bc1f7daa2f798cbd64dd9e82faff5c780e1c`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A6THB2.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:59.676093+00:00.  

```json
{"citation":{"authors":["Huang Y.H.","Lo Y.H.","Huang W.","Huang C.Y."],"citationCrossReferences":[{"database":"PubMed","id":"22938024"},{"database":"DOI","id":"10.1111/gtc.12001"}],"citationType":"journal article","firstPage":"837","id":"22938024","journal":"Genes Cells","lastPage":"849","publicationDate":"2012","title":"Crystal structure and DNA-binding mode of Klebsiella pneumoniae primosomal PriB protein.","volume":"17"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4APV","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 700721 / MGH 78578"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.10 ANGSTROMS) OF 2-102","SEQUENCE REVISION TO N-TERMINUS","FUNCTION","DNA-BINDING","MUTAGENESIS OF PHE-42; ARG-44; TRP-47 AND LYS-82"]}
```

Source SHA-256: `112d26e808dc1fd38595dddb8c79bc1f7daa2f798cbd64dd9e82faff5c780e1c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6THB2?format=txt&versions=62)  
**Locator:** `lines 37-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 2.  
**Retrieved:** 2026-11-01T06:27:50.187758+00:00.  

```text
RN   [4] {ECO:0007744|PDB:4APV}
RP   X-RAY CRYSTALLOGRAPHY (2.10 ANGSTROMS) OF 2-102, SEQUENCE REVISION TO
RP   N-TERMINUS, FUNCTION, DNA-BINDING, AND MUTAGENESIS OF PHE-42; ARG-44;
RP   TRP-47 AND LYS-82.
RC   STRAIN=ATCC 700721 / MGH 78578;
RX   PubMed=22938024; DOI=10.1111/gtc.12001;
RA   Huang Y.H., Lo Y.H., Huang W., Huang C.Y.;
RT   "Crystal structure and DNA-binding mode of Klebsiella pneumoniae primosomal
RT   PriB protein.";
RL   Genes Cells 17:837-849(2012).
```

Source SHA-256: `dab4e075ff062d16bde88f88b9273b736fe7b9722b7009b1ba54f0a04e92086c`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6THB2?format=txt&versions=62)  
**Locator:** `lines 54-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 2.  
**Retrieved:** 2026-11-01T06:27:50.187758+00:00.  

```text
CC   -!- FUNCTION: Binds single-stranded (ss)DNA at the primosome assembly site
CC       (PAS). One study finds it binds 15 nucleotide (nt) ssDNA
CC       (PubMed:21931731). Another study finds the minimal ssDNA length for
CC       binding to PriB is 25 nt; prefers dT(30) over dA(30) (PubMed:22938024).
CC       Also binds 22 nt dsDNA (PubMed:22938024).
CC       {ECO:0000269|PubMed:22938024}.
```

Source SHA-256: `dab4e075ff062d16bde88f88b9273b736fe7b9722b7009b1ba54f0a04e92086c`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A6THB2?format=txt&versions=62)  
**Locator:** `lines 88-88`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 62 / 2.  
**Retrieved:** 2026-11-01T06:27:50.187758+00:00.  

```text
DR   GO; GO:0003697; F:single-stranded DNA binding; IEA:UniProtKB-UniRule.
```

Source SHA-256: `dab4e075ff062d16bde88f88b9273b736fe7b9722b7009b1ba54f0a04e92086c`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 27998-28008`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0003697
name: single-stranded DNA binding
namespace: molecular_function
alt_id: GO:0003698
alt_id: GO:0003699
def: "Binding to single-stranded DNA." [GOC:elh, GOC:vw, PMID:22976174]
comment: Note that this term is restricted to those cases where the binding is to a single-stranded DNA molecule, not to one of the stands of double-stranded DNA.
synonym: "ssDNA binding" EXACT [GOC:mah]
is_a: GO:0003677 ! DNA binding

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 159. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
