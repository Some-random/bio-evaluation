# GO_molecular_function_0157

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **C** — G protein-coupled receptor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKQNPAKTARMWIIICLLFVLGQATDNDRDFKMCGKWLHGIAPQNLEYDLKTGCERIEISANESTLSIQGRITAKCTQSSSIQLDSNPHQNQSHFCVFWEPLLDLLIVEVNGKNHTLCKPNGLQGTCCTDLSQGVQDNAHMYGIVNGSVKGDIITGDLKGNYIFDGAHINCKEKFCDEARLKPRGANMIEEVVMRFNAKGRVDLPCAQGTVIEMDEEFTGHNFTVPAPRFVDANTIPSVYIPSSLRSVSRRKSKVVCTYYKNKTLFERGPSKSALLDDIVGLSVENETIRNLIEPVKIRFHHRPFAPDSSGRCVSWDTKQDNEVNWKDDGCDTVKINEEQTECHCNHLTYFAILVQVEQKSTVRHLKALTFITAVGCAVSLVSCLVLFYWLCKRRRGKKNQISLVHRGLVVAIFLLCLFFILTGILANVANETVCQLTGSLLHYGLLSTLCWMAMEVFHTFLLVRKVFNSPLPIWIFYLMGFGFPFLLVSILLSVGDIYGERKIKPSDDVNNPYRMCWMTEGDKSQLAHYIINIGLLAVVVSSGLVMLFLVVREIRNRPDWKKIHVAFLSIWGLTCLYGTTWALGFLDFGPFSEVTLFLFCIINSLQGFFLMLRYYALERMKKKDVSSSDGSSSGSSKQHMLQTNEKS

[Multiple Choices]
A. cardiolipin synthase activity
B. manganese ion binding
C. G protein-coupled receptor activity
D. rRNA (uridine-N3-)-methyltransferase activity
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

> The sequence matches the zebrafish ADGRG1 protein, and the matched entry annotates G protein-coupled receptor activity. Its function annotation is supported by cited experimental evidence for G-protein signaling; the GO term itself is annotated by computational inference (IEA:InterPro).

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a large extracellular N-terminal region followed by a cluster of seven strongly hydrophobic membrane-spanning segments and a cytoplasmic tail, a characteristic GPCR architecture. This meaningfully favors GPCR activity over the listed enzymatic alternatives.


**Missing item-specific fact**

> No protein-specific annotation is necessary to distinguish these choices at the broad functional level, though experimental evidence or family identification would confirm the receptor's precise activity.


**Reason**

> The supplied sequence itself provides a recognizable GPCR topology, while the distractors describe unrelated enzyme activities or ion binding.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The seven-transmembrane receptor architecture strongly distinguishes choice C from the other listed functions.


### Important caveats

