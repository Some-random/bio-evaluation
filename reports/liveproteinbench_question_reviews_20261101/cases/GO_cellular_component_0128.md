# GO_cellular_component_0128

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSHTSTPNHASAAPPRKWYDMTSAEFYVYVVAFMCGISMLMPINAVFSAPSYMLQYYLYATKDPNHVPQMTNFWSNVMTYYNLIGLVTGLVMEPLTLLKSFRKIPMLVRLLGGLCILIVEIIVLMAVPARGTTEGGAVATMCIAGFIGGLGKSIFESTVYGMFGAFPPSFTSIMMGGVGISGVLTSLIQIIVKAALPDTYEGVKKQSYIYYSLDVGIQAATFIALIMMRFNSFAQLHFGDLGGVKSKVDAGSLAGAGENVREPGAEATELEQYTEPAIGQIQEKNAEAHKDDPLVDREHSDDVDEHGDALRAVEGPTSNEILRATSIISVLRSIKWMFVSCAFVFVVTLFLFPGIATGMFPESKWFATVAVFIFNCCDVLGRVAPALRFMWPRSYNQRWIIVAASFARVIFVPLLLLYSYHYIPSEAYGYVIMVIFGFSSGYVASMSLTLGPQSKGIDNDGKRFVAGTLMGISILVGGTIGTVLSIMTQTIREKY

[Multiple Choices]
A. plasma membrane
B. egg coat
C. endocytic vesicle
D. nucleoplasm
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

> The exact sequence matches a Crithidia fasciculata adenosine transporter entry annotated to the plasma membrane. The GO annotation is IEA:TreeGrafter, and the separate multipass-membrane annotation is computational; these support the key but do not constitute direct experimental localization evidence.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The many hydrophobic segments support a multipass membrane protein and make nucleoplasm and egg coat poor fits. They do not, by themselves, establish whether its primary location is the plasma membrane or an endocytic vesicle.


**Missing item-specific fact**

> The protein-specific localization of this transporter, supplied here by an external GO annotation rather than by the sequence alone.


**Reason**

> Choosing A over C depends on item-specific localization information. Recognizing the sequence or invoking a predictor does not provide a biological argument from the supplied input that distinguishes those compartments.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> The sequence supports membrane association but does not resolve plasma membrane versus endocytic-vesicle localization. The external annotation supports A, but that information was not supplied in the question.


### Important caveats

