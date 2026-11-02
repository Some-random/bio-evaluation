# GO_cellular_component_0060

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **A** — cell surface

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSNRGQLSIEMVILVLAVLVSGSYVALDLSKGAFETTAVNDVQESSYCGFTPDFGATSIDKALVKLTTGIININPNAAVTNNEFNATYTNTTDNTVVTYSLDNVHPNLIKNYADGTIVKVPLNETWKNFTASNIILRMKSDYVCTINGENVSMESNCFEITAPLGSDSFDFQMSAGTGAGQYYLRLVDQEVTIEFSLE

[Multiple Choices]
A. cell surface
B. mitochondrial [2Fe-2S] assembly complex
C. ATP-binding cassette (ABC) transporter complex
D. egg chorion
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

> The exact sequence matches a UniProt record annotated as a probable minor pilin, with cell-surface localization and a cell-surface GO annotation. The localization is supported by transferred or computational annotation, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic leader followed by a largely non-multipass globular region is compatible with an exported pilin rather than an ABC transporter component; the sequence also lacks an obvious ATP-binding domain. This supports a cell-surface-associated protein over the listed complex options.


**Missing item-specific fact**

> A protein-specific identification as a minor pilin would strengthen the inference that it is surface-associated; the sequence alone does not establish direct experimental localization.


**Reason**

> The sequence architecture provides a meaningful biological basis for choosing the surface-associated option among these choices, though it predicts export/pilin-like character more directly than it proves cell-surface attachment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The signal-peptide/pilin-like architecture favors cell-surface association over the listed alternatives. Secreted localization is also annotated, but it is not a separate choice.


### Important caveats

