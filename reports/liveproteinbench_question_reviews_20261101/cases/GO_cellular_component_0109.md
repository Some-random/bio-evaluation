# GO_cellular_component_0109

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **C** — nucleus

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSLLYGLLILAFTRSCLVVGQCSINIPDDLKGEEAPVILVKTGNNVKLFRPEEKTTTFPKGTELLLACTGEGNGLKSNGQETTTLSCNGNQFESAAKEKLKDMSCKSMAKAVVEQTTKRCMGNDFNLYEAGYKVNGKFYGSVYDICYNGKGQSSGYTHNFIYGRTWKYKLPEKPYEHYSSRDPQAGKDLDKLYKEQKERFKNTKVNGKPLLDDEHYFTEGQLTPDTSIITGADKLSTYDYANIAPLFKDIYDGNIWRYENMTQELADQRQATFEEYTGGFYSYEVEKWKPIGLDNAEFPTHRVPKYIYKLVVDTESKDGIVFVTLNDPYHKSPASENLCKDICSEANINEPDFKNVEKGYTICCSYGDFGNRIRTLPKDIHVKGLLKY

[Multiple Choices]
A. perikaryon
B. centrosome
C. nucleus
D. tRNA methyltransferase complex
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

### Expected-answer support: contradicted

> The sequence matches a Tsal2A precursor with an N-terminal signal peptide, and the matched UniProt record describes it as secreted and assigns extracellular region with IDA evidence. The nucleus annotation is computational (IEA:TreeGrafter), so it does not support nucleus as the primary location over the secretion evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The hydrophobic N-terminus is consistent with a signal peptide and secretion, which argues against the listed intracellular locations. But secretion is not an option, so this does not biologically distinguish nucleus from the other listed choices as the correct answer.


**Missing item-specific fact**

> Selecting nucleus would require the protein-specific GO annotation; in the matched record it is a computational TreeGrafter annotation, not a fact supplied in the question.


**Reason**

> The sequence supports a likely location that the choices omit. Choosing nucleus therefore depends on an item-specific annotation or memorized identity rather than a defensible inference from the supplied choices and sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices omit secreted/extracellular, the location supported by the matched record. None of the listed choices is well supported as the protein's primary location.


### Important caveats

