# GO_molecular_function_0142

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — DNA-binding transcription factor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MELRDWLRVDVKAGKPLFDQLRTQVIDGVRAGALPPGTRLPTVRDLAGQLGVAANTVARAYRELESAAIVETRGRFGTFISRFDPTDAAMAAAAKEYVGVARALGLTKSDAMRYLTHVPDD

[Multiple Choices]
A. calmodulin binding
B. DNA-binding transcription factor activity
C. calcium ion binding
D. xylan 1,4-beta-xylosidase activity
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

> The matched 121-aa sequence is annotated as an HTH-type transcriptional regulator, and cited functional studies describe transcriptional regulation. The specific GO annotation for DNA-binding transcription factor activity is computational (IEA:InterPro), rather than direct experimental evidence of DNA binding in the supplied excerpts, but it is consistent with the protein identity and function.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence is a compact, largely helix-compatible protein with a plausible N-terminal HTH-like DNA-binding region. That architecture favors a bacterial transcription factor over a xylan-degrading enzyme; the sequence also lacks an evident calcium-binding EF-hand pattern. These are predictive clues, not proof.


**Missing item-specific fact**

> No external fact is indispensable for a plausible choice, though verified domain annotation or direct DNA-binding evidence is not supplied.


**Reason**

> The sequence and choices provide a meaningful domain-level basis to favor B over the unrelated enzyme and calcium-binding options. Identifying the exact protein or recalling its database entry is not needed for that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B is the best-supported choice among the options; the sequence-based inference is not definitive, but no alternative is comparably supported.


### Important caveats

