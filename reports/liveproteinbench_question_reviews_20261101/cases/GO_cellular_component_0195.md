# GO_cellular_component_0195

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MQPFGDAWSQRHLAGVVLAGSVLSIVGSLYMILGFFFLRECRSFRHKLILGLAVSDLLLALNFFIPSLSMVTGREISSPWNEGFCSANGFLMQLFFAQIDVWQISIALITLLMLSGPSMVLKWIRENVWAVWLFPWLVSLIAAFFAFGFWDYANVGGFCWLGSRNIRLYFNYIPRWIIILVCLVIYIAVYRLILHARRRANIQKTYRGRASDRAPPQPVTTTAPATNPESEKVNPDEISSGNGSSSLDTSRSGSSTGFTQTVHDPAVAGQIQTAAERAQEEAEQQKQVRKIAIQMISYPLAYAVLWAIPTIVMIIQVARGGEGVSIHVEGLAKMLLVFNGFVDAHVYGFNERTAMGWRQRIRPAAQEDDEEAAGTSGGVHEVVSRPEPTLKNPNVWQQNMV

[Multiple Choices]
A. virion membrane
B. plasma membrane
C. ATAC complex
D. virus tail, tube
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

> The sequence-matched UniProt record reports experimentally supported localization to the cell membrane and annotates plasma membrane by UniProtKB-SubCell inference. The protein can relocalize to the vacuole after ligand stimulation, so plasma membrane is supported but not its only possible location.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a prominent multipass, GPCR-like membrane-protein architecture, consistent with a eukaryotic cell-surface receptor. That makes plasma membrane a defensible choice over the viral structures and chromatin-remodeling complex in the other options.


**Missing item-specific fact**

> The exact experimental localization and ligand-triggered vacuolar relocalization are not supplied; those are needed to establish this protein's observed localization rather than infer its likely compartment.


**Reason**

> The sequence and options provide a meaningful biological basis for selecting plasma membrane, although sequence-based inference alone does not establish the protein's full localization behavior.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports a membrane receptor, while the alternatives describe viral components or a chromatin complex. Vacuolar relocalization is not among the choices.


### Important caveats

- The experimental annotation says cell membrane; the more specific plasma membrane GO annotation is computationally inferred.
- The record notes ligand-stimulated relocalization to the vacuole, so localization can be condition-dependent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a prominent multipass, GPCR-like membrane-protein architecture, consistent with a eukaryotic cell-surface receptor. That makes plasma membrane a defensible choice over the viral structures and chromatin-remodeling complex in the other options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact experimental localization and ligand-triggered vacuolar relocalization are not supplied; those are needed to establish this protein's observed localization rather than infer its likely compartment.",
    "reason": "The sequence and options provide a meaningful biological basis for selecting plasma membrane, although sequence-based inference alone does not establish the protein's full localization behavior."
  },
  "case_id": "GO_cellular_component_0195",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports experimentally supported localization to the cell membrane and annotates plasma membrane by UniProtKB-SubCell inference. The protein can relocalize to the vacuole after ligand stimulation, so plasma membrane is supported but not its only possible location."
  },
  "important_caveats": [
    "The experimental annotation says cell membrane; the more specific plasma membrane GO annotation is computationally inferred.",
    "The record notes ligand-stimulated relocalization to the vacuole, so localization can be condition-dependent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a membrane receptor, while the alternatives describe viral components or a chromatin complex. Vacuolar relocalization is not among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0195",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports experimentally supported localization to the cell membrane and annotates plasma membrane by UniProtKB-SubCell inference. The protein can relocalize to the vacuole after ligand stimulation, so plasma membrane is supported but not its only possible location.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a prominent multipass, GPCR-like membrane-protein architecture, consistent with a eukaryotic cell-surface receptor. That makes plasma membrane a defensible choice over the viral structures and chromatin-remodeling complex in the other options.",
    "missing_item_specific_fact": "The exact experimental localization and ligand-triggered vacuolar relocalization are not supplied; those are needed to establish this protein's observed localization rather than infer its likely compartment.",
    "reason": "The sequence and options provide a meaningful biological basis for selecting plasma membrane, although sequence-based inference alone does not establish the protein's full localization behavior."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a membrane receptor, while the alternatives describe viral components or a chromatin complex. Vacuolar relocalization is not among the choices."
  },
  "important_caveats": [
    "The experimental annotation says cell membrane; the more specific plasma membrane GO annotation is computationally inferred.",
    "The record notes ligand-stimulated relocalization to the vacuole, so localization can be condition-dependent."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotation (C5/H3) states 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:38649409). GO:0005886 (plasma membrane) has 'cell membrane' as an EXACT synonym (GO1), and the GO cross-reference (C6/H4) directly assigns GO:0005886. The protein is identified as Ascaroside receptor GPR3, a GPCR, which is canonically a plasma membrane protein. The sequence displays the characteristic 7-TM GPCR topology consistent with this annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains approximately seven distinct hydrophobic stretches arranged in the canonical 7-transmembrane (7-TM) GPCR architecture, preceded by a signal-peptide-like N-terminal region and followed by a long intracellular C-terminal tail. This 7-TM topology is the hallmark of G-protein-coupled receptors, which are exclusively plasma membrane proteins in eukaryotes. This directly eliminates the ATAC complex (a soluble nuclear chromatin-remodeling assembly with no TM domains) and the virus tail tube (a viral structural protein with a completely different fold). While virion membrane proteins can contain TM domains, they do not exhibit the 7-TM GPCR topology with conserved motifs (e.g., the NPxxY-like motif visible near the C-terminus, the DRY-like motif in the third intracellular loop region). The overall architecture—extracellular N-terminus, seven TM helices, intracellular loops, and phosphorylation-site-rich C-tail—is diagnostic of a cell-surface receptor, not a viral envelope protein.