- The sequence match identifies the protein as Tsal2A, but that accession and its annotations were reviewer-only information.
- The extracellular assignment is cited as IDA in UniProt; the cited primary study was not independently retrieved here.
- A computational nucleus annotation exists, but it is not equivalent to experimental evidence of primary nuclear residence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The hydrophobic N-terminus is consistent with a signal peptide and secretion, which argues against the listed intracellular locations. But secretion is not an option, so this does not biologically distinguish nucleus from the other listed choices as the correct answer.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Selecting nucleus would require the protein-specific GO annotation; in the matched record it is a computational TreeGrafter annotation, not a fact supplied in the question.",
    "reason": "The sequence supports a likely location that the choices omit. Choosing nucleus therefore depends on an item-specific annotation or memorized identity rather than a defensible inference from the supplied choices and sequence."
  },
  "case_id": "GO_cellular_component_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The sequence matches a Tsal2A precursor with an N-terminal signal peptide, and the matched UniProt record describes it as secreted and assigns extracellular region with IDA evidence. The nucleus annotation is computational (IEA:TreeGrafter), so it does not support nucleus as the primary location over the secretion evidence."
  },
  "important_caveats": [
    "The sequence match identifies the protein as Tsal2A, but that accession and its annotations were reviewer-only information.",
    "The extracellular assignment is cited as IDA in UniProt; the cited primary study was not independently retrieved here.",
    "A computational nucleus annotation exists, but it is not equivalent to experimental evidence of primary nuclear residence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices omit secreted/extracellular, the location supported by the matched record. None of the listed choices is well supported as the protein's primary location."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0109",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence matches a Tsal2A precursor with an N-terminal signal peptide, and the matched UniProt record describes it as secreted and assigns extracellular region with IDA evidence. The nucleus annotation is computational (IEA:TreeGrafter), so it does not support nucleus as the primary location over the secretion evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The hydrophobic N-terminus is consistent with a signal peptide and secretion, which argues against the listed intracellular locations. But secretion is not an option, so this does not biologically distinguish nucleus from the other listed choices as the correct answer.",
    "missing_item_specific_fact": "Selecting nucleus would require the protein-specific GO annotation; in the matched record it is a computational TreeGrafter annotation, not a fact supplied in the question.",
    "reason": "The sequence supports a likely location that the choices omit. Choosing nucleus therefore depends on an item-specific annotation or memorized identity rather than a defensible inference from the supplied choices and sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices omit secreted/extracellular, the location supported by the matched record. None of the listed choices is well supported as the protein's primary location."
  },
  "important_caveats": [
    "The sequence match identifies the protein as Tsal2A, but that accession and its annotations were reviewer-only information.",
    "The extracellular assignment is cited as IDA in UniProt; the cited primary study was not independently retrieved here.",
    "A computational nucleus annotation exists, but it is not equivalent to experimental evidence of primary nuclear residence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The protein is Salivary protein Tsal2A (UniProt A3FMN3) from Glossina morsitans morsitans. Its primary, experimentally-supported subcellular location is 'Secreted' (ECO:0000305|PubMed:23110062) with GO annotation GO:0005576 (extracellular region, IDA:UniProtKB). The 'nucleus' annotation (GO:0005634) exists only as a low-confidence IEA:TreeGrafter computational prediction, not experimental evidence. The protein is a secreted salivary gland protein with a clear N-terminal signal peptide. The author's answer of 'nucleus' is contradicted by the primary experimental annotation and is not the 'primary' cellular component for this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal sequence 'MSLLYGLLILAFTRSCLVVGQ' contains a clear hydrophobic signal peptide, strongly indicating the protein enters the secretory pathway rather than the nucleus. Multiple conserved cysteines are characteristic of secreted proteins. No nuclear localization signal (NLS) is apparent. Sequence reasoning would argue AGAINST nucleus and FOR secretion/extracellular localization.


**Missing item-specific fact**

> The author's answer depends on the presence of a specific IEA:TreeGrafter GO annotation (GO:0005634, nucleus) in the UniProt database for this particular protein, which is a low-confidence computational prediction contradicted by the experimental 'Secreted' annotation. Without knowing this specific database entry, biological reasoning from the sequence would not lead to 'nucleus'.


**Reason**

> The sequence contains a signal peptide indicating secretion, no NLS, and no features suggesting nuclear, centrosomal, or tRNA-methyltransferase-complex localization. The correct biological answer (secreted/extracellular) is not among the options. Selecting 'nucleus' requires knowledge that a TreeGrafter computational annotation assigned GO:0005634 to this specific UniProt entry, which is a database-specific lookup rather than a reasoning conclusion from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> None of the four options (perikaryon, centrosome, nucleus, tRNA methyltransferase complex) match the experimentally-verified location (secreted/extracellular). The 'nucleus' option is present only as an IEA:TreeGrafter prediction and is contradicted by IDA-level experimental evidence. No option is biologically correct for this protein.


### Important caveats

- The 'nucleus' GO annotation exists in the database but is IEA:TreeGrafter (computational homology transfer), the lowest-confidence evidence type, and is contradicted by the IDA:UniProtKB 'extracellular region' annotation.
- The protein is explicitly named 'Salivary protein Tsal2A' and its function involves nucleic acid binding in saliva, confirming its secreted nature.
- The benchmark may have been constructed from a dataset that included all GO annotations (including IEA) without filtering for evidence quality.
- The entry was first publicly released 2025-02-05; the author's data-construction date and exact annotation snapshot are unknown.
- The sequence-match is confirmed (SHA256 match) between the benchmark sequence and UniProt A3FMN3.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'MSLLYGLLILAFTRSCLVVGQ' contains a clear hydrophobic signal peptide, strongly indicating the protein enters the secretory pathway rather than the nucleus. Multiple conserved cysteines are characteristic of secreted proteins. No nuclear localization signal (NLS) is apparent. Sequence reasoning would argue AGAINST nucleus and FOR secretion/extracellular localization.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The author's answer depends on the presence of a specific IEA:TreeGrafter GO annotation (GO:0005634, nucleus) in the UniProt database for this particular protein, which is a low-confidence computational prediction contradicted by the experimental 'Secreted' annotation. Without knowing this specific database entry, biological reasoning from the sequence would not lead to 'nucleus'.",
    "reason": "The sequence contains a signal peptide indicating secretion, no NLS, and no features suggesting nuclear, centrosomal, or tRNA-methyltransferase-complex localization. The correct biological answer (secreted/extracellular) is not among the options. Selecting 'nucleus' requires knowledge that a TreeGrafter computational annotation assigned GO:0005634 to this specific UniProt entry, which is a database-specific lookup rather than a reasoning conclusion from the sequence."
  },
  "case_id": "GO_cellular_component_0109",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6"
    ],
    "judgment": "contradicted",
    "reason": "The protein is Salivary protein Tsal2A (UniProt A3FMN3) from Glossina morsitans morsitans. Its primary, experimentally-supported subcellular location is 'Secreted' (ECO:0000305|PubMed:23110062) with GO annotation GO:0005576 (extracellular region, IDA:UniProtKB). The 'nucleus' annotation (GO:0005634) exists only as a low-confidence IEA:TreeGrafter computational prediction, not experimental evidence. The protein is a secreted salivary gland protein with a clear N-terminal signal peptide. The author's answer of 'nucleus' is contradicted by the primary experimental annotation and is not the 'primary' cellular component for this protein."
  },
  "important_caveats": [
    "The 'nucleus' GO annotation exists in the database but is IEA:TreeGrafter (computational homology transfer), the lowest-confidence evidence type, and is contradicted by the IDA:UniProtKB 'extracellular region' annotation.",
    "The protein is explicitly named 'Salivary protein Tsal2A' and its function involves nucleic acid binding in saliva, confirming its secreted nature.",
    "The benchmark may have been constructed from a dataset that included all GO annotations (including IEA) without filtering for evidence quality.",
    "The entry was first publicly released 2025-02-05; the author's data-construction date and exact annotation snapshot are unknown.",
    "The sequence-match is confirmed (SHA256 match) between the benchmark sequence and UniProt A3FMN3."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options (perikaryon, centrosome, nucleus, tRNA methyltransferase complex) match the experimentally-verified location (secreted/extracellular). The 'nucleus' option is present only as an IEA:TreeGrafter prediction and is contradicted by IDA-level experimental evidence. No option is biologically correct for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0109",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The protein is Salivary protein Tsal2A (UniProt A3FMN3) from Glossina morsitans morsitans. Its primary, experimentally-supported subcellular location is 'Secreted' (ECO:0000305|PubMed:23110062) with GO annotation GO:0005576 (extracellular region, IDA:UniProtKB). The 'nucleus' annotation (GO:0005634) exists only as a low-confidence IEA:TreeGrafter computational prediction, not experimental evidence. The protein is a secreted salivary gland protein with a clear N-terminal signal peptide. The author's answer of 'nucleus' is contradicted by the primary experimental annotation and is not the 'primary' cellular component for this protein.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H3", "H4", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal sequence 'MSLLYGLLILAFTRSCLVVGQ' contains a clear hydrophobic signal peptide, strongly indicating the protein enters the secretory pathway rather than the nucleus. Multiple conserved cysteines are characteristic of secreted proteins. No nuclear localization signal (NLS) is apparent. Sequence reasoning would argue AGAINST nucleus and FOR secretion/extracellular localization.",
    "missing_item_specific_fact": "The author's answer depends on the presence of a specific IEA:TreeGrafter GO annotation (GO:0005634, nucleus) in the UniProt database for this particular protein, which is a low-confidence computational prediction contradicted by the experimental 'Secreted' annotation. Without knowing this specific database entry, biological reasoning from the sequence would not lead to 'nucleus'.",
    "reason": "The sequence contains a signal peptide indicating secretion, no NLS, and no features suggesting nuclear, centrosomal, or tRNA-methyltransferase-complex localization. The correct biological answer (secreted/extracellular) is not among the options. Selecting 'nucleus' requires knowledge that a TreeGrafter computational annotation assigned GO:0005634 to this specific UniProt entry, which is a database-specific lookup rather than a reasoning conclusion from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "None of the four options (perikaryon, centrosome, nucleus, tRNA methyltransferase complex) match the experimentally-verified location (secreted/extracellular). The 'nucleus' option is present only as an IEA:TreeGrafter prediction and is contradicted by IDA-level experimental evidence. No option is biologically correct for this protein."
  },
  "important_caveats": [
    "The 'nucleus' GO annotation exists in the database but is IEA:TreeGrafter (computational homology transfer), the lowest-confidence evidence type, and is contradicted by the IDA:UniProtKB 'extracellular region' annotation.",
    "The protein is explicitly named 'Salivary protein Tsal2A' and its function involves nucleic acid binding in saliva, confirming its secreted nature.",
    "The benchmark may have been constructed from a dataset that included all GO annotations (including IEA) without filtering for evidence quality.",
    "The entry was first publicly released 2025-02-05; the author's data-construction date and exact annotation snapshot are unknown.",
    "The sequence-match is confirmed (SHA256 match) between the benchmark sequence and UniProt A3FMN3."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `mixed_location_annotations_require_qualification`.

> C5/H3 say secreted and C6/H4 assign extracellular region with IDA; C8/H6 also carry nucleus via IEA:TreeGrafter.

**Remaining uncertainty:** The source contrast and evidence classes are traced; a primary-location inference should remain qualified rather than an exclusion of every additional location.

Evidence checked: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6).

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A3FMN3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 43. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3FMN3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:55.735059+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"23110062","source":"PubMed"}],"value":"3.1.-.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000312","id":"ABN58709.1","source":"EMBL"}],"value":"Tsal2 form A"}}],"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Salivary protein Tsal2A"}}}
```

Source SHA-256: `ffec1889b6e2b4da5bc84e64d5de4c27ea429dd747f9fcbcc7da7373ae275544`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3FMN3.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:55.735059+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000305","id":"23110062","source":"PubMed"}],"id":"SL-0243","value":"Secreted"}}]}
```

