# GO_cellular_component_0115

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — extracellular region

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAKFSKGQISIELILLMTAVLLAGILVSVNMTRFTFEGDILSDVREDAFQVFEISTDTPIIVYSLNFSNVKISPSTNLYNAWLQINDTGNDTYLWYYSDGTFKGLANTSDPDESITEENLVLLPHEGYASDIIFRSNVPTAMSWDSYEIDFNDIKKFEIIANDVENNPISYSLTHGDSPETSNQAYLNIKANEVTIIVTKANDKVFEVIANTTSGTIELLPYTETSP

[Multiple Choices]
A. checkpoint clamp complex
B. extracellular region
C. cell tip
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

> The exact sequence match is annotated as a probable minor pilin, with secreted, cell-surface, and fimbrium locations; the matching record also carries an extracellular-region GO annotation. The localization evidence is transferred or computational rather than direct experimental evidence, but it supports choice B.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence begins with a strongly hydrophobic N-terminal segment consistent with an export signal. That favors a secreted or externally exposed protein over the nuclear options, and is consistent with the extracellular-region choice.


**Missing item-specific fact**

> The precise identity as a probable minor pilin and the transferred localization annotation are not supplied; they would corroborate the inference, but the N-terminal export-signal pattern provides meaningful grounds for choosing among these options.


**Reason**

> The sequence supports broad export from the cell, which distinguishes the extracellular choice from the intracellular nuclear choices without needing to recognize the exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The record also indicates cell-surface and fimbrium localization, but neither is offered as a choice. Among the listed options, extracellular region is the supported selection.


### Important caveats

