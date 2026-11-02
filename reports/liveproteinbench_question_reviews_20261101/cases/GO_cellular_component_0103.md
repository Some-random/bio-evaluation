# GO_cellular_component_0103

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — cell outer membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAVFPLSAKHRKYALRALAVSIILVSAAYIASTEGTERVRPQRVEQKLPPLSWGGSGVQTAYWVQEAVQPGDSLADVLARSGMARDEIARITEKYGGEADLRHLRADQSVHVLVGGDGSAREVQFFTDEDGERNLVALEKKGGIWRRSASDADMKVLPTLRSVVVKTSARGSLARAEVPVEIRESLSGIFAGRFSLDGLKEGDAVRLLYDSLYFHGQQVAAGDILAAEVVKGGTTHQAFYYRSDKEGGGGGNYYDEDGRVLQEKGGFNIEPLVYTRISSPFGYRMHPILHTWRLHTGIDYAAPQGTPVRASADGVITFKGRKGGYGNAVMIRHANGVETLYAHLSAFSQAQGNVRGGEVIGFVGSTGRSTGPHLHYEARINGQPVNPVSVALPTPELTQADKAAFAAQKQKADALLARLRGIPVTVSQSD

[Multiple Choices]
A. host cell
B. centrosome
C. cell outer membrane
D. aggresome
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

> The exact sequence matches the UniProt entry, which assigns cell outer membrane localization. However, the annotation says the mature protein is probably associated with the outer membrane by similarity; it is not direct experimental localization evidence in the supplied excerpts.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic region is consistent with export from a bacterium, making the eukaryotic centrosome and aggresome poor fits. That signal alone does not distinguish an outer-membrane protein from one localized elsewhere after export.


**Missing item-specific fact**

> The protein-specific evidence that this sequence is Neisseria Mpg and that its mature form is associated with the cell outer membrane, an assignment available in database annotation but absent from the question input.


**Reason**

> General sequence reasoning can suggest export and disfavor some distractors, but it does not establish the precise outer-membrane localization over other possible destinations. Choosing C therefore depends on protein-specific annotation or knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied choices include several poor fits for a bacterial protein, but the sequence-based export signal does not itself establish a competing listed localization. The supported key is C, with the qualification that its annotation is probable and transferred by similarity.


### Important caveats

