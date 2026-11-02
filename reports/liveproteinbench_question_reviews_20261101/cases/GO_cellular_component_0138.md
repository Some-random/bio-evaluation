# GO_cellular_component_0138

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — cytosolic large ribosomal subunit

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAFHKLVKNSAYYSRFQTKFKRRRQGKTDYYARKRLITQAKNKYNAPKYRLVVRFTNRDIITQMVTSEINGDKIFAAAYSHELRAYGINHGLTNWAAAYATGLLLARRVLAKLGLDKTFTGVEEPNGEYTLTEAAETEDGERRPFKAILDVGLARTSTGARVFGVMKGASDGGIFIPHSENRFPGYDIETEELDTEVLKKYIYGGHVAEYMETLADDDEERYKSQFVKYIEDDVEADSLEELYAEAHKQIRADPFRKYVSDAPKKSKEEWKAESLKYKKAKLSREERKARVEAKIKQLLAEQDE

[Multiple Choices]
A. perikaryon
B. nuclear pore nuclear basket
C. extracellular space
D. cytosolic large ribosomal subunit
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

> The exact sequence matches a UniProt entry identifying the protein as large ribosomal subunit protein uL18/60S ribosomal protein L5. The entry places it in the cytoplasm and annotates it to the cytosolic large ribosomal subunit. The GO annotation is computational (IEA:TreeGrafter), while the cited structural study provides supporting ribosomal-complex context; the evidence supports D but does not make the GO annotation itself a direct experimental localization measurement.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The basic N-terminal region and lack of an obvious secretion signal are consistent with an intracellular protein, but do not specifically distinguish a ribosomal subunit protein from other intracellular options. Choosing D requires identifying the particular protein as uL18/L5 or otherwise knowing its ribosomal annotation.


**Missing item-specific fact**

> The protein-specific identity and association with the cytosolic large ribosomal subunit are not supplied in the question.


**Reason**

> General sequence-level clues can weakly favor an intracellular, potentially RNA-associated protein, but they do not establish the precise cellular component among the relevant alternatives. Exact-sequence recognition or an external protein-specific annotation is needed.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports D. The other options are not comparably supported as the protein's primary location; broad intracellular sequence clues alone would not resolve the answer, but that is a lookup-dependence issue rather than evidence that multiple choices are equally defensible.


### Important caveats

