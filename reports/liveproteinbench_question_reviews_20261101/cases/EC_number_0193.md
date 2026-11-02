# EC_number_0193

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.1.3.16

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | reasoning-supported | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MASSDLEAATALKVQGNKAFGQHEWPTAVDFYTQAIAKYDREPSFFSNRAQAHIKLEAYGFAIADATKALELDPAYTKAYWRRALANTAILNYKDALRDFKVVAKREPNNRDAKVKLADCEKLVRRMEFEKAIEVGDPPSAFEDLDIDAIAVDDSYDGVRLEKEMTQEFIDDMIERFKNGKKIHRKYAFQIVKAVKDIVYAEPTMVEIGVDQGTKLTVCGDTHGQFFDLLEIFRLNGYPSEKHAYLFNGDFVDRGSWSTEIALLLYAYKWLRPNGIFLNRGNHETDDMNKVYGFEGECKAKYNERMFKVFSESFSALPLATLIGNKYLVLHGGLFSDDNTSLDDIRKLDRHNQRQPGQQGLMMEMLWTDPQTEPGRGPSKRGVGLQFGPDVTKRFCEKNGLEAIIRSHEVRMEGYEVEHDGRCITVFSAPKYCDTTENKGAFINVGPELKLDFQVFEAVPHPDIKPMAYAQNSIMSMM

[Multiple Choices]
A. 3.1.3.16
B. 3.1.3.112
C. 2.7.13.3
D. 1.5.1.32
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

> The exact supplied sequence matches the UniProt record for a serine/threonine-protein phosphatase annotated with EC 3.1.3.16. Its catalytic-activity annotations assign that EC to dephosphorylation of protein-bound serine and threonine residues, citing PubMed 17475320. This supports A, though the cited paper was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal TPR-rich region and a C-terminal catalytic domain characteristic of PP5-like serine/threonine protein phosphatases. That architecture supports protein phosphatase activity and distinguishes A from the kinase and reductase choices; the phosphatase-family context also favors A over the other listed phosphatase EC.


**Missing item-specific fact**

> No additional item-specific fact is essential for a defensible family-level inference from the sequence, although exact EC assignment is more secure with a family annotation or experimental characterization.


**Reason**

> The sequence provides meaningful evidence for a PP5-like protein phosphatase rather than requiring recognition of the exact sequence or its database record. The reviewer-only annotation confirms the key but is not treated as input available to the original model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence's phosphatase architecture supports A; the other options describe enzyme activities not indicated by that architecture.


### Important caveats

