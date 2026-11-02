# GO_cellular_component_0119

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQAYESGDERGLIYGYVLNGRGGGRRVGRNQIAVLDLLPEESLWLHWDRGVPEAQAWLRDSAGLSEFACDLLLEEATRPRLLDLGAESLLVFLRGVNLNPGAEPEDMVSLRVFADARRVISLRLRPLKAVADLLEDLEAGKGPKTASEVVYYLAHYLTDRVDTLISGIADQLDAVEELVEADERASPDQHQLRTLRRRSAGLRRYLAPQRDIYSQLARYKLSWFVEDDADYWNELNNRLTRNLEELELIRERISVLQEAESRRITERMNRTMYLLGIITGFFLPMSFVTGLLGINVGGIPGADAPHGFWLACLLIGGVATFQWWVFRRLRWL

[Multiple Choices]
A. plasma membrane
B. cytoplasm
C. aggresome
D. primosome complex
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

> The supplied sequence matches the annotated protein. UniProt records its cell-inner-membrane localization with experimental evidence, and assigns plasma membrane with experimental evidence; the GO term encompasses the bacterial inner membrane.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has strongly hydrophobic segments near its C-terminus, consistent with membrane-spanning helices. That supports a membrane location over cytoplasm, while aggresome and primosome complex are poor fits for a bacterial membrane protein.


**Missing item-specific fact**

> No protein-specific annotation is needed to make the membrane choice a defensible inference, although the precise experimental localization is not stated in the input.


**Reason**

> The sequence provides a concrete membrane-localization signal, and the options make the competing complex localizations biologically implausible.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The hydrophobic membrane-spanning segments favor plasma membrane over the non-membrane alternatives; the bacterial inner membrane corresponds to the relevant GO plasma-membrane term.


### Important caveats

