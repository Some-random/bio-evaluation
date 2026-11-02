# GO_cellular_component_0024

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — extracellular region

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MFKRFNRGQISFEFSIIVLSILLISTITITYFLTSSFDEGTRTLDKIDLGAKTAVSLVNSGYNGTQTEGTLIYAGMTWDNAGNNYENITVYISNTTPVPVNTRLFVKNYTIESQGIDTTKYDFTIAWSG

[Multiple Choices]
A. extracellular region
B. mitochondrion
C. L-cysteine desulfurase complex
D. collagen-containing extracellular matrix
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

> The sequence-matched UniProt record assigns this protein to secreted, cell-surface, and fimbrial locations, and includes an extracellular-region GO annotation. The GO annotation is IEA; the location annotation is attributed to literature but is not itself a direct experimental result in the supplied evidence.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus has a basic region followed by a long hydrophobic stretch, consistent with an export/prepilin signal and supporting a non-mitochondrial, externally located protein. The sequence also lacks an evident collagen-like repeat pattern, making the collagen-containing matrix option a poor fit.


**Missing item-specific fact**

> Identifying the protein specifically as the archaeal pilin EpdA and knowing its reported secretion/fimbrial localization would require a protein-specific annotation or literature lookup, but the sequence provides meaningful grounds for favoring the broad extracellular option.


**Reason**

> The N-terminal sequence provides a defensible export-signal argument that distinguishes extracellular localization from the listed intracellular alternatives; the more specific reported pilin identity is not necessary to make that broad choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein may also be associated with the cell surface and fimbriae, but those are not listed choices. Among the options, extracellular region is the best-supported broad location; the collagen-containing extracellular matrix option is not equivalent.


### Important caveats

