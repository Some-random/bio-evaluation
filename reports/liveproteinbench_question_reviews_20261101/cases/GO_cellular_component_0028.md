# GO_cellular_component_0028

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGQFRFLALIVAVLCFSVALFLPTADEPDQDSYSVPLNQSVNTSQPPSSEMVPSDIRLTPLPQPKRIHYMVKVGDTLSGIFAQLGVPYSILQKILSVDLDHLQLDMIQPGEELELMMDDMGQLSRLIYHMSIVEKAIYTRENDGSFSYDFQEISGEWREILFSGEINGSFSVSARRVGLTSSQVANITQVMKDKIDFSRSLRAGDRFDILVKQQYLGEHNTGNSEIKAISFKLAKGDVSAFLAEDGRFYDRAGNSLERAFNRYPVDKAYRQITSGFNPKRKHPVTGRVVPHNGTDFATPIGAPVYSTGDGKVIVVRKHPYAGNYLVIEHNSVYKTRYLHLDKILVKKGQLVKRGQKIALAGATGRLTGPHLHFEVLVRNRPVDAMKADLPIAKSLSSNQKTSFLARVSEFDHLVQANQQEVALDET

[Multiple Choices]
A. host cell nucleolus
B. vesicle
C. nematocyst
D. plasma membrane
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

### Expected-answer support: contradicted

> The sequence-matched UniProt record annotates ShyB as periplasmic, not as a plasma-membrane protein. The localization annotation is associated with a cited study, while the GO annotation is computationally assigned; neither supports choice D.

