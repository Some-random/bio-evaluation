# EC_number_0199

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 3.2.1.20

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKTFAPLLATLLLAGFGSALQWWEHGNFYQVYPRSFKDSDGNGIGDLDGVTEKLQYLKDVGMDGIWLSPIFASPMADFGYDISDFYNIQGEYGDLAAFERLSAKCKELGLRLILDFVPNHTSNQHEYFKKSVQKEDPYTNYYVWHPGVTNEDGTKSPPSNWISVFRGSAWEWNEDRQEYYLHQFLKEQPDLNYRDPALVEEMKNVLKFWLNKGVSGFRIDAVPYLFESVEVENRYVDEPLSRATDDAENPAYLIHNQTMDQPETYDMIYQWRAVLDEFTAKDNQTRIMMTEGYTSIPNVMKFFGEGEQNGAQIPFNFQMISNLRKTSTAADFARYANLWLDNLPAGRRSNWVLGNHDNNRIGSRLGEAKIDLYNIALQTLPDIAVTYYGEEIGMVDQPIPFNETVDPAGLRAGPDDYTLYSRDPARTPMQWNSDKNAGFSSADKTWLPVATNYKQLNVKAQDAAQKSHLKLFKRLTTYRKRQILTHGDLDLRTTDSNLVLYKRKVDKVGYVVVVLNFSDEPQSLAAIKQQFPGADDRLQVVASSKLVTIKDNKWINVADTELPGESAIVLQKLWGPNPVVVYEA

[Multiple Choices]
A. 3.2.1.20
B. 3.2.1.105
C. 2.7.11.1
D. 1.1.1.17
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

> The exact supplied sequence matches the UniProt entry annotated as EC 3.2.1.20. The entry reports the catalytic reaction and cites experimental evidence (ECO:0000269) for that EC assignment; this is more than a computational prediction, although the cited papers were not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic signal sequence and enzyme-like sequence are consistent with a secreted glycosidase, so the kinase and dehydrogenase choices are biologically less plausible. Those clues do not establish the substrate specificity needed to distinguish the two glycosidase EC choices.


**Missing item-specific fact**

> The protein's experimentally established catalytic activity and substrate specificity—hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues—are not supplied in the question.


**Reason**

> Identifying the precise EC number requires protein-specific functional knowledge absent from the input; recognizing the sequence or consulting its annotation would be lookup, not reasoning from the provided information.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied reviewer-only evidence supports choice A for this exact sequence. The sequence alone does not adequately distinguish the two glycosidase options, but that limitation does not make the experimentally supported answer ambiguous.


### Important caveats