- The sequence matches the cited UniProt record, but that identity and its annotations were reviewer-only information.
- The supplied evidence supports transcriptional regulation and a curator-assigned HTH-type name; the specific GO term is InterPro-inferred, and the excerpts do not independently establish direct DNA binding experimentally.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence is a compact, largely helix-compatible protein with a plausible N-terminal HTH-like DNA-binding region. That architecture favors a bacterial transcription factor over a xylan-degrading enzyme; the sequence also lacks an evident calcium-binding EF-hand pattern. These are predictive clues, not proof.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No external fact is indispensable for a plausible choice, though verified domain annotation or direct DNA-binding evidence is not supplied.",
    "reason": "The sequence and choices provide a meaningful domain-level basis to favor B over the unrelated enzyme and calcium-binding options. Identifying the exact protein or recalling its database entry is not needed for that inference."
  },
  "case_id": "GO_molecular_function_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The matched 121-aa sequence is annotated as an HTH-type transcriptional regulator, and cited functional studies describe transcriptional regulation. The specific GO annotation for DNA-binding transcription factor activity is computational (IEA:InterPro), rather than direct experimental evidence of DNA binding in the supplied excerpts, but it is consistent with the protein identity and function."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but that identity and its annotations were reviewer-only information.",
    "The supplied evidence supports transcriptional regulation and a curator-assigned HTH-type name; the specific GO term is InterPro-inferred, and the excerpts do not independently establish direct DNA binding experimentally."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the best-supported choice among the options; the sequence-based inference is not definitive, but no alternative is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched 121-aa sequence is annotated as an HTH-type transcriptional regulator, and cited functional studies describe transcriptional regulation. The specific GO annotation for DNA-binding transcription factor activity is computational (IEA:InterPro), rather than direct experimental evidence of DNA binding in the supplied excerpts, but it is consistent with the protein identity and function.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence is a compact, largely helix-compatible protein with a plausible N-terminal HTH-like DNA-binding region. That architecture favors a bacterial transcription factor over a xylan-degrading enzyme; the sequence also lacks an evident calcium-binding EF-hand pattern. These are predictive clues, not proof.",
    "missing_item_specific_fact": "No external fact is indispensable for a plausible choice, though verified domain annotation or direct DNA-binding evidence is not supplied.",
    "reason": "The sequence and choices provide a meaningful domain-level basis to favor B over the unrelated enzyme and calcium-binding options. Identifying the exact protein or recalling its database entry is not needed for that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B is the best-supported choice among the options; the sequence-based inference is not definitive, but no alternative is comparably supported."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but that identity and its annotations were reviewer-only information.",
    "The supplied evidence supports transcriptional regulation and a curator-assigned HTH-type name; the specific GO term is InterPro-inferred, and the excerpts do not independently establish direct DNA binding experimentally."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry O06550 annotates this 121-aa protein as an 'HTH-type transcriptional regulator Rv1152' (C4) with experimentally supported function as a transcriptional regulator (ECO:0000269, PubMed:27349953, 35898907; C5/H4). GO:0003700 (DNA-binding transcription factor activity) is assigned via IEA:InterPro (C6/H6), consistent with the HTH domain and the protein's demonstrated role in negative regulation of gene expression. The GO term definition (GO1) matches the protein's activity. While the specific GO:0003700 annotation is computational (IEA), the underlying transcriptional regulator function with DNA binding is experimentally confirmed.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO1](#evidence-go1).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Elimination arguments exist: (1) 121 aa is too small for a glycosidase, ruling out D; (2) no EF-hand or canonical calcium-binding motif is apparent, weakly arguing against C; (3) calmodulin binding is essentially a eukaryotic phenomenon and no calmodulin-binding amphipathic helix is evident, arguing against A. The sequence is predominantly alpha-helical (high Ala, Leu, Val, Glu), consistent with a small DNA-binding regulator. However, the positive identification of the HTH motif in the region ~residues 80-120 ('GVARALGLTKSDAMRYLTH') is not textbook-obvious from the raw sequence and requires structural prediction or domain-database tools to confidently assign.


**Missing item-specific fact**

> Confident positive identification of the GntR-family HTH DNA-binding domain from this specific 121-aa sequence requires running a domain-prediction tool (e.g., InterProScan, HHpred) or recognizing the exact sequence from database memory. The HTH periodicity here is subtle and not the canonical textbook example that would allow unambiguous visual identification.


**Reason**

> While elimination of D (size) and weak arguments against A and C provide some reasoning grounds, the positive assignment of 'DNA-binding transcription factor activity' from this sequence depends on recognizing the HTH motif, which is not trivially apparent without computational domain prediction or prior knowledge of this specific protein. The question is answerable by elimination of clearly wrong options, but the positive evidence for B is not strongly encoded in the raw sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is clearly eliminated by size (121 aa vs. typical glycosidase >200 aa). A is strongly disfavored because calmodulin binding is a eukaryotic-specific interaction and no calmodulin-binding motif is present. C is weakly disfavored by absence of calcium-binding motifs. B is the only option consistent with the helical content and small size of the protein. No genuine ambiguity among the choices.


### Important caveats

- The GO:0003700 annotation is IEA:InterPro (computational), not directly experimental, though the protein's transcriptional regulator function is experimentally supported.
- The model is not given organism information; ruling out calmodulin binding (A) requires inferring the protein is bacterial from sequence features or general knowledge.
- The HTH motif in this GntR-family regulator is in the C-terminal half of this small protein, which is atypical (GntR HTH domains are often N-terminal), making visual identification harder.
- The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt O06550.
- The GO annotation was first publicly released 2025-02-05; if the benchmark was constructed earlier, the annotation may not have been available at construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Elimination arguments exist: (1) 121 aa is too small for a glycosidase, ruling out D; (2) no EF-hand or canonical calcium-binding motif is apparent, weakly arguing against C; (3) calmodulin binding is essentially a eukaryotic phenomenon and no calmodulin-binding amphipathic helix is evident, arguing against A. The sequence is predominantly alpha-helical (high Ala, Leu, Val, Glu), consistent with a small DNA-binding regulator. However, the positive identification of the HTH motif in the region ~residues 80-120 ('GVARALGLTKSDAMRYLTH') is not textbook-obvious from the raw sequence and requires structural prediction or domain-database tools to confidently assign.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Confident positive identification of the GntR-family HTH DNA-binding domain from this specific 121-aa sequence requires running a domain-prediction tool (e.g., InterProScan, HHpred) or recognizing the exact sequence from database memory. The HTH periodicity here is subtle and not the canonical textbook example that would allow unambiguous visual identification.",
    "reason": "While elimination of D (size) and weak arguments against A and C provide some reasoning grounds, the positive assignment of 'DNA-binding transcription factor activity' from this sequence depends on recognizing the HTH motif, which is not trivially apparent without computational domain prediction or prior knowledge of this specific protein. The question is answerable by elimination of clearly wrong options, but the positive evidence for B is not strongly encoded in the raw sequence alone."
  },
  "case_id": "GO_molecular_function_0142",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5",
      "H6",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry O06550 annotates this 121-aa protein as an 'HTH-type transcriptional regulator Rv1152' (C4) with experimentally supported function as a transcriptional regulator (ECO:0000269, PubMed:27349953, 35898907; C5/H4). GO:0003700 (DNA-binding transcription factor activity) is assigned via IEA:InterPro (C6/H6), consistent with the HTH domain and the protein's demonstrated role in negative regulation of gene expression. The GO term definition (GO1) matches the protein's activity. While the specific GO:0003700 annotation is computational (IEA), the underlying transcriptional regulator function with DNA binding is experimentally confirmed."
  },
  "important_caveats": [
    "The GO:0003700 annotation is IEA:InterPro (computational), not directly experimental, though the protein's transcriptional regulator function is experimentally supported.",
    "The model is not given organism information; ruling out calmodulin binding (A) requires inferring the protein is bacterial from sequence features or general knowledge.",
    "The HTH motif in this GntR-family regulator is in the C-terminal half of this small protein, which is atypical (GntR HTH domains are often N-terminal), making visual identification harder.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt O06550.",
    "The GO annotation was first publicly released 2025-02-05; if the benchmark was constructed earlier, the annotation may not have been available at construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is clearly eliminated by size (121 aa vs. typical glycosidase >200 aa). A is strongly disfavored because calmodulin binding is a eukaryotic-specific interaction and no calmodulin-binding motif is present. C is weakly disfavored by absence of calcium-binding motifs. B is the only option consistent with the helical content and small size of the protein. No genuine ambiguity among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0142",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry O06550 annotates this 121-aa protein as an 'HTH-type transcriptional regulator Rv1152' (C4) with experimentally supported function as a transcriptional regulator (ECO:0000269, PubMed:27349953, 35898907; C5/H4). GO:0003700 (DNA-binding transcription factor activity) is assigned via IEA:InterPro (C6/H6), consistent with the HTH domain and the protein's demonstrated role in negative regulation of gene expression. The GO term definition (GO1) matches the protein's activity. While the specific GO:0003700 annotation is computational (IEA), the underlying transcriptional regulator function with DNA binding is experimentally confirmed.",
    "evidence_ids": ["C4", "C5", "C6", "H4", "H5", "H6", "GO1"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Elimination arguments exist: (1) 121 aa is too small for a glycosidase, ruling out D; (2) no EF-hand or canonical calcium-binding motif is apparent, weakly arguing against C; (3) calmodulin binding is essentially a eukaryotic phenomenon and no calmodulin-binding amphipathic helix is evident, arguing against A. The sequence is predominantly alpha-helical (high Ala, Leu, Val, Glu), consistent with a small DNA-binding regulator. However, the positive identification of the HTH motif in the region ~residues 80-120 ('GVARALGLTKSDAMRYLTH') is not textbook-obvious from the raw sequence and requires structural prediction or domain-database tools to confidently assign.",
    "missing_item_specific_fact": "Confident positive identification of the GntR-family HTH DNA-binding domain from this specific 121-aa sequence requires running a domain-prediction tool (e.g., InterProScan, HHpred) or recognizing the exact sequence from database memory. The HTH periodicity here is subtle and not the canonical textbook example that would allow unambiguous visual identification.",
    "reason": "While elimination of D (size) and weak arguments against A and C provide some reasoning grounds, the positive assignment of 'DNA-binding transcription factor activity' from this sequence depends on recognizing the HTH motif, which is not trivially apparent without computational domain prediction or prior knowledge of this specific protein. The question is answerable by elimination of clearly wrong options, but the positive evidence for B is not strongly encoded in the raw sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is clearly eliminated by size (121 aa vs. typical glycosidase >200 aa). A is strongly disfavored because calmodulin binding is a eukaryotic-specific interaction and no calmodulin-binding motif is present. C is weakly disfavored by absence of calcium-binding motifs. B is the only option consistent with the helical content and small size of the protein. No genuine ambiguity among the choices."
  },
  "important_caveats": [
    "The GO:0003700 annotation is IEA:InterPro (computational), not directly experimental, though the protein's transcriptional regulator function is experimentally supported.",
    "The model is not given organism information; ruling out calmodulin binding (A) requires inferring the protein is bacterial from sequence features or general knowledge.",
    "The HTH motif in this GntR-family regulator is in the C-terminal half of this small protein, which is atypical (GntR HTH domains are often N-terminal), making visual identification harder.",
    "The reviewer-only evidence confirms sequence match (SHA256 identical) between the benchmark sequence and UniProt O06550.",
    "The GO annotation was first publicly released 2025-02-05; if the benchmark was constructed earlier, the annotation may not have been available at construction time."
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

**Accession:** `O06550` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 163. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O06550.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:07.032497+00:00.  

```json
"O06550"
```

Source SHA-256: `c7ab1f2688438fb4baf505af551bbb720e92c739974db2ad5f042ca1ccd9e558`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O06550.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:07.032497+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"HTH-type transcriptional regulator Rv1152"}}}
```

Source SHA-256: `c7ab1f2688438fb4baf505af551bbb720e92c739974db2ad5f042ca1ccd9e558`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O06550.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:07.032497+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"27349953","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"35898907","source":"PubMed"}],"value":"Transcriptional regulator that modulates resistance to vancomycin and aminoglycosides (PubMed:27349953, PubMed:35898907). Negatively regulates the expression of several genes responsive to vancomycin, resulting in decreased susceptibility of bacteria to vancomycin (PubMed:27349953). Negatively regulates the expression of genes encoding the ribosome binding protein Hsp, the small subunit of sulfate adenylyltransferase CysD, the L-lysine-epsilon aminotransferase LAT and the protease HtpX (PubMed:27349953). Also modulates purine metabolism and aminoglycoside antibiotic resistance (PubMed:35898907). Negatively regulates the expression of purine metabolism-related genes and the accumulation of purine metabolites, which affects aminoglycoside antibiotic resistance (PubMed:35898907)"}]}
```

