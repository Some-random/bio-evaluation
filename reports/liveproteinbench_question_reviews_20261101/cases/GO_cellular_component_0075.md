# GO_cellular_component_0075

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
MWPPVDVRSLTAESLGRASLILAVDLLLFVTSILNITVIAFTPDLSDVIGCYLISLSVADLLTAIFVIPLSIYSTLEGNWRIGGDNSIICKSAAYLQIALFCSTVYTFAWICIDRYSAMMKPSRYSEQSLTRCKCWIVFSWLTSMLLCCPIIVARMQVVFYPDAQLCVLDWSATSAYSVTLLLLVFVPTLVTVFNTGWKIWSAMRNPAALDDSQRMLVETDPNFVLTGFLFVTFFLSWLPLITLKVCELIWGPFDMDLSMLTFFFVWLAVSGPCCKFLIYMFTNHQFRRSFLSYISCSMCCSSRSRYEYHDIGNNSFL

[Multiple Choices]
A. mitochondrial inner membrane
B. dendrite
C. plasma membrane
D. SAGA-type complex
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

> The sequence matches the cited UniProt record, which annotates the protein to the cell membrane and includes a plasma-membrane GO annotation. These support choice C, though the cited location annotation is computationally inferred rather than direct experimental localization.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has many hydrophobic transmembrane segments and GPCR-like features, including a DRY motif, consistent with a multipass cell-surface receptor. That makes plasma membrane a defensible choice over a dendrite or a nuclear SAGA complex, and favors it over the mitochondrial inner membrane.


**Missing item-specific fact**

> No protein-specific fact is strictly required for a defensible prediction, although knowing this receptor’s annotation or experimentally established localization would strengthen the inference.


**Reason**

> The sequence provides meaningful evidence for a multipass receptor, and the choices make plasma membrane a biologically reasonable inference. This is predictive rather than conclusive: multiple transmembrane segments alone do not establish exact localization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice C is the strongest fit. The sequence does not prove plasma-membrane localization, but the alternatives are substantially less consistent with the receptor-like sequence.


### Important caveats

