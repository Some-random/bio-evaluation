# GO_cellular_component_0188

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — microvillus membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAQWWLILLGLWTVLPSLAGGKLLNVCMNSKHHKQEPGPEDKLYFECMPWKDNACCTRDTSWEAHLDEPLLFNFSMTHCGLLTPLCHKHFIQAICFYECSPNLGPWIQPVVPNRQEEQRLWDVPLCLEDCEEWWKDCRTSHTCKADWLHGWVWDQGKNGCPAHAPCLPFSDYFPTPADLCEKIWNNTFKASPERRNSGRCLQKWFEPTHGNPNVEVALHFAGSASAPQLSYSITAFSLCLLLHA

[Multiple Choices]
A. kinetoplast
B. microvillus membrane
C. vitelline envelope
D. SAGA complex
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

> The exact sequence matches rat JUNO. Its UniProt record assigns microvillus membrane, and describes it as GPI-anchored at oolemma microvilli. The specific microvillus annotation is transferred by similarity, while experimental evidence supports plasma-membrane localization; this supports B at the annotation level, not as a direct experiment specifically establishing microvillus localization in rat.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic stretch and C-terminal hydrophobic region are consistent with a secreted, membrane-associated protein, which can make a membrane location more plausible than a kinetoplast or SAGA complex. They do not distinguish microvillus membrane from other membrane or egg-associated locations.


**Missing item-specific fact**

> Identifying the protein as JUNO and knowing its oocyte-surface localization at microvilli requires protein-specific annotation or biological knowledge absent from the sequence and prompt.


**Reason**

> The sequence offers broad clues about membrane association, but selecting the precise microvillus membrane option depends on a protein-specific localization fact, not a general inference from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence alone does not resolve the precise location, but the matching annotation supports B; the other choices are distinct compartments or complexes.


### Important caveats

