# EC_number_0122

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 2.7.11.24

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAEFVRAQIFGTTFEITSRYTELAPVGMGAFGLVCSAKDQLTNQAVAVKKIMKPFSTPVLSKRTYRELKLLKHLRHENVISLSDIFISPLEDIYFVTELLGTDLHRLLTSRPLEKQFIQYFLYQILRGLKYVHSAGVVHRDLKPSNILVNENCDLKICDFGLARIQDPQMTGYVSTRYYRAPEIMLTWQKYDVEVDIWSVGCIFAEMLEGKPLFPGKDHVNQFSIITELLGTPPDDVIQTICSENTLRFVQSLPKRERQPLTKKFKNADPQAIELLERMLVFDPRTRIRAGDALADPYLAPYHDPTDEPEAEEKFDWSFNDADLPVDTWKIMMYSEILDYHNVDAQNGEEVGVPQ

[Multiple Choices]
A. 2.7.11.24
B. 2.7.11.1
C. 2.7.8.43
D. 4.3.1.24
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

> The exact sequence matches a UniProt entry annotated as MAP kinase HOG1 with EC 2.7.11.24. The catalytic activity annotation assigns this EC to serine and threonine phosphorylation. However, the EC assignment is transferred by similarity from UniProtKB:P32485, not demonstrated here by a direct assay of this protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains protein-kinase features, supporting a kinase function and making the non-kinase choices poor fits. Those features do not distinguish the MAP-kinase EC 2.7.11.24 from the broader serine/threonine-kinase EC 2.7.11.1.


**Missing item-specific fact**

> The protein-specific identification as HOG1/MAP kinase, or equivalent evidence for its MAPK subtype, is needed to select the specific EC assignment over the broader kinase option.


**Reason**

> The input supplies a sequence but no organism or functional annotation. Recognizing its particular identity or establishing its MAPK subtype requires item-specific information; generic kinase motifs do not resolve the key distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The kinase options overlap in broad catalytic chemistry, but the question requests a complete EC number and the supported annotation assigns the more specific MAPK EC number.


### Important caveats