- The UniProt cell-membrane annotation carries ECO:0000255, and the GO plasma-membrane annotation carries IBA evidence; these should not be described as direct experimental localization.
- The sequence match and database annotations are reviewer-only evidence, not information supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has many hydrophobic transmembrane segments and GPCR-like features, including a DRY motif, consistent with a multipass cell-surface receptor. That makes plasma membrane a defensible choice over a dendrite or a nuclear SAGA complex, and favors it over the mitochondrial inner membrane.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No protein-specific fact is strictly required for a defensible prediction, although knowing this receptor’s annotation or experimentally established localization would strengthen the inference.",
    "reason": "The sequence provides meaningful evidence for a multipass receptor, and the choices make plasma membrane a biologically reasonable inference. This is predictive rather than conclusive: multiple transmembrane segments alone do not establish exact localization."
  },
  "case_id": "GO_cellular_component_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, which annotates the protein to the cell membrane and includes a plasma-membrane GO annotation. These support choice C, though the cited location annotation is computationally inferred rather than direct experimental localization."
  },
  "important_caveats": [
    "The UniProt cell-membrane annotation carries ECO:0000255, and the GO plasma-membrane annotation carries IBA evidence; these should not be described as direct experimental localization.",
    "The sequence match and database annotations are reviewer-only evidence, not information supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is the strongest fit. The sequence does not prove plasma-membrane localization, but the alternatives are substantially less consistent with the receptor-like sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the cited UniProt record, which annotates the protein to the cell membrane and includes a plasma-membrane GO annotation. These support choice C, though the cited location annotation is computationally inferred rather than direct experimental localization.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has many hydrophobic transmembrane segments and GPCR-like features, including a DRY motif, consistent with a multipass cell-surface receptor. That makes plasma membrane a defensible choice over a dendrite or a nuclear SAGA complex, and favors it over the mitochondrial inner membrane.",
    "missing_item_specific_fact": "No protein-specific fact is strictly required for a defensible prediction, although knowing this receptor’s annotation or experimentally established localization would strengthen the inference.",
    "reason": "The sequence provides meaningful evidence for a multipass receptor, and the choices make plasma membrane a biologically reasonable inference. This is predictive rather than conclusive: multiple transmembrane segments alone do not establish exact localization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice C is the strongest fit. The sequence does not prove plasma-membrane localization, but the alternatives are substantially less consistent with the receptor-like sequence."
  },
  "important_caveats": [
    "The UniProt cell-membrane annotation carries ECO:0000255, and the GO plasma-membrane annotation carries IBA evidence; these should not be described as direct experimental localization.",
    "The sequence match and database annotations are reviewer-only evidence, not information supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt O17899 (PCDR1_CAEEL) is annotated as 'Cell membrane' with 'Multi-pass membrane protein' topology (evidence ECO:0000255, computational prediction) and carries GO:0005886 (plasma membrane) via IBA:GO_Central. 'Cell membrane' is an EXACT synonym of 'plasma membrane' per GO ontology. The protein is identified as a G protein-coupled receptor (melatonin receptor pdcr-1), consistent with plasma membrane localization. The annotation is computational rather than experimentally derived, but it is the authoritative database annotation for this sequence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays approximately seven hydrophobic stretches (~20-25 residues each) separated by shorter hydrophilic loops, a topology pattern characteristic of 7-transmembrane G protein-coupled receptors. GPCRs are canonically plasma membrane proteins. Option D (SAGA-type complex) is eliminated because it is a nuclear transcriptional coactivator complex with no relation to multi-pass membrane topology. Option A (mitochondrial inner membrane) is disfavored because the sequence lacks an N-terminal amphipathic mitochondrial targeting presequence and the 7-TM GPCR topology is not typical of mitochondrial inner membrane carriers or respiratory chain subunits. Option B (dendrite) is an anatomical sub-compartment of a neuron; while a GPCR could reside in dendritic plasma membrane, the primary GO cellular component for a multi-pass membrane receptor is 'plasma membrane' (GO:0005886), not the anatomical structure. Thus, general knowledge of membrane protein topology and GO ontology structure allows a model to select C without memorizing this specific UniProt entry.


**Missing item-specific fact**

> None strictly required. The specific identity as 'melatonin receptor pdcr-1' and its C. elegans context confirm the answer, but the reasoning from 7-TM topology → GPCR → plasma membrane is general biology. A model that recognizes the multi-pass membrane pattern and knows GPCRs reside at the plasma membrane can distinguish C from A, B, and D.


**Reason**

> The sequence itself provides sufficient structural information (multi-TM helix pattern consistent with GPCR architecture) to reason toward plasma membrane. The distractors are eliminable through general biological knowledge: SAGA is nuclear, mitochondrial inner membrane proteins have distinct targeting signals and topologies, and 'dendrite' is an anatomical rather than molecular compartment term. No protein-specific experimental measurement is needed beyond standard membrane biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option B (dendrite) might superficially seem plausible for a C. elegans neuronal receptor, but GO cellular component annotation for a GPCR is 'plasma membrane' regardless of which neuronal process it occupies. Option A is weakly plausible for any multi-pass membrane protein, but the absence of a mitochondrial targeting signal and the GPCR-like topology pattern disfavor it. No option is genuinely co-defensible with C given standard biological reasoning.


### Important caveats

- The UniProt subcellular location annotation uses evidence code ECO:0000255 (automatic/computational prediction), not direct experimental localization. The GO annotation uses IBA:GO_Central (inference from phylogenetic propagation), also computational.
- The sequence match to O17899 is exact (SHA-256 verified), confirming the protein identity.
- The 2019 PubMed reference (30692178) describes functional and mutagenesis studies of pdcr-1 but the UniProt subcellular location annotation does not cite this paper; it remains a computational prediction.
- The author's source snapshot date is unknown; however, the sequence has been unchanged since 1998 (sequence version 1), and the Swiss-Prot entry was first publicly released in April 2025, so the annotation existed at the time of benchmark construction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays approximately seven hydrophobic stretches (~20-25 residues each) separated by shorter hydrophilic loops, a topology pattern characteristic of 7-transmembrane G protein-coupled receptors. GPCRs are canonically plasma membrane proteins. Option D (SAGA-type complex) is eliminated because it is a nuclear transcriptional coactivator complex with no relation to multi-pass membrane topology. Option A (mitochondrial inner membrane) is disfavored because the sequence lacks an N-terminal amphipathic mitochondrial targeting presequence and the 7-TM GPCR topology is not typical of mitochondrial inner membrane carriers or respiratory chain subunits. Option B (dendrite) is an anatomical sub-compartment of a neuron; while a GPCR could reside in dendritic plasma membrane, the primary GO cellular component for a multi-pass membrane receptor is 'plasma membrane' (GO:0005886), not the anatomical structure. Thus, general knowledge of membrane protein topology and GO ontology structure allows a model to select C without memorizing this specific UniProt entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The specific identity as 'melatonin receptor pdcr-1' and its C. elegans context confirm the answer, but the reasoning from 7-TM topology → GPCR → plasma membrane is general biology. A model that recognizes the multi-pass membrane pattern and knows GPCRs reside at the plasma membrane can distinguish C from A, B, and D.",
    "reason": "The sequence itself provides sufficient structural information (multi-TM helix pattern consistent with GPCR architecture) to reason toward plasma membrane. The distractors are eliminable through general biological knowledge: SAGA is nuclear, mitochondrial inner membrane proteins have distinct targeting signals and topologies, and 'dendrite' is an anatomical rather than molecular compartment term. No protein-specific experimental measurement is needed beyond standard membrane biology."
  },
  "case_id": "GO_cellular_component_0075",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "UniProt O17899 (PCDR1_CAEEL) is annotated as 'Cell membrane' with 'Multi-pass membrane protein' topology (evidence ECO:0000255, computational prediction) and carries GO:0005886 (plasma membrane) via IBA:GO_Central. 'Cell membrane' is an EXACT synonym of 'plasma membrane' per GO ontology. The protein is identified as a G protein-coupled receptor (melatonin receptor pdcr-1), consistent with plasma membrane localization. The annotation is computational rather than experimentally derived, but it is the authoritative database annotation for this sequence."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation uses evidence code ECO:0000255 (automatic/computational prediction), not direct experimental localization. The GO annotation uses IBA:GO_Central (inference from phylogenetic propagation), also computational.",
    "The sequence match to O17899 is exact (SHA-256 verified), confirming the protein identity.",
    "The 2019 PubMed reference (30692178) describes functional and mutagenesis studies of pdcr-1 but the UniProt subcellular location annotation does not cite this paper; it remains a computational prediction.",
    "The author's source snapshot date is unknown; however, the sequence has been unchanged since 1998 (sequence version 1), and the Swiss-Prot entry was first publicly released in April 2025, so the annotation existed at the time of benchmark construction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B (dendrite) might superficially seem plausible for a C. elegans neuronal receptor, but GO cellular component annotation for a GPCR is 'plasma membrane' regardless of which neuronal process it occupies. Option A is weakly plausible for any multi-pass membrane protein, but the absence of a mitochondrial targeting signal and the GPCR-like topology pattern disfavor it. No option is genuinely co-defensible with C given standard biological reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0075",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt O17899 (PCDR1_CAEEL) is annotated as 'Cell membrane' with 'Multi-pass membrane protein' topology (evidence ECO:0000255, computational prediction) and carries GO:0005886 (plasma membrane) via IBA:GO_Central. 'Cell membrane' is an EXACT synonym of 'plasma membrane' per GO ontology. The protein is identified as a G protein-coupled receptor (melatonin receptor pdcr-1), consistent with plasma membrane localization. The annotation is computational rather than experimentally derived, but it is the authoritative database annotation for this sequence.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays approximately seven hydrophobic stretches (~20-25 residues each) separated by shorter hydrophilic loops, a topology pattern characteristic of 7-transmembrane G protein-coupled receptors. GPCRs are canonically plasma membrane proteins. Option D (SAGA-type complex) is eliminated because it is a nuclear transcriptional coactivator complex with no relation to multi-pass membrane topology. Option A (mitochondrial inner membrane) is disfavored because the sequence lacks an N-terminal amphipathic mitochondrial targeting presequence and the 7-TM GPCR topology is not typical of mitochondrial inner membrane carriers or respiratory chain subunits. Option B (dendrite) is an anatomical sub-compartment of a neuron; while a GPCR could reside in dendritic plasma membrane, the primary GO cellular component for a multi-pass membrane receptor is 'plasma membrane' (GO:0005886), not the anatomical structure. Thus, general knowledge of membrane protein topology and GO ontology structure allows a model to select C without memorizing this specific UniProt entry.",
    "missing_item_specific_fact": "None strictly required. The specific identity as 'melatonin receptor pdcr-1' and its C. elegans context confirm the answer, but the reasoning from 7-TM topology → GPCR → plasma membrane is general biology. A model that recognizes the multi-pass membrane pattern and knows GPCRs reside at the plasma membrane can distinguish C from A, B, and D.",
    "reason": "The sequence itself provides sufficient structural information (multi-TM helix pattern consistent with GPCR architecture) to reason toward plasma membrane. The distractors are eliminable through general biological knowledge: SAGA is nuclear, mitochondrial inner membrane proteins have distinct targeting signals and topologies, and 'dendrite' is an anatomical rather than molecular compartment term. No protein-specific experimental measurement is needed beyond standard membrane biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option B (dendrite) might superficially seem plausible for a C. elegans neuronal receptor, but GO cellular component annotation for a GPCR is 'plasma membrane' regardless of which neuronal process it occupies. Option A is weakly plausible for any multi-pass membrane protein, but the absence of a mitochondrial targeting signal and the GPCR-like topology pattern disfavor it. No option is genuinely co-defensible with C given standard biological reasoning."
  },
  "important_caveats": [
    "The UniProt subcellular location annotation uses evidence code ECO:0000255 (automatic/computational prediction), not direct experimental localization. The GO annotation uses IBA:GO_Central (inference from phylogenetic propagation), also computational.",
    "The sequence match to O17899 is exact (SHA-256 verified), confirming the protein identity.",
    "The 2019 PubMed reference (30692178) describes functional and mutagenesis studies of pdcr-1 but the UniProt subcellular location annotation does not cite this paper; it remains a computational prediction.",
    "The author's source snapshot date is unknown; however, the sequence has been unchanged since 1998 (sequence version 1), and the Swiss-Prot entry was first publicly released in April 2025, so the annotation existed at the time of benchmark construction."
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

**Accession:** `O17899` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 149. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O17899.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:08.695552+00:00.  

```json
"O17899"
```

Source SHA-256: `57408f874822ee8530f21bd6b9e1d0f0116745485f2ba3536498ad086498d0f6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O17899.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:08.695552+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `57408f874822ee8530f21bd6b9e1d0f0116745485f2ba3536498ad086498d0f6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O17899.json)  
**Locator:** `/uniProtKBCrossReferences/24`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:08.695552+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `57408f874822ee8530f21bd6b9e1d0f0116745485f2ba3536498ad086498d0f6`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O17899?format=txt&versions=149)  
**Locator:** `lines 47-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 149 / 1.  
**Retrieved:** 2026-11-02T04:29:13.646977+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000255}; Multi-pass membrane
CC       protein {ECO:0000255}.
```

Source SHA-256: `d19df2056192527093f5764fb03d847f2eb72aec7681a596ae2cab0c45472c70`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O17899?format=txt&versions=149)  
**Locator:** `lines 86-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 149 / 1.  
**Retrieved:** 2026-11-02T04:29:13.646977+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IBA:GO_Central.
```

Source SHA-256: `d19df2056192527093f5764fb03d847f2eb72aec7681a596ae2cab0c45472c70`.

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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 75. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
