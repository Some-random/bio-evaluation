# GO_cellular_component_0127

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — cytosol

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTVNLTELDAHEQPSDQMRAIWKSYSRADKEELLLNGAIDDLEKPEKAAEFVVAGTVPAATLTKGFAFLGSGFDAAASDAPIYYHPLLPGLLIFPSIVPLEVQKTLLSKLIHRDLSVPAHQTNMHLHYELPYVERKPTDGEGEPEDCRQSFFSHSPDSPVRFQPKDPDVHKPLSMKQVMDRRLHWVTLGGQYDWTNRVYPEEEPPKFPPDVAGFLETVFPDTIAQAAIVNFYTPGDTMMMHRDVSEETDKGLVSLSLGCDGLFMIAPSDIGKMSEEERPEDVKKQYLLLRLRSGDAIYMIKESRYAWHGVPKVLKGTCPEALEDWPAEDGRFEEWRGWMKNKRINLNVRQMRE

[Multiple Choices]
A. centrosome
B. cytosol
C. RNA polymerase II transcription regulator complex
D. lysosomal membrane
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

> The sequence-matched UniProt record assigns GO:0005829 (cytosol), but with ISS evidence, so this is a computational/inferred annotation rather than direct experimental proof of cytosolic localization. The cited experimental localization is to cytoplasm/P-bodies, which supports a cytoplasmic location but is not itself an exact cytosol measurement.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has no obvious transmembrane segment or clear organelle-targeting peptide, which favors a soluble intracellular protein over a lysosomal membrane protein. That does not distinguish cytosol from other intracellular locations or establish the specific localization.


**Missing item-specific fact**

> The protein-specific localization annotation or experimental observation that this sequence-matched protein is cytoplasmic/P-body-associated, and its inferred cytosol GO assignment.


**Reason**

> The sequence and choices support only broad solubility-related inference; selecting cytosol over other intracellular possibilities depends on protein-specific localization information not supplied to the model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The available sequence-matched annotation supports the keyed cytosol option. The localization evidence also mentions P-bodies, but that location is not an offered choice; the other choices are not comparably supported.


### Important caveats