- The sequence match applies to the supplied 355-residue protein.
- The supporting database EC assignment is based on similarity to another UniProt entry; the cited evidence does not establish direct experimental confirmation for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains protein-kinase features, supporting a kinase function and making the non-kinase choices poor fits. Those features do not distinguish the MAP-kinase EC 2.7.11.24 from the broader serine/threonine-kinase EC 2.7.11.1.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as HOG1/MAP kinase, or equivalent evidence for its MAPK subtype, is needed to select the specific EC assignment over the broader kinase option.",
    "reason": "The input supplies a sequence but no organism or functional annotation. Recognizing its particular identity or establishing its MAPK subtype requires item-specific information; generic kinase motifs do not resolve the key distinction."
  },
  "case_id": "EC_number_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as MAP kinase HOG1 with EC 2.7.11.24. The catalytic activity annotation assigns this EC to serine and threonine phosphorylation. However, the EC assignment is transferred by similarity from UniProtKB:P32485, not demonstrated here by a direct assay of this protein."
  },
  "important_caveats": [
    "The sequence match applies to the supplied 355-residue protein.",
    "The supporting database EC assignment is based on similarity to another UniProt entry; the cited evidence does not establish direct experimental confirmation for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase options overlap in broad catalytic chemistry, but the question requests a complete EC number and the supported annotation assigns the more specific MAPK EC number."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as MAP kinase HOG1 with EC 2.7.11.24. The catalytic activity annotation assigns this EC to serine and threonine phosphorylation. However, the EC assignment is transferred by similarity from UniProtKB:P32485, not demonstrated here by a direct assay of this protein.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains protein-kinase features, supporting a kinase function and making the non-kinase choices poor fits. Those features do not distinguish the MAP-kinase EC 2.7.11.24 from the broader serine/threonine-kinase EC 2.7.11.1.",
    "missing_item_specific_fact": "The protein-specific identification as HOG1/MAP kinase, or equivalent evidence for its MAPK subtype, is needed to select the specific EC assignment over the broader kinase option.",
    "reason": "The input supplies a sequence but no organism or functional annotation. Recognizing its particular identity or establishing its MAPK subtype requires item-specific information; generic kinase motifs do not resolve the key distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The kinase options overlap in broad catalytic chemistry, but the question requests a complete EC number and the supported annotation assigns the more specific MAPK EC number."
  },
  "important_caveats": [
    "The sequence match applies to the supplied 355-residue protein.",
    "The supporting database EC assignment is based on similarity to another UniProt entry; the cited evidence does not establish direct experimental confirmation for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A5B9GBF0) identifies this protein as Mitogen-activated protein kinase HOG1 from Aureobasidium melanogenum, with EC 2.7.11.24 assigned via similarity (ECO:0000250) to S. cerevisiae HOG1 (P32485). The catalytic activity is phosphorylation of L-seryl and L-threonyl residues on proteins using ATP, consistent with MAP kinase function. The sequence matches exactly (SHA256 confirmed). Note that the EC assignment is by similarity, not direct experimental measurement on this specific protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains canonical protein kinase motifs: HRD catalytic loop (HRDLKPSN), DFG motif (DFGLARIQ), and APE motif (APEIMLTWQ), clearly identifying it as a protein kinase (EC 2.7.11.x) and eliminating C (phosphatidylcholine synthase, EC 2.7.8.43) and D (cysteine synthase, EC 4.3.1.24). Within the kinase class, the activation loop region 'MTGYVSTRYYRAPEIM' contains a TGY motif, which is the hallmark TXY activation-loop signature of the MAP kinase family (ERK, p38, JNK, HOG1), distinguishing it from PKA (EC 2.7.11.1), which lacks this motif and has a different activation-loop architecture. EC 2.7.11.24 is the standard EC number for mitogen-activated protein kinases.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides identifiable kinase domain motifs and a TGY-like activation loop that allow reasoning from general protein kinase family knowledge to distinguish MAP kinase (2.7.11.24) from PKA (2.7.11.1). The non-kinase options C and D are eliminated by the presence of catalytic kinase motifs. While precise EC assignment benefits from database lookup, the biological argument from sequence features is meaningful and sufficient among the given choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly non-kinase enzymes eliminated by the presence of HRD/DFG/APE motifs. Option B (PKA) is a kinase but lacks the TXY activation-loop motif present in this sequence. Option A is the only choice consistent with both the kinase classification and the MAP kinase-specific activation loop signature.


### Important caveats

- The EC 2.7.11.24 assignment in UniProt is based on similarity (ECO:0000250) to P32485 (S. cerevisiae HOG1), not direct experimental characterization of this specific A. melanogenum protein.
- The TGY motif identification from raw sequence requires familiarity with kinase family signatures; a model without this knowledge would struggle to distinguish A from B.
- The protein is from a fungal organism (Aureobasidium melanogenum), and HOG1 is the canonical fungal MAP kinase involved in osmotic stress signaling, well-documented in the literature (PubMed:33375973).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs: HRD catalytic loop (HRDLKPSN), DFG motif (DFGLARIQ), and APE motif (APEIMLTWQ), clearly identifying it as a protein kinase (EC 2.7.11.x) and eliminating C (phosphatidylcholine synthase, EC 2.7.8.43) and D (cysteine synthase, EC 4.3.1.24). Within the kinase class, the activation loop region 'MTGYVSTRYYRAPEIM' contains a TGY motif, which is the hallmark TXY activation-loop signature of the MAP kinase family (ERK, p38, JNK, HOG1), distinguishing it from PKA (EC 2.7.11.1), which lacks this motif and has a different activation-loop architecture. EC 2.7.11.24 is the standard EC number for mitogen-activated protein kinases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides identifiable kinase domain motifs and a TGY-like activation loop that allow reasoning from general protein kinase family knowledge to distinguish MAP kinase (2.7.11.24) from PKA (2.7.11.1). The non-kinase options C and D are eliminated by the presence of catalytic kinase motifs. While precise EC assignment benefits from database lookup, the biological argument from sequence features is meaningful and sufficient among the given choices."
  },
  "case_id": "EC_number_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A5B9GBF0) identifies this protein as Mitogen-activated protein kinase HOG1 from Aureobasidium melanogenum, with EC 2.7.11.24 assigned via similarity (ECO:0000250) to S. cerevisiae HOG1 (P32485). The catalytic activity is phosphorylation of L-seryl and L-threonyl residues on proteins using ATP, consistent with MAP kinase function. The sequence matches exactly (SHA256 confirmed). Note that the EC assignment is by similarity, not direct experimental measurement on this specific protein."
  },
  "important_caveats": [
    "The EC 2.7.11.24 assignment in UniProt is based on similarity (ECO:0000250) to P32485 (S. cerevisiae HOG1), not direct experimental characterization of this specific A. melanogenum protein.",
    "The TGY motif identification from raw sequence requires familiarity with kinase family signatures; a model without this knowledge would struggle to distinguish A from B.",
    "The protein is from a fungal organism (Aureobasidium melanogenum), and HOG1 is the canonical fungal MAP kinase involved in osmotic stress signaling, well-documented in the literature (PubMed:33375973)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly non-kinase enzymes eliminated by the presence of HRD/DFG/APE motifs. Option B (PKA) is a kinase but lacks the TXY activation-loop motif present in this sequence. Option A is the only choice consistent with both the kinase classification and the MAP kinase-specific activation loop signature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A5B9GBF0) identifies this protein as Mitogen-activated protein kinase HOG1 from Aureobasidium melanogenum, with EC 2.7.11.24 assigned via similarity (ECO:0000250) to S. cerevisiae HOG1 (P32485). The catalytic activity is phosphorylation of L-seryl and L-threonyl residues on proteins using ATP, consistent with MAP kinase function. The sequence matches exactly (SHA256 confirmed). Note that the EC assignment is by similarity, not direct experimental measurement on this specific protein.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains canonical protein kinase motifs: HRD catalytic loop (HRDLKPSN), DFG motif (DFGLARIQ), and APE motif (APEIMLTWQ), clearly identifying it as a protein kinase (EC 2.7.11.x) and eliminating C (phosphatidylcholine synthase, EC 2.7.8.43) and D (cysteine synthase, EC 4.3.1.24). Within the kinase class, the activation loop region 'MTGYVSTRYYRAPEIM' contains a TGY motif, which is the hallmark TXY activation-loop signature of the MAP kinase family (ERK, p38, JNK, HOG1), distinguishing it from PKA (EC 2.7.11.1), which lacks this motif and has a different activation-loop architecture. EC 2.7.11.24 is the standard EC number for mitogen-activated protein kinases.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides identifiable kinase domain motifs and a TGY-like activation loop that allow reasoning from general protein kinase family knowledge to distinguish MAP kinase (2.7.11.24) from PKA (2.7.11.1). The non-kinase options C and D are eliminated by the presence of catalytic kinase motifs. While precise EC assignment benefits from database lookup, the biological argument from sequence features is meaningful and sufficient among the given choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly non-kinase enzymes eliminated by the presence of HRD/DFG/APE motifs. Option B (PKA) is a kinase but lacks the TXY activation-loop motif present in this sequence. Option A is the only choice consistent with both the kinase classification and the MAP kinase-specific activation loop signature."
  },
  "important_caveats": [
    "The EC 2.7.11.24 assignment in UniProt is based on similarity (ECO:0000250) to P32485 (S. cerevisiae HOG1), not direct experimental characterization of this specific A. melanogenum protein.",
    "The TGY motif identification from raw sequence requires familiarity with kinase family signatures; a model without this knowledge would struggle to distinguish A from B.",
    "The protein is from a fungal organism (Aureobasidium melanogenum), and HOG1 is the canonical fungal MAP kinase involved in osmotic stress signaling, well-documented in the literature (PubMed:33375973)."
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

**Accession:** `A0A5B9GBF0` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 29. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5B9GBF0.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:49.473180+00:00.  

```json
"A0A5B9GBF0"
```

Source SHA-256: `fba079004196dc4aa9a4146777e2ad8ed7d3390b474caa53a6cffcdd32fef7bf`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5B9GBF0.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:49.473180+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33375973","source":"PubMed"}],"value":"High osmolarity glycerol response protein 1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"value":"2.7.11.24"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"33375973","source":"PubMed"}],"value":"Mitogen-activated protein kinase HOG1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"33375973","source":"PubMed"}],"value":"MAP kinase HOG1"}]}}
```

Source SHA-256: `fba079004196dc4aa9a4146777e2ad8ed7d3390b474caa53a6cffcdd32fef7bf`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5B9GBF0.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:49.473180+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:17990"}}],"reaction":{"ecNumber":"2.7.11.24","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"name":"L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17989"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:83421"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `fba079004196dc4aa9a4146777e2ad8ed7d3390b474caa53a6cffcdd32fef7bf`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A5B9GBF0.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:49.473180+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:46609"}}],"reaction":{"ecNumber":"2.7.11.24","evidences":[{"evidenceCode":"ECO:0000250","id":"P32485","source":"UniProtKB"}],"name":"L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] + ADP + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:46608"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:30616"},{"database":"ChEBI","id":"CHEBI:61977"},{"database":"ChEBI","id":"CHEBI:456216"}]}}
```

