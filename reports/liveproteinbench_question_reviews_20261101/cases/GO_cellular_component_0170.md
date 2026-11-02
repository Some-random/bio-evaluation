# GO_cellular_component_0170

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — plasma membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MIIDLFQSKKLIISIIILILRISLFSCAEHLFFNNNFNFFNFSENNHAKVNELNIDTKYLYQGLRNINIYLALSALNGITKEKINDISQWNGYKTRNNDETNISNVVVTEWKQLNKKSFFLKNNNISNNDNLIKGMPNPYFINSLTEDINNINLYFNIRNDIKYGEIIYKGTYIPHIYNNIFLIFLISYMYWFCIKILFNGYIKGKYVAKEYILKISTLFIFFVILKISLIFLPAILSCIVCLILTFYFYSISMSPCKDIFYLFESTRIKKEPIGWIIIVYAESILIGNVIYNFLCPPKIIIIFIRYIQNDFLVKIICLTIILFISFLIFFLMISNIFPAKKAQNFVFSFTSSYLIVSCFAYFWNIFLLRFLNNTNIFQIEPIMFFSYTPKFVFNRQNMFALFMIFAMSILSIIFPRIKKLKQNIFDMKENIYDSDIDIGKASKNRYNIILNYFT

[Multiple Choices]
A. rhoptry
B. vacuolar membrane
C. spindle
D. plasma membrane
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

> The exact sequence matches UniProt Pbs54. Its curated subcellular-location annotation, citing experimental evidence, reports plasma-membrane localization in female gametes and ookinetes. This supports D, though localization varies by developmental stage.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic sequence supports that this is a multipass membrane protein, making a membrane location more plausible than spindle or rhoptry. That does not distinguish the plasma membrane from the vacuolar membrane.


**Missing item-specific fact**

> The protein-specific localization evidence that Pbs54 is found at the plasma membrane in particular Plasmodium developmental stages.


**Reason**

> The input sequence supports membrane association but does not supply a clear signal that identifies which membrane. Selecting D over B therefore depends on an item-specific localization fact absent from the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports plasma-membrane localization, but the protein also localizes to flagella and residual body in male gametes. The question does not specify a developmental stage or define what counts as the primary location; neither alternative membrane option is supported by the supplied evidence.


### Important caveats

