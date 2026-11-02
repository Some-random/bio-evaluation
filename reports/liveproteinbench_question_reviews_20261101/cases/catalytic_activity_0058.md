# catalytic_activity_0058

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — 4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MNKRDELIGLCIDFLAKVKDKTANANIERWLNENYGPDSETYQKISTLVIDGVAEGWAANDEISGPHYRRSRLCEPCAETFYFSITAVYMDSKGHELDNQQRTFRGDYHSHPYGELNMVIPLDEGAVLAGPLGWQGAGWTAPAPGSQHYPEVKNGALIAFFFLPAGRISYDFQAQG

[Multiple Choices]
A. a beta-lactam + H2O = a substituted beta-amino acid
B. 4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)
C. (S)-norprotosinomenine + S-adenosyl-L-methionine = (S)-6-O-methylnorprotosinomenine + S-adenosyl-L-homocysteine + H(+)
D. L-leucine(in) = L-leucine(out)
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

> The sequence exactly matches a UniProt entry annotated as 4-hydroxylaminobenzoate lyase, with the reaction in choice B. The catalytic-activity annotation cites experimental evidence (ECO:0000269) and a primary publication.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a soluble protein rather than an obvious membrane transporter, which may weigh against D. But the supplied sequence and choices provide no concrete basis to identify the specific reaction in B over the other enzyme reactions.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental characterization identifying this sequence as a 4-hydroxylaminobenzoate lyase and establishing its reaction.


**Reason**

> The exact catalytic transformation is not inferable from general sequence features supplied here; identifying it requires an item-specific functional fact. The reviewer-only annotation supports the key but was not available to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports B, and no alternative reaction is supported for this sequence. The lack of a reasoning path from the supplied input is a lookup-dependence issue, not evidence that another option is correct.


### Important caveats

