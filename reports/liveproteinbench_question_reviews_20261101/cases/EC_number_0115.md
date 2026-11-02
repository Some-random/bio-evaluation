# EC_number_0115

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 7.6.2.2

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MADTAITVDGAEKRYGDKKALDGLDLRVARGTVHGVLGPNGAGKTTLVRVLSTLLRPDAGRIEVSGHDVVREAYAVRLRIGLLGQHAALDEELGGRQNLELFGRLHHLGARRARARADELLERFDLADTGRKTVRQYSGGMRRRLDLAASLITEPEVLFLDEPTTGLDPRGRAEVWDSVRSLVGGGTTVLLTTQYLEEADQLADRISVVDAGRVIAEGTADELKAETGGDRIDVVLREAGQLGAAVALLPLTGVTVDTDRRLLSAPVTDRMEALSGVVRALQEAGIEAEDVALRRPTLDEVFLHLTGDDRRVKEAA

[Multiple Choices]
A. 6.3.5.1
B. 2.4.2.14
C. 2.5.1.160
D. 7.6.2.2
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry annotating this protein as daunorubicin resistance ATP-binding protein DrrA3 with EC 7.6.2.2. The curated catalytic-activity annotation specifies ATP-dependent daunorubicin transport and cites a publication. This supports D, though it is literature-linked database annotation rather than independent validation here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The GPNGAGKTT P-loop-like motif supports ATP binding and makes an ATPase-related function plausible. It does not establish that this protein couples ATP hydrolysis to transport, or identify the transported substrate; thus it cannot by itself justify the complete EC number.


**Missing item-specific fact**

> The protein-specific function as a daunorubicin-efflux ATP-binding component, needed to assign EC 7.6.2.2, is absent from the supplied sequence and choices.


**Reason**

> The sequence offers a general ATP-binding clue, but the decisive transport function and substrate assignment come from protein-specific annotation or experimental literature, not from a sufficiently distinguishing argument in the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports the keyed option; no alternative is comparably supported.


### Important caveats

- The reviewer-only UniProt evidence is sequence-matched and includes a literature citation, but the exact author source snapshot is unknown.
- A P-loop motif is evidence for likely nucleotide binding, not proof of the specific transport reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The GPNGAGKTT P-loop-like motif supports ATP binding and makes an ATPase-related function plausible. It does not establish that this protein couples ATP hydrolysis to transport, or identify the transported substrate; thus it cannot by itself justify the complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific function as a daunorubicin-efflux ATP-binding component, needed to assign EC 7.6.2.2, is absent from the supplied sequence and choices.",
    "reason": "The sequence offers a general ATP-binding clue, but the decisive transport function and substrate assignment come from protein-specific annotation or experimental literature, not from a sufficiently distinguishing argument in the input."
  },
  "case_id": "EC_number_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotating this protein as daunorubicin resistance ATP-binding protein DrrA3 with EC 7.6.2.2. The curated catalytic-activity annotation specifies ATP-dependent daunorubicin transport and cites a publication. This supports D, though it is literature-linked database annotation rather than independent validation here."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence is sequence-matched and includes a literature citation, but the exact author source snapshot is unknown.",
    "A P-loop motif is evidence for likely nucleotide binding, not proof of the specific transport reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports the keyed option; no alternative is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotating this protein as daunorubicin resistance ATP-binding protein DrrA3 with EC 7.6.2.2. The curated catalytic-activity annotation specifies ATP-dependent daunorubicin transport and cites a publication. This supports D, though it is literature-linked database annotation rather than independent validation here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The GPNGAGKTT P-loop-like motif supports ATP binding and makes an ATPase-related function plausible. It does not establish that this protein couples ATP hydrolysis to transport, or identify the transported substrate; thus it cannot by itself justify the complete EC number.",
    "missing_item_specific_fact": "The protein-specific function as a daunorubicin-efflux ATP-binding component, needed to assign EC 7.6.2.2, is absent from the supplied sequence and choices.",
    "reason": "The sequence offers a general ATP-binding clue, but the decisive transport function and substrate assignment come from protein-specific annotation or experimental literature, not from a sufficiently distinguishing argument in the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports the keyed option; no alternative is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only UniProt evidence is sequence-matched and includes a literature citation, but the exact author source snapshot is unknown.",
    "A P-loop motif is evidence for likely nucleotide binding, not proof of the specific transport reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXU7 (DRRA3_STRC4) from Streptomyces coeruleorubidus assigns EC 7.6.2.2 to this 316-aa sequence (sequence SHA256 match confirmed). The EC number is supported by curator inference (ECO:0000305) based on PubMed:39375957, which documented daunorubicin efflux function, induction, and disruption phenotype. The catalytic reaction (daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + Pi + H+) is consistent with EC 7.6.2.2 (ABC-type drug transporter). The evidence is database-curated annotation referencing a functional study, not direct kinetic characterization, but it is a legitimate annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Walker A (P-loop) motif 'GPNGAGKT' and an ABC signature motif region ('LDEPTTGLDPRG'), which together identify this as an ABC transporter nucleotide-binding domain (NBD). ABC transporters are classified under EC 7 (translocases). Among the four choices, only D (7.6.2.2) falls under EC class 7; the others are a ligase (6.3.5.1, glutamine synthetase) and transferases (2.4.2.14, purine nucleoside phosphorylase; 2.5.1.160). Recognizing the ABC NBD architecture and the EC classification hierarchy (EC 7 = translocases) is sufficient to eliminate A, B, and C and select D.