Source SHA-256: `ffec1889b6e2b4da5bc84e64d5de4c27ea429dd747f9fcbcc7da7373ae275544`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3FMN3.json)  
**Locator:** `/uniProtKBCrossReferences/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:55.735059+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"23110062","source":"PubMed"}],"id":"GO:0005576","properties":[{"key":"GoTerm","value":"C:extracellular region"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `ffec1889b6e2b4da5bc84e64d5de4c27ea429dd747f9fcbcc7da7373ae275544`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A3FMN3.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:26:55.735059+00:00.  

```json
{"database":"GO","id":"GO:0005634","properties":[{"key":"GoTerm","value":"C:nucleus"},{"key":"GoEvidenceType","value":"IEA:TreeGrafter"}]}
```

Source SHA-256: `ffec1889b6e2b4da5bc84e64d5de4c27ea429dd747f9fcbcc7da7373ae275544`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3FMN3?format=txt&versions=43)  
**Locator:** `lines 47-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-02T04:26:57.843760+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000305|PubMed:23110062}.
```

Source SHA-256: `536ab519e8a60564cb105c157bc3915399519199d9ee3dbc6d98a78c1f3456d5`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3FMN3?format=txt&versions=43)  
**Locator:** `lines 63-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-02T04:26:57.843760+00:00.  

```text
DR   GO; GO:0005576; C:extracellular region; IDA:UniProtKB.
```

Source SHA-256: `536ab519e8a60564cb105c157bc3915399519199d9ee3dbc6d98a78c1f3456d5`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A3FMN3?format=txt&versions=43)  
**Locator:** `lines 65-65`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 43 / 1.  
**Retrieved:** 2026-11-02T04:26:57.843760+00:00.  

```text
DR   GO; GO:0005634; C:nucleus; IEA:TreeGrafter.
```

Source SHA-256: `536ab519e8a60564cb105c157bc3915399519199d9ee3dbc6d98a78c1f3456d5`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 109. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
