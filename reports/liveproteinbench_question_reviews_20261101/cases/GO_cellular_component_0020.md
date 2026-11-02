# GO_cellular_component_0020

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MALVRFATIITVLCHLAIQDGAAKSFPHGEKAPFPLTLIHINDLHARFDETNQKSSTCTNSKECIAGIARVYHTIKQLKSEYKTKNPLYLNAGDNFQGTLWYNLLRWNVTAYFIKELPPDAMTLGNHEFDHSPKGLAPYLAELEKMKIPTVVANLEKNGEPALKDSKIARSIVLKVGNRKVGVIGALYDKTHLVAQTGMVTLTNSIEAVRKEAQELKKKNVNIIVVLSHCGLDGDKQLAEEAGDLIDVIVGAHSHSLLLNKDAKVPYDTKYDTIEGDYPLVVKKSNNHTVLITQARSFGKYVGRLTVNFDCEGEVQSWEGYPIYMNNSVKQDEEVLRELEPWRAEVKRLGTQVIGTTEVFLDRESCRWCECTLGDLIADAYADQYTNSTVQPVAFVQAGNFRNPIEKGDITNGLAIEAAPYGSSVDMIKLSGADLWSAIDHSFTLDDEFRYNTAQVSGMAVVADLSKKPYERVQSIDIVGANGAKTALKKDQIYYVVVPSYLADGKDGFAMLKKGTNRVTGPLDSDVLIEYVRKRQTIAKTMFQEKRVVIENHTNGTCSWDLDSQRYKPK

[Multiple Choices]
A. microvillus membrane
B. centrosome
C. plasma membrane
D. caveola
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

> The exact-matching sequence has a plasma-membrane GO annotation with IBA evidence, which supports C as a computational inference, not as direct experimental localization. The record also reports experimentally supported secretion and extracellular-region localization, so plasma membrane is not established as its primary residence.