- The reviewer-only annotation is sequence-matched and reports experimental evidence, but the author's exact annotation snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has strongly hydrophobic segments near its C-terminus, consistent with membrane-spanning helices. That supports a membrane location over cytoplasm, while aggresome and primosome complex are poor fits for a bacterial membrane protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation is needed to make the membrane choice a defensible inference, although the precise experimental localization is not stated in the input.",
    "reason": "The sequence provides a concrete membrane-localization signal, and the options make the competing complex localizations biologically implausible."
  },
  "case_id": "GO_cellular_component_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated protein. UniProt records its cell-inner-membrane localization with experimental evidence, and assigns plasma membrane with experimental evidence; the GO term encompasses the bacterial inner membrane."
  },
  "important_caveats": [
    "The reviewer-only annotation is sequence-matched and reports experimental evidence, but the author's exact annotation snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The hydrophobic membrane-spanning segments favor plasma membrane over the non-membrane alternatives; the bacterial inner membrane corresponds to the relevant GO plasma-membrane term."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated protein. UniProt records its cell-inner-membrane localization with experimental evidence, and assigns plasma membrane with experimental evidence; the GO term encompasses the bacterial inner membrane.",
    "evidence_ids": ["C5", "C6", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has strongly hydrophobic segments near its C-terminus, consistent with membrane-spanning helices. That supports a membrane location over cytoplasm, while aggresome and primosome complex are poor fits for a bacterial membrane protein.",
    "missing_item_specific_fact": "No protein-specific annotation is needed to make the membrane choice a defensible inference, although the precise experimental localization is not stated in the input.",
    "reason": "The sequence provides a concrete membrane-localization signal, and the options make the competing complex localizations biologically implausible."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The hydrophobic membrane-spanning segments favor plasma membrane over the non-membrane alternatives; the bacterial inner membrane corresponds to the relevant GO plasma-membrane term."
  },
  "important_caveats": [
    "The reviewer-only annotation is sequence-matched and reports experimental evidence, but the author's exact annotation snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9ZIH2 (CmaX, Pseudomonas aeruginosa PAO1) is experimentally annotated as a multi-pass membrane protein of the cell inner membrane (ECO:0000269, PubMed:34175341, cryo-EM structure PDB 7NH9). The GO term GO:0005886 'plasma membrane' carries the NARROW synonym 'bacterial inner membrane' and EXACT synonym 'cytoplasmic membrane' (evidence C6, GO2). Thus 'plasma membrane' is the correct GO Cellular Component term for this bacterial inner-membrane transporter, backed by experimental (EXP) evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal ~80 residues (LLGIITGFFLPMSFVTGLLGINVGGIPGADAPHGFWLACLLIGGVATFQWWVFRRLRWL) contain multiple contiguous hydrophobic stretches consistent with transmembrane helices, providing visible sequence-level evidence for membrane association. Additionally, distractor C (aggresome) is a eukaryotic dynein/microtubule-dependent inclusion body (GO3) and is biologically impossible for a prokaryotic protein; distractor D (primosome complex) is a DNA-replication helicase-primase complex (GO4) with no sequence resemblance to this protein. The remaining choice between A (plasma membrane) and B (cytoplasm) can be addressed by recognizing the hydrophobic TM-like segments as incompatible with a soluble cytoplasmic protein.


**Missing item-specific fact**

> None strictly required. The hydrophobic stretches are visible in the provided sequence, and the GO definitions supplied in the ontology excerpts allow elimination of C and D. However, confidently identifying the protein as multi-pass rather than peripherally associated would benefit from structural data.


**Reason**

> A general biologist can note the hydrophobic C-terminal region as suggestive of transmembrane helices, eliminate the eukaryotic-only aggresome and the replication-specific primosome, and choose plasma membrane over cytoplasm. The reasoning is not mathematically certain from sequence alone but constitutes a defensible biological argument using general knowledge of membrane protein sequence signatures.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly eliminable by general biological knowledge (aggresome is eukaryotic; primosome is a replication complex). The A-vs-B distinction is supported by visible hydrophobic stretches in the sequence. No other option is defensible.


### Important caveats

- The model is not told the organism is Pseudomonas aeruginosa; recognizing the bacterial context would strengthen the reasoning but is not strictly necessary since GO:0005886 applies to both prokaryotic and eukaryotic plasma membranes.
- The hydrophobic TM-like region is confined to the C-terminal ~80 of 332 residues; the majority of the protein is charged/polar, so the membrane signal is present but not overwhelming from sequence inspection alone.
- The GO annotation in the current UniProt entry is EXP (experimental, cryo-EM); in the historical archived version (entry 153) it was IEA (inferred from electronic annotation via UniProt-SubCell), though the underlying subcellular-location comment was already experimentally supported.
- The reviewer-only evidence confirms the sequence match (SHA-256 identical) and that the expected answer aligns with experimental data, but this evidence was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal ~80 residues (LLGIITGFFLPMSFVTGLLGINVGGIPGADAPHGFWLACLLIGGVATFQWWVFRRLRWL) contain multiple contiguous hydrophobic stretches consistent with transmembrane helices, providing visible sequence-level evidence for membrane association. Additionally, distractor C (aggresome) is a eukaryotic dynein/microtubule-dependent inclusion body (GO3) and is biologically impossible for a prokaryotic protein; distractor D (primosome complex) is a DNA-replication helicase-primase complex (GO4) with no sequence resemblance to this protein. The remaining choice between A (plasma membrane) and B (cytoplasm) can be addressed by recognizing the hydrophobic TM-like segments as incompatible with a soluble cytoplasmic protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The hydrophobic stretches are visible in the provided sequence, and the GO definitions supplied in the ontology excerpts allow elimination of C and D. However, confidently identifying the protein as multi-pass rather than peripherally associated would benefit from structural data.",
    "reason": "A general biologist can note the hydrophobic C-terminal region as suggestive of transmembrane helices, eliminate the eukaryotic-only aggresome and the replication-specific primosome, and choose plasma membrane over cytoplasm. The reasoning is not mathematically certain from sequence alone but constitutes a defensible biological argument using general knowledge of membrane protein sequence signatures."
  },
  "case_id": "GO_cellular_component_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9ZIH2 (CmaX, Pseudomonas aeruginosa PAO1) is experimentally annotated as a multi-pass membrane protein of the cell inner membrane (ECO:0000269, PubMed:34175341, cryo-EM structure PDB 7NH9). The GO term GO:0005886 'plasma membrane' carries the NARROW synonym 'bacterial inner membrane' and EXACT synonym 'cytoplasmic membrane' (evidence C6, GO2). Thus 'plasma membrane' is the correct GO Cellular Component term for this bacterial inner-membrane transporter, backed by experimental (EXP) evidence."
  },
  "important_caveats": [
    "The model is not told the organism is Pseudomonas aeruginosa; recognizing the bacterial context would strengthen the reasoning but is not strictly necessary since GO:0005886 applies to both prokaryotic and eukaryotic plasma membranes.",
    "The hydrophobic TM-like region is confined to the C-terminal ~80 of 332 residues; the majority of the protein is charged/polar, so the membrane signal is present but not overwhelming from sequence inspection alone.",
    "The GO annotation in the current UniProt entry is EXP (experimental, cryo-EM); in the historical archived version (entry 153) it was IEA (inferred from electronic annotation via UniProt-SubCell), though the underlying subcellular-location comment was already experimentally supported.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) and that the expected answer aligns with experimental data, but this evidence was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminable by general biological knowledge (aggresome is eukaryotic; primosome is a replication complex). The A-vs-B distinction is supported by visible hydrophobic stretches in the sequence. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9ZIH2 (CmaX, Pseudomonas aeruginosa PAO1) is experimentally annotated as a multi-pass membrane protein of the cell inner membrane (ECO:0000269, PubMed:34175341, cryo-EM structure PDB 7NH9). The GO term GO:0005886 'plasma membrane' carries the NARROW synonym 'bacterial inner membrane' and EXACT synonym 'cytoplasmic membrane' (evidence C6, GO2). Thus 'plasma membrane' is the correct GO Cellular Component term for this bacterial inner-membrane transporter, backed by experimental (EXP) evidence.",
    "evidence_ids": ["C5", "C6", "C7", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal ~80 residues (LLGIITGFFLPMSFVTGLLGINVGGIPGADAPHGFWLACLLIGGVATFQWWVFRRLRWL) contain multiple contiguous hydrophobic stretches consistent with transmembrane helices, providing visible sequence-level evidence for membrane association. Additionally, distractor C (aggresome) is a eukaryotic dynein/microtubule-dependent inclusion body (GO3) and is biologically impossible for a prokaryotic protein; distractor D (primosome complex) is a DNA-replication helicase-primase complex (GO4) with no sequence resemblance to this protein. The remaining choice between A (plasma membrane) and B (cytoplasm) can be addressed by recognizing the hydrophobic TM-like segments as incompatible with a soluble cytoplasmic protein.",
    "missing_item_specific_fact": "None strictly required. The hydrophobic stretches are visible in the provided sequence, and the GO definitions supplied in the ontology excerpts allow elimination of C and D. However, confidently identifying the protein as multi-pass rather than peripherally associated would benefit from structural data.",
    "reason": "A general biologist can note the hydrophobic C-terminal region as suggestive of transmembrane helices, eliminate the eukaryotic-only aggresome and the replication-specific primosome, and choose plasma membrane over cytoplasm. The reasoning is not mathematically certain from sequence alone but constitutes a defensible biological argument using general knowledge of membrane protein sequence signatures."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly eliminable by general biological knowledge (aggresome is eukaryotic; primosome is a replication complex). The A-vs-B distinction is supported by visible hydrophobic stretches in the sequence. No other option is defensible."
  },
  "important_caveats": [
    "The model is not told the organism is Pseudomonas aeruginosa; recognizing the bacterial context would strengthen the reasoning but is not strictly necessary since GO:0005886 applies to both prokaryotic and eukaryotic plasma membranes.",
    "The hydrophobic TM-like region is confined to the C-terminal ~80 of 332 residues; the majority of the protein is charged/polar, so the membrane signal is present but not overwhelming from sequence inspection alone.",
    "The GO annotation in the current UniProt entry is EXP (experimental, cryo-EM); in the historical archived version (entry 153) it was IEA (inferred from electronic annotation via UniProt-SubCell), though the underlying subcellular-location comment was already experimentally supported.",
    "The reviewer-only evidence confirms the sequence match (SHA-256 identical) and that the expected answer aligns with experimental data, but this evidence was not available to the evaluated model."
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

**Accession:** `Q9ZIH2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 153. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)  
**Locator:** `/comments/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:54.880542+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"34175341","source":"PubMed"}],"id":"SL-0037","value":"Cell inner membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000269","id":"34175341","source":"PubMed"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)  
**Locator:** `/uniProtKBCrossReferences/23`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:54.880542+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"34175341","source":"PubMed"}],"id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9ZIH2.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:54.880542+00:00.  

