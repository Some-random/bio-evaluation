# GO_cellular_component_0058

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
MCNVSQDSCNIDSRLDSLFPPTLYIFVMVIGFPTNCLSLWAAFVQVRQKNELGVYLLNLSISDLLYIATLPPWVNYFLHQDNWIHGPESCKLFGFILYTNIYISIGFLSCISVDRYLAVAHPLKFAKVRRVKTAAVVSAVVWAIEIGANSAPLFHNELFEDRFNHTFCFEKYPMEDWVAQMNLYRVFVGFLFPWVLMLFCYQGILRAVKTNVSTEREEKAKIKRLALSLIAILLFCFAPYHLILLSRSVVYLGQPCDCTFEENIFTAYHVSLALTSLNCVADPILYCLANEGARSEVTRGLAPLMKFFSASRPNMDSFARSVTLDTPWSSRRAAAPSPRSWSLCGQTGGRGRRSRVRRRRDCKC

[Multiple Choices]
A. fungal-type cell wall
B. plasma membrane
C. nucleolus
D. chromosome
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

> The exact sequence match is annotated as a multipass cell-membrane protein, with a plasma-membrane GO annotation. The location evidence is computational or transferred by similarity rather than direct experimental evidence for this protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has multiple long hydrophobic segments consistent with a multipass membrane protein and a GPCR-like architecture. That strongly favors a membrane location over the fungal cell wall, nucleolus, or chromosome; a cell-surface receptor is plausibly at the plasma membrane.


**Missing item-specific fact**

> No protein-specific annotation is strictly necessary to distinguish these choices, although such annotation supports the plasma-membrane assignment.


**Reason**

> The sequence provides meaningful biological grounds for choosing B over the clearly incompatible cell-wall and nuclear options. The database evidence is corroborative, not the only basis for the choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the plasma membrane is the only one consistent with the sequence's multipass receptor-like architecture.


### Important caveats

