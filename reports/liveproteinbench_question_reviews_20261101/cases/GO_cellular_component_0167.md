# GO_cellular_component_0167

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **D** — peptidoglycan-based cell wall

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | valid_review |

**Paired comparison:** key differ; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MLVTVGSMNERVPDSSGLPLRAMVMVLLFLGVVFLLLVWQALGSSPNSEDDSSAISTMTTTTAAPTSTSVKPAAPRAEVRVYNISGTEGAAARTADRLKAAGFTVTDVGNLSLPDVAATTVYYTEVEGERATADAVGRTLGAAVELRLPELSDQPPGVIVVVTG

[Multiple Choices]
A. collagen-containing extracellular matrix
B. motile cilium
C. histone deacetylase complex
D. peptidoglycan-based cell wall
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

> The exact matching historical UniProt record annotates the protein to peptidoglycan-based cell wall with evidence code HDA (H6). However, this supports the recorded GO annotation, not conclusively that the cell wall is its primary location: experimental localization in the same record places it in the cytoplasm and peripherally associated with the inner membrane (H4).

Citations as saved: [H6](#evidence-h6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic region is consistent with membrane association, but does not distinguish cell-wall localization from cytoplasmic or membrane localization. The eukaryote-specific distractors make D comparatively plausible if the protein is known to be bacterial, but the sequence alone does not establish that its primary location is the peptidoglycan-based cell wall.


**Missing item-specific fact**

> The protein-specific GO annotation to peptidoglycan-based cell wall, or other evidence establishing this protein's location, is absent from the input.


**Reason**

> Choosing D depends on protein-specific annotation or localization evidence, not a sufficiently discriminating inference from the sequence and choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports D as an annotation; although experimental localization also reports cytoplasm and inner-membrane association, those locations are not among the choices.


### Important caveats

- The cell-wall annotation is database evidence with code HDA; it should not be conflated with definitive evidence that this is the protein's primary cellular component.
- The experimental cytoplasm and inner-membrane localization evidence complicates interpreting D as a primary-location answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic region is consistent with membrane association, but does not distinguish cell-wall localization from cytoplasmic or membrane localization. The eukaryote-specific distractors make D comparatively plausible if the protein is known to be bacterial, but the sequence alone does not establish that its primary location is the peptidoglycan-based cell wall.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific GO annotation to peptidoglycan-based cell wall, or other evidence establishing this protein's location, is absent from the input.",
    "reason": "Choosing D depends on protein-specific annotation or localization evidence, not a sufficiently discriminating inference from the sequence and choices."
  },
  "case_id": "GO_cellular_component_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "H6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact matching historical UniProt record annotates the protein to peptidoglycan-based cell wall with evidence code HDA (H6). However, this supports the recorded GO annotation, not conclusively that the cell wall is its primary location: experimental localization in the same record places it in the cytoplasm and peripherally associated with the inner membrane (H4)."
  },
  "important_caveats": [
    "The cell-wall annotation is database evidence with code HDA; it should not be conflated with definitive evidence that this is the protein's primary cellular component.",
    "The experimental cytoplasm and inner-membrane localization evidence complicates interpreting D as a primary-location answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports D as an annotation; although experimental localization also reports cytoplasm and inner-membrane association, those locations are not among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0167",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact matching historical UniProt record annotates the protein to peptidoglycan-based cell wall with evidence code HDA (H6). However, this supports the recorded GO annotation, not conclusively that the cell wall is its primary location: experimental localization in the same record places it in the cytoplasm and peripherally associated with the inner membrane (H4).",
    "evidence_ids": ["H6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic region is consistent with membrane association, but does not distinguish cell-wall localization from cytoplasmic or membrane localization. The eukaryote-specific distractors make D comparatively plausible if the protein is known to be bacterial, but the sequence alone does not establish that its primary location is the peptidoglycan-based cell wall.",
    "missing_item_specific_fact": "The protein-specific GO annotation to peptidoglycan-based cell wall, or other evidence establishing this protein's location, is absent from the input.",
    "reason": "Choosing D depends on protein-specific annotation or localization evidence, not a sufficiently discriminating inference from the sequence and choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports D as an annotation; although experimental localization also reports cytoplasm and inner-membrane association, those locations are not among the choices."
  },
  "important_caveats": [
    "The cell-wall annotation is database evidence with code HDA; it should not be conflated with definitive evidence that this is the protein's primary cellular component.",
    "The experimental cytoplasm and inner-membrane localization evidence complicates interpreting D as a primary-location answer."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The protein is VirR (P96277) from Mycobacterium tuberculosis H37Rv, a 164-aa protein. The curated UniProt SUBCELLULAR LOCATION comment (C5/H4, evidence ECO:0000269/PubMed:24248369) states: 'Cell inner membrane; Peripheral membrane protein; Cytoplasmic side. Cytoplasm.' with the note that 'VirR is located in the cytosol, where it is associated with the plasma membrane without crossing it.' The experimental GO annotations (EXP:UniProtKB) are GO:0005737 cytoplasm (C6) and GO:0005886 plasma membrane (C7). The GO:0009274 peptidoglycan-based cell wall annotation (H6) carries only the HDA:MTBBASE evidence code — a low-confidence high-throughput database annotation, not experimental data. The primary cellular component is cytoplasm/plasma membrane, not the peptidoglycan cell wall. The expected answer D is contradicted by the stronger experimental and curated evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model could eliminate options A (collagen-containing extracellular matrix), B (motile cilium), and C (histone deacetylase complex) as eukaryotic-specific compartments irrelevant to a bacterium, leaving D. However, this elimination does not confirm that the protein is actually in the peptidoglycan cell wall. The sequence lacks any peptidoglycan-binding domain (e.g., LysM, SH3b, Amidase) and lacks a secretion signal peptide; instead it shows an N-terminal hydrophobic membrane-anchoring region consistent with cytoplasmic/peripheral membrane localization. The correct primary location (cytoplasm/plasma membrane) is not among the choices at all.


**Missing item-specific fact**

> The HDA:MTBBASE database annotation linking this specific protein to GO:0009274 is an item-specific external fact absent from the sequence. More critically, the correct primary location (cytoplasm/plasma membrane, supported by experimental evidence) is not offered as a choice, making the question fundamentally unanswerable by reasoning toward the true biology.


**Reason**

> While general biological knowledge (bacteria lack collagen, cilia, histone deacetylase complexes) allows elimination of A–C, this leads to D, which is not the protein's actual location. The expected answer D depends on a specific low-confidence database annotation (HDA:MTBBASE), and the true experimental location is not among the options. Sequence features (hydrophobic membrane-anchor, no peptidoglycan-binding motifs, no secretion signal) argue against D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> None of the four options matches the experimentally determined primary location (cytoplasm / plasma membrane). The question is not ambiguous among the choices so much as it is misconstructed: the correct answer is absent from the option set. D is the only bacterial-relevant compartment but is not where this protein actually resides.


### Important caveats

- The GO:0009274 annotation for P96277 carries evidence code HDA:MTBBASE, a high-throughput database annotation from MTBBASE, not experimental evidence. The benchmark may have selected this annotation as ground truth without distinguishing evidence strength.
- The curated UniProt SUBCELLULAR LOCATION (ECO:0000269, experimental) explicitly places VirR in the cytosol associated with the cytoplasmic face of the plasma membrane — directly contradicting a peptidoglycan cell wall assignment.
- The sequence (164 aa) shows an N-terminal hydrophobic stretch (~residues 15–30) consistent with membrane anchoring, not a cleavable signal peptide for secretion to the cell wall.
- The identity of the protein (P96277) was inferred from reviewer-only metadata; the evaluated model saw only the raw sequence and the four choices.
- The question's option set omits the correct primary compartments (cytoplasm GO:0005737, plasma membrane GO:0005886), making the item structurally flawed regardless of which option is designated correct.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model could eliminate options A (collagen-containing extracellular matrix), B (motile cilium), and C (histone deacetylase complex) as eukaryotic-specific compartments irrelevant to a bacterium, leaving D. However, this elimination does not confirm that the protein is actually in the peptidoglycan cell wall. The sequence lacks any peptidoglycan-binding domain (e.g., LysM, SH3b, Amidase) and lacks a secretion signal peptide; instead it shows an N-terminal hydrophobic membrane-anchoring region consistent with cytoplasmic/peripheral membrane localization. The correct primary location (cytoplasm/plasma membrane) is not among the choices at all.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The HDA:MTBBASE database annotation linking this specific protein to GO:0009274 is an item-specific external fact absent from the sequence. More critically, the correct primary location (cytoplasm/plasma membrane, supported by experimental evidence) is not offered as a choice, making the question fundamentally unanswerable by reasoning toward the true biology.",
    "reason": "While general biological knowledge (bacteria lack collagen, cilia, histone deacetylase complexes) allows elimination of A–C, this leads to D, which is not the protein's actual location. The expected answer D depends on a specific low-confidence database annotation (HDA:MTBBASE), and the true experimental location is not among the options. Sequence features (hydrophobic membrane-anchor, no peptidoglycan-binding motifs, no secretion signal) argue against D."
  },
  "case_id": "GO_cellular_component_0167",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H4",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "contradicted",
    "reason": "The protein is VirR (P96277) from Mycobacterium tuberculosis H37Rv, a 164-aa protein. The curated UniProt SUBCELLULAR LOCATION comment (C5/H4, evidence ECO:0000269/PubMed:24248369) states: 'Cell inner membrane; Peripheral membrane protein; Cytoplasmic side. Cytoplasm.' with the note that 'VirR is located in the cytosol, where it is associated with the plasma membrane without crossing it.' The experimental GO annotations (EXP:UniProtKB) are GO:0005737 cytoplasm (C6) and GO:0005886 plasma membrane (C7). The GO:0009274 peptidoglycan-based cell wall annotation (H6) carries only the HDA:MTBBASE evidence code — a low-confidence high-throughput database annotation, not experimental data. The primary cellular component is cytoplasm/plasma membrane, not the peptidoglycan cell wall. The expected answer D is contradicted by the stronger experimental and curated evidence."
  },
  "important_caveats": [
    "The GO:0009274 annotation for P96277 carries evidence code HDA:MTBBASE, a high-throughput database annotation from MTBBASE, not experimental evidence. The benchmark may have selected this annotation as ground truth without distinguishing evidence strength.",
    "The curated UniProt SUBCELLULAR LOCATION (ECO:0000269, experimental) explicitly places VirR in the cytosol associated with the cytoplasmic face of the plasma membrane — directly contradicting a peptidoglycan cell wall assignment.",
    "The sequence (164 aa) shows an N-terminal hydrophobic stretch (~residues 15–30) consistent with membrane anchoring, not a cleavable signal peptide for secretion to the cell wall.",
    "The identity of the protein (P96277) was inferred from reviewer-only metadata; the evaluated model saw only the raw sequence and the four choices.",
    "The question's option set omits the correct primary compartments (cytoplasm GO:0005737, plasma membrane GO:0005886), making the item structurally flawed regardless of which option is designated correct."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options matches the experimentally determined primary location (cytoplasm / plasma membrane). The question is not ambiguous among the choices so much as it is misconstructed: the correct answer is absent from the option set. D is the only bacterial-relevant compartment but is not where this protein actually resides."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0167",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The protein is VirR (P96277) from Mycobacterium tuberculosis H37Rv, a 164-aa protein. The curated UniProt SUBCELLULAR LOCATION comment (C5/H4, evidence ECO:0000269/PubMed:24248369) states: 'Cell inner membrane; Peripheral membrane protein; Cytoplasmic side. Cytoplasm.' with the note that 'VirR is located in the cytosol, where it is associated with the plasma membrane without crossing it.' The experimental GO annotations (EXP:UniProtKB) are GO:0005737 cytoplasm (C6) and GO:0005886 plasma membrane (C7). The GO:0009274 peptidoglycan-based cell wall annotation (H6) carries only the HDA:MTBBASE evidence code — a low-confidence high-throughput database annotation, not experimental data. The primary cellular component is cytoplasm/plasma membrane, not the peptidoglycan cell wall. The expected answer D is contradicted by the stronger experimental and curated evidence.",
    "evidence_ids": ["C5", "C6", "C7", "H4", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model could eliminate options A (collagen-containing extracellular matrix), B (motile cilium), and C (histone deacetylase complex) as eukaryotic-specific compartments irrelevant to a bacterium, leaving D. However, this elimination does not confirm that the protein is actually in the peptidoglycan cell wall. The sequence lacks any peptidoglycan-binding domain (e.g., LysM, SH3b, Amidase) and lacks a secretion signal peptide; instead it shows an N-terminal hydrophobic membrane-anchoring region consistent with cytoplasmic/peripheral membrane localization. The correct primary location (cytoplasm/plasma membrane) is not among the choices at all.",
    "missing_item_specific_fact": "The HDA:MTBBASE database annotation linking this specific protein to GO:0009274 is an item-specific external fact absent from the sequence. More critically, the correct primary location (cytoplasm/plasma membrane, supported by experimental evidence) is not offered as a choice, making the question fundamentally unanswerable by reasoning toward the true biology.",
    "reason": "While general biological knowledge (bacteria lack collagen, cilia, histone deacetylase complexes) allows elimination of A–C, this leads to D, which is not the protein's actual location. The expected answer D depends on a specific low-confidence database annotation (HDA:MTBBASE), and the true experimental location is not among the options. Sequence features (hydrophobic membrane-anchor, no peptidoglycan-binding motifs, no secretion signal) argue against D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options matches the experimentally determined primary location (cytoplasm / plasma membrane). The question is not ambiguous among the choices so much as it is misconstructed: the correct answer is absent from the option set. D is the only bacterial-relevant compartment but is not where this protein actually resides."
  },
  "important_caveats": [
    "The GO:0009274 annotation for P96277 carries evidence code HDA:MTBBASE, a high-throughput database annotation from MTBBASE, not experimental evidence. The benchmark may have selected this annotation as ground truth without distinguishing evidence strength.",
    "The curated UniProt SUBCELLULAR LOCATION (ECO:0000269, experimental) explicitly places VirR in the cytosol associated with the cytoplasmic face of the plasma membrane — directly contradicting a peptidoglycan cell wall assignment.",
    "The sequence (164 aa) shows an N-terminal hydrophobic stretch (~residues 15–30) consistent with membrane anchoring, not a cleavable signal peptide for secretion to the cell wall.",
    "The identity of the protein (P96277) was inferred from reviewer-only metadata; the evaluated model saw only the raw sequence and the four choices.",
    "The question's option set omits the correct primary compartments (cytoplasm GO:0005737, plasma membrane GO:0005886), making the item structurally flawed regardless of which option is designated correct."
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

**Accession:** `P96277` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 136. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P96277.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:08.695621+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24248369","source":"PubMed"}],"value":"Subcellular fractionation and topologic analyses suggest that VirR is located in the cytosol, where it is associated with the plasma membrane without crossing it"}]},"subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"24248369","source":"PubMed"}],"id":"SL-0037","value":"Cell inner membrane"},"orientation":{"evidences":[{"evidenceCode":"ECO:0000269","id":"24248369","source":"PubMed"}],"id":"SL-9910","value":"Cytoplasmic side"},"topology":{"evidences":[{"evidenceCode":"ECO:0000269","id":"24248369","source":"PubMed"}],"id":"SL-9903","value":"Peripheral membrane protein"}},{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"31285241","source":"PubMed"}],"id":"SL-0086","value":"Cytoplasm"}}]}
```

Source SHA-256: `50dc24e09769c87e9d9e8f99cff758c5946bf28fabde62058d84108ce1a51d28`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P96277.json)  
**Locator:** `/uniProtKBCrossReferences/17`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:08.695621+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"31285241","source":"PubMed"}],"id":"GO:0005737","properties":[{"key":"GoTerm","value":"C:cytoplasm"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `50dc24e09769c87e9d9e8f99cff758c5946bf28fabde62058d84108ce1a51d28`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P96277.json)  
**Locator:** `/uniProtKBCrossReferences/18`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:08.695621+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000269","id":"24248369","source":"PubMed"}],"id":"GO:0005886","properties":[{"key":"GoTerm","value":"C:plasma membrane"},{"key":"GoEvidenceType","value":"EXP:UniProtKB"}]}
```

