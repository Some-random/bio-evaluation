# GO_biological_process_0094

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_biological_process`  
**Author expected answer:** **D** — cellular response to acidic pH

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MCNVSQDSCNIDSRLDSLFPPTLYIFVMVIGFPTNCLSLWAAFVQVRQKNELGVYLLNLSISDLLYIATLPPWVNYFLHQDNWIHGPESCKLFGFILYTNIYISIGFLSCISVDRYLAVAHPLKFAKVRRVKTAAVVSAVVWAIEIGANSAPLFHNELFEDRFNHTFCFEKYPMEDWVAQMNLYRVFVGFLFPWVLMLFCYQGILRAVKTNVSTEREEKAKIKRLALSLIAILLFCFAPYHLILLSRSVVYLGQPCDCTFEENIFTAYHVSLALTSLNCVADPILYCLANEGARSEVTRGLAPLMKFFSASRPNMDSFARSVTLDTPWSSRRAAAPSPRSWSLCGQTGGRGRRSRVRRRRDCKC

[Multiple Choices]
A. symbiont-mediated suppression of host innate immune response
B. lysine biosynthetic process via aminoadipic acid
C. erythrocyte enucleation
D. cellular response to acidic pH
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the sequence in the identified GPR4 entry. That entry describes a proton-sensing receptor activated by extracellular pH and annotates cellular response to acidic pH with IDA evidence; the archived entry also contains this annotation.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence's multiple hydrophobic segments support a membrane receptor, consistent with a seven-transmembrane GPCR. That broad inference does not establish proton sensing or a cellular response to acidic pH.


**Missing item-specific fact**

> The protein-specific evidence that this GPCR is GPR4 and is activated by extracellular pH, supporting the acidic-pH response annotation.


**Reason**

> The sequence alone does not meaningfully distinguish this receptor's ligand/stimulus and biological process from the many possible functions of GPCRs. The specific proton-sensing function requires an item-specific annotation or experimental finding absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the sequence-matched protein's documented proton-sensing function supports D; the other choices describe unrelated processes.


### Important caveats

- The supporting GO annotation is recorded as IDA and the function annotation cites a publication, but the primary study was not independently reviewed here.
- The reviewer-only identity and annotation evidence was not supplied to the evaluated model; the author’s exact source snapshot is unknown.
- Support for D does not establish that it is the protein's exclusive or uniquely primary biological process.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's multiple hydrophobic segments support a membrane receptor, consistent with a seven-transmembrane GPCR. That broad inference does not establish proton sensing or a cellular response to acidic pH.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific evidence that this GPCR is GPR4 and is activated by extracellular pH, supporting the acidic-pH response annotation.",
    "reason": "The sequence alone does not meaningfully distinguish this receptor's ligand/stimulus and biological process from the many possible functions of GPCRs. The specific proton-sensing function requires an item-specific annotation or experimental finding absent from the input."
  },
  "case_id": "GO_biological_process_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the identified GPR4 entry. That entry describes a proton-sensing receptor activated by extracellular pH and annotates cellular response to acidic pH with IDA evidence; the archived entry also contains this annotation."
  },
  "important_caveats": [
    "The supporting GO annotation is recorded as IDA and the function annotation cites a publication, but the primary study was not independently reviewed here.",
    "The reviewer-only identity and annotation evidence was not supplied to the evaluated model; the author’s exact source snapshot is unknown.",
    "Support for D does not establish that it is the protein's exclusive or uniquely primary biological process."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence-matched protein's documented proton-sensing function supports D; the other choices describe unrelated processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the identified GPR4 entry. That entry describes a proton-sensing receptor activated by extracellular pH and annotates cellular response to acidic pH with IDA evidence; the archived entry also contains this annotation.",
    "evidence_ids": ["C1", "C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence's multiple hydrophobic segments support a membrane receptor, consistent with a seven-transmembrane GPCR. That broad inference does not establish proton sensing or a cellular response to acidic pH.",
    "missing_item_specific_fact": "The protein-specific evidence that this GPCR is GPR4 and is activated by extracellular pH, supporting the acidic-pH response annotation.",
    "reason": "The sequence alone does not meaningfully distinguish this receptor's ligand/stimulus and biological process from the many possible functions of GPCRs. The specific proton-sensing function requires an item-specific annotation or experimental finding absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the sequence-matched protein's documented proton-sensing function supports D; the other choices describe unrelated processes."
  },
  "important_caveats": [
    "The supporting GO annotation is recorded as IDA and the function annotation cites a publication, but the primary study was not independently reviewed here.",
    "The reviewer-only identity and annotation evidence was not supplied to the evaluated model; the author’s exact source snapshot is unknown.",
    "Support for D does not establish that it is the protein's exclusive or uniquely primary biological process."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A4W3GG95 (cmGPR4, Callorhinchus milii) carries GO:0071468 'cellular response to acidic pH' with IDA evidence (ECO:0000314) from PubMed:39753131, a 2025 Cell paper demonstrating proton-sensing function. The FUNCTION comment explicitly states: 'Proton-sensing G protein-coupled receptor activated by extracellular pH, which is required to monitor pH changes and generate adaptive reactions.' The sequence in the benchmark matches the canonical entry (SHA-256 confirmed). The annotation is experimentally supported (IDA), not merely computational inference.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays hallmark class-A GPCR features: seven hydrophobic transmembrane stretches, the conserved DRY motif (visible in 'SISVDRYLAVAHPLK'), and a C-terminal cytoplasmic tail with basic residues. This identifies the protein as a G protein-coupled receptor, a membrane signal-transducer. Among the four options: (A) symbiont-mediated suppression of host innate immune response applies to pathogen/symbiont effector proteins, not vertebrate membrane receptors; (B) lysine biosynthetic process via aminoadipic acid is a fungal/plant cytosolic enzymatic pathway incompatible with a 7-TM receptor; (C) erythrocyte enucleation is a developmental process mediated by transcription factors and cytoskeletal regulators, not GPCRs. Only option D, 'cellular response to acidic pH,' describes a signaling process in which a GPCR can participate. Thus, general GPCR identification plus elimination of the three incompatible options yields D.


**Missing item-specific fact**

> Positive identification of the specific proton-sensing (GPR4) identity from the sequence alone would require knowledge of the particular residue determinants for extracellular pH sensing (e.g., Glu-51, Val-119, Pro-122, Leu-123 per PubMed:39753131). However, this is not needed to select D, because the elimination argument suffices among the given choices.


**Reason**

> The reasoning chain—recognize GPCR architecture from the sequence, then eliminate options that are categorically incompatible with a vertebrate 7-TM receptor—is a valid application of general structural biology and functional-genomics knowledge. The correct answer is reached without needing to recall the specific UniProt annotation for this ghost-shark ortholog.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four provided options, only D is biologically compatible with a vertebrate GPCR. The other three describe processes (pathogen immune suppression, fungal amino-acid biosynthesis, erythrocyte maturation) that are categorically incompatible with a 7-TM membrane receptor. GO:0007189 (adenylate cyclase-activating GPCR signaling pathway) is also annotated on this protein but is not among the choices, so it does not create ambiguity.


### Important caveats

- The GO:0071468 annotation is IDA (direct assay) from a 2025 Cell publication, giving strong experimental support, but the annotation was added to Swiss-Prot in January 2026 (entry version 30+); the benchmark author's source snapshot is unknown and may predate this annotation.
- The protein is a ghost shark (Callorhinchus milii) ortholog of GPR4; the proton-sensing mechanism was characterized in Mus and Xenopus GPR4 and transferred by similarity plus direct assay on the ghost-shark ortholog.
- The elimination-based reasoning is valid but somewhat coarse: it distinguishes 'GPCR-compatible' from 'non-GPCR' options rather than positively identifying proton sensing from sequence features alone.
- The reviewer-only evidence (UniProt accession, GO annotations, PubMed reference) was not available to the evaluated model; the model must rely on sequence-derived inference and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays hallmark class-A GPCR features: seven hydrophobic transmembrane stretches, the conserved DRY motif (visible in 'SISVDRYLAVAHPLK'), and a C-terminal cytoplasmic tail with basic residues. This identifies the protein as a G protein-coupled receptor, a membrane signal-transducer. Among the four options: (A) symbiont-mediated suppression of host innate immune response applies to pathogen/symbiont effector proteins, not vertebrate membrane receptors; (B) lysine biosynthetic process via aminoadipic acid is a fungal/plant cytosolic enzymatic pathway incompatible with a 7-TM receptor; (C) erythrocyte enucleation is a developmental process mediated by transcription factors and cytoskeletal regulators, not GPCRs. Only option D, 'cellular response to acidic pH,' describes a signaling process in which a GPCR can participate. Thus, general GPCR identification plus elimination of the three incompatible options yields D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Positive identification of the specific proton-sensing (GPR4) identity from the sequence alone would require knowledge of the particular residue determinants for extracellular pH sensing (e.g., Glu-51, Val-119, Pro-122, Leu-123 per PubMed:39753131). However, this is not needed to select D, because the elimination argument suffices among the given choices.",
    "reason": "The reasoning chain—recognize GPCR architecture from the sequence, then eliminate options that are categorically incompatible with a vertebrate 7-TM receptor—is a valid application of general structural biology and functional-genomics knowledge. The correct answer is reached without needing to recall the specific UniProt annotation for this ghost-shark ortholog."
  },
  "case_id": "GO_biological_process_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "C8",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A4W3GG95 (cmGPR4, Callorhinchus milii) carries GO:0071468 'cellular response to acidic pH' with IDA evidence (ECO:0000314) from PubMed:39753131, a 2025 Cell paper demonstrating proton-sensing function. The FUNCTION comment explicitly states: 'Proton-sensing G protein-coupled receptor activated by extracellular pH, which is required to monitor pH changes and generate adaptive reactions.' The sequence in the benchmark matches the canonical entry (SHA-256 confirmed). The annotation is experimentally supported (IDA), not merely computational inference."
  },
  "important_caveats": [
    "The GO:0071468 annotation is IDA (direct assay) from a 2025 Cell publication, giving strong experimental support, but the annotation was added to Swiss-Prot in January 2026 (entry version 30+); the benchmark author's source snapshot is unknown and may predate this annotation.",
    "The protein is a ghost shark (Callorhinchus milii) ortholog of GPR4; the proton-sensing mechanism was characterized in Mus and Xenopus GPR4 and transferred by similarity plus direct assay on the ghost-shark ortholog.",
    "The elimination-based reasoning is valid but somewhat coarse: it distinguishes 'GPCR-compatible' from 'non-GPCR' options rather than positively identifying proton sensing from sequence features alone.",
    "The reviewer-only evidence (UniProt accession, GO annotations, PubMed reference) was not available to the evaluated model; the model must rely on sequence-derived inference and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided options, only D is biologically compatible with a vertebrate GPCR. The other three describe processes (pathogen immune suppression, fungal amino-acid biosynthesis, erythrocyte maturation) that are categorically incompatible with a 7-TM membrane receptor. GO:0007189 (adenylate cyclase-activating GPCR signaling pathway) is also annotated on this protein but is not among the choices, so it does not create ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A4W3GG95 (cmGPR4, Callorhinchus milii) carries GO:0071468 'cellular response to acidic pH' with IDA evidence (ECO:0000314) from PubMed:39753131, a 2025 Cell paper demonstrating proton-sensing function. The FUNCTION comment explicitly states: 'Proton-sensing G protein-coupled receptor activated by extracellular pH, which is required to monitor pH changes and generate adaptive reactions.' The sequence in the benchmark matches the canonical entry (SHA-256 confirmed). The annotation is experimentally supported (IDA), not merely computational inference.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "C8", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays hallmark class-A GPCR features: seven hydrophobic transmembrane stretches, the conserved DRY motif (visible in 'SISVDRYLAVAHPLK'), and a C-terminal cytoplasmic tail with basic residues. This identifies the protein as a G protein-coupled receptor, a membrane signal-transducer. Among the four options: (A) symbiont-mediated suppression of host innate immune response applies to pathogen/symbiont effector proteins, not vertebrate membrane receptors; (B) lysine biosynthetic process via aminoadipic acid is a fungal/plant cytosolic enzymatic pathway incompatible with a 7-TM receptor; (C) erythrocyte enucleation is a developmental process mediated by transcription factors and cytoskeletal regulators, not GPCRs. Only option D, 'cellular response to acidic pH,' describes a signaling process in which a GPCR can participate. Thus, general GPCR identification plus elimination of the three incompatible options yields D.",
    "missing_item_specific_fact": "Positive identification of the specific proton-sensing (GPR4) identity from the sequence alone would require knowledge of the particular residue determinants for extracellular pH sensing (e.g., Glu-51, Val-119, Pro-122, Leu-123 per PubMed:39753131). However, this is not needed to select D, because the elimination argument suffices among the given choices.",
    "reason": "The reasoning chain—recognize GPCR architecture from the sequence, then eliminate options that are categorically incompatible with a vertebrate 7-TM receptor—is a valid application of general structural biology and functional-genomics knowledge. The correct answer is reached without needing to recall the specific UniProt annotation for this ghost-shark ortholog."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four provided options, only D is biologically compatible with a vertebrate GPCR. The other three describe processes (pathogen immune suppression, fungal amino-acid biosynthesis, erythrocyte maturation) that are categorically incompatible with a 7-TM membrane receptor. GO:0007189 (adenylate cyclase-activating GPCR signaling pathway) is also annotated on this protein but is not among the choices, so it does not create ambiguity."
  },
  "important_caveats": [
    "The GO:0071468 annotation is IDA (direct assay) from a 2025 Cell publication, giving strong experimental support, but the annotation was added to Swiss-Prot in January 2026 (entry version 30+); the benchmark author's source snapshot is unknown and may predate this annotation.",
    "The protein is a ghost shark (Callorhinchus milii) ortholog of GPR4; the proton-sensing mechanism was characterized in Mus and Xenopus GPR4 and transferred by similarity plus direct assay on the ghost-shark ortholog.",
    "The elimination-based reasoning is valid but somewhat coarse: it distinguishes 'GPCR-compatible' from 'non-GPCR' options rather than positively identifying proton sensing from sequence features alone.",
    "The reviewer-only evidence (UniProt accession, GO annotations, PubMed reference) was not available to the evaluated model; the model must rely on sequence-derived inference and general biological knowledge."
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

**Accession:** `A0A4W3GG95` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
"A0A4W3GG95"
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"G protein-coupled receptor 4"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"39753131","source":"PubMed"}],"value":"cmGPR4"}]}}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A6I8PUB9","source":"UniProtKB"},{"evidenceCode":"ECO:0000269","id":"39753131","source":"PubMed"}],"value":"Proton-sensing G protein-coupled receptor activated by extracellular pH, which is required to monitor pH changes and generate adaptive reactions (PubMed:39753131). Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate cyclase (By similarity)"}]}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/uniProtKBCrossReferences/10`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"39753131","source":"PubMed"}],"id":"GO:0071468","properties":[{"key":"GoTerm","value":"P:cellular response to acidic pH"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A4W3GG95.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:47.202623+00:00.  

```json
{"citation":{"authors":["Wen X.","Shang P.","Chen H.","Guo L.","Rong N.","Jiang X.","Li X.","Liu J.","Yang G.","Zhang J.","Zhu K.","Meng Q.","He X.","Wang Z.","Liu Z.","Cheng H.","Zheng Y.","Zhang B.","Pang J.","Liu Z.","Xiao P.","Chen Y.","Liu L.","Luo F.","Yu X.","Yi F.","Zhang P.","Yang F.","Deng C.","Sun J.P."],"citationCrossReferences":[{"database":"PubMed","id":"39753131"},{"database":"DOI","id":"10.1016/j.cell.2024.12.001"}],"citationType":"journal article","firstPage":"653","id":"39753131","journal":"Cell","lastPage":"670","publicationDate":"2025","title":"Evolutionary study and structural basis of proton sensing by Mus GPR4 and Xenopus GPR4.","volume":"188"},"referenceNumber":2,"referencePositions":["FUNCTION","MUTAGENESIS OF GLU-51; VAL-119; PRO-122 AND LEU-123"]}
```

Source SHA-256: `a92b2a2611b3e831e67c290051c3b607ae4d71a21502ae38da2c507908426245`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)  
**Locator:** `lines 31-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.027017+00:00.  

```text
CC   -!- FUNCTION: Proton-sensing G-protein coupled receptor activated by
CC       extracellular pH, which is required to monitor pH changes and generate
CC       adaptive reactions (PubMed:39753131). Ligand binding causes a
CC       conformation change that triggers signaling via guanine nucleotide-
CC       binding proteins (G proteins) and modulates the activity of downstream
CC       effectors, such as adenylate cyclase (By similarity).
CC       {ECO:0000250|UniProtKB:A0A6I8PUB9, ECO:0000269|PubMed:39753131}.
```

Source SHA-256: `2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A4W3GG95?format=txt&versions=30)  
**Locator:** `lines 67-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-01T06:27:31.027017+00:00.  

```text
DR   GO; GO:0071468; P:cellular response to acidic pH; IDA:UniProtKB.
```

Source SHA-256: `2de235f5ecdbc32faad1779acf9f8307edf330e58265fd2df418707701078865`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 94. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