- The cited UniProt catalytic-activity annotation carries experimental evidence attribution, but the primary paper was not independently retrieved or validated here.
- The sequence match is exact; the author’s precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble protein rather than an obvious membrane transporter, which may weigh against D. But the supplied sequence and choices provide no concrete basis to identify the specific reaction in B over the other enzyme reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental characterization identifying this sequence as a 4-hydroxylaminobenzoate lyase and establishing its reaction.",
    "reason": "The exact catalytic transformation is not inferable from general sequence features supplied here; identifying it requires an item-specific functional fact. The reviewer-only annotation supports the key but was not available to the evaluated model."
  },
  "case_id": "catalytic_activity_0058",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches a UniProt entry annotated as 4-hydroxylaminobenzoate lyase, with the reaction in choice B. The catalytic-activity annotation cites experimental evidence (ECO:0000269) and a primary publication."
  },
  "important_caveats": [
    "The cited UniProt catalytic-activity annotation carries experimental evidence attribution, but the primary paper was not independently retrieved or validated here.",
    "The sequence match is exact; the author’s precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports B, and no alternative reaction is supported for this sequence. The lack of a reasoning path from the supplied input is a lookup-dependence issue, not evidence that another option is correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0058",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches a UniProt entry annotated as 4-hydroxylaminobenzoate lyase, with the reaction in choice B. The catalytic-activity annotation cites experimental evidence (ECO:0000269) and a primary publication.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a soluble protein rather than an obvious membrane transporter, which may weigh against D. But the supplied sequence and choices provide no concrete basis to identify the specific reaction in B over the other enzyme reactions.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental characterization identifying this sequence as a 4-hydroxylaminobenzoate lyase and establishing its reaction.",
    "reason": "The exact catalytic transformation is not inferable from general sequence features supplied here; identifying it requires an item-specific functional fact. The reviewer-only annotation supports the key but was not available to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports B, and no alternative reaction is supported for this sequence. The lack of a reasoning path from the supplied input is a lookup-dependence issue, not evidence that another option is correct."
  },
  "important_caveats": [
    "The cited UniProt catalytic-activity annotation carries experimental evidence attribution, but the primary paper was not independently retrieved or validated here.",
    "The sequence match is exact; the author’s precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (176 AA) matches UniProt Q9FD33 (PNBB_PSEPU) exactly. The entry is annotated as '4-hydroxylaminobenzoate lyase' (EC 4.3.3.-) with the catalytic activity '4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)' supported by experimental evidence (ECO:0000269, PubMed:11157934). The expected answer B matches the annotated reaction verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can reasonably eliminate D (a 176-residue soluble protein is far too small for a multi-TM membrane amino acid transporter) and C (no recognizable SAM-binding motif such as the VLDLGCGxxGxxD consensus). The absence of the classic class-A beta-lactamase SXXK/SDN/KTG motifs weakly disfavors A. However, positively identifying the reaction as 4-hydroxylaminobenzoate → 3,4-dihydroxybenzoate + NH4+ (a C–N lyase in the 4-nitrobenzoate catabolism pathway of P. putida TW3) requires recognizing this specific enzyme or its family, which is not derivable from generic sequence features.


**Missing item-specific fact**

> The specific identity of the enzyme as 4-hydroxylaminobenzoate lyase (PnbB) in the pnb nitrobenzoate-catabolism operon, and the particular C–N bond-cleavage reaction it catalyzes, are protein-specific annotations not inferable from general catalytic motifs in this 176-aa sequence.


**Reason**

> While partial elimination of D and C is possible by size and domain reasoning, and the absence of beta-lactamase motifs mildly disfavors A, the positive identification of the exact lyase reaction (B) depends on knowing this particular enzyme's function rather than on a generalizable sequence-to-function argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is clearly infeasible for a 176-aa soluble protein; C lacks any SAM-binding domain; A is disfavored by absence of beta-lactamase motifs. Only B remains as a plausible match, though reaching it requires lookup rather than deduction.


### Important caveats

- The UniProt entry was first publicly released on 2025-02-05; if the benchmark was constructed before that date, the annotation may not have been available in public databases at construction time.
- The EC number is still listed as 4.3.3.- (unassigned sub-class), indicating the enzyme family is not yet fully characterized in the EC scheme.
- Evidence code ECO:0000269 indicates direct experimental evidence (from PubMed:11157934), lending confidence to the annotation.
- The reviewer-only accession Q9FD33 was inferred mechanically from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can reasonably eliminate D (a 176-residue soluble protein is far too small for a multi-TM membrane amino acid transporter) and C (no recognizable SAM-binding motif such as the VLDLGCGxxGxxD consensus). The absence of the classic class-A beta-lactamase SXXK/SDN/KTG motifs weakly disfavors A. However, positively identifying the reaction as 4-hydroxylaminobenzoate → 3,4-dihydroxybenzoate + NH4+ (a C–N lyase in the 4-nitrobenzoate catabolism pathway of P. putida TW3) requires recognizing this specific enzyme or its family, which is not derivable from generic sequence features.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of the enzyme as 4-hydroxylaminobenzoate lyase (PnbB) in the pnb nitrobenzoate-catabolism operon, and the particular C–N bond-cleavage reaction it catalyzes, are protein-specific annotations not inferable from general catalytic motifs in this 176-aa sequence.",
    "reason": "While partial elimination of D and C is possible by size and domain reasoning, and the absence of beta-lactamase motifs mildly disfavors A, the positive identification of the exact lyase reaction (B) depends on knowing this particular enzyme's function rather than on a generalizable sequence-to-function argument."
  },
  "case_id": "catalytic_activity_0058",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence (176 AA) matches UniProt Q9FD33 (PNBB_PSEPU) exactly. The entry is annotated as '4-hydroxylaminobenzoate lyase' (EC 4.3.3.-) with the catalytic activity '4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)' supported by experimental evidence (ECO:0000269, PubMed:11157934). The expected answer B matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released on 2025-02-05; if the benchmark was constructed before that date, the annotation may not have been available in public databases at construction time.",
    "The EC number is still listed as 4.3.3.- (unassigned sub-class), indicating the enzyme family is not yet fully characterized in the EC scheme.",
    "Evidence code ECO:0000269 indicates direct experimental evidence (from PubMed:11157934), lending confidence to the annotation.",
    "The reviewer-only accession Q9FD33 was inferred mechanically from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is clearly infeasible for a 176-aa soluble protein; C lacks any SAM-binding domain; A is disfavored by absence of beta-lactamase motifs. Only B remains as a plausible match, though reaching it requires lookup rather than deduction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0058",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (176 AA) matches UniProt Q9FD33 (PNBB_PSEPU) exactly. The entry is annotated as '4-hydroxylaminobenzoate lyase' (EC 4.3.3.-) with the catalytic activity '4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)' supported by experimental evidence (ECO:0000269, PubMed:11157934). The expected answer B matches the annotated reaction verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model can reasonably eliminate D (a 176-residue soluble protein is far too small for a multi-TM membrane amino acid transporter) and C (no recognizable SAM-binding motif such as the VLDLGCGxxGxxD consensus). The absence of the classic class-A beta-lactamase SXXK/SDN/KTG motifs weakly disfavors A. However, positively identifying the reaction as 4-hydroxylaminobenzoate → 3,4-dihydroxybenzoate + NH4+ (a C–N lyase in the 4-nitrobenzoate catabolism pathway of P. putida TW3) requires recognizing this specific enzyme or its family, which is not derivable from generic sequence features.",
    "missing_item_specific_fact": "The specific identity of the enzyme as 4-hydroxylaminobenzoate lyase (PnbB) in the pnb nitrobenzoate-catabolism operon, and the particular C–N bond-cleavage reaction it catalyzes, are protein-specific annotations not inferable from general catalytic motifs in this 176-aa sequence.",
    "reason": "While partial elimination of D and C is possible by size and domain reasoning, and the absence of beta-lactamase motifs mildly disfavors A, the positive identification of the exact lyase reaction (B) depends on knowing this particular enzyme's function rather than on a generalizable sequence-to-function argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is clearly infeasible for a 176-aa soluble protein; C lacks any SAM-binding domain; A is disfavored by absence of beta-lactamase motifs. Only B remains as a plausible match, though reaching it requires lookup rather than deduction."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released on 2025-02-05; if the benchmark was constructed before that date, the annotation may not have been available in public databases at construction time.",
    "The EC number is still listed as 4.3.3.- (unassigned sub-class), indicating the enzyme family is not yet fully characterized in the EC scheme.",
    "Evidence code ECO:0000269 indicates direct experimental evidence (from PubMed:11157934), lending confidence to the annotation.",
    "The reviewer-only accession Q9FD33 was inferred mechanically from dataset metadata and was not provided to the evaluated model."
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

