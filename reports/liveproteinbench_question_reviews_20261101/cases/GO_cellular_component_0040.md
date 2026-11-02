# GO_cellular_component_0040

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKNRNPLIRKLLTQYFVTTGILLAFLVMIPLVIRFIAGTRTWYGTEPIYYILRFFADRWLFCVAIGALLIWFGTTIYYMTKAIGYLNETIQATTQLIEEPSKRITLSSHLIDVQEEMNQLREKSLQDQRAAKEAEQRKNDLIVYLAHDLRTPLTSVIGYLTLLKEEPQLSNAMRNRYTEIALQKAQRLELLISEFFEITRFNLTTIVLQTETTDLSLMLEQLTFEFLPLLEEKNLNWQLNLQKNVLATVDTEKIARVFDNLIRNAINYSYPDSPLLLELVESDSIHIRLTNRGKTIPEEMIGRLFEPFYRMDSSRATATSGTGLGLPIAKEILLASGGDISAESKDETIIFNVRLPKPANN

[Multiple Choices]
A. side of membrane
B. Golgi apparatus
C. plasma membrane
D. nuclear periphery
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

> The exact sequence matches the VanSC entry, which describes a multipass membrane protein and records plasma membrane localization. These are annotation-based supports, not direct experimental localization evidence; the plasma membrane GO annotation is computationally assigned.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has strongly hydrophobic N-terminal segments consistent with membrane-spanning helices, followed by a large soluble signaling/kinase region. This supports a membrane sensor protein; in a bacterial context, the cell membrane is the plasma membrane. Golgi apparatus and nuclear periphery are not plausible bacterial compartments, while “side of membrane” is a less direct description than the membrane compartment itself.


**Missing item-specific fact**

> The formal UniProt/GO annotation is not supplied, but it is not required for the broad biological distinction among these choices.


**Reason**

> Sequence architecture and the bacterial-type sensor-kinase organization provide meaningful grounds to favor the plasma membrane, rather than selection requiring recall of this protein’s exact database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> “Side of membrane” is a generic membrane-leaflet component description, whereas plasma membrane names the cellular compartment. The latter is the clearer primary-location choice here.


### Important caveats