- The reviewer-only record matches the supplied sequence exactly.
- The supporting EC annotation cites a PubMed source, but the primary paper was not independently retrieved and validated here.
- The author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal TPR-rich region and a C-terminal catalytic domain characteristic of PP5-like serine/threonine protein phosphatases. That architecture supports protein phosphatase activity and distinguishes A from the kinase and reductase choices; the phosphatase-family context also favors A over the other listed phosphatase EC.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "No additional item-specific fact is essential for a defensible family-level inference from the sequence, although exact EC assignment is more secure with a family annotation or experimental characterization.",
    "reason": "The sequence provides meaningful evidence for a PP5-like protein phosphatase rather than requiring recognition of the exact sequence or its database record. The reviewer-only annotation confirms the key but is not treated as input available to the original model."
  },
  "case_id": "EC_number_0193",
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
    "reason": "The exact supplied sequence matches the UniProt record for a serine/threonine-protein phosphatase annotated with EC 3.1.3.16. Its catalytic-activity annotations assign that EC to dephosphorylation of protein-bound serine and threonine residues, citing PubMed 17475320. This supports A, though the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence exactly.",
    "The supporting EC annotation cites a PubMed source, but the primary paper was not independently retrieved and validated here.",
    "The author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence's phosphatase architecture supports A; the other options describe enzyme activities not indicated by that architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0193",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt record for a serine/threonine-protein phosphatase annotated with EC 3.1.3.16. Its catalytic-activity annotations assign that EC to dephosphorylation of protein-bound serine and threonine residues, citing PubMed 17475320. This supports A, though the cited paper was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal TPR-rich region and a C-terminal catalytic domain characteristic of PP5-like serine/threonine protein phosphatases. That architecture supports protein phosphatase activity and distinguishes A from the kinase and reductase choices; the phosphatase-family context also favors A over the other listed phosphatase EC.",
    "missing_item_specific_fact": "No additional item-specific fact is essential for a defensible family-level inference from the sequence, although exact EC assignment is more secure with a family annotation or experimental characterization.",
    "reason": "The sequence provides meaningful evidence for a PP5-like protein phosphatase rather than requiring recognition of the exact sequence or its database record. The reviewer-only annotation confirms the key but is not treated as input available to the original model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence's phosphatase architecture supports A; the other options describe enzyme activities not indicated by that architecture."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence exactly.",
    "The supporting EC annotation cites a PubMed source, but the primary paper was not independently retrieved and validated here.",
    "The author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q2U919 (PPP5_ASPOR, sequence matched exactly at 478 AA) is annotated as Serine/threonine-protein phosphatase T with EC 3.1.3.16. The catalytic activities (dephosphorylation of O-phospho-L-seryl-&#91;protein&#93; and O-phospho-L-threonyl-&#91;protein&#93;) are supported by experimental evidence (ECO:0000305, PubMed:17475320, Feng et al. 2007, which demonstrated dephosphorylation activity). The EC assignment is backed by both current (C4, C5, C6) and historical (H2, H4, H5) UniProt records.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5), [C7](#evidence-c7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark PPP-family phosphatase catalytic motifs: 'GDTHGQ' (metal-binding/active-site region) and 'GDFVDRGSW' (conserved PPP catalytic domain signature), along with the characteristic His-Asp-His-Asp metal coordination residues. These motifs are diagnostic of serine/threonine protein phosphatases of the PPP superfamily (PP1, PP2A, PP2B, PP4, PP5, PP6), which are classified under EC 3.1.3.16. Options C (2.7.13.3, a transferase/kinase) and D (1.5.1.32, an oxidoreductase) are eliminated by recognizing the sequence as a hydrolase with phosphatase motifs rather than a kinase or redox enzyme. The PPP-family catalytic architecture is inconsistent with the mechanistic requirements of EC 3.1.3.112 (a different phosphatase class or substrate specificity), further supporting 3.1.3.16.


**Missing item-specific fact**

> The exact identity and substrate specificity of EC 3.1.3.112 would need to be known to definitively exclude it, but the PPP-family motifs are well-established general knowledge sufficient to assign EC 3.1.3.16.


**Reason**

> The PPP-family catalytic motifs (GDTHGQ, GDFVDRGSW, metal-binding residues) are widely taught features of serine/threonine protein phosphatases and provide a concrete sequence-based argument for EC 3.1.3.16. Eliminating C and D requires only recognizing the enzyme class (hydrolase vs. transferase/oxidoreductase). The distinction from B relies on knowing that PPP-family motifs define EC 3.1.3.16 specifically, which is general biochemistry knowledge rather than an obscure database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly wrong enzyme classes (kinase, oxidoreductase). Option B (3.1.3.112) represents a different phosphatase subclass whose catalytic architecture would not match the PPP-family motifs observed. The PPP motifs are specific enough to support a single defensible answer.


### Important caveats