Citations as saved: [C7](#evidence-c7), [H6](#evidence-h6), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with entry into the secretory pathway, but does not distinguish plasma membrane from microvillus membrane or caveola; the sequence offers no clear basis for assigning one of those specific membrane locations.


**Missing item-specific fact**

> The protein-specific GO plasma-membrane annotation or experimental localization information is absent from the question.


**Reason**

> Choosing C depends on the item-specific annotation rather than a sequence feature that meaningfully separates the membrane-related options. The secretory signal does not establish plasma-membrane residence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options include specialized membrane regions that are biologically portions of the plasma membrane, but the supplied sequence does not indicate localization to either microvilli or caveolae.


### Important caveats

- The plasma-membrane annotation is IBA-based; it is not direct experimental evidence for plasma-membrane residence.
- The cited experimental subcellular-location annotation reports secretion, and a GO annotation reports extracellular region.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with entry into the secretory pathway, but does not distinguish plasma membrane from microvillus membrane or caveola; the sequence offers no clear basis for assigning one of those specific membrane locations.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific GO plasma-membrane annotation or experimental localization information is absent from the question.",
    "reason": "Choosing C depends on the item-specific annotation rather than a sequence feature that meaningfully separates the membrane-related options. The secretory signal does not establish plasma-membrane residence."
  },
  "case_id": "GO_cellular_component_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H6",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact-matching sequence has a plasma-membrane GO annotation with IBA evidence, which supports C as a computational inference, not as direct experimental localization. The record also reports experimentally supported secretion and extracellular-region localization, so plasma membrane is not established as its primary residence."
  },
  "important_caveats": [
    "The plasma-membrane annotation is IBA-based; it is not direct experimental evidence for plasma-membrane residence.",
    "The cited experimental subcellular-location annotation reports secretion, and a GO annotation reports extracellular region."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options include specialized membrane regions that are biologically portions of the plasma membrane, but the supplied sequence does not indicate localization to either microvilli or caveolae."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matching sequence has a plasma-membrane GO annotation with IBA evidence, which supports C as a computational inference, not as direct experimental localization. The record also reports experimentally supported secretion and extracellular-region localization, so plasma membrane is not established as its primary residence.",
    "evidence_ids": ["C7", "H6", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with entry into the secretory pathway, but does not distinguish plasma membrane from microvillus membrane or caveola; the sequence offers no clear basis for assigning one of those specific membrane locations.",
    "missing_item_specific_fact": "The protein-specific GO plasma-membrane annotation or experimental localization information is absent from the question.",
    "reason": "Choosing C depends on the item-specific annotation rather than a sequence feature that meaningfully separates the membrane-related options. The secretory signal does not establish plasma-membrane residence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options include specialized membrane regions that are biologically portions of the plasma membrane, but the supplied sequence does not indicate localization to either microvilli or caveolae."
  },
  "important_caveats": [
    "The plasma-membrane annotation is IBA-based; it is not direct experimental evidence for plasma-membrane residence.",
    "The cited experimental subcellular-location annotation reports secretion, and a GO annotation reports extracellular region."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The GO:0005886 (plasma membrane) annotation exists for this protein (evidence C7, H6), albeit with IBA:GO_Central (computational inference) evidence. However, the primary experimental evidence (ECO:0000269, PubMed:39294191; evidence C5, H4, C6, H5) states the subcellular location is 'Secreted' with GO:0005576 (extracellular region, IDA). The protein is an ecto-5'-nucleotidase/apyrase from Anopheles gambiae salivary glands. Among the four forced choices (microvillus membrane, centrosome, plasma membrane, caveola), plasma membrane is the most defensible because: (1) the IBA annotation exists, (2) ecto-enzymes are conceptually associated with the cell surface, and (3) the other three options are clearly incompatible. The key is weakly supported by the computational annotation and is the best available choice, though the true experimental location is 'secreted/extracellular' rather than membrane-bound.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence (MALVRFATIITVLCHLAIQD...) is a classic signal peptide directing the protein into the secretory pathway. The protein contains conserved nucleotidase/apyrase motifs (e.g., the 'GDLIADAYAD' and 'GANGAKTALKK' regions characteristic of the ecto-nucleotidase family), indicating it is an ecto-enzyme acting on extracellular nucleotides. No transmembrane helix or GPI-anchor signal is apparent in the mature sequence. Among the choices: centrosome (B) is incompatible with a secreted enzyme; caveola (D) requires caveolin-binding motifs and palmitoylation sites absent here; microvillus membrane (A) requires specific apical-targeting signals not present. Plasma membrane (C) is the most general cell-surface compartment consistent with an ecto-enzyme acting on the extracellular face, making it the best answer among the forced choices.


**Missing item-specific fact**

> The experimental determination that the protein is fully secreted (not membrane-anchored) rather than a membrane-bound ecto-enzyme. Without this, a model cannot be certain the protein is not actually membrane-anchored vs. freely secreted, though this distinction does not change the best answer among the four choices.


**Reason**

> A model can reason from the signal peptide, absence of transmembrane domains, ecto-enzyme family identification, and the specificity requirements of caveola/microvillus targeting to eliminate three options and select plasma membrane. The reasoning does not require memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four choices, plasma membrane is clearly the most defensible. Centrosome is incompatible with a secreted enzyme. Caveola and microvillus membrane are highly specific plasma membrane subdomains requiring targeting signals absent from this sequence. No other option is competitive.


### Important caveats

- The true experimentally-determined primary location is 'Secreted' (extracellular region, GO:0005576, IDA), not 'plasma membrane' (GO:0005886, IBA computational inference). The forced-choice format makes plasma membrane the best available answer, but it is not the protein's actual primary location.
- The plasma membrane GO annotation (C7/H6) carries only IBA:GO_Central evidence (computational inference from related proteins), not experimental data. The experimental evidence (C5/H4, C6/H5) points to secretion.
- The 2024 Nature Communications paper (PubMed:39294191) that established the 'Secreted' location was published in 2024; the original benchmark may have been constructed before this annotation was updated, potentially explaining why 'plasma membrane' was chosen as the key based on the IBA annotation available at construction time.
- The protein is from Anopheles gambiae (insect), not a mammalian system. Caveola and microvillus membrane are primarily mammalian/vertebrate concepts; their applicability to insect salivary gland biology is questionable, further weakening options A and D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence (MALVRFATIITVLCHLAIQD...) is a classic signal peptide directing the protein into the secretory pathway. The protein contains conserved nucleotidase/apyrase motifs (e.g., the 'GDLIADAYAD' and 'GANGAKTALKK' regions characteristic of the ecto-nucleotidase family), indicating it is an ecto-enzyme acting on extracellular nucleotides. No transmembrane helix or GPI-anchor signal is apparent in the mature sequence. Among the choices: centrosome (B) is incompatible with a secreted enzyme; caveola (D) requires caveolin-binding motifs and palmitoylation sites absent here; microvillus membrane (A) requires specific apical-targeting signals not present. Plasma membrane (C) is the most general cell-surface compartment consistent with an ecto-enzyme acting on the extracellular face, making it the best answer among the forced choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The experimental determination that the protein is fully secreted (not membrane-anchored) rather than a membrane-bound ecto-enzyme. Without this, a model cannot be certain the protein is not actually membrane-anchored vs. freely secreted, though this distinction does not change the best answer among the four choices.",
    "reason": "A model can reason from the signal peptide, absence of transmembrane domains, ecto-enzyme family identification, and the specificity requirements of caveola/microvillus targeting to eliminate three options and select plasma membrane. The reasoning does not require memorizing this specific protein's annotation."
  },
  "case_id": "GO_cellular_component_0020",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The GO:0005886 (plasma membrane) annotation exists for this protein (evidence C7, H6), albeit with IBA:GO_Central (computational inference) evidence. However, the primary experimental evidence (ECO:0000269, PubMed:39294191; evidence C5, H4, C6, H5) states the subcellular location is 'Secreted' with GO:0005576 (extracellular region, IDA). The protein is an ecto-5'-nucleotidase/apyrase from Anopheles gambiae salivary glands. Among the four forced choices (microvillus membrane, centrosome, plasma membrane, caveola), plasma membrane is the most defensible because: (1) the IBA annotation exists, (2) ecto-enzymes are conceptually associated with the cell surface, and (3) the other three options are clearly incompatible. The key is weakly supported by the computational annotation and is the best available choice, though the true experimental location is 'secreted/extracellular' rather than membrane-bound."
  },
  "important_caveats": [
    "The true experimentally-determined primary location is 'Secreted' (extracellular region, GO:0005576, IDA), not 'plasma membrane' (GO:0005886, IBA computational inference). The forced-choice format makes plasma membrane the best available answer, but it is not the protein's actual primary location.",
    "The plasma membrane GO annotation (C7/H6) carries only IBA:GO_Central evidence (computational inference from related proteins), not experimental data. The experimental evidence (C5/H4, C6/H5) points to secretion.",
    "The 2024 Nature Communications paper (PubMed:39294191) that established the 'Secreted' location was published in 2024; the original benchmark may have been constructed before this annotation was updated, potentially explaining why 'plasma membrane' was chosen as the key based on the IBA annotation available at construction time.",
    "The protein is from Anopheles gambiae (insect), not a mammalian system. Caveola and microvillus membrane are primarily mammalian/vertebrate concepts; their applicability to insect salivary gland biology is questionable, further weakening options A and D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, plasma membrane is clearly the most defensible. Centrosome is incompatible with a secreted enzyme. Caveola and microvillus membrane are highly specific plasma membrane subdomains requiring targeting signals absent from this sequence. No other option is competitive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0020",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The GO:0005886 (plasma membrane) annotation exists for this protein (evidence C7, H6), albeit with IBA:GO_Central (computational inference) evidence. However, the primary experimental evidence (ECO:0000269, PubMed:39294191; evidence C5, H4, C6, H5) states the subcellular location is 'Secreted' with GO:0005576 (extracellular region, IDA). The protein is an ecto-5'-nucleotidase/apyrase from Anopheles gambiae salivary glands. Among the four forced choices (microvillus membrane, centrosome, plasma membrane, caveola), plasma membrane is the most defensible because: (1) the IBA annotation exists, (2) ecto-enzymes are conceptually associated with the cell surface, and (3) the other three options are clearly incompatible. The key is weakly supported by the computational annotation and is the best available choice, though the true experimental location is 'secreted/extracellular' rather than membrane-bound.",
    "evidence_ids": ["C5", "C6", "C7", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence (MALVRFATIITVLCHLAIQD...) is a classic signal peptide directing the protein into the secretory pathway. The protein contains conserved nucleotidase/apyrase motifs (e.g., the 'GDLIADAYAD' and 'GANGAKTALKK' regions characteristic of the ecto-nucleotidase family), indicating it is an ecto-enzyme acting on extracellular nucleotides. No transmembrane helix or GPI-anchor signal is apparent in the mature sequence. Among the choices: centrosome (B) is incompatible with a secreted enzyme; caveola (D) requires caveolin-binding motifs and palmitoylation sites absent here; microvillus membrane (A) requires specific apical-targeting signals not present. Plasma membrane (C) is the most general cell-surface compartment consistent with an ecto-enzyme acting on the extracellular face, making it the best answer among the forced choices.",
    "missing_item_specific_fact": "The experimental determination that the protein is fully secreted (not membrane-anchored) rather than a membrane-bound ecto-enzyme. Without this, a model cannot be certain the protein is not actually membrane-anchored vs. freely secreted, though this distinction does not change the best answer among the four choices.",
    "reason": "A model can reason from the signal peptide, absence of transmembrane domains, ecto-enzyme family identification, and the specificity requirements of caveola/microvillus targeting to eliminate three options and select plasma membrane. The reasoning does not require memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four choices, plasma membrane is clearly the most defensible. Centrosome is incompatible with a secreted enzyme. Caveola and microvillus membrane are highly specific plasma membrane subdomains requiring targeting signals absent from this sequence. No other option is competitive."
  },
  "important_caveats": [
    "The true experimentally-determined primary location is 'Secreted' (extracellular region, GO:0005576, IDA), not 'plasma membrane' (GO:0005886, IBA computational inference). The forced-choice format makes plasma membrane the best available answer, but it is not the protein's actual primary location.",
    "The plasma membrane GO annotation (C7/H6) carries only IBA:GO_Central evidence (computational inference from related proteins), not experimental data. The experimental evidence (C5/H4, C6/H5) points to secretion.",
    "The 2024 Nature Communications paper (PubMed:39294191) that established the 'Secreted' location was published in 2024; the original benchmark may have been constructed before this annotation was updated, potentially explaining why 'plasma membrane' was chosen as the key based on the IBA annotation available at construction time.",
    "The protein is from Anopheles gambiae (insect), not a mammalian system. Caveola and microvillus membrane are primarily mammalian/vertebrate concepts; their applicability to insect salivary gland biology is questionable, further weakening options A and D."
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

**Accession:** `Q5TVM9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 120. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)  
**Locator:** `/comments/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:23.238423+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"39294191","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}}]}
```

Source SHA-256: `d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)  
**Locator:** `/uniProtKBCrossReferences/15`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:23.238423+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"17913537","source":"PubMed"},{"evidenceCode":"ECO:0000314","id":"39294191","source":"PubMed"}],"id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5TVM9.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:23.238423+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `d9052fa8ef05e8e69b89dab60cf36fb3e5b7be30c46effc6cc02e314338d28a0`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)  
**Locator:** `lines 114-114`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 120 / 1.  
**Retrieved:** 2026-11-01T06:28:38.028811+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000269|PubMed:39294191}.
```

Source SHA-256: `dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)  
**Locator:** `lines 154-154`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 120 / 1.  
**Retrieved:** 2026-11-01T06:28:38.028811+00:00.  

```text
DR   GO; GO:0005615; C:extracellular space; IDA:UniProtKB.
```

Source SHA-256: `dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5TVM9?format=txt&versions=120)  
**Locator:** `lines 155-155`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 120 / 1.  
**Retrieved:** 2026-11-01T06:28:38.028811+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IBA:GO_Central.
```

Source SHA-256: `dc7c135ba0e00346e9feec3ec57f78300f98f0e06c9e00b0cc63acc479548945`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 20. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