```json
{"citation":{"authors":["Stetsenko A.","Stehantsev P.","Dranenko N.O.","Gelfand M.S.","Guskov A."],"citationCrossReferences":[{"database":"PubMed","id":"34175341"},{"database":"DOI","id":"10.1016/j.ijbiomac.2021.06.130"}],"citationType":"journal article","firstPage":"760","id":"34175341","journal":"Int. J. Biol. Macromol.","lastPage":"767","publicationDate":"2021","title":"Structural and biochemical characterization of a novel ZntB (CmaX) transporter protein from Pseudomonas aeruginosa.","volume":"184"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7NH9","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 15692 / DSM 22644 / CIP 104116 / JCM 14847 / LMG 12228 / 1C / PRS 101 / PAO1"}],"referenceNumber":3,"referencePositions":["STRUCTURE BY ELECTRON MICROSCOPY (3.03 ANGSTROMS)","FUNCTION","TRANSPORTER ACTIVITY","SUBUNIT","SUBCELLULAR LOCATION","TOPOLOGY"]}
```

Source SHA-256: `a00f4c0271bbd4fae7afeb16e71be27aaff79dadde11086a04686cc2d5355d0e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)  
**Locator:** `lines 66-68`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 1.  
**Retrieved:** 2026-11-02T04:33:58.139616+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell inner membrane
CC       {ECO:0000269|PubMed:34175341}; Multi-pass membrane protein
CC       {ECO:0000269|PubMed:34175341}.
```

