# EC_number_0140

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 2.1.2.1

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATYALSQAHREQMEKSLVDSDPEIAQIMEKEIQRQRESILLIASENVTSRAVFDALGSPMSNKYSEGYPGARYYGGNQHIDAIELTCQARALKAFNLDPEKWGVNVQCLSGSPANLEVYQALMRPHDRLMGLDLPHGGHLSHGYQTPSRKISAVSTYFETFPYRVNTETGIIDYDTLEANAELYRPKCLVAGTSAYCRLIDYGRMRKIADKVGAYLIVDMAHISGLVAAGVIPSPFEYADVVTTTTHKSLRGPRGAMIFFRKGVRSTDPKTGKEIMYDLEGPINFSVFPGHQGGPHNHTITALAVALKQAATPEFRQYQEQVLKNAKALEVEFKALGHKLVSDGTDSHMVLLDLRPKGLDGARVEAVLEQINIACNKNSIPGDKSALTPCGIRIGTPAMTSRGMSEEDFKRVARYIDQVINLCKSIQADLPKEANKLKDFKAKVASGSVPEILALRKEVAEWASTYPLPV

[Multiple Choices]
A. 2.1.1.27
B. 3.5.2.6
C. 2.1.1.34
D. 2.1.2.1
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

> The sequence exactly matches the historical UniProt entry annotated as cytosolic serine hydroxymethyltransferase with EC 2.1.2.1. The cited reaction is the conversion of glycine to L-serine using methylenetetrahydrofolate. The annotation is supported by transfer from a reference protein (ECO:0000250), so it supports the key but is not, by itself, direct experimental evidence for this exact protein.

