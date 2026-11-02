# catalytic_activity_0136

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — L-histidine = D-histidine

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MDRKVQVLDFIKINPAGNITILIDNFDIYDKNIPKLSEEIMKETNLYAEQVGFIKDSHLQMMGGEFCGNASRAFASLLAFRDKDFSKQKNYNITCSGESKVLDVDVRNDGAKNKFLAKIKMPKFLSLEEINVDEYKLGLVRFSGINHFIFNIKENKETSFENIIDLVKKYLSNEEYSAFGIMFFDSDNLSMKPYVYVKEVGSGVYENSCASGTTALGYYLKKCKNLDRAKIVQPNGWLEYIIENDEMYIDGPVEIIAEGKIYIGK

[Multiple Choices]
A. glycyl-tRNA(Gly) + acetyl-CoA = N-acetylglycyl-tRNA(Gly) + CoA + H(+)
B. L-histidine = D-histidine
C. (9S)-hydroperoxy-(10E,12Z,15Z)-octadecatrienoate = colnelenate + H2O
D. benzoyl-CoA + L-lysyl-[protein] = N(6)-benzoyl-L-lysyl-[protein] + CoA + H(+)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The matched sequence is annotated as a histidine racemase, with the reaction L-histidine = D-histidine. The historical record cites experimental evidence (ECO:0000269) for this catalytic activity, although the cited paper was not independently reviewed here.

