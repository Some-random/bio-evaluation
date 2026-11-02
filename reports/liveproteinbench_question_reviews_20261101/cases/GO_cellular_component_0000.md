# GO_cellular_component_0000

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKQNPAKTARMWIIICLLFVLGQATDNDRDFKMCGKWLHGIAPQNLEYDLKTGCERIEISANESTLSIQGRITAKCTQSSSIQLDSNPHQNQSHFCVFWEPLLDLLIVEVNGKNHTLCKPNGLQGTCCTDLSQGVQDNAHMYGIVNGSVKGDIITGDLKGNYIFDGAHINCKEKFCDEARLKPRGANMIEEVVMRFNAKGRVDLPCAQGTVIEMDEEFTGHNFTVPAPRFVDANTIPSVYIPSSLRSVSRRKSKVVCTYYKNKTLFERGPSKSALLDDIVGLSVENETIRNLIEPVKIRFHHRPFAPDSSGRCVSWDTKQDNEVNWKDDGCDTVKINEEQTECHCNHLTYFAILVQVEQKSTVRHLKALTFITAVGCAVSLVSCLVLFYWLCKRRRGKKNQISLVHRGLVVAIFLLCLFFILTGILANVANETVCQLTGSLLHYGLLSTLCWMAMEVFHTFLLVRKVFNSPLPIWIFYLMGFGFPFLLVSILLSVGDIYGERKIKPSDDVNNPYRMCWMTEGDKSQLAHYIINIGLLAVVVSSGLVMLFLVVREIRNRPDWKKIHVAFLSIWGLTCLYGTTWALGFLDFGPFSEVTLFLFCIINSLQGFFLMLRYYALERMKKKDVSSSDGSSSGSSKQHMLQTNEKS

[Multiple Choices]
A. Dbf4-dependent protein kinase complex
B. neuronal cell body
C. plasma membrane
D. acrosomal membrane
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

> The exact-matching UniProt entry annotates the protein to the cell membrane and records plasma membrane as a GO cellular-component annotation. The localization is supported by database annotation, though the evidence is transferred or computational rather than a direct experimental localization shown here.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The signal peptide and multiple hydrophobic transmembrane segments support a membrane protein, consistent with an adhesion GPCR. They do not by themselves establish plasma membrane rather than another membrane compartment.


**Missing item-specific fact**

> The protein-specific localization annotation or experimental evidence establishing its cellular location is not supplied in the question.


**Reason**

> Sequence reasoning meaningfully favors a membrane-associated choice over the kinase complex and neuronal cell body, but resolving plasma membrane versus the specialized acrosomal membrane requires protein-specific localization information not given in the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports membrane localization broadly, but the supplied choices do not provide evidence that this protein is associated with sperm or the acrosome; reviewer-only annotations support plasma membrane.


### Important caveats