- The reviewed subcellular-location annotation is transferred from another UniProt protein, and the multipass topology annotation is computational; neither alone establishes direct experimental localization of this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has multiple long hydrophobic segments consistent with a multipass membrane protein and a GPCR-like architecture. That strongly favors a membrane location over the fungal cell wall, nucleolus, or chromosome; a cell-surface receptor is plausibly at the plasma membrane.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific annotation is strictly necessary to distinguish these choices, although such annotation supports the plasma-membrane assignment.",
    "reason": "The sequence provides meaningful biological grounds for choosing B over the clearly incompatible cell-wall and nuclear options. The database evidence is corroborative, not the only basis for the choice."
  },
  "case_id": "GO_cellular_component_0058",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a multipass cell-membrane protein, with a plasma-membrane GO annotation. The location evidence is computational or transferred by similarity rather than direct experimental evidence for this protein."
  },
  "important_caveats": [
    "The reviewed subcellular-location annotation is transferred from another UniProt protein, and the multipass topology annotation is computational; neither alone establishes direct experimental localization of this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the plasma membrane is the only one consistent with the sequence's multipass receptor-like architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0058",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a multipass cell-membrane protein, with a plasma-membrane GO annotation. The location evidence is computational or transferred by similarity rather than direct experimental evidence for this protein.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has multiple long hydrophobic segments consistent with a multipass membrane protein and a GPCR-like architecture. That strongly favors a membrane location over the fungal cell wall, nucleolus, or chromosome; a cell-surface receptor is plausibly at the plasma membrane.",
    "missing_item_specific_fact": "No protein-specific annotation is strictly necessary to distinguish these choices, although such annotation supports the plasma-membrane assignment.",
    "reason": "The sequence provides meaningful biological grounds for choosing B over the clearly incompatible cell-wall and nuclear options. The database evidence is corroborative, not the only basis for the choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the plasma membrane is the only one consistent with the sequence's multipass receptor-like architecture."
  },
  "important_caveats": [
    "The reviewed subcellular-location annotation is transferred from another UniProt protein, and the multipass topology annotation is computational; neither alone establishes direct experimental localization of this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProtKB entry (A0A4W3GG95, GPR4_CALMI) annotates this protein as a 'Multi-pass membrane protein' located at the 'Cell membrane' (evidence ECO:0000250, inferred by similarity to human GPR4 P46093). The GO cross-reference explicitly assigns GO:0005886 (plasma membrane). The protein is identified as G protein-coupled receptor 4 from Callorhinchus milii, a family universally localized to the plasma membrane. The sequence itself exhibits the classic 7-transmembrane hydrophobic segment architecture of GPCRs, consistent with plasma membrane localization.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO3](#evidence-go3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 364-aa sequence contains approximately seven long hydrophobic stretches (e.g., 'LYIFVMVIGFPTNCLSLWAAFVQVR', 'LLNLSISDLLYIATLPPWVNYFL', 'VAQMNLYRVFVGFLFPWVLMLFCYQ', etc.) separated by shorter hydrophilic loops, which is the hallmark topology of a seven-transmembrane (7TM) receptor. Multi-pass membrane proteins with this architecture are integral plasma membrane proteins. The C-terminal tail ending in 'RRRRRDCKC' with multiple arginines is consistent with a cytoplasmic tail of a membrane receptor. A model can identify the 7TM pattern from hydrophobicity analysis and apply the general biological principle that multi-pass membrane proteins reside in the plasma membrane, without needing to memorize this specific protein's database entry.


**Missing item-specific fact**

> None critical. While exact GPCR family assignment (GPR4) would require database lookup, the multi-pass membrane topology is directly inferable from the sequence's hydrophobic segment pattern.


**Reason**

> The sequence's hydrophobicity pattern clearly reveals a multi-pass membrane protein architecture. General biology dictates that such proteins are plasma membrane residents. The distractors are eliminable by reasoning: fungal-type cell wall (A) is incompatible with a vertebrate protein bearing transmembrane domains; nucleolus (C) and chromosome (D) require soluble nuclear localization signals or DNA-binding domains absent here, and are incompatible with membrane-spanning segments. The reasoning path from sequence features to plasma membrane localization is concrete and does not depend on memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are mutually exclusive and biologically incompatible with the observed 7TM topology. Only plasma membrane (B) accommodates a multi-pass membrane protein. Fungal cell wall, nucleolus, and chromosome are all structurally and functionally inconsistent with a vertebrate multi-pass membrane receptor.


### Important caveats

- The UniProt subcellular location annotation carries evidence code ECO:0000250 (inferred by similarity to P46093, human GPR4), meaning the localization is by homology transfer rather than direct experimental measurement on this specific shark protein.
- The GO annotation uses ISS/IEA evidence types (inferred from sequence/similarity), not direct experimental evidence.
- The sequence is from Callorhinchus milii (ghost shark), a vertebrate; the 'fungal-type cell wall' option is categorically inapplicable to any vertebrate protein, making that distractor trivially eliminable.
- The protein entry was first publicly released in June 2025; the benchmark construction date relative to this release is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 364-aa sequence contains approximately seven long hydrophobic stretches (e.g., 'LYIFVMVIGFPTNCLSLWAAFVQVR', 'LLNLSISDLLYIATLPPWVNYFL', 'VAQMNLYRVFVGFLFPWVLMLFCYQ', etc.) separated by shorter hydrophilic loops, which is the hallmark topology of a seven-transmembrane (7TM) receptor. Multi-pass membrane proteins with this architecture are integral plasma membrane proteins. The C-terminal tail ending in 'RRRRRDCKC' with multiple arginines is consistent with a cytoplasmic tail of a membrane receptor. A model can identify the 7TM pattern from hydrophobicity analysis and apply the general biological principle that multi-pass membrane proteins reside in the plasma membrane, without needing to memorize this specific protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While exact GPCR family assignment (GPR4) would require database lookup, the multi-pass membrane topology is directly inferable from the sequence's hydrophobic segment pattern.",
    "reason": "The sequence's hydrophobicity pattern clearly reveals a multi-pass membrane protein architecture. General biology dictates that such proteins are plasma membrane residents. The distractors are eliminable by reasoning: fungal-type cell wall (A) is incompatible with a vertebrate protein bearing transmembrane domains; nucleolus (C) and chromosome (D) require soluble nuclear localization signals or DNA-binding domains absent here, and are incompatible with membrane-spanning segments. The reasoning path from sequence features to plasma membrane localization is concrete and does not depend on memorizing this specific protein's annotation."
  },
  "case_id": "GO_cellular_component_0058",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "GO3"
    ],
    "judgment": "supported",
    "reason": "The UniProtKB entry (A0A4W3GG95, GPR4_CALMI) annotates this protein as a 'Multi-pass membrane protein' located at the 'Cell membrane' (evidence ECO:0000250, inferred by similarity to human GPR4 P46093). The GO cross-reference explicitly assigns GO:0005886 (plasma membrane). The protein is identified as G protein-coupled receptor 4 from Callorhinchus milii, a family universally localized to the plasma membrane. The sequence itself exhibits the classic 7-transmembrane hydrophobic segment architecture of GPCRs, consistent with plasma membrane localization."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation carries evidence code ECO:0000250 (inferred by similarity to P46093, human GPR4), meaning the localization is by homology transfer rather than direct experimental measurement on this specific shark protein.",
    "The GO annotation uses ISS/IEA evidence types (inferred from sequence/similarity), not direct experimental evidence.",
    "The sequence is from Callorhinchus milii (ghost shark), a vertebrate; the 'fungal-type cell wall' option is categorically inapplicable to any vertebrate protein, making that distractor trivially eliminable.",
    "The protein entry was first publicly released in June 2025; the benchmark construction date relative to this release is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive and biologically incompatible with the observed 7TM topology. Only plasma membrane (B) accommodates a multi-pass membrane protein. Fungal cell wall, nucleolus, and chromosome are all structurally and functionally inconsistent with a vertebrate multi-pass membrane receptor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0058",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProtKB entry (A0A4W3GG95, GPR4_CALMI) annotates this protein as a 'Multi-pass membrane protein' located at the 'Cell membrane' (evidence ECO:0000250, inferred by similarity to human GPR4 P46093). The GO cross-reference explicitly assigns GO:0005886 (plasma membrane). The protein is identified as G protein-coupled receptor 4 from Callorhinchus milii, a family universally localized to the plasma membrane. The sequence itself exhibits the classic 7-transmembrane hydrophobic segment architecture of GPCRs, consistent with plasma membrane localization.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "GO3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 364-aa sequence contains approximately seven long hydrophobic stretches (e.g., 'LYIFVMVIGFPTNCLSLWAAFVQVR', 'LLNLSISDLLYIATLPPWVNYFL', 'VAQMNLYRVFVGFLFPWVLMLFCYQ', etc.) separated by shorter hydrophilic loops, which is the hallmark topology of a seven-transmembrane (7TM) receptor. Multi-pass membrane proteins with this architecture are integral plasma membrane proteins. The C-terminal tail ending in 'RRRRRDCKC' with multiple arginines is consistent with a cytoplasmic tail of a membrane receptor. A model can identify the 7TM pattern from hydrophobicity analysis and apply the general biological principle that multi-pass membrane proteins reside in the plasma membrane, without needing to memorize this specific protein's database entry.",
    "missing_item_specific_fact": "None critical. While exact GPCR family assignment (GPR4) would require database lookup, the multi-pass membrane topology is directly inferable from the sequence's hydrophobic segment pattern.",
    "reason": "The sequence's hydrophobicity pattern clearly reveals a multi-pass membrane protein architecture. General biology dictates that such proteins are plasma membrane residents. The distractors are eliminable by reasoning: fungal-type cell wall (A) is incompatible with a vertebrate protein bearing transmembrane domains; nucleolus (C) and chromosome (D) require soluble nuclear localization signals or DNA-binding domains absent here, and are incompatible with membrane-spanning segments. The reasoning path from sequence features to plasma membrane localization is concrete and does not depend on memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are mutually exclusive and biologically incompatible with the observed 7TM topology. Only plasma membrane (B) accommodates a multi-pass membrane protein. Fungal cell wall, nucleolus, and chromosome are all structurally and functionally inconsistent with a vertebrate multi-pass membrane receptor."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation carries evidence code ECO:0000250 (inferred by similarity to P46093, human GPR4), meaning the localization is by homology transfer rather than direct experimental measurement on this specific shark protein.",
    "The GO annotation uses ISS/IEA evidence types (inferred from sequence/similarity), not direct experimental evidence.",
    "The sequence is from Callorhinchus milii (ghost shark), a vertebrate; the 'fungal-type cell wall' option is categorically inapplicable to any vertebrate protein, making that distractor trivially eliminable.",
    "The protein entry was first publicly released in June 2025; the benchmark construction date relative to this release is unknown."
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

**Accession:** `A0A4W3GG95` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"G protein-coupled receptor 4"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39753131","source":"PubMed"}],"value":"cmGPR4"}]}}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P46093","source":"UniProtKB"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/uniProtKBCrossReferences/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)  
**Locator:** `lines 46-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.027017+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000250|UniProtKB:P46093};
CC       Multi-pass membrane protein {ECO:0000255}.
```

Source SHA-256: `2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)  
**Locator:** `lines 64-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.027017+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865`.

### Evidence GO3

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 58. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