- The GO extracellular-region annotation is computationally assigned (IEA), while the cited subcellular-location annotation is literature-attributed; the excerpts do not independently establish the experiments underlying it.
- The reviewer-only database identity and localization information were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus has a basic region followed by a long hydrophobic stretch, consistent with an export/prepilin signal and supporting a non-mitochondrial, externally located protein. The sequence also lacks an evident collagen-like repeat pattern, making the collagen-containing matrix option a poor fit.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Identifying the protein specifically as the archaeal pilin EpdA and knowing its reported secretion/fimbrial localization would require a protein-specific annotation or literature lookup, but the sequence provides meaningful grounds for favoring the broad extracellular option.",
    "reason": "The N-terminal sequence provides a defensible export-signal argument that distinguishes extracellular localization from the listed intracellular alternatives; the more specific reported pilin identity is not necessary to make that broad choice."
  },
  "case_id": "GO_cellular_component_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H4",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein to secreted, cell-surface, and fimbrial locations, and includes an extracellular-region GO annotation. The GO annotation is IEA; the location annotation is attributed to literature but is not itself a direct experimental result in the supplied evidence."
  },
  "important_caveats": [
    "The GO extracellular-region annotation is computationally assigned (IEA), while the cited subcellular-location annotation is literature-attributed; the excerpts do not independently establish the experiments underlying it.",
    "The reviewer-only database identity and localization information were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may also be associated with the cell surface and fimbriae, but those are not listed choices. Among the options, extracellular region is the best-supported broad location; the collagen-containing extracellular matrix option is not equivalent."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein to secreted, cell-surface, and fimbrial locations, and includes an extracellular-region GO annotation. The GO annotation is IEA; the location annotation is attributed to literature but is not itself a direct experimental result in the supplied evidence.",
    "evidence_ids": ["C5", "C7", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus has a basic region followed by a long hydrophobic stretch, consistent with an export/prepilin signal and supporting a non-mitochondrial, externally located protein. The sequence also lacks an evident collagen-like repeat pattern, making the collagen-containing matrix option a poor fit.",
    "missing_item_specific_fact": "Identifying the protein specifically as the archaeal pilin EpdA and knowing its reported secretion/fimbrial localization would require a protein-specific annotation or literature lookup, but the sequence provides meaningful grounds for favoring the broad extracellular option.",
    "reason": "The N-terminal sequence provides a defensible export-signal argument that distinguishes extracellular localization from the listed intracellular alternatives; the more specific reported pilin identity is not necessary to make that broad choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein may also be associated with the cell surface and fimbriae, but those are not listed choices. Among the options, extracellular region is the best-supported broad location; the collagen-containing extracellular matrix option is not equivalent."
  },
  "important_caveats": [
    "The GO extracellular-region annotation is computationally assigned (IEA), while the cited subcellular-location annotation is literature-attributed; the excerpts do not independently establish the experiments underlying it.",
    "The reviewer-only database identity and localization information were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q6M0N7 annotates the protein's subcellular location as Secreted, Cell surface, and Fimbrium (C5, H4), and includes GO:0005576 'extracellular region' as an IEA:UniProtKB-SubCell annotation (C7, H6). Among the four options, 'extracellular region' is the only one consistent with a secreted/cell-surface pilin from an archaeon. The protein is definitively not mitochondrial (archaea lack mitochondria), not a cysteine desulfurase complex (it is a structural pilin), and not part of a collagen-containing matrix (collagen is vertebrate-specific). The GO term note that 'extracellular region' is intended for non-surface-attached products introduces minor imprecision, but the annotation is present in the database and A is clearly the best among the given choices.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H4](#evidence-h4), [H6](#evidence-h6), [GO1](#evidence-go1), [GO2](#evidence-go2), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains a clearly hydrophobic stretch (IIVLSILLISTITITYFLT) characteristic of a signal peptide, indicating the protein is exported from the cytoplasm. The protein is only 129 aa with no enzymatic catalytic motifs, arguing against C (L-cysteine desulfurase complex, a PLP-dependent enzyme). No mitochondrial targeting presequence (amphipathic N-terminal helix) is present, and the overall sequence composition is inconsistent with mitochondrial import signals, arguing against B. No Gly-X-Y collagen repeats are present and the small size is incompatible with a collagen-containing matrix, arguing against D. The combination of a signal peptide, small structural-protein size, and absence of organellar targeting sequences supports an extracellular/secreted localization.


**Missing item-specific fact**

> None critical. Knowing the organism is an archaeon (Methanococcus maripaludis) would definitively exclude mitochondrion, but the absence of a mitochondrial targeting sequence in the sequence itself already argues against B. Identifying the protein as a specific pilin (EpdA) would confirm the answer but is not strictly necessary given the signal-peptide reasoning.


**Reason**

> The sequence provides a recognizable signal peptide, small size, and absence of enzymatic or organellar-targeting features. General biological knowledge about signal peptides indicating secretion, the absence of mitochondrial targeting sequences, and the lack of collagen repeats or desulfurase motifs allow a model to eliminate B, C, and D through reasoning rather than requiring recall of this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While 'cell surface' would be a more precise GO term than 'extracellular region' for a pilin (per the GO:0005576 usage note), 'cell surface' is not among the options. Among the four given choices, A is unambiguously the best fit. The distractors B, C, and D are clearly incompatible with the sequence features and biological context.


### Important caveats

- The GO:0005576 annotation is IEA:UniProtKB-SubCell (inferred from electronic annotation of the SubCell field), not a direct experimental GO annotation. The primary experimental evidence (PubMed:17114255, PubMed:21075925) supports 'Secreted/Cell surface/Fimbrium' rather than specifically 'extracellular region'.
- The GO definition note for GO:0005576 states it is 'intended to annotate gene products that are not attached to the cell surface,' which is slightly at odds with a pilin that is a structural component of surface fimbriae. However, the annotation exists in the database and A remains the best option among those provided.
- The organism identity (archaeon) is not explicitly stated in the question; a model must infer non-eukaryotic context from sequence features or general knowledge to fully exclude mitochondrion.
- The UniProt entry was first publicly released on 2025-04-09, so the benchmark's author may have had access to this annotation at construction time, but this is a reviewer-only observation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a clearly hydrophobic stretch (IIVLSILLISTITITYFLT) characteristic of a signal peptide, indicating the protein is exported from the cytoplasm. The protein is only 129 aa with no enzymatic catalytic motifs, arguing against C (L-cysteine desulfurase complex, a PLP-dependent enzyme). No mitochondrial targeting presequence (amphipathic N-terminal helix) is present, and the overall sequence composition is inconsistent with mitochondrial import signals, arguing against B. No Gly-X-Y collagen repeats are present and the small size is incompatible with a collagen-containing matrix, arguing against D. The combination of a signal peptide, small structural-protein size, and absence of organellar targeting sequences supports an extracellular/secreted localization.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Knowing the organism is an archaeon (Methanococcus maripaludis) would definitively exclude mitochondrion, but the absence of a mitochondrial targeting sequence in the sequence itself already argues against B. Identifying the protein as a specific pilin (EpdA) would confirm the answer but is not strictly necessary given the signal-peptide reasoning.",
    "reason": "The sequence provides a recognizable signal peptide, small size, and absence of enzymatic or organellar-targeting features. General biological knowledge about signal peptides indicating secretion, the absence of mitochondrial targeting sequences, and the lack of collagen repeats or desulfurase motifs allow a model to eliminate B, C, and D through reasoning rather than requiring recall of this specific UniProt entry."
  },
  "case_id": "GO_cellular_component_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H4",
      "H6",
      "GO1",
      "GO2",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q6M0N7 annotates the protein's subcellular location as Secreted, Cell surface, and Fimbrium (C5, H4), and includes GO:0005576 'extracellular region' as an IEA:UniProtKB-SubCell annotation (C7, H6). Among the four options, 'extracellular region' is the only one consistent with a secreted/cell-surface pilin from an archaeon. The protein is definitively not mitochondrial (archaea lack mitochondria), not a cysteine desulfurase complex (it is a structural pilin), and not part of a collagen-containing matrix (collagen is vertebrate-specific). The GO term note that 'extracellular region' is intended for non-surface-attached products introduces minor imprecision, but the annotation is present in the database and A is clearly the best among the given choices."
  },
  "important_caveats": [
    "The GO:0005576 annotation is IEA:UniProtKB-SubCell (inferred from electronic annotation of the SubCell field), not a direct experimental GO annotation. The primary experimental evidence (PubMed:17114255, PubMed:21075925) supports 'Secreted/Cell surface/Fimbrium' rather than specifically 'extracellular region'.",
    "The GO definition note for GO:0005576 states it is 'intended to annotate gene products that are not attached to the cell surface,' which is slightly at odds with a pilin that is a structural component of surface fimbriae. However, the annotation exists in the database and A remains the best option among those provided.",
    "The organism identity (archaeon) is not explicitly stated in the question; a model must infer non-eukaryotic context from sequence features or general knowledge to fully exclude mitochondrion.",
    "The UniProt entry was first publicly released on 2025-04-09, so the benchmark's author may have had access to this annotation at construction time, but this is a reviewer-only observation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While 'cell surface' would be a more precise GO term than 'extracellular region' for a pilin (per the GO:0005576 usage note), 'cell surface' is not among the options. Among the four given choices, A is unambiguously the best fit. The distractors B, C, and D are clearly incompatible with the sequence features and biological context."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q6M0N7 annotates the protein's subcellular location as Secreted, Cell surface, and Fimbrium (C5, H4), and includes GO:0005576 'extracellular region' as an IEA:UniProtKB-SubCell annotation (C7, H6). Among the four options, 'extracellular region' is the only one consistent with a secreted/cell-surface pilin from an archaeon. The protein is definitively not mitochondrial (archaea lack mitochondria), not a cysteine desulfurase complex (it is a structural pilin), and not part of a collagen-containing matrix (collagen is vertebrate-specific). The GO term note that 'extracellular region' is intended for non-surface-attached products introduces minor imprecision, but the annotation is present in the database and A is clearly the best among the given choices.",
    "evidence_ids": ["C5", "C7", "H4", "H6", "GO1", "GO2", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains a clearly hydrophobic stretch (IIVLSILLISTITITYFLT) characteristic of a signal peptide, indicating the protein is exported from the cytoplasm. The protein is only 129 aa with no enzymatic catalytic motifs, arguing against C (L-cysteine desulfurase complex, a PLP-dependent enzyme). No mitochondrial targeting presequence (amphipathic N-terminal helix) is present, and the overall sequence composition is inconsistent with mitochondrial import signals, arguing against B. No Gly-X-Y collagen repeats are present and the small size is incompatible with a collagen-containing matrix, arguing against D. The combination of a signal peptide, small structural-protein size, and absence of organellar targeting sequences supports an extracellular/secreted localization.",
    "missing_item_specific_fact": "None critical. Knowing the organism is an archaeon (Methanococcus maripaludis) would definitively exclude mitochondrion, but the absence of a mitochondrial targeting sequence in the sequence itself already argues against B. Identifying the protein as a specific pilin (EpdA) would confirm the answer but is not strictly necessary given the signal-peptide reasoning.",
    "reason": "The sequence provides a recognizable signal peptide, small size, and absence of enzymatic or organellar-targeting features. General biological knowledge about signal peptides indicating secretion, the absence of mitochondrial targeting sequences, and the lack of collagen repeats or desulfurase motifs allow a model to eliminate B, C, and D through reasoning rather than requiring recall of this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While 'cell surface' would be a more precise GO term than 'extracellular region' for a pilin (per the GO:0005576 usage note), 'cell surface' is not among the options. Among the four given choices, A is unambiguously the best fit. The distractors B, C, and D are clearly incompatible with the sequence features and biological context."
  },
  "important_caveats": [
    "The GO:0005576 annotation is IEA:UniProtKB-SubCell (inferred from electronic annotation of the SubCell field), not a direct experimental GO annotation. The primary experimental evidence (PubMed:17114255, PubMed:21075925) supports 'Secreted/Cell surface/Fimbrium' rather than specifically 'extracellular region'.",
    "The GO definition note for GO:0005576 states it is 'intended to annotate gene products that are not attached to the cell surface,' which is slightly at odds with a pilin that is a structural component of surface fimbriae. However, the annotation exists in the database and A remains the best option among those provided.",
    "The organism identity (archaeon) is not explicitly stated in the question; a model must infer non-eukaryotic context from sequence features or general knowledge to fully exclude mitochondrion.",
    "The UniProt entry was first publicly released on 2025-04-09, so the benchmark's author may have had access to this annotation at construction time, but this is a reviewer-only observation."
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

**Accession:** `Q6M0N7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 79. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:41.616325+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"17114255","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"17114255","source":"PubMed"}],"id":"SL-0310","value":"Cell surface"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"17114255","source":"PubMed"},{"evidenceCode":"ECO:0000305","id":"21075925","source":"PubMed"}],"id":"SL-0113","value":"Fimbrium"}}]}
```

Source SHA-256: `b4d3c92c92ead45123888e45348606d29c3ae34f9b057b90358cd28477fe4b49`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6M0N7.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:41.616325+00:00.  

```json
{"database":"GO","id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `b4d3c92c92ead45123888e45348606d29c3ae34f9b057b90358cd28477fe4b49`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N7?format=txt&versions=79)  
**Locator:** `lines 50-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-02T04:31:43.547179+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305|PubMed:17114255}. Cell
CC       surface {ECO:0000305|PubMed:17114255}. Fimbrium
CC       {ECO:0000305|PubMed:17114255, ECO:0000305|PubMed:21075925}.
```

Source SHA-256: `5654410b03ab2b92216e8a4d5cd369e58586563c2aaee840ec0c699d5542b1e5`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6M0N7?format=txt&versions=79)  
**Locator:** `lines 77-77`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-02T04:31:43.547179+00:00.  

```text
DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.
```

Source SHA-256: `5654410b03ab2b92216e8a4d5cd369e58586563c2aaee840ec0c699d5542b1e5`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 57481-57505`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005576
name: extracellular region
namespace: cellular_component
def: "The space external to the outermost structure of a cell. For cells without external protective or external encapsulating structures this refers to space outside of the plasma membrane. This term covers the host cell environment outside an intracellular parasite." [GOC:curators]
comment: Note that this term is intended to annotate gene products that are not attached to the cell surface. For gene products at the cell surface, consider annotating to external side of plasma membrane ; GO:0009897.
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_prokaryote
subset: goslim_prokaryote_ribbon
subset: goslim_yeast
synonym: "extracellular" EXACT []
xref: Wikipedia:Extracellular
is_a: GO:0110165 ! cellular anatomical structure

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 58975-58998`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005739
name: mitochondrion
namespace: cellular_component
def: "A semiautonomous, self replicating organelle that occurs in varying numbers, shapes, and sizes in the cytoplasm of virtually all eukaryotic cells. It is notably the site of tissue respiration." [GOC:giardia, ISBN:0198506732]
comment: Some anaerobic or microaerophilic organisms (e.g. Entamoeba histolytica, Giardia intestinalis and several Microsporidia species) do not have mitochondria, and contain mitochondrion-related organelles (MROs) instead, called mitosomes or hydrogenosomes, very likely derived from mitochondria. To annotate gene products located in these mitochondrial relics in species such as Entamoeba histolytica, Giardia intestinalis or others, please use GO:0032047 'mitosome' or GO:0042566 'hydrogenosome'. (See PMID:24316280 for a list of species currently known to contain mitochondrion-related organelles.)
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_flybase_ribbon
subset: goslim_generic
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_yeast
synonym: "mitochondria" EXACT []
xref: NIF_Subcellular:sao1860313010
xref: Wikipedia:Mitochondrion
is_a: GO:0043231 ! intracellular membrane-bounded organelle
relationship: part_of GO:0005737 ! cytoplasm

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 550305-550314`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:1990221
name: L-cysteine desulfurase complex
namespace: cellular_component
def: "A protein complex capable of cysteine desulfurase activity decomposing L-cysteine to L-alanine and sulfur. It belongs to a ubiquitous family of pyridoxal 5-phosphate (PLP)-dependent enzymes." [GOC:bhm, PMID:11827487]
synonym: "IscS" NARROW [GOC:bhm, GOC:dph]
synonym: "NifS" NARROW [GOC:bhm, GOC:dph]
synonym: "SufS complex" NARROW []
is_a: GO:1990228 ! sulfurtransferase complex

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 24. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
