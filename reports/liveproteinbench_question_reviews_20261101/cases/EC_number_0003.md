# EC_number_0003

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 1.14.13.247

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTANPTSIHQRLDRRLSGFSLEQPFYTSPEVYALDLQHIFYKQWLYAVPVCQLAKAGSYTTLRVGAYEVVIVRSRDGEVRAFHNSCRHRGSLICKARQGQVAKLVCPYHQWTYELDGKLIWANDMGPDFDASKYGLKPVNLRNLDGLIYICLSDTPPDFQTFAQLARPYLEVHDLKDAKVAFTSTIIEKGNWKLVWENNRECYHCSSNHPALCRSFPLDPEVAGVQADGGVSKKLQAHFDRCEAAGTPAQFVLAGDGQYRLARMPLQEKALSYTMDGKAAVSRHLGRVAPPDAGTLLMFHYPSTWNHFLPDHSLTFRVMPISPTETEVTTTWLVHKDAVEGVDYDLKRLTEVWIATNDEDREIVETNQQGILSPAYVPGPYSPGQESGVMQFVDWYAASLERALAPRQVAAE

[Multiple Choices]
A. 1.14.13.238
B. 1.14.13.247
C. 2.7.11.24
D. 3.2.2.5
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

> The exact sequence matches the UniProt entry annotated as stachydrine N-demethylase, EC 1.14.13.247. The annotation cites experimental evidence for the enzyme function and catalytic reaction, supporting choice B.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may suggest an oxygenase, but they do not establish the specific substrate or reaction needed to distinguish the closely related oxygenase choices.


**Missing item-specific fact**

> The protein's demonstrated stachydrine/proline-betaine N-demethylation activity, or an equivalent protein-specific functional annotation, is not supplied in the question.


**Reason**

> Choosing the complete EC number requires the enzyme's specific catalytic activity. General sequence reasoning does not meaningfully resolve the distinction between options A and B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> From the supplied sequence and choices alone, the specific activity separating these two oxygenase EC numbers is not established; the reviewer-only evidence supports B.


### Important caveats

