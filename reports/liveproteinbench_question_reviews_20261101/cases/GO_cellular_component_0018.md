# GO_cellular_component_0018

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — extracellular region

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKPAIFLMLFVAMFLISEGEGFKPKDAPQERSVFSPVVQSCPRCHRRDHFGKCRKLDPCPDK

[Multiple Choices]
A. Dbf4-dependent protein kinase complex
B. RISC-loading complex
C. extracellular region
D. Golgi membrane
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

> The sequence has an N-terminal hydrophobic segment consistent with a secretion signal, followed by a short cysteine-rich peptide. The sequence-matched UniProt record annotates the protein as secreted and gives extracellular region as a GO cellular-component term. These annotations include curator inference and electronic annotation; the cited paper supports toxin identification but the excerpts do not establish direct experimental localization.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic stretch is consistent with a signal peptide, and the remaining short, cysteine-rich sequence is compatible with a secreted peptide toxin. This supports extracellular localization over the intracellular complexes or Golgi membrane listed.


**Missing item-specific fact**

> No additional item-specific fact is required to distinguish the choices by sequence-based biological inference, although the protein’s exact identity and localization annotation require external lookup.


**Reason**

> The signal-peptide pattern gives meaningful grounds for selecting extracellular region. The reviewer-only identity and annotations support the key but are not needed for that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is also annotated to the nematocyst, but that location is not among the choices. Of the listed options, extracellular region best matches the secretion evidence.


### Important caveats

