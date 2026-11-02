# EC_number_0155

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **D** — 3.1.3.16

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGVEEADKLKQLGNAAFSERKWHLAIDMYTKAIELTKTPTLFCNRALAELRAELPGAALADADAALGIEPTFAKAYYHKASAYLSLGKHKQALTNYKKVVDLAPQNSDAQAKVEFCKKEIRRINFENAIMTPDEAPLSQTIKLGSVRADYDGPRIENETVTVEFVEAMKEHFRLEKLIDRHDVIFILLEVQKILKKCPNFVSINVPVGEEITVCGDTHGQYYDLLNIFKLNGNPLETNRYLFNGDFVDRGSYSFENIMTLFAYKVLYPDHFFLSRGNHEGVSMNRMYGFEGEVTQKYNSEMFRLFTEVFNSLPIGHIINNEVFVVHGGLYSSDKVTLDDLQHPNRFRDIPESGLICESLWSDPQPMPGRAPSKRGVSCLSFGPDVTETFLNNNNLKLLVRSHEVKDEGYEIEHGGKCITVFSAPNYCDQMGNKGAFIRFTGGDMKPRFTTFTHVPHPGKRPMHYATGFGLF

[Multiple Choices]
A. 3.1.3.112
B. 5.3.1.8
C. 2.7.7.80
D. 3.1.3.16
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

> The exact sequence matches UniProt entry Q388N2, whose archived annotation assigns EC 3.1.3.16 and describes dephosphorylation of phosphoserine- and phosphothreonine-containing proteins, citing PubMed 11290414. This supports choice D, though the cited primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support inference of a phosphatase, but the exact EC requires knowing its substrate/reaction specificity; the supplied sequence and prompt do not establish that specificity.


**Missing item-specific fact**

> The protein-specific catalytic annotation or experimental characterization identifying this enzyme as a protein serine/threonine phosphatase (EC 3.1.3.16).


**Reason**

> Choosing the complete EC number depends on an item-specific function annotation or characterization absent from the input, rather than a sufficiently discriminating general biological argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The reviewer-only annotation supports D, and the listed alternatives correspond to different EC classifications; no evidence supplied supports another option for this sequence.


### Important caveats