- The UniProt annotation is linked to experimental evidence and a cited study, but the primary paper was not independently reviewed here.
- The exact sequence match is established in reviewer-only evidence; the accession and annotation were not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may suggest an oxygenase, but they do not establish the specific substrate or reaction needed to distinguish the closely related oxygenase choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's demonstrated stachydrine/proline-betaine N-demethylation activity, or an equivalent protein-specific functional annotation, is not supplied in the question.",
    "reason": "Choosing the complete EC number requires the enzyme's specific catalytic activity. General sequence reasoning does not meaningfully resolve the distinction between options A and B."
  },
  "case_id": "EC_number_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as stachydrine N-demethylase, EC 1.14.13.247. The annotation cites experimental evidence for the enzyme function and catalytic reaction, supporting choice B."
  },
  "important_caveats": [
    "The UniProt annotation is linked to experimental evidence and a cited study, but the primary paper was not independently reviewed here.",
    "The exact sequence match is established in reviewer-only evidence; the accession and annotation were not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "From the supplied sequence and choices alone, the specific activity separating these two oxygenase EC numbers is not established; the reviewer-only evidence supports B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as stachydrine N-demethylase, EC 1.14.13.247. The annotation cites experimental evidence for the enzyme function and catalytic reaction, supporting choice B.",
    "evidence_ids": ["C1", "C4", "C5", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may suggest an oxygenase, but they do not establish the specific substrate or reaction needed to distinguish the closely related oxygenase choices.",
    "missing_item_specific_fact": "The protein's demonstrated stachydrine/proline-betaine N-demethylation activity, or an equivalent protein-specific functional annotation, is not supplied in the question.",
    "reason": "Choosing the complete EC number requires the enzyme's specific catalytic activity. General sequence reasoning does not meaningfully resolve the distinction between options A and B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "From the supplied sequence and choices alone, the specific activity separating these two oxygenase EC numbers is not established; the reviewer-only evidence supports B."
  },
  "important_caveats": [
    "The UniProt annotation is linked to experimental evidence and a cited study, but the primary paper was not independently reviewed here.",
    "The exact sequence match is established in reviewer-only evidence; the accession and annotation were not provided to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt Q92ZP9 (STC2_RHIME, Stachydrine N-demethylase) with exact SHA256 match. The EC number 1.14.13.247 is annotated with experimental evidence (ECO:0000269, PubMed:22224443, a 2012 JACS paper reporting 1.59 Å X-ray crystallography in complex with iron and &#91;2Fe-2S&#93; cluster). The catalytic reaction (L-proline betaine + NAD(P)H + O2 + H+ → N-methyl-L-proline + formaldehyde + NAD(P)+ + H2O) is experimentally validated. The author key B is fully supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains Rieske-type &#91;2Fe-2S&#93; cluster motifs (e.g., CPYH and CYHCSSNHPALCRSF patterns) and NAD(P)H-binding architecture, which confidently places the enzyme in EC class 1.14.13 (oxidoreductases acting on paired donors, NADH/NADPH, incorporation of one oxygen atom). This reasoning eliminates C (2.7.11.24, a protein kinase) and D (3.2.2.5, a glycosylase) as they belong to entirely different EC top-level classes (transferase, hydrolase). However, options A (1.14.13.238) and B (1.14.13.247) share the same 3-digit class and differ only in the 4th digit, which encodes the exact substrate (stachydrine/L-proline betaine vs. the substrate of EC 1.14.13.238). Both would share Rieske-type motifs, mononuclear iron coordination, and NAD(P)H cofactor usage. No general biological reasoning from the sequence alone distinguishes which specific quaternary ammonium substrate this enzyme demethylates.


**Missing item-specific fact**

> The specific substrate identity of this enzyme (stachydrine/L-proline betaine for EC 1.14.13.247) versus the substrate of EC 1.14.13.238. The 4th-digit EC assignment depends on the experimentally determined substrate specificity, which is not inferable from sequence motifs shared across the 1.14.13 family.


**Reason**

> While the broad EC class (1.14.13) is reasoning-accessible from Rieske-type motifs and oxidoreductase architecture, the critical distinction between the two viable options (A vs B) hinges on the exact 4th-digit substrate specificity. This is an item-specific annotation derived from experimental substrate assays (PubMed:22224443), not from general sequence-to-function inference. A model must either memorize this protein's database entry or possess a trained predictor that has internalized the sequence-substrate mapping.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Options A (1.14.13.238) and B (1.14.13.247) are both in the same EC 1.14.13 family (Rieske-type NAD(P)H-dependent monooxygenases/demethylases). Without the specific substrate annotation, both are plausible for a sequence exhibiting Rieske-type motifs and NAD(P)H-binding features. The question's wording ('most accurate EC number') does not provide substrate context or active-site specificity information that would allow reasoning to favor one 4th digit over the other.


### Important caveats

- The EC 1.14.13.247 annotation is backed by X-ray crystallographic and spectroscopic evidence (ECO:0000269), making it a high-confidence experimental assignment rather than a computational prediction.
- The identity of EC 1.14.13.238 was not independently verified in the supplied evidence; its substrate specificity relative to 1.14.13.247 was not detailed in the excerpts.
- The sequence-to-EC-number task at the 4-digit level for closely related enzymes in the same 3-digit class is inherently a database-lookup problem rather than a reasoning problem, as the 4th digit encodes substrate identity not encoded in conserved catalytic motifs.
- Distractors C and D are effectively eliminated by basic EC-class reasoning (kinase vs. hydrolase vs. oxidoreductase), reducing the effective discrimination to a binary A-vs-B choice that requires substrate-specific knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains Rieske-type [2Fe-2S] cluster motifs (e.g., CPYH and CYHCSSNHPALCRSF patterns) and NAD(P)H-binding architecture, which confidently places the enzyme in EC class 1.14.13 (oxidoreductases acting on paired donors, NADH/NADPH, incorporation of one oxygen atom). This reasoning eliminates C (2.7.11.24, a protein kinase) and D (3.2.2.5, a glycosylase) as they belong to entirely different EC top-level classes (transferase, hydrolase). However, options A (1.14.13.238) and B (1.14.13.247) share the same 3-digit class and differ only in the 4th digit, which encodes the exact substrate (stachydrine/L-proline betaine vs. the substrate of EC 1.14.13.238). Both would share Rieske-type motifs, mononuclear iron coordination, and NAD(P)H cofactor usage. No general biological reasoning from the sequence alone distinguishes which specific quaternary ammonium substrate this enzyme demethylates.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity of this enzyme (stachydrine/L-proline betaine for EC 1.14.13.247) versus the substrate of EC 1.14.13.238. The 4th-digit EC assignment depends on the experimentally determined substrate specificity, which is not inferable from sequence motifs shared across the 1.14.13 family.",
    "reason": "While the broad EC class (1.14.13) is reasoning-accessible from Rieske-type motifs and oxidoreductase architecture, the critical distinction between the two viable options (A vs B) hinges on the exact 4th-digit substrate specificity. This is an item-specific annotation derived from experimental substrate assays (PubMed:22224443), not from general sequence-to-function inference. A model must either memorize this protein's database entry or possess a trained predictor that has internalized the sequence-substrate mapping."
  },
  "case_id": "EC_number_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q92ZP9 (STC2_RHIME, Stachydrine N-demethylase) with exact SHA256 match. The EC number 1.14.13.247 is annotated with experimental evidence (ECO:0000269, PubMed:22224443, a 2012 JACS paper reporting 1.59 Å X-ray crystallography in complex with iron and [2Fe-2S] cluster). The catalytic reaction (L-proline betaine + NAD(P)H + O2 + H+ → N-methyl-L-proline + formaldehyde + NAD(P)+ + H2O) is experimentally validated. The author key B is fully supported."
  },
  "important_caveats": [
    "The EC 1.14.13.247 annotation is backed by X-ray crystallographic and spectroscopic evidence (ECO:0000269), making it a high-confidence experimental assignment rather than a computational prediction.",
    "The identity of EC 1.14.13.238 was not independently verified in the supplied evidence; its substrate specificity relative to 1.14.13.247 was not detailed in the excerpts.",
    "The sequence-to-EC-number task at the 4-digit level for closely related enzymes in the same 3-digit class is inherently a database-lookup problem rather than a reasoning problem, as the 4th digit encodes substrate identity not encoded in conserved catalytic motifs.",
    "Distractors C and D are effectively eliminated by basic EC-class reasoning (kinase vs. hydrolase vs. oxidoreductase), reducing the effective discrimination to a binary A-vs-B choice that requires substrate-specific knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Options A (1.14.13.238) and B (1.14.13.247) are both in the same EC 1.14.13 family (Rieske-type NAD(P)H-dependent monooxygenases/demethylases). Without the specific substrate annotation, both are plausible for a sequence exhibiting Rieske-type motifs and NAD(P)H-binding features. The question's wording ('most accurate EC number') does not provide substrate context or active-site specificity information that would allow reasoning to favor one 4th digit over the other."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt Q92ZP9 (STC2_RHIME, Stachydrine N-demethylase) with exact SHA256 match. The EC number 1.14.13.247 is annotated with experimental evidence (ECO:0000269, PubMed:22224443, a 2012 JACS paper reporting 1.59 Å X-ray crystallography in complex with iron and [2Fe-2S] cluster). The catalytic reaction (L-proline betaine + NAD(P)H + O2 + H+ → N-methyl-L-proline + formaldehyde + NAD(P)+ + H2O) is experimentally validated. The author key B is fully supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains Rieske-type [2Fe-2S] cluster motifs (e.g., CPYH and CYHCSSNHPALCRSF patterns) and NAD(P)H-binding architecture, which confidently places the enzyme in EC class 1.14.13 (oxidoreductases acting on paired donors, NADH/NADPH, incorporation of one oxygen atom). This reasoning eliminates C (2.7.11.24, a protein kinase) and D (3.2.2.5, a glycosylase) as they belong to entirely different EC top-level classes (transferase, hydrolase). However, options A (1.14.13.238) and B (1.14.13.247) share the same 3-digit class and differ only in the 4th digit, which encodes the exact substrate (stachydrine/L-proline betaine vs. the substrate of EC 1.14.13.238). Both would share Rieske-type motifs, mononuclear iron coordination, and NAD(P)H cofactor usage. No general biological reasoning from the sequence alone distinguishes which specific quaternary ammonium substrate this enzyme demethylates.",
    "missing_item_specific_fact": "The specific substrate identity of this enzyme (stachydrine/L-proline betaine for EC 1.14.13.247) versus the substrate of EC 1.14.13.238. The 4th-digit EC assignment depends on the experimentally determined substrate specificity, which is not inferable from sequence motifs shared across the 1.14.13 family.",
    "reason": "While the broad EC class (1.14.13) is reasoning-accessible from Rieske-type motifs and oxidoreductase architecture, the critical distinction between the two viable options (A vs B) hinges on the exact 4th-digit substrate specificity. This is an item-specific annotation derived from experimental substrate assays (PubMed:22224443), not from general sequence-to-function inference. A model must either memorize this protein's database entry or possess a trained predictor that has internalized the sequence-substrate mapping."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Options A (1.14.13.238) and B (1.14.13.247) are both in the same EC 1.14.13 family (Rieske-type NAD(P)H-dependent monooxygenases/demethylases). Without the specific substrate annotation, both are plausible for a sequence exhibiting Rieske-type motifs and NAD(P)H-binding features. The question's wording ('most accurate EC number') does not provide substrate context or active-site specificity information that would allow reasoning to favor one 4th digit over the other."
  },
  "important_caveats": [
    "The EC 1.14.13.247 annotation is backed by X-ray crystallographic and spectroscopic evidence (ECO:0000269), making it a high-confidence experimental assignment rather than a computational prediction.",
    "The identity of EC 1.14.13.238 was not independently verified in the supplied evidence; its substrate specificity relative to 1.14.13.247 was not detailed in the excerpts.",
    "The sequence-to-EC-number task at the 4-digit level for closely related enzymes in the same 3-digit class is inherently a database-lookup problem rather than a reasoning problem, as the 4th digit encodes substrate identity not encoded in conserved catalytic motifs.",
    "Distractors C and D are effectively eliminated by basic EC-class reasoning (kinase vs. hydrolase vs. oxidoreductase), reducing the effective discrimination to a binary A-vs-B choice that requires substrate-specific knowledge."
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

**Accession:** `Q92ZP9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 138. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:35.950168+00:00.  

```json
"Q92ZP9"
```

Source SHA-256: `276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:35.950168+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"22224443","source":"PubMed"}],"value":"Rieske-type mononuclear non-heme enzyme"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"22224443","source":"PubMed"}],"value":"1.14.13.247"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Stachydrine N-demethylase"}}}
```

Source SHA-256: `276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:35.950168+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.14.13.247","evidences":[{"evidenceCode":"ECO:0000269","id":"22224443","source":"PubMed"}],"name":"L-proline betaine + NADH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NAD(+) + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:61616"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:16842"},{"database":"ChEBI","id":"CHEBI:35280"},{"database":"ChEBI","id":"CHEBI:57540"},{"database":"ChEBI","id":"CHEBI:57945"},{"database":"ChEBI","id":"CHEBI:133743"}]}}
```

Source SHA-256: `276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:35.950168+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.14.13.247","evidences":[{"evidenceCode":"ECO:0000269","id":"22224443","source":"PubMed"}],"name":"L-proline betaine + NADPH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NADP(+) + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:19357"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:15379"},{"database":"ChEBI","id":"CHEBI:16842"},{"database":"ChEBI","id":"CHEBI:35280"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:133743"}]}}
```

Source SHA-256: `276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:32:35.950168+00:00.  

```json
{"citation":{"authors":["Daughtry K.D.","Xiao Y.","Stoner-Ma D.","Cho E.","Orville A.M.","Liu P.","Allen K.N."],"citationCrossReferences":[{"database":"PubMed","id":"22224443"},{"database":"DOI","id":"10.1021/ja2111898"}],"citationType":"journal article","firstPage":"2823","id":"22224443","journal":"J. Am. Chem. Soc.","lastPage":"2834","publicationDate":"2012","title":"Quaternary ammonium oxidative demethylation: X-ray crystallographic, resonance Raman, and UV-visible spectroscopic analysis of a Rieske-type demethylase.","volume":"134"},"evidences":[{"evidenceCode":"ECO:0007744","id":"3VCA","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"3VCP","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"1021"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.59 ANGSTROMS) IN COMPLEX WITH IRON AND IRON-SULFUR (2FE-2S)","FUNCTION","CATALYTIC ACTIVITY","REACTION MECHANISM","COFACTOR","SUBUNIT"]}
```

Source SHA-256: `276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 138 / 1.  
**Retrieved:** 2026-11-02T04:32:39.981731+00:00.  

```text
DE   RecName: Full=Stachydrine N-demethylase {ECO:0000305};
DE            EC=1.14.13.247 {ECO:0000269|PubMed:22224443};
DE   AltName: Full=Rieske-type mononuclear non-heme enzyme {ECO:0000303|PubMed:22224443};
```

Source SHA-256: `654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)  
**Locator:** `lines 56-67`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 138 / 1.  
**Retrieved:** 2026-11-02T04:32:39.981731+00:00.  