Source SHA-256: `c7ab1f2688438fb4baf505af551bbb720e92c739974db2ad5f042ca1ccd9e558`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O06550.json)  
**Locator:** `/uniProtKBCrossReferences/21`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:07.032497+00:00.  

```json
{"database":"GO","id":"GO:0003700","properties":[{"key":"GoTerm","value":"F:DNA-binding transcription factor activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `c7ab1f2688438fb4baf505af551bbb720e92c739974db2ad5f042ca1ccd9e558`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O06550?format=txt&versions=163)  
**Locator:** `lines 57-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 163 / 1.  
**Retrieved:** 2026-11-02T04:29:09.238836+00:00.  

```text
CC   -!- FUNCTION: Transcriptional regulator that modulates resistance to
CC       vancomycin and aminoglycosides (PubMed:27349953, PubMed:35898907).
CC       Negatively regulates the expression of several genes responsive to
CC       vancomycin, resulting in decreased susceptibility of bacteria to
CC       vancomycin (PubMed:27349953). Negatively regulates the expression of
CC       genes encoding the ribosome binding protein Hsp, the small subunit of
CC       sulfate adenylyltransferase CysD, the L-lysine-epsilon aminotransferase
CC       LAT and the protease HtpX (PubMed:27349953). Also modulates purine
CC       metabolism and aminoglycoside antibiotic resistance (PubMed:35898907).
CC       Negatively regulates the expression of purine metabolism-related genes
CC       and the accumulation of purine metabolites, which affects
CC       aminoglycoside antibiotic resistance (PubMed:35898907).
CC       {ECO:0000269|PubMed:27349953, ECO:0000269|PubMed:35898907}.
```