Citations as saved: [H1](#evidence-h1), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct enzyme activities, but the sequence and prompt provide no decisive general biological clue that identifies this protein specifically as a histidine racemase.


**Missing item-specific fact**

> The protein-specific functional identification as a histidine racemase, or equivalent experimental or database evidence linking this sequence to histidine racemization.


**Reason**

> Selecting B depends on knowing the function of this particular protein; recognizing its exact sequence or recalling its annotation would be lookup or memorization, not reasoning from supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer evidence supports B for the matched sequence; no other listed reaction is supported by that evidence.


### Important caveats

- The reviewer-only database evidence was not provided to the evaluated model.
- The historical UniProt sequence matches the benchmark sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct enzyme activities, but the sequence and prompt provide no decisive general biological clue that identifies this protein specifically as a histidine racemase.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional identification as a histidine racemase, or equivalent experimental or database evidence linking this sequence to histidine racemization.",
    "reason": "Selecting B depends on knowing the function of this particular protein; recognizing its exact sequence or recalling its annotation would be lookup or memorization, not reasoning from supplied evidence."
  },
  "case_id": "catalytic_activity_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as a histidine racemase, with the reaction L-histidine = D-histidine. The historical record cites experimental evidence (ECO:0000269) for this catalytic activity, although the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not provided to the evaluated model.",
    "The historical UniProt sequence matches the benchmark sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B for the matched sequence; no other listed reaction is supported by that evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as a histidine racemase, with the reaction L-histidine = D-histidine. The historical record cites experimental evidence (ECO:0000269) for this catalytic activity, although the cited paper was not independently reviewed here.",
    "evidence_ids": ["H1", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct enzyme activities, but the sequence and prompt provide no decisive general biological clue that identifies this protein specifically as a histidine racemase.",
    "missing_item_specific_fact": "The protein-specific functional identification as a histidine racemase, or equivalent experimental or database evidence linking this sequence to histidine racemization.",
    "reason": "Selecting B depends on knowing the function of this particular protein; recognizing its exact sequence or recalling its annotation would be lookup or memorization, not reasoning from supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer evidence supports B for the matched sequence; no other listed reaction is supported by that evidence."
  },
  "important_caveats": [
    "The reviewer-only database evidence was not provided to the evaluated model.",
    "The historical UniProt sequence matches the benchmark sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q8RI81 (sequence matched, 265 aa) annotates this protein as Histidine racemase (EC 5.1.1.24) with catalytic activity 'L-histidine = D-histidine' supported by experimental evidence (ECO:0000269|PubMed:39424140, a 2024 J. Biol. Chem. paper reporting X-ray crystallography, mutagenesis, and enzymatic characterization of this cofactor-independent histidine racemase from Fusobacterium nucleatum). The annotation is experimentally verified, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could weakly eliminate options A and D (which require GNAT-fold acyltransferase motifs) and C (which requires a lipoxygenase/COX-like fold with conserved His residues and a specific hydrophobic channel) based on the absence of those characteristic motifs in the sequence. However, this negative elimination does not positively identify the enzyme as a histidine racemase. Critically, this enzyme is a cofactor-independent racemase with a novel fold (per the 2024 paper), so it lacks the PLP-binding motifs (e.g., the conserved Lys in the PLP-binding pocket) that would normally flag an amino acid racemase from sequence. No positive sequence signature in the supplied 265-aa sequence uniquely or reliably points to 'histidine racemase' activity.


**Missing item-specific fact**

> The specific knowledge that this Fusobacterium nucleatum 265-aa protein (Q8RI81) is the recently characterized cofactor-independent histidine racemase (EC 5.1.1.24) with a novel fold, as described in the 2024 PubMed 39424140 paper. Without this item-specific annotation or memorization, the sequence provides no positive identifying motif for this activity.


**Reason**

> The protein is a recently discovered enzyme (Swiss-Prot entry first released 2025-04-09) with a novel fold and no cofactor, meaning it lacks the canonical sequence signatures (PLP-binding Lys, GNAT fold, lipoxygenase His-box) that would allow general biological reasoning to identify its activity. Selection of answer B depends on knowing this specific protein's experimentally determined function rather than on reasoning from general enzymology principles.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (GNAT-fold acetyltransferase), C (lipoxygenase isomerase), and D (GNAT-fold lysine acyltransferase) can be reasonably excluded based on the absence of their characteristic structural motifs in the sequence. While B cannot be positively identified from sequence alone, it remains the only surviving option after elimination of the other three, so no other choice is genuinely defensible.


### Important caveats

- The UniProt annotation for this protein was only integrated into Swiss-Prot on 2025-04-09, based on a 2024 publication. Depending on the benchmark construction date, this annotation may have been very recent or even unavailable at the time of question creation.
- The enzyme is described as having a novel fold and being cofactor-independent, making it exceptionally difficult to classify by homology or motif-based reasoning.
- The active-site residues (Cys-67 and Cys-209) identified by mutagenesis are not part of a recognizable general catalytic motif that would enable prediction from sequence alone.
- Reviewer-only evidence confirms the key is correct but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could weakly eliminate options A and D (which require GNAT-fold acyltransferase motifs) and C (which requires a lipoxygenase/COX-like fold with conserved His residues and a specific hydrophobic channel) based on the absence of those characteristic motifs in the sequence. However, this negative elimination does not positively identify the enzyme as a histidine racemase. Critically, this enzyme is a cofactor-independent racemase with a novel fold (per the 2024 paper), so it lacks the PLP-binding motifs (e.g., the conserved Lys in the PLP-binding pocket) that would normally flag an amino acid racemase from sequence. No positive sequence signature in the supplied 265-aa sequence uniquely or reliably points to 'histidine racemase' activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific knowledge that this Fusobacterium nucleatum 265-aa protein (Q8RI81) is the recently characterized cofactor-independent histidine racemase (EC 5.1.1.24) with a novel fold, as described in the 2024 PubMed 39424140 paper. Without this item-specific annotation or memorization, the sequence provides no positive identifying motif for this activity.",
    "reason": "The protein is a recently discovered enzyme (Swiss-Prot entry first released 2025-04-09) with a novel fold and no cofactor, meaning it lacks the canonical sequence signatures (PLP-binding Lys, GNAT fold, lipoxygenase His-box) that would allow general biological reasoning to identify its activity. Selection of answer B depends on knowing this specific protein's experimentally determined function rather than on reasoning from general enzymology principles."
  },
  "case_id": "catalytic_activity_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q8RI81 (sequence matched, 265 aa) annotates this protein as Histidine racemase (EC 5.1.1.24) with catalytic activity 'L-histidine = D-histidine' supported by experimental evidence (ECO:0000269|PubMed:39424140, a 2024 J. Biol. Chem. paper reporting X-ray crystallography, mutagenesis, and enzymatic characterization of this cofactor-independent histidine racemase from Fusobacterium nucleatum). The annotation is experimentally verified, not merely computational."
  },
  "important_caveats": [
    "The UniProt annotation for this protein was only integrated into Swiss-Prot on 2025-04-09, based on a 2024 publication. Depending on the benchmark construction date, this annotation may have been very recent or even unavailable at the time of question creation.",
    "The enzyme is described as having a novel fold and being cofactor-independent, making it exceptionally difficult to classify by homology or motif-based reasoning.",
    "The active-site residues (Cys-67 and Cys-209) identified by mutagenesis are not part of a recognizable general catalytic motif that would enable prediction from sequence alone.",
    "Reviewer-only evidence confirms the key is correct but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (GNAT-fold acetyltransferase), C (lipoxygenase isomerase), and D (GNAT-fold lysine acyltransferase) can be reasonably excluded based on the absence of their characteristic structural motifs in the sequence. While B cannot be positively identified from sequence alone, it remains the only surviving option after elimination of the other three, so no other choice is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q8RI81 (sequence matched, 265 aa) annotates this protein as Histidine racemase (EC 5.1.1.24) with catalytic activity 'L-histidine = D-histidine' supported by experimental evidence (ECO:0000269|PubMed:39424140, a 2024 J. Biol. Chem. paper reporting X-ray crystallography, mutagenesis, and enzymatic characterization of this cofactor-independent histidine racemase from Fusobacterium nucleatum). The annotation is experimentally verified, not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could weakly eliminate options A and D (which require GNAT-fold acyltransferase motifs) and C (which requires a lipoxygenase/COX-like fold with conserved His residues and a specific hydrophobic channel) based on the absence of those characteristic motifs in the sequence. However, this negative elimination does not positively identify the enzyme as a histidine racemase. Critically, this enzyme is a cofactor-independent racemase with a novel fold (per the 2024 paper), so it lacks the PLP-binding motifs (e.g., the conserved Lys in the PLP-binding pocket) that would normally flag an amino acid racemase from sequence. No positive sequence signature in the supplied 265-aa sequence uniquely or reliably points to 'histidine racemase' activity.",
    "missing_item_specific_fact": "The specific knowledge that this Fusobacterium nucleatum 265-aa protein (Q8RI81) is the recently characterized cofactor-independent histidine racemase (EC 5.1.1.24) with a novel fold, as described in the 2024 PubMed 39424140 paper. Without this item-specific annotation or memorization, the sequence provides no positive identifying motif for this activity.",
    "reason": "The protein is a recently discovered enzyme (Swiss-Prot entry first released 2025-04-09) with a novel fold and no cofactor, meaning it lacks the canonical sequence signatures (PLP-binding Lys, GNAT fold, lipoxygenase His-box) that would allow general biological reasoning to identify its activity. Selection of answer B depends on knowing this specific protein's experimentally determined function rather than on reasoning from general enzymology principles."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (GNAT-fold acetyltransferase), C (lipoxygenase isomerase), and D (GNAT-fold lysine acyltransferase) can be reasonably excluded based on the absence of their characteristic structural motifs in the sequence. While B cannot be positively identified from sequence alone, it remains the only surviving option after elimination of the other three, so no other choice is genuinely defensible."
  },
  "important_caveats": [
    "The UniProt annotation for this protein was only integrated into Swiss-Prot on 2025-04-09, based on a 2024 publication. Depending on the benchmark construction date, this annotation may have been very recent or even unavailable at the time of question creation.",
    "The enzyme is described as having a novel fold and being cofactor-independent, making it exceptionally difficult to classify by homology or motif-based reasoning.",
    "The active-site residues (Cys-67 and Cys-209) identified by mutagenesis are not part of a recognizable general catalytic motif that would enable prediction from sequence alone.",
    "Reviewer-only evidence confirms the key is correct but was not available to the evaluated model."
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

**Accession:** `Q8RI81` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 79. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.407556+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39424140","source":"PubMed"}],"value":"5.1.1.24"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39424140","source":"PubMed"}],"value":"Histidine racemase"}}}
```

Source SHA-256: `0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.407556+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"5.1.1.24","evidences":[{"evidenceCode":"ECO:0000269","id":"39424140","source":"PubMed"}],"name":"L-histidine = D-histidine","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:59188"},{"database":"ChEBI","id":"CHEBI:57595"},{"database":"ChEBI","id":"CHEBI:142967"}]}}
```

Source SHA-256: `0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:25.407556+00:00.  