- The EC 3.1.3.16 annotation carries evidence code ECO:0000305 (inferred by curator) based on PubMed:17475320, which demonstrated catalytic activity experimentally. The protein name annotation itself uses ECO:0000250 (similarity to P53043, human PP5).
- The exact identity of EC 3.1.3.112 was not independently verified from the provided evidence; the reasoning assumes it represents a mechanistically distinct phosphatase class incompatible with PPP-family motifs.
- Sequence-to-EC mapping via motif recognition is a well-established approach for PPP-family phosphatases but the specific 4-digit EC assignment (vs. 3-digit 3.1.3.-) depends on substrate specificity knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark PPP-family phosphatase catalytic motifs: 'GDTHGQ' (metal-binding/active-site region) and 'GDFVDRGSW' (conserved PPP catalytic domain signature), along with the characteristic His-Asp-His-Asp metal coordination residues. These motifs are diagnostic of serine/threonine protein phosphatases of the PPP superfamily (PP1, PP2A, PP2B, PP4, PP5, PP6), which are classified under EC 3.1.3.16. Options C (2.7.13.3, a transferase/kinase) and D (1.5.1.32, an oxidoreductase) are eliminated by recognizing the sequence as a hydrolase with phosphatase motifs rather than a kinase or redox enzyme. The PPP-family catalytic architecture is inconsistent with the mechanistic requirements of EC 3.1.3.112 (a different phosphatase class or substrate specificity), further supporting 3.1.3.16.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact identity and substrate specificity of EC 3.1.3.112 would need to be known to definitively exclude it, but the PPP-family motifs are well-established general knowledge sufficient to assign EC 3.1.3.16.",
    "reason": "The PPP-family catalytic motifs (GDTHGQ, GDFVDRGSW, metal-binding residues) are widely taught features of serine/threonine protein phosphatases and provide a concrete sequence-based argument for EC 3.1.3.16. Eliminating C and D requires only recognizing the enzyme class (hydrolase vs. transferase/oxidoreductase). The distinction from B relies on knowing that PPP-family motifs define EC 3.1.3.16 specifically, which is general biochemistry knowledge rather than an obscure database annotation."
  },
  "case_id": "EC_number_0193",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4",
      "H5",
      "C7"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q2U919 (PPP5_ASPOR, sequence matched exactly at 478 AA) is annotated as Serine/threonine-protein phosphatase T with EC 3.1.3.16. The catalytic activities (dephosphorylation of O-phospho-L-seryl-[protein] and O-phospho-L-threonyl-[protein]) are supported by experimental evidence (ECO:0000305, PubMed:17475320, Feng et al. 2007, which demonstrated dephosphorylation activity). The EC assignment is backed by both current (C4, C5, C6) and historical (H2, H4, H5) UniProt records."
  },
  "important_caveats": [
    "The EC 3.1.3.16 annotation carries evidence code ECO:0000305 (inferred by curator) based on PubMed:17475320, which demonstrated catalytic activity experimentally. The protein name annotation itself uses ECO:0000250 (similarity to P53043, human PP5).",
    "The exact identity of EC 3.1.3.112 was not independently verified from the provided evidence; the reasoning assumes it represents a mechanistically distinct phosphatase class incompatible with PPP-family motifs.",
    "Sequence-to-EC mapping via motif recognition is a well-established approach for PPP-family phosphatases but the specific 4-digit EC assignment (vs. 3-digit 3.1.3.-) depends on substrate specificity knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly wrong enzyme classes (kinase, oxidoreductase). Option B (3.1.3.112) represents a different phosphatase subclass whose catalytic architecture would not match the PPP-family motifs observed. The PPP motifs are specific enough to support a single defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0193",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q2U919 (PPP5_ASPOR, sequence matched exactly at 478 AA) is annotated as Serine/threonine-protein phosphatase T with EC 3.1.3.16. The catalytic activities (dephosphorylation of O-phospho-L-seryl-[protein] and O-phospho-L-threonyl-[protein]) are supported by experimental evidence (ECO:0000305, PubMed:17475320, Feng et al. 2007, which demonstrated dephosphorylation activity). The EC assignment is backed by both current (C4, C5, C6) and historical (H2, H4, H5) UniProt records.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4", "H5", "C7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark PPP-family phosphatase catalytic motifs: 'GDTHGQ' (metal-binding/active-site region) and 'GDFVDRGSW' (conserved PPP catalytic domain signature), along with the characteristic His-Asp-His-Asp metal coordination residues. These motifs are diagnostic of serine/threonine protein phosphatases of the PPP superfamily (PP1, PP2A, PP2B, PP4, PP5, PP6), which are classified under EC 3.1.3.16. Options C (2.7.13.3, a transferase/kinase) and D (1.5.1.32, an oxidoreductase) are eliminated by recognizing the sequence as a hydrolase with phosphatase motifs rather than a kinase or redox enzyme. The PPP-family catalytic architecture is inconsistent with the mechanistic requirements of EC 3.1.3.112 (a different phosphatase class or substrate specificity), further supporting 3.1.3.16.",
    "missing_item_specific_fact": "The exact identity and substrate specificity of EC 3.1.3.112 would need to be known to definitively exclude it, but the PPP-family motifs are well-established general knowledge sufficient to assign EC 3.1.3.16.",
    "reason": "The PPP-family catalytic motifs (GDTHGQ, GDFVDRGSW, metal-binding residues) are widely taught features of serine/threonine protein phosphatases and provide a concrete sequence-based argument for EC 3.1.3.16. Eliminating C and D requires only recognizing the enzyme class (hydrolase vs. transferase/oxidoreductase). The distinction from B relies on knowing that PPP-family motifs define EC 3.1.3.16 specifically, which is general biochemistry knowledge rather than an obscure database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly wrong enzyme classes (kinase, oxidoreductase). Option B (3.1.3.112) represents a different phosphatase subclass whose catalytic architecture would not match the PPP-family motifs observed. The PPP motifs are specific enough to support a single defensible answer."
  },
  "important_caveats": [
    "The EC 3.1.3.16 annotation carries evidence code ECO:0000305 (inferred by curator) based on PubMed:17475320, which demonstrated catalytic activity experimentally. The protein name annotation itself uses ECO:0000250 (similarity to P53043, human PP5).",
    "The exact identity of EC 3.1.3.112 was not independently verified from the provided evidence; the reasoning assumes it represents a mechanistically distinct phosphatase class incompatible with PPP-family motifs.",
    "Sequence-to-EC mapping via motif recognition is a well-established approach for PPP-family phosphatases but the specific 4-digit EC assignment (vs. 3-digit 3.1.3.-) depends on substrate specificity knowledge."
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

**Accession:** `Q2U919` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 127. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
"Q2U919"
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"17475320","source":"PubMed"}],"value":"AoPPT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"value":"3.1.3.16"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000250","id":"P53043","source":"UniProtKB"}],"value":"Serine/threonine-protein phosphatase T"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P53043","source":"UniProtKB"}],"value":"PPT"}]}}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:20630"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"name":"O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:20629"},{"database":"Rhea","id":"RHEA-COMP:9863"},{"database":"Rhea","id":"RHEA-COMP:11604"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:29999"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:83421"}]}}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:47005"}}],"reaction":{"ecNumber":"3.1.3.16","evidences":[{"evidenceCode":"ECO:0000305","id":"17475320","source":"PubMed"}],"name":"O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] + phosphate","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:47004"},{"database":"Rhea","id":"RHEA-COMP:11060"},{"database":"Rhea","id":"RHEA-COMP:11605"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:30013"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:61977"}]}}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2U919.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:21.139726+00:00.  