- The sequence match is exact, but the accession and database evidence were reviewer-only and absent from the evaluated input.
- The cytosolic large ribosomal subunit GO annotation is computationally assigned; the cited structural evidence concerns a ribosomal assembly complex and should not be conflated with a direct localization assay.
- The exact source snapshot used by the author is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The basic N-terminal region and lack of an obvious secretion signal are consistent with an intracellular protein, but do not specifically distinguish a ribosomal subunit protein from other intracellular options. Choosing D requires identifying the particular protein as uL18/L5 or otherwise knowing its ribosomal annotation.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and association with the cytosolic large ribosomal subunit are not supplied in the question.",
    "reason": "General sequence-level clues can weakly favor an intracellular, potentially RNA-associated protein, but they do not establish the precise cellular component among the relevant alternatives. Exact-sequence recognition or an external protein-specific annotation is needed."
  },
  "case_id": "GO_cellular_component_0138",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry identifying the protein as large ribosomal subunit protein uL18/60S ribosomal protein L5. The entry places it in the cytoplasm and annotates it to the cytosolic large ribosomal subunit. The GO annotation is computational (IEA:TreeGrafter), while the cited structural study provides supporting ribosomal-complex context; the evidence supports D but does not make the GO annotation itself a direct experimental localization measurement."
  },
  "important_caveats": [
    "The sequence match is exact, but the accession and database evidence were reviewer-only and absent from the evaluated input.",
    "The cytosolic large ribosomal subunit GO annotation is computationally assigned; the cited structural evidence concerns a ribosomal assembly complex and should not be conflated with a direct localization assay.",
    "The exact source snapshot used by the author is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D. The other options are not comparably supported as the protein's primary location; broad intracellular sequence clues alone would not resolve the answer, but that is a lookup-dependence issue rather than evidence that multiple choices are equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0138",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry identifying the protein as large ribosomal subunit protein uL18/60S ribosomal protein L5. The entry places it in the cytoplasm and annotates it to the cytosolic large ribosomal subunit. The GO annotation is computational (IEA:TreeGrafter), while the cited structural study provides supporting ribosomal-complex context; the evidence supports D but does not make the GO annotation itself a direct experimental localization measurement.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The basic N-terminal region and lack of an obvious secretion signal are consistent with an intracellular protein, but do not specifically distinguish a ribosomal subunit protein from other intracellular options. Choosing D requires identifying the particular protein as uL18/L5 or otherwise knowing its ribosomal annotation.",
    "missing_item_specific_fact": "The protein-specific identity and association with the cytosolic large ribosomal subunit are not supplied in the question.",
    "reason": "General sequence-level clues can weakly favor an intracellular, potentially RNA-associated protein, but they do not establish the precise cellular component among the relevant alternatives. Exact-sequence recognition or an external protein-specific annotation is needed."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports D. The other options are not comparably supported as the protein's primary location; broad intracellular sequence clues alone would not resolve the answer, but that is a lookup-dependence issue rather than evidence that multiple choices are equally defensible."
  },
  "important_caveats": [
    "The sequence match is exact, but the accession and database evidence were reviewer-only and absent from the evaluated input.",
    "The cytosolic large ribosomal subunit GO annotation is computationally assigned; the cited structural evidence concerns a ribosomal assembly complex and should not be conflated with a direct localization assay.",
    "The exact source snapshot used by the author is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt G0SEG2 (RL5_CHATD), annotated as 'Large ribosomal subunit protein uL18' (alt. 60S ribosomal protein L5). GO:0022625 'cytosolic large ribosomal subunit' is annotated (IEA:TreeGrafter), and the protein's identity as a 60S ribosomal protein is corroborated by PDB structure 7OZS (in complex with RPL11, RRS1, RPF2, SYO1, and 5S RNA) and PubMed:37291423. The UniProt subcellular location is 'Cytoplasm,' consistent with cytosolic ribosome membership. The expected answer D is scientifically supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal ~80 residues contain dense clusters of basic residues (FKRRR, RK, AK, KY, AR, RVLAKL) characteristic of the RNA-binding N-terminal domain found in ribosomal proteins. The overall length (304 aa) is consistent with ribosomal protein size. No N-terminal hydrophobic signal peptide is present, ruling out extracellular secretion (C). No nuclear localization signal or nuclear-basket protein architecture (e.g., coiled-coil Tpr/Mlp-like domains) is evident, making nuclear pore nuclear basket (B) unlikely. The perikaryon (A) is a highly specific neuronal cell-body term (GO:0043204: 'portion of the cell soma that excludes the nucleus'), inapplicable to a ribosomal protein and to any non-neuronal organism. The combination of small size, basic RNA-binding N-terminus, and absence of compartment-specific targeting signals points to a cytosolic ribosomal protein, and since only 'large ribosomal subunit' is offered among the choices, D is the best answer.


**Missing item-specific fact**

> Precise distinction between large (60S) and small (40S) ribosomal subunit membership from sequence alone would require structural or database knowledge; however, only 'large' is offered as an option, mitigating this gap.


**Reason**

> The basic N-terminal RNA-binding region, small protein size, and absence of signal peptides or nuclear targeting motifs provide a concrete biological argument that distinguishes D from A, B, and C without requiring memorization of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent highly distinct cellular compartments (neuronal cell body, nuclear basket, extracellular, cytosolic ribosome). The sequence features (basic N-terminal RNA-binding region, no signal peptide, no NLS) meaningfully favor D. Perikaryon is a neuronal-specific term inapplicable to a ribosomal protein. No other option is defensible given the sequence characteristics.


### Important caveats

- The GO annotation for cytosolic large ribosomal subunit (GO:0022625) carries evidence code IEA:TreeGrafter (computational), not direct experimental GO annotation. However, the protein's identity as a 60S ribosomal protein is well-supported by PDB structures and literature.
- The model does not receive organism information; the perikaryon distractor (a neuronal-specific term) is trivially eliminated for a fungal protein but requires the model to either recognize the term's specificity or rely on sequence features.
- The specific assignment to 'large' vs 'small' ribosomal subunit is not derivable from primary sequence features alone; the question is mitigated by offering only 'large' as the ribosomal option.
- The UniProt entry was first public on 2025-02-05; the benchmark's author source snapshot is unknown, though sequence match is confirmed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal ~80 residues contain dense clusters of basic residues (FKRRR, RK, AK, KY, AR, RVLAKL) characteristic of the RNA-binding N-terminal domain found in ribosomal proteins. The overall length (304 aa) is consistent with ribosomal protein size. No N-terminal hydrophobic signal peptide is present, ruling out extracellular secretion (C). No nuclear localization signal or nuclear-basket protein architecture (e.g., coiled-coil Tpr/Mlp-like domains) is evident, making nuclear pore nuclear basket (B) unlikely. The perikaryon (A) is a highly specific neuronal cell-body term (GO:0043204: 'portion of the cell soma that excludes the nucleus'), inapplicable to a ribosomal protein and to any non-neuronal organism. The combination of small size, basic RNA-binding N-terminus, and absence of compartment-specific targeting signals points to a cytosolic ribosomal protein, and since only 'large ribosomal subunit' is offered among the choices, D is the best answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise distinction between large (60S) and small (40S) ribosomal subunit membership from sequence alone would require structural or database knowledge; however, only 'large' is offered as an option, mitigating this gap.",
    "reason": "The basic N-terminal RNA-binding region, small protein size, and absence of signal peptides or nuclear targeting motifs provide a concrete biological argument that distinguishes D from A, B, and C without requiring memorization of this specific protein's database entry."
  },
  "case_id": "GO_cellular_component_0138",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt G0SEG2 (RL5_CHATD), annotated as 'Large ribosomal subunit protein uL18' (alt. 60S ribosomal protein L5). GO:0022625 'cytosolic large ribosomal subunit' is annotated (IEA:TreeGrafter), and the protein's identity as a 60S ribosomal protein is corroborated by PDB structure 7OZS (in complex with RPL11, RRS1, RPF2, SYO1, and 5S RNA) and PubMed:37291423. The UniProt subcellular location is 'Cytoplasm,' consistent with cytosolic ribosome membership. The expected answer D is scientifically supported."
  },
  "important_caveats": [
    "The GO annotation for cytosolic large ribosomal subunit (GO:0022625) carries evidence code IEA:TreeGrafter (computational), not direct experimental GO annotation. However, the protein's identity as a 60S ribosomal protein is well-supported by PDB structures and literature.",
    "The model does not receive organism information; the perikaryon distractor (a neuronal-specific term) is trivially eliminated for a fungal protein but requires the model to either recognize the term's specificity or rely on sequence features.",
    "The specific assignment to 'large' vs 'small' ribosomal subunit is not derivable from primary sequence features alone; the question is mitigated by offering only 'large' as the ribosomal option.",
    "The UniProt entry was first public on 2025-02-05; the benchmark's author source snapshot is unknown, though sequence match is confirmed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct cellular compartments (neuronal cell body, nuclear basket, extracellular, cytosolic ribosome). The sequence features (basic N-terminal RNA-binding region, no signal peptide, no NLS) meaningfully favor D. Perikaryon is a neuronal-specific term inapplicable to a ribosomal protein. No other option is defensible given the sequence characteristics."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0138",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt G0SEG2 (RL5_CHATD), annotated as 'Large ribosomal subunit protein uL18' (alt. 60S ribosomal protein L5). GO:0022625 'cytosolic large ribosomal subunit' is annotated (IEA:TreeGrafter), and the protein's identity as a 60S ribosomal protein is corroborated by PDB structure 7OZS (in complex with RPL11, RRS1, RPF2, SYO1, and 5S RNA) and PubMed:37291423. The UniProt subcellular location is 'Cytoplasm,' consistent with cytosolic ribosome membership. The expected answer D is scientifically supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal ~80 residues contain dense clusters of basic residues (FKRRR, RK, AK, KY, AR, RVLAKL) characteristic of the RNA-binding N-terminal domain found in ribosomal proteins. The overall length (304 aa) is consistent with ribosomal protein size. No N-terminal hydrophobic signal peptide is present, ruling out extracellular secretion (C). No nuclear localization signal or nuclear-basket protein architecture (e.g., coiled-coil Tpr/Mlp-like domains) is evident, making nuclear pore nuclear basket (B) unlikely. The perikaryon (A) is a highly specific neuronal cell-body term (GO:0043204: 'portion of the cell soma that excludes the nucleus'), inapplicable to a ribosomal protein and to any non-neuronal organism. The combination of small size, basic RNA-binding N-terminus, and absence of compartment-specific targeting signals points to a cytosolic ribosomal protein, and since only 'large ribosomal subunit' is offered among the choices, D is the best answer.",
    "missing_item_specific_fact": "Precise distinction between large (60S) and small (40S) ribosomal subunit membership from sequence alone would require structural or database knowledge; however, only 'large' is offered as an option, mitigating this gap.",
    "reason": "The basic N-terminal RNA-binding region, small protein size, and absence of signal peptides or nuclear targeting motifs provide a concrete biological argument that distinguishes D from A, B, and C without requiring memorization of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent highly distinct cellular compartments (neuronal cell body, nuclear basket, extracellular, cytosolic ribosome). The sequence features (basic N-terminal RNA-binding region, no signal peptide, no NLS) meaningfully favor D. Perikaryon is a neuronal-specific term inapplicable to a ribosomal protein. No other option is defensible given the sequence characteristics."
  },
  "important_caveats": [
    "The GO annotation for cytosolic large ribosomal subunit (GO:0022625) carries evidence code IEA:TreeGrafter (computational), not direct experimental GO annotation. However, the protein's identity as a 60S ribosomal protein is well-supported by PDB structures and literature.",
    "The model does not receive organism information; the perikaryon distractor (a neuronal-specific term) is trivially eliminated for a fungal protein but requires the model to either recognize the term's specificity or rely on sequence features.",
    "The specific assignment to 'large' vs 'small' ribosomal subunit is not derivable from primary sequence features alone; the question is mitigated by offering only 'large' as the ribosomal option.",
    "The UniProt entry was first public on 2025-02-05; the benchmark's author source snapshot is unknown, though sequence match is confirmed."
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

**Accession:** `G0SEG2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 56. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SEG2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:25.225490+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"37291423","source":"PubMed"}],"value":"60S ribosomal protein L5"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"37291423","source":"PubMed"}],"value":"ctRPL5"}]}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305","id":"37291423","source":"PubMed"}],"value":"Large ribosomal subunit protein uL18"}}}
```

Source SHA-256: `e52661008777f00d9958563cec58f7858295fc04f9c1711da6ec03a5d3c5a023`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SEG2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:25.225490+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"37291423","source":"PubMed"}],"id":"SL-0086","value":"Cytoplasm"}}]}
```

Source SHA-256: `e52661008777f00d9958563cec58f7858295fc04f9c1711da6ec03a5d3c5a023`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SEG2.json)  
**Locator:** `/uniProtKBCrossReferences/74`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:25.225490+00:00.  

```json
{"database":"GO","id":"GO:0022625","properties":[{"key":"GoTerm","value":"C:cytosolic large ribosomal subunit"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `e52661008777f00d9958563cec58f7858295fc04f9c1711da6ec03a5d3c5a023`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0SEG2.json)  
**Locator:** `/references/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:28:25.225490+00:00.  

```json
{"citation":{"authors":["Castillo Duque de Estrada N.M.","Thoms M.","Flemming D.","Hammaren H.M.","Buschauer R.","Ameismeier M.","Bassler J.","Beck M.","Beckmann R.","Hurt E."],"citationCrossReferences":[{"database":"PubMed","id":"37291423"},{"database":"DOI","id":"10.1038/s41594-023-01006-7"}],"citationType":"journal article","firstPage":"1119","id":"37291423","journal":"Nat. Struct. Mol. Biol.","lastPage":"1131","publicationDate":"2023","title":"Structure of nascent 5S RNPs at the crossroad between ribosome assembly and MDM2-p53 pathways.","volume":"30"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7OZS","source":"PDB"}],"referenceNumber":8,"referencePositions":["STRUCTURE BY ELECTRON MICROSCOPY (3.50 ANGSTROMS) IN COMPLEX WITH RPL11; RRS1; RPF2; SYO1 AND 5S RNA","FUNCTION","SUBUNIT"]}
```

Source SHA-256: `e52661008777f00d9958563cec58f7858295fc04f9c1711da6ec03a5d3c5a023`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SEG2?format=txt&versions=56)  
**Locator:** `lines 71-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 56 / 1.  
**Retrieved:** 2026-11-02T04:28:28.823797+00:00.  

```text
RN   [8] {ECO:0007744|PDB:7OZS}
RP   STRUCTURE BY ELECTRON MICROSCOPY (3.50 ANGSTROMS) IN COMPLEX WITH RPL11;
RP   RRS1; RPF2; SYO1 AND 5S RNA, FUNCTION, AND SUBUNIT.
RX   PubMed=37291423; DOI=10.1038/s41594-023-01006-7;
RA   Castillo Duque de Estrada N.M., Thoms M., Flemming D., Hammaren H.M.,
RA   Buschauer R., Ameismeier M., Bassler J., Beck M., Beckmann R., Hurt E.;
RT   "Structure of nascent 5S RNPs at the crossroad between ribosome assembly
RT   and MDM2-p53 pathways.";
RL   Nat. Struct. Mol. Biol. 30:1119-1131(2023).
```

Source SHA-256: `de21ed9c5893dab95459cc199cc0c02ce4d43bb6a09f9dad35281a744e77edb9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SEG2?format=txt&versions=56)  
**Locator:** `lines 102-102`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 56 / 1.  
**Retrieved:** 2026-11-02T04:28:28.823797+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:37291423}.
```

Source SHA-256: `de21ed9c5893dab95459cc199cc0c02ce4d43bb6a09f9dad35281a744e77edb9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0SEG2?format=txt&versions=56)  
**Locator:** `lines 173-173`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 56 / 1.  
**Retrieved:** 2026-11-02T04:28:28.823797+00:00.  

```text
DR   GO; GO:0022625; C:cytosolic large ribosomal subunit; IEA:TreeGrafter.
```

Source SHA-256: `de21ed9c5893dab95459cc199cc0c02ce4d43bb6a09f9dad35281a744e77edb9`.

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 160556-160571`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0022625
name: cytosolic large ribosomal subunit
namespace: cellular_component
alt_id: GO:0005842
alt_id: GO:0009282
alt_id: GO:0030498
alt_id: GO:0030872
def: "The large subunit of a ribosome located in the cytosol." [GOC:mtg_sensu]
synonym: "50S ribosomal subunit" NARROW []
synonym: "60S ribosomal subunit" NARROW []
synonym: "eukaryotic ribosomal LSU" NARROW []
synonym: "prokaryotic large ribosomal subunit" NARROW []
is_a: GO:0015934 ! large ribosomal subunit
relationship: part_of GO:0022626 ! cytosolic ribosome

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 138. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
