# GO_cellular_component_0107

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — cytosolic large ribosomal subunit

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKYPKQIRTYCPFCKRHTIHKVEKVKKRPRSELSAGQRRFRRKLKGYTGFPRPNPAGREKPVKKLDLRFRCTVCGKAHTRGQGFRVKKFELVEV

[Multiple Choices]
A. neuromuscular junction
B. cytosolic large ribosomal subunit
C. mitochondrial inner membrane
D. Golgi apparatus
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

> The supplied sequence exactly matches the reviewed Thermococcus kodakarensis protein annotated as large ribosomal subunit protein eL42. Its GO annotation is cytosolic large ribosomal subunit, supporting choice B. This support is annotation-based: the protein name uses a HAMAP computational rule, and the GO annotation has IBA evidence, not direct experimental localization in the supplied evidence.

Citations as saved: [C1](#evidence-c1), [C3](#evidence-c3), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The short, Lys/Arg-rich sequence lacks an obvious transmembrane segment or secretory signal, which weighs against the mitochondrial inner membrane and Golgi choices; its basic character is compatible with a ribosomal protein. But those broad features do not identify it specifically as a large-subunit ribosomal protein.


**Missing item-specific fact**

> Identifying the sequence as archaeal ribosomal protein eL42, or otherwise establishing its membership in the large ribosomal subunit, requires protein-family or homology information not provided in the question.


**Reason**

> Sequence composition can make B plausible and the membrane/secretory options less plausible, but the precise ribosomal-subunit localization depends on identifying this particular protein family.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied annotation supports B, and the other choices are not comparably supported by the sequence. The sequence-only evidence is less decisive than the reviewer-only protein annotation.


### Important caveats

- Reviewer-only accession and annotation evidence was not available to the evaluated model.
- The GO evidence is IBA, so it should not be represented as direct experimental localization.
- The GO term has a prokaryotic large-ribosomal-subunit synonym, making its use for this archaeal protein appropriate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The short, Lys/Arg-rich sequence lacks an obvious transmembrane segment or secretory signal, which weighs against the mitochondrial inner membrane and Golgi choices; its basic character is compatible with a ribosomal protein. But those broad features do not identify it specifically as a large-subunit ribosomal protein.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying the sequence as archaeal ribosomal protein eL42, or otherwise establishing its membership in the large ribosomal subunit, requires protein-family or homology information not provided in the question.",
    "reason": "Sequence composition can make B plausible and the membrane/secretory options less plausible, but the precise ribosomal-subunit localization depends on identifying this particular protein family."
  },
  "case_id": "GO_cellular_component_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C3",
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Thermococcus kodakarensis protein annotated as large ribosomal subunit protein eL42. Its GO annotation is cytosolic large ribosomal subunit, supporting choice B. This support is annotation-based: the protein name uses a HAMAP computational rule, and the GO annotation has IBA evidence, not direct experimental localization in the supplied evidence."
  },
  "important_caveats": [
    "Reviewer-only accession and annotation evidence was not available to the evaluated model.",
    "The GO evidence is IBA, so it should not be represented as direct experimental localization.",
    "The GO term has a prokaryotic large-ribosomal-subunit synonym, making its use for this archaeal protein appropriate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied annotation supports B, and the other choices are not comparably supported by the sequence. The sequence-only evidence is less decisive than the reviewer-only protein annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed Thermococcus kodakarensis protein annotated as large ribosomal subunit protein eL42. Its GO annotation is cytosolic large ribosomal subunit, supporting choice B. This support is annotation-based: the protein name uses a HAMAP computational rule, and the GO annotation has IBA evidence, not direct experimental localization in the supplied evidence.",
    "evidence_ids": ["C1", "C3", "C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The short, Lys/Arg-rich sequence lacks an obvious transmembrane segment or secretory signal, which weighs against the mitochondrial inner membrane and Golgi choices; its basic character is compatible with a ribosomal protein. But those broad features do not identify it specifically as a large-subunit ribosomal protein.",
    "missing_item_specific_fact": "Identifying the sequence as archaeal ribosomal protein eL42, or otherwise establishing its membership in the large ribosomal subunit, requires protein-family or homology information not provided in the question.",
    "reason": "Sequence composition can make B plausible and the membrane/secretory options less plausible, but the precise ribosomal-subunit localization depends on identifying this particular protein family."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied annotation supports B, and the other choices are not comparably supported by the sequence. The sequence-only evidence is less decisive than the reviewer-only protein annotation."
  },
  "important_caveats": [
    "Reviewer-only accession and annotation evidence was not available to the evaluated model.",
    "The GO evidence is IBA, so it should not be represented as direct experimental localization.",
    "The GO term has a prokaryotic large-ribosomal-subunit synonym, making its use for this archaeal protein appropriate."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q5JE51 is named 'Large ribosomal subunit protein eL42' (gene rpl44e) with GO annotation GO:0022625 'cytosolic large ribosomal subunit'. The sequence matches exactly (94 aa, SHA256 confirmed). The annotation evidence code is IBA:GO_Central (computational transfer), not direct experimental evidence, but the protein name, zinc-binding motifs (C-x-x-C patterns consistent with eL42), and highly basic character are consistent with a ribosomal protein. The expected answer B aligns with the database annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 94-aa sequence is extremely short, highly basic (many K/R residues), and contains paired cysteine motifs (CPFCKR...CTVCGKAHTRGQGFRVKKFELVEV) characteristic of zinc-binding ribosomal proteins. It lacks any signal peptide, transmembrane domain, mitochondrial targeting sequence, or Golgi retention signal, making options C (mitochondrial inner membrane) and D (Golgi apparatus) inconsistent with the sequence's biophysical properties. Option A (neuromuscular junction) is a vertebrate/invertebrate synaptic structure with no plausible connection to a small, basic, zinc-binding protein. The basic, compact, rRNA-interacting character is a well-known hallmark of ribosomal proteins, making B the only biologically coherent option. Additionally, if the model recognizes the organism as archaeal (Thermococcus kodakarensis), options A, C, and D can be eliminated outright since archaea lack neuromuscular junctions, mitochondria, and Golgi apparatus.


**Missing item-specific fact**

> The exact distinction between 'large' and 'small' ribosomal subunit membership, and the precise GO term 'cytosolic large ribosomal subunit' vs. a more generic 'ribosome' annotation, would benefit from knowing the specific eL42 zinc-binding motif. However, B is the only ribosomal option among the choices, so this granularity is not required to select the correct answer.


**Reason**

> General biological reasoning about protein biophysics (basic charge, zinc-binding motifs, absence of organelle-targeting signals) and cell biology (archaea lack mitochondria, Golgi, and neuromuscular junctions) provides meaningful grounds to eliminate A, C, and D and select B. The sequence itself carries sufficient structural and compositional information to support this inference without requiring memorization of the specific UniProt annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A, C, and D describe eukaryotic-specific structures or compartments with no plausible association to a small, basic, zinc-binding archaeal protein. B is the only option consistent with the sequence's biophysical properties and biological context. No ambiguity among choices.


### Important caveats

- The GO annotation uses evidence code IBA:GO_Central (inferred by biological aspect from another annotation), meaning the 'cytosolic large ribosomal subunit' assignment is computationally transferred rather than experimentally verified for this specific archaeal protein.
- The term 'cytosolic large ribosomal subunit' (GO:0022625) is eukaryotic-centric; archaeal ribosomes are structurally related but taxonomically distinct. UniProt nonetheless assigns this term via IBA transfer, so the expected answer matches the database annotation despite this taxonomic nuance.
- The organism identity (Thermococcus kodakarensis, an archaeon) is not provided in the evaluated model input; the model must infer prokaryotic/archaeal origin from sequence features or general knowledge to fully leverage the elimination of eukaryotic-specific compartments.
- The reviewer identified the accession (Q5JE51) from dataset metadata absent from the model input; this identification is reviewer-only and does not affect the model's reasoning pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 94-aa sequence is extremely short, highly basic (many K/R residues), and contains paired cysteine motifs (CPFCKR...CTVCGKAHTRGQGFRVKKFELVEV) characteristic of zinc-binding ribosomal proteins. It lacks any signal peptide, transmembrane domain, mitochondrial targeting sequence, or Golgi retention signal, making options C (mitochondrial inner membrane) and D (Golgi apparatus) inconsistent with the sequence's biophysical properties. Option A (neuromuscular junction) is a vertebrate/invertebrate synaptic structure with no plausible connection to a small, basic, zinc-binding protein. The basic, compact, rRNA-interacting character is a well-known hallmark of ribosomal proteins, making B the only biologically coherent option. Additionally, if the model recognizes the organism as archaeal (Thermococcus kodakarensis), options A, C, and D can be eliminated outright since archaea lack neuromuscular junctions, mitochondria, and Golgi apparatus.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact distinction between 'large' and 'small' ribosomal subunit membership, and the precise GO term 'cytosolic large ribosomal subunit' vs. a more generic 'ribosome' annotation, would benefit from knowing the specific eL42 zinc-binding motif. However, B is the only ribosomal option among the choices, so this granularity is not required to select the correct answer.",
    "reason": "General biological reasoning about protein biophysics (basic charge, zinc-binding motifs, absence of organelle-targeting signals) and cell biology (archaea lack mitochondria, Golgi, and neuromuscular junctions) provides meaningful grounds to eliminate A, C, and D and select B. The sequence itself carries sufficient structural and compositional information to support this inference without requiring memorization of the specific UniProt annotation."
  },
  "case_id": "GO_cellular_component_0107",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q5JE51 is named 'Large ribosomal subunit protein eL42' (gene rpl44e) with GO annotation GO:0022625 'cytosolic large ribosomal subunit'. The sequence matches exactly (94 aa, SHA256 confirmed). The annotation evidence code is IBA:GO_Central (computational transfer), not direct experimental evidence, but the protein name, zinc-binding motifs (C-x-x-C patterns consistent with eL42), and highly basic character are consistent with a ribosomal protein. The expected answer B aligns with the database annotation."
  },
  "important_caveats": [
    "The GO annotation uses evidence code IBA:GO_Central (inferred by biological aspect from another annotation), meaning the 'cytosolic large ribosomal subunit' assignment is computationally transferred rather than experimentally verified for this specific archaeal protein.",
    "The term 'cytosolic large ribosomal subunit' (GO:0022625) is eukaryotic-centric; archaeal ribosomes are structurally related but taxonomically distinct. UniProt nonetheless assigns this term via IBA transfer, so the expected answer matches the database annotation despite this taxonomic nuance.",
    "The organism identity (Thermococcus kodakarensis, an archaeon) is not provided in the evaluated model input; the model must infer prokaryotic/archaeal origin from sequence features or general knowledge to fully leverage the elimination of eukaryotic-specific compartments.",
    "The reviewer identified the accession (Q5JE51) from dataset metadata absent from the model input; this identification is reviewer-only and does not affect the model's reasoning pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D describe eukaryotic-specific structures or compartments with no plausible association to a small, basic, zinc-binding archaeal protein. B is the only option consistent with the sequence's biophysical properties and biological context. No ambiguity among choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0107",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q5JE51 is named 'Large ribosomal subunit protein eL42' (gene rpl44e) with GO annotation GO:0022625 'cytosolic large ribosomal subunit'. The sequence matches exactly (94 aa, SHA256 confirmed). The annotation evidence code is IBA:GO_Central (computational transfer), not direct experimental evidence, but the protein name, zinc-binding motifs (C-x-x-C patterns consistent with eL42), and highly basic character are consistent with a ribosomal protein. The expected answer B aligns with the database annotation.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 94-aa sequence is extremely short, highly basic (many K/R residues), and contains paired cysteine motifs (CPFCKR...CTVCGKAHTRGQGFRVKKFELVEV) characteristic of zinc-binding ribosomal proteins. It lacks any signal peptide, transmembrane domain, mitochondrial targeting sequence, or Golgi retention signal, making options C (mitochondrial inner membrane) and D (Golgi apparatus) inconsistent with the sequence's biophysical properties. Option A (neuromuscular junction) is a vertebrate/invertebrate synaptic structure with no plausible connection to a small, basic, zinc-binding protein. The basic, compact, rRNA-interacting character is a well-known hallmark of ribosomal proteins, making B the only biologically coherent option. Additionally, if the model recognizes the organism as archaeal (Thermococcus kodakarensis), options A, C, and D can be eliminated outright since archaea lack neuromuscular junctions, mitochondria, and Golgi apparatus.",
    "missing_item_specific_fact": "The exact distinction between 'large' and 'small' ribosomal subunit membership, and the precise GO term 'cytosolic large ribosomal subunit' vs. a more generic 'ribosome' annotation, would benefit from knowing the specific eL42 zinc-binding motif. However, B is the only ribosomal option among the choices, so this granularity is not required to select the correct answer.",
    "reason": "General biological reasoning about protein biophysics (basic charge, zinc-binding motifs, absence of organelle-targeting signals) and cell biology (archaea lack mitochondria, Golgi, and neuromuscular junctions) provides meaningful grounds to eliminate A, C, and D and select B. The sequence itself carries sufficient structural and compositional information to support this inference without requiring memorization of the specific UniProt annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A, C, and D describe eukaryotic-specific structures or compartments with no plausible association to a small, basic, zinc-binding archaeal protein. B is the only option consistent with the sequence's biophysical properties and biological context. No ambiguity among choices."
  },
  "important_caveats": [
    "The GO annotation uses evidence code IBA:GO_Central (inferred by biological aspect from another annotation), meaning the 'cytosolic large ribosomal subunit' assignment is computationally transferred rather than experimentally verified for this specific archaeal protein.",
    "The term 'cytosolic large ribosomal subunit' (GO:0022625) is eukaryotic-centric; archaeal ribosomes are structurally related but taxonomically distinct. UniProt nonetheless assigns this term via IBA transfer, so the expected answer matches the database annotation despite this taxonomic nuance.",
    "The organism identity (Thermococcus kodakarensis, an archaeon) is not provided in the evaluated model input; the model must infer prokaryotic/archaeal origin from sequence features or general knowledge to fully leverage the elimination of eukaryotic-specific compartments.",
    "The reviewer identified the accession (Q5JE51) from dataset metadata absent from the model input; this identification is reviewer-only and does not affect the model's reasoning pathway."
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

**Accession:** `Q5JE51` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 107. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JE51.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:15.985869+00:00.  

```json
"Q5JE51"
```

Source SHA-256: `3f4f49f4fdcd815348ad11724d3db6ac5069cf1b1096d21c9283e9d4baee6a33`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JE51.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:15.985869+00:00.  

```json
{"commonName":"Pyrococcus kodakaraensis (strain KOD1)","lineage":["Archaea","Methanobacteriati","Methanobacteriota","Thermococci","Thermococcales","Thermococcaceae","Thermococcus"],"scientificName":"Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)","taxonId":69014}
```

Source SHA-256: `3f4f49f4fdcd815348ad11724d3db6ac5069cf1b1096d21c9283e9d4baee6a33`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JE51.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:15.985869+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_01476","source":"HAMAP-Rule"}],"value":"Large ribosomal subunit protein eL42"}}}
```

Source SHA-256: `3f4f49f4fdcd815348ad11724d3db6ac5069cf1b1096d21c9283e9d4baee6a33`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5JE51.json)  
**Locator:** `/uniProtKBCrossReferences/25`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:15.985869+00:00.  

```json
{"database":"GO","id":"GO:0022625","properties":[{"key":"GoTerm","value":"C:cytosolic large ribosomal subunit"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `3f4f49f4fdcd815348ad11724d3db6ac5069cf1b1096d21c9283e9d4baee6a33`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JE51?format=txt&versions=107)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-02T04:31:20.329246+00:00.  

```text
ID   RL44E_THEKO             Reviewed;          94 AA.
AC   Q5JE51;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   15-FEB-2005, sequence version 1.
DT   28-JAN-2026, entry version 107.
DE   RecName: Full=Large ribosomal subunit protein eL42 {ECO:0000255|HAMAP-Rule:MF_01476};
GN   Name=rpl44e {ECO:0000255|HAMAP-Rule:MF_01476};
GN   OrderedLocusNames=TK1098 {ECO:0000312|EMBL:BAD85287.1};
OS   Thermococcus kodakarensis (strain ATCC BAA-918 / JCM 12380 / KOD1)
OS   (Pyrococcus kodakaraensis (strain KOD1)).
OC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;
OC   Thermococcaceae; Thermococcus.
OX   NCBI_TaxID=69014;
```

Source SHA-256: `54b03ede26cd2994aa8e16a71cdff8115aa30c55b07be10c28b083c9be3d4ed5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5JE51?format=txt&versions=107)  
**Locator:** `lines 75-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 107 / 1.  
**Retrieved:** 2026-11-02T04:31:20.329246+00:00.  

```text
DR   GO; GO:0022625; C:cytosolic large ribosomal subunit; IBA:GO_Central.
```

Source SHA-256: `54b03ede26cd2994aa8e16a71cdff8115aa30c55b07be10c28b083c9be3d4ed5`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 160556-160571`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0022625
name: cytosolic large ribosomal subunit
namespace: cellular_component
alt_id: GO:0005842
alt_id: GO:0009282
alt_id: GO:0030498
alt_id: GO:0030872
def: "The large subunit of a ribosome located in the cytosol." [GOC:mtg_sensu]
synonym: "50S ribosomal subunit" NARROW []
synonym: "60S ribosomal subunit" NARROW []
synonym: "eukaryotic ribosomal LSU" NARROW []
synonym: "prokaryotic large ribosomal subunit" NARROW []
is_a: GO:0015934 ! large ribosomal subunit
relationship: part_of GO:0022626 ! cytosolic ribosome

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 107. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