- The sequence match and functional annotation come from reviewer-only UniProt evidence and were not available to the evaluated model.
- The annotation cites experimental evidence, but the primary studies were not independently validated here; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic signal sequence and enzyme-like sequence are consistent with a secreted glycosidase, so the kinase and dehydrogenase choices are biologically less plausible. Those clues do not establish the substrate specificity needed to distinguish the two glycosidase EC choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's experimentally established catalytic activity and substrate specificity—hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues—are not supplied in the question.",
    "reason": "Identifying the precise EC number requires protein-specific functional knowledge absent from the input; recognizing the sequence or consulting its annotation would be lookup, not reasoning from the provided information."
  },
  "case_id": "EC_number_0199",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as EC 3.2.1.20. The entry reports the catalytic reaction and cites experimental evidence (ECO:0000269) for that EC assignment; this is more than a computational prediction, although the cited papers were not independently reviewed here."
  },
  "important_caveats": [
    "The sequence match and functional annotation come from reviewer-only UniProt evidence and were not available to the evaluated model.",
    "The annotation cites experimental evidence, but the primary studies were not independently validated here; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer-only evidence supports choice A for this exact sequence. The sequence alone does not adequately distinguish the two glycosidase options, but that limitation does not make the experimentally supported answer ambiguous."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches the UniProt entry annotated as EC 3.2.1.20. The entry reports the catalytic reaction and cites experimental evidence (ECO:0000269) for that EC assignment; this is more than a computational prediction, although the cited papers were not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic signal sequence and enzyme-like sequence are consistent with a secreted glycosidase, so the kinase and dehydrogenase choices are biologically less plausible. Those clues do not establish the substrate specificity needed to distinguish the two glycosidase EC choices.",
    "missing_item_specific_fact": "The protein's experimentally established catalytic activity and substrate specificity—hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues—are not supplied in the question.",
    "reason": "Identifying the precise EC number requires protein-specific functional knowledge absent from the input; recognizing the sequence or consulting its annotation would be lookup, not reasoning from the provided information."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied reviewer-only evidence supports choice A for this exact sequence. The sequence alone does not adequately distinguish the two glycosidase options, but that limitation does not make the experimentally supported answer ambiguous."
  },
  "important_caveats": [
    "The sequence match and functional annotation come from reviewer-only UniProt evidence and were not available to the evaluated model.",
    "The annotation cites experimental evidence, but the primary studies were not independently validated here; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry B0XAA1 (MALT_CULQU) exactly (SHA-256 confirmed). The entry is annotated as Salivary alpha-glucosidase with EC 3.2.1.20, supported by experimental evidence (ECO:0000269) from two independent studies (PubMed:25746591, 2015; PubMed:38428508, 2024) reporting catalytic activity: hydrolysis of terminal, non-reducing (1→4)-linked α-D-glucose residues with release of α-D-glucose. This is experimental, not merely computational, annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Choices C (2.7.11.1, protein kinase) and D (1.1.1.17, alcohol dehydrogenase) can be plausibly eliminated by general reasoning: the sequence lacks Rossmann-fold GxGxxG motifs, zinc-binding residues, and the glycine-rich loop / catalytic Lys / DFG triad characteristic of kinases or alcohol dehydrogenases. The N-terminal hydrophobic stretch suggests a secreted protein, consistent with a glycosidase. However, distinguishing A (3.2.1.20, α-glucosidase, GH family 31) from B (3.2.1.105, α-N-acetylglucosaminidase, GH family 27) requires recognizing specific GH-family catalytic motifs (e.g., the DxxNDxxE nucleophile/acid-base arrangement of GH31 vs. the Glu-x-Asp-x-Glu catalytic triad of GH27) or aligning to known family signatures. This is specialized structural/biochemical knowledge of glycoside hydrolase families, not general biological reasoning.


**Missing item-specific fact**

> The specific glycoside hydrolase family assignment (GH31 vs GH27) of this particular sequence, which determines whether the substrate specificity is α-glucose (EC 3.2.1.20) or α-N-acetylglucosamine (EC 3.2.1.105). Without database alignment or memorized family signatures, the two glycosidase options cannot be reliably distinguished from the raw sequence.


**Reason**

> While C and D are eliminable by general reasoning (absence of kinase/dehydrogenase structural motifs), the critical A-vs-B distinction between two closely related glycoside hydrolase EC numbers requires item-specific knowledge of GH-family active-site architecture or database lookup. General biological knowledge of 'it's a glycosidase' narrows to 3.2.1.x but cannot resolve the fourth digit.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (3.2.1.20) and B (3.2.1.105) are glycoside hydrolases acting on α-linked sugars. Without structural alignment or explicit family assignment, a knowledgeable model could reasonably argue for either based on partial motif matching. C and D are clearly eliminable, but A vs B is genuinely ambiguous from sequence alone without lookup.


### Important caveats

- The EC annotation is experimentally supported (ECO:0000269) by two independent studies, strengthening the key.
- The sequence is from Culex quinquefasciatus (Southern house mosquito), a salivary protein—context that might hint at a digestive/feeding role but does not by itself resolve GH31 vs GH27.
- The reviewer-only evidence confirms sequence match and annotation, but this information was not available to the evaluated model.
- The distinction between 3.2.1.20 and 3.2.1.105 is a fourth-digit (substrate-specificity) distinction within the same EC class, making it inherently harder to resolve from sequence than a first-digit (reaction class) distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choices C (2.7.11.1, protein kinase) and D (1.1.1.17, alcohol dehydrogenase) can be plausibly eliminated by general reasoning: the sequence lacks Rossmann-fold GxGxxG motifs, zinc-binding residues, and the glycine-rich loop / catalytic Lys / DFG triad characteristic of kinases or alcohol dehydrogenases. The N-terminal hydrophobic stretch suggests a secreted protein, consistent with a glycosidase. However, distinguishing A (3.2.1.20, α-glucosidase, GH family 31) from B (3.2.1.105, α-N-acetylglucosaminidase, GH family 27) requires recognizing specific GH-family catalytic motifs (e.g., the DxxNDxxE nucleophile/acid-base arrangement of GH31 vs. the Glu-x-Asp-x-Glu catalytic triad of GH27) or aligning to known family signatures. This is specialized structural/biochemical knowledge of glycoside hydrolase families, not general biological reasoning.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific glycoside hydrolase family assignment (GH31 vs GH27) of this particular sequence, which determines whether the substrate specificity is α-glucose (EC 3.2.1.20) or α-N-acetylglucosamine (EC 3.2.1.105). Without database alignment or memorized family signatures, the two glycosidase options cannot be reliably distinguished from the raw sequence.",
    "reason": "While C and D are eliminable by general reasoning (absence of kinase/dehydrogenase structural motifs), the critical A-vs-B distinction between two closely related glycoside hydrolase EC numbers requires item-specific knowledge of GH-family active-site architecture or database lookup. General biological knowledge of 'it's a glycosidase' narrows to 3.2.1.x but cannot resolve the fourth digit."
  },
  "case_id": "EC_number_0199",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry B0XAA1 (MALT_CULQU) exactly (SHA-256 confirmed). The entry is annotated as Salivary alpha-glucosidase with EC 3.2.1.20, supported by experimental evidence (ECO:0000269) from two independent studies (PubMed:25746591, 2015; PubMed:38428508, 2024) reporting catalytic activity: hydrolysis of terminal, non-reducing (1→4)-linked α-D-glucose residues with release of α-D-glucose. This is experimental, not merely computational, annotation."
  },
  "important_caveats": [
    "The EC annotation is experimentally supported (ECO:0000269) by two independent studies, strengthening the key.",
    "The sequence is from Culex quinquefasciatus (Southern house mosquito), a salivary protein—context that might hint at a digestive/feeding role but does not by itself resolve GH31 vs GH27.",
    "The reviewer-only evidence confirms sequence match and annotation, but this information was not available to the evaluated model.",
    "The distinction between 3.2.1.20 and 3.2.1.105 is a fourth-digit (substrate-specificity) distinction within the same EC class, making it inherently harder to resolve from sequence than a first-digit (reaction class) distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (3.2.1.20) and B (3.2.1.105) are glycoside hydrolases acting on α-linked sugars. Without structural alignment or explicit family assignment, a knowledgeable model could reasonably argue for either based on partial motif matching. C and D are clearly eliminable, but A vs B is genuinely ambiguous from sequence alone without lookup."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0199",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry B0XAA1 (MALT_CULQU) exactly (SHA-256 confirmed). The entry is annotated as Salivary alpha-glucosidase with EC 3.2.1.20, supported by experimental evidence (ECO:0000269) from two independent studies (PubMed:25746591, 2015; PubMed:38428508, 2024) reporting catalytic activity: hydrolysis of terminal, non-reducing (1→4)-linked α-D-glucose residues with release of α-D-glucose. This is experimental, not merely computational, annotation.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Choices C (2.7.11.1, protein kinase) and D (1.1.1.17, alcohol dehydrogenase) can be plausibly eliminated by general reasoning: the sequence lacks Rossmann-fold GxGxxG motifs, zinc-binding residues, and the glycine-rich loop / catalytic Lys / DFG triad characteristic of kinases or alcohol dehydrogenases. The N-terminal hydrophobic stretch suggests a secreted protein, consistent with a glycosidase. However, distinguishing A (3.2.1.20, α-glucosidase, GH family 31) from B (3.2.1.105, α-N-acetylglucosaminidase, GH family 27) requires recognizing specific GH-family catalytic motifs (e.g., the DxxNDxxE nucleophile/acid-base arrangement of GH31 vs. the Glu-x-Asp-x-Glu catalytic triad of GH27) or aligning to known family signatures. This is specialized structural/biochemical knowledge of glycoside hydrolase families, not general biological reasoning.",
    "missing_item_specific_fact": "The specific glycoside hydrolase family assignment (GH31 vs GH27) of this particular sequence, which determines whether the substrate specificity is α-glucose (EC 3.2.1.20) or α-N-acetylglucosamine (EC 3.2.1.105). Without database alignment or memorized family signatures, the two glycosidase options cannot be reliably distinguished from the raw sequence.",
    "reason": "While C and D are eliminable by general reasoning (absence of kinase/dehydrogenase structural motifs), the critical A-vs-B distinction between two closely related glycoside hydrolase EC numbers requires item-specific knowledge of GH-family active-site architecture or database lookup. General biological knowledge of 'it's a glycosidase' narrows to 3.2.1.x but cannot resolve the fourth digit."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (3.2.1.20) and B (3.2.1.105) are glycoside hydrolases acting on α-linked sugars. Without structural alignment or explicit family assignment, a knowledgeable model could reasonably argue for either based on partial motif matching. C and D are clearly eliminable, but A vs B is genuinely ambiguous from sequence alone without lookup."
  },
  "important_caveats": [
    "The EC annotation is experimentally supported (ECO:0000269) by two independent studies, strengthening the key.",
    "The sequence is from Culex quinquefasciatus (Southern house mosquito), a salivary protein—context that might hint at a digestive/feeding role but does not by itself resolve GH31 vs GH27.",
    "The reviewer-only evidence confirms sequence match and annotation, but this information was not available to the evaluated model.",
    "The distinction between 3.2.1.20 and 3.2.1.105 is a fourth-digit (substrate-specificity) distinction within the same EC class, making it inherently harder to resolve from sequence than a first-digit (reaction class) distinction."
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

**Accession:** `B0XAA1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 92. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:15.565561+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"25746591","source":"PubMed"}],"value":"CQMalI"}}],"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"25746591","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38428508","source":"PubMed"}],"value":"3.2.1.20"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38428508","source":"PubMed"}],"value":"Salivary alpha-glucosidase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38428508","source":"PubMed"}],"value":"CxGluc"}]}}
```

Source SHA-256: `9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:15.565561+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.20","evidences":[{"evidenceCode":"ECO:0000269","id":"25746591","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"38428508","source":"PubMed"}],"name":"Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose."}}
```

Source SHA-256: `9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:15.565561+00:00.  

```json
{"citation":{"authors":["Suthangkornkul R.","Sirichaiyakul P.","Sungvornyothin S.","Thepouyporn A.","Svasti J.","Arthan D."],"citationCrossReferences":[{"database":"PubMed","id":"25746591"},{"database":"DOI","id":"10.1016/j.pep.2015.02.018"}],"citationType":"journal article","firstPage":"145","id":"25746591","journal":"Protein Expr. Purif.","lastPage":"150","publicationDate":"2015","title":"Functional expression and molecular characterization of Culex quinquefasciatus salivary alpha-glucosidase (MalI).","volume":"110"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","GLYCOSYLATION"]}
```

Source SHA-256: `9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0XAA1.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:27:15.565561+00:00.  

```json
{"citation":{"authors":["Williams A.E.","Gittis A.G.","Botello K.","Cruz P.","Martin-Martin I.","Valenzuela Leon P.C.","Sumner B.","Bonilla B.","Calvo E."],"citationCrossReferences":[{"database":"PubMed","id":"38428508"},{"database":"DOI","id":"10.1016/j.ibmb.2024.104097"}],"citationType":"journal article","firstPage":"104097","id":"38428508","journal":"Insect Biochem. Mol. Biol.","lastPage":"104097","publicationDate":"2024","title":"Structural and functional comparisons of salivary alpha-glucosidases from the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex quinquefasciatus.","volume":"167"},"evidences":[{"evidenceCode":"ECO:0000305"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBCELLULAR LOCATION","TISSUE SPECIFICITY"]}
```

Source SHA-256: `9afccd0935d9c913183f609d3d8afcc2196f79187f5d0532d2ba6ed0e5048c10`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)  
**Locator:** `lines 6-10`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-02T04:27:18.547256+00:00.  

```text
DE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};
DE            Short=CxGluc {ECO:0000303|PubMed:38428508};
DE            EC=3.2.1.20 {ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};
DE   AltName: Full=CQMalI {ECO:0000303|PubMed:25746591};
DE   Flags: Precursor;
```

Source SHA-256: `5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)  
**Locator:** `lines 32-40`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-02T04:27:18.547256+00:00.  

```text
RN   [2] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL
RP   PROPERTIES, AND GLYCOSYLATION.
RX   PubMed=25746591; DOI=10.1016/j.pep.2015.02.018;
RA   Suthangkornkul R., Sirichaiyakul P., Sungvornyothin S., Thepouyporn A.,
RA   Svasti J., Arthan D.;
RT   "Functional expression and molecular characterization of Culex
RT   quinquefasciatus salivary alpha-glucosidase (MalI).";
RL   Protein Expr. Purif. 110:145-150(2015).
```

Source SHA-256: `5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)  
**Locator:** `lines 41-50`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-02T04:27:18.547256+00:00.  

```text
RN   [3] {ECO:0000305}
RP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR
RP   LOCATION, AND TISSUE SPECIFICITY.
RX   PubMed=38428508; DOI=10.1016/j.ibmb.2024.104097;
RA   Williams A.E., Gittis A.G., Botello K., Cruz P., Martin-Martin I.,
RA   Valenzuela Leon P.C., Sumner B., Bonilla B., Calvo E.;
RT   "Structural and functional comparisons of salivary alpha-glucosidases from
RT   the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex
RT   quinquefasciatus.";
RL   Insect Biochem. Mol. Biol. 167:104097-104097(2024).
```

Source SHA-256: `5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0XAA1?format=txt&versions=92)  
**Locator:** `lines 56-59`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 92 / 1.  
**Retrieved:** 2026-11-02T04:27:18.547256+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-
CC         glucose residues with release of alpha-D-glucose.; EC=3.2.1.20;
CC         Evidence={ECO:0000269|PubMed:25746591, ECO:0000269|PubMed:38428508};
```

Source SHA-256: `5fda9ac6361a740657451da46434a8060a2e37043092db9553e846bf116af583`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 199. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