- The sequence match and protein identity were established using reviewer-only sources; they were not available in the evaluated input.
- The experimental annotation is for cytoplasm/P-bodies, whereas the cytosol GO annotation is ISS-based; these are related but not identical evidence claims.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has no obvious transmembrane segment or clear organelle-targeting peptide, which favors a soluble intracellular protein over a lysosomal membrane protein. That does not distinguish cytosol from other intracellular locations or establish the specific localization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization annotation or experimental observation that this sequence-matched protein is cytoplasmic/P-body-associated, and its inferred cytosol GO assignment.",
    "reason": "The sequence and choices support only broad solubility-related inference; selecting cytosol over other intracellular possibilities depends on protein-specific localization information not supplied to the model."
  },
  "case_id": "GO_cellular_component_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns GO:0005829 (cytosol), but with ISS evidence, so this is a computational/inferred annotation rather than direct experimental proof of cytosolic localization. The cited experimental localization is to cytoplasm/P-bodies, which supports a cytoplasmic location but is not itself an exact cytosol measurement."
  },
  "important_caveats": [
    "The sequence match and protein identity were established using reviewer-only sources; they were not available in the evaluated input.",
    "The experimental annotation is for cytoplasm/P-bodies, whereas the cytosol GO annotation is ISS-based; these are related but not identical evidence claims."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available sequence-matched annotation supports the keyed cytosol option. The localization evidence also mentions P-bodies, but that location is not an offered choice; the other choices are not comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns GO:0005829 (cytosol), but with ISS evidence, so this is a computational/inferred annotation rather than direct experimental proof of cytosolic localization. The cited experimental localization is to cytoplasm/P-bodies, which supports a cytoplasmic location but is not itself an exact cytosol measurement.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has no obvious transmembrane segment or clear organelle-targeting peptide, which favors a soluble intracellular protein over a lysosomal membrane protein. That does not distinguish cytosol from other intracellular locations or establish the specific localization.",
    "missing_item_specific_fact": "The protein-specific localization annotation or experimental observation that this sequence-matched protein is cytoplasmic/P-body-associated, and its inferred cytosol GO assignment.",
    "reason": "The sequence and choices support only broad solubility-related inference; selecting cytosol over other intracellular possibilities depends on protein-specific localization information not supplied to the model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available sequence-matched annotation supports the keyed cytosol option. The localization evidence also mentions P-bodies, but that location is not an offered choice; the other choices are not comparably supported."
  },
  "important_caveats": [
    "The sequence match and protein identity were established using reviewer-only sources; they were not available in the evaluated input.",
    "The experimental annotation is for cytoplasm/P-bodies, whereas the cytosol GO annotation is ISS-based; these are related but not identical evidence claims."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The experimental subcellular location annotation (ECO:0000269, PubMed:30535195) places this protein in 'Cytoplasm, P-body' (C5/H3). P-bodies are cytoplasmic structures, and the GO cytosol term (GO:0005829, C6/H4) is a component of cytoplasm. Among the four options, cytosol is the closest match to the experimentally determined cytoplasmic/P-body localization. The other options (centrosome, RNA Pol II transcription regulator complex, lysosomal membrane) have no supporting annotation. The GO cytosol annotation itself is ISS (inferred), but the underlying experimental evidence for cytoplasmic/P-body localization is solid.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [C9](#evidence-c9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence encodes a 353-aa soluble enzyme (Fe(II)/α-ketoglutarate dioxygenase fold, characteristic AlkB-family 'HRD...H...H' facial triad motifs visible in the sequence). It lacks transmembrane segments (eliminating lysosomal membrane, D), lacks DNA-binding or multi-subunit complex-forming domains typical of transcription regulator complexes (eliminating C), and lacks centrosomal protein motifs or coiled-coil/γ-tubulin-binding regions (eliminating A). With no signal peptide, mitochondrial targeting sequence, or nuclear localization signal, and being a small soluble enzyme, cytosol is the default and only remaining viable compartment among the options.


**Missing item-specific fact**

> The specific experimental finding that this RNA demethylase localizes to cytoplasmic P-bodies rather than the nucleus (where one might intuitively expect an RNA-modifying enzyme to act) is a protein-specific experimental result. However, since 'nucleus' is not among the answer choices, this nuance does not affect the answer selection.


**Reason**

> Elimination of the three distractors relies on general biological knowledge: no TM domains rules out membrane localization; the protein is a small catalytic enzyme, not a transcription complex subunit; and it lacks centrosomal structural motifs. The remaining option (cytosol) is the default for a soluble enzyme with no targeting signals. The reasoning is primarily by elimination but is grounded in standard protein-localization biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other option is defensible. The experimental evidence clearly places the protein in the cytoplasm (P-body). Centrosome is implausible for a fungal enzyme with no centrosomal motifs; lysosomal membrane is excluded by the absence of TM domains; RNA Pol II transcription regulator complex is a nuclear multi-subunit complex incompatible with a small soluble dioxygenase. The slight imprecision between 'P-body' (experimental) and 'cytosol' (answer) is acceptable since P-bodies reside in the cytosol and P-body is not an option.


### Important caveats

- The experimental annotation specifies 'Cytoplasm, P-body' while the answer is 'cytosol.' P-bodies are cytoplasmic ribonucleoprotein granules, and cytosol (GO:0005829) is part_of cytoplasm (GO:0005737), so the mapping is reasonable but not perfectly precise.
- A GO nucleus annotation (ISS:PAMGO_MGG) also exists (C7/H5), but 'nucleus' is not among the options, so it does not create ambiguity in answer selection.
- The GO cytosol annotation is ISS (inferred by similarity), while the experimental evidence is for 'Cytoplasm, P-body.' The answer relies on the experimental cytoplasmic evidence rather than the ISS cytosol annotation per se.
- The organism is Pyricularia oryzae (a fungus); fungi lack canonical centrosomes, further weakening option A, though this organism-specific fact is not stated in the question input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence encodes a 353-aa soluble enzyme (Fe(II)/α-ketoglutarate dioxygenase fold, characteristic AlkB-family 'HRD...H...H' facial triad motifs visible in the sequence). It lacks transmembrane segments (eliminating lysosomal membrane, D), lacks DNA-binding or multi-subunit complex-forming domains typical of transcription regulator complexes (eliminating C), and lacks centrosomal protein motifs or coiled-coil/γ-tubulin-binding regions (eliminating A). With no signal peptide, mitochondrial targeting sequence, or nuclear localization signal, and being a small soluble enzyme, cytosol is the default and only remaining viable compartment among the options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific experimental finding that this RNA demethylase localizes to cytoplasmic P-bodies rather than the nucleus (where one might intuitively expect an RNA-modifying enzyme to act) is a protein-specific experimental result. However, since 'nucleus' is not among the answer choices, this nuance does not affect the answer selection.",
    "reason": "Elimination of the three distractors relies on general biological knowledge: no TM domains rules out membrane localization; the protein is a small catalytic enzyme, not a transcription complex subunit; and it lacks centrosomal structural motifs. The remaining option (cytosol) is the default for a soluble enzyme with no targeting signals. The reasoning is primarily by elimination but is grounded in standard protein-localization biology."
  },
  "case_id": "GO_cellular_component_0127",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The experimental subcellular location annotation (ECO:0000269, PubMed:30535195) places this protein in 'Cytoplasm, P-body' (C5/H3). P-bodies are cytoplasmic structures, and the GO cytosol term (GO:0005829, C6/H4) is a component of cytoplasm. Among the four options, cytosol is the closest match to the experimentally determined cytoplasmic/P-body localization. The other options (centrosome, RNA Pol II transcription regulator complex, lysosomal membrane) have no supporting annotation. The GO cytosol annotation itself is ISS (inferred), but the underlying experimental evidence for cytoplasmic/P-body localization is solid."
  },
  "important_caveats": [
    "The experimental annotation specifies 'Cytoplasm, P-body' while the answer is 'cytosol.' P-bodies are cytoplasmic ribonucleoprotein granules, and cytosol (GO:0005829) is part_of cytoplasm (GO:0005737), so the mapping is reasonable but not perfectly precise.",
    "A GO nucleus annotation (ISS:PAMGO_MGG) also exists (C7/H5), but 'nucleus' is not among the options, so it does not create ambiguity in answer selection.",
    "The GO cytosol annotation is ISS (inferred by similarity), while the experimental evidence is for 'Cytoplasm, P-body.' The answer relies on the experimental cytoplasmic evidence rather than the ISS cytosol annotation per se.",
    "The organism is Pyricularia oryzae (a fungus); fungi lack canonical centrosomes, further weakening option A, though this organism-specific fact is not stated in the question input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other option is defensible. The experimental evidence clearly places the protein in the cytoplasm (P-body). Centrosome is implausible for a fungal enzyme with no centrosomal motifs; lysosomal membrane is excluded by the absence of TM domains; RNA Pol II transcription regulator complex is a nuclear multi-subunit complex incompatible with a small soluble dioxygenase. The slight imprecision between 'P-body' (experimental) and 'cytosol' (answer) is acceptable since P-bodies reside in the cytosol and P-body is not an option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0127",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The experimental subcellular location annotation (ECO:0000269, PubMed:30535195) places this protein in 'Cytoplasm, P-body' (C5/H3). P-bodies are cytoplasmic structures, and the GO cytosol term (GO:0005829, C6/H4) is a component of cytoplasm. Among the four options, cytosol is the closest match to the experimentally determined cytoplasmic/P-body localization. The other options (centrosome, RNA Pol II transcription regulator complex, lysosomal membrane) have no supporting annotation. The GO cytosol annotation itself is ISS (inferred), but the underlying experimental evidence for cytoplasmic/P-body localization is solid.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "C9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence encodes a 353-aa soluble enzyme (Fe(II)/α-ketoglutarate dioxygenase fold, characteristic AlkB-family 'HRD...H...H' facial triad motifs visible in the sequence). It lacks transmembrane segments (eliminating lysosomal membrane, D), lacks DNA-binding or multi-subunit complex-forming domains typical of transcription regulator complexes (eliminating C), and lacks centrosomal protein motifs or coiled-coil/γ-tubulin-binding regions (eliminating A). With no signal peptide, mitochondrial targeting sequence, or nuclear localization signal, and being a small soluble enzyme, cytosol is the default and only remaining viable compartment among the options.",
    "missing_item_specific_fact": "The specific experimental finding that this RNA demethylase localizes to cytoplasmic P-bodies rather than the nucleus (where one might intuitively expect an RNA-modifying enzyme to act) is a protein-specific experimental result. However, since 'nucleus' is not among the answer choices, this nuance does not affect the answer selection.",
    "reason": "Elimination of the three distractors relies on general biological knowledge: no TM domains rules out membrane localization; the protein is a small catalytic enzyme, not a transcription complex subunit; and it lacks centrosomal structural motifs. The remaining option (cytosol) is the default for a soluble enzyme with no targeting signals. The reasoning is primarily by elimination but is grounded in standard protein-localization biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other option is defensible. The experimental evidence clearly places the protein in the cytoplasm (P-body). Centrosome is implausible for a fungal enzyme with no centrosomal motifs; lysosomal membrane is excluded by the absence of TM domains; RNA Pol II transcription regulator complex is a nuclear multi-subunit complex incompatible with a small soluble dioxygenase. The slight imprecision between 'P-body' (experimental) and 'cytosol' (answer) is acceptable since P-bodies reside in the cytosol and P-body is not an option."
  },
  "important_caveats": [
    "The experimental annotation specifies 'Cytoplasm, P-body' while the answer is 'cytosol.' P-bodies are cytoplasmic ribonucleoprotein granules, and cytosol (GO:0005829) is part_of cytoplasm (GO:0005737), so the mapping is reasonable but not perfectly precise.",
    "A GO nucleus annotation (ISS:PAMGO_MGG) also exists (C7/H5), but 'nucleus' is not among the options, so it does not create ambiguity in answer selection.",
    "The GO cytosol annotation is ISS (inferred by similarity), while the experimental evidence is for 'Cytoplasm, P-body.' The answer relies on the experimental cytoplasmic evidence rather than the ISS cytosol annotation per se.",
    "The organism is Pyricularia oryzae (a fungus); fungi lack canonical centrosomes, further weakening option A, though this organism-specific fact is not stated in the question input."
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

**Accession:** `G4MZ21` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 55. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MZ21.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:43.333607+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"30535195","source":"PubMed"}],"id":"SL-0230","value":"Cytoplasm, P-body"}}]}
```

Source SHA-256: `912b707615953e09c752dc6d954d39172df78da8b465c36f8304f450ed73836b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MZ21.json)  
**Locator:** `/uniProtKBCrossReferences/16`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:43.333607+00:00.  