- The sequence match and localization annotation are reviewer-only evidence, not information supplied to the evaluated model.
- The cited GO annotation is inferred by sequence similarity (ISS); the excerpts do not establish direct experimental localization of this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic region is consistent with export from a bacterium, making the eukaryotic centrosome and aggresome poor fits. That signal alone does not distinguish an outer-membrane protein from one localized elsewhere after export.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific evidence that this sequence is Neisseria Mpg and that its mature form is associated with the cell outer membrane, an assignment available in database annotation but absent from the question input.",
    "reason": "General sequence reasoning can suggest export and disfavor some distractors, but it does not establish the precise outer-membrane localization over other possible destinations. Choosing C therefore depends on protein-specific annotation or knowledge."
  },
  "case_id": "GO_cellular_component_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which assigns cell outer membrane localization. However, the annotation says the mature protein is probably associated with the outer membrane by similarity; it is not direct experimental localization evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The sequence match and localization annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The cited GO annotation is inferred by sequence similarity (ISS); the excerpts do not establish direct experimental localization of this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied choices include several poor fits for a bacterial protein, but the sequence-based export signal does not itself establish a competing listed localization. The supported key is C, with the qualification that its annotation is probable and transferred by similarity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry, which assigns cell outer membrane localization. However, the annotation says the mature protein is probably associated with the outer membrane by similarity; it is not direct experimental localization evidence in the supplied excerpts.",
    "evidence_ids": ["C1", "C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic region is consistent with export from a bacterium, making the eukaryotic centrosome and aggresome poor fits. That signal alone does not distinguish an outer-membrane protein from one localized elsewhere after export.",
    "missing_item_specific_fact": "The protein-specific evidence that this sequence is Neisseria Mpg and that its mature form is associated with the cell outer membrane, an assignment available in database annotation but absent from the question input.",
    "reason": "General sequence reasoning can suggest export and disfavor some distractors, but it does not establish the precise outer-membrane localization over other possible destinations. Choosing C therefore depends on protein-specific annotation or knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied choices include several poor fits for a bacterial protein, but the sequence-based export signal does not itself establish a competing listed localization. The supported key is C, with the qualification that its annotation is probable and transferred by similarity."
  },
  "important_caveats": [
    "The sequence match and localization annotation are reviewer-only evidence, not information supplied to the evaluated model.",
    "The cited GO annotation is inferred by sequence similarity (ISS); the excerpts do not establish direct experimental localization of this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry Q5F676 (MPG_NEIG1, 430 AA, sequence matched) annotates the subcellular location as 'Cell outer membrane' (SL-0040) with evidence code ECO:0000250 (similarity to E0N688) and ECO:0000305 (curator). The GO cross-reference GO:0009279 (C:cell outer membrane) is annotated with ISS/IEA. The protein is a DD-carboxypeptidase/endopeptidase from Neisseria gonorrhoeae (Gram-negative bacterium) with an N-terminal signal peptide, consistent with outer membrane association. The annotation is by similarity rather than direct experimental localization for this specific protein, but it is the explicit database annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6), [C4](#evidence-c4), [C3](#evidence-c3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'MAVFPLSAKHRKYALRALAVSIILVSAAYIAST' contains a clear hydrophobic signal peptide (ALAVSIILVSAAYIAST), indicating membrane targeting. The protein is bacterial (prokaryotic sequence features, ~430 AA peptidase architecture). In Gram-negative bacteria, signal peptides direct proteins to the outer membrane. 'Centrosome' (GO:0005813) and 'aggresome' (GO:0016235) are eukaryotic structures irrelevant to a bacterium. 'Host cell' (GO:0043657) refers to a cell within a host organism and is used for pathogen/viral proteins that enter host cells, not for a bacterium's own membrane-targeted peptidase. The combination of (1) observable signal peptide, (2) bacterial protein context, and (3) peptidase function acting on peptidoglycan provides a concrete biological argument for outer membrane localization over the alternatives.


**Missing item-specific fact**

> None strictly required. The signal peptide is directly observable in the sequence, and the biological principle (bacterial signal peptide → outer membrane) is general knowledge. Exact organism identification from sequence alone adds confidence but is not strictly necessary to eliminate the eukaryotic distractors and 'host cell.'


**Reason**

> A model can observe the N-terminal hydrophobic signal peptide, infer bacterial origin from sequence architecture, apply the general principle that Gram-negative bacterial signal peptides target the outer membrane, and eliminate centrosome/aggresome as eukaryotic structures and 'host cell' as inapplicable to a bacterium's own membrane protein. This constitutes a concrete biological reasoning chain rather than pure lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B (centrosome) and D (aggresome) are unambiguously eukaryotic structures and cannot apply to a bacterial protein. Option A (host cell) is a GO term for a cell within a host organism, inapplicable to a bacterium's own outer membrane protein. Only C (cell outer membrane) is consistent with a bacterial peptidase bearing an N-terminal signal peptide.


### Important caveats

- The UniProt annotation for subcellular location is by similarity (ISS/ECO:0000250), not direct experimental localization of this specific protein. The curator note states 'probably associated with the cell outer membrane.'
- The reviewer-only evidence identifies the protein as Q5F676 from Neisseria gonorrhoeae, but this accession and organism name were not provided to the evaluated model; the model must infer bacterial origin from sequence features alone.
- The GO annotation evidence code is IEA/ISS (inferred), not experimental (e.g., IDA, IPI), meaning the outer membrane localization is a computational/similarity-based assignment rather than a direct experimental measurement for this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'MAVFPLSAKHRKYALRALAVSIILVSAAYIAST' contains a clear hydrophobic signal peptide (ALAVSIILVSAAYIAST), indicating membrane targeting. The protein is bacterial (prokaryotic sequence features, ~430 AA peptidase architecture). In Gram-negative bacteria, signal peptides direct proteins to the outer membrane. 'Centrosome' (GO:0005813) and 'aggresome' (GO:0016235) are eukaryotic structures irrelevant to a bacterium. 'Host cell' (GO:0043657) refers to a cell within a host organism and is used for pathogen/viral proteins that enter host cells, not for a bacterium's own membrane-targeted peptidase. The combination of (1) observable signal peptide, (2) bacterial protein context, and (3) peptidase function acting on peptidoglycan provides a concrete biological argument for outer membrane localization over the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required. The signal peptide is directly observable in the sequence, and the biological principle (bacterial signal peptide → outer membrane) is general knowledge. Exact organism identification from sequence alone adds confidence but is not strictly necessary to eliminate the eukaryotic distractors and 'host cell.'",
    "reason": "A model can observe the N-terminal hydrophobic signal peptide, infer bacterial origin from sequence architecture, apply the general principle that Gram-negative bacterial signal peptides target the outer membrane, and eliminate centrosome/aggresome as eukaryotic structures and 'host cell' as inapplicable to a bacterium's own membrane protein. This constitutes a concrete biological reasoning chain rather than pure lookup."
  },
  "case_id": "GO_cellular_component_0103",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H5",
      "H6",
      "C4",
      "C3"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry Q5F676 (MPG_NEIG1, 430 AA, sequence matched) annotates the subcellular location as 'Cell outer membrane' (SL-0040) with evidence code ECO:0000250 (similarity to E0N688) and ECO:0000305 (curator). The GO cross-reference GO:0009279 (C:cell outer membrane) is annotated with ISS/IEA. The protein is a DD-carboxypeptidase/endopeptidase from Neisseria gonorrhoeae (Gram-negative bacterium) with an N-terminal signal peptide, consistent with outer membrane association. The annotation is by similarity rather than direct experimental localization for this specific protein, but it is the explicit database annotation."
  },
  "important_caveats": [
    "The UniProt annotation for subcellular location is by similarity (ISS/ECO:0000250), not direct experimental localization of this specific protein. The curator note states 'probably associated with the cell outer membrane.'",
    "The reviewer-only evidence identifies the protein as Q5F676 from Neisseria gonorrhoeae, but this accession and organism name were not provided to the evaluated model; the model must infer bacterial origin from sequence features alone.",
    "The GO annotation evidence code is IEA/ISS (inferred), not experimental (e.g., IDA, IPI), meaning the outer membrane localization is a computational/similarity-based assignment rather than a direct experimental measurement for this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (centrosome) and D (aggresome) are unambiguously eukaryotic structures and cannot apply to a bacterial protein. Option A (host cell) is a GO term for a cell within a host organism, inapplicable to a bacterium's own outer membrane protein. Only C (cell outer membrane) is consistent with a bacterial peptidase bearing an N-terminal signal peptide."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0103",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProtKB entry Q5F676 (MPG_NEIG1, 430 AA, sequence matched) annotates the subcellular location as 'Cell outer membrane' (SL-0040) with evidence code ECO:0000250 (similarity to E0N688) and ECO:0000305 (curator). The GO cross-reference GO:0009279 (C:cell outer membrane) is annotated with ISS/IEA. The protein is a DD-carboxypeptidase/endopeptidase from Neisseria gonorrhoeae (Gram-negative bacterium) with an N-terminal signal peptide, consistent with outer membrane association. The annotation is by similarity rather than direct experimental localization for this specific protein, but it is the explicit database annotation.",
    "evidence_ids": ["C5", "C6", "H5", "H6", "C4", "C3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'MAVFPLSAKHRKYALRALAVSIILVSAAYIAST' contains a clear hydrophobic signal peptide (ALAVSIILVSAAYIAST), indicating membrane targeting. The protein is bacterial (prokaryotic sequence features, ~430 AA peptidase architecture). In Gram-negative bacteria, signal peptides direct proteins to the outer membrane. 'Centrosome' (GO:0005813) and 'aggresome' (GO:0016235) are eukaryotic structures irrelevant to a bacterium. 'Host cell' (GO:0043657) refers to a cell within a host organism and is used for pathogen/viral proteins that enter host cells, not for a bacterium's own membrane-targeted peptidase. The combination of (1) observable signal peptide, (2) bacterial protein context, and (3) peptidase function acting on peptidoglycan provides a concrete biological argument for outer membrane localization over the alternatives.",
    "missing_item_specific_fact": "None strictly required. The signal peptide is directly observable in the sequence, and the biological principle (bacterial signal peptide → outer membrane) is general knowledge. Exact organism identification from sequence alone adds confidence but is not strictly necessary to eliminate the eukaryotic distractors and 'host cell.'",
    "reason": "A model can observe the N-terminal hydrophobic signal peptide, infer bacterial origin from sequence architecture, apply the general principle that Gram-negative bacterial signal peptides target the outer membrane, and eliminate centrosome/aggresome as eukaryotic structures and 'host cell' as inapplicable to a bacterium's own membrane protein. This constitutes a concrete biological reasoning chain rather than pure lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B (centrosome) and D (aggresome) are unambiguously eukaryotic structures and cannot apply to a bacterial protein. Option A (host cell) is a GO term for a cell within a host organism, inapplicable to a bacterium's own outer membrane protein. Only C (cell outer membrane) is consistent with a bacterial peptidase bearing an N-terminal signal peptide."
  },
  "important_caveats": [
    "The UniProt annotation for subcellular location is by similarity (ISS/ECO:0000250), not direct experimental localization of this specific protein. The curator note states 'probably associated with the cell outer membrane.'",
    "The reviewer-only evidence identifies the protein as Q5F676 from Neisseria gonorrhoeae, but this accession and organism name were not provided to the evaluated model; the model must infer bacterial origin from sequence features alone.",
    "The GO annotation evidence code is IEA/ISS (inferred), not experimental (e.g., IDA, IPI), meaning the outer membrane localization is a computational/similarity-based assignment rather than a direct experimental measurement for this protein."
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

**Accession:** `Q5F676` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 88. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:11.230902+00:00.  

```json
"Q5F676"
```

Source SHA-256: `fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec`.

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)  
**Locator:** `/organism`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:11.230902+00:00.  

```json
{"evidences":[{"evidenceCode":"ECO:0000312","id":"AAW90311.1","source":"EMBL"},{"evidenceCode":"ECO:0000312","id":"UP000000535","source":"Proteomes"}],"lineage":["Bacteria","Pseudomonadati","Pseudomonadota","Betaproteobacteria","Neisseriales","Neisseriaceae","Neisseria"],"scientificName":"Neisseria gonorrhoeae (strain ATCC 700825 / FA 1090)","taxonId":242231}
```

Source SHA-256: `fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:11.230902+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23839218","source":"PubMed"}],"value":"Metalloprotease NGO1686"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"23839218","source":"PubMed"}],"value":"Metalloprotease active against peptidoglycan"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Outer membrane protein"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"OMP"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22334697","source":"PubMed"}],"value":"Virulence factor NG1686"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22334697","source":"PubMed"},{"evidenceCode":"ECO:0000303","id":"23839218","source":"PubMed"}],"value":"Zinc metallopeptidase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16194237","source":"PubMed"}],"value":"Zinc metalloprotease"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Zinc-dependent metallopeptidase"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22334697","source":"PubMed"}],"value":"3.4.17.-"},{"evidences":[{"evidenceCode":"ECO:0000269","id":"22334697","source":"PubMed"}],"value":"3.4.24.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"DD-carboxypeptidase/endopeptidase Mpg"}}}
```

Source SHA-256: `fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:11.230902+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"E0N688","source":"UniProtKB"},{"evidenceCode":"ECO:0000305"}],"value":"There is a signal or a transmembrane region in the N-terminus of the pre-protein (Probable). Mature protein is probably associated with the cell outer membrane (By similarity)"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000250","id":"E0N688","source":"UniProtKB"}],"id":"SL-0040","value":"Cell outer membrane"}}]}
```

Source SHA-256: `fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5F676.json)  
**Locator:** `/uniProtKBCrossReferences/12`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:11.230902+00:00.  

```json
{"database":"GO","id":"GO:0009279","properties":[{"key":"GoTerm","value":"C:cell outer membrane"},{"key":"GoEvidenceType","value":"ISS:UniProtKB"}]}
```

Source SHA-256: `fb861969d91ac7cb49b42e1ec2a04ceb76231816638b32a5169beda68ec7a6ec`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)  
**Locator:** `lines 104-108`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 88 / 1.  
**Retrieved:** 2026-11-02T04:31:15.062188+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell outer membrane
CC       {ECO:0000250|UniProtKB:E0N688}. Note=There is a signal or a
CC       transmembrane region in the N-terminus of the pre-protein (Probable).
CC       Mature protein is probably associated with the cell outer membrane (By
CC       similarity). {ECO:0000250|UniProtKB:E0N688, ECO:0000305}.
```

Source SHA-256: `1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5F676?format=txt&versions=88)  
**Locator:** `lines 152-152`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 88 / 1.  
**Retrieved:** 2026-11-02T04:31:15.062188+00:00.  

```text
DR   GO; GO:0009279; C:cell outer membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `1017096d3fe4aad03188356cc0c1ec3da8e606828eca694bd37794091f70cb15`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 103. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
