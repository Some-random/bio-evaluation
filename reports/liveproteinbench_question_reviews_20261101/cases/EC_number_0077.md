# EC_number_0077

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 3.1.3.16

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MGQTLSEPVVDKTSSEGEDDCCIYGVSAMQGWRISMEDAHAAVLDLHAKYTSPEETSTDPAKRLAFFGVYDGHGGDKVALFAGENVHKIVAKQDSFAKGDIEQALKDGFLATDRAILEDPKYEEEVSGCTAAVSVISKHKIWVANAGDSRSVLGVKGRAKPLSFDHKPQNEGEKARISAAGGFVDFGRVNGNLALSRAIGDFEFKKSPELAPEQQIVTAYPDVTVHELSDDDEFLVIACDGIWDCQSSQAVVEFVRRGIAAKQELYRICENMMDNCLASNSETGGVGCDNMTMIIIGLLNGRTKEECGDAAEFRGPGIRNQFEENPDDYDMENDRARGFSVRSGRIILLGDGTELVPDQNDEELFDQTEEDRDLPSQVQRELPDSARNEREGTPGPQSKTDATSKSEEGSSASTSESTVTPAGSSTSGAPEKSTS

[Multiple Choices]
A. 3.1.3.112
B. 3.1.3.16
C. 2.3.1.319
D. 4.2.1.18
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

> The exact-match sequence is annotated as EC 3.1.3.16, and the record cites PubMed evidence (ECO:0000269) for protein serine dephosphorylation. The historical record also carries this EC assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a conserved, acidic PP2C-like catalytic core, including motifs such as DGHGG and GDGT, consistent with a metal-dependent protein phosphatase. That provides a biological basis for selecting the protein-phosphatase option over the acyltransferase and dehydratase options; the alternative phosphatase choice is not as consistent with this catalytic family.


**Missing item-specific fact**

> An experimental substrate profile would establish activity and specificity more directly, but the sequence-family evidence meaningfully distinguishes the listed choices.


**Reason**

> The supplied sequence contains recognizable phosphatase-family features, not merely an identity that must be recalled from a database. Those features support the EC class represented by B, while the reviewer-only annotation corroborates the key but is not information supplied to the evaluated model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence supports a PP2C-like protein phosphatase, and no other listed choice is comparably supported.


### Important caveats