- The microvillus localization annotation is based on transferred evidence (ECO:0000250), whereas the cited experimental evidence supports plasma-membrane localization.
- The exact author data snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch and C-terminal hydrophobic region are consistent with a secreted, membrane-associated protein, which can make a membrane location more plausible than a kinetoplast or SAGA complex. They do not distinguish microvillus membrane from other membrane or egg-associated locations.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying the protein as JUNO and knowing its oocyte-surface localization at microvilli requires protein-specific annotation or biological knowledge absent from the sequence and prompt.",
    "reason": "The sequence offers broad clues about membrane association, but selecting the precise microvillus membrane option depends on a protein-specific localization fact, not a general inference from the supplied input."
  },
  "case_id": "GO_cellular_component_0188",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches rat JUNO. Its UniProt record assigns microvillus membrane, and describes it as GPI-anchored at oolemma microvilli. The specific microvillus annotation is transferred by similarity, while experimental evidence supports plasma-membrane localization; this supports B at the annotation level, not as a direct experiment specifically establishing microvillus localization in rat."
  },
  "important_caveats": [
    "The microvillus localization annotation is based on transferred evidence (ECO:0000250), whereas the cited experimental evidence supports plasma-membrane localization.",
    "The exact author data snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone does not resolve the precise location, but the matching annotation supports B; the other choices are distinct compartments or complexes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0188",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches rat JUNO. Its UniProt record assigns microvillus membrane, and describes it as GPI-anchored at oolemma microvilli. The specific microvillus annotation is transferred by similarity, while experimental evidence supports plasma-membrane localization; this supports B at the annotation level, not as a direct experiment specifically establishing microvillus localization in rat.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic stretch and C-terminal hydrophobic region are consistent with a secreted, membrane-associated protein, which can make a membrane location more plausible than a kinetoplast or SAGA complex. They do not distinguish microvillus membrane from other membrane or egg-associated locations.",
    "missing_item_specific_fact": "Identifying the protein as JUNO and knowing its oocyte-surface localization at microvilli requires protein-specific annotation or biological knowledge absent from the sequence and prompt.",
    "reason": "The sequence offers broad clues about membrane association, but selecting the precise microvillus membrane option depends on a protein-specific localization fact, not a general inference from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone does not resolve the precise location, but the matching annotation supports B; the other choices are distinct compartments or complexes."
  },
  "important_caveats": [
    "The microvillus localization annotation is based on transferred evidence (ECO:0000250), whereas the cited experimental evidence supports plasma-membrane localization.",
    "The exact author data snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt F1M928 (JUNO_RAT) explicitly annotates 'Cell projection, microvillus membrane' in its SUBCELLULAR LOCATION comment (C5, H3), with the note 'GPI-anchored at the oolemma microvilli.' GO term GO:0031528 (microvillus membrane) is cross-referenced (C6, H5). The evidence code for this annotation is IEA (transferred from UniProtKB:A6ND01/Q9EQF4), while plasma membrane carries IDA evidence. However, the microvillus membrane annotation is present and not contradicted. The expected answer aligns with the annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits (1) an N-terminal signal peptide (MAQWWLILLGLWTVLPSLAGG) indicating entry into the secretory pathway, which eliminates the nuclear SAGA complex (D); (2) a C-terminal hydrophobic region (FSLCLLLHA) consistent with a GPI anchor, indicating membrane anchoring rather than free secretion, which eliminates the extracellular vitelline envelope (C); (3) a cysteine-rich, ~244-aa folate-receptor-like fold with no mitochondrial targeting presequence, eliminating the kinetoplast (A), a mitochondrial DNA substructure specific to kinetoplastid parasites. Among the remaining options, microvillus membrane (B) is the only GPI-anchored membrane localization, making it the sole viable answer.


**Missing item-specific fact**

> The specific identification of this protein as JUNO/folate receptor 4 and its documented localization to oolemma microvilli (rather than general plasma membrane) is protein-specific knowledge. However, since 'plasma membrane' is not among the choices, the reasoning from signal peptide + GPI anchor + non-mitochondrial/non-nuclear character sufficiently distinguishes B from A, C, and D without requiring the exact protein identity.


**Reason**

> A model can reason from visible sequence features (signal peptide, GPI-anchor-like C-terminus, absence of mitochondrial targeting sequence, absence of nuclear localization signal) to eliminate three of four options. The specific 'microvillus' sub-localization within the membrane is protein-specific, but among the four given choices, only B is a membrane compartment compatible with a GPI-anchored secretory-pathway protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span fundamentally different compartments (parasite mitochondrial substructure, extracellular glycoprotein layer, nuclear chromatin complex, plasma-membrane microdomain). The sequence features cleanly eliminate A, C, and D. No two options are equally defensible given the GPI-anchor and signal-peptide evidence.


### Important caveats

- The microvillus membrane annotation carries IEA evidence (transferred from mouse JUNO Q9EQF4 and another protein A6ND01), not direct experimental evidence for this rat sequence. The IDA-evidenced location is plasma membrane (GO:0005886), which is not offered as a choice.
- The GPI anchor is inferred by similarity (ECO:0000250) rather than experimentally confirmed for this specific rat JUNO sequence.
- The reviewer-only evidence was absent from the evaluated model input; the model must rely solely on sequence features and general biological knowledge.
- The C-terminal hydrophobic stretch (FSLCLLLHA, 9 residues) is short for a canonical GPI-anchor signal; a model might not confidently identify a GPI anchor without recognizing the folate-receptor family context.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits (1) an N-terminal signal peptide (MAQWWLILLGLWTVLPSLAGG) indicating entry into the secretory pathway, which eliminates the nuclear SAGA complex (D); (2) a C-terminal hydrophobic region (FSLCLLLHA) consistent with a GPI anchor, indicating membrane anchoring rather than free secretion, which eliminates the extracellular vitelline envelope (C); (3) a cysteine-rich, ~244-aa folate-receptor-like fold with no mitochondrial targeting presequence, eliminating the kinetoplast (A), a mitochondrial DNA substructure specific to kinetoplastid parasites. Among the remaining options, microvillus membrane (B) is the only GPI-anchored membrane localization, making it the sole viable answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific identification of this protein as JUNO/folate receptor 4 and its documented localization to oolemma microvilli (rather than general plasma membrane) is protein-specific knowledge. However, since 'plasma membrane' is not among the choices, the reasoning from signal peptide + GPI anchor + non-mitochondrial/non-nuclear character sufficiently distinguishes B from A, C, and D without requiring the exact protein identity.",
    "reason": "A model can reason from visible sequence features (signal peptide, GPI-anchor-like C-terminus, absence of mitochondrial targeting sequence, absence of nuclear localization signal) to eliminate three of four options. The specific 'microvillus' sub-localization within the membrane is protein-specific, but among the four given choices, only B is a membrane compartment compatible with a GPI-anchored secretory-pathway protein."
  },
  "case_id": "GO_cellular_component_0188",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt F1M928 (JUNO_RAT) explicitly annotates 'Cell projection, microvillus membrane' in its SUBCELLULAR LOCATION comment (C5, H3), with the note 'GPI-anchored at the oolemma microvilli.' GO term GO:0031528 (microvillus membrane) is cross-referenced (C6, H5). The evidence code for this annotation is IEA (transferred from UniProtKB:A6ND01/Q9EQF4), while plasma membrane carries IDA evidence. However, the microvillus membrane annotation is present and not contradicted. The expected answer aligns with the annotation."
  },
  "important_caveats": [
    "The microvillus membrane annotation carries IEA evidence (transferred from mouse JUNO Q9EQF4 and another protein A6ND01), not direct experimental evidence for this rat sequence. The IDA-evidenced location is plasma membrane (GO:0005886), which is not offered as a choice.",
    "The GPI anchor is inferred by similarity (ECO:0000250) rather than experimentally confirmed for this specific rat JUNO sequence.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely solely on sequence features and general biological knowledge.",
    "The C-terminal hydrophobic stretch (FSLCLLLHA, 9 residues) is short for a canonical GPI-anchor signal; a model might not confidently identify a GPI anchor without recognizing the folate-receptor family context."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different compartments (parasite mitochondrial substructure, extracellular glycoprotein layer, nuclear chromatin complex, plasma-membrane microdomain). The sequence features cleanly eliminate A, C, and D. No two options are equally defensible given the GPI-anchor and signal-peptide evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0188",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt F1M928 (JUNO_RAT) explicitly annotates 'Cell projection, microvillus membrane' in its SUBCELLULAR LOCATION comment (C5, H3), with the note 'GPI-anchored at the oolemma microvilli.' GO term GO:0031528 (microvillus membrane) is cross-referenced (C6, H5). The evidence code for this annotation is IEA (transferred from UniProtKB:A6ND01/Q9EQF4), while plasma membrane carries IDA evidence. However, the microvillus membrane annotation is present and not contradicted. The expected answer aligns with the annotation.",
    "evidence_ids": ["C5", "C6", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits (1) an N-terminal signal peptide (MAQWWLILLGLWTVLPSLAGG) indicating entry into the secretory pathway, which eliminates the nuclear SAGA complex (D); (2) a C-terminal hydrophobic region (FSLCLLLHA) consistent with a GPI anchor, indicating membrane anchoring rather than free secretion, which eliminates the extracellular vitelline envelope (C); (3) a cysteine-rich, ~244-aa folate-receptor-like fold with no mitochondrial targeting presequence, eliminating the kinetoplast (A), a mitochondrial DNA substructure specific to kinetoplastid parasites. Among the remaining options, microvillus membrane (B) is the only GPI-anchored membrane localization, making it the sole viable answer.",
    "missing_item_specific_fact": "The specific identification of this protein as JUNO/folate receptor 4 and its documented localization to oolemma microvilli (rather than general plasma membrane) is protein-specific knowledge. However, since 'plasma membrane' is not among the choices, the reasoning from signal peptide + GPI anchor + non-mitochondrial/non-nuclear character sufficiently distinguishes B from A, C, and D without requiring the exact protein identity.",
    "reason": "A model can reason from visible sequence features (signal peptide, GPI-anchor-like C-terminus, absence of mitochondrial targeting sequence, absence of nuclear localization signal) to eliminate three of four options. The specific 'microvillus' sub-localization within the membrane is protein-specific, but among the four given choices, only B is a membrane compartment compatible with a GPI-anchored secretory-pathway protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different compartments (parasite mitochondrial substructure, extracellular glycoprotein layer, nuclear chromatin complex, plasma-membrane microdomain). The sequence features cleanly eliminate A, C, and D. No two options are equally defensible given the GPI-anchor and signal-peptide evidence."
  },
  "important_caveats": [
    "The microvillus membrane annotation carries IEA evidence (transferred from mouse JUNO Q9EQF4 and another protein A6ND01), not direct experimental evidence for this rat sequence. The IDA-evidenced location is plasma membrane (GO:0005886), which is not offered as a choice.",
    "The GPI anchor is inferred by similarity (ECO:0000250) rather than experimentally confirmed for this specific rat JUNO sequence.",
    "The reviewer-only evidence was absent from the evaluated model input; the model must rely solely on sequence features and general biological knowledge.",
    "The C-terminal hydrophobic stretch (FSLCLLLHA, 9 residues) is short for a canonical GPI-anchor signal; a model might not confidently identify a GPI anchor without recognizing the folate-receptor family context."
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

**Accession:** `F1M928` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 92. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:11.745036+00:00.  

```json
{"alternativeNames":[{"fullName":{"value":"Folate receptor 4"}},{"fullName":{"value":"Folate receptor delta"},"shortNames":[{"value":"FR-delta"}]},{"fullName":{"value":"IZUMO1 receptor protein JUNO"}}],"flag":"Precursor","recommendedName":{"fullName":{"value":"Sperm-egg fusion protein Juno"}}}
```

Source SHA-256: `b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:11.745036+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9EQF4","source":"UniProtKB"}],"value":"GPI-anchored at the oolemma microvilli"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"37951137","source":"PubMed"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9EQF4","source":"UniProtKB"}],"id":"SL-9902","value":"Lipid-anchor, GPI-anchor"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"A6ND01","source":"UniProtKB"}],"id":"SL-0294","value":"Cell projection, microvillus membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9EQF4","source":"UniProtKB"}],"id":"SL-9902","value":"Lipid-anchor, GPI-anchor"}}]}
```

Source SHA-256: `b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)  
**Locator:** `/uniProtKBCrossReferences/30`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:11.745036+00:00.  

```json
{"database":"GO","id":"GO:0031528","properties":[{"key":"GoTerm","value":"C:microvillus membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/F1M928.json)  
**Locator:** `/uniProtKBCrossReferences/31`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:11.745036+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"37951137","source":"PubMed"}],"id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `b56a36704099444e686e704fe8993d737b0fe848fed00c7247b8f75bf147a97d`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92)  
**Locator:** `lines 100-104`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 2.  
**Retrieved:** 2026-11-02T04:28:13.956568+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:37951137};
CC       Lipid-anchor, GPI-anchor {ECO:0000250|UniProtKB:Q9EQF4}. Cell
CC       projection, microvillus membrane {ECO:0000250|UniProtKB:A6ND01}; Lipid-
CC       anchor, GPI-anchor {ECO:0000250|UniProtKB:Q9EQF4}. Note=GPI-anchored at
CC       the oolemma microvilli. {ECO:0000250|UniProtKB:Q9EQF4}.
```

Source SHA-256: `57bdb51b29963fdcfb395f44171ffb2ca0c93e66ec625c64278875faf6b4aa52`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92)  
**Locator:** `lines 148-148`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 2.  
**Retrieved:** 2026-11-02T04:28:13.956568+00:00.  

```text
DR   GO; GO:0031528; C:microvillus membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `57bdb51b29963fdcfb395f44171ffb2ca0c93e66ec625c64278875faf6b4aa52`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/F1M928?format=txt&versions=92)  
**Locator:** `lines 149-149`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 2.  
**Retrieved:** 2026-11-02T04:28:13.956568+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IDA:UniProtKB.
```

Source SHA-256: `57bdb51b29963fdcfb395f44171ffb2ca0c93e66ec625c64278875faf6b4aa52`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 188. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