```json
{"citation":{"authors":["Lamer T.","Chen P.","Venter M.J.","van Belkum M.J.","Wijewardane A.","Wu C.","Lemieux M.J.","Vederas J.C."],"citationCrossReferences":[{"database":"PubMed","id":"39424140"},{"database":"DOI","id":"10.1016/j.jbc.2024.107896"}],"citationType":"journal article","firstPage":"107896","id":"39424140","journal":"J. Biol. Chem.","lastPage":"107896","publicationDate":"2024","title":"Discovery, characterization, and structure of a cofactor-independent histidine racemase from the oral pathogen Fusobacterium nucleatum.","volume":"300"},"evidences":[{"evidenceCode":"ECO:0007744","id":"9CR1","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"9CR6","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355"}],"referenceNumber":3,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.5 ANGSTROMS) OF MUTANTS SER-67 AND SER-209","FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","ACTIVE SITE","MUTAGENESIS OF CYS-67 AND CYS-209"]}
```

Source SHA-256: `0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:41.693468+00:00.  

```text
ID   HISR_FUSNN              Reviewed;         265 AA.
AC   Q8RI81;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-JUN-2002, sequence version 1.
DT   28-JAN-2026, entry version 79.
DE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};
DE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};
GN   Name=hisR {ECO:0000303|PubMed:39424140};
GN   OrderedLocusNames=FN1732 {ECO:0000312|EMBL:AAL93847.1};
OS   Fusobacterium nucleatum subsp. nucleatum (strain ATCC 25586 / DSM 15643 /
OS   BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355).
OC   Bacteria; Fusobacteriati; Fusobacteriota; Fusobacteriia; Fusobacteriales;
OC   Fusobacteriaceae; Fusobacterium.
OX   NCBI_TaxID=190304;
```

Source SHA-256: `c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:41.693468+00:00.  