- The cited UniProt annotation links the EC assignment to a publication, but this audit has not independently evaluated the primary paper.
- Sequence-family recognition supports the choice but is not itself an experimental measurement of this protein's catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a conserved, acidic PP2C-like catalytic core, including motifs such as DGHGG and GDGT, consistent with a metal-dependent protein phosphatase. That provides a biological basis for selecting the protein-phosphatase option over the acyltransferase and dehydratase options; the alternative phosphatase choice is not as consistent with this catalytic family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "An experimental substrate profile would establish activity and specificity more directly, but the sequence-family evidence meaningfully distinguishes the listed choices.",
    "reason": "The supplied sequence contains recognizable phosphatase-family features, not merely an identity that must be recalled from a database. Those features support the EC class represented by B, while the reviewer-only annotation corroborates the key but is not information supplied to the evaluated model."
  },
  "case_id": "EC_number_0077",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact-match sequence is annotated as EC 3.1.3.16, and the record cites PubMed evidence (ECO:0000269) for protein serine dephosphorylation. The historical record also carries this EC assignment."
  },
  "important_caveats": [
    "The cited UniProt annotation links the EC assignment to a publication, but this audit has not independently evaluated the primary paper.",
    "Sequence-family recognition supports the choice but is not itself an experimental measurement of this protein's catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a PP2C-like protein phosphatase, and no other listed choice is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0077",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-match sequence is annotated as EC 3.1.3.16, and the record cites PubMed evidence (ECO:0000269) for protein serine dephosphorylation. The historical record also carries this EC assignment.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a conserved, acidic PP2C-like catalytic core, including motifs such as DGHGG and GDGT, consistent with a metal-dependent protein phosphatase. That provides a biological basis for selecting the protein-phosphatase option over the acyltransferase and dehydratase options; the alternative phosphatase choice is not as consistent with this catalytic family.",
    "missing_item_specific_fact": "An experimental substrate profile would establish activity and specificity more directly, but the sequence-family evidence meaningfully distinguishes the listed choices.",
    "reason": "The supplied sequence contains recognizable phosphatase-family features, not merely an identity that must be recalled from a database. Those features support the EC class represented by B, while the reviewer-only annotation corroborates the key but is not information supplied to the evaluated model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence supports a PP2C-like protein phosphatase, and no other listed choice is comparably supported."
  },
  "important_caveats": [
    "The cited UniProt annotation links the EC assignment to a publication, but this audit has not independently evaluated the primary paper.",
    "Sequence-family recognition supports the choice but is not itself an experimental measurement of this protein's catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A7U2MSD6 (PP2C2_ASPFN) from Aspergillus flavus carries EC 3.1.3.16 with direct experimental evidence (ECO:0000269, PubMed:37754565, a 2023 MBio paper reporting catalytic activity assays). The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed). The annotated catalytic reactions (dephosphorylation of O-phospho-L-seryl- and O-phospho-L-threonyl-&#91;protein&#93;) are consistent with EC 3.1.3.16 (protein serine/threonine phosphatase, PP2C family).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark PP2C-superfamily motifs: multiple 'GD' dipeptide motifs (e.g., 'AGDSRSVLG', 'CDGIWDC'), a DxT/S-like region, and conserved aspartate residues in the spatial arrangement characteristic of the metal-dependent PP2C phosphatase fold. PP2C is the canonical enzyme assigned EC 3.1.3.16. The other options represent clearly different reaction classes: 2.3.1.319 is an acyltransferase (transferase class, EC 2.x.x.x) and 4.2.1.18 is a hydro-lyase (EC 4.x.x.x), neither of which involves phosphoester hydrolysis. EC 3.1.3.112 is a phosphatase but of a different subfamily (a lipid/inositol phosphate phosphatase), lacking the PP2C GD-motif architecture. Recognizing the PP2C fold from these conserved sequence signatures and mapping it to the canonical EC 3.1.3.16 is a well-established bioinformatics inference.


**Missing item-specific fact**

> None critical. The PP2C fold motifs are visible in the supplied sequence. The exact distinction between EC 3.1.3.112 and 3.1.3.16 relies on knowing that 3.1.3.112 is not a PP2C-family enzyme, which is standard enzyme-taxonomy knowledge.


**Reason**

> A model with general protein-structure knowledge can identify the PP2C GD motifs and DxT/S region in the sequence, infer a metal-dependent serine/threonine phosphatase fold, and map this to EC 3.1.3.16. The transferase (C) and lyase (D) options are excluded by reaction-class reasoning. Distinguishing 3.1.3.112 from 3.1.3.16 requires knowing that 3.1.3.112 is not a PP2C, which is part of standard EC taxonomy knowledge rather than an obscure item-specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PP2C sequence motifs in the supplied sequence point specifically to EC 3.1.3.16. Options C (transferase) and D (lyase) are different reaction classes and can be excluded. Option A (3.1.3.112) is a phosphatase but of a different subfamily lacking the PP2C GD-motif architecture visible in the sequence. No two options are equally defensible given the sequence evidence.


### Important caveats

- The EC 3.1.3.16 annotation is backed by direct experimental assay (ECO:0000269) from PubMed:37754565, not merely computational prediction.
- The PP2C motif recognition is a well-established bioinformatics approach, but distinguishing between two 3.1.3.x phosphatases (A vs B) is more demanding than cross-class discrimination; a model lacking knowledge of what 3.1.3.112 specifically is may struggle.
- The UniProt entry was first publicly released on 2025-02-05 (Swiss-Prot), so the experimental annotation post-dates some possible training cutoffs; however, the PP2C fold itself is a long-known protein family.
- All reviewer evidence is reviewer-only and was not available to the evaluated model; the model must rely on sequence motifs and general enzyme knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark PP2C-superfamily motifs: multiple 'GD' dipeptide motifs (e.g., 'AGDSRSVLG', 'CDGIWDC'), a DxT/S-like region, and conserved aspartate residues in the spatial arrangement characteristic of the metal-dependent PP2C phosphatase fold. PP2C is the canonical enzyme assigned EC 3.1.3.16. The other options represent clearly different reaction classes: 2.3.1.319 is an acyltransferase (transferase class, EC 2.x.x.x) and 4.2.1.18 is a hydro-lyase (EC 4.x.x.x), neither of which involves phosphoester hydrolysis. EC 3.1.3.112 is a phosphatase but of a different subfamily (a lipid/inositol phosphate phosphatase), lacking the PP2C GD-motif architecture. Recognizing the PP2C fold from these conserved sequence signatures and mapping it to the canonical EC 3.1.3.16 is a well-established bioinformatics inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The PP2C fold motifs are visible in the supplied sequence. The exact distinction between EC 3.1.3.112 and 3.1.3.16 relies on knowing that 3.1.3.112 is not a PP2C-family enzyme, which is standard enzyme-taxonomy knowledge.",
    "reason": "A model with general protein-structure knowledge can identify the PP2C GD motifs and DxT/S region in the sequence, infer a metal-dependent serine/threonine phosphatase fold, and map this to EC 3.1.3.16. The transferase (C) and lyase (D) options are excluded by reaction-class reasoning. Distinguishing 3.1.3.112 from 3.1.3.16 requires knowing that 3.1.3.112 is not a PP2C, which is part of standard EC taxonomy knowledge rather than an obscure item-specific annotation."
  },
  "case_id": "EC_number_0077",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A7U2MSD6 (PP2C2_ASPFN) from Aspergillus flavus carries EC 3.1.3.16 with direct experimental evidence (ECO:0000269, PubMed:37754565, a 2023 MBio paper reporting catalytic activity assays). The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed). The annotated catalytic reactions (dephosphorylation of O-phospho-L-seryl- and O-phospho-L-threonyl-[protein]) are consistent with EC 3.1.3.16 (protein serine/threonine phosphatase, PP2C family)."
  },
  "important_caveats": [
    "The EC 3.1.3.16 annotation is backed by direct experimental assay (ECO:0000269) from PubMed:37754565, not merely computational prediction.",
    "The PP2C motif recognition is a well-established bioinformatics approach, but distinguishing between two 3.1.3.x phosphatases (A vs B) is more demanding than cross-class discrimination; a model lacking knowledge of what 3.1.3.112 specifically is may struggle.",
    "The UniProt entry was first publicly released on 2025-02-05 (Swiss-Prot), so the experimental annotation post-dates some possible training cutoffs; however, the PP2C fold itself is a long-known protein family.",
    "All reviewer evidence is reviewer-only and was not available to the evaluated model; the model must rely on sequence motifs and general enzyme knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PP2C sequence motifs in the supplied sequence point specifically to EC 3.1.3.16. Options C (transferase) and D (lyase) are different reaction classes and can be excluded. Option A (3.1.3.112) is a phosphatase but of a different subfamily lacking the PP2C GD-motif architecture visible in the sequence. No two options are equally defensible given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0077",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A7U2MSD6 (PP2C2_ASPFN) from Aspergillus flavus carries EC 3.1.3.16 with direct experimental evidence (ECO:0000269, PubMed:37754565, a 2023 MBio paper reporting catalytic activity assays). The benchmark sequence matches the UniProt sequence exactly (SHA256 confirmed). The annotated catalytic reactions (dephosphorylation of O-phospho-L-seryl- and O-phospho-L-threonyl-[protein]) are consistent with EC 3.1.3.16 (protein serine/threonine phosphatase, PP2C family).",
    "evidence_ids": ["C1", "C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark PP2C-superfamily motifs: multiple 'GD' dipeptide motifs (e.g., 'AGDSRSVLG', 'CDGIWDC'), a DxT/S-like region, and conserved aspartate residues in the spatial arrangement characteristic of the metal-dependent PP2C phosphatase fold. PP2C is the canonical enzyme assigned EC 3.1.3.16. The other options represent clearly different reaction classes: 2.3.1.319 is an acyltransferase (transferase class, EC 2.x.x.x) and 4.2.1.18 is a hydro-lyase (EC 4.x.x.x), neither of which involves phosphoester hydrolysis. EC 3.1.3.112 is a phosphatase but of a different subfamily (a lipid/inositol phosphate phosphatase), lacking the PP2C GD-motif architecture. Recognizing the PP2C fold from these conserved sequence signatures and mapping it to the canonical EC 3.1.3.16 is a well-established bioinformatics inference.",
    "missing_item_specific_fact": "None critical. The PP2C fold motifs are visible in the supplied sequence. The exact distinction between EC 3.1.3.112 and 3.1.3.16 relies on knowing that 3.1.3.112 is not a PP2C-family enzyme, which is standard enzyme-taxonomy knowledge.",
    "reason": "A model with general protein-structure knowledge can identify the PP2C GD motifs and DxT/S region in the sequence, infer a metal-dependent serine/threonine phosphatase fold, and map this to EC 3.1.3.16. The transferase (C) and lyase (D) options are excluded by reaction-class reasoning. Distinguishing 3.1.3.112 from 3.1.3.16 requires knowing that 3.1.3.112 is not a PP2C, which is part of standard EC taxonomy knowledge rather than an obscure item-specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PP2C sequence motifs in the supplied sequence point specifically to EC 3.1.3.16. Options C (transferase) and D (lyase) are different reaction classes and can be excluded. Option A (3.1.3.112) is a phosphatase but of a different subfamily lacking the PP2C GD-motif architecture visible in the sequence. No two options are equally defensible given the sequence evidence."
  },
  "important_caveats": [
    "The EC 3.1.3.16 annotation is backed by direct experimental assay (ECO:0000269) from PubMed:37754565, not merely computational prediction.",
    "The PP2C motif recognition is a well-established bioinformatics approach, but distinguishing between two 3.1.3.x phosphatases (A vs B) is more demanding than cross-class discrimination; a model lacking knowledge of what 3.1.3.112 specifically is may struggle.",
    "The UniProt entry was first publicly released on 2025-02-05 (Swiss-Prot), so the experimental annotation post-dates some possible training cutoffs; however, the PP2C fold itself is a long-known protein family.",
    "All reviewer evidence is reviewer-only and was not available to the evaluated model; the model must rely on sequence motifs and general enzyme knowledge."
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

**Accession:** `A0A7U2MSD6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 15. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2MSD6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:55.167306+00:00.  

```json
"A0A7U2MSD6"
```

Source SHA-256: `9342418fd834736c043c972b8270772251d43ab2517d953f2052bd9c0a8a0cbb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2MSD6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:55.167306+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"37754565","source":"PubMed"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"37754565","source":"PubMed"}],"value":"Protein phosphatase 2C homolog 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PP2C-2"}]}}
```

Source SHA-256: `9342418fd834736c043c972b8270772251d43ab2517d953f2052bd9c0a8a0cbb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2MSD6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:55.167306+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"37754565","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:20630"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000269","id":"37754565","source":"PubMed"}],"name":"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20629"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:83421"}]}}
```

Source SHA-256: `9342418fd834736c043c972b8270772251d43ab2517d953f2052bd9c0a8a0cbb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2MSD6.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:55.167306+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"37754565","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:47005"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000305","id":"37754565","source":"PubMed"}],"name":"O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:47004"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:61977"}]}}
```

Source SHA-256: `9342418fd834736c043c972b8270772251d43ab2517d953f2052bd9c0a8a0cbb`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7U2MSD6.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:25:55.167306+00:00.  

```json
{"citation":{"authors":["Zhu Z.","Yang M.","Yang G.","Zhang B.","Cao X.","Yuan J.","Ge F.","Wang S."],"citationCrossReferences":[{"database":"PubMed","id":"37754565"},{"database":"DOI","id":"10.1128/mbio.00977-23"}],"citationType":"journal article","firstPage":"e0097723","id":"37754565","journal":"MBio","lastPage":"e0097723","publicationDate":"2023","title":"PP2C phosphatases Ptc1 and Ptc2 dephosphorylate PGK1 to regulate autophagy and aflatoxin synthesis in the pathogenic fungus Aspergillus flavus.","volume":"14"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","COFACTOR","SUBCELLULAR LOCATION","DISRUPTION PHENOTYPE","MUTAGENESIS OF ASP-71; ASP-148 AND ASP-240"]}
```

Source SHA-256: `9342418fd834736c043c972b8270772251d43ab2517d953f2052bd9c0a8a0cbb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2MSD6?format=txt&versions=15)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:25:59.751437+00:00.  

```text
ID   PP2C2_ASPFN             Reviewed;         435 AA.
AC   A0A7U2MSD6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   02-JUN-2021, sequence version 1.
DT   28-JAN-2026, entry version 15.
DE   RecName: Full=Protein phosphatase 2C homolog 2 {ECO:0000303|PubMed:37754565};
DE            Short=PP2C-2 {ECO:0000305};
DE            EC=3.1.3.16 {ECO:0000269|PubMed:37754565};
GN   Name=ptc2 {ECO:0000303|PubMed:37754565};
GN   ORFNames=F9C07_2102428 {ECO:0000312|EMBL:QRD88625.1};
OS   Aspergillus flavus (strain ATCC 200026 / FGSC A1120 / IAM 13836 / NRRL 3357
OS   / JCM 12722 / SRRC 167).
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=332952 {ECO:0000312|Proteomes:UP000596276};
```

Source SHA-256: `9599bc1c47b9179a3bc022cfe8fb6d87387d02041dea39b93328ccba23324c1e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2MSD6?format=txt&versions=15)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:25:59.751437+00:00.  

```text
DE   RecName: Full=Protein phosphatase 2C homolog 2 {ECO:0000303|PubMed:37754565};
DE            Short=PP2C-2 {ECO:0000305};
DE            EC=3.1.3.16 {ECO:0000269|PubMed:37754565};
```

Source SHA-256: `9599bc1c47b9179a3bc022cfe8fb6d87387d02041dea39b93328ccba23324c1e`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2MSD6?format=txt&versions=15)  
**Locator:** `lines 27-34`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:25:59.751437+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBCELLULAR LOCATION, DISRUPTION
RP   PHENOTYPE, AND MUTAGENESIS OF ASP-71; ASP-148 AND ASP-240.
RX   PubMed=37754565; DOI=10.1128/mbio.00977-23;
RA   Zhu Z., Yang M., Yang G., Zhang B., Cao X., Yuan J., Ge F., Wang S.;
RT   "PP2C phosphatases Ptc1 and Ptc2 dephosphorylate PGK1 to regulate autophagy
RT   and aflatoxin synthesis in the pathogenic fungus Aspergillus flavus.";
RL   MBio 14:e0097723-e0097723(2023).
```

Source SHA-256: `9599bc1c47b9179a3bc022cfe8fb6d87387d02041dea39b93328ccba23324c1e`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2MSD6?format=txt&versions=15)  
**Locator:** `lines 41-48`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:25:59.751437+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:20629, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15377, ChEBI:CHEBI:29999, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:83421; EC=3.1.3.16;
CC         Evidence={ECO:0000269|PubMed:37754565};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:20630;
CC         Evidence={ECO:0000269|PubMed:37754565};
```

Source SHA-256: `9599bc1c47b9179a3bc022cfe8fb6d87387d02041dea39b93328ccba23324c1e`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7U2MSD6?format=txt&versions=15)  
**Locator:** `lines 49-56`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 15 / 1.  
**Retrieved:** 2026-11-02T04:25:59.751437+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:47004, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15377, ChEBI:CHEBI:30013, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:61977; EC=3.1.3.16;
CC         Evidence={ECO:0000305|PubMed:37754565};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:47005;
CC         Evidence={ECO:0000305|PubMed:37754565};
```

Source SHA-256: `9599bc1c47b9179a3bc022cfe8fb6d87387d02041dea39b93328ccba23324c1e`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 77. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