Source SHA-256: `ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9ZIH2?format=txt&versions=153)  
**Locator:** `lines 98-98`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 153 / 1.  
**Retrieved:** 2026-11-02T04:33:58.139616+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `ef1f3b913665475f320bd32d9a7e46b733d69ecc2d4104881ec5fd04fc3481b9`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 60420-60454`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005886
name: plasma membrane
namespace: cellular_component
alt_id: GO:0005887
alt_id: GO:0005904
def: "The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins." [ISBN:0716731363]
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "bacterial inner membrane" NARROW []
synonym: "cell membrane" EXACT []
synonym: "cellular membrane" EXACT [NIF_Subcellular:sao6433132645]
synonym: "cytoplasmic membrane" EXACT []
synonym: "inner endospore membrane" NARROW []
synonym: "integral component of plasma membrane" NARROW []
synonym: "integral to plasma membrane" NARROW []
synonym: "juxtamembrane" BROAD []
synonym: "plasma membrane lipid bilayer" NARROW [GOC:mah]
synonym: "plasmalemma" EXACT []
xref: NIF_Subcellular:sao1663586795
xref: Wikipedia:Cell_membrane
is_a: GO:0016020 ! membrane
relationship: part_of GO:0071944 ! cell periphery

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 124908-124915`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0016235
name: aggresome
namespace: cellular_component
def: "An inclusion body formed by dynein-dependent retrograde transport of an aggregated protein on microtubules." [PMID:11121744]
xref: Wikipedia:Aggresome
is_a: GO:0016234 ! inclusion body

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 549032-549040`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:1990077
name: primosome complex
namespace: cellular_component
def: "Any of a family of protein complexes that form at the origin of replication or stalled replication forks and function in replication primer synthesis in all organisms. Early complexes initiate double-stranded DNA unwinding. The core unit consists of a replicative helicase and a primase. The helicase further unwinds the DNA and recruits the polymerase machinery. The primase synthesizes RNA primers that act as templates for complementary stand replication by the polymerase machinery. The primosome contains a number of associated proteins and protein complexes and contributes to the processes of replication initiation, lagging strand elongation, and replication restart." [GOC:bhm, GOC:mah, PMID:21856207]
synonym: "primosome" EXACT []
is_a: GO:0032993 ! protein-DNA complex
relationship: part_of GO:0030894 ! replisome

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 119. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