- The experimental annotation is stage-specific; the evidence does not establish plasma membrane as the sole or universally primary location.
- The GO plasma-membrane cross-reference is computationally assigned, whereas the cited subcellular-location annotation carries experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic sequence supports that this is a multipass membrane protein, making a membrane location more plausible than spindle or rhoptry. That does not distinguish the plasma membrane from the vacuolar membrane.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization evidence that Pbs54 is found at the plasma membrane in particular Plasmodium developmental stages.",
    "reason": "The input sequence supports membrane association but does not supply a clear signal that identifies which membrane. Selecting D over B therefore depends on an item-specific localization fact absent from the question."
  },
  "case_id": "GO_cellular_component_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt Pbs54. Its curated subcellular-location annotation, citing experimental evidence, reports plasma-membrane localization in female gametes and ookinetes. This supports D, though localization varies by developmental stage."
  },
  "important_caveats": [
    "The experimental annotation is stage-specific; the evidence does not establish plasma membrane as the sole or universally primary location.",
    "The GO plasma-membrane cross-reference is computationally assigned, whereas the cited subcellular-location annotation carries experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports plasma-membrane localization, but the protein also localizes to flagella and residual body in male gametes. The question does not specify a developmental stage or define what counts as the primary location; neither alternative membrane option is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt Pbs54. Its curated subcellular-location annotation, citing experimental evidence, reports plasma-membrane localization in female gametes and ookinetes. This supports D, though localization varies by developmental stage.",
    "evidence_ids": ["C1", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic sequence supports that this is a multipass membrane protein, making a membrane location more plausible than spindle or rhoptry. That does not distinguish the plasma membrane from the vacuolar membrane.",
    "missing_item_specific_fact": "The protein-specific localization evidence that Pbs54 is found at the plasma membrane in particular Plasmodium developmental stages.",
    "reason": "The input sequence supports membrane association but does not supply a clear signal that identifies which membrane. Selecting D over B therefore depends on an item-specific localization fact absent from the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports plasma-membrane localization, but the protein also localizes to flagella and residual body in male gametes. The question does not specify a developmental stage or define what counts as the primary location; neither alternative membrane option is supported by the supplied evidence."
  },
  "important_caveats": [
    "The experimental annotation is stage-specific; the evidence does not establish plasma membrane as the sole or universally primary location.",
    "The GO plasma-membrane cross-reference is computationally assigned, whereas the cited subcellular-location annotation carries experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A509AKT6 (Pbs54, Plasmodium berghei) annotates the protein as a multi-pass membrane protein at the cell membrane, with experimental evidence (ECO:0000269, PubMed:37774810) showing localization to the plasma membrane in female gametes and ookinetes. GO:0005886 (plasma membrane) is cross-referenced. The protein also localizes to flagella in male gametes, but among the four given choices (rhoptry, vacuolar membrane, spindle, plasma membrane), plasma membrane is the only one matching the annotated experimental localization.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5), [C8](#evidence-c8), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a signal peptide at the N-terminus (MIIDLFQSKKLIISIIILILRISLFSCAEHLF…) followed by numerous long hydrophobic stretches (e.g., ILFNGYIKGKYVAKEYILKISTLFIFFVILKISLIFLPAILSCIVCLILTFYFYSISMSPCKDIF…, IIIVYAESILIGNVIYNFLCPPKIIIIFIRYIQNDFLVKIICLTIILFISFLIFFLMISNIFPAKKAQNFVFSFTSSYLIVSCFAYFWNIFLLRFLNNTNIFQIEPIMFFSYTPKFVFNRQNMFALFMIFAMSILSIIFPRIKKLKQ), consistent with a multi-pass transmembrane protein. This topology rules out spindle (a microtubule-associated structure, not a membrane compartment) and makes rhoptry unlikely (rhoptry contents are predominantly soluble secreted proteins; while rhoptry membrane proteins exist, they are far less common). Between plasma membrane and vacuolar membrane, the general cell-biological principle is that signal-peptide-containing multi-pass membrane proteins are most commonly targeted to the plasma membrane rather than an internal vacuolar membrane. The overall extreme hydrophobicity and multi-pass architecture are most parsimoniously explained by a cell-surface membrane protein.


**Missing item-specific fact**

> None critical. The distinction between plasma membrane and vacuolar membrane from sequence alone is not perfectly clean, but the multi-pass TM + signal peptide architecture provides a defensible general-biology argument favoring plasma membrane over vacuolar membrane.


**Reason**

> The sequence features (signal peptide, multiple long TM helices, extreme hydrophobicity) provide concrete grounds to identify a membrane compartment and, by general biological reasoning about multi-pass membrane protein targeting, to favor plasma membrane over the other three options. Spindle and rhoptry are eliminable through structural/functional reasoning. The remaining ambiguity between plasma membrane and vacuolar membrane is resolved by the general principle that signal-peptide multi-pass membrane proteins are predominantly cell-surface proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Spindle is clearly incompatible with a multi-pass membrane protein. Rhoptry is unlikely given the multi-pass TM architecture (rhoptry contents are mainly soluble). Vacuolar membrane is a theoretical possibility for a membrane protein but is less consistent with the signal-peptide + multi-pass TM targeting pattern than plasma membrane. Only plasma membrane is fully consistent with all sequence features and general targeting principles.


### Important caveats

- The protein also localizes to flagella/cilium in male gametes (UniProt SL-0117), but 'flagellum' or 'cilium' is not among the four choices, so this does not create ambiguity within the given options.
- The GO annotation for plasma membrane is IEA:UniProtKB-SubCell (inferred from UniProt subcellular location), which traces back to experimental evidence (ECO:0000269, PubMed:37774810). The underlying experimental data is from a 2024 paper; the exact author data-construction snapshot is unknown.
- The distinction between plasma membrane and vacuolar membrane from sequence alone relies on a general targeting principle rather than a hard sequence determinant; a trained membrane-protein predictor would likely classify this as plasma membrane but could in principle assign it to another membrane compartment.
- The protein name 'Membrane protein Pbs54' and its role in gamete fertilization (plasma membrane fusion events) further support plasma membrane, but this context is not available to the evaluated model from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a signal peptide at the N-terminus (MIIDLFQSKKLIISIIILILRISLFSCAEHLF…) followed by numerous long hydrophobic stretches (e.g., ILFNGYIKGKYVAKEYILKISTLFIFFVILKISLIFLPAILSCIVCLILTFYFYSISMSPCKDIF…, IIIVYAESILIGNVIYNFLCPPKIIIIFIRYIQNDFLVKIICLTIILFISFLIFFLMISNIFPAKKAQNFVFSFTSSYLIVSCFAYFWNIFLLRFLNNTNIFQIEPIMFFSYTPKFVFNRQNMFALFMIFAMSILSIIFPRIKKLKQ), consistent with a multi-pass transmembrane protein. This topology rules out spindle (a microtubule-associated structure, not a membrane compartment) and makes rhoptry unlikely (rhoptry contents are predominantly soluble secreted proteins; while rhoptry membrane proteins exist, they are far less common). Between plasma membrane and vacuolar membrane, the general cell-biological principle is that signal-peptide-containing multi-pass membrane proteins are most commonly targeted to the plasma membrane rather than an internal vacuolar membrane. The overall extreme hydrophobicity and multi-pass architecture are most parsimoniously explained by a cell-surface membrane protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The distinction between plasma membrane and vacuolar membrane from sequence alone is not perfectly clean, but the multi-pass TM + signal peptide architecture provides a defensible general-biology argument favoring plasma membrane over vacuolar membrane.",
    "reason": "The sequence features (signal peptide, multiple long TM helices, extreme hydrophobicity) provide concrete grounds to identify a membrane compartment and, by general biological reasoning about multi-pass membrane protein targeting, to favor plasma membrane over the other three options. Spindle and rhoptry are eliminable through structural/functional reasoning. The remaining ambiguity between plasma membrane and vacuolar membrane is resolved by the general principle that signal-peptide multi-pass membrane proteins are predominantly cell-surface proteins."
  },
  "case_id": "GO_cellular_component_0170",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5",
      "C8",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A509AKT6 (Pbs54, Plasmodium berghei) annotates the protein as a multi-pass membrane protein at the cell membrane, with experimental evidence (ECO:0000269, PubMed:37774810) showing localization to the plasma membrane in female gametes and ookinetes. GO:0005886 (plasma membrane) is cross-referenced. The protein also localizes to flagella in male gametes, but among the four given choices (rhoptry, vacuolar membrane, spindle, plasma membrane), plasma membrane is the only one matching the annotated experimental localization."
  },
  "important_caveats": [
    "The protein also localizes to flagella/cilium in male gametes (UniProt SL-0117), but 'flagellum' or 'cilium' is not among the four choices, so this does not create ambiguity within the given options.",
    "The GO annotation for plasma membrane is IEA:UniProtKB-SubCell (inferred from UniProt subcellular location), which traces back to experimental evidence (ECO:0000269, PubMed:37774810). The underlying experimental data is from a 2024 paper; the exact author data-construction snapshot is unknown.",
    "The distinction between plasma membrane and vacuolar membrane from sequence alone relies on a general targeting principle rather than a hard sequence determinant; a trained membrane-protein predictor would likely classify this as plasma membrane but could in principle assign it to another membrane compartment.",
    "The protein name 'Membrane protein Pbs54' and its role in gamete fertilization (plasma membrane fusion events) further support plasma membrane, but this context is not available to the evaluated model from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Spindle is clearly incompatible with a multi-pass membrane protein. Rhoptry is unlikely given the multi-pass TM architecture (rhoptry contents are mainly soluble). Vacuolar membrane is a theoretical possibility for a membrane protein but is less consistent with the signal-peptide + multi-pass TM targeting pattern than plasma membrane. Only plasma membrane is fully consistent with all sequence features and general targeting principles."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0170",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A509AKT6 (Pbs54, Plasmodium berghei) annotates the protein as a multi-pass membrane protein at the cell membrane, with experimental evidence (ECO:0000269, PubMed:37774810) showing localization to the plasma membrane in female gametes and ookinetes. GO:0005886 (plasma membrane) is cross-referenced. The protein also localizes to flagella in male gametes, but among the four given choices (rhoptry, vacuolar membrane, spindle, plasma membrane), plasma membrane is the only one matching the annotated experimental localization.",
    "evidence_ids": ["C5", "C7", "H3", "H5", "C8", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a signal peptide at the N-terminus (MIIDLFQSKKLIISIIILILRISLFSCAEHLF…) followed by numerous long hydrophobic stretches (e.g., ILFNGYIKGKYVAKEYILKISTLFIFFVILKISLIFLPAILSCIVCLILTFYFYSISMSPCKDIF…, IIIVYAESILIGNVIYNFLCPPKIIIIFIRYIQNDFLVKIICLTIILFISFLIFFLMISNIFPAKKAQNFVFSFTSSYLIVSCFAYFWNIFLLRFLNNTNIFQIEPIMFFSYTPKFVFNRQNMFALFMIFAMSILSIIFPRIKKLKQ), consistent with a multi-pass transmembrane protein. This topology rules out spindle (a microtubule-associated structure, not a membrane compartment) and makes rhoptry unlikely (rhoptry contents are predominantly soluble secreted proteins; while rhoptry membrane proteins exist, they are far less common). Between plasma membrane and vacuolar membrane, the general cell-biological principle is that signal-peptide-containing multi-pass membrane proteins are most commonly targeted to the plasma membrane rather than an internal vacuolar membrane. The overall extreme hydrophobicity and multi-pass architecture are most parsimoniously explained by a cell-surface membrane protein.",
    "missing_item_specific_fact": "None critical. The distinction between plasma membrane and vacuolar membrane from sequence alone is not perfectly clean, but the multi-pass TM + signal peptide architecture provides a defensible general-biology argument favoring plasma membrane over vacuolar membrane.",
    "reason": "The sequence features (signal peptide, multiple long TM helices, extreme hydrophobicity) provide concrete grounds to identify a membrane compartment and, by general biological reasoning about multi-pass membrane protein targeting, to favor plasma membrane over the other three options. Spindle and rhoptry are eliminable through structural/functional reasoning. The remaining ambiguity between plasma membrane and vacuolar membrane is resolved by the general principle that signal-peptide multi-pass membrane proteins are predominantly cell-surface proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Spindle is clearly incompatible with a multi-pass membrane protein. Rhoptry is unlikely given the multi-pass TM architecture (rhoptry contents are mainly soluble). Vacuolar membrane is a theoretical possibility for a membrane protein but is less consistent with the signal-peptide + multi-pass TM targeting pattern than plasma membrane. Only plasma membrane is fully consistent with all sequence features and general targeting principles."
  },
  "important_caveats": [
    "The protein also localizes to flagella/cilium in male gametes (UniProt SL-0117), but 'flagellum' or 'cilium' is not among the four choices, so this does not create ambiguity within the given options.",
    "The GO annotation for plasma membrane is IEA:UniProtKB-SubCell (inferred from UniProt subcellular location), which traces back to experimental evidence (ECO:0000269, PubMed:37774810). The underlying experimental data is from a 2024 paper; the exact author data-construction snapshot is unknown.",
    "The distinction between plasma membrane and vacuolar membrane from sequence alone relies on a general targeting principle rather than a hard sequence determinant; a trained membrane-protein predictor would likely classify this as plasma membrane but could in principle assign it to another membrane compartment.",
    "The protein name 'Membrane protein Pbs54' and its role in gamete fertilization (plasma membrane fusion events) further support plasma membrane, but this context is not available to the evaluated model from the sequence alone."
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

**Accession:** `A0A509AKT6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.898557+00:00.  

```json
"A0A509AKT6"
```

Source SHA-256: `5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.898557+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"37774810","source":"PubMed"}],"value":"In male gametes, localizes to the flagella and residual body; in female gametes, localizes to the plasma membrane. In ookinetes, localizes to the plasma membrane"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"37774810","source":"PubMed"}],"id":"SL-0117","value":"Cell projection, cilium, flagellum"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"37774810","source":"PubMed"}],"id":"SL-0039","value":"Cell membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.898557+00:00.  