- The reviewer-only database evidence supports the key but was not supplied to the evaluated model.
- The GO annotation is computationally inferred; separate cited experimental evidence supports the protein's G-protein signaling function.
- Sequence architecture supports the broad receptor classification but does not by itself establish every detail of ligand or signaling specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a large extracellular N-terminal region followed by a cluster of seven strongly hydrophobic membrane-spanning segments and a cytoplasmic tail, a characteristic GPCR architecture. This meaningfully favors GPCR activity over the listed enzymatic alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation is necessary to distinguish these choices at the broad functional level, though experimental evidence or family identification would confirm the receptor's precise activity.",
    "reason": "The supplied sequence itself provides a recognizable GPCR topology, while the distractors describe unrelated enzyme activities or ion binding."
  },
  "case_id": "GO_molecular_function_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the zebrafish ADGRG1 protein, and the matched entry annotates G protein-coupled receptor activity. Its function annotation is supported by cited experimental evidence for G-protein signaling; the GO term itself is annotated by computational inference (IEA:InterPro)."
  },
  "important_caveats": [
    "The reviewer-only database evidence supports the key but was not supplied to the evaluated model.",
    "The GO annotation is computationally inferred; separate cited experimental evidence supports the protein's G-protein signaling function.",
    "Sequence architecture supports the broad receptor classification but does not by itself establish every detail of ligand or signaling specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The seven-transmembrane receptor architecture strongly distinguishes choice C from the other listed functions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the zebrafish ADGRG1 protein, and the matched entry annotates G protein-coupled receptor activity. Its function annotation is supported by cited experimental evidence for G-protein signaling; the GO term itself is annotated by computational inference (IEA:InterPro).",
    "evidence_ids": ["C1", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a large extracellular N-terminal region followed by a cluster of seven strongly hydrophobic membrane-spanning segments and a cytoplasmic tail, a characteristic GPCR architecture. This meaningfully favors GPCR activity over the listed enzymatic alternatives.",
    "missing_item_specific_fact": "No protein-specific annotation is necessary to distinguish these choices at the broad functional level, though experimental evidence or family identification would confirm the receptor's precise activity.",
    "reason": "The supplied sequence itself provides a recognizable GPCR topology, while the distractors describe unrelated enzyme activities or ion binding."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The seven-transmembrane receptor architecture strongly distinguishes choice C from the other listed functions."
  },
  "important_caveats": [
    "The reviewer-only database evidence supports the key but was not supplied to the evaluated model.",
    "The GO annotation is computationally inferred; separate cited experimental evidence supports the protein's G-protein signaling function.",
    "Sequence architecture supports the broad receptor classification but does not by itself establish every detail of ligand or signaling specificity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `answerability_check:missing_item_specific_fact_must_be_text`.

### Expected-answer support: supported

> The sequence matches UniProt Q59I63 (Adhesion G protein-coupled receptor G1 / GPR56, Danio rerio). The UniProt entry explicitly annotates the protein as 'Adhesion G protein-coupled receptor G1' with GO:0004930 'G protein-coupled receptor activity' (evidence IEA:InterPro), and the protein's GPCR function is experimentally supported by ECO:0000269 (direct assay) evidence from PubMed:25607772 and PubMed:29367382, which demonstrate Gα12/13 coupling and RhoA activation. The expected answer C is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal ~250 residues of the sequence contain approximately seven hydrophobic stretches separated by short hydrophilic loops, consistent with the canonical 7-transmembrane helix bundle of GPCRs. The large N-terminal extracellular region (~400 residues) with conserved motifs (e.g., a GPS-like cleavage site 'CWMTEGDKS' and a GAIN-domain fold) is the hallmark architecture of class B/adhesion GPCRs. Additionally, a conserved NPxxY motif (NPYR near residue ~510) is present in the TM6-TM7 region. These structural features allow a knowledgeable model to identify the protein as a GPCR and exclude the other options: cardiolipin synthase (single-pass membrane phosphatidyltransferase), manganese ion binding (metal-coordinating protein, typically soluble or single-pass), and rRNA methyltransferase (soluble Rossmann-fold enzyme) are all incompatible with a multi-pass transmembrane receptor architecture.


**Missing item-specific fact**

`null` (as saved; not replaced with an inferred value)

**Reason**

> The 7TM topology and large extracellular N-terminal domain are identifiable from the sequence through general knowledge of membrane protein hydrophobicity patterns and GPCR structural biology. The distractors represent fundamentally different protein architectures (soluble enzymes, single-pass membrane proteins) that are inconsistent with the observed multi-pass transmembrane topology. This constitutes a concrete biological argument distinguishable from the sequence without memorizing the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent highly distinct molecular function categories (phosphatidyltransferase enzyme, metal-ion binding, 7TM receptor, nucleotide methyltransferase). The multi-pass transmembrane architecture with ~7 hydrophobic segments and a large extracellular N-terminal domain is uniquely consistent with GPCR activity among the choices. No other option is defensible for this sequence.


### Important caveats

- The GO:0004930 annotation in UniProt carries evidence code IEA:InterPro (computational), but the protein's GPCR function is independently supported by experimental evidence (ECO:0000269) from two primary publications.
- Identifying exactly 7 TM helices from a raw sequence is non-trivial; a model may estimate 6-8 hydrophobic segments. However, the overall multi-pass architecture is unambiguous and sufficient to exclude the single-pass or soluble distractors.
- The sequence is from zebrafish (Danio rerio), a non-model organism for some functional studies, but the GPCR annotation is well-established through orthology and direct experimentation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal ~250 residues of the sequence contain approximately seven hydrophobic stretches separated by short hydrophilic loops, consistent with the canonical 7-transmembrane helix bundle of GPCRs. The large N-terminal extracellular region (~400 residues) with conserved motifs (e.g., a GPS-like cleavage site 'CWMTEGDKS' and a GAIN-domain fold) is the hallmark architecture of class B/adhesion GPCRs. Additionally, a conserved NPxxY motif (NPYR near residue ~510) is present in the TM6-TM7 region. These structural features allow a knowledgeable model to identify the protein as a GPCR and exclude the other options: cardiolipin synthase (single-pass membrane phosphatidyltransferase), manganese ion binding (metal-coordinating protein, typically soluble or single-pass), and rRNA methyltransferase (soluble Rossmann-fold enzyme) are all incompatible with a multi-pass transmembrane receptor architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": null,
    "reason": "The 7TM topology and large extracellular N-terminal domain are identifiable from the sequence through general knowledge of membrane protein hydrophobicity patterns and GPCR structural biology. The distractors represent fundamentally different protein architectures (soluble enzymes, single-pass membrane proteins) that are inconsistent with the observed multi-pass transmembrane topology. This constitutes a concrete biological argument distinguishable from the sequence without memorizing the specific UniProt entry."
  },
  "case_id": "GO_molecular_function_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H4",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q59I63 (Adhesion G protein-coupled receptor G1 / GPR56, Danio rerio). The UniProt entry explicitly annotates the protein as 'Adhesion G protein-coupled receptor G1' with GO:0004930 'G protein-coupled receptor activity' (evidence IEA:InterPro), and the protein's GPCR function is experimentally supported by ECO:0000269 (direct assay) evidence from PubMed:25607772 and PubMed:29367382, which demonstrate Gα12/13 coupling and RhoA activation. The expected answer C is well-supported."
  },
  "important_caveats": [
    "The GO:0004930 annotation in UniProt carries evidence code IEA:InterPro (computational), but the protein's GPCR function is independently supported by experimental evidence (ECO:0000269) from two primary publications.",
    "Identifying exactly 7 TM helices from a raw sequence is non-trivial; a model may estimate 6-8 hydrophobic segments. However, the overall multi-pass architecture is unambiguous and sufficient to exclude the single-pass or soluble distractors.",
    "The sequence is from zebrafish (Danio rerio), a non-model organism for some functional studies, but the GPCR annotation is well-established through orthology and direct experimentation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct molecular function categories (phosphatidyltransferase enzyme, metal-ion binding, 7TM receptor, nucleotide methyltransferase). The multi-pass transmembrane architecture with ~7 hydrophobic segments and a large extracellular N-terminal domain is uniquely consistent with GPCR activity among the choices. No other option is defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q59I63 (Adhesion G protein-coupled receptor G1 / GPR56, Danio rerio). The UniProt entry explicitly annotates the protein as 'Adhesion G protein-coupled receptor G1' with GO:0004930 'G protein-coupled receptor activity' (evidence IEA:InterPro), and the protein's GPCR function is experimentally supported by ECO:0000269 (direct assay) evidence from PubMed:25607772 and PubMed:29367382, which demonstrate Gα12/13 coupling and RhoA activation. The expected answer C is well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H4", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal ~250 residues of the sequence contain approximately seven hydrophobic stretches separated by short hydrophilic loops, consistent with the canonical 7-transmembrane helix bundle of GPCRs. The large N-terminal extracellular region (~400 residues) with conserved motifs (e.g., a GPS-like cleavage site 'CWMTEGDKS' and a GAIN-domain fold) is the hallmark architecture of class B/adhesion GPCRs. Additionally, a conserved NPxxY motif (NPYR near residue ~510) is present in the TM6-TM7 region. These structural features allow a knowledgeable model to identify the protein as a GPCR and exclude the other options: cardiolipin synthase (single-pass membrane phosphatidyltransferase), manganese ion binding (metal-coordinating protein, typically soluble or single-pass), and rRNA methyltransferase (soluble Rossmann-fold enzyme) are all incompatible with a multi-pass transmembrane receptor architecture.",
    "missing_item_specific_fact": null,
    "reason": "The 7TM topology and large extracellular N-terminal domain are identifiable from the sequence through general knowledge of membrane protein hydrophobicity patterns and GPCR structural biology. The distractors represent fundamentally different protein architectures (soluble enzymes, single-pass membrane proteins) that are inconsistent with the observed multi-pass transmembrane topology. This constitutes a concrete biological argument distinguishable from the sequence without memorizing the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct molecular function categories (phosphatidyltransferase enzyme, metal-ion binding, 7TM receptor, nucleotide methyltransferase). The multi-pass transmembrane architecture with ~7 hydrophobic segments and a large extracellular N-terminal domain is uniquely consistent with GPCR activity among the choices. No other option is defensible for this sequence."
  },
  "important_caveats": [
    "The GO:0004930 annotation in UniProt carries evidence code IEA:InterPro (computational), but the protein's GPCR function is independently supported by experimental evidence (ECO:0000269) from two primary publications.",
    "Identifying exactly 7 TM helices from a raw sequence is non-trivial; a model may estimate 6-8 hydrophobic segments. However, the overall multi-pass architecture is unambiguous and sufficient to exclude the single-pass or soluble distractors.",
    "The sequence is from zebrafish (Danio rerio), a non-model organism for some functional studies, but the GPCR annotation is well-established through orthology and direct experimentation."
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

**Accession:** `Q59I63` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 119. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
"Q59I63"
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"25607772","source":"PubMed"}],"value":"G protein-coupled receptor 56"}}],"contains":[{"alternativeNames":[{"fullName":{"value":"ADGRG1 N-terminal fragment"},"shortNames":[{"value":"ADGRG1 NT"}]}],"recommendedName":{"fullName":{"value":"Adhesion G protein-coupled receptor G1, N-terminal fragment"}}},{"alternativeNames":[{"fullName":{"value":"ADGRG1 C-terminal fragment"},"shortNames":[{"value":"ADGRG1 CT"}]}],"recommendedName":{"fullName":{"value":"Adhesion G protein-coupled receptor G1, C-terminal fragment"}}}],"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Adhesion G protein-coupled receptor G1"}}}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"25607772","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"29367382","source":"PubMed"}],"value":"Adhesion G protein-coupled receptor (aGPCR), which is involved in oligodendrocyte development and maintenance of peripheral myelin (PubMed:25607772, PubMed:29367382). Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as RhoA pathway (PubMed:25607772). Adgrg1 is coupled to G(12) and/or G(13) G proteins (gna12 and gna13, respectively) and mediates the activation Rho small GTPases (PubMed:25607772, PubMed:29367382). Adgrg1-dependent RhoA signaling promotes timely radial sorting of axons (PubMed:29367382). Required to establish proper myelin thickness and facilitate organization of the myelin sheath in the mature peripheral nervous system (PubMed:29367382)"}]}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/uniProtKBCrossReferences/27`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"database":"GO","id":"GO:0004930","properties":[{"key":"GoTerm","value":"F:G protein-coupled receptor activity"},{"key":"GoEvidenceType","value":"IEA:InterPro"}]}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"citation":{"authors":["Ackerman S.D.","Garcia C.","Piao X.","Gutmann D.H.","Monk K.R."],"citationCrossReferences":[{"database":"PubMed","id":"25607772"},{"database":"DOI","id":"10.1038/ncomms7122"}],"citationType":"journal article","firstPage":"6122","id":"25607772","journal":"Nat. Commun.","lastPage":"6122","publicationDate":"2015","title":"The adhesion GPCR Gpr56 regulates oligodendrocyte development via interactions with Galpha12/13 and RhoA.","volume":"6"},"referenceNumber":3,"referencePositions":["FUNCTION","DEVELOPMENTAL STAGE","DISRUPTION PHENOTYPE","MUTAGENESIS OF 325-ASN-TRP-326"]}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"citation":{"authors":["Ackerman S.D.","Luo R.","Poitelon Y.","Mogha A.","Harty B.L.","D'Rozario M.","Sanchez N.E.","Lakkaraju A.K.K.","Gamble P.","Li J.","Qu J.","MacEwan M.R.","Ray W.Z.","Aguzzi A.","Feltri M.L.","Piao X.","Monk K.R."],"citationCrossReferences":[{"database":"PubMed","id":"29367382"},{"database":"DOI","id":"10.1084/jem.20161714"}],"citationType":"journal article","firstPage":"941","id":"29367382","journal":"J. Exp. Med.","lastPage":"961","publicationDate":"2018","title":"GPR56/ADGRG1 regulates development and maintenance of peripheral myelin.","volume":"215"},"referenceNumber":4,"referencePositions":["FUNCTION"]}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)  
**Locator:** `lines 93-105`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 2.  
**Retrieved:** 2026-11-02T04:31:04.584714+00:00.  