**Missing item-specific fact**

> None required. The 7-TM GPCR architecture is identifiable from the hydrophobicity pattern and topology of the sequence using general structural biology knowledge.


**Reason**

> A model with general knowledge of membrane protein topology can identify the 7-TM GPCR pattern from the sequence's hydrophobic stretches and distinguish it from viral membrane proteins, nuclear complexes, and viral structural proteins. The reasoning chain (multi-pass TM → GPCR topology → plasma membrane) relies on general biological knowledge rather than a protein-specific database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span very different biological categories (viral envelope, cell-surface receptor, nuclear chromatin complex, viral structural protein). The 7-TM GPCR architecture uniquely identifies the plasma membrane option. No other option is defensible given the sequence topology.


### Important caveats

- The UniProt GO annotation for plasma membrane carries evidence code IEA (inferred from electronic annotation, derived from the 'Cell membrane' subcellular location), while the primary subcellular location annotation itself is backed by experimental evidence (ECO:0000269, PubMed:38649409).
- The protein also relocalizes to the vacuole upon ligand stimulation (noted in C5/H3), but the primary/steady-state location is the cell membrane, consistent with the expected answer.
- The organism is a fungus (Arthrobotrys oligospora); 'plasma membrane' and 'cell membrane' are EXACT synonyms in GO (GO1), so the terminology is fully interchangeable here.
- The reviewer-only evidence confirms the sequence matches UniProt entry G1XJN1 exactly (SHA-256 match), but the evaluated model had no access to this identification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains approximately seven distinct hydrophobic stretches arranged in the canonical 7-transmembrane (7-TM) GPCR architecture, preceded by a signal-peptide-like N-terminal region and followed by a long intracellular C-terminal tail. This 7-TM topology is the hallmark of G-protein-coupled receptors, which are exclusively plasma membrane proteins in eukaryotes. This directly eliminates the ATAC complex (a soluble nuclear chromatin-remodeling assembly with no TM domains) and the virus tail tube (a viral structural protein with a completely different fold). While virion membrane proteins can contain TM domains, they do not exhibit the 7-TM GPCR topology with conserved motifs (e.g., the NPxxY-like motif visible near the C-terminus, the DRY-like motif in the third intracellular loop region). The overall architecture—extracellular N-terminus, seven TM helices, intracellular loops, and phosphorylation-site-rich C-tail—is diagnostic of a cell-surface receptor, not a viral envelope protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required. The 7-TM GPCR architecture is identifiable from the hydrophobicity pattern and topology of the sequence using general structural biology knowledge.",
    "reason": "A model with general knowledge of membrane protein topology can identify the 7-TM GPCR pattern from the sequence's hydrophobic stretches and distinguish it from viral membrane proteins, nuclear complexes, and viral structural proteins. The reasoning chain (multi-pass TM → GPCR topology → plasma membrane) relies on general biological knowledge rather than a protein-specific database lookup."
  },
  "case_id": "GO_cellular_component_0195",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO1",
      "C4"
    ],
    "judgment": "supported",
    "reason": "UniProt annotation (C5/H3) states 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:38649409). GO:0005886 (plasma membrane) has 'cell membrane' as an EXACT synonym (GO1), and the GO cross-reference (C6/H4) directly assigns GO:0005886. The protein is identified as Ascaroside receptor GPR3, a GPCR, which is canonically a plasma membrane protein. The sequence displays the characteristic 7-TM GPCR topology consistent with this annotation."
  },
  "important_caveats": [
    "The UniProt GO annotation for plasma membrane carries evidence code IEA (inferred from electronic annotation, derived from the 'Cell membrane' subcellular location), while the primary subcellular location annotation itself is backed by experimental evidence (ECO:0000269, PubMed:38649409).",
    "The protein also relocalizes to the vacuole upon ligand stimulation (noted in C5/H3), but the primary/steady-state location is the cell membrane, consistent with the expected answer.",
    "The organism is a fungus (Arthrobotrys oligospora); 'plasma membrane' and 'cell membrane' are EXACT synonyms in GO (GO1), so the terminology is fully interchangeable here.",
    "The reviewer-only evidence confirms the sequence matches UniProt entry G1XJN1 exactly (SHA-256 match), but the evaluated model had no access to this identification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span very different biological categories (viral envelope, cell-surface receptor, nuclear chromatin complex, viral structural protein). The 7-TM GPCR architecture uniquely identifies the plasma membrane option. No other option is defensible given the sequence topology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0195",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotation (C5/H3) states 'Cell membrane; Multi-pass membrane protein' with experimental evidence (ECO:0000269, PubMed:38649409). GO:0005886 (plasma membrane) has 'cell membrane' as an EXACT synonym (GO1), and the GO cross-reference (C6/H4) directly assigns GO:0005886. The protein is identified as Ascaroside receptor GPR3, a GPCR, which is canonically a plasma membrane protein. The sequence displays the characteristic 7-TM GPCR topology consistent with this annotation.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO1", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains approximately seven distinct hydrophobic stretches arranged in the canonical 7-transmembrane (7-TM) GPCR architecture, preceded by a signal-peptide-like N-terminal region and followed by a long intracellular C-terminal tail. This 7-TM topology is the hallmark of G-protein-coupled receptors, which are exclusively plasma membrane proteins in eukaryotes. This directly eliminates the ATAC complex (a soluble nuclear chromatin-remodeling assembly with no TM domains) and the virus tail tube (a viral structural protein with a completely different fold). While virion membrane proteins can contain TM domains, they do not exhibit the 7-TM GPCR topology with conserved motifs (e.g., the NPxxY-like motif visible near the C-terminus, the DRY-like motif in the third intracellular loop region). The overall architecture—extracellular N-terminus, seven TM helices, intracellular loops, and phosphorylation-site-rich C-tail—is diagnostic of a cell-surface receptor, not a viral envelope protein.",
    "missing_item_specific_fact": "None required. The 7-TM GPCR architecture is identifiable from the hydrophobicity pattern and topology of the sequence using general structural biology knowledge.",
    "reason": "A model with general knowledge of membrane protein topology can identify the 7-TM GPCR pattern from the sequence's hydrophobic stretches and distinguish it from viral membrane proteins, nuclear complexes, and viral structural proteins. The reasoning chain (multi-pass TM → GPCR topology → plasma membrane) relies on general biological knowledge rather than a protein-specific database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span very different biological categories (viral envelope, cell-surface receptor, nuclear chromatin complex, viral structural protein). The 7-TM GPCR architecture uniquely identifies the plasma membrane option. No other option is defensible given the sequence topology."
  },
  "important_caveats": [
    "The UniProt GO annotation for plasma membrane carries evidence code IEA (inferred from electronic annotation, derived from the 'Cell membrane' subcellular location), while the primary subcellular location annotation itself is backed by experimental evidence (ECO:0000269, PubMed:38649409).",
    "The protein also relocalizes to the vacuole upon ligand stimulation (noted in C5/H3), but the primary/steady-state location is the cell membrane, consistent with the expected answer.",
    "The organism is a fungus (Arthrobotrys oligospora); 'plasma membrane' and 'cell membrane' are EXACT synonyms in GO (GO1), so the terminology is fully interchangeable here.",
    "The reviewer-only evidence confirms the sequence matches UniProt entry G1XJN1 exactly (SHA-256 match), but the evaluated model had no access to this identification."
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

**Accession:** `G1XJN1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 46. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.818783+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Ascaroside receptor GPR3"}}}
```

Source SHA-256: `d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.818783+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38649409","source":"PubMed"}],"value":"Relocalizes to the vacuole following stimulation by ligand"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"38649409","source":"PubMed"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G1XJN1.json)  
**Locator:** `/uniProtKBCrossReferences/11`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.818783+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `d1cb02451e5c1d2640cfcdf6c12c2a6a6f5853805bd439c3031dde0eea563a37`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 43-45`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:38649409};
CC       Multi-pass membrane protein {ECO:0000255}. Note=Relocalizes to the
CC       vacuole following stimulation by ligand. {ECO:0000269|PubMed:38649409}.
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G1XJN1?format=txt&versions=46)  
**Locator:** `lines 69-69`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 46 / 1.  
**Retrieved:** 2026-11-01T06:28:00.513965+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `3c78ac63e30f9e6fea6d4c3a7ddd8ee59ee45f0a9c5a7225b00c7055bec78804`.

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 195. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
