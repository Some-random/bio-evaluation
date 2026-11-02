# GO_molecular_function_0037

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_molecular_function`  
**Author expected answer:** **A** — DNA-binding transcription factor activity

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMGNKLTLPAELPDEQDLRAVLAYNMRLFRVNKGWSQEELARQCGLDRTYVSAVERKRWNIALSNIEKMAAALGVAAYQLLLPPQERLKLMTNSADTRQMPSESGI

[Multiple Choices]
A. DNA-binding transcription factor activity
B. riboflavin reductase (NADPH) activity
C. UDP-N-acetylglucosamine 2-epimerase activity
D. delta(3)-delta(2)-enoyl-CoA isomerase activity
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

> The exact sequence match is annotated as a transcriptional regulator that binds a specific DNA sequence; the function annotation carries experimental evidence code ECO:0000269. This supports choice A. The separate GO annotation is IBA-based, so it is computational inference rather than direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 106-residue sequence is consistent with a small, predominantly helical bacterial DNA-binding regulator, including a basic region compatible with DNA interaction. That profile favors a transcription-factor function over the listed metabolic enzyme activities, whose catalytic functions are not indicated by an evident motif in this sequence.


**Missing item-specific fact**

> Experimental confirmation that this particular protein binds a regulatory DNA site and modulates transcription is absent from the input; sequence-based reasoning supports the choice but does not establish that specific activity on its own.


**Reason**

> A defensible sequence-level fold/class inference distinguishes A from the three enzyme choices, though confirmation of the protein’s exact regulatory activity depends on item-specific evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the choices, the sequence-level profile favors a small DNA-binding transcription regulator; no listed enzyme activity is comparably supported.


### Important caveats

- The reviewer-only annotations and sequence identification were not supplied to the evaluated model.
- The experimental support is reported in the matched UniProt functional annotation; the cited primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 106-residue sequence is consistent with a small, predominantly helical bacterial DNA-binding regulator, including a basic region compatible with DNA interaction. That profile favors a transcription-factor function over the listed metabolic enzyme activities, whose catalytic functions are not indicated by an evident motif in this sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Experimental confirmation that this particular protein binds a regulatory DNA site and modulates transcription is absent from the input; sequence-based reasoning supports the choice but does not establish that specific activity on its own.",
    "reason": "A defensible sequence-level fold/class inference distinguishes A from the three enzyme choices, though confirmation of the protein’s exact regulatory activity depends on item-specific evidence."
  },
  "case_id": "GO_molecular_function_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a transcriptional regulator that binds a specific DNA sequence; the function annotation carries experimental evidence code ECO:0000269. This supports choice A. The separate GO annotation is IBA-based, so it is computational inference rather than direct experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only annotations and sequence identification were not supplied to the evaluated model.",
    "The experimental support is reported in the matched UniProt functional annotation; the cited primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, the sequence-level profile favors a small DNA-binding transcription regulator; no listed enzyme activity is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match is annotated as a transcriptional regulator that binds a specific DNA sequence; the function annotation carries experimental evidence code ECO:0000269. This supports choice A. The separate GO annotation is IBA-based, so it is computational inference rather than direct experimental evidence.",
    "evidence_ids": ["C5", "H3", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 106-residue sequence is consistent with a small, predominantly helical bacterial DNA-binding regulator, including a basic region compatible with DNA interaction. That profile favors a transcription-factor function over the listed metabolic enzyme activities, whose catalytic functions are not indicated by an evident motif in this sequence.",
    "missing_item_specific_fact": "Experimental confirmation that this particular protein binds a regulatory DNA site and modulates transcription is absent from the input; sequence-based reasoning supports the choice but does not establish that specific activity on its own.",
    "reason": "A defensible sequence-level fold/class inference distinguishes A from the three enzyme choices, though confirmation of the protein’s exact regulatory activity depends on item-specific evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the choices, the sequence-level profile favors a small DNA-binding transcription regulator; no listed enzyme activity is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only annotations and sequence identification were not supplied to the evaluated model.",
    "The experimental support is reported in the matched UniProt functional annotation; the cited primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (Q7DDD9, NHTF from Neisseria meningitidis MC58) is annotated as 'HTH-type transcriptional repressor NMB1204' and 'Neisseria hypothetical transcription factor.' Experimental evidence (PubMed:22373915, ECO:0000269) demonstrates it acts as a transcriptional regulator binding a specific palindromic DNA sequence (5'-TGTNANTNACA-3'). X-ray crystallography (PDB:3VK0, 1.88 Å) confirmed DNA-binding. GO:0003700 (DNA-binding transcription factor activity) is annotated (IBA:GO_Central), and GO:0003677 (DNA binding) is annotated (IEA:InterPro). The expected answer A matches the experimentally validated molecular function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [C8](#evidence-c8), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H5](#evidence-h5), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is only 106 amino acids long. Riboflavin reductase (FMN reductase family, EC 1.5.1.30) typically requires ~150-200+ residues for its FMN-binding and catalytic pocket; UDP-GlcNAc 2-epimerase (EC 5.1.3.14) is a multi-domain enzyme of ~300+ residues; delta(3)-delta(2)-enoyl-CoA isomerase (EC 5.3.3.8) requires a Tyr/Asp catalytic dyad in a ~250-residue alpha/beta fold. None of these enzymatic activities can be accommodated in a 106-residue polypeptide. Conversely, small bacterial HTH-type transcriptional repressors of ~100-110 residues (e.g., Trp repressor at 108 aa, Lac repressor headpiece) are well-established. The amino acid composition—charged residues interspersed with hydrophobic helical stretches—is consistent with a small DNA-binding regulatory protein rather than an enzyme requiring a complex active site.


**Missing item-specific fact**

> None critical. The size-exclusion argument eliminates all three enzymatic distractors on general biochemical grounds. Exact HTH motif identification would strengthen the case but is not strictly required to exclude B, C, and D.


**Reason**

> The 106-residue length imposes a hard structural constraint: the three enzymatic options require active-site architectures (cofactor pockets, multi-domain folds, catalytic dyads) that cannot exist in a protein of this size. This is a concrete biochemical/structural argument, not a vague heuristic. Small bacterial repressors of this length are a well-known protein class. Thus general biological reasoning meaningfully distinguishes A from B, C, and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three enzymatic distractors (B, C, D) are each incompatible with a 106-residue polypeptide based on the minimum structural requirements of their respective enzyme classes. Only option A (DNA-binding transcription factor activity) is consistent with the protein's size and composition.


### Important caveats

- The GO:0003700 annotation carries IBA:GO_Central (computational propagation), but the underlying experimental evidence (PubMed:22373915, PDB:3VK0) directly supports DNA binding and transcriptional regulation.
- The protein is named 'hypothetical transcription factor' in UniProt, indicating its full regulatory role was characterized relatively recently (2012 publication).
- The size-exclusion reasoning eliminates the enzymatic options but does not, by itself, prove the protein is specifically a transcription factor rather than some other small DNA-binding protein; however, among the four given choices, only A is structurally plausible for a 106-aa protein.
- The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what a model could infer from the 106-aa sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is only 106 amino acids long. Riboflavin reductase (FMN reductase family, EC 1.5.1.30) typically requires ~150-200+ residues for its FMN-binding and catalytic pocket; UDP-GlcNAc 2-epimerase (EC 5.1.3.14) is a multi-domain enzyme of ~300+ residues; delta(3)-delta(2)-enoyl-CoA isomerase (EC 5.3.3.8) requires a Tyr/Asp catalytic dyad in a ~250-residue alpha/beta fold. None of these enzymatic activities can be accommodated in a 106-residue polypeptide. Conversely, small bacterial HTH-type transcriptional repressors of ~100-110 residues (e.g., Trp repressor at 108 aa, Lac repressor headpiece) are well-established. The amino acid composition—charged residues interspersed with hydrophobic helical stretches—is consistent with a small DNA-binding regulatory protein rather than an enzyme requiring a complex active site.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The size-exclusion argument eliminates all three enzymatic distractors on general biochemical grounds. Exact HTH motif identification would strengthen the case but is not strictly required to exclude B, C, and D.",
    "reason": "The 106-residue length imposes a hard structural constraint: the three enzymatic options require active-site architectures (cofactor pockets, multi-domain folds, catalytic dyads) that cannot exist in a protein of this size. This is a concrete biochemical/structural argument, not a vague heuristic. Small bacterial repressors of this length are a well-known protein class. Thus general biological reasoning meaningfully distinguishes A from B, C, and D."
  },
  "case_id": "GO_molecular_function_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "C8",
      "H1",
      "H2",
      "H3",
      "H5",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein (Q7DDD9, NHTF from Neisseria meningitidis MC58) is annotated as 'HTH-type transcriptional repressor NMB1204' and 'Neisseria hypothetical transcription factor.' Experimental evidence (PubMed:22373915, ECO:0000269) demonstrates it acts as a transcriptional regulator binding a specific palindromic DNA sequence (5'-TGTNANTNACA-3'). X-ray crystallography (PDB:3VK0, 1.88 Å) confirmed DNA-binding. GO:0003700 (DNA-binding transcription factor activity) is annotated (IBA:GO_Central), and GO:0003677 (DNA binding) is annotated (IEA:InterPro). The expected answer A matches the experimentally validated molecular function."
  },
  "important_caveats": [
    "The GO:0003700 annotation carries IBA:GO_Central (computational propagation), but the underlying experimental evidence (PubMed:22373915, PDB:3VK0) directly supports DNA binding and transcriptional regulation.",
    "The protein is named 'hypothetical transcription factor' in UniProt, indicating its full regulatory role was characterized relatively recently (2012 publication).",
    "The size-exclusion reasoning eliminates the enzymatic options but does not, by itself, prove the protein is specifically a transcription factor rather than some other small DNA-binding protein; however, among the four given choices, only A is structurally plausible for a 106-aa protein.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what a model could infer from the 106-aa sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three enzymatic distractors (B, C, D) are each incompatible with a 106-residue polypeptide based on the minimum structural requirements of their respective enzyme classes. Only option A (DNA-binding transcription factor activity) is consistent with the protein's size and composition."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (Q7DDD9, NHTF from Neisseria meningitidis MC58) is annotated as 'HTH-type transcriptional repressor NMB1204' and 'Neisseria hypothetical transcription factor.' Experimental evidence (PubMed:22373915, ECO:0000269) demonstrates it acts as a transcriptional regulator binding a specific palindromic DNA sequence (5'-TGTNANTNACA-3'). X-ray crystallography (PDB:3VK0, 1.88 Å) confirmed DNA-binding. GO:0003700 (DNA-binding transcription factor activity) is annotated (IBA:GO_Central), and GO:0003677 (DNA binding) is annotated (IEA:InterPro). The expected answer A matches the experimentally validated molecular function.",
    "evidence_ids": ["C4", "C5", "C7", "C8", "H1", "H2", "H3", "H5", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is only 106 amino acids long. Riboflavin reductase (FMN reductase family, EC 1.5.1.30) typically requires ~150-200+ residues for its FMN-binding and catalytic pocket; UDP-GlcNAc 2-epimerase (EC 5.1.3.14) is a multi-domain enzyme of ~300+ residues; delta(3)-delta(2)-enoyl-CoA isomerase (EC 5.3.3.8) requires a Tyr/Asp catalytic dyad in a ~250-residue alpha/beta fold. None of these enzymatic activities can be accommodated in a 106-residue polypeptide. Conversely, small bacterial HTH-type transcriptional repressors of ~100-110 residues (e.g., Trp repressor at 108 aa, Lac repressor headpiece) are well-established. The amino acid composition—charged residues interspersed with hydrophobic helical stretches—is consistent with a small DNA-binding regulatory protein rather than an enzyme requiring a complex active site.",
    "missing_item_specific_fact": "None critical. The size-exclusion argument eliminates all three enzymatic distractors on general biochemical grounds. Exact HTH motif identification would strengthen the case but is not strictly required to exclude B, C, and D.",
    "reason": "The 106-residue length imposes a hard structural constraint: the three enzymatic options require active-site architectures (cofactor pockets, multi-domain folds, catalytic dyads) that cannot exist in a protein of this size. This is a concrete biochemical/structural argument, not a vague heuristic. Small bacterial repressors of this length are a well-known protein class. Thus general biological reasoning meaningfully distinguishes A from B, C, and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three enzymatic distractors (B, C, D) are each incompatible with a 106-residue polypeptide based on the minimum structural requirements of their respective enzyme classes. Only option A (DNA-binding transcription factor activity) is consistent with the protein's size and composition."
  },
  "important_caveats": [
    "The GO:0003700 annotation carries IBA:GO_Central (computational propagation), but the underlying experimental evidence (PubMed:22373915, PDB:3VK0) directly supports DNA binding and transcriptional regulation.",
    "The protein is named 'hypothetical transcription factor' in UniProt, indicating its full regulatory role was characterized relatively recently (2012 publication).",
    "The size-exclusion reasoning eliminates the enzymatic options but does not, by itself, prove the protein is specifically a transcription factor rather than some other small DNA-binding protein; however, among the four given choices, only A is structurally plausible for a 106-aa protein.",
    "The reviewer-only evidence was not available to the evaluated model; the reasoning assessment is based solely on what a model could infer from the 106-aa sequence and general biological knowledge."
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

**Accession:** `Q7DDD9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 103. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7DDD9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:48.577032+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"HTH-type transcriptional repressor NMB1204"}}],"recommendedName":{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22373915","source":"PubMed"}],"value":"Neisseria hypothetical transcription factor"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"22373915","source":"PubMed"}],"value":"NHTF"}]}}
```

Source SHA-256: `47c3a6c86a4ec0366df23b5e91ccf89657aeb92e315db4d971108fcac0a1fd36`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7DDD9.json)  
**Locator:** `/comments/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:48.577032+00:00.  

```json
{"commentType":"FUNCTION","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22373915","source":"PubMed"}],"value":"Transcriptional regulator probably involved in the response to nitrogen levels (PubMed:22373915). Down-regulates its own expression as well as the expression of the downstream gene, glnD, which encodes the [Protein-PII] uridylyltransferase, a key enzyme in the nitrogen regulation system (PubMed:22373915). Acts by binding to a specific palindromic DNA sequence (5'-TGTNANTNACA-3') in its 5'-untranslated region (PubMed:22373915)"}]}
```

Source SHA-256: `47c3a6c86a4ec0366df23b5e91ccf89657aeb92e315db4d971108fcac0a1fd36`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7DDD9.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:48.577032+00:00.  

```json
{"database":"GO","id":"GO:0003700","properties":[{"key":"GoTerm","value":"F:DNA-binding transcription factor activity"},{"key":"GoEvidenceType","value":"IBA:GO_Central"}]}
```

Source SHA-256: `47c3a6c86a4ec0366df23b5e91ccf89657aeb92e315db4d971108fcac0a1fd36`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7DDD9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:31:48.577032+00:00.  

```json
{"citation":{"authors":["Wang H.C.","Ko T.P.","Wu M.L.","Ku S.C.","Wu H.J.","Wang A.H."],"citationCrossReferences":[{"database":"PubMed","id":"22373915"},{"database":"DOI","id":"10.1093/nar/gks177"}],"citationType":"journal article","firstPage":"5718","id":"22373915","journal":"Nucleic Acids Res.","lastPage":"5730","publicationDate":"2012","title":"Neisseria conserved protein DMP19 is a DNA mimic protein that prevents DNA binding to a hypothetical nitrogen-response transcription factor.","volume":"40"},"evidences":[{"evidenceCode":"ECO:0007744","id":"3VK0","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"ATCC BAA-335 / MC58"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.88 ANGSTROMS)","FUNCTION","DNA-BINDING","ACTIVITY REGULATION","SUBUNIT","INTERACTION WITH DMP19","INDUCTION"]}
```

Source SHA-256: `47c3a6c86a4ec0366df23b5e91ccf89657aeb92e315db4d971108fcac0a1fd36`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7DDD9?format=txt&versions=103)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 103 / 1.  
**Retrieved:** 2026-11-02T04:31:51.451900+00:00.  