```json
{"citation":{"authors":["Feng B.","Zhao C.H.","Tanaka S.","Imanaka H.","Imamura K.","Nakanishi K."],"citationCrossReferences":[{"database":"PubMed","id":"17475320"},{"database":"DOI","id":"10.1016/j.ijbiomac.2007.03.005"}],"citationType":"journal article","firstPage":"281","id":"17475320","journal":"Int. J. Biol. Macromol.","lastPage":"285","publicationDate":"2007","title":"TPR domain of Ser/Thr phosphatase of Aspergillus oryzae shows no auto-inhibitory effect on the dephosphorylation activity.","volume":"41"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"17475320","source":"PubMed"}],"type":"STRAIN","value":"AGL142-72"}],"referenceNumber":2,"referencePositions":["CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `6676178685d6229700b2ed516c3ca232d2558330a425e199b609fbecba8e2b23`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-01T06:28:33.211950+00:00.  

```text
DE   RecName: Full=Serine/threonine-protein phosphatase T {ECO:0000250|UniProtKB:P53043};
DE            Short=PPT {ECO:0000250|UniProtKB:P53043};
DE            EC=3.1.3.16 {ECO:0000305|PubMed:17475320};
DE   AltName: Full=AoPPT {ECO:0000303|PubMed:17475320};
```

Source SHA-256: `2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)  
**Locator:** `lines 47-54`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-01T06:28:33.211950+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:20629, Rhea:RHEA-COMP:9863, Rhea:RHEA-
CC         COMP:11604, ChEBI:CHEBI:15377, ChEBI:CHEBI:29999, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:83421; EC=3.1.3.16;
CC         Evidence={ECO:0000305|PubMed:17475320};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:20630;
CC         Evidence={ECO:0000305|PubMed:17475320};
```

Source SHA-256: `2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2U919?format=txt&versions=127)  
**Locator:** `lines 55-62`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 127 / 1.  
**Retrieved:** 2026-11-01T06:28:33.211950+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=O-phospho-L-threonyl-[protein] + H2O = L-threonyl-[protein] +
CC         phosphate; Xref=Rhea:RHEA:47004, Rhea:RHEA-COMP:11060, Rhea:RHEA-
CC         COMP:11605, ChEBI:CHEBI:15377, ChEBI:CHEBI:30013, ChEBI:CHEBI:43474,
CC         ChEBI:CHEBI:61977; EC=3.1.3.16;
CC         Evidence={ECO:0000305|PubMed:17475320};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:47005;
CC         Evidence={ECO:0000305|PubMed:17475320};
```

Source SHA-256: `2651cbb7ccfd83249fbb6eae9366ac5480fd9278b87d40a7024c3dcc2b8c5a20`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 193. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