```json
{"database":"GO","id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-SubCell"}]}
```

Source SHA-256: `5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A509AKT6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:23.898557+00:00.  

```json
{"citation":{"authors":["Pang W.","Bai J.","Zhu L.","Liu F.","Wu Y.","Yang F.","Zheng L.","Liu P.","Zhang Y.","Wang M.","Li J.","Zhu X.","Cui L.","Cao Y."],"citationCrossReferences":[{"database":"PubMed","id":"37774810"},{"database":"DOI","id":"10.1016/j.ijpara.2023.08.003"}],"citationType":"journal article","firstPage":"99","id":"37774810","journal":"Int. J. Parasitol.","lastPage":"107","publicationDate":"2024","title":"Functional characterization of a conserved membrane protein, Pbs54, involved in gamete fertilization in Plasmodium berghei.","volume":"54"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","DEVELOPMENTAL STAGE","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `5f12f41d692d932165f3b4e32653a23e5a692f941e64b936309ea1b6a4bbad25`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 25-33`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION
RP   PHENOTYPE.
RX   PubMed=37774810; DOI=10.1016/j.ijpara.2023.08.003;
RA   Pang W., Bai J., Zhu L., Liu F., Wu Y., Yang F., Zheng L., Liu P.,
RA   Zhang Y., Wang M., Li J., Zhu X., Cui L., Cao Y.;
RT   "Functional characterization of a conserved membrane protein, Pbs54,
RT   involved in gamete fertilization in Plasmodium berghei.";
RL   Int. J. Parasitol. 54:99-107(2024).
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 37-43`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell projection, cilium, flagellum
CC       {ECO:0000269|PubMed:37774810}. Cell membrane
CC       {ECO:0000269|PubMed:37774810}; Multi-pass membrane protein
CC       {ECO:0000255}. Note=In male gametes, localizes to the flagella and
CC       residual body; in female gametes, localizes to the plasma membrane. In
CC       ookinetes, localizes to the plasma membrane.
CC       {ECO:0000269|PubMed:37774810}.
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A509AKT6?format=txt&versions=19)  
**Locator:** `lines 75-75`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:25:27.030552+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `6d40908ee73c41ed5a2c9670ef889cabc4ff6bd15769a8b8824958da5cb4a8f5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 170. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