- The localization annotations are inferred or transferred from a related entry, not established here by direct experimental evidence.
- The GO extracellular-region term has a cell-surface distinction; the record separately annotates cell surface and fimbrium, so the precise localization wording merits care.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence begins with a strongly hydrophobic N-terminal segment consistent with an export signal. That favors a secreted or externally exposed protein over the nuclear options, and is consistent with the extracellular-region choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The precise identity as a probable minor pilin and the transferred localization annotation are not supplied; they would corroborate the inference, but the N-terminal export-signal pattern provides meaningful grounds for choosing among these options.",
    "reason": "The sequence supports broad export from the cell, which distinguishes the extracellular choice from the intracellular nuclear choices without needing to recognize the exact protein."
  },
  "case_id": "GO_cellular_component_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a probable minor pilin, with secreted, cell-surface, and fimbrium locations; the matching record also carries an extracellular-region GO annotation. The localization evidence is transferred or computational rather than direct experimental evidence, but it supports choice B."
  },
  "important_caveats": [
    "The localization annotations are inferred or transferred from a related entry, not established here by direct experimental evidence.",
    "The GO extracellular-region term has a cell-surface distinction; the record separately annotates cell surface and fimbrium, so the precise localization wording merits care."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The record also indicates cell-surface and fimbrium localization, but neither is offered as a choice. Among the listed options, extracellular region is the supported selection."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a probable minor pilin, with secreted, cell-surface, and fimbrium locations; the matching record also carries an extracellular-region GO annotation. The localization evidence is transferred or computational rather than direct experimental evidence, but it supports choice B.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence begins with a strongly hydrophobic N-terminal segment consistent with an export signal. That favors a secreted or externally exposed protein over the nuclear options, and is consistent with the extracellular-region choice.",
    "missing_item_specific_fact": "The precise identity as a probable minor pilin and the transferred localization annotation are not supplied; they would corroborate the inference, but the N-terminal export-signal pattern provides meaningful grounds for choosing among these options.",
    "reason": "The sequence supports broad export from the cell, which distinguishes the extracellular choice from the intracellular nuclear choices without needing to recognize the exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The record also indicates cell-surface and fimbrium localization, but neither is offered as a choice. Among the listed options, extracellular region is the supported selection."
  },
  "important_caveats": [
    "The localization annotations are inferred or transferred from a related entry, not established here by direct experimental evidence.",
    "The GO extracellular-region term has a cell-surface distinction; the record separately annotates cell surface and fimbrium, so the precise localization wording merits care."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q6LZM4 (Probable minor pilin MMP0600, Methanococcus maripaludis) is annotated with GO:0005576 (extracellular region) via ISS:UniProtKB, and its subcellular location is listed as Secreted, Cell surface, and Fimbrium. The annotation evidence code is ECO:0000250 (inferred from sequence similarity to Q6LWM4), making it a computational transfer rather than direct experimental proof, but it is a legitimate UniProt annotation. Among the four choices, 'extracellular region' is the most appropriate for a secreted pilin/fimbrial protein. Note that the GO definition for extracellular region states it is intended for products 'not attached to the cell surface,' creating minor tension with the pilus/cell-surface annotations, but among the given options B remains the best-supported choice.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region (residues ~8–25: ELILLMTAVLLAGILVSVN) is a hydrophobic stretch consistent with a prokaryotic-type signal peptide, indicating entry into the secretion pathway and thus an extracellular destination. Two options can be eliminated by general biology: (A) checkpoint clamp complex is a eukaryotic DNA-repair structure (Rad9/Rad1/Hus1 heterotrimer) with no archaeal or prokaryotic counterpart; (D) nucleoplasm requires a membrane-bound nucleus, which archaea lack. Between B (extracellular region) and C (cell tip), the presence of a signal peptide supports general secretion/extracellular localization without requiring the additional, specific evidence needed to assign a protein to the narrow 'cell tip' sub-compartment (defined as the end of the longest axis of an elongated cell). A coccus-shaped archaeon like Methanococcus further weakens 'cell tip,' though morphology is not stated in the prompt.


**Missing item-specific fact**

> Precise knowledge that this protein is a minor pilin (and thus a pilus/fimbrium component) would confirm the extracellular assignment definitively, but the signal-peptide-based secretion reasoning provides a defensible general argument for choosing B over C without that specific annotation.


**Reason**

> The sequence contains an identifiable N-terminal signal peptide, and the elimination of eukaryotic-specific terms (checkpoint clamp, nucleoplasm) follows from general cell biology. The B-vs-C distinction is supported by the parsimony of assigning a secreted protein to the general 'extracellular region' rather than the highly specific 'cell tip' sub-compartment absent additional morphological or functional context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both 'extracellular region' and 'cell tip' describe locations external to the cell membrane. Without explicit organism morphology (Methanococcus is a coccus, making 'cell tip' inapplicable) or knowledge that the protein is a pilin, a model could argue for C based on the signal peptide alone. However, 'cell tip' is a very specific sub-compartment requiring additional evidence (elongated cell shape, polar targeting), making B the more parsimonious and defensible choice from the sequence data alone. The GO definition note that extracellular region is for products 'not attached to the cell surface' introduces minor tension with the pilin annotation, but among the four options B remains the best fit.


### Important caveats

- The UniProt annotation evidence is ECO:0000250 (ISS – Inferred from Sequence or Structural Similarity to Q6LWM4), not direct experimental localization. The 'probable' qualifier in the protein name reflects this computational basis.
- The GO term definition for extracellular region (GO:0005576) explicitly notes it is for products 'not attached to the cell surface,' which is in slight tension with the pilus/fimbrium/cell-surface annotations for this pilin. Among the given choices, B is still the closest match.
- The organism identity (Methanococcus maripaludis, an archaeal coccus) is not provided in the question input; elimination of nucleoplasm and checkpoint clamp relies on the model inferring prokaryotic/archaeal context from sequence features.
- The accession Q6LZM4 was inferred by the reviewer from dataset metadata and was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region (residues ~8–25: ELILLMTAVLLAGILVSVN) is a hydrophobic stretch consistent with a prokaryotic-type signal peptide, indicating entry into the secretion pathway and thus an extracellular destination. Two options can be eliminated by general biology: (A) checkpoint clamp complex is a eukaryotic DNA-repair structure (Rad9/Rad1/Hus1 heterotrimer) with no archaeal or prokaryotic counterpart; (D) nucleoplasm requires a membrane-bound nucleus, which archaea lack. Between B (extracellular region) and C (cell tip), the presence of a signal peptide supports general secretion/extracellular localization without requiring the additional, specific evidence needed to assign a protein to the narrow 'cell tip' sub-compartment (defined as the end of the longest axis of an elongated cell). A coccus-shaped archaeon like Methanococcus further weakens 'cell tip,' though morphology is not stated in the prompt.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise knowledge that this protein is a minor pilin (and thus a pilus/fimbrium component) would confirm the extracellular assignment definitively, but the signal-peptide-based secretion reasoning provides a defensible general argument for choosing B over C without that specific annotation.",
    "reason": "The sequence contains an identifiable N-terminal signal peptide, and the elimination of eukaryotic-specific terms (checkpoint clamp, nucleoplasm) follows from general cell biology. The B-vs-C distinction is supported by the parsimony of assigning a secreted protein to the general 'extracellular region' rather than the highly specific 'cell tip' sub-compartment absent additional morphological or functional context."
  },
  "case_id": "GO_cellular_component_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "UniProt Q6LZM4 (Probable minor pilin MMP0600, Methanococcus maripaludis) is annotated with GO:0005576 (extracellular region) via ISS:UniProtKB, and its subcellular location is listed as Secreted, Cell surface, and Fimbrium. The annotation evidence code is ECO:0000250 (inferred from sequence similarity to Q6LWM4), making it a computational transfer rather than direct experimental proof, but it is a legitimate UniProt annotation. Among the four choices, 'extracellular region' is the most appropriate for a secreted pilin/fimbrial protein. Note that the GO definition for extracellular region states it is intended for products 'not attached to the cell surface,' creating minor tension with the pilus/cell-surface annotations, but among the given options B remains the best-supported choice."
  },
  "important_caveats": [
    "The UniProt annotation evidence is ECO:0000250 (ISS – Inferred from Sequence or Structural Similarity to Q6LWM4), not direct experimental localization. The 'probable' qualifier in the protein name reflects this computational basis.",
    "The GO term definition for extracellular region (GO:0005576) explicitly notes it is for products 'not attached to the cell surface,' which is in slight tension with the pilus/fimbrium/cell-surface annotations for this pilin. Among the given choices, B is still the closest match.",
    "The organism identity (Methanococcus maripaludis, an archaeal coccus) is not provided in the question input; elimination of nucleoplasm and checkpoint clamp relies on the model inferring prokaryotic/archaeal context from sequence features.",
    "The accession Q6LZM4 was inferred by the reviewer from dataset metadata and was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both 'extracellular region' and 'cell tip' describe locations external to the cell membrane. Without explicit organism morphology (Methanococcus is a coccus, making 'cell tip' inapplicable) or knowledge that the protein is a pilin, a model could argue for C based on the signal peptide alone. However, 'cell tip' is a very specific sub-compartment requiring additional evidence (elongated cell shape, polar targeting), making B the more parsimonious and defensible choice from the sequence data alone. The GO definition note that extracellular region is for products 'not attached to the cell surface' introduces minor tension with the pilin annotation, but among the four options B remains the best fit."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q6LZM4 (Probable minor pilin MMP0600, Methanococcus maripaludis) is annotated with GO:0005576 (extracellular region) via ISS:UniProtKB, and its subcellular location is listed as Secreted, Cell surface, and Fimbrium. The annotation evidence code is ECO:0000250 (inferred from sequence similarity to Q6LWM4), making it a computational transfer rather than direct experimental proof, but it is a legitimate UniProt annotation. Among the four choices, 'extracellular region' is the most appropriate for a secreted pilin/fimbrial protein. Note that the GO definition for extracellular region states it is intended for products 'not attached to the cell surface,' creating minor tension with the pilus/cell-surface annotations, but among the given options B remains the best-supported choice.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region (residues ~8–25: ELILLMTAVLLAGILVSVN) is a hydrophobic stretch consistent with a prokaryotic-type signal peptide, indicating entry into the secretion pathway and thus an extracellular destination. Two options can be eliminated by general biology: (A) checkpoint clamp complex is a eukaryotic DNA-repair structure (Rad9/Rad1/Hus1 heterotrimer) with no archaeal or prokaryotic counterpart; (D) nucleoplasm requires a membrane-bound nucleus, which archaea lack. Between B (extracellular region) and C (cell tip), the presence of a signal peptide supports general secretion/extracellular localization without requiring the additional, specific evidence needed to assign a protein to the narrow 'cell tip' sub-compartment (defined as the end of the longest axis of an elongated cell). A coccus-shaped archaeon like Methanococcus further weakens 'cell tip,' though morphology is not stated in the prompt.",
    "missing_item_specific_fact": "Precise knowledge that this protein is a minor pilin (and thus a pilus/fimbrium component) would confirm the extracellular assignment definitively, but the signal-peptide-based secretion reasoning provides a defensible general argument for choosing B over C without that specific annotation.",
    "reason": "The sequence contains an identifiable N-terminal signal peptide, and the elimination of eukaryotic-specific terms (checkpoint clamp, nucleoplasm) follows from general cell biology. The B-vs-C distinction is supported by the parsimony of assigning a secreted protein to the general 'extracellular region' rather than the highly specific 'cell tip' sub-compartment absent additional morphological or functional context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both 'extracellular region' and 'cell tip' describe locations external to the cell membrane. Without explicit organism morphology (Methanococcus is a coccus, making 'cell tip' inapplicable) or knowledge that the protein is a pilin, a model could argue for C based on the signal peptide alone. However, 'cell tip' is a very specific sub-compartment requiring additional evidence (elongated cell shape, polar targeting), making B the more parsimonious and defensible choice from the sequence data alone. The GO definition note that extracellular region is for products 'not attached to the cell surface' introduces minor tension with the pilin annotation, but among the four options B remains the best fit."
  },
  "important_caveats": [
    "The UniProt annotation evidence is ECO:0000250 (ISS – Inferred from Sequence or Structural Similarity to Q6LWM4), not direct experimental localization. The 'probable' qualifier in the protein name reflects this computational basis.",
    "The GO term definition for extracellular region (GO:0005576) explicitly notes it is for products 'not attached to the cell surface,' which is in slight tension with the pilus/fimbrium/cell-surface annotations for this pilin. Among the given choices, B is still the closest match.",
    "The organism identity (Methanococcus maripaludis, an archaeal coccus) is not provided in the question input; elimination of nucleoplasm and checkpoint clamp relies on the model inferring prokaryotic/archaeal context from sequence features.",
    "The accession Q6LZM4 was inferred by the reviewer from dataset metadata and was not available to the evaluated model."
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

**Accession:** `Q6LZM4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 80. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:38.398302+00:00.  

```json
"Q6LZM4"
```

Source SHA-256: `f4e15b88d1de834c8968199fb487de5cb1d3b2653afd5624458251196680c21c`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:38.398302+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Probable minor pilin MMP0600"}}}
```

Source SHA-256: `f4e15b88d1de834c8968199fb487de5cb1d3b2653afd5624458251196680c21c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:38.398302+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q6LWM4","source":"UniProtKB"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q6LWM4","source":"UniProtKB"}],"id":"SL-0310","value":"Cell surface"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q6LWM4","source":"UniProtKB"}],"id":"SL-0113","value":"Fimbrium"}}]}
```

Source SHA-256: `f4e15b88d1de834c8968199fb487de5cb1d3b2653afd5624458251196680c21c`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZM4.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:38.398302+00:00.  

```json
{"database":"GO","id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `f4e15b88d1de834c8968199fb487de5cb1d3b2653afd5624458251196680c21c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZM4?format=txt&versions=80)  
**Locator:** `lines 35-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-02T04:31:41.131095+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000250|UniProtKB:Q6LWM4}. Cell
CC       surface {ECO:0000250|UniProtKB:Q6LWM4}. Fimbrium
CC       {ECO:0000250|UniProtKB:Q6LWM4}.
```

Source SHA-256: `0b89110e2133845208853fddfaa063e9db830b5242d99c856679094f308f579d`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZM4?format=txt&versions=80)  
**Locator:** `lines 65-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 80 / 1.  
**Retrieved:** 2026-11-02T04:31:41.131095+00:00.  

```text
DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.
```

Source SHA-256: `0b89110e2133845208853fddfaa063e9db830b5242d99c856679094f308f579d`.

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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 115. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