```json
{"database":"GO","id":"GO:0005829","properties":[{"key":"GoTerm","value":"C:cytosol"},{"key":"GoEvidenceType","value":"ISS:PAMGO_MGG"}]}
```

Source SHA-256: `912b707615953e09c752dc6d954d39172df78da8b465c36f8304f450ed73836b`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MZ21.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:43.333607+00:00.  

```json
{"database":"GO","id":"GO:0005634","properties":[{"key":"GoTerm","value":"C:nucleus"},{"key":"GoEvidenceType","value":"ISS:PAMGO_MGG"}]}
```

Source SHA-256: `912b707615953e09c752dc6d954d39172df78da8b465c36f8304f450ed73836b`.

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MZ21.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:43.333607+00:00.  

```json
{"citation":{"authors":["Shi Y.","Wang H.","Wang J.","Liu X.","Lin F.","Lu J."],"citationCrossReferences":[{"database":"PubMed","id":"30535195"},{"database":"DOI","id":"10.1093/femsle/fny286"}],"citationType":"journal article","firstPage":"0","id":"30535195","journal":"FEMS Microbiol. Lett.","lastPage":"0","publicationDate":"2019","title":"N6-methyladenosine RNA methylation is involved in virulence of the rice blast fungus Pyricularia oryzae (syn. Magnaporthe oryzae).","volume":"366"},"referenceNumber":2,"referencePositions":["FUNCTION","DISRUPTION PHENOTYPE","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `912b707615953e09c752dc6d954d39172df78da8b465c36f8304f450ed73836b`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MZ21?format=txt&versions=55)  
**Locator:** `lines 56-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:28:46.833043+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cytoplasm, P-body {ECO:0000269|PubMed:30535195}.
```

Source SHA-256: `e832e85da73e8a1dac05b9fac1aca7862c0ad15ede95319cb354b3e45fe3fb4e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MZ21?format=txt&versions=55)  
**Locator:** `lines 81-81`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:28:46.833043+00:00.  

```text
DR   GO; GO:0005829; C:cytosol; ISS:PAMGO_MGG.
```

Source SHA-256: `e832e85da73e8a1dac05b9fac1aca7862c0ad15ede95319cb354b3e45fe3fb4e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MZ21?format=txt&versions=55)  
**Locator:** `lines 82-82`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-02T04:28:46.833043+00:00.  

```text
DR   GO; GO:0005634; C:nucleus; ISS:PAMGO_MGG.
```

Source SHA-256: `e832e85da73e8a1dac05b9fac1aca7862c0ad15ede95319cb354b3e45fe3fb4e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 127. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