Citations as saved: [H5](#evidence-h5), [H6](#evidence-h6), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic stretch is consistent with a bacterial export signal, and the rest of the sequence lacks an obvious additional membrane-spanning region, favoring a soluble exported protein over a membrane-embedded one. This does not establish its precise destination.


**Missing item-specific fact**

> The protein-specific localization to the periplasm, which is not among the answer choices.


**Reason**

> Sequence features suggest export but do not distinguish periplasm from other possible destinations with enough specificity to select a listed answer. The matching protein annotation supplies the relevant localization, and it conflicts with the keyed choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence points to the periplasm, which is not offered. It does not make plasma membrane equivalent to periplasm; therefore no listed option is clearly defensible as the primary location.


### Important caveats

- The reviewer-only record matches the supplied sequence and includes a historical record available by the stated cutoff.
- The periplasmic UniProt annotation is attributed to a publication but uses curator-inference evidence; the GO periplasm annotation is computationally assigned. These are annotations, not independently validated direct experimental measurements here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a bacterial export signal, and the rest of the sequence lacks an obvious additional membrane-spanning region, favoring a soluble exported protein over a membrane-embedded one. This does not establish its precise destination.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization to the periplasm, which is not among the answer choices.",
    "reason": "Sequence features suggest export but do not distinguish periplasm from other possible destinations with enough specificity to select a listed answer. The matching protein annotation supplies the relevant localization, and it conflicts with the keyed choice."
  },
  "case_id": "GO_cellular_component_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "H5",
      "H6",
      "C5",
      "C6"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched UniProt record annotates ShyB as periplasmic, not as a plasma-membrane protein. The localization annotation is associated with a cited study, while the GO annotation is computationally assigned; neither supports choice D."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence and includes a historical record available by the stated cutoff.",
    "The periplasmic UniProt annotation is attributed to a publication but uses curator-inference evidence; the GO periplasm annotation is computationally assigned. These are annotations, not independently validated direct experimental measurements here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence points to the periplasm, which is not offered. It does not make plasma membrane equivalent to periplasm; therefore no listed option is clearly defensible as the primary location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0028",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched UniProt record annotates ShyB as periplasmic, not as a plasma-membrane protein. The localization annotation is associated with a cited study, while the GO annotation is computationally assigned; neither supports choice D.",
    "evidence_ids": ["H5", "H6", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a bacterial export signal, and the rest of the sequence lacks an obvious additional membrane-spanning region, favoring a soluble exported protein over a membrane-embedded one. This does not establish its precise destination.",
    "missing_item_specific_fact": "The protein-specific localization to the periplasm, which is not among the answer choices.",
    "reason": "Sequence features suggest export but do not distinguish periplasm from other possible destinations with enough specificity to select a listed answer. The matching protein annotation supplies the relevant localization, and it conflicts with the keyed choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence points to the periplasm, which is not offered. It does not make plasma membrane equivalent to periplasm; therefore no listed option is clearly defensible as the primary location."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence and includes a historical record available by the stated cutoff.",
    "The periplasmic UniProt annotation is attributed to a publication but uses curator-inference evidence; the GO periplasm annotation is computationally assigned. These are annotations, not independently validated direct experimental measurements here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The UniProt entry Q9KUL5 (Peptidoglycan DD-endopeptidase ShyB, Vibrio cholerae) explicitly annotates the subcellular location as 'Periplasm' (GO:0042597, periplasmic space) with experimental evidence (ECO:0000305, PubMed:23834664). The GO cross-reference confirms 'C:periplasmic space.' The plasma membrane (GO:0005886, synonym 'bacterial inner membrane') is a distinct structure from the periplasmic space in Gram-negative bacteria. The protein has an N-terminal Sec signal peptide (MGQFRFLALIVAVLCFSVALFLPTA) for export but no transmembrane anchor, so its mature functional location is the periplasm, not the membrane itself. The expected answer 'plasma membrane' contradicts the experimentally supported annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H5](#evidence-h5), [H6](#evidence-h6), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is clearly bacterial (hydrophobic N-terminal signal peptide, peptidoglycan endopeptidase domain). Options A (host cell nucleolus) and C (nematocyst) are eukaryotic/cnidarian-specific structures incompatible with a bacterial protein. Option B (vesicle) is inconsistent with a soluble peptidoglycan-hydrolyzing enzyme lacking vesicle-targeting motifs. By elimination, D (plasma membrane) is the only remaining option. A model can reach D through general biological reasoning about organism type and protein function, even though the true location (periplasm) is not listed.


**Missing item-specific fact**

> The correct biological answer (periplasm) is absent from the options, so the model cannot positively identify the true location. It arrives at D only by elimination of clearly impossible choices, not by recognizing the actual compartment.


**Reason**

> General biological knowledge (bacterial organism, peptidoglycan enzyme function, absence of eukaryotic/cnidarian/vesicular features) allows elimination of A, B, and C, leaving D. This constitutes a valid reasoning path, though the underlying key is factually incorrect.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the true answer (periplasm) is missing, the remaining options A, B, and C are so clearly incompatible with a bacterial peptidoglycan endopeptidase that only D survives elimination. No alternative among the listed options is defensible as the correct answer.


### Important caveats

- The expected answer 'plasma membrane' is contradicted by the experimentally supported annotation of 'periplasm' (GO:0042597). The question key appears to conflate the periplasmic space with the plasma membrane, or to treat 'cell envelope' as equivalent to 'plasma membrane.'
- The correct GO term (periplasmic space, GO:0042597) is not among the four choices, making the question structurally flawed: the model is forced to select the least-wrong option rather than the correct one.
- The GO term GO:0005886 lists 'bacterial inner membrane' as a NARROW synonym, confirming that 'plasma membrane' in bacterial context refers to the inner membrane itself, not the periplasmic space between inner and outer membranes.
- The model's selection of D would be correct per the answer key but biologically inaccurate; this may cause scoring inconsistencies if the benchmark is later corrected.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is clearly bacterial (hydrophobic N-terminal signal peptide, peptidoglycan endopeptidase domain). Options A (host cell nucleolus) and C (nematocyst) are eukaryotic/cnidarian-specific structures incompatible with a bacterial protein. Option B (vesicle) is inconsistent with a soluble peptidoglycan-hydrolyzing enzyme lacking vesicle-targeting motifs. By elimination, D (plasma membrane) is the only remaining option. A model can reach D through general biological reasoning about organism type and protein function, even though the true location (periplasm) is not listed.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The correct biological answer (periplasm) is absent from the options, so the model cannot positively identify the true location. It arrives at D only by elimination of clearly impossible choices, not by recognizing the actual compartment.",
    "reason": "General biological knowledge (bacterial organism, peptidoglycan enzyme function, absence of eukaryotic/cnidarian/vesicular features) allows elimination of A, B, and C, leaving D. This constitutes a valid reasoning path, though the underlying key is factually incorrect."
  },
  "case_id": "GO_cellular_component_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H5",
      "H6",
      "GO1"
    ],
    "judgment": "contradicted",
    "reason": "The UniProt entry Q9KUL5 (Peptidoglycan DD-endopeptidase ShyB, Vibrio cholerae) explicitly annotates the subcellular location as 'Periplasm' (GO:0042597, periplasmic space) with experimental evidence (ECO:0000305, PubMed:23834664). The GO cross-reference confirms 'C:periplasmic space.' The plasma membrane (GO:0005886, synonym 'bacterial inner membrane') is a distinct structure from the periplasmic space in Gram-negative bacteria. The protein has an N-terminal Sec signal peptide (MGQFRFLALIVAVLCFSVALFLPTA) for export but no transmembrane anchor, so its mature functional location is the periplasm, not the membrane itself. The expected answer 'plasma membrane' contradicts the experimentally supported annotation."
  },
  "important_caveats": [
    "The expected answer 'plasma membrane' is contradicted by the experimentally supported annotation of 'periplasm' (GO:0042597). The question key appears to conflate the periplasmic space with the plasma membrane, or to treat 'cell envelope' as equivalent to 'plasma membrane.'",
    "The correct GO term (periplasmic space, GO:0042597) is not among the four choices, making the question structurally flawed: the model is forced to select the least-wrong option rather than the correct one.",
    "The GO term GO:0005886 lists 'bacterial inner membrane' as a NARROW synonym, confirming that 'plasma membrane' in bacterial context refers to the inner membrane itself, not the periplasmic space between inner and outer membranes.",
    "The model's selection of D would be correct per the answer key but biologically inaccurate; this may cause scoring inconsistencies if the benchmark is later corrected."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the true answer (periplasm) is missing, the remaining options A, B, and C are so clearly incompatible with a bacterial peptidoglycan endopeptidase that only D survives elimination. No alternative among the listed options is defensible as the correct answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0028",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The UniProt entry Q9KUL5 (Peptidoglycan DD-endopeptidase ShyB, Vibrio cholerae) explicitly annotates the subcellular location as 'Periplasm' (GO:0042597, periplasmic space) with experimental evidence (ECO:0000305, PubMed:23834664). The GO cross-reference confirms 'C:periplasmic space.' The plasma membrane (GO:0005886, synonym 'bacterial inner membrane') is a distinct structure from the periplasmic space in Gram-negative bacteria. The protein has an N-terminal Sec signal peptide (MGQFRFLALIVAVLCFSVALFLPTA) for export but no transmembrane anchor, so its mature functional location is the periplasm, not the membrane itself. The expected answer 'plasma membrane' contradicts the experimentally supported annotation.",
    "evidence_ids": ["C5", "C6", "C7", "H5", "H6", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is clearly bacterial (hydrophobic N-terminal signal peptide, peptidoglycan endopeptidase domain). Options A (host cell nucleolus) and C (nematocyst) are eukaryotic/cnidarian-specific structures incompatible with a bacterial protein. Option B (vesicle) is inconsistent with a soluble peptidoglycan-hydrolyzing enzyme lacking vesicle-targeting motifs. By elimination, D (plasma membrane) is the only remaining option. A model can reach D through general biological reasoning about organism type and protein function, even though the true location (periplasm) is not listed.",
    "missing_item_specific_fact": "The correct biological answer (periplasm) is absent from the options, so the model cannot positively identify the true location. It arrives at D only by elimination of clearly impossible choices, not by recognizing the actual compartment.",
    "reason": "General biological knowledge (bacterial organism, peptidoglycan enzyme function, absence of eukaryotic/cnidarian/vesicular features) allows elimination of A, B, and C, leaving D. This constitutes a valid reasoning path, though the underlying key is factually incorrect."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the true answer (periplasm) is missing, the remaining options A, B, and C are so clearly incompatible with a bacterial peptidoglycan endopeptidase that only D survives elimination. No alternative among the listed options is defensible as the correct answer."
  },
  "important_caveats": [
    "The expected answer 'plasma membrane' is contradicted by the experimentally supported annotation of 'periplasm' (GO:0042597). The question key appears to conflate the periplasmic space with the plasma membrane, or to treat 'cell envelope' as equivalent to 'plasma membrane.'",
    "The correct GO term (periplasmic space, GO:0042597) is not among the four choices, making the question structurally flawed: the model is forced to select the least-wrong option rather than the correct one.",
    "The GO term GO:0005886 lists 'bacterial inner membrane' as a NARROW synonym, confirming that 'plasma membrane' in bacterial context refers to the inner membrane itself, not the periplasmic space between inner and outer membranes.",
    "The model's selection of D would be correct per the answer key but biologically inaccurate; this may cause scoring inconsistencies if the benchmark is later corrected."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `current_historical_evidence_type_distinction`.

> C5/H5 annotate periplasm; C6 currently labels periplasmic space IC:UniProtKB with ECO:0000305, whereas H6 historically labels it IEA:UniProtKB-SubCell. No cited field asserts plasma membrane.

**Remaining uncertainty:** The model calls the GO annotation computational without separating current IC from historical IEA. Preserve that source/version distinction; periplasm evidence does not by itself exclude all membrane association.

Evidence checked: [H5](#evidence-h5), [H6](#evidence-h6), [C5](#evidence-c5), [C6](#evidence-c6).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `Q9KUL5` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 122. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:03.079631+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"23834664","source":"PubMed"}],"id":"SL-0200","value":"Periplasm"}}]}
```

Source SHA-256: `1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:03.079631+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000305","id":"30782657","source":"PubMed"}],"id":"GO:0042597","properties":[{"key":"GoTerm","value":"C:periplasmic space"},{"key":"GoEvidenceType","value":"IC:UniProtKB"}]}
```

Source SHA-256: `1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KUL5.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:33:03.079631+00:00.  

```json
{"citation":{"authors":["Doerr T.","Cava F.","Lam H.","Davis B.M.","Waldor M.K."],"citationCrossReferences":[{"database":"PubMed","id":"23834664"},{"database":"DOI","id":"10.1111/mmi.12323"}],"citationType":"journal article","firstPage":"949","id":"23834664","journal":"Mol. Microbiol.","lastPage":"962","publicationDate":"2013","title":"Substrate specificity of an elongation-specific peptidoglycan endopeptidase and its implications for cell wall architecture and growth of Vibrio cholerae.","volume":"89"},"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"23834664","source":"PubMed"}],"type":"STRAIN","value":"ATCC 39315 / El Tor Inaba N16961"}],"referenceNumber":2,"referencePositions":["SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `1a012051c558ee6fd878608af744d11d6b39c2a2321431a37e26522e1959abde`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)  
**Locator:** `lines 79-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:33:12.389220+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:23834664}.
```

Source SHA-256: `b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KUL5?format=txt&versions=122)  
**Locator:** `lines 121-121`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:33:12.389220+00:00.  

```text
DR   GO; GO:0042597; C:periplasmic space; IEA:UniProtKB-SubCell.
```

Source SHA-256: `b9f7a140df11a5f08c01597b78b8022558b8ed9a38f84cfba42460807a20b310`.

### Evidence GO1

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