Source SHA-256: `fba079004196dc4aa9a4146777e2ad8ed7d3390b474caa53a6cffcdd32fef7bf`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5B9GBF0?format=txt&versions=29)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 29 / 1.  
**Retrieved:** 2026-11-01T06:27:31.440600+00:00.  

```text
ID   HOG1_AURME              Reviewed;         355 AA.
AC   A0A5B9GBF0;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   13-NOV-2019, sequence version 1.
DT   28-JAN-2026, entry version 29.
DE   RecName: Full=Mitogen-activated protein kinase HOG1 {ECO:0000303|PubMed:33375973};
DE            Short=MAP kinase HOG1 {ECO:0000303|PubMed:33375973};
DE            EC=2.7.11.24 {ECO:0000250|UniProtKB:P32485};
DE   AltName: Full=High osmolarity glycerol response protein 1 {ECO:0000303|PubMed:33375973};
GN   Name=HOG1 {ECO:0000303|PubMed:33375973};
GN   ORFNames=KCU76_g14496, KCU76_g8675, KCV03_g1946;
OS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;
OC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.
OX   NCBI_TaxID=46634;
```

Source SHA-256: `b41aad72deba1b2a50b4811f2707c4302afb398ce10bc95f1c81941f78b1051a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5B9GBF0?format=txt&versions=29)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 29 / 1.  
**Retrieved:** 2026-11-01T06:27:31.440600+00:00.  

```text
DE   RecName: Full=Mitogen-activated protein kinase HOG1 {ECO:0000303|PubMed:33375973};
DE            Short=MAP kinase HOG1 {ECO:0000303|PubMed:33375973};
DE            EC=2.7.11.24 {ECO:0000250|UniProtKB:P32485};
DE   AltName: Full=High osmolarity glycerol response protein 1 {ECO:0000303|PubMed:33375973};
```

Source SHA-256: `b41aad72deba1b2a50b4811f2707c4302afb398ce10bc95f1c81941f78b1051a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5B9GBF0?format=txt&versions=29)  
**Locator:** `lines 57-64`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 29 / 1.  
**Retrieved:** 2026-11-01T06:27:31.440600+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-seryl-[protein] + ATP = O-phospho-L-seryl-[protein] + ADP +
CC         H(+); Xref=Rhea:RHEA:17989, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15378, ChEBI:CHEBI:29999, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:83421, ChEBI:CHEBI:456216; EC=2.7.11.24;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:17990;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
```

Source SHA-256: `b41aad72deba1b2a50b4811f2707c4302afb398ce10bc95f1c81941f78b1051a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A5B9GBF0?format=txt&versions=29)  
**Locator:** `lines 65-72`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 29 / 1.  
**Retrieved:** 2026-11-01T06:27:31.440600+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-threonyl-[protein] + ATP = O-phospho-L-threonyl-[protein] +
CC         ADP + H(+); Xref=Rhea:RHEA:46608, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15378, ChEBI:CHEBI:30013, ChEBI:CHEBI:30616,
CC         ChEBI:CHEBI:61977, ChEBI:CHEBI:456216; EC=2.7.11.24;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:46609;
CC         Evidence={ECO:0000250|UniProtKB:P32485};
```

Source SHA-256: `b41aad72deba1b2a50b4811f2707c4302afb398ce10bc95f1c81941f78b1051a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 122. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