Source SHA-256: `b202ed49330900f70cf624f1be0cc4acbf4176ebe1d4c740e96474ec85c8038e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O06550?format=txt&versions=163)  
**Locator:** `lines 101-101`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 163 / 1.  
**Retrieved:** 2026-11-02T04:29:09.238836+00:00.  

```text
DR   GO; GO:0003677; F:DNA binding; IEA:UniProtKB-KW.
```

Source SHA-256: `b202ed49330900f70cf624f1be0cc4acbf4176ebe1d4c740e96474ec85c8038e`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O06550?format=txt&versions=163)  
**Locator:** `lines 102-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 163 / 1.  
**Retrieved:** 2026-11-02T04:29:09.238836+00:00.  

```text
DR   GO; GO:0003700; F:DNA-binding transcription factor activity; IEA:InterPro.
```

Source SHA-256: `b202ed49330900f70cf624f1be0cc4acbf4176ebe1d4c740e96474ec85c8038e`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 28009-28049`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0003700
name: DNA-binding transcription factor activity
namespace: molecular_function
alt_id: GO:0000130
alt_id: GO:0001071
alt_id: GO:0001130
alt_id: GO:0001131
alt_id: GO:0001151
alt_id: GO:0001199
alt_id: GO:0001204
def: "A transcription regulator activity that modulates transcription of gene sets via selective and non-covalent binding to a specific double-stranded genomic DNA sequence (sometimes referred to as a motif) within a cis-regulatory region. Regulatory regions include promoters (proximal and distal) and enhancers. Genes are transcriptional units, and include bacterial operons." [GOC:txnOH-2018]
comment: Usage guidance: Most DNA-binding transcription factors do not have enzymatic activity. The presence of specific DNA-binding domains known to be present in DNA-binding transcription factors (HOX, GATA etc) should be used to help decide whether a protein is a DNA binding transcription factor or a coregulator. If a protein has an enzymatic activity (for example, ubiquitin ligase, histone acetyl transferase) and no known DNA binding domain, consider annotating to GO:0003712 transcription coregulator activity. Special care should be taken with proteins containing zinc fingers, Myb/SANT and ARID domains, since only a subset of proteins containing these domains directly and selectively bind to regulatory DNA motifs in cis-regulatory regions.
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_plant
subset: goslim_yeast
synonym: "bacterial-type DNA binding transcription factor activity" NARROW []
synonym: "bacterial-type RNA polymerase core promoter proximal region sequence-specific DNA binding transcription factor activity" NARROW []
synonym: "bacterial-type RNA polymerase transcription enhancer sequence-specific DNA binding transcription factor activity" NARROW []
synonym: "bacterial-type RNA polymerase transcription factor activity, metal ion regulated sequence-specific DNA binding" NARROW []
synonym: "bacterial-type RNA polymerase transcription factor activity, sequence-specific DNA binding" NARROW []
synonym: "DNA binding transcription factor activity" EXACT []
synonym: "gene-specific transcription factor activity" EXACT []
synonym: "metal ion regulated sequence-specific DNA binding bacterial-type RNA polymerase transcription factor activity" NARROW []
synonym: "metal ion regulated sequence-specific DNA binding transcription factor activity" NARROW []
synonym: "nucleic acid binding transcription factor activity" BROAD []
synonym: "sequence-specific DNA binding bacterial-type RNA polymerase transcription factor activity" NARROW []
synonym: "sequence-specific DNA binding transcription factor activity" EXACT []
synonym: "transcription factor activity" BROAD []
synonym: "transcription factor activity, bacterial-type RNA polymerase core promoter proximal region sequence-specific binding" NARROW []
synonym: "transcription factor activity, bacterial-type RNA polymerase proximal promoter sequence-specific DNA binding" NARROW []
synonym: "transcription factor activity, bacterial-type RNA polymerase transcription enhancer sequence-specific binding" NARROW []
synonym: "transcription factor activity, metal ion regulated sequence-specific DNA binding" NARROW []
xref: Reactome:R-HSA-163666 "Formation of ChREBP:MLX heterodimer"
is_a: GO:0140110 ! transcription regulator activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 142. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