- The matched record identifies the protein as an adenosine transporter, but its cited functional work does not, in the provided excerpts, independently establish cellular localization.
- The annotation and historical record are reviewer-only evidence; the author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The many hydrophobic segments support a multipass membrane protein and make nucleoplasm and egg coat poor fits. They do not, by themselves, establish whether its primary location is the plasma membrane or an endocytic vesicle.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization of this transporter, supplied here by an external GO annotation rather than by the sequence alone.",
    "reason": "Choosing A over C depends on item-specific localization information. Recognizing the sequence or invoking a predictor does not provide a biological argument from the supplied input that distinguishes those compartments."
  },
  "case_id": "GO_cellular_component_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a Crithidia fasciculata adenosine transporter entry annotated to the plasma membrane. The GO annotation is IEA:TreeGrafter, and the separate multipass-membrane annotation is computational; these support the key but do not constitute direct experimental localization evidence."
  },
  "important_caveats": [
    "The matched record identifies the protein as an adenosine transporter, but its cited functional work does not, in the provided excerpts, independently establish cellular localization.",
    "The annotation and historical record are reviewer-only evidence; the author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "The sequence supports membrane association but does not resolve plasma membrane versus endocytic-vesicle localization. The external annotation supports A, but that information was not supplied in the question."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a Crithidia fasciculata adenosine transporter entry annotated to the plasma membrane. The GO annotation is IEA:TreeGrafter, and the separate multipass-membrane annotation is computational; these support the key but do not constitute direct experimental localization evidence.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The many hydrophobic segments support a multipass membrane protein and make nucleoplasm and egg coat poor fits. They do not, by themselves, establish whether its primary location is the plasma membrane or an endocytic vesicle.",
    "missing_item_specific_fact": "The protein-specific localization of this transporter, supplied here by an external GO annotation rather than by the sequence alone.",
    "reason": "Choosing A over C depends on item-specific localization information. Recognizing the sequence or invoking a predictor does not provide a biological argument from the supplied input that distinguishes those compartments."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "The sequence supports membrane association but does not resolve plasma membrane versus endocytic-vesicle localization. The external annotation supports A, but that information was not supplied in the question."
  },
  "important_caveats": [
    "The matched record identifies the protein as an adenosine transporter, but its cited functional work does not, in the provided excerpts, independently establish cellular localization.",
    "The annotation and historical record are reviewer-only evidence; the author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry J9UD11 (Crithidia fasciculata adenosine transporter 1, CfAT1) annotates the protein as 'Membrane; Multi-pass membrane protein' (ECO:0000255, inferred by similarity) and carries GO:0005886 C:plasma membrane with evidence code IEA:TreeGrafter. The protein is characterized in PubMed 24120444 as a high-affinity equilibrative nucleoside transporter, a class canonically located at the plasma membrane for adenosine uptake from the extracellular environment. The GO annotation is computational (IEA) rather than experimentally verified for this specific protein, but it is consistent with the protein's function and topology. The expected answer 'plasma membrane' is supported by the annotation and by biological reasoning about ENT-family transporters.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains approximately 11-12 long hydrophobic stretches spanning the entire length, characteristic of a multi-pass integral membrane protein. This immediately eliminates 'egg coat' (B: an extracellular matrix protein, not a membrane protein) and 'nucleoplasm' (D: a soluble nuclear compartment incompatible with a multi-pass membrane topology; no NLS present). Distinguishing 'plasma membrane' (A) from 'endocytic vesicle' (C): multi-pass transporters with this many TM helices (~11-12) that mediate small-molecule uptake are canonically resident at the plasma membrane. Endocytic vesicle membrane proteins (e.g., SNAREs, V-ATPase subunits, sorting receptors) typically have different topologies (fewer TM segments, single-pass, or distinct domain architectures). The topology and hydrophobicity pattern are consistent with a major-facilitator-superfamily-like or equilibrative-nucleoside-transporter-like fold, which functions at the cell surface to import extracellular ligands.


**Missing item-specific fact**

> None strictly required. Recognizing the specific ENT family from sequence alone is challenging, but the general principle that multi-pass small-molecule transporters reside at the plasma membrane is standard cell biology knowledge sufficient to prefer A over C.


**Reason**

> The sequence's multi-pass membrane topology eliminates B and D through straightforward reasoning. The distinction between A and C rests on the general biological principle that multi-pass transporters for small extracellular molecules (nucleosides, sugars, amino acids) are plasma membrane proteins, whereas endocytic vesicle proteins have different architectural signatures. This is defensible general biological reasoning rather than a protein-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B (egg coat) and D (nucleoplasm) are clearly incompatible with a multi-pass membrane protein sequence. C (endocytic vesicle) is the only plausible competitor to A, but the ~11-12 TM helix topology and transporter-like architecture favor plasma membrane over endocytic vesicle. No other option is defensible.


### Important caveats

- The GO 'plasma membrane' annotation carries evidence code IEA:TreeGrafter (inferred electronic annotation by similarity), not direct experimental localization data for this specific protein.
- The UniProt subcellular location comment states 'Membrane; Multi-pass membrane protein' (ECO:0000255, inferred by similarity) without specifying which membrane.
- The protein is from Crithidia fasciculata (a trypanosomatid); plasma membrane localization of ENTs is well-established in metazoans but the specific subcellular distribution in trypanosomatids may have nuances not captured by TreeGrafter inference.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt J9UD11, entry version 26.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains approximately 11-12 long hydrophobic stretches spanning the entire length, characteristic of a multi-pass integral membrane protein. This immediately eliminates 'egg coat' (B: an extracellular matrix protein, not a membrane protein) and 'nucleoplasm' (D: a soluble nuclear compartment incompatible with a multi-pass membrane topology; no NLS present). Distinguishing 'plasma membrane' (A) from 'endocytic vesicle' (C): multi-pass transporters with this many TM helices (~11-12) that mediate small-molecule uptake are canonically resident at the plasma membrane. Endocytic vesicle membrane proteins (e.g., SNAREs, V-ATPase subunits, sorting receptors) typically have different topologies (fewer TM segments, single-pass, or distinct domain architectures). The topology and hydrophobicity pattern are consistent with a major-facilitator-superfamily-like or equilibrative-nucleoside-transporter-like fold, which functions at the cell surface to import extracellular ligands.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. Recognizing the specific ENT family from sequence alone is challenging, but the general principle that multi-pass small-molecule transporters reside at the plasma membrane is standard cell biology knowledge sufficient to prefer A over C.",
    "reason": "The sequence's multi-pass membrane topology eliminates B and D through straightforward reasoning. The distinction between A and C rests on the general biological principle that multi-pass transporters for small extracellular molecules (nucleosides, sugars, amino acids) are plasma membrane proteins, whereas endocytic vesicle proteins have different architectural signatures. This is defensible general biological reasoning rather than a protein-specific lookup."
  },
  "case_id": "GO_cellular_component_0128",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry J9UD11 (Crithidia fasciculata adenosine transporter 1, CfAT1) annotates the protein as 'Membrane; Multi-pass membrane protein' (ECO:0000255, inferred by similarity) and carries GO:0005886 C:plasma membrane with evidence code IEA:TreeGrafter. The protein is characterized in PubMed 24120444 as a high-affinity equilibrative nucleoside transporter, a class canonically located at the plasma membrane for adenosine uptake from the extracellular environment. The GO annotation is computational (IEA) rather than experimentally verified for this specific protein, but it is consistent with the protein's function and topology. The expected answer 'plasma membrane' is supported by the annotation and by biological reasoning about ENT-family transporters."
  },
  "important_caveats": [
    "The GO 'plasma membrane' annotation carries evidence code IEA:TreeGrafter (inferred electronic annotation by similarity), not direct experimental localization data for this specific protein.",
    "The UniProt subcellular location comment states 'Membrane; Multi-pass membrane protein' (ECO:0000255, inferred by similarity) without specifying which membrane.",
    "The protein is from Crithidia fasciculata (a trypanosomatid); plasma membrane localization of ENTs is well-established in metazoans but the specific subcellular distribution in trypanosomatids may have nuances not captured by TreeGrafter inference.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt J9UD11, entry version 26."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B (egg coat) and D (nucleoplasm) are clearly incompatible with a multi-pass membrane protein sequence. C (endocytic vesicle) is the only plausible competitor to A, but the ~11-12 TM helix topology and transporter-like architecture favor plasma membrane over endocytic vesicle. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0128",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry J9UD11 (Crithidia fasciculata adenosine transporter 1, CfAT1) annotates the protein as 'Membrane; Multi-pass membrane protein' (ECO:0000255, inferred by similarity) and carries GO:0005886 C:plasma membrane with evidence code IEA:TreeGrafter. The protein is characterized in PubMed 24120444 as a high-affinity equilibrative nucleoside transporter, a class canonically located at the plasma membrane for adenosine uptake from the extracellular environment. The GO annotation is computational (IEA) rather than experimentally verified for this specific protein, but it is consistent with the protein's function and topology. The expected answer 'plasma membrane' is supported by the annotation and by biological reasoning about ENT-family transporters.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains approximately 11-12 long hydrophobic stretches spanning the entire length, characteristic of a multi-pass integral membrane protein. This immediately eliminates 'egg coat' (B: an extracellular matrix protein, not a membrane protein) and 'nucleoplasm' (D: a soluble nuclear compartment incompatible with a multi-pass membrane topology; no NLS present). Distinguishing 'plasma membrane' (A) from 'endocytic vesicle' (C): multi-pass transporters with this many TM helices (~11-12) that mediate small-molecule uptake are canonically resident at the plasma membrane. Endocytic vesicle membrane proteins (e.g., SNAREs, V-ATPase subunits, sorting receptors) typically have different topologies (fewer TM segments, single-pass, or distinct domain architectures). The topology and hydrophobicity pattern are consistent with a major-facilitator-superfamily-like or equilibrative-nucleoside-transporter-like fold, which functions at the cell surface to import extracellular ligands.",
    "missing_item_specific_fact": "None strictly required. Recognizing the specific ENT family from sequence alone is challenging, but the general principle that multi-pass small-molecule transporters reside at the plasma membrane is standard cell biology knowledge sufficient to prefer A over C.",
    "reason": "The sequence's multi-pass membrane topology eliminates B and D through straightforward reasoning. The distinction between A and C rests on the general biological principle that multi-pass transporters for small extracellular molecules (nucleosides, sugars, amino acids) are plasma membrane proteins, whereas endocytic vesicle proteins have different architectural signatures. This is defensible general biological reasoning rather than a protein-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B (egg coat) and D (nucleoplasm) are clearly incompatible with a multi-pass membrane protein sequence. C (endocytic vesicle) is the only plausible competitor to A, but the ~11-12 TM helix topology and transporter-like architecture favor plasma membrane over endocytic vesicle. No other option is defensible."
  },
  "important_caveats": [
    "The GO 'plasma membrane' annotation carries evidence code IEA:TreeGrafter (inferred electronic annotation by similarity), not direct experimental localization data for this specific protein.",
    "The UniProt subcellular location comment states 'Membrane; Multi-pass membrane protein' (ECO:0000255, inferred by similarity) without specifying which membrane.",
    "The protein is from Crithidia fasciculata (a trypanosomatid); plasma membrane localization of ENTs is well-established in metazoans but the specific subcellular distribution in trypanosomatids may have nuances not captured by TreeGrafter inference.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt J9UD11, entry version 26."
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

**Accession:** `J9UD11` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 26. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
"J9UD11"
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-0162","value":"Membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/uniProtKBCrossReferences/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9UD11.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:53.178363+00:00.  

```json
{"citation":{"authors":["Arendt C.S."],"citationCrossReferences":[{"database":"PubMed","id":"24120444"},{"database":"DOI","id":"10.1016/j.molbiopara.2013.09.007"}],"citationType":"journal article","firstPage":"75","id":"24120444","journal":"Mol. Biochem. Parasitol.","lastPage":"79","publicationDate":"2013","title":"Crithidia fasciculata adenosine transporter 1 (CfAT1), a novel high-affinity equilibrative nucleoside transporter specific for adenosine.","volume":"191"},"evidences":[{"evidenceCode":"ECO:0000312","id":"AFR68832.1","source":"EMBL"},{"evidenceCode":"ECO:0000312","id":"AFR68833.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","TRANSPORTER ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","MUTAGENESIS OF LYS-153","VARIANTS MET-433 AND VAL-481"]}
```

Source SHA-256: `b8a834408fc72a31b2ce6a3190a6f2a1e7030d828c3ec7442331408414d4777c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)  
**Locator:** `lines 30-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:28:56.181587+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Membrane {ECO:0000255}; Multi-pass membrane
CC       protein {ECO:0000255}.
```

Source SHA-256: `52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9UD11?format=txt&versions=26)  
**Locator:** `lines 44-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 26 / 1.  
**Retrieved:** 2026-11-02T04:28:56.181587+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.
```

Source SHA-256: `52f5c9978ed3814d8396e7feee320cd18c812e512a57459050eeb591ed24b7a6`.

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 128. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
