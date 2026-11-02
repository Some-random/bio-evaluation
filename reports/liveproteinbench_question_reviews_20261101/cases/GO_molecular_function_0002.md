# GO_molecular_function_0002

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **B** — endopeptidase activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKNNKISGFQWAMTIFVFFVITMALSIMLRDFQSIIGVKHFIFEVTDLAPLIAAIICILVFKYKKVQLAGLKFSISLKVIERLLLALILPLIILIIGMYSFNTFADSFILLQSTGLSVPITHILIGHILMAFVVEFGFRSYLQNIVETKMNTFFASIVVGLMYSVFSANTTYGTEFAAYNFLYTFSFSMILGELIRATKGRTIYIATTFHASMTFGLIFLFSEEIGDLFSIKVIAISTAIVAVGYIGLSLIIRGIAYLTTRRNLEELEPNNYLDHVNDDEETNHTEAEKSSSNIKDAEKTGVATASTVGVAKNDTENTVADEPSIHEGTEKTEPQHHIGNQTESNHDEDHDITSESVESAESVKQAPQSDDLTNDSNEDEIEQSLKEPVTYKEDRRSSVVIDAEKHIEKTEEQSSDKNK

[Multiple Choices]
A. dUMP kinase activity
B. endopeptidase activity
C. DNA binding
D. endonuclease activity
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The exact sequence has a UniProt GO annotation for endopeptidase activity, but its evidence is computational (IEA:UniProtKB-ARBA), not direct experimental confirmation. The accompanying functional description instead characterizes LyrA as probably non-catalytic in SagB-mediated peptidoglycan processing, so the annotation should not be treated as experimentally established.