**Accession:** `Q9FD33` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 36. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD33.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:47.631253+00:00.  

```json
"Q9FD33"
```

Source SHA-256: `d2783e27679757a9b718b176118361fd861642c522fe7e3dec6c34c2ed0578cf`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD33.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:47.631253+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"11157934","source":"PubMed"}],"value":"4.3.3.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"11157934","source":"PubMed"}],"value":"4-hydroxylaminobenzoate lyase"}}}
```

Source SHA-256: `d2783e27679757a9b718b176118361fd861642c522fe7e3dec6c34c2ed0578cf`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD33.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:47.631253+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"11157934","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:80204"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"11157934","source":"PubMed"}],"name":"4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate + NH4(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:80203"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:28938"},{"database":"ChEBI","id":"CHEBI:36241"},{"database":"ChEBI","id":"CHEBI:231457"}]}}
```

Source SHA-256: `d2783e27679757a9b718b176118361fd861642c522fe7e3dec6c34c2ed0578cf`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9FD33.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:47.631253+00:00.  

```json
{"citation":{"authors":["Hughes M.A.","Williams P.A."],"citationCrossReferences":[{"database":"PubMed","id":"11157934"},{"database":"DOI","id":"10.1128/jb.183.4.1225-1232.2001"}],"citationType":"journal article","firstPage":"1225","id":"11157934","journal":"J. Bacteriol.","lastPage":"1232","publicationDate":"2001","title":"Cloning and characterisation of the pnb genes, encoding enzymes for 4-nitrobenzoate catabolism in Pseudomonas putida TW3.","volume":"183"},"referenceComments":[{"type":"STRAIN","value":"TW3"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY"]}
```

Source SHA-256: `d2783e27679757a9b718b176118361fd861642c522fe7e3dec6c34c2ed0578cf`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD33?format=txt&versions=36)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:32:52.128518+00:00.  

```text
ID   PNBB_PSEPU              Reviewed;         176 AA.
AC   Q9FD33;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   01-MAR-2001, sequence version 1.
DT   28-JAN-2026, entry version 36.
DE   RecName: Full=4-hydroxylaminobenzoate lyase {ECO:0000303|PubMed:11157934};
DE            EC=4.3.3.- {ECO:0000269|PubMed:11157934};
GN   Name=pnbB {ECO:0000303|PubMed:11157934};
OS   Pseudomonas putida (Arthrobacter siderocapsulatus).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.
OX   NCBI_TaxID=303;
```

Source SHA-256: `6691247797bb30cca466436872237092529deaffd2d4d5e25ce14a2e63546333`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD33?format=txt&versions=36)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:32:52.128518+00:00.  

```text
DE   RecName: Full=4-hydroxylaminobenzoate lyase {ECO:0000303|PubMed:11157934};
DE            EC=4.3.3.- {ECO:0000269|PubMed:11157934};
```

Source SHA-256: `6691247797bb30cca466436872237092529deaffd2d4d5e25ce14a2e63546333`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD33?format=txt&versions=36)  
**Locator:** `lines 13-20`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:32:52.128518+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND CATALYTIC ACTIVITY.
RC   STRAIN=TW3;
RX   PubMed=11157934; DOI=10.1128/jb.183.4.1225-1232.2001;
RA   Hughes M.A., Williams P.A.;
RT   "Cloning and characterisation of the pnb genes, encoding enzymes for 4-
RT   nitrobenzoate catabolism in Pseudomonas putida TW3.";
RL   J. Bacteriol. 183:1225-1232(2001).
```

Source SHA-256: `6691247797bb30cca466436872237092529deaffd2d4d5e25ce14a2e63546333`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9FD33?format=txt&versions=36)  
**Locator:** `lines 26-32`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 36 / 1.  
**Retrieved:** 2026-11-02T04:32:52.128518+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4-hydroxylaminobenzoate + H2O + H(+) = 3,4-dihydroxybenzoate +
CC         NH4(+); Xref=Rhea:RHEA:80203, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:28938, ChEBI:CHEBI:36241, ChEBI:CHEBI:231457;
CC         Evidence={ECO:0000269|PubMed:11157934};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80204;
CC         Evidence={ECO:0000269|PubMed:11157934};
```

Source SHA-256: `6691247797bb30cca466436872237092529deaffd2d4d5e25ce14a2e63546333`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 58. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