Citations as saved: [H2](#evidence-h2), [H4](#evidence-h4), [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices represent different enzyme families and reaction types, but the input gives only a sequence and no organism, pathway, or functional context. Recognizing this particular sequence as serine hydroxymethyltransferase would require protein-specific family identification; the choices alone do not establish that identity.


**Missing item-specific fact**

> The sequence's functional annotation or experimentally characterized reaction as serine hydroxymethyltransferase, or equivalent protein-specific homology evidence, is not supplied.


**Reason**

> A family-level sequence analysis might predict the answer, but the prompt provides no explicit, generally interpretable motif or other context that reliably distinguishes this exact EC assignment from the alternatives. Recalling the sequence's database identity would be lookup or memorization, not reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched sequence annotation and specified reaction support EC 2.1.2.1; the other choices classify different reactions.


### Important caveats

- The annotation evidence is transferred from a reference protein rather than shown here as a direct assay of the matched protein.
- The reviewer-only accession and database evidence were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices represent different enzyme families and reaction types, but the input gives only a sequence and no organism, pathway, or functional context. Recognizing this particular sequence as serine hydroxymethyltransferase would require protein-specific family identification; the choices alone do not establish that identity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's functional annotation or experimentally characterized reaction as serine hydroxymethyltransferase, or equivalent protein-specific homology evidence, is not supplied.",
    "reason": "A family-level sequence analysis might predict the answer, but the prompt provides no explicit, generally interpretable motif or other context that reliably distinguishes this exact EC assignment from the alternatives. Recalling the sequence's database identity would be lookup or memorization, not reasoning from supplied context."
  },
  "case_id": "EC_number_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H4",
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt entry annotated as cytosolic serine hydroxymethyltransferase with EC 2.1.2.1. The cited reaction is the conversion of glycine to L-serine using methylenetetrahydrofolate. The annotation is supported by transfer from a reference protein (ECO:0000250), so it supports the key but is not, by itself, direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The annotation evidence is transferred from a reference protein rather than shown here as a direct assay of the matched protein.",
    "The reviewer-only accession and database evidence were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence annotation and specified reaction support EC 2.1.2.1; the other choices classify different reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the historical UniProt entry annotated as cytosolic serine hydroxymethyltransferase with EC 2.1.2.1. The cited reaction is the conversion of glycine to L-serine using methylenetetrahydrofolate. The annotation is supported by transfer from a reference protein (ECO:0000250), so it supports the key but is not, by itself, direct experimental evidence for this exact protein.",
    "evidence_ids": ["H2", "H4", "C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices represent different enzyme families and reaction types, but the input gives only a sequence and no organism, pathway, or functional context. Recognizing this particular sequence as serine hydroxymethyltransferase would require protein-specific family identification; the choices alone do not establish that identity.",
    "missing_item_specific_fact": "The sequence's functional annotation or experimentally characterized reaction as serine hydroxymethyltransferase, or equivalent protein-specific homology evidence, is not supplied.",
    "reason": "A family-level sequence analysis might predict the answer, but the prompt provides no explicit, generally interpretable motif or other context that reliably distinguishes this exact EC assignment from the alternatives. Recalling the sequence's database identity would be lookup or memorization, not reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched sequence annotation and specified reaction support EC 2.1.2.1; the other choices classify different reactions."
  },
  "important_caveats": [
    "The annotation evidence is transferred from a reference protein rather than shown here as a direct assay of the matched protein.",
    "The reviewer-only accession and database evidence were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q4WXF4 (sequence matched, 471 AA) annotates this protein as 'Serine hydroxymethyltransferase, cytosolic' with EC 2.1.2.1. The EC assignment carries evidence code ECO:0000250 (similarity to P34896, human SHMT), and a 2025 PubMed paper (39825596) provides experimental functional characterization (FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE) confirming cytosolic SHMT activity in Aspergillus fumigatus. The catalytic activity comment (C5/H4) lists the canonical SHMT reaction: (6R)-5,10-methylene-THF + glycine + H₂O → (6S)-THF + L-serine (RHEA:15481). The expected answer D (2.1.2.1) is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved PLP-dependent enzyme motif 'GGNQHIDAIEL' (around residues 100–112) and the 'DLPHGG' motif, both hallmark signatures of the SHMT family within PLP fold-type I enzymes. SHMT is a well-known PLP-dependent enzyme that catalyzes the reversible serine ↔ glycine conversion coupled to folate. The three distractors belong to entirely different enzyme classes: 2.1.1.27 (nicotinamide N-methyltransferase, a small SAM-dependent methyltransferase with no PLP cofactor), 3.5.2.6 (dihydrofolate synthase, a hydrolase acting on C–N bonds), and 2.1.1.34 (a methyltransferase). None of these would contain the PLP-binding GGNQHIDAIEL motif or the characteristic SHMT fold architecture. A knowledgeable reader can recognize the PLP signature and the SHMT-specific conserved motifs, then eliminate the non-PLP distractors, arriving at EC 2.1.2.1.


**Missing item-specific fact**

> None critical. The GGNQHIDAIEL / DLPHGG motifs are general biochemical knowledge for PLP-dependent enzymes and specifically for the SHMT family. Recognizing these motifs and knowing that EC 2.1.2.1 corresponds to SHMT is within standard biochemistry knowledge.


**Reason**

> The sequence provides identifiable PLP-enzyme and SHMT-family motifs that distinguish the correct answer from the distractors, which are from unrelated enzyme classes (methyltransferases, hydrolases). This constitutes a concrete biological argument from the supplied sequence rather than pure database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span three distinct EC classes (2.1.1.x methyltransferases, 3.5.2.x hydrolases, 2.1.2.x transferases of one-carbon groups). The PLP-dependent SHMT signature in the sequence cleanly selects 2.1.2.1 and excludes the others. No alternative choice is defensible given the sequence features.


### Important caveats

- The primary UniProt EC annotation uses evidence code ECO:0000250 (similarity to P34896), i.e., it is a transfer annotation rather than direct experimental measurement on this specific fungal protein. However, the 2025 PubMed reference (39825596) provides experimental functional evidence (gene disruption phenotype, subcellular localization) supporting SHMT activity in A. fumigatus.
- The reviewer-only evidence confirms the sequence is a 471-aa match to Q4WXF4 (GLYC_ASPFU). The model was not given the accession or UniProt annotation.
- EC 2.1.1.34 is a relatively obscure entry; its exact identity may be less familiar to some readers, but it is a methyltransferase and would not carry the PLP SHMT motif, so it remains distinguishable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved PLP-dependent enzyme motif 'GGNQHIDAIEL' (around residues 100–112) and the 'DLPHGG' motif, both hallmark signatures of the SHMT family within PLP fold-type I enzymes. SHMT is a well-known PLP-dependent enzyme that catalyzes the reversible serine ↔ glycine conversion coupled to folate. The three distractors belong to entirely different enzyme classes: 2.1.1.27 (nicotinamide N-methyltransferase, a small SAM-dependent methyltransferase with no PLP cofactor), 3.5.2.6 (dihydrofolate synthase, a hydrolase acting on C–N bonds), and 2.1.1.34 (a methyltransferase). None of these would contain the PLP-binding GGNQHIDAIEL motif or the characteristic SHMT fold architecture. A knowledgeable reader can recognize the PLP signature and the SHMT-specific conserved motifs, then eliminate the non-PLP distractors, arriving at EC 2.1.2.1.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The GGNQHIDAIEL / DLPHGG motifs are general biochemical knowledge for PLP-dependent enzymes and specifically for the SHMT family. Recognizing these motifs and knowing that EC 2.1.2.1 corresponds to SHMT is within standard biochemistry knowledge.",
    "reason": "The sequence provides identifiable PLP-enzyme and SHMT-family motifs that distinguish the correct answer from the distractors, which are from unrelated enzyme classes (methyltransferases, hydrolases). This constitutes a concrete biological argument from the supplied sequence rather than pure database lookup."
  },
  "case_id": "EC_number_0140",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q4WXF4 (sequence matched, 471 AA) annotates this protein as 'Serine hydroxymethyltransferase, cytosolic' with EC 2.1.2.1. The EC assignment carries evidence code ECO:0000250 (similarity to P34896, human SHMT), and a 2025 PubMed paper (39825596) provides experimental functional characterization (FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE) confirming cytosolic SHMT activity in Aspergillus fumigatus. The catalytic activity comment (C5/H4) lists the canonical SHMT reaction: (6R)-5,10-methylene-THF + glycine + H₂O → (6S)-THF + L-serine (RHEA:15481). The expected answer D (2.1.2.1) is well-supported."
  },
  "important_caveats": [
    "The primary UniProt EC annotation uses evidence code ECO:0000250 (similarity to P34896), i.e., it is a transfer annotation rather than direct experimental measurement on this specific fungal protein. However, the 2025 PubMed reference (39825596) provides experimental functional evidence (gene disruption phenotype, subcellular localization) supporting SHMT activity in A. fumigatus.",
    "The reviewer-only evidence confirms the sequence is a 471-aa match to Q4WXF4 (GLYC_ASPFU). The model was not given the accession or UniProt annotation.",
    "EC 2.1.1.34 is a relatively obscure entry; its exact identity may be less familiar to some readers, but it is a methyltransferase and would not carry the PLP SHMT motif, so it remains distinguishable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three distinct EC classes (2.1.1.x methyltransferases, 3.5.2.x hydrolases, 2.1.2.x transferases of one-carbon groups). The PLP-dependent SHMT signature in the sequence cleanly selects 2.1.2.1 and excludes the others. No alternative choice is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0140",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q4WXF4 (sequence matched, 471 AA) annotates this protein as 'Serine hydroxymethyltransferase, cytosolic' with EC 2.1.2.1. The EC assignment carries evidence code ECO:0000250 (similarity to P34896, human SHMT), and a 2025 PubMed paper (39825596) provides experimental functional characterization (FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE) confirming cytosolic SHMT activity in Aspergillus fumigatus. The catalytic activity comment (C5/H4) lists the canonical SHMT reaction: (6R)-5,10-methylene-THF + glycine + H₂O → (6S)-THF + L-serine (RHEA:15481). The expected answer D (2.1.2.1) is well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved PLP-dependent enzyme motif 'GGNQHIDAIEL' (around residues 100–112) and the 'DLPHGG' motif, both hallmark signatures of the SHMT family within PLP fold-type I enzymes. SHMT is a well-known PLP-dependent enzyme that catalyzes the reversible serine ↔ glycine conversion coupled to folate. The three distractors belong to entirely different enzyme classes: 2.1.1.27 (nicotinamide N-methyltransferase, a small SAM-dependent methyltransferase with no PLP cofactor), 3.5.2.6 (dihydrofolate synthase, a hydrolase acting on C–N bonds), and 2.1.1.34 (a methyltransferase). None of these would contain the PLP-binding GGNQHIDAIEL motif or the characteristic SHMT fold architecture. A knowledgeable reader can recognize the PLP signature and the SHMT-specific conserved motifs, then eliminate the non-PLP distractors, arriving at EC 2.1.2.1.",
    "missing_item_specific_fact": "None critical. The GGNQHIDAIEL / DLPHGG motifs are general biochemical knowledge for PLP-dependent enzymes and specifically for the SHMT family. Recognizing these motifs and knowing that EC 2.1.2.1 corresponds to SHMT is within standard biochemistry knowledge.",
    "reason": "The sequence provides identifiable PLP-enzyme and SHMT-family motifs that distinguish the correct answer from the distractors, which are from unrelated enzyme classes (methyltransferases, hydrolases). This constitutes a concrete biological argument from the supplied sequence rather than pure database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span three distinct EC classes (2.1.1.x methyltransferases, 3.5.2.x hydrolases, 2.1.2.x transferases of one-carbon groups). The PLP-dependent SHMT signature in the sequence cleanly selects 2.1.2.1 and excludes the others. No alternative choice is defensible given the sequence features."
  },
  "important_caveats": [
    "The primary UniProt EC annotation uses evidence code ECO:0000250 (similarity to P34896), i.e., it is a transfer annotation rather than direct experimental measurement on this specific fungal protein. However, the 2025 PubMed reference (39825596) provides experimental functional evidence (gene disruption phenotype, subcellular localization) supporting SHMT activity in A. fumigatus.",
    "The reviewer-only evidence confirms the sequence is a 471-aa match to Q4WXF4 (GLYC_ASPFU). The model was not given the accession or UniProt annotation.",
    "EC 2.1.1.34 is a relatively obscure entry; its exact identity may be less familiar to some readers, but it is a methyltransferase and would not carry the PLP SHMT motif, so it remains distinguishable."
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

**Accession:** `Q4WXF4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 122. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.546837+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P34896","source":"UniProtKB"}],"value":"2.1.2.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39825596","source":"PubMed"}],"value":"Serine hydroxymethyltransferase, cytosolic"}}}
```

Source SHA-256: `58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.546837+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.1.2.1","evidences":[{"evidenceCode":"ECO:0000250","id":"P34896","source":"UniProtKB"}],"name":"(6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:15481"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15636"},{"database":"ChEBI","id":"CHEBI:33384"},{"database":"ChEBI","id":"CHEBI:57305"},{"database":"ChEBI","id":"CHEBI:57453"}]}}
```

Source SHA-256: `58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:56.546837+00:00.  

```json
{"citation":{"authors":["Alharthi R.","Sueiro-Olivares M.","Storer I.","Bin Shuraym H.","Scott J.","Al-Shidhani R.","Fortune-Grant R.","Bignell E.","Tabernero L.","Bromley M.","Zhao C.","Amich J."],"citationCrossReferences":[{"database":"PubMed","id":"39825596"},{"database":"DOI","id":"10.1080/21505594.2024.2449075"}],"citationType":"journal article","firstPage":"2449075","id":"39825596","journal":"Virulence","lastPage":"2449075","publicationDate":"2025","title":"The sulfur-related metabolic status of Aspergillus fumigatus during infection reveals cytosolic serine hydroxymethyltransferase as a promising antifungal target.","volume":"16"},"referenceNumber":2,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","INDUCTION","DISRUPTION PHENOTYPE","BIOTECHNOLOGY"]}
```

Source SHA-256: `58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:31:00.835030+00:00.  

```text
ID   GLYC_ASPFU              Reviewed;         471 AA.
AC   Q4WXF4;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-JUL-2005, sequence version 1.
DT   28-JAN-2026, entry version 122.
DE   RecName: Full=Serine hydroxymethyltransferase, cytosolic {ECO:0000303|PubMed:39825596};
DE            EC=2.1.2.1 {ECO:0000250|UniProtKB:P34896};
GN   Name=shmB {ECO:0000303|PubMed:39825596}; ORFNames=AFUA_3G09320;
OS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /
OS   Af293) (Neosartorya fumigata).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Fumigati.
OX   NCBI_TaxID=330879;
```

Source SHA-256: `86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:31:00.835030+00:00.  

```text
DE   RecName: Full=Serine hydroxymethyltransferase, cytosolic {ECO:0000303|PubMed:39825596};
DE            EC=2.1.2.1 {ECO:0000250|UniProtKB:P34896};
```

Source SHA-256: `86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)  
**Locator:** `lines 40-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:31:00.835030+00:00.  

```text
RN   [2]
RP   FUNCTION, SUBCELLULAR LOCATION, INDUCTION, DISRUPTION PHENOTYPE, AND
RP   BIOTECHNOLOGY.
RX   PubMed=39825596; DOI=10.1080/21505594.2024.2449075;
RA   Alharthi R., Sueiro-Olivares M., Storer I., Bin Shuraym H., Scott J.,
RA   Al-Shidhani R., Fortune-Grant R., Bignell E., Tabernero L., Bromley M.,
RA   Zhao C., Amich J.;
RT   "The sulfur-related metabolic status of Aspergillus fumigatus during
RT   infection reveals cytosolic serine hydroxymethyltransferase as a promising
RT   antifungal target.";
RL   Virulence 16:2449075-2449075(2025).
```

Source SHA-256: `86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)  
**Locator:** `lines 55-60`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 122 / 1.  
**Retrieved:** 2026-11-02T04:31:00.835030+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=(6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O =
CC         (6S)-5,6,7,8-tetrahydrofolate + L-serine; Xref=Rhea:RHEA:15481,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15636, ChEBI:CHEBI:33384,
CC         ChEBI:CHEBI:57305, ChEBI:CHEBI:57453; EC=2.1.2.1;
CC         Evidence={ECO:0000250|UniProtKB:P34896};
```

Source SHA-256: `86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 140. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
