# GO_molecular_function_0004

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **D** — serine-type endopeptidase inhibitor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSRILFVFLAVMAIFSTSFGQQCGLNEEFKSCGSCEPTCAKPRVTICTMECKIGCQCKSGYLRNGEGTCVLPEKC

[Multiple Choices]
A. glycosyltransferase activity
B. zinc ion binding
C. glycine hydroxymethyltransferase activity
D. serine-type endopeptidase inhibitor activity
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

> The exact 75-residue sequence matches the cited UniProt record. That record reports experimentally supported inhibition of serine proteases and assigns GO:0004867 with IDA evidence, supporting D.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment and short, cysteine-rich sequence suggest a secreted peptide, making the large-enzyme choices A and C unlikely. These features do not establish serine-protease inhibition rather than another activity, including possible metal binding.


**Missing item-specific fact**

> The protein-specific finding that this peptide inhibits serine proteases, which is established by the cited experimental annotation but is not supplied in the question.


**Reason**

> Sequence architecture narrows the choices but does not uniquely establish the molecular activity. Selecting D with confidence depends on an item-specific functional fact absent from the model input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer evidence supports D. The sequence alone leaves uncertainty, but does not establish that another listed option is also a correct molecular-function annotation.


### Important caveats

- The functional assay and annotation are reviewer-only evidence, not information provided to the evaluated model.
- The sequence match is exact; the author’s precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and short, cysteine-rich sequence suggest a secreted peptide, making the large-enzyme choices A and C unlikely. These features do not establish serine-protease inhibition rather than another activity, including possible metal binding.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific finding that this peptide inhibits serine proteases, which is established by the cited experimental annotation but is not supplied in the question.",
    "reason": "Sequence architecture narrows the choices but does not uniquely establish the molecular activity. Selecting D with confidence depends on an item-specific functional fact absent from the model input."
  },
  "case_id": "GO_molecular_function_0004",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact 75-residue sequence matches the cited UniProt record. That record reports experimentally supported inhibition of serine proteases and assigns GO:0004867 with IDA evidence, supporting D."
  },
  "important_caveats": [
    "The functional assay and annotation are reviewer-only evidence, not information provided to the evaluated model.",
    "The sequence match is exact; the author’s precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D. The sequence alone leaves uncertainty, but does not establish that another listed option is also a correct molecular-function annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0004",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 75-residue sequence matches the cited UniProt record. That record reports experimentally supported inhibition of serine proteases and assigns GO:0004867 with IDA evidence, supporting D.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment and short, cysteine-rich sequence suggest a secreted peptide, making the large-enzyme choices A and C unlikely. These features do not establish serine-protease inhibition rather than another activity, including possible metal binding.",
    "missing_item_specific_fact": "The protein-specific finding that this peptide inhibits serine proteases, which is established by the cited experimental annotation but is not supplied in the question.",
    "reason": "Sequence architecture narrows the choices but does not uniquely establish the molecular activity. Selecting D with confidence depends on an item-specific functional fact absent from the model input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer evidence supports D. The sequence alone leaves uncertainty, but does not establish that another listed option is also a correct molecular-function annotation."
  },
  "important_caveats": [
    "The functional assay and annotation are reviewer-only evidence, not information provided to the evaluated model.",
    "The sequence match is exact; the author’s precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry U5T7E4 (sequence matched exactly, 75 aa, SHA256 identical) annotates this protein as 'Venom serine protease inhibitor BiVSPI' with GO:0004867 (serine-type endopeptidase inhibitor activity) supported by IDA (Inferred by Direct Assay, ECO:0000269) from PubMed:24158004. Experimental IC50/Ki values against chymotrypsin, subtilisin A, and proteinase K are reported. The GO annotation is an IDA-level assignment, not a computational transfer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 75-residue sequence contains a clear N-terminal hydrophobic signal peptide (MSRILFVFLAVMAIFSTSF), eight cysteines spaced in patterns consistent with multiple disulfide bonds (C-x-x-C, C-x-C motifs typical of small inhibitor folds), and no catalytic residues (no Ser-His-Asp triad, no PLP-binding lysine, no GT-A/B motifs, no canonical Cys2His2/Cys4 zinc-binding cluster). Options A (glycosyltransferase, typically >300 aa) and C (glycine hydroxymethyltransferase, a ~350-aa PLP-dependent enzyme) are eliminated by the protein's tiny size and absence of enzyme motifs. Option B (zinc ion binding) is disfavored because the cysteine spacing matches disulfide-bonded inhibitor scaffolds rather than tetrahedral zinc-coordination geometries, and no histidines are present. The remaining architecture—small secreted, disulfide-stabilized, non-catalytic—is the hallmark of a small protease inhibitor, making D the best-supported choice by positive structural inference and elimination.


**Missing item-specific fact**

> None strictly required; however, confirming the specific 'serine-type' target class (as opposed to, e.g., a cysteine-protease inhibitor) relies on recognizing the particular inhibitor fold or knowing the venom context, which adds predictive difficulty but does not introduce an unanswerable lookup gap among the four given options.


**Reason**

> General knowledge of protein size ranges, signal peptides, disulfide-bond motifs, catalytic-site requirements, and zinc-coordination geometry provides concrete grounds to eliminate A, C, and B, and to positively infer a small secreted inhibitor fold consistent with D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C describe large enzymes incompatible with a 75-aa protein. Option B lacks a convincing zinc-coordination motif. D is the only option consistent with the observed architecture. No other option is defensible.


### Important caveats

- The GO annotation is IDA (direct assay) from a single 2014 study; the protein also exhibits antimicrobial activity against bacteria and fungi, but the GO Molecular Function term assigned is specifically the protease-inhibitor activity.
- The reviewer-only UniProt accession and metadata were not available to the evaluated model; reasoning must proceed from the raw sequence and general biology.
- The protein is a precursor (75 aa includes the signal peptide); the mature inhibitor is shorter, but this does not affect the GO MF assignment.
- The 'serine-type' specificity is supported by experimental data showing activity against chymotrypsin/subtilisin/proteinase K but not trypsin/elastase; a model reasoning purely from sequence might infer 'protease inhibitor' broadly but would still select D as the closest GO term among the four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 75-residue sequence contains a clear N-terminal hydrophobic signal peptide (MSRILFVFLAVMAIFSTSF), eight cysteines spaced in patterns consistent with multiple disulfide bonds (C-x-x-C, C-x-C motifs typical of small inhibitor folds), and no catalytic residues (no Ser-His-Asp triad, no PLP-binding lysine, no GT-A/B motifs, no canonical Cys2His2/Cys4 zinc-binding cluster). Options A (glycosyltransferase, typically >300 aa) and C (glycine hydroxymethyltransferase, a ~350-aa PLP-dependent enzyme) are eliminated by the protein's tiny size and absence of enzyme motifs. Option B (zinc ion binding) is disfavored because the cysteine spacing matches disulfide-bonded inhibitor scaffolds rather than tetrahedral zinc-coordination geometries, and no histidines are present. The remaining architecture—small secreted, disulfide-stabilized, non-catalytic—is the hallmark of a small protease inhibitor, making D the best-supported choice by positive structural inference and elimination.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; however, confirming the specific 'serine-type' target class (as opposed to, e.g., a cysteine-protease inhibitor) relies on recognizing the particular inhibitor fold or knowing the venom context, which adds predictive difficulty but does not introduce an unanswerable lookup gap among the four given options.",
    "reason": "General knowledge of protein size ranges, signal peptides, disulfide-bond motifs, catalytic-site requirements, and zinc-coordination geometry provides concrete grounds to eliminate A, C, and B, and to positively infer a small secreted inhibitor fold consistent with D."
  },
  "case_id": "GO_molecular_function_0004",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "H1"
    ],
    "judgment": "supported",
    "reason": "UniProt entry U5T7E4 (sequence matched exactly, 75 aa, SHA256 identical) annotates this protein as 'Venom serine protease inhibitor BiVSPI' with GO:0004867 (serine-type endopeptidase inhibitor activity) supported by IDA (Inferred by Direct Assay, ECO:0000269) from PubMed:24158004. Experimental IC50/Ki values against chymotrypsin, subtilisin A, and proteinase K are reported. The GO annotation is an IDA-level assignment, not a computational transfer."
  },
  "important_caveats": [
    "The GO annotation is IDA (direct assay) from a single 2014 study; the protein also exhibits antimicrobial activity against bacteria and fungi, but the GO Molecular Function term assigned is specifically the protease-inhibitor activity.",
    "The reviewer-only UniProt accession and metadata were not available to the evaluated model; reasoning must proceed from the raw sequence and general biology.",
    "The protein is a precursor (75 aa includes the signal peptide); the mature inhibitor is shorter, but this does not affect the GO MF assignment.",
    "The 'serine-type' specificity is supported by experimental data showing activity against chymotrypsin/subtilisin/proteinase K but not trypsin/elastase; a model reasoning purely from sequence might infer 'protease inhibitor' broadly but would still select D as the closest GO term among the four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C describe large enzymes incompatible with a 75-aa protein. Option B lacks a convincing zinc-coordination motif. D is the only option consistent with the observed architecture. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0004",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry U5T7E4 (sequence matched exactly, 75 aa, SHA256 identical) annotates this protein as 'Venom serine protease inhibitor BiVSPI' with GO:0004867 (serine-type endopeptidase inhibitor activity) supported by IDA (Inferred by Direct Assay, ECO:0000269) from PubMed:24158004. Experimental IC50/Ki values against chymotrypsin, subtilisin A, and proteinase K are reported. The GO annotation is an IDA-level assignment, not a computational transfer.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 75-residue sequence contains a clear N-terminal hydrophobic signal peptide (MSRILFVFLAVMAIFSTSF), eight cysteines spaced in patterns consistent with multiple disulfide bonds (C-x-x-C, C-x-C motifs typical of small inhibitor folds), and no catalytic residues (no Ser-His-Asp triad, no PLP-binding lysine, no GT-A/B motifs, no canonical Cys2His2/Cys4 zinc-binding cluster). Options A (glycosyltransferase, typically >300 aa) and C (glycine hydroxymethyltransferase, a ~350-aa PLP-dependent enzyme) are eliminated by the protein's tiny size and absence of enzyme motifs. Option B (zinc ion binding) is disfavored because the cysteine spacing matches disulfide-bonded inhibitor scaffolds rather than tetrahedral zinc-coordination geometries, and no histidines are present. The remaining architecture—small secreted, disulfide-stabilized, non-catalytic—is the hallmark of a small protease inhibitor, making D the best-supported choice by positive structural inference and elimination.",
    "missing_item_specific_fact": "None strictly required; however, confirming the specific 'serine-type' target class (as opposed to, e.g., a cysteine-protease inhibitor) relies on recognizing the particular inhibitor fold or knowing the venom context, which adds predictive difficulty but does not introduce an unanswerable lookup gap among the four given options.",
    "reason": "General knowledge of protein size ranges, signal peptides, disulfide-bond motifs, catalytic-site requirements, and zinc-coordination geometry provides concrete grounds to eliminate A, C, and B, and to positively infer a small secreted inhibitor fold consistent with D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C describe large enzymes incompatible with a 75-aa protein. Option B lacks a convincing zinc-coordination motif. D is the only option consistent with the observed architecture. No other option is defensible."
  },
  "important_caveats": [
    "The GO annotation is IDA (direct assay) from a single 2014 study; the protein also exhibits antimicrobial activity against bacteria and fungi, but the GO Molecular Function term assigned is specifically the protease-inhibitor activity.",
    "The reviewer-only UniProt accession and metadata were not available to the evaluated model; reasoning must proceed from the raw sequence and general biology.",
    "The protein is a precursor (75 aa includes the signal peptide); the mature inhibitor is shorter, but this does not affect the GO MF assignment.",
    "The 'serine-type' specificity is supported by experimental data showing activity against chymotrypsin/subtilisin/proteinase K but not trypsin/elastase; a model reasoning purely from sequence might infer 'protease inhibitor' broadly but would still select D as the closest GO term among the four choices."
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

**Accession:** `U5T7E4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 31. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/U5T7E4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:01.726773+00:00.  

```json
{"flag":"Precursor","recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"24158004","source":"PubMed"}],"value":"Venom serine protease inhibitor BiVSPI"}}}
```

Source SHA-256: `fbc5842cbc1fb8fdcf4a2ce81aee2d573a2a31b81dfaeaf9b3fede6c3e1b848c`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/U5T7E4.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:01.726773+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"24158004","source":"PubMed"}],"value":"Antimicrobial venom serine protease inhibitor. Exhibits inhibitory activity against chymotrypsin (IC(50)=19.56 nM, Ki=15.24 nM) and microbial serine proteases, such as subtilisin A (IC(50)=6.57 nM, Ki=6.83 nM) and proteinase K (IC(50)=7.11 nM, Ki=7.02 nM). Has not activity against trypsin, plasmin, tPA, thrombin, factor Xa or elastase. Binds and inhibits Gram-positive bacteria (B.subtilis (MIC=29.45 uM), B.thuringiensis (MIC=91.03 uM)) and the entomopathogenic fungus B.bassiana (MIC=30.09 uM) but not to E.coli"}]}
```

Source SHA-256: `fbc5842cbc1fb8fdcf4a2ce81aee2d573a2a31b81dfaeaf9b3fede6c3e1b848c`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/U5T7E4.json)  
**Locator:** `/uniProtKBCrossReferences/5`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:34:01.726773+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"24158004","source":"PubMed"}],"id":"GO:0004867","properties":[{"key":"GoTerm","value":"F:serine-type endopeptidase inhibitor activity"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `fbc5842cbc1fb8fdcf4a2ce81aee2d573a2a31b81dfaeaf9b3fede6c3e1b848c`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/U5T7E4?format=txt&versions=31)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:34:04.526434+00:00.  

```text
ID   TILVI_BOMIG             Reviewed;          75 AA.
AC   U5T7E4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   22-JAN-2014, sequence version 1.
DT   28-JAN-2026, entry version 31.
DE   RecName: Full=Venom serine protease inhibitor BiVSPI {ECO:0000303|PubMed:24158004};
DE   Flags: Precursor;
OS   Bombus ignitus (Bumblebee).
OC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;
OC   Neoptera; Endopterygota; Hymenoptera; Apocrita; Aculeata; Apoidea;
OC   Anthophila; Apidae; Bombus; Bombus.
OX   NCBI_TaxID=130704;
```

Source SHA-256: `d7145a1a4accaf1efa4f61bacd7f1b5022feb4fe402ba99e5f1997756e2c42eb`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/U5T7E4?format=txt&versions=31)  
**Locator:** `lines 22-30`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:34:04.526434+00:00.  