```text
ID   NHTF_NEIMB              Reviewed;         106 AA.
AC   Q7DDD9;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUL-2004, sequence version 1.
DT   28-JAN-2026, entry version 103.
DE   RecName: Full=Neisseria hypothetical transcription factor {ECO:0000303|PubMed:22373915};
DE            Short=NHTF {ECO:0000303|PubMed:22373915};
DE   AltName: Full=HTH-type transcriptional repressor NMB1204 {ECO:0000305};
GN   OrderedLocusNames=NMB1204 {ECO:0000312|EMBL:AAF41586.1};
OS   Neisseria meningitidis serogroup B (strain ATCC BAA-335 / MC58).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria; Neisseriales;
OC   Neisseriaceae; Neisseria.
OX   NCBI_TaxID=122586;
```

Source SHA-256: `29cf12a02a3813795443a88081f5c678c4bf2c2b1d15f5bbd174d0f3cf40d4e5`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7DDD9?format=txt&versions=103)  
**Locator:** `lines 29-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 103 / 1.  
**Retrieved:** 2026-11-02T04:31:51.451900+00:00.  

```text
RN   [2] {ECO:0007744|PDB:3VK0}
RP   X-RAY CRYSTALLOGRAPHY (1.88 ANGSTROMS), FUNCTION, DNA-BINDING, ACTIVITY
RP   REGULATION, SUBUNIT, INTERACTION WITH DMP19, AND INDUCTION.
RC   STRAIN=ATCC BAA-335 / MC58;
RX   PubMed=22373915; DOI=10.1093/nar/gks177;
RA   Wang H.C., Ko T.P., Wu M.L., Ku S.C., Wu H.J., Wang A.H.;
RT   "Neisseria conserved protein DMP19 is a DNA mimic protein that prevents DNA
RT   binding to a hypothetical nitrogen-response transcription factor.";
RL   Nucleic Acids Res. 40:5718-5730(2012).
```

Source SHA-256: `29cf12a02a3813795443a88081f5c678c4bf2c2b1d15f5bbd174d0f3cf40d4e5`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7DDD9?format=txt&versions=103)  
**Locator:** `lines 38-44`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 103 / 1.  
**Retrieved:** 2026-11-02T04:31:51.451900+00:00.  

```text
CC   -!- FUNCTION: Transcriptional regulator probably involved in the response
CC       to nitrogen levels (PubMed:22373915). Down-regulates its own expression
CC       as well as the expression of the downstream gene, glnD, which encodes
CC       the [Protein-PII] uridylyltransferase, a key enzyme in the nitrogen
CC       regulation system (PubMed:22373915). Acts by binding to a specific
CC       palindromic DNA sequence (5'-TGTNANTNACA-3') in its 5'-untranslated
CC       region (PubMed:22373915). {ECO:0000269|PubMed:22373915}.
```

Source SHA-256: `29cf12a02a3813795443a88081f5c678c4bf2c2b1d15f5bbd174d0f3cf40d4e5`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7DDD9?format=txt&versions=103)  
**Locator:** `lines 79-79`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 103 / 1.  
**Retrieved:** 2026-11-02T04:31:51.451900+00:00.  

```text
DR   GO; GO:0003700; F:DNA-binding transcription factor activity; IBA:GO_Central.
```

Source SHA-256: `29cf12a02a3813795443a88081f5c678c4bf2c2b1d15f5bbd174d0f3cf40d4e5`.

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)  
**Locator:** `lines 28009-28049`  
**Scope:** current ontology; exact historical benchmark ontology unknown.  
**Retrieved:** 2026-11-01T07:04:24.975173+00:00.  

```text
[Term]
id: GO:0003700
name: DNA-binding transcription factor activity
namespace: molecular_function
alt_id: GO:0000130
alt_id: GO:0001071
alt_id: GO:0001130
alt_id: GO:0001131
alt_id: GO:0001151
alt_id: GO:0001199
alt_id: GO:0001204
def: "A transcription regulator activity that modulates transcription of gene sets via selective and non-covalent binding to a specific double-stranded genomic DNA sequence (sometimes referred to as a motif) within a cis-regulatory region. Regulatory regions include promoters (proximal and distal) and enhancers. Genes are transcriptional units, and include bacterial operons." [GOC:txnOH-2018]
comment: Usage guidance: Most DNA-binding transcription factors do not have enzymatic activity. The presence of specific DNA-binding domains known to be present in DNA-binding transcription factors (HOX, GATA etc) should be used to help decide whether a protein is a DNA binding transcription factor or a coregulator. If a protein has an enzymatic activity (for example, ubiquitin ligase, histone acetyl transferase) and no known DNA binding domain, consider annotating to GO:0003712 transcription coregulator activity. Special care should be taken with proteins containing zinc fingers, Myb/SANT and ARID domains, since only a subset of proteins containing these domains directly and selectively bind to regulatory DNA motifs in cis-regulatory regions.
subset: goslim_agr
subset: goslim_candida
subset: goslim_chembl
subset: goslim_drosophila
subset: goslim_metagenomics
subset: goslim_mouse
subset: goslim_plant
subset: goslim_yeast
synonym: "bacterial-type DNA binding transcription factor activity" NARROW []
synonym: "bacterial-type RNA polymerase core promoter proximal region sequence-specific DNA binding transcription factor activity" NARROW []
synonym: "bacterial-type RNA polymerase transcription enhancer sequence-specific DNA binding transcription factor activity" NARROW []
synonym: "bacterial-type RNA polymerase transcription factor activity, metal ion regulated sequence-specific DNA binding" NARROW []
synonym: "bacterial-type RNA polymerase transcription factor activity, sequence-specific DNA binding" NARROW []
synonym: "DNA binding transcription factor activity" EXACT []
synonym: "gene-specific transcription factor activity" EXACT []
synonym: "metal ion regulated sequence-specific DNA binding bacterial-type RNA polymerase transcription factor activity" NARROW []
synonym: "metal ion regulated sequence-specific DNA binding transcription factor activity" NARROW []
synonym: "nucleic acid binding transcription factor activity" BROAD []
synonym: "sequence-specific DNA binding bacterial-type RNA polymerase transcription factor activity" NARROW []
synonym: "sequence-specific DNA binding transcription factor activity" EXACT []
synonym: "transcription factor activity" BROAD []
synonym: "transcription factor activity, bacterial-type RNA polymerase core promoter proximal region sequence-specific binding" NARROW []
synonym: "transcription factor activity, bacterial-type RNA polymerase proximal promoter sequence-specific DNA binding" NARROW []
synonym: "transcription factor activity, bacterial-type RNA polymerase transcription enhancer sequence-specific binding" NARROW []
synonym: "transcription factor activity, metal ion regulated sequence-specific DNA binding" NARROW []
xref: Reactome:R-HSA-163666 "Formation of ChREBP:MLX heterodimer"
is_a: GO:0140110 ! transcription regulator activity

```

Source SHA-256: `b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 37. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