```text
CC   -!- FUNCTION: Adhesion G-protein coupled receptor (aGPCR), which is
CC       involved in oligodendrocyte development and maintenance of peripheral
CC       myelin (PubMed:25607772, PubMed:29367382). Ligand binding causes a
CC       conformation change that triggers signaling via guanine nucleotide-
CC       binding proteins (G proteins) and modulates the activity of downstream
CC       effectors, such as RhoA pathway (PubMed:25607772). Adgrg1 is coupled to
CC       G(12) and/or G(13) G proteins (gna12 and gna13, respectively) and
CC       mediates the activation Rho small GTPases (PubMed:25607772,
CC       PubMed:29367382). Adgrg1-dependent RhoA signaling promotes timely
CC       radial sorting of axons (PubMed:29367382). Required to establish proper
CC       myelin thickness and facilitate organization of the myelin sheath in
CC       the mature peripheral nervous system (PubMed:29367382).
CC       {ECO:0000269|PubMed:25607772, ECO:0000269|PubMed:29367382}.
```

Source SHA-256: `b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)  
**Locator:** `lines 169-169`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 2.  
**Retrieved:** 2026-11-02T04:31:04.584714+00:00.  

```text
DR   GO; GO:0004930; F:G protein-coupled receptor activity; IEA:InterPro.
```

Source SHA-256: `b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 52078-52112`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0004930
name: G protein-coupled receptor activity
namespace: molecular_function
alt_id: GO:0001622
alt_id: GO:0001623
alt_id: GO:0001624
alt_id: GO:0001625
alt_id: GO:0016526
def: "Combining with an extracellular signal and transmitting the signal across the membrane by activating an associated G-protein; promotes the exchange of GDP for GTP on the alpha subunit of a heterotrimeric G-protein complex." [GOC:bf, Wikipedia:GPCR]
subset: goslim_chembl
synonym: "EBV-induced receptor" NARROW []
synonym: "Epstein-Barr Virus-induced receptor activity" NARROW []
synonym: "G protein coupled receptor activity" EXACT []
synonym: "G protein linked receptor activity" EXACT []
synonym: "G-protein coupled receptor activity" EXACT []
synonym: "G-protein coupled receptor activity, unknown ligand" NARROW []
synonym: "G-protein linked receptor activity" EXACT []
synonym: "GPCR activity" EXACT []
synonym: "ligand-dependent GPCR activity" EXACT []
synonym: "Mas proto-oncogene receptor activity" NARROW []
synonym: "orphan G protein coupled receptor activity" NARROW []
synonym: "orphan G-protein coupled receptor activity" NARROW []
synonym: "orphan GPCR activity" NARROW []
synonym: "RDC1 receptor activity" NARROW []
synonym: "receptor activity, G-protein coupled" EXACT [GOC:bf]
synonym: "SREB receptor" NARROW []
synonym: "super conserved receptor expressed in brain receptor activity" NARROW []
xref: Reactome:R-HSA-114552 "Thrombin-activated PARs activate G12/13"
xref: Reactome:R-HSA-114558 "Thrombin-activated PARs activate Gq"
xref: Reactome:R-HSA-167408 "The high affinity receptor complex binds to G-protein"
xref: Reactome:R-HSA-381706 "GLP1R:GLP1 activates G(s)"
xref: Wikipedia:GPCR
is_a: GO:0004888 ! transmembrane signaling receptor activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 157. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