Citations as saved: [C1](#evidence-c1), [C6](#evidence-c6), [C5](#evidence-c5), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is strongly hydrophobic and suggests a multipass membrane protein, which weighs against soluble kinase, DNA-binding, and endonuclease functions. But it does not provide a clear basis for assigning endopeptidase activity; the sequence-level clues do not establish that this membrane protein catalyzes peptide-bond hydrolysis.


**Missing item-specific fact**

> Distinguishing B requires the protein-specific GO annotation or other external functional evidence; the supplied sequence alone does not identify the reported ARBA assignment.


**Reason**

> General sequence reasoning can disfavor several choices, but does not meaningfully establish B. The key depends on an item-specific annotation absent from the model input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence does not clearly support any listed activity. B matches the database annotation, but the provided functional description points to a likely non-catalytic regulatory or scaffold role rather than endopeptidase activity.


### Important caveats

- The annotation and historical record match the supplied sequence, but the author's exact source snapshot is unknown.
- The GO annotation is computational; the cited functional description does not directly establish endopeptidase catalysis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and suggests a multipass membrane protein, which weighs against soluble kinase, DNA-binding, and endonuclease functions. But it does not provide a clear basis for assigning endopeptidase activity; the sequence-level clues do not establish that this membrane protein catalyzes peptide-bond hydrolysis.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Distinguishing B requires the protein-specific GO annotation or other external functional evidence; the supplied sequence alone does not identify the reported ARBA assignment.",
    "reason": "General sequence reasoning can disfavor several choices, but does not meaningfully establish B. The key depends on an item-specific annotation absent from the model input."
  },
  "case_id": "GO_molecular_function_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C6",
      "C5",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence has a UniProt GO annotation for endopeptidase activity, but its evidence is computational (IEA:UniProtKB-ARBA), not direct experimental confirmation. The accompanying functional description instead characterizes LyrA as probably non-catalytic in SagB-mediated peptidoglycan processing, so the annotation should not be treated as experimentally established."
  },
  "important_caveats": [
    "The annotation and historical record match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The GO annotation is computational; the cited functional description does not directly establish endopeptidase catalysis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence does not clearly support any listed activity. B matches the database annotation, but the provided functional description points to a likely non-catalytic regulatory or scaffold role rather than endopeptidase activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence has a UniProt GO annotation for endopeptidase activity, but its evidence is computational (IEA:UniProtKB-ARBA), not direct experimental confirmation. The accompanying functional description instead characterizes LyrA as probably non-catalytic in SagB-mediated peptidoglycan processing, so the annotation should not be treated as experimentally established.",
    "evidence_ids": ["C1", "C6", "C5", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and suggests a multipass membrane protein, which weighs against soluble kinase, DNA-binding, and endonuclease functions. But it does not provide a clear basis for assigning endopeptidase activity; the sequence-level clues do not establish that this membrane protein catalyzes peptide-bond hydrolysis.",
    "missing_item_specific_fact": "Distinguishing B requires the protein-specific GO annotation or other external functional evidence; the supplied sequence alone does not identify the reported ARBA assignment.",
    "reason": "General sequence reasoning can disfavor several choices, but does not meaningfully establish B. The key depends on an item-specific annotation absent from the model input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence does not clearly support any listed activity. B matches the database annotation, but the provided functional description points to a likely non-catalytic regulatory or scaffold role rather than endopeptidase activity."
  },
  "important_caveats": [
    "The annotation and historical record match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The GO annotation is computational; the cited functional description does not directly establish endopeptidase catalysis."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0H3KA40 (LyrA/SpdC, Lysostaphin resistance protein A) carries the GO annotation GO:0004175 (endopeptidase activity) as evidenced in C6 and H5. However, this annotation is solely IEA:UniProtKB-ARBA (automatic rule-based inference), not experimentally validated. Critically, the experimental FUNCTION comment (C5, H4; ECO:0000269 PubMed:33593946) states the protein 'probably plays a non-catalytic role in the cleavage of nascent peptidoglycan' and acts 'as a scaffold protein.' The annotation exists and matches the expected answer, but its evidentiary basis is weak and partially contradicted by experimental data.

Citations as saved: [C6](#evidence-c6), [H5](#evidence-h5), [C5](#evidence-c5), [H4](#evidence-h4), [C8](#evidence-c8), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The 419-aa sequence shows a hydrophobic N-terminal/transmembrane region, a large hydrophobic middle segment, and an acidic C-terminal tail. No recognizable catalytic triad, peptidase motif (e.g., Ser-His-Asp, Cys-His-Asn), kinase motif, DNA-binding domain (helix-turn-helix, zinc finger), or nuclease active site is identifiable from the sequence. All four options (dUMP kinase, endopeptidase, DNA binding, endonuclease) lack sequence-level support. The protein is in fact a membrane-associated scaffolding/regulatory protein with no intrinsic catalytic activity.


**Missing item-specific fact**

> The specific UniProt annotation assigning GO:0004175 (endopeptidase activity) to LyrA/SpdC via ARBA rule-based inference, which cannot be derived from sequence features alone since no peptidase catalytic motif is present.


**Reason**

> None of the four options can be distinguished from the amino acid sequence by general biological reasoning. The protein lacks any recognizable catalytic motif for peptidases, kinases, nucleases, or DNA-binding domains. Selection of answer B depends entirely on knowing the specific database annotation for this protein, which is itself an automatic inference contradicted by experimental evidence showing a non-catalytic scaffolding role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While none of the four options accurately describe the protein's true molecular function (scaffolding/regulatory protein in peptidoglycan processing), the annotation uniquely assigns GO:0004175. The other three options have zero supporting annotation or sequence evidence. However, the 'correct' answer itself is scientifically questionable given the experimental evidence of non-catalytic function.


### Important caveats

- The GO:0004175 annotation is IEA:UniProtKB-ARBA only (automatic rule-based inference), not experimentally verified.
- Experimental evidence (PubMed:33593946) explicitly describes a 'non-catalytic role' and 'scaffold protein' function, directly contradicting endopeptidase (catalytic) activity.
- The protein's true molecular function (scaffolding, protein binding, regulation of SagB) is not among the four options.
- The ARBA rule likely assigned endopeptidase activity based on the protein's involvement in peptidoglycan cleavage pathways, conflating pathway participation with intrinsic catalytic function.
- Sequence identity to UniProt A0A0H3KA40 is confirmed (SHA256 match), but the model receives no accession or name information.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 419-aa sequence shows a hydrophobic N-terminal/transmembrane region, a large hydrophobic middle segment, and an acidic C-terminal tail. No recognizable catalytic triad, peptidase motif (e.g., Ser-His-Asp, Cys-His-Asn), kinase motif, DNA-binding domain (helix-turn-helix, zinc finger), or nuclease active site is identifiable from the sequence. All four options (dUMP kinase, endopeptidase, DNA binding, endonuclease) lack sequence-level support. The protein is in fact a membrane-associated scaffolding/regulatory protein with no intrinsic catalytic activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt annotation assigning GO:0004175 (endopeptidase activity) to LyrA/SpdC via ARBA rule-based inference, which cannot be derived from sequence features alone since no peptidase catalytic motif is present.",
    "reason": "None of the four options can be distinguished from the amino acid sequence by general biological reasoning. The protein lacks any recognizable catalytic motif for peptidases, kinases, nucleases, or DNA-binding domains. Selection of answer B depends entirely on knowing the specific database annotation for this protein, which is itself an automatic inference contradicted by experimental evidence showing a non-catalytic scaffolding role."
  },
  "case_id": "GO_molecular_function_0002",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "H5",
      "C5",
      "H4",
      "C8",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H3KA40 (LyrA/SpdC, Lysostaphin resistance protein A) carries the GO annotation GO:0004175 (endopeptidase activity) as evidenced in C6 and H5. However, this annotation is solely IEA:UniProtKB-ARBA (automatic rule-based inference), not experimentally validated. Critically, the experimental FUNCTION comment (C5, H4; ECO:0000269 PubMed:33593946) states the protein 'probably plays a non-catalytic role in the cleavage of nascent peptidoglycan' and acts 'as a scaffold protein.' The annotation exists and matches the expected answer, but its evidentiary basis is weak and partially contradicted by experimental data."
  },
  "important_caveats": [
    "The GO:0004175 annotation is IEA:UniProtKB-ARBA only (automatic rule-based inference), not experimentally verified.",
    "Experimental evidence (PubMed:33593946) explicitly describes a 'non-catalytic role' and 'scaffold protein' function, directly contradicting endopeptidase (catalytic) activity.",
    "The protein's true molecular function (scaffolding, protein binding, regulation of SagB) is not among the four options.",
    "The ARBA rule likely assigned endopeptidase activity based on the protein's involvement in peptidoglycan cleavage pathways, conflating pathway participation with intrinsic catalytic function.",
    "Sequence identity to UniProt A0A0H3KA40 is confirmed (SHA256 match), but the model receives no accession or name information."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While none of the four options accurately describe the protein's true molecular function (scaffolding/regulatory protein in peptidoglycan processing), the annotation uniquely assigns GO:0004175. The other three options have zero supporting annotation or sequence evidence. However, the 'correct' answer itself is scientifically questionable given the experimental evidence of non-catalytic function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0002",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0H3KA40 (LyrA/SpdC, Lysostaphin resistance protein A) carries the GO annotation GO:0004175 (endopeptidase activity) as evidenced in C6 and H5. However, this annotation is solely IEA:UniProtKB-ARBA (automatic rule-based inference), not experimentally validated. Critically, the experimental FUNCTION comment (C5, H4; ECO:0000269 PubMed:33593946) states the protein 'probably plays a non-catalytic role in the cleavage of nascent peptidoglycan' and acts 'as a scaffold protein.' The annotation exists and matches the expected answer, but its evidentiary basis is weak and partially contradicted by experimental data.",
    "evidence_ids": ["C6", "H5", "C5", "H4", "C8", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The 419-aa sequence shows a hydrophobic N-terminal/transmembrane region, a large hydrophobic middle segment, and an acidic C-terminal tail. No recognizable catalytic triad, peptidase motif (e.g., Ser-His-Asp, Cys-His-Asn), kinase motif, DNA-binding domain (helix-turn-helix, zinc finger), or nuclease active site is identifiable from the sequence. All four options (dUMP kinase, endopeptidase, DNA binding, endonuclease) lack sequence-level support. The protein is in fact a membrane-associated scaffolding/regulatory protein with no intrinsic catalytic activity.",
    "missing_item_specific_fact": "The specific UniProt annotation assigning GO:0004175 (endopeptidase activity) to LyrA/SpdC via ARBA rule-based inference, which cannot be derived from sequence features alone since no peptidase catalytic motif is present.",
    "reason": "None of the four options can be distinguished from the amino acid sequence by general biological reasoning. The protein lacks any recognizable catalytic motif for peptidases, kinases, nucleases, or DNA-binding domains. Selection of answer B depends entirely on knowing the specific database annotation for this protein, which is itself an automatic inference contradicted by experimental evidence showing a non-catalytic scaffolding role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While none of the four options accurately describe the protein's true molecular function (scaffolding/regulatory protein in peptidoglycan processing), the annotation uniquely assigns GO:0004175. The other three options have zero supporting annotation or sequence evidence. However, the 'correct' answer itself is scientifically questionable given the experimental evidence of non-catalytic function."
  },
  "important_caveats": [
    "The GO:0004175 annotation is IEA:UniProtKB-ARBA only (automatic rule-based inference), not experimentally verified.",
    "Experimental evidence (PubMed:33593946) explicitly describes a 'non-catalytic role' and 'scaffold protein' function, directly contradicting endopeptidase (catalytic) activity.",
    "The protein's true molecular function (scaffolding, protein binding, regulation of SagB) is not among the four options.",
    "The ARBA rule likely assigned endopeptidase activity based on the protein's involvement in peptidoglycan cleavage pathways, conflating pathway participation with intrinsic catalytic function.",
    "Sequence identity to UniProt A0A0H3KA40 is confirmed (SHA256 match), but the model receives no accession or name information."
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

**Accession:** `A0A0H3KA40` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 36. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:09.578744+00:00.  

```json
"A0A0H3KA40"
```

Source SHA-256: `01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:09.578744+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q2FVT1","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"20923422","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"33593946","source":"PubMed"}],"value":"Involved in bacterial cell envelope homeostasis (PubMed:33593946). Regulates peptidoglycan processing by N-acetylglucosaminidase SagB, perhaps acting as a scaffold protein (PubMed:33593946). As part of a complex with SagB, probably plays a non-catalytic role in the cleavage of nascent peptidoglycan, preferentially yielding longer lipid-linked oligomers (By similarity). Pleiotropic regulator of gene expression, probably acting via interactions with multiple two-component systems (By similarity). Plays a role in the abundant deposition of the immunoglobulin G-binding protein A (spa) at the cross-wall, a subcellular structure that initially arises from cytokinesis (PubMed:20923422)"}]}
```

Source SHA-256: `01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)  
**Locator:** `/uniProtKBCrossReferences/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:09.578744+00:00.  

```json
{"database":"GO","id":"GO:0004175","properties":[{"key":"GoTerm","value":"F:endopeptidase activity"},{"key":"GoEvidenceType","value":"IEA:UniProtKB-ARBA"}]}
```

Source SHA-256: `01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H3KA40.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:09.578744+00:00.  

```json
{"citation":{"authors":["Willing S.","Schneewind O.","Missiakas D."],"citationCrossReferences":[{"database":"PubMed","id":"33593946"},{"database":"DOI","id":"10.1128/jb.00014-21"}],"citationType":"journal article","firstPage":"0","id":"33593946","journal":"J. Bacteriol.","lastPage":"0","publicationDate":"2021","title":"Regulated cleavage of glycan strands by the murein hydrolase SagB in S. aureus involves a direct interaction with LyrA (SpdC).","volume":"203"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","INTERACTION WITH SAGB","MUTAGENESIS OF GLU-135; ARG-139; ARG-196 AND HIS-210"]}
```

Source SHA-256: `01b319fc1f34daeda156e8cfc7e6f4bb541e8c4bcb4a73e8f3c4f78c8d2c62d2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)  
**Locator:** `lines 32-39`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:11.851883+00:00.  

```text
RN   [3] {ECO:0000305}
RP   FUNCTION, INTERACTION WITH SAGB, AND MUTAGENESIS OF GLU-135; ARG-139;
RP   ARG-196 AND HIS-210.
RX   PubMed=33593946; DOI=10.1128/jb.00014-21;
RA   Willing S., Schneewind O., Missiakas D.;
RT   "Regulated cleavage of glycan strands by the murein hydrolase SagB in S.
RT   aureus involves a direct interaction with LyrA (SpdC).";
RL   J. Bacteriol. 203:0-0(2021).
```

Source SHA-256: `d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)  
**Locator:** `lines 40-52`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:11.851883+00:00.  

```text
CC   -!- FUNCTION: Involved in bacterial cell envelope homeostasis
CC       (PubMed:33593946). Regulates peptidoglycan processing by N-
CC       acetylglucosaminidase SagB, perhaps acting as a scaffold protein
CC       (PubMed:33593946). As part of a complex with SagB, probably plays a
CC       non-catalytic role in the cleavage of nascent peptidoglycan,
CC       preferentially yielding longer lipid-linked oligomers (By similarity).
CC       Pleiotropic regulator of gene expression, probably acting via
CC       interactions with multiple two-component systems (By similarity). Plays
CC       a role in the abundant deposition of the immunoglobulin G-binding
CC       protein A (spa) at the cross-wall, a subcellular structure that
CC       initially arises from cytokinesis (PubMed:20923422).
CC       {ECO:0000250|UniProtKB:Q2FVT1, ECO:0000269|PubMed:20923422,
CC       ECO:0000269|PubMed:33593946}.
```

Source SHA-256: `d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H3KA40?format=txt&versions=36)  
**Locator:** `lines 86-86`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:24:11.851883+00:00.  

```text
DR   GO; GO:0004175; F:endopeptidase activity; IEA:UniProtKB-ARBA.
```

Source SHA-256: `d02c88a1544f67f6b8c7af47b40f478812539c62fe01fc0b43e7958088f0d2ff`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 2. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