```text
CC   -!- FUNCTION: Antimicrobial venom serine protease inhibitor. Exhibits
CC       inhibitory activity against chymotrypsin (IC(50)=19.56 nM, Ki=15.24 nM)
CC       and microbial serine proteases, such as subtilisin A (IC(50)=6.57 nM,
CC       Ki=6.83 nM) and proteinase K (IC(50)=7.11 nM, Ki=7.02 nM). Has not
CC       activity against trypsin, plasmin, tPA, thrombin, factor Xa or
CC       elastase. Binds and inhibits Gram-positive bacteria (B.subtilis
CC       (MIC=29.45 uM), B.thuringiensis (MIC=91.03 uM)) and the
CC       entomopathogenic fungus B.bassiana (MIC=30.09 uM) but not to E.coli.
CC       {ECO:0000269|PubMed:24158004}.
```

Source SHA-256: `d7145a1a4accaf1efa4f61bacd7f1b5022feb4fe402ba99e5f1997756e2c42eb`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/U5T7E4?format=txt&versions=31)  
**Locator:** `lines 46-46`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 31 / 1.  
**Retrieved:** 2026-11-02T04:34:04.526434+00:00.  

```text
DR   GO; GO:0004867; F:serine-type endopeptidase inhibitor activity; IDA:UniProtKB.
```

Source SHA-256: `d7145a1a4accaf1efa4f61bacd7f1b5022feb4fe402ba99e5f1997756e2c42eb`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 4. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