Source SHA-256: `50dc24e09769c87e9d9e8f99cff758c5946bf28fabde62058d84108ce1a51d28`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P96277?format=txt&versions=136)  
**Locator:** `lines 89-95`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 2.  
**Retrieved:** 2026-11-02T04:30:15.043382+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Cell inner membrane
CC       {ECO:0000269|PubMed:24248369}; Peripheral membrane protein
CC       {ECO:0000269|PubMed:24248369}; Cytoplasmic side
CC       {ECO:0000269|PubMed:24248369}. Cytoplasm {ECO:0000269|PubMed:31285241}.
CC       Note=Subcellular fractionation and topologic analyses suggest that VirR
CC       is located in the cytosol, where it is associated with the plasma
CC       membrane without crossing it. {ECO:0000269|PubMed:24248369}.
```

Source SHA-256: `53ba58c04d416cac1c559fd5dcb54fc6d644e0d38cc28631e46a6f7202aa84a7`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P96277?format=txt&versions=136)  
**Locator:** `lines 140-140`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 2.  
**Retrieved:** 2026-11-02T04:30:15.043382+00:00.  

```text
DR   GO; GO:0005737; C:cytoplasm; IEA:UniProtKB-SubCell.
```

Source SHA-256: `53ba58c04d416cac1c559fd5dcb54fc6d644e0d38cc28631e46a6f7202aa84a7`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P96277?format=txt&versions=136)  
**Locator:** `lines 141-141`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 2.  
**Retrieved:** 2026-11-02T04:30:15.043382+00:00.  

```text
DR   GO; GO:0009274; C:peptidoglycan-based cell wall; HDA:MTBBASE.
```

Source SHA-256: `53ba58c04d416cac1c559fd5dcb54fc6d644e0d38cc28631e46a6f7202aa84a7`.

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P96277?format=txt&versions=136)  
**Locator:** `lines 142-142`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 136 / 2.  
**Retrieved:** 2026-11-02T04:30:15.043382+00:00.  

```text
DR   GO; GO:0005886; C:plasma membrane; IEA:UniProtKB-SubCell.
```

Source SHA-256: `53ba58c04d416cac1c559fd5dcb54fc6d644e0d38cc28631e46a6f7202aa84a7`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 167. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