- The sequence-matched UniProt subcellular-location annotation is curator-inferred, and its GO extracellular-region annotation is electronic; the excerpts do not show direct experimental localization.
- The exact author-side database snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a signal peptide, and the remaining short, cysteine-rich sequence is compatible with a secreted peptide toxin. This supports extracellular localization over the intracellular complexes or Golgi membrane listed.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No additional item-specific fact is required to distinguish the choices by sequence-based biological inference, although the protein’s exact identity and localization annotation require external lookup.",
    "reason": "The signal-peptide pattern gives meaningful grounds for selecting extracellular region. The reviewer-only identity and annotations support the key but are not needed for that inference."
  },
  "case_id": "GO_cellular_component_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence has an N-terminal hydrophobic segment consistent with a secretion signal, followed by a short cysteine-rich peptide. The sequence-matched UniProt record annotates the protein as secreted and gives extracellular region as a GO cellular-component term. These annotations include curator inference and electronic annotation; the cited paper supports toxin identification but the excerpts do not establish direct experimental localization."
  },
  "important_caveats": [
    "The sequence-matched UniProt subcellular-location annotation is curator-inferred, and its GO extracellular-region annotation is electronic; the excerpts do not show direct experimental localization.",
    "The exact author-side database snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is also annotated to the nematocyst, but that location is not among the choices. Of the listed options, extracellular region best matches the secretion evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence has an N-terminal hydrophobic segment consistent with a secretion signal, followed by a short cysteine-rich peptide. The sequence-matched UniProt record annotates the protein as secreted and gives extracellular region as a GO cellular-component term. These annotations include curator inference and electronic annotation; the cited paper supports toxin identification but the excerpts do not establish direct experimental localization.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C8", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch is consistent with a signal peptide, and the remaining short, cysteine-rich sequence is compatible with a secreted peptide toxin. This supports extracellular localization over the intracellular complexes or Golgi membrane listed.",
    "missing_item_specific_fact": "No additional item-specific fact is required to distinguish the choices by sequence-based biological inference, although the protein’s exact identity and localization annotation require external lookup.",
    "reason": "The signal-peptide pattern gives meaningful grounds for selecting extracellular region. The reviewer-only identity and annotations support the key but are not needed for that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is also annotated to the nematocyst, but that location is not among the choices. Of the listed options, extracellular region best matches the secretion evidence."
  },
  "important_caveats": [
    "The sequence-matched UniProt subcellular-location annotation is curator-inferred, and its GO extracellular-region annotation is electronic; the excerpts do not show direct experimental localization.",
    "The exact author-side database snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0P0UTJ1 (U-stichotoxin-Hau1a, a sea anemone peptide toxin) annotates the protein as Secreted and Nematocyst (ECO:0000305), with GO:0005576 (extracellular region) assigned via IEA:UniProtKB-SubCell. The protein is a small secreted stichotoxin released from nematocysts into the extracellular environment. The sequence matches the benchmark exactly (62 aa, SHA256 confirmed). The GO annotation is database-derived (IEA) rather than direct experimental localization, but the secreted nature of sea anemone peptide toxins is well-established biologically.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [C4](#evidence-c4), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal ~20 residues (MKPAIFLMLFVAMFLISE) form a classic hydrophobic signal peptide, indicating entry into the secretory pathway. The protein is only 62 aa with five cysteines forming a compact disulfide-bonded toxin fold, inconsistent with a transmembrane Golgi protein (no hydrophobic TM segment after the signal peptide) or with large multi-subunit complexes (Dbf4-dependent kinase, RISC-loading complex). The combination of signal peptide + very small size + cysteine-rich compact structure + absence of any transmembrane helix points to a secreted extracellular peptide toxin rather than a membrane-anchored or nuclear/cytoplasmic complex component.


**Missing item-specific fact**

> None critical. While recognizing the exact sea anemone toxin would confirm the answer, the general sequence features (signal peptide, small size, Cys-rich, no TM domain) provide a defensible biological argument to distinguish C from A, B, and D.


**Reason**

> A model with general knowledge of signal peptides, secreted peptide toxins, and membrane protein topology can reason from the sequence features to exclude nuclear/cytoplasmic complexes (A, B) and Golgi membrane (D, no TM domain, too small for a membrane protein), arriving at extracellular region (C). This does not require memorizing this specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (Dbf4-dependent kinase complex, nuclear) and B (RISC-loading complex, cytoplasmic) are clearly incompatible with a small secreted peptide. Option D (Golgi membrane) is the closest distractor but is excluded by the absence of a transmembrane domain and the very small cysteine-rich peptide architecture. C is the only defensible answer among the four choices.


### Important caveats

- The GO annotation for extracellular region carries IEA (inferred from electronic annotation) evidence, derived from the UniProtKB-SubCell 'Secreted' annotation, not direct experimental measurement of extracellular localization.
- The more precise biological location is the nematocyst (a specialized secretory organelle), but this is not among the answer choices; 'extracellular region' is the best available match for a secreted toxin.
- The signal peptide reasoning is a general heuristic; in principle, a signal peptide could route to the Golgi membrane. However, the 62-aa cysteine-rich architecture without any TM segment makes Golgi membrane highly implausible.
- The UniProt entry was first publicly released in April 2025; the benchmark construction date is unknown, so the author may have sourced this from a different database or annotation pipeline.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal ~20 residues (MKPAIFLMLFVAMFLISE) form a classic hydrophobic signal peptide, indicating entry into the secretory pathway. The protein is only 62 aa with five cysteines forming a compact disulfide-bonded toxin fold, inconsistent with a transmembrane Golgi protein (no hydrophobic TM segment after the signal peptide) or with large multi-subunit complexes (Dbf4-dependent kinase, RISC-loading complex). The combination of signal peptide + very small size + cysteine-rich compact structure + absence of any transmembrane helix points to a secreted extracellular peptide toxin rather than a membrane-anchored or nuclear/cytoplasmic complex component.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. While recognizing the exact sea anemone toxin would confirm the answer, the general sequence features (signal peptide, small size, Cys-rich, no TM domain) provide a defensible biological argument to distinguish C from A, B, and D.",
    "reason": "A model with general knowledge of signal peptides, secreted peptide toxins, and membrane protein topology can reason from the sequence features to exclude nuclear/cytoplasmic complexes (A, B) and Golgi membrane (D, no TM domain, too small for a membrane protein), arriving at extracellular region (C). This does not require memorizing this specific UniProt entry."
  },
  "case_id": "GO_cellular_component_0018",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "C4",
      "C8"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0P0UTJ1 (U-stichotoxin-Hau1a, a sea anemone peptide toxin) annotates the protein as Secreted and Nematocyst (ECO:0000305), with GO:0005576 (extracellular region) assigned via IEA:UniProtKB-SubCell. The protein is a small secreted stichotoxin released from nematocysts into the extracellular environment. The sequence matches the benchmark exactly (62 aa, SHA256 confirmed). The GO annotation is database-derived (IEA) rather than direct experimental localization, but the secreted nature of sea anemone peptide toxins is well-established biologically."
  },
  "important_caveats": [
    "The GO annotation for extracellular region carries IEA (inferred from electronic annotation) evidence, derived from the UniProtKB-SubCell 'Secreted' annotation, not direct experimental measurement of extracellular localization.",
    "The more precise biological location is the nematocyst (a specialized secretory organelle), but this is not among the answer choices; 'extracellular region' is the best available match for a secreted toxin.",
    "The signal peptide reasoning is a general heuristic; in principle, a signal peptide could route to the Golgi membrane. However, the 62-aa cysteine-rich architecture without any TM segment makes Golgi membrane highly implausible.",
    "The UniProt entry was first publicly released in April 2025; the benchmark construction date is unknown, so the author may have sourced this from a different database or annotation pipeline."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (Dbf4-dependent kinase complex, nuclear) and B (RISC-loading complex, cytoplasmic) are clearly incompatible with a small secreted peptide. Option D (Golgi membrane) is the closest distractor but is excluded by the absence of a transmembrane domain and the very small cysteine-rich peptide architecture. C is the only defensible answer among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0018",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0P0UTJ1 (U-stichotoxin-Hau1a, a sea anemone peptide toxin) annotates the protein as Secreted and Nematocyst (ECO:0000305), with GO:0005576 (extracellular region) assigned via IEA:UniProtKB-SubCell. The protein is a small secreted stichotoxin released from nematocysts into the extracellular environment. The sequence matches the benchmark exactly (62 aa, SHA256 confirmed). The GO annotation is database-derived (IEA) rather than direct experimental localization, but the secreted nature of sea anemone peptide toxins is well-established biologically.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "C4", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal ~20 residues (MKPAIFLMLFVAMFLISE) form a classic hydrophobic signal peptide, indicating entry into the secretory pathway. The protein is only 62 aa with five cysteines forming a compact disulfide-bonded toxin fold, inconsistent with a transmembrane Golgi protein (no hydrophobic TM segment after the signal peptide) or with large multi-subunit complexes (Dbf4-dependent kinase, RISC-loading complex). The combination of signal peptide + very small size + cysteine-rich compact structure + absence of any transmembrane helix points to a secreted extracellular peptide toxin rather than a membrane-anchored or nuclear/cytoplasmic complex component.",
    "missing_item_specific_fact": "None critical. While recognizing the exact sea anemone toxin would confirm the answer, the general sequence features (signal peptide, small size, Cys-rich, no TM domain) provide a defensible biological argument to distinguish C from A, B, and D.",
    "reason": "A model with general knowledge of signal peptides, secreted peptide toxins, and membrane protein topology can reason from the sequence features to exclude nuclear/cytoplasmic complexes (A, B) and Golgi membrane (D, no TM domain, too small for a membrane protein), arriving at extracellular region (C). This does not require memorizing this specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (Dbf4-dependent kinase complex, nuclear) and B (RISC-loading complex, cytoplasmic) are clearly incompatible with a small secreted peptide. Option D (Golgi membrane) is the closest distractor but is excluded by the absence of a transmembrane domain and the very small cysteine-rich peptide architecture. C is the only defensible answer among the four choices."
  },
  "important_caveats": [
    "The GO annotation for extracellular region carries IEA (inferred from electronic annotation) evidence, derived from the UniProtKB-SubCell 'Secreted' annotation, not direct experimental measurement of extracellular localization.",
    "The more precise biological location is the nematocyst (a specialized secretory organelle), but this is not among the answer choices; 'extracellular region' is the best available match for a secreted toxin.",
    "The signal peptide reasoning is a general heuristic; in principle, a signal peptide could route to the Golgi membrane. However, the 62-aa cysteine-rich architecture without any TM segment makes Golgi membrane highly implausible.",
    "The UniProt entry was first publicly released in April 2025; the benchmark construction date is unknown, so the author may have sourced this from a different database or annotation pipeline."
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

**Accession:** `A0A0P0UTJ1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 7. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTJ1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:18.532032+00:00.  

```json
"A0A0P0UTJ1"
```

Source SHA-256: `98939d009c5a3f007f7e349cd57e90d5bc7f4c18b1470491c9ff5e2f46908cd9`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTJ1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:18.532032+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39530114","source":"PubMed"}],"value":"Hau I"}}],"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39530114","source":"PubMed"}],"value":"U-stichotoxin-Hau1a"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39530114","source":"PubMed"}],"value":"U-SHTX-Hau1a"}]}}
```

Source SHA-256: `98939d009c5a3f007f7e349cd57e90d5bc7f4c18b1470491c9ff5e2f46908cd9`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTJ1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:18.532032+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000305"}],"id":"SL-0177","value":"Nematocyst"}}]}
```

Source SHA-256: `98939d009c5a3f007f7e349cd57e90d5bc7f4c18b1470491c9ff5e2f46908cd9`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTJ1.json)  
**Locator:** `/uniProtKBCrossReferences/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:18.532032+00:00.  

```json
{"database":"GO","id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `98939d009c5a3f007f7e349cd57e90d5bc7f4c18b1470491c9ff5e2f46908cd9`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0P0UTJ1.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:18.532032+00:00.  

```json
{"citation":{"authors":["Homma T.","Ishida M.","Nagashima Y.","Shiomi K."],"citationCrossReferences":[{"database":"PubMed","id":"39530114"},{"database":"DOI","id":"10.1590/1678-9199-jvatitd-2024-0019"}],"citationType":"journal article","firstPage":"e20240019","id":"39530114","journal":"J. Venom. Anim. Toxins Incl. Trop. Dis.","lastPage":"e20240019","publicationDate":"2024","title":"Isolation and cDNA cloning of four peptide toxins from the sea anemone Heteractis aurora.","volume":"30"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAS68532.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","PROTEIN SEQUENCE OF 32-59","MASS SPECTROMETRY","TOXIC DOSE","HYDROXYLATION AT PRO-36"]}
```

Source SHA-256: `98939d009c5a3f007f7e349cd57e90d5bc7f4c18b1470491c9ff5e2f46908cd9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0P0UTJ1?format=txt&versions=7)  
**Locator:** `lines 27-27`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 7 / 1.  
**Retrieved:** 2026-11-02T04:24:22.267049+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305}. Nematocyst {ECO:0000305}.
```

Source SHA-256: `95447d93c5df6a8d1dcc875dd8c343247cd6400977fa5d975dc64c19d33368f9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0P0UTJ1?format=txt&versions=7)  
**Locator:** `lines 39-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 7 / 1.  
**Retrieved:** 2026-11-02T04:24:22.267049+00:00.  

```text
DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.
```

Source SHA-256: `95447d93c5df6a8d1dcc875dd8c343247cd6400977fa5d975dc64c19d33368f9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 18. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