- The current and archived UniProt records match the supplied sequence, but the author’s exact source snapshot is unknown.
- The UniProt functional annotation cites a publication; that primary evidence was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support inference of a phosphatase, but the exact EC requires knowing its substrate/reaction specificity; the supplied sequence and prompt do not establish that specificity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental characterization identifying this enzyme as a protein serine/threonine phosphatase (EC 3.1.3.16).",
    "reason": "Choosing the complete EC number depends on an item-specific function annotation or characterization absent from the input, rather than a sufficiently discriminating general biological argument."
  },
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry Q388N2, whose archived annotation assigns EC 3.1.3.16 and describes dephosphorylation of phosphoserine- and phosphothreonine-containing proteins, citing PubMed 11290414. This supports choice D, though the cited primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The current and archived UniProt records match the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The UniProt functional annotation cites a publication; that primary evidence was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports D, and the listed alternatives correspond to different EC classifications; no evidence supplied supports another option for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry Q388N2, whose archived annotation assigns EC 3.1.3.16 and describes dephosphorylation of phosphoserine- and phosphothreonine-containing proteins, citing PubMed 11290414. This supports choice D, though the cited primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support inference of a phosphatase, but the exact EC requires knowing its substrate/reaction specificity; the supplied sequence and prompt do not establish that specificity.",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental characterization identifying this enzyme as a protein serine/threonine phosphatase (EC 3.1.3.16).",
    "reason": "Choosing the complete EC number depends on an item-specific function annotation or characterization absent from the input, rather than a sufficiently discriminating general biological argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The reviewer-only annotation supports D, and the listed alternatives correspond to different EC classifications; no evidence supplied supports another option for this sequence."
  },
  "important_caveats": [
    "The current and archived UniProt records match the supplied sequence, but the author’s exact source snapshot is unknown.",
    "The UniProt functional annotation cites a publication; that primary evidence was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q388N2 (PPP5_TRYB2, Trypanosoma brucei brucei) with identical SHA-256. The entry is annotated as Serine/threonine-protein phosphatase T with EC=3.1.3.16, supported by catalytic activity reactions (O-phospho-L-seryl-&#91;protein&#93; + H2O = L-seryl-&#91;protein&#93; + phosphate and the threonyl equivalent). The evidence code is ECO:0000305 (curator inference) backed by PubMed:11290414 (Chaudhuri, 2001, Gene 266:1-13), a cloning and characterization paper. The annotation is a curator-assigned EC number based on sequence similarity to the PP5 family with experimental characterization in the reference, not a direct kinetic measurement, but it is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical PPP-family phosphatase catalytic motifs: GDTHGQ (GD…HG motif), EHGGKC (HGG motif), NGDFVDRGS (GDF motif), and HGGLYSSD. These are well-known, textbook hallmarks of the PPP superfamily of serine/threonine protein phosphatases (PP1, PP2A, PP5, PP7, etc.). Recognizing these motifs identifies the enzyme as a PPP-family protein phosphatase, which is classified under EC 3.1.3.16 (protein serine/threonine phosphatase). This eliminates B (5.3.1.8, an isomerase), C (2.7.7.80, a nucleotidyltransferase), and A (3.1.3.112, a lipid phosphatase acting on phosphatidylinositol phosphates, which lacks PPP-family motifs and belongs to a different structural class). The distinction between protein phosphatases (PPP motifs) and lipid phosphatases (e.g., PTEN/SH2-domain-containing phosphatases) is general biochemical knowledge.


**Missing item-specific fact**

> None critical. The PPP-family motifs are directly observable in the supplied sequence, and their association with EC 3.1.3.16 is standard biochemical knowledge.


**Reason**

> A model with knowledge of phosphatase superfamily architecture can identify the GD, HGG, and GDF motifs in the sequence and conclude the protein is a PPP-family serine/threonine protein phosphatase (EC 3.1.3.16), distinguishing it from the lipid phosphatase (3.1.3.112), isomerase (5.3.1.8), and transferase (2.7.7.80) options. This is general domain-knowledge reasoning, not item-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PPP-family motifs unambiguously indicate a serine/threonine protein phosphatase. Options B and C belong to entirely different EC classes (isomerase, transferase). Option A (3.1.3.112) is a lipid phosphatase with a completely different fold and no PPP motifs. Only D is consistent with the observed catalytic motifs.


### Important caveats

- The UniProt EC assignment uses evidence code ECO:0000305 (curator inference from sequence similarity to characterized PP5 homologs), supported by a 2001 cloning/characterization paper. It is not a direct experimental kinetic assay result, but the PPP-family assignment is robust.
- The reviewer-only evidence confirms the sequence-to-entry match (SHA-256 identical) but was not available to the evaluated model.
- The model must recognize PPP-family motifs (GD, HGG, GDF) from the raw sequence without database access; this is feasible for a model trained on protein biochemistry but represents a non-trivial recognition task for less specialized models.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical PPP-family phosphatase catalytic motifs: GDTHGQ (GD…HG motif), EHGGKC (HGG motif), NGDFVDRGS (GDF motif), and HGGLYSSD. These are well-known, textbook hallmarks of the PPP superfamily of serine/threonine protein phosphatases (PP1, PP2A, PP5, PP7, etc.). Recognizing these motifs identifies the enzyme as a PPP-family protein phosphatase, which is classified under EC 3.1.3.16 (protein serine/threonine phosphatase). This eliminates B (5.3.1.8, an isomerase), C (2.7.7.80, a nucleotidyltransferase), and A (3.1.3.112, a lipid phosphatase acting on phosphatidylinositol phosphates, which lacks PPP-family motifs and belongs to a different structural class). The distinction between protein phosphatases (PPP motifs) and lipid phosphatases (e.g., PTEN/SH2-domain-containing phosphatases) is general biochemical knowledge.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The PPP-family motifs are directly observable in the supplied sequence, and their association with EC 3.1.3.16 is standard biochemical knowledge.",
    "reason": "A model with knowledge of phosphatase superfamily architecture can identify the GD, HGG, and GDF motifs in the sequence and conclude the protein is a PPP-family serine/threonine protein phosphatase (EC 3.1.3.16), distinguishing it from the lipid phosphatase (3.1.3.112), isomerase (5.3.1.8), and transferase (2.7.7.80) options. This is general domain-knowledge reasoning, not item-specific lookup."
  },
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q388N2 (PPP5_TRYB2, Trypanosoma brucei brucei) with identical SHA-256. The entry is annotated as Serine/threonine-protein phosphatase T with EC=3.1.3.16, supported by catalytic activity reactions (O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate and the threonyl equivalent). The evidence code is ECO:0000305 (curator inference) backed by PubMed:11290414 (Chaudhuri, 2001, Gene 266:1-13), a cloning and characterization paper. The annotation is a curator-assigned EC number based on sequence similarity to the PP5 family with experimental characterization in the reference, not a direct kinetic measurement, but it is well-supported."
  },
  "important_caveats": [
    "The UniProt EC assignment uses evidence code ECO:0000305 (curator inference from sequence similarity to characterized PP5 homologs), supported by a 2001 cloning/characterization paper. It is not a direct experimental kinetic assay result, but the PPP-family assignment is robust.",
    "The reviewer-only evidence confirms the sequence-to-entry match (SHA-256 identical) but was not available to the evaluated model.",
    "The model must recognize PPP-family motifs (GD, HGG, GDF) from the raw sequence without database access; this is feasible for a model trained on protein biochemistry but represents a non-trivial recognition task for less specialized models."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PPP-family motifs unambiguously indicate a serine/threonine protein phosphatase. Options B and C belong to entirely different EC classes (isomerase, transferase). Option A (3.1.3.112) is a lipid phosphatase with a completely different fold and no PPP motifs. Only D is consistent with the observed catalytic motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0155",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q388N2 (PPP5_TRYB2, Trypanosoma brucei brucei) with identical SHA-256. The entry is annotated as Serine/threonine-protein phosphatase T with EC=3.1.3.16, supported by catalytic activity reactions (O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate and the threonyl equivalent). The evidence code is ECO:0000305 (curator inference) backed by PubMed:11290414 (Chaudhuri, 2001, Gene 266:1-13), a cloning and characterization paper. The annotation is a curator-assigned EC number based on sequence similarity to the PP5 family with experimental characterization in the reference, not a direct kinetic measurement, but it is well-supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical PPP-family phosphatase catalytic motifs: GDTHGQ (GD…HG motif), EHGGKC (HGG motif), NGDFVDRGS (GDF motif), and HGGLYSSD. These are well-known, textbook hallmarks of the PPP superfamily of serine/threonine protein phosphatases (PP1, PP2A, PP5, PP7, etc.). Recognizing these motifs identifies the enzyme as a PPP-family protein phosphatase, which is classified under EC 3.1.3.16 (protein serine/threonine phosphatase). This eliminates B (5.3.1.8, an isomerase), C (2.7.7.80, a nucleotidyltransferase), and A (3.1.3.112, a lipid phosphatase acting on phosphatidylinositol phosphates, which lacks PPP-family motifs and belongs to a different structural class). The distinction between protein phosphatases (PPP motifs) and lipid phosphatases (e.g., PTEN/SH2-domain-containing phosphatases) is general biochemical knowledge.",
    "missing_item_specific_fact": "None critical. The PPP-family motifs are directly observable in the supplied sequence, and their association with EC 3.1.3.16 is standard biochemical knowledge.",
    "reason": "A model with knowledge of phosphatase superfamily architecture can identify the GD, HGG, and GDF motifs in the sequence and conclude the protein is a PPP-family serine/threonine protein phosphatase (EC 3.1.3.16), distinguishing it from the lipid phosphatase (3.1.3.112), isomerase (5.3.1.8), and transferase (2.7.7.80) options. This is general domain-knowledge reasoning, not item-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PPP-family motifs unambiguously indicate a serine/threonine protein phosphatase. Options B and C belong to entirely different EC classes (isomerase, transferase). Option A (3.1.3.112) is a lipid phosphatase with a completely different fold and no PPP motifs. Only D is consistent with the observed catalytic motifs."
  },
  "important_caveats": [
    "The UniProt EC assignment uses evidence code ECO:0000305 (curator inference from sequence similarity to characterized PP5 homologs), supported by a 2001 cloning/characterization paper. It is not a direct experimental kinetic assay result, but the PPP-family assignment is robust.",
    "The reviewer-only evidence confirms the sequence-to-entry match (SHA-256 identical) but was not available to the evaluated model.",
    "The model must recognize PPP-family motifs (GD, HGG, GDF) from the raw sequence without database access; this is feasible for a model trained on protein biochemistry but represents a non-trivial recognition task for less specialized models."
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

**Accession:** `Q388N2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 114. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
"Q388N2"
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"11290414","source":"PubMed"}],"value":"TbPP5"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"11290414","source":"PubMed"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Serine/threonine-protein phosphatase T"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"PPT"}]}}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"11290414","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:20630"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000305","id":"11290414","source":"PubMed"}],"name":"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20629"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:83421"}]}}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"11290414","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:47005"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000305","id":"11290414","source":"PubMed"}],"name":"O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:47004"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:61977"}]}}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q388N2.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:44.659218+00:00.  

```json
{"citation":{"authors":["Chaudhuri M."],"citationCrossReferences":[{"database":"PubMed","id":"11290414"},{"database":"DOI","id":"10.1016/s0378-1119(01)00367-5"}],"citationType":"journal article","firstPage":"1","id":"11290414","journal":"Gene","lastPage":"13","publicationDate":"2001","title":"Cloning and characterization of a novel serine/threonine protein phosphatase type 5 from Trypanosoma brucei.","volume":"266"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"11290414","source":"PubMed"}],"type":"STRAIN","value":"LUMP 1026"}],"referenceNumber":2,"referencePositions":["CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `8d8adced98584260feb2d973bbdc1cfedd05c91c22d7759b69dbc8e335985936`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:30:47.011986+00:00.  

```text
DE   RecName: Full=Serine/threonine-protein phosphatase T {ECO:0000305};
DE            Short=PPT {ECO:0000305};
DE            EC=3.1.3.16 {ECO:0000305|PubMed:11290414};
DE   AltName: Full=TbPP5 {ECO:0000303|PubMed:11290414};
```

Source SHA-256: `ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)  
**Locator:** `lines 51-58`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:30:47.011986+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:20629, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15377, ChEBI:CHEBI:29999, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:83421; EC=3.1.3.16;
CC         Evidence={ECO:0000305|PubMed:11290414};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:20630;
CC         Evidence={ECO:0000305|PubMed:11290414};
```

Source SHA-256: `ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q388N2?format=txt&versions=114)  
**Locator:** `lines 59-66`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 114 / 1.  
**Retrieved:** 2026-11-02T04:30:47.011986+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:47004, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15377, ChEBI:CHEBI:30013, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:61977; EC=3.1.3.16;
CC         Evidence={ECO:0000305|PubMed:11290414};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:47005;
CC         Evidence={ECO:0000305|PubMed:11290414};
```

Source SHA-256: `ceefd57fac247af4269990ea2789068697ac2e8d9452900d9533c01a71737c9f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 155. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