- The matching historical UniProt record annotates cell membrane and plasma membrane, but the cell-membrane localization is transferred from another UniProt entry and the GO annotation is IEA.
- The precise historical source snapshot used by the question author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The signal peptide and multiple hydrophobic transmembrane segments support a membrane protein, consistent with an adhesion GPCR. They do not by themselves establish plasma membrane rather than another membrane compartment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization annotation or experimental evidence establishing its cellular location is not supplied in the question.",
    "reason": "Sequence reasoning meaningfully favors a membrane-associated choice over the kinase complex and neuronal cell body, but resolving plasma membrane versus the specialized acrosomal membrane requires protein-specific localization information not given in the input."
  },
  "case_id": "GO_cellular_component_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact-matching UniProt entry annotates the protein to the cell membrane and records plasma membrane as a GO cellular-component annotation. The localization is supported by database annotation, though the evidence is transferred or computational rather than a direct experimental localization shown here."
  },
  "important_caveats": [
    "The matching historical UniProt record annotates cell membrane and plasma membrane, but the cell-membrane localization is transferred from another UniProt entry and the GO annotation is IEA.",
    "The precise historical source snapshot used by the question author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports membrane localization broadly, but the supplied choices do not provide evidence that this protein is associated with sperm or the acrosome; reviewer-only annotations support plasma membrane."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matching UniProt entry annotates the protein to the cell membrane and records plasma membrane as a GO cellular-component annotation. The localization is supported by database annotation, though the evidence is transferred or computational rather than a direct experimental localization shown here.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The signal peptide and multiple hydrophobic transmembrane segments support a membrane protein, consistent with an adhesion GPCR. They do not by themselves establish plasma membrane rather than another membrane compartment.",
    "missing_item_specific_fact": "The protein-specific localization annotation or experimental evidence establishing its cellular location is not supplied in the question.",
    "reason": "Sequence reasoning meaningfully favors a membrane-associated choice over the kinase complex and neuronal cell body, but resolving plasma membrane versus the specialized acrosomal membrane requires protein-specific localization information not given in the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports membrane localization broadly, but the supplied choices do not provide evidence that this protein is associated with sperm or the acrosome; reviewer-only annotations support plasma membrane."
  },
  "important_caveats": [
    "The matching historical UniProt record annotates cell membrane and plasma membrane, but the cell-membrane localization is transferred from another UniProt entry and the GO annotation is IEA.",
    "The precise historical source snapshot used by the question author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q59I63, ADGRG1/GPR56 from Danio rerio) annotates the protein as a 'Cell membrane; Multi-pass membrane protein' (C5/H4) with GO:0005886 (plasma membrane) (C6/H5). The protein is identified as an Adhesion G protein-coupled receptor, a family universally localized to the plasma membrane. The evidence codes are ECO:0000250 (similarity to human ortholog Q9Y653) and ECO:0000255 (rule-based topology prediction), which are computational/similarity-based rather than direct experimental evidence for the zebrafish protein. However, GPCR localization to the plasma membrane is a universal biological principle, and the 7TM architecture visible in the sequence independently confirms this. The expected answer C (plasma membrane) is scientifically well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains seven distinct hydrophobic stretches of ~20-25 residues arranged in the canonical 7-transmembrane (7TM) GPCR architecture, preceded by a large extracellular N-terminal domain. The 7TM topology is a well-known structural signature: any protein with seven membrane-spanning helices in this arrangement is a GPCR, and all GPCRs reside at the plasma membrane. This reasoning chain (count hydrophobic segments → identify 7TM topology → GPCR → plasma membrane) is general biological knowledge. The distractors are eliminable by general reasoning: a Dbf4-dependent kinase complex (A) is nuclear with no TM domains; 'neuronal cell body' (B) denotes a subcellular region (soma), not a membrane compartment; acrosomal membrane (D) is a sperm-specific organelle incompatible with a broadly expressed receptor.


**Missing item-specific fact**

> None required. The 7TM architecture is directly observable in the sequence and the GPCR→plasma membrane mapping is general biology, not an item-specific annotation lookup.


**Reason**

> A model with knowledge of membrane protein topology can identify the seven hydrophobic segments in the sequence, recognize the 7TM GPCR fold, and conclude plasma membrane localization without needing to know the specific protein identity or its database annotation. The distractors are eliminated by general cell biology (kinase complexes are nuclear; acrosomal membranes are sperm-specific; 'neuronal cell body' is a soma region, not a membrane).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The 7TM architecture unambiguously identifies a GPCR, whose primary cellular component is the plasma membrane. Option B (neuronal cell body) might seem tangentially relevant because ADGRG1 is expressed in neural cells, but as a GO Cellular Component term it denotes the soma region rather than the membrane, and the 7TM topology places the protein at the membrane itself. Options A and D are structurally incompatible with a multi-pass membrane protein. No alternative answer is defensible.


### Important caveats

- The UniProt subcellular location annotation uses ECO:0000250 (inferred by similarity to human Q9Y653) and ECO:0000255 (rule-based topology), not direct experimental evidence for the zebrafish protein. However, the universal GPCR-plasma membrane association and the visible 7TM sequence architecture provide independent confirmation.
- The GO annotation evidence is ISS/IEA (inferred from sequence similarity or electronic annotation), not direct experimental localization.
- The protein is a precursor with autoproteolytic cleavage (GPS motif), yielding N- and C-terminal fragments; both remain membrane-associated, so this does not alter the plasma membrane assignment.
- The reviewer-only accession (Q59I63) was inferred from dataset metadata and was not provided to the evaluated model; the model must reason from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains seven distinct hydrophobic stretches of ~20-25 residues arranged in the canonical 7-transmembrane (7TM) GPCR architecture, preceded by a large extracellular N-terminal domain. The 7TM topology is a well-known structural signature: any protein with seven membrane-spanning helices in this arrangement is a GPCR, and all GPCRs reside at the plasma membrane. This reasoning chain (count hydrophobic segments → identify 7TM topology → GPCR → plasma membrane) is general biological knowledge. The distractors are eliminable by general reasoning: a Dbf4-dependent kinase complex (A) is nuclear with no TM domains; 'neuronal cell body' (B) denotes a subcellular region (soma), not a membrane compartment; acrosomal membrane (D) is a sperm-specific organelle incompatible with a broadly expressed receptor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. The 7TM architecture is directly observable in the sequence and the GPCR→plasma membrane mapping is general biology, not an item-specific annotation lookup.",
    "reason": "A model with knowledge of membrane protein topology can identify the seven hydrophobic segments in the sequence, recognize the 7TM GPCR fold, and conclude plasma membrane localization without needing to know the specific protein identity or its database annotation. The distractors are eliminated by general cell biology (kinase complexes are nuclear; acrosomal membranes are sperm-specific; 'neuronal cell body' is a soma region, not a membrane)."
  },
  "case_id": "GO_cellular_component_0000",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q59I63, ADGRG1/GPR56 from Danio rerio) annotates the protein as a 'Cell membrane; Multi-pass membrane protein' (C5/H4) with GO:0005886 (plasma membrane) (C6/H5). The protein is identified as an Adhesion G protein-coupled receptor, a family universally localized to the plasma membrane. The evidence codes are ECO:0000250 (similarity to human ortholog Q9Y653) and ECO:0000255 (rule-based topology prediction), which are computational/similarity-based rather than direct experimental evidence for the zebrafish protein. However, GPCR localization to the plasma membrane is a universal biological principle, and the 7TM architecture visible in the sequence independently confirms this. The expected answer C (plasma membrane) is scientifically well-supported."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation uses ECO:0000250 (inferred by similarity to human Q9Y653) and ECO:0000255 (rule-based topology), not direct experimental evidence for the zebrafish protein. However, the universal GPCR-plasma membrane association and the visible 7TM sequence architecture provide independent confirmation.",
    "The GO annotation evidence is ISS/IEA (inferred from sequence similarity or electronic annotation), not direct experimental localization.",
    "The protein is a precursor with autoproteolytic cleavage (GPS motif), yielding N- and C-terminal fragments; both remain membrane-associated, so this does not alter the plasma membrane assignment.",
    "The reviewer-only accession (Q59I63) was inferred from dataset metadata and was not provided to the evaluated model; the model must reason from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The 7TM architecture unambiguously identifies a GPCR, whose primary cellular component is the plasma membrane. Option B (neuronal cell body) might seem tangentially relevant because ADGRG1 is expressed in neural cells, but as a GO Cellular Component term it denotes the soma region rather than the membrane, and the 7TM topology places the protein at the membrane itself. Options A and D are structurally incompatible with a multi-pass membrane protein. No alternative answer is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0000",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q59I63, ADGRG1/GPR56 from Danio rerio) annotates the protein as a 'Cell membrane; Multi-pass membrane protein' (C5/H4) with GO:0005886 (plasma membrane) (C6/H5). The protein is identified as an Adhesion G protein-coupled receptor, a family universally localized to the plasma membrane. The evidence codes are ECO:0000250 (similarity to human ortholog Q9Y653) and ECO:0000255 (rule-based topology prediction), which are computational/similarity-based rather than direct experimental evidence for the zebrafish protein. However, GPCR localization to the plasma membrane is a universal biological principle, and the 7TM architecture visible in the sequence independently confirms this. The expected answer C (plasma membrane) is scientifically well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains seven distinct hydrophobic stretches of ~20-25 residues arranged in the canonical 7-transmembrane (7TM) GPCR architecture, preceded by a large extracellular N-terminal domain. The 7TM topology is a well-known structural signature: any protein with seven membrane-spanning helices in this arrangement is a GPCR, and all GPCRs reside at the plasma membrane. This reasoning chain (count hydrophobic segments → identify 7TM topology → GPCR → plasma membrane) is general biological knowledge. The distractors are eliminable by general reasoning: a Dbf4-dependent kinase complex (A) is nuclear with no TM domains; 'neuronal cell body' (B) denotes a subcellular region (soma), not a membrane compartment; acrosomal membrane (D) is a sperm-specific organelle incompatible with a broadly expressed receptor.",
    "missing_item_specific_fact": "None required. The 7TM architecture is directly observable in the sequence and the GPCR→plasma membrane mapping is general biology, not an item-specific annotation lookup.",
    "reason": "A model with knowledge of membrane protein topology can identify the seven hydrophobic segments in the sequence, recognize the 7TM GPCR fold, and conclude plasma membrane localization without needing to know the specific protein identity or its database annotation. The distractors are eliminated by general cell biology (kinase complexes are nuclear; acrosomal membranes are sperm-specific; 'neuronal cell body' is a soma region, not a membrane)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The 7TM architecture unambiguously identifies a GPCR, whose primary cellular component is the plasma membrane. Option B (neuronal cell body) might seem tangentially relevant because ADGRG1 is expressed in neural cells, but as a GO Cellular Component term it denotes the soma region rather than the membrane, and the 7TM topology places the protein at the membrane itself. Options A and D are structurally incompatible with a multi-pass membrane protein. No alternative answer is defensible."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation uses ECO:0000250 (inferred by similarity to human Q9Y653) and ECO:0000255 (rule-based topology), not direct experimental evidence for the zebrafish protein. However, the universal GPCR-plasma membrane association and the visible 7TM sequence architecture provide independent confirmation.",
    "The GO annotation evidence is ISS/IEA (inferred from sequence similarity or electronic annotation), not direct experimental localization.",
    "The protein is a precursor with autoproteolytic cleavage (GPS motif), yielding N- and C-terminal fragments; both remain membrane-associated, so this does not alter the plasma membrane assignment.",
    "The reviewer-only accession (Q59I63) was inferred from dataset metadata and was not provided to the evaluated model; the model must reason from sequence alone."
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
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9Y653","source":"UniProtKB"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q59I63.json)  
**Locator:** `/uniProtKBCrossReferences/26`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:01.992326+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `a16a326ac63664dbc4e3b324e2c1c9ff44948e77fb05c1001e3446f3a60d30fe`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)  
**Locator:** `lines 121-122`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 2.  
**Retrieved:** 2026-11-02T04:31:04.584714+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:Q9Y653};
CC       Multi-pass membrane protein {ECO:0000255}.
```

Source SHA-256: `b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q59I63?format=txt&versions=119)  
**Locator:** `lines 168-168`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 119 / 2.  
**Retrieved:** 2026-11-02T04:31:04.584714+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `b3b3944ca7d7dd4847591f08fda1ac31f6e70235cc8a188b119e1d57001755c0`.

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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 0. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