- The current and historical UniProt sequence matches support applicability to this exact sequence.
- The cited localization evidence is transferred by similarity, and the GO cell-surface annotation is computational; the excerpts do not establish experimental validation.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic leader followed by a largely non-multipass globular region is compatible with an exported pilin rather than an ABC transporter component; the sequence also lacks an obvious ATP-binding domain. This supports a cell-surface-associated protein over the listed complex options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "A protein-specific identification as a minor pilin would strengthen the inference that it is surface-associated; the sequence alone does not establish direct experimental localization.",
    "reason": "The sequence architecture provides a meaningful biological basis for choosing the surface-associated option among these choices, though it predicts export/pilin-like character more directly than it proves cell-surface attachment."
  },
  "case_id": "GO_cellular_component_0060",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated as a probable minor pilin, with cell-surface localization and a cell-surface GO annotation. The localization is supported by transferred or computational annotation, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The current and historical UniProt sequence matches support applicability to this exact sequence.",
    "The cited localization evidence is transferred by similarity, and the GO cell-surface annotation is computational; the excerpts do not establish experimental validation.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal-peptide/pilin-like architecture favors cell-surface association over the listed alternatives. Secreted localization is also annotated, but it is not a separate choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0060",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt record annotated as a probable minor pilin, with cell-surface localization and a cell-surface GO annotation. The localization is supported by transferred or computational annotation, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic leader followed by a largely non-multipass globular region is compatible with an exported pilin rather than an ABC transporter component; the sequence also lacks an obvious ATP-binding domain. This supports a cell-surface-associated protein over the listed complex options.",
    "missing_item_specific_fact": "A protein-specific identification as a minor pilin would strengthen the inference that it is surface-associated; the sequence alone does not establish direct experimental localization.",
    "reason": "The sequence architecture provides a meaningful biological basis for choosing the surface-associated option among these choices, though it predicts export/pilin-like character more directly than it proves cell-surface attachment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal-peptide/pilin-like architecture favors cell-surface association over the listed alternatives. Secreted localization is also annotated, but it is not a separate choice."
  },
  "important_caveats": [
    "The current and historical UniProt sequence matches support applicability to this exact sequence.",
    "The cited localization evidence is transferred by similarity, and the GO cell-surface annotation is computational; the excerpts do not establish experimental validation.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q6LZC0 (Probable minor pilin MMP0709 from Methanococcus maripaludis) lists subcellular locations as Secreted, Cell surface, and Fimbrium (evidence ECO:0000250, ISS from Q6LWM4). GO cross-references include GO:0009986 (cell surface), GO:0005576 (extracellular region), and GO:0009289 (pilus). The protein is a pilin, a structural subunit of pili/fimbriae on the cell surface. The annotation evidence is computational (ISS by similarity to Q6LWM4) rather than direct experimental, but it consistently supports 'cell surface' as the primary localization. The N-terminal hydrophobic stretch (VILVLAVLVSGSYVAL, residues ~11-26) is consistent with a signal peptide for secretion to the cell surface.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic stretch (MVILVLAVLVSGSYVAL) is a recognizable signal peptide, indicating the protein is secreted and localized to the cell surface or extracellular space. Option C (ABC transporter complex) is eliminated because the sequence lacks Walker A/B nucleotide-binding motifs and the characteristic ABC signature. Option B (mitochondrial &#91;2Fe-2S&#93; assembly complex) is eliminated because the sequence lacks a mitochondrial targeting sequence (no N-terminal amphipathic cationic helix) and the protein's small size (~198 AA) and pilin-like domain architecture are inconsistent with Fe-S cluster assembly machinery. Option D (egg chorion) is eliminated because egg chorion proteins are large structural glycoproteins of animal eggs, inconsistent with a small secreted protein bearing a pilin-like domain. The combination of signal peptide + small structural domain + absence of transporter/mitochondrial features points to cell surface.


**Missing item-specific fact**

> The specific identification as a 'minor pilin' and the exact GO annotation (cell surface vs. extracellular region vs. pilus) are database annotations. However, among the four provided choices, only 'cell surface' is consistent with a secreted structural protein lacking ABC/mitochondrial/egg-chorion features, so the multiple-choice format is resolvable by elimination.


**Reason**

> A model with general biological knowledge can identify the signal peptide, recognize the absence of ABC transporter motifs, note the lack of mitochondrial targeting signals, and reject egg chorion based on protein size and domain type. The elimination of three distractors through feature-absence reasoning, combined with the positive signal-peptide evidence, provides a concrete biological argument for choosing 'cell surface' without needing to look up the specific UniProt entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, only 'cell surface' is consistent with a small secreted protein bearing a signal peptide and pilin-like domain. The other three options (mitochondrial Fe-S assembly complex, ABC transporter complex, egg chorion) are clearly incompatible with the sequence features. No ambiguity exists among the provided options.


### Important caveats

- The UniProt annotation evidence is ISS (Inferred from Sequence Similarity to Q6LWM4), not direct experimental evidence. The 'Probable' qualifier in the protein name reflects computational prediction.
- The organism (Methanococcus maripaludis, an archaeon) is not stated in the question input. Elimination of mitochondrial and egg chorion options relies on recognizing archaeal/non-animal context or on sequence-feature absence, not on explicit organism metadata.
- The annotation also includes 'extracellular region' and 'pilus' as valid locations, but neither is offered as a distractor, so the single correct option among the four is unambiguous.
- The accession Q6LZC0 and its Swiss-Prot entry were first publicly released in April 2025; the benchmark may have been constructed from a TrEMBL or genomic annotation source predating Swiss-Prot curation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MVILVLAVLVSGSYVAL) is a recognizable signal peptide, indicating the protein is secreted and localized to the cell surface or extracellular space. Option C (ABC transporter complex) is eliminated because the sequence lacks Walker A/B nucleotide-binding motifs and the characteristic ABC signature. Option B (mitochondrial [2Fe-2S] assembly complex) is eliminated because the sequence lacks a mitochondrial targeting sequence (no N-terminal amphipathic cationic helix) and the protein's small size (~198 AA) and pilin-like domain architecture are inconsistent with Fe-S cluster assembly machinery. Option D (egg chorion) is eliminated because egg chorion proteins are large structural glycoproteins of animal eggs, inconsistent with a small secreted protein bearing a pilin-like domain. The combination of signal peptide + small structural domain + absence of transporter/mitochondrial features points to cell surface.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific identification as a 'minor pilin' and the exact GO annotation (cell surface vs. extracellular region vs. pilus) are database annotations. However, among the four provided choices, only 'cell surface' is consistent with a secreted structural protein lacking ABC/mitochondrial/egg-chorion features, so the multiple-choice format is resolvable by elimination.",
    "reason": "A model with general biological knowledge can identify the signal peptide, recognize the absence of ABC transporter motifs, note the lack of mitochondrial targeting signals, and reject egg chorion based on protein size and domain type. The elimination of three distractors through feature-absence reasoning, combined with the positive signal-peptide evidence, provides a concrete biological argument for choosing 'cell surface' without needing to look up the specific UniProt entry."
  },
  "case_id": "GO_cellular_component_0060",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q6LZC0 (Probable minor pilin MMP0709 from Methanococcus maripaludis) lists subcellular locations as Secreted, Cell surface, and Fimbrium (evidence ECO:0000250, ISS from Q6LWM4). GO cross-references include GO:0009986 (cell surface), GO:0005576 (extracellular region), and GO:0009289 (pilus). The protein is a pilin, a structural subunit of pili/fimbriae on the cell surface. The annotation evidence is computational (ISS by similarity to Q6LWM4) rather than direct experimental, but it consistently supports 'cell surface' as the primary localization. The N-terminal hydrophobic stretch (VILVLAVLVSGSYVAL, residues ~11-26) is consistent with a signal peptide for secretion to the cell surface."
  },
  "important_caveats": [
    "The UniProt annotation evidence is ISS (Inferred from Sequence Similarity to Q6LWM4), not direct experimental evidence. The 'Probable' qualifier in the protein name reflects computational prediction.",
    "The organism (Methanococcus maripaludis, an archaeon) is not stated in the question input. Elimination of mitochondrial and egg chorion options relies on recognizing archaeal/non-animal context or on sequence-feature absence, not on explicit organism metadata.",
    "The annotation also includes 'extracellular region' and 'pilus' as valid locations, but neither is offered as a distractor, so the single correct option among the four is unambiguous.",
    "The accession Q6LZC0 and its Swiss-Prot entry were first publicly released in April 2025; the benchmark may have been constructed from a TrEMBL or genomic annotation source predating Swiss-Prot curation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only 'cell surface' is consistent with a small secreted protein bearing a signal peptide and pilin-like domain. The other three options (mitochondrial Fe-S assembly complex, ABC transporter complex, egg chorion) are clearly incompatible with the sequence features. No ambiguity exists among the provided options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0060",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q6LZC0 (Probable minor pilin MMP0709 from Methanococcus maripaludis) lists subcellular locations as Secreted, Cell surface, and Fimbrium (evidence ECO:0000250, ISS from Q6LWM4). GO cross-references include GO:0009986 (cell surface), GO:0005576 (extracellular region), and GO:0009289 (pilus). The protein is a pilin, a structural subunit of pili/fimbriae on the cell surface. The annotation evidence is computational (ISS by similarity to Q6LWM4) rather than direct experimental, but it consistently supports 'cell surface' as the primary localization. The N-terminal hydrophobic stretch (VILVLAVLVSGSYVAL, residues ~11-26) is consistent with a signal peptide for secretion to the cell surface.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch (MVILVLAVLVSGSYVAL) is a recognizable signal peptide, indicating the protein is secreted and localized to the cell surface or extracellular space. Option C (ABC transporter complex) is eliminated because the sequence lacks Walker A/B nucleotide-binding motifs and the characteristic ABC signature. Option B (mitochondrial [2Fe-2S] assembly complex) is eliminated because the sequence lacks a mitochondrial targeting sequence (no N-terminal amphipathic cationic helix) and the protein's small size (~198 AA) and pilin-like domain architecture are inconsistent with Fe-S cluster assembly machinery. Option D (egg chorion) is eliminated because egg chorion proteins are large structural glycoproteins of animal eggs, inconsistent with a small secreted protein bearing a pilin-like domain. The combination of signal peptide + small structural domain + absence of transporter/mitochondrial features points to cell surface.",
    "missing_item_specific_fact": "The specific identification as a 'minor pilin' and the exact GO annotation (cell surface vs. extracellular region vs. pilus) are database annotations. However, among the four provided choices, only 'cell surface' is consistent with a secreted structural protein lacking ABC/mitochondrial/egg-chorion features, so the multiple-choice format is resolvable by elimination.",
    "reason": "A model with general biological knowledge can identify the signal peptide, recognize the absence of ABC transporter motifs, note the lack of mitochondrial targeting signals, and reject egg chorion based on protein size and domain type. The elimination of three distractors through feature-absence reasoning, combined with the positive signal-peptide evidence, provides a concrete biological argument for choosing 'cell surface' without needing to look up the specific UniProt entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, only 'cell surface' is consistent with a small secreted protein bearing a signal peptide and pilin-like domain. The other three options (mitochondrial Fe-S assembly complex, ABC transporter complex, egg chorion) are clearly incompatible with the sequence features. No ambiguity exists among the provided options."
  },
  "important_caveats": [
    "The UniProt annotation evidence is ISS (Inferred from Sequence Similarity to Q6LWM4), not direct experimental evidence. The 'Probable' qualifier in the protein name reflects computational prediction.",
    "The organism (Methanococcus maripaludis, an archaeon) is not stated in the question input. Elimination of mitochondrial and egg chorion options relies on recognizing archaeal/non-animal context or on sequence-feature absence, not on explicit organism metadata.",
    "The annotation also includes 'extracellular region' and 'pilus' as valid locations, but neither is offered as a distractor, so the single correct option among the four is unambiguous.",
    "The accession Q6LZC0 and its Swiss-Prot entry were first publicly released in April 2025; the benchmark may have been constructed from a TrEMBL or genomic annotation source predating Swiss-Prot curation."
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

**Accession:** `Q6LZC0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 75. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZC0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:36.716902+00:00.  

```json
"Q6LZC0"
```

Source SHA-256: `3db999749abf6c20699452461ca055eda952536b51b4b243a842e55072268151`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZC0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:36.716902+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Probable minor pilin MMP0709"}}}
```

Source SHA-256: `3db999749abf6c20699452461ca055eda952536b51b4b243a842e55072268151`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZC0.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:36.716902+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q6LWM4","source":"UniProtKB"}],"id":"SL-0243","value":"Secreted"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q6LWM4","source":"UniProtKB"}],"id":"SL-0310","value":"Cell surface"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q6LWM4","source":"UniProtKB"}],"id":"SL-0113","value":"Fimbrium"}}]}
```

Source SHA-256: `3db999749abf6c20699452461ca055eda952536b51b4b243a842e55072268151`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZC0.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:36.716902+00:00.  

```json
{"database":"GO","id":"GO:0009986","properties":[{"key":"GoTerm","value":"C:cell surface"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `3db999749abf6c20699452461ca055eda952536b51b4b243a842e55072268151`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZC0.json)  
**Locator:** `/uniProtKBCrossReferences/13`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:36.716902+00:00.  

```json
{"database":"GO","id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `3db999749abf6c20699452461ca055eda952536b51b4b243a842e55072268151`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LZC0.json)  
**Locator:** `/uniProtKBCrossReferences/14`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:36.716902+00:00.  

```json
{"database":"GO","id":"GO:0009289","properties":[{"key":"GoTerm","value":"C:pilus"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `3db999749abf6c20699452461ca055eda952536b51b4b243a842e55072268151`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZC0?format=txt&versions=75)  
**Locator:** `lines 35-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:31:40.518419+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000250|UniProtKB:Q6LWM4}. Cell
CC       surface {ECO:0000250|UniProtKB:Q6LWM4}. Fimbrium
CC       {ECO:0000250|UniProtKB:Q6LWM4}.
```

Source SHA-256: `61362a31ad043a1d4de7160cee8e25e0f26f8c0cb1765bb8133df45d8e8d5e54`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZC0?format=txt&versions=75)  
**Locator:** `lines 64-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:31:40.518419+00:00.  

```text
DR   GO; GO:0009986; C:cell surface; IEA:UniProtKB-SubCell.
```

Source SHA-256: `61362a31ad043a1d4de7160cee8e25e0f26f8c0cb1765bb8133df45d8e8d5e54`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LZC0?format=txt&versions=75)  
**Locator:** `lines 65-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 75 / 1.  
**Retrieved:** 2026-11-02T04:31:40.518419+00:00.  

```text
DR   GO; GO:0005576; C:extracellular region; IEA:UniProtKB-SubCell.
```

Source SHA-256: `61362a31ad043a1d4de7160cee8e25e0f26f8c0cb1765bb8133df45d8e8d5e54`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 60. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