**Missing item-specific fact**

> None required to distinguish among the given choices. Identifying the specific substrate (daunorubicin) to pin the 4th digit would require the PubMed reference, but since only one EC 7 option is offered, general ABC-transporter recognition suffices.


**Reason**

> A model with knowledge of ABC transporter domain architecture (Walker A, ABC signature) and the EC classification system (EC 7 = translocases, EC 6 = ligases, EC 2 = transferases) can reason from the sequence motifs to the correct class and select D without memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Walker A and ABC signature motifs are unambiguous indicators of an ABC transporter NBD. The other three options belong to entirely different EC classes (ligase, transferase) with incompatible domain architectures. No other option is defensible given the clear sequence evidence.


### Important caveats

- The EC assignment uses evidence code ECO:0000305 (curator inference), not direct in vitro kinetic measurement of the 7.6.2.2 reaction. The underlying study (Dong et al. 2024) demonstrated daunorubicin efflux function genetically (disruption phenotype, induction) rather than purifying the protein and measuring transport kinetics.
- The UniProt entry was first public in Feb 2025; the author's source snapshot is unknown. If the benchmark was constructed before this entry existed, the annotation provenance differs from what is shown here.
- Distinguishing the 4th digit (7.6.2.2 vs. other 7.6.2.x ABC drug transporters) would require substrate specificity knowledge not derivable from sequence alone, but this is moot since only one EC 7 option is presented.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Walker A (P-loop) motif 'GPNGAGKT' and an ABC signature motif region ('LDEPTTGLDPRG'), which together identify this as an ABC transporter nucleotide-binding domain (NBD). ABC transporters are classified under EC 7 (translocases). Among the four choices, only D (7.6.2.2) falls under EC class 7; the others are a ligase (6.3.5.1, glutamine synthetase) and transferases (2.4.2.14, purine nucleoside phosphorylase; 2.5.1.160). Recognizing the ABC NBD architecture and the EC classification hierarchy (EC 7 = translocases) is sufficient to eliminate A, B, and C and select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None required to distinguish among the given choices. Identifying the specific substrate (daunorubicin) to pin the 4th digit would require the PubMed reference, but since only one EC 7 option is offered, general ABC-transporter recognition suffices.",
    "reason": "A model with knowledge of ABC transporter domain architecture (Walker A, ABC signature) and the EC classification system (EC 7 = translocases, EC 6 = ligases, EC 2 = transferases) can reason from the sequence motifs to the correct class and select D without memorizing this specific protein's annotation."
  },
  "case_id": "EC_number_0115",
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
    "reason": "UniProt entry P0DXU7 (DRRA3_STRC4) from Streptomyces coeruleorubidus assigns EC 7.6.2.2 to this 316-aa sequence (sequence SHA256 match confirmed). The EC number is supported by curator inference (ECO:0000305) based on PubMed:39375957, which documented daunorubicin efflux function, induction, and disruption phenotype. The catalytic reaction (daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + Pi + H+) is consistent with EC 7.6.2.2 (ABC-type drug transporter). The evidence is database-curated annotation referencing a functional study, not direct kinetic characterization, but it is a legitimate annotation."
  },
  "important_caveats": [
    "The EC assignment uses evidence code ECO:0000305 (curator inference), not direct in vitro kinetic measurement of the 7.6.2.2 reaction. The underlying study (Dong et al. 2024) demonstrated daunorubicin efflux function genetically (disruption phenotype, induction) rather than purifying the protein and measuring transport kinetics.",
    "The UniProt entry was first public in Feb 2025; the author's source snapshot is unknown. If the benchmark was constructed before this entry existed, the annotation provenance differs from what is shown here.",
    "Distinguishing the 4th digit (7.6.2.2 vs. other 7.6.2.x ABC drug transporters) would require substrate specificity knowledge not derivable from sequence alone, but this is moot since only one EC 7 option is presented."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Walker A and ABC signature motifs are unambiguous indicators of an ABC transporter NBD. The other three options belong to entirely different EC classes (ligase, transferase) with incompatible domain architectures. No other option is defensible given the clear sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXU7 (DRRA3_STRC4) from Streptomyces coeruleorubidus assigns EC 7.6.2.2 to this 316-aa sequence (sequence SHA256 match confirmed). The EC number is supported by curator inference (ECO:0000305) based on PubMed:39375957, which documented daunorubicin efflux function, induction, and disruption phenotype. The catalytic reaction (daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + Pi + H+) is consistent with EC 7.6.2.2 (ABC-type drug transporter). The evidence is database-curated annotation referencing a functional study, not direct kinetic characterization, but it is a legitimate annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Walker A (P-loop) motif 'GPNGAGKT' and an ABC signature motif region ('LDEPTTGLDPRG'), which together identify this as an ABC transporter nucleotide-binding domain (NBD). ABC transporters are classified under EC 7 (translocases). Among the four choices, only D (7.6.2.2) falls under EC class 7; the others are a ligase (6.3.5.1, glutamine synthetase) and transferases (2.4.2.14, purine nucleoside phosphorylase; 2.5.1.160). Recognizing the ABC NBD architecture and the EC classification hierarchy (EC 7 = translocases) is sufficient to eliminate A, B, and C and select D.",
    "missing_item_specific_fact": "None required to distinguish among the given choices. Identifying the specific substrate (daunorubicin) to pin the 4th digit would require the PubMed reference, but since only one EC 7 option is offered, general ABC-transporter recognition suffices.",
    "reason": "A model with knowledge of ABC transporter domain architecture (Walker A, ABC signature) and the EC classification system (EC 7 = translocases, EC 6 = ligases, EC 2 = transferases) can reason from the sequence motifs to the correct class and select D without memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Walker A and ABC signature motifs are unambiguous indicators of an ABC transporter NBD. The other three options belong to entirely different EC classes (ligase, transferase) with incompatible domain architectures. No other option is defensible given the clear sequence evidence."
  },
  "important_caveats": [
    "The EC assignment uses evidence code ECO:0000305 (curator inference), not direct in vitro kinetic measurement of the 7.6.2.2 reaction. The underlying study (Dong et al. 2024) demonstrated daunorubicin efflux function genetically (disruption phenotype, induction) rather than purifying the protein and measuring transport kinetics.",
    "The UniProt entry was first public in Feb 2025; the author's source snapshot is unknown. If the benchmark was constructed before this entry existed, the annotation provenance differs from what is shown here.",
    "Distinguishing the 4th digit (7.6.2.2 vs. other 7.6.2.x ABC drug transporters) would require substrate specificity knowledge not derivable from sequence alone, but this is moot since only one EC 7 option is presented."
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

**Accession:** `P0DXU7` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.757107+00:00.  

```json
"P0DXU7"
```

Source SHA-256: `e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.757107+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"value":"7.6.2.2"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Daunorubicin resistance ATP-binding protein DrrA3"}}}
```

Source SHA-256: `e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.757107+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:33148"}}],"reaction":{"ecNumber":"7.6.2.2","evidences":[{"evidenceCode":"ECO:0000305","id":"39375957","source":"PubMed"}],"name":"daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:33147"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:64677"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:39.757107+00:00.  

```json
{"citation":{"authors":["Dong J.","Ning J.","Tian Y.","Li H.","Chen H.","Guan W."],"citationCrossReferences":[{"database":"PubMed","id":"39375957"},{"database":"DOI","id":"10.1111/1751-7915.70023"}],"citationType":"journal article","firstPage":"e70023","id":"39375957","journal":"Microb. Biotechnol.","lastPage":"e70023","publicationDate":"2024","title":"The involvement of multiple ABC transporters in daunorubicin efflux in Streptomyces coeruleorubidus.","volume":"17"},"referenceNumber":2,"referencePositions":["FUNCTION IN DAUNORUBICIN EFFLUX","INDUCTION","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:44.049376+00:00.  

```text
ID   DRRA3_STRC4             Reviewed;         316 AA.
AC   P0DXU7;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA3 {ECO:0000305};
DE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};
GN   Name=drrA3 {ECO:0000303|PubMed:39375957};
GN   ORFNames=R5U08_20725 {ECO:0000312|EMBL:WOT36399.1};
OS   Streptomyces coeruleorubidus.
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;
OC   Streptomycetaceae; Streptomyces.
OX   NCBI_TaxID=116188;
```

Source SHA-256: `42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:44.049376+00:00.  

```text
DE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA3 {ECO:0000305};
DE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};
```

Source SHA-256: `42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)  
**Locator:** `lines 19-25`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:44.049376+00:00.  

```text
RN   [2]
RP   FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, AND DISRUPTION PHENOTYPE.
RX   PubMed=39375957; DOI=10.1111/1751-7915.70023;
RA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;
RT   "The involvement of multiple ABC transporters in daunorubicin efflux in
RT   Streptomyces coeruleorubidus.";
RL   Microb. Biotechnol. 17:e70023-e70023(2024).
```

Source SHA-256: `42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)  
**Locator:** `lines 33-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:44.049376+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP +
CC         phosphate + H(+); Xref=Rhea:RHEA:33147, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:30616, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:64677, ChEBI:CHEBI:456216; EC=7.6.2.2;
CC         Evidence={ECO:0000305|PubMed:39375957};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33148;
CC         Evidence={ECO:0000305|PubMed:39375957};
```

Source SHA-256: `42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 115. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