- The cited subcellular-location annotation is computational, and the GO plasma-membrane annotation is IEA:TreeGrafter; these should not be represented as experimental confirmation.
- The reviewer-only sequence match and database identity support the key but were not information supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has strongly hydrophobic N-terminal segments consistent with membrane-spanning helices, followed by a large soluble signaling/kinase region. This supports a membrane sensor protein; in a bacterial context, the cell membrane is the plasma membrane. Golgi apparatus and nuclear periphery are not plausible bacterial compartments, while “side of membrane” is a less direct description than the membrane compartment itself.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The formal UniProt/GO annotation is not supplied, but it is not required for the broad biological distinction among these choices.",
    "reason": "Sequence architecture and the bacterial-type sensor-kinase organization provide meaningful grounds to favor the plasma membrane, rather than selection requiring recall of this protein’s exact database entry."
  },
  "case_id": "GO_cellular_component_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the VanSC entry, which describes a multipass membrane protein and records plasma membrane localization. These are annotation-based supports, not direct experimental localization evidence; the plasma membrane GO annotation is computationally assigned."
  },
  "important_caveats": [
    "The cited subcellular-location annotation is computational, and the GO plasma-membrane annotation is IEA:TreeGrafter; these should not be represented as experimental confirmation.",
    "The reviewer-only sequence match and database identity support the key but were not information supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "“Side of membrane” is a generic membrane-leaflet component description, whereas plasma membrane names the cellular compartment. The latter is the clearer primary-location choice here."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the VanSC entry, which describes a multipass membrane protein and records plasma membrane localization. These are annotation-based supports, not direct experimental localization evidence; the plasma membrane GO annotation is computationally assigned.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has strongly hydrophobic N-terminal segments consistent with membrane-spanning helices, followed by a large soluble signaling/kinase region. This supports a membrane sensor protein; in a bacterial context, the cell membrane is the plasma membrane. Golgi apparatus and nuclear periphery are not plausible bacterial compartments, while “side of membrane” is a less direct description than the membrane compartment itself.",
    "missing_item_specific_fact": "The formal UniProt/GO annotation is not supplied, but it is not required for the broad biological distinction among these choices.",
    "reason": "Sequence architecture and the bacterial-type sensor-kinase organization provide meaningful grounds to favor the plasma membrane, rather than selection requiring recall of this protein’s exact database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "“Side of membrane” is a generic membrane-leaflet component description, whereas plasma membrane names the cellular compartment. The latter is the clearer primary-location choice here."
  },
  "important_caveats": [
    "The cited subcellular-location annotation is computational, and the GO plasma-membrane annotation is IEA:TreeGrafter; these should not be represented as experimental confirmation.",
    "The reviewer-only sequence match and database identity support the key but were not information supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein Q9KJT3 (Sensor protein VanSC/VanS) from Enterococcus gallinarum is annotated in UniProt as a multi-pass membrane protein (C5/H3, ECO:0000255 inferred by similarity) and carries the GO:0005886 plasma membrane annotation (C6/H4, IEA:TreeGrafter). As a prokaryotic sensor histidine kinase (EC 2.7.13.3) with multiple predicted transmembrane helices in its N-terminal region, its cellular location is the bacterial plasma membrane (cytoplasmic membrane). The GO term GO:0005886 explicitly includes 'cytoplasmic membrane' and 'cell membrane' as EXACT synonyms and is included in goslim_prokaryote. B (Golgi apparatus) and D (nuclear periphery) are eukaryotic structures absent in bacteria. A (side of membrane) is a very general term describing one leaflet of a bilayer, which is less appropriate for a multi-pass protein that traverses the entire membrane. The expected answer C is consistent with the annotation, though the evidence code is computational (IEA/ECO:0000255) rather than direct experimental localization.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2), [GO4](#evidence-go4), [GO3](#evidence-go3), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple reasoning steps distinguish the answer: (1) The organism is a bacterium (Enterococcus gallinarum), which lacks a Golgi apparatus and a nucleus, immediately eliminating B and D. (2) The N-terminal ~100 residues contain multiple hydrophobic stretches consistent with transmembrane helices, and the C-terminal region contains a histidine kinase domain (HAMP/HisKA architecture), identifying this as a membrane-embedded sensor kinase. (3) For a prokaryote, the only cellular membrane is the plasma membrane (cytoplasmic membrane), making C the specific correct term. (4) The protein is annotated as multi-pass (traverses the bilayer), so 'side of membrane' (A), which describes one leaflet, is less appropriate than 'plasma membrane' (C), which describes the whole membrane structure the protein resides in.


**Missing item-specific fact**

> None critical. General knowledge of prokaryotic cell biology (no Golgi, no nucleus, single plasma membrane), recognition of transmembrane helices in the sequence, and knowledge that two-component sensor histidine kinases are membrane-embedded proteins are sufficient to reach the answer.


**Reason**

> The question provides the sequence and the biological context (a protein to localize). A model with general biological knowledge can: recognize bacterial origin from the sequence context or infer it, eliminate eukaryotic-only compartments (B, D), identify TM domains and a kinase domain indicating a membrane sensor, and conclude that for a bacterium the relevant membrane is the plasma membrane. The distinction between A and C follows from the multi-pass topology (spans the bilayer, not just one side) and the specificity of 'plasma membrane' as the prokaryotic membrane term.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B (Golgi apparatus) and D (nuclear periphery) are definitively excluded for a bacterium. A (side of membrane) is a valid GO term but describes one leaflet of a bilayer; a multi-pass membrane protein spans the entire membrane, making 'plasma membrane' the more accurate and specific annotation. The GO database explicitly assigns GO:0005886 to this protein. No other option is genuinely defensible.


### Important caveats

- The GO:0005886 annotation carries evidence code IEA:TreeGrafter (electronic inference by similarity), not direct experimental evidence. The X-ray structure (PDB 8DX0) only covers residues 208-361 (the kinase domain), not the transmembrane regions.
- The UniProt subcellular location comment uses ECO:0000255 (inferred by similarity), meaning the membrane assignment is based on homology to characterized sensor kinases rather than direct experimental localization of VanS.
- The sequence-to-accession mapping (Q9KJT3) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; however, the reasoning path does not require knowing the accession.
- The GO ontology snapshot used by the benchmark authors is unknown; the current ontology was used for verification.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple reasoning steps distinguish the answer: (1) The organism is a bacterium (Enterococcus gallinarum), which lacks a Golgi apparatus and a nucleus, immediately eliminating B and D. (2) The N-terminal ~100 residues contain multiple hydrophobic stretches consistent with transmembrane helices, and the C-terminal region contains a histidine kinase domain (HAMP/HisKA architecture), identifying this as a membrane-embedded sensor kinase. (3) For a prokaryote, the only cellular membrane is the plasma membrane (cytoplasmic membrane), making C the specific correct term. (4) The protein is annotated as multi-pass (traverses the bilayer), so 'side of membrane' (A), which describes one leaflet, is less appropriate than 'plasma membrane' (C), which describes the whole membrane structure the protein resides in.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. General knowledge of prokaryotic cell biology (no Golgi, no nucleus, single plasma membrane), recognition of transmembrane helices in the sequence, and knowledge that two-component sensor histidine kinases are membrane-embedded proteins are sufficient to reach the answer.",
    "reason": "The question provides the sequence and the biological context (a protein to localize). A model with general biological knowledge can: recognize bacterial origin from the sequence context or infer it, eliminate eukaryotic-only compartments (B, D), identify TM domains and a kinase domain indicating a membrane sensor, and conclude that for a bacterium the relevant membrane is the plasma membrane. The distinction between A and C follows from the multi-pass topology (spans the bilayer, not just one side) and the specificity of 'plasma membrane' as the prokaryotic membrane term."
  },
  "case_id": "GO_cellular_component_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO2",
      "GO4",
      "GO3",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein Q9KJT3 (Sensor protein VanSC/VanS) from Enterococcus gallinarum is annotated in UniProt as a multi-pass membrane protein (C5/H3, ECO:0000255 inferred by similarity) and carries the GO:0005886 plasma membrane annotation (C6/H4, IEA:TreeGrafter). As a prokaryotic sensor histidine kinase (EC 2.7.13.3) with multiple predicted transmembrane helices in its N-terminal region, its cellular location is the bacterial plasma membrane (cytoplasmic membrane). The GO term GO:0005886 explicitly includes 'cytoplasmic membrane' and 'cell membrane' as EXACT synonyms and is included in goslim_prokaryote. B (Golgi apparatus) and D (nuclear periphery) are eukaryotic structures absent in bacteria. A (side of membrane) is a very general term describing one leaflet of a bilayer, which is less appropriate for a multi-pass protein that traverses the entire membrane. The expected answer C is consistent with the annotation, though the evidence code is computational (IEA/ECO:0000255) rather than direct experimental localization."
  },
  "important_caveats": [
    "The GO:0005886 annotation carries evidence code IEA:TreeGrafter (electronic inference by similarity), not direct experimental evidence. The X-ray structure (PDB 8DX0) only covers residues 208-361 (the kinase domain), not the transmembrane regions.",
    "The UniProt subcellular location comment uses ECO:0000255 (inferred by similarity), meaning the membrane assignment is based on homology to characterized sensor kinases rather than direct experimental localization of VanS.",
    "The sequence-to-accession mapping (Q9KJT3) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; however, the reasoning path does not require knowing the accession.",
    "The GO ontology snapshot used by the benchmark authors is unknown; the current ontology was used for verification."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B (Golgi apparatus) and D (nuclear periphery) are definitively excluded for a bacterium. A (side of membrane) is a valid GO term but describes one leaflet of a bilayer; a multi-pass membrane protein spans the entire membrane, making 'plasma membrane' the more accurate and specific annotation. The GO database explicitly assigns GO:0005886 to this protein. No other option is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein Q9KJT3 (Sensor protein VanSC/VanS) from Enterococcus gallinarum is annotated in UniProt as a multi-pass membrane protein (C5/H3, ECO:0000255 inferred by similarity) and carries the GO:0005886 plasma membrane annotation (C6/H4, IEA:TreeGrafter). As a prokaryotic sensor histidine kinase (EC 2.7.13.3) with multiple predicted transmembrane helices in its N-terminal region, its cellular location is the bacterial plasma membrane (cytoplasmic membrane). The GO term GO:0005886 explicitly includes 'cytoplasmic membrane' and 'cell membrane' as EXACT synonyms and is included in goslim_prokaryote. B (Golgi apparatus) and D (nuclear periphery) are eukaryotic structures absent in bacteria. A (side of membrane) is a very general term describing one leaflet of a bilayer, which is less appropriate for a multi-pass protein that traverses the entire membrane. The expected answer C is consistent with the annotation, though the evidence code is computational (IEA/ECO:0000255) rather than direct experimental localization.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO2", "GO4", "GO3", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple reasoning steps distinguish the answer: (1) The organism is a bacterium (Enterococcus gallinarum), which lacks a Golgi apparatus and a nucleus, immediately eliminating B and D. (2) The N-terminal ~100 residues contain multiple hydrophobic stretches consistent with transmembrane helices, and the C-terminal region contains a histidine kinase domain (HAMP/HisKA architecture), identifying this as a membrane-embedded sensor kinase. (3) For a prokaryote, the only cellular membrane is the plasma membrane (cytoplasmic membrane), making C the specific correct term. (4) The protein is annotated as multi-pass (traverses the bilayer), so 'side of membrane' (A), which describes one leaflet, is less appropriate than 'plasma membrane' (C), which describes the whole membrane structure the protein resides in.",
    "missing_item_specific_fact": "None critical. General knowledge of prokaryotic cell biology (no Golgi, no nucleus, single plasma membrane), recognition of transmembrane helices in the sequence, and knowledge that two-component sensor histidine kinases are membrane-embedded proteins are sufficient to reach the answer.",
    "reason": "The question provides the sequence and the biological context (a protein to localize). A model with general biological knowledge can: recognize bacterial origin from the sequence context or infer it, eliminate eukaryotic-only compartments (B, D), identify TM domains and a kinase domain indicating a membrane sensor, and conclude that for a bacterium the relevant membrane is the plasma membrane. The distinction between A and C follows from the multi-pass topology (spans the bilayer, not just one side) and the specificity of 'plasma membrane' as the prokaryotic membrane term."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B (Golgi apparatus) and D (nuclear periphery) are definitively excluded for a bacterium. A (side of membrane) is a valid GO term but describes one leaflet of a bilayer; a multi-pass membrane protein spans the entire membrane, making 'plasma membrane' the more accurate and specific annotation. The GO database explicitly assigns GO:0005886 to this protein. No other option is genuinely defensible."
  },
  "important_caveats": [
    "The GO:0005886 annotation carries evidence code IEA:TreeGrafter (electronic inference by similarity), not direct experimental evidence. The X-ray structure (PDB 8DX0) only covers residues 208-361 (the kinase domain), not the transmembrane regions.",
    "The UniProt subcellular location comment uses ECO:0000255 (inferred by similarity), meaning the membrane assignment is based on homology to characterized sensor kinases rather than direct experimental localization of VanS.",
    "The sequence-to-accession mapping (Q9KJT3) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model; however, the reasoning path does not require knowing the accession.",
    "The GO ontology snapshot used by the benchmark authors is unknown; the current ontology was used for verification."
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

**Accession:** `Q9KJT3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 116. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
"Q9KJT3"
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Vancomycin histidine protein kinase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Vancomycin resistance protein VanSC"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q06240","source":"UniProtKB"}],"value":"2.7.13.3"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Sensor protein VanSC"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"VanS"},{"evidences":[{"evidenceCode":"ECO:0000303","id":"36764524","source":"PubMed"}],"value":"VanSC"}]}}
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-0162","value":"Membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9KJT3.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:57.402699+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `ee33b15ec361df125314162e4a4f908af9fa7205027ed66a72d0e347dc4cb508`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KJT3?format=txt&versions=116)  
**Locator:** `lines 42-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:33:04.938411+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Membrane {ECO:0000255}; Multi-pass membrane
CC       protein {ECO:0000255}.
```

Source SHA-256: `3a9c1fbae546e8df9a94d1ae1786bc246e118381f34915268ec1ab8d8786c6af`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9KJT3?format=txt&versions=116)  
**Locator:** `lines 60-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 116 / 1.  
**Retrieved:** 2026-11-02T04:33:04.938411+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.
```

Source SHA-256: `3a9c1fbae546e8df9a94d1ae1786bc246e118381f34915268ec1ab8d8786c6af`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 59587-59612`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0005794
name: Golgi apparatus
namespace: cellular_component
def: "A membrane-bound cytoplasmic organelle of the endomembrane system that further processes the core oligosaccharides (e.g. N-glycans) added to proteins in the endoplasmic reticulum and packages them into membrane-bound vesicles. The Golgi apparatus operates at the intersection of the secretory, lysosomal, and endocytic pathways." [ISBN:0198506732, PMID:9695800]
comment: Note that the Golgi apparatus can be located in various places in the cytoplasm. In plants and lower animal cells, the Golgi apparatus exists as many copies of discrete stacks dispersed throughout the cytoplasm, while the Golgi apparatus of interphase mammalian cells is a juxtanuclear, often pericentriolar reticulum, where the discrete Golgi stacks are stitched together to form a compact and interconnected ribbon, sometimes called the Golgi ribbon.
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_euk_cellular_processes_ribbon
subset: goslim_generic
subset: goslim_mouse
subset: goslim_pir
subset: goslim_plant
subset: goslim_plant_ribbon
subset: goslim_yeast
synonym: "Golgi" BROAD []
synonym: "Golgi complex" EXACT []
synonym: "Golgi ribbon" NARROW []
xref: NIF_Subcellular:sao451912436
xref: Wikipedia:Golgi_apparatus
is_a: GO:0043231 ! intracellular membrane-bounded organelle
relationship: part_of GO:0005737 ! cytoplasm
relationship: part_of GO:0012505 ! endomembrane system

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

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
**Locator:** `lines 208650-208657`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0034399
name: nuclear periphery
namespace: cellular_component
def: "The portion of the nuclear lumen proximal to the inner nuclear membrane." [GOC:krc, GOC:mah]
is_a: GO:0110165 ! cellular anatomical structure
relationship: part_of GO:0031981 ! nuclear lumen

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 408943-408950`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0098552
name: side of membrane
namespace: cellular_component
def: "A cellular component consisting of one leaflet of a membrane bilayer and any protein embedded or anchored in it or attached to its surface." [GOC:dos]
is_a: GO:0110165 ! cellular anatomical structure
relationship: part_of GO:0016020 ! membrane

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 40. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