```text
DE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};
DE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};
```

Source SHA-256: `c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)  
**Locator:** `lines 36-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:41.693468+00:00.  

```text
RN   [3] {ECO:0007744|PDB:9CR1, ECO:0007744|PDB:9CR6}
RP   X-RAY CRYSTALLOGRAPHY (2.5 ANGSTROMS) OF MUTANTS SER-67 AND SER-209,
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL
RP   PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF CYS-67 AND CYS-209.
RC   STRAIN=ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC
RC   2640 / LMG 13131 / VPI 4355;
RX   PubMed=39424140; DOI=10.1016/j.jbc.2024.107896;
RA   Lamer T., Chen P., Venter M.J., van Belkum M.J., Wijewardane A., Wu C.,
RA   Lemieux M.J., Vederas J.C.;
RT   "Discovery, characterization, and structure of a cofactor-independent
RT   histidine racemase from the oral pathogen Fusobacterium nucleatum.";
RL   J. Biol. Chem. 300:107896-107896(2024).
```

Source SHA-256: `c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)  
**Locator:** `lines 55-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 79 / 1.  
**Retrieved:** 2026-11-01T06:28:41.693468+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-histidine = D-histidine; Xref=Rhea:RHEA:59188,
CC         ChEBI:CHEBI:57595, ChEBI:CHEBI:142967; EC=5.1.1.24;
CC         Evidence={ECO:0000269|PubMed:39424140};
```

Source SHA-256: `c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 136. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