```text
RN   [4] {ECO:0007744|PDB:3VCA, ECO:0007744|PDB:3VCP}
RP   X-RAY CRYSTALLOGRAPHY (1.59 ANGSTROMS) IN COMPLEX WITH IRON AND IRON-SULFUR
RP   (2FE-2S), FUNCTION, CATALYTIC ACTIVITY, REACTION MECHANISM, COFACTOR, AND
RP   SUBUNIT.
RC   STRAIN=1021;
RX   PubMed=22224443; DOI=10.1021/ja2111898;
RA   Daughtry K.D., Xiao Y., Stoner-Ma D., Cho E., Orville A.M., Liu P.,
RA   Allen K.N.;
RT   "Quaternary ammonium oxidative demethylation: X-ray crystallographic,
RT   resonance Raman, and UV-visible spectroscopic analysis of a Rieske-type
RT   demethylase.";
RL   J. Am. Chem. Soc. 134:2823-2834(2012).
```

Source SHA-256: `654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)  
**Locator:** `lines 97-103`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 138 / 1.  
**Retrieved:** 2026-11-02T04:32:39.981731+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-proline betaine + NADH + O2 + H(+) = N-methyl-L-proline +
CC         formaldehyde + NAD(+) + H2O; Xref=Rhea:RHEA:61616, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:15379, ChEBI:CHEBI:16842,
CC         ChEBI:CHEBI:35280, ChEBI:CHEBI:57540, ChEBI:CHEBI:57945,
CC         ChEBI:CHEBI:133743; EC=1.14.13.247;
CC         Evidence={ECO:0000269|PubMed:22224443};
```

Source SHA-256: `654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b`.

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)  
**Locator:** `lines 104-110`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 138 / 1.  
**Retrieved:** 2026-11-02T04:32:39.981731+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-proline betaine + NADPH + O2 + H(+) = N-methyl-L-proline +
CC         formaldehyde + NADP(+) + H2O; Xref=Rhea:RHEA:19357,
CC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,
CC         ChEBI:CHEBI:16842, ChEBI:CHEBI:35280, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58349, ChEBI:CHEBI:133743; EC=1.14.13.247;
CC         Evidence={ECO:0000269|PubMed:22224443};
```

Source SHA-256: `654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 3. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
