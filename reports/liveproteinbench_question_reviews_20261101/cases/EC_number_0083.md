# EC_number_0083

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **B** — 2.4.1.391

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKPHNSEKYFVKNGQPHFLISGEVHYFRINPKLWRNHLQLLKQTGADTVSTYIPWDWHEIEEDDFDFEGKTHPARNLIRFIKLCKEENLDLIVKPGPYILAEYENQGLPSWLLKKLSKNAFALDENGNVISPDLVSYLSDEFLEYTFKWYDKVMPIISKHQKEHYGPITMMQLCNEIGVFQWLSGKSDYNPKVINLYKEFIIQRYKTIEKLNSVYSTNYNSFDDLKAPSGKIKLRSDYCAYFDFHLFFREYYNKYISILKNKIRSFGINIKLTHNIPGWIYGNASELPMLISTYSEIMKNHPDIIFGLDHIPEFVSFRNAHSDLACNKILEAMQPEAPVWAAEFQAGTREHHVKAYAKDLETFYIASLAHGIKGFNYYMFSQGINPEGKGFYGKTFYFQTALDAASNKLALYDSIKKVNRFIRKEQKDLLRTNVNSEICVGFYKPYFFTELISSQLLKEKKLNVEELGLYIDPRFLREEILFNGLLRGLQTLNYNYDVVDLENCDLKSLTAYKQLWITSAEFMDAETQNLLSEFVLNGGNLILYPAVPTLDNYLNRCEILKNNFGIEFITKDSSHKVSAFGIEDVFTAFSKKQIYNDTNSKPIAFTQENEICGIRKKIGKGELTILGFAFGYTSDEHLELIDKLVKLNKIKRELFVSDKDIQFVVRENNKSRYIFFLNYHNERKTFNYRKSSELKKKKSEEISIAPFSYKVIKENK

[Multiple Choices]
A. 2.4.1.261
B. 2.4.1.391
C. 3.2.1.8
D. 2.8.1.7
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

> The exact 716-aa sequence matches the UniProt entry for this protein. That entry assigns EC 2.4.1.391 and links the catalytic-activity annotation to experimental evidence in a cited publication, supporting choice B.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support broad functional-family inference, but the input gives no concrete basis for identifying the enzyme's specific beta-1,2-glucosyltransferase activity and distinguishing this complete EC number from the alternatives.


**Missing item-specific fact**

> The protein-specific experimentally characterized catalytic activity, classified as EC 2.4.1.391.


**Reason**

> The supported answer depends on a protein-specific functional annotation or experimental result absent from the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports one EC number, but the supplied sequence and choices alone do not provide a reliable way to distinguish it.


### Important caveats

- The evidence establishes the EC assignment for the sequence-matched UniProt entry; the author's exact source snapshot is unknown.
- The EC annotation is linked to experimental evidence in the cited publication, but that primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support broad functional-family inference, but the input gives no concrete basis for identifying the enzyme's specific beta-1,2-glucosyltransferase activity and distinguishing this complete EC number from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific experimentally characterized catalytic activity, classified as EC 2.4.1.391.",
    "reason": "The supported answer depends on a protein-specific functional annotation or experimental result absent from the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "case_id": "EC_number_0083",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The exact 716-aa sequence matches the UniProt entry for this protein. That entry assigns EC 2.4.1.391 and links the catalytic-activity annotation to experimental evidence in a cited publication, supporting choice B."
  },
  "important_caveats": [
    "The evidence establishes the EC assignment for the sequence-matched UniProt entry; the author's exact source snapshot is unknown.",
    "The EC annotation is linked to experimental evidence in the cited publication, but that primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one EC number, but the supplied sequence and choices alone do not provide a reliable way to distinguish it."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 716-aa sequence matches the UniProt entry for this protein. That entry assigns EC 2.4.1.391 and links the catalytic-activity annotation to experimental evidence in a cited publication, supporting choice B.",
    "evidence_ids": ["C1", "C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support broad functional-family inference, but the input gives no concrete basis for identifying the enzyme's specific beta-1,2-glucosyltransferase activity and distinguishing this complete EC number from the alternatives.",
    "missing_item_specific_fact": "The protein-specific experimentally characterized catalytic activity, classified as EC 2.4.1.391.",
    "reason": "The supported answer depends on a protein-specific functional annotation or experimental result absent from the question. Recognizing the sequence or recalling its database entry would be lookup or memorization, not reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports one EC number, but the supplied sequence and choices alone do not provide a reliable way to distinguish it."
  },
  "important_caveats": [
    "The evidence establishes the EC assignment for the sequence-matched UniProt entry; the author's exact source snapshot is unknown.",
    "The EC annotation is linked to experimental evidence in the cited publication, but that primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt entry I0AIT9 (716 AA, SHA256 confirmed). UniProt annotates this protein as Beta-1,2-glucosyltransferase with EC 2.4.1.391, assigned with evidence code ECO:0000269 (direct assay evidence) from PubMed:35065074 (Kobayashi et al., 2022, J. Biol. Chem.). The characterization included X-ray crystallography at 1.56 Å in complexes with beta-D-glucose, sophorose, and alternative substrates, plus mutagenesis of active-site Glu-176 and Glu-343. The catalytic reaction (a D-glucoside + &#91;(1->2)-beta-D-glucosyl&#93;(n) → a beta-D-glucosyl-(1->2)-D-glucoside + &#91;(1->2)-beta-D-glucosyl&#93;(n-1)) confirms the EC assignment. This is experimental, not merely computational or similarity-based annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One could potentially eliminate C (EC 3.2.1.8, endo-1,4-beta-xylanase, a hydrolase) and D (EC 2.8.1.7, a sulfurtransferase) by noting the absence of typical hydrolase or sulfurtransferase catalytic motifs and the overall size/composition suggesting a transferase. However, distinguishing A (EC 2.4.1.261) from B (EC 2.4.1.391) requires knowing the specific glycosidic linkage formed (1,3 vs 1,2), which depends on active-site geometry determined by X-ray crystallography and enzymatic assays, not on recognizable sequence motifs.


**Missing item-specific fact**

> The specific linkage specificity (beta-1,2 vs beta-1,3 or other) of this particular glycosyltransferase from Ignavibacterium album, which was characterized as a 'novel' enzyme in 2022 and cannot be inferred from sequence motifs alone. The protein lacks well-known GT-A/GT-B fold signatures that would allow confident linkage prediction from primary sequence.


**Reason**

> Both A and B are glycosyltransferases in the 2.4.1.x subclass. The distinction between beta-1,2 and beta-1,3 (or other) glucosyltransferase activity depends on precise active-site architecture revealed only by structural and enzymatic characterization. This enzyme was described as 'novel' in its 2022 publication, meaning no well-established sequence-to-linkage heuristic exists. A model would need to recognize this specific sequence (or its close homologs) and recall its database annotation. Eliminating C and D through general enzyme-class reasoning is possible, but the critical A-vs-B discrimination is item-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Without structural or functional knowledge specific to this protein, both 2.4.1.261 and 2.4.1.391 are plausible glycosyltransferase assignments. The sequence provides no obvious motif that distinguishes 1,2-linkage from 1,3-linkage specificity. A model lacking specific knowledge of I0AIT9 could reasonably select either A or B.


### Important caveats

- The UniProt entry was first publicly released in April 2025; the underlying paper is from 2022. The benchmark's author source snapshot is unknown, so it is unclear whether the annotation was available at question-construction time.
- The identity origin note states the accession was inferred from dataset image-path metadata, not from the evaluated model's input.
- EC 2.4.1.261 and 2.4.1.391 are both in the glycosyltransferase (2.4.1.x) subclass; their distinction is at the level of glycosidic linkage specificity, which is not reliably predictable from primary sequence for novel enzymes.
- The elimination of options C (hydrolase) and D (sulfurtransferase) is more straightforward from general biological reasoning, but the critical discrimination is between A and B.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One could potentially eliminate C (EC 3.2.1.8, endo-1,4-beta-xylanase, a hydrolase) and D (EC 2.8.1.7, a sulfurtransferase) by noting the absence of typical hydrolase or sulfurtransferase catalytic motifs and the overall size/composition suggesting a transferase. However, distinguishing A (EC 2.4.1.261) from B (EC 2.4.1.391) requires knowing the specific glycosidic linkage formed (1,3 vs 1,2), which depends on active-site geometry determined by X-ray crystallography and enzymatic assays, not on recognizable sequence motifs.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific linkage specificity (beta-1,2 vs beta-1,3 or other) of this particular glycosyltransferase from Ignavibacterium album, which was characterized as a 'novel' enzyme in 2022 and cannot be inferred from sequence motifs alone. The protein lacks well-known GT-A/GT-B fold signatures that would allow confident linkage prediction from primary sequence.",
    "reason": "Both A and B are glycosyltransferases in the 2.4.1.x subclass. The distinction between beta-1,2 and beta-1,3 (or other) glucosyltransferase activity depends on precise active-site architecture revealed only by structural and enzymatic characterization. This enzyme was described as 'novel' in its 2022 publication, meaning no well-established sequence-to-linkage heuristic exists. A model would need to recognize this specific sequence (or its close homologs) and recall its database annotation. Eliminating C and D through general enzyme-class reasoning is possible, but the critical A-vs-B discrimination is item-specific lookup."
  },
  "case_id": "EC_number_0083",
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
    "reason": "The sequence exactly matches UniProt entry I0AIT9 (716 AA, SHA256 confirmed). UniProt annotates this protein as Beta-1,2-glucosyltransferase with EC 2.4.1.391, assigned with evidence code ECO:0000269 (direct assay evidence) from PubMed:35065074 (Kobayashi et al., 2022, J. Biol. Chem.). The characterization included X-ray crystallography at 1.56 Å in complexes with beta-D-glucose, sophorose, and alternative substrates, plus mutagenesis of active-site Glu-176 and Glu-343. The catalytic reaction (a D-glucoside + [(1->2)-beta-D-glucosyl](n) → a beta-D-glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1)) confirms the EC assignment. This is experimental, not merely computational or similarity-based annotation."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released in April 2025; the underlying paper is from 2022. The benchmark's author source snapshot is unknown, so it is unclear whether the annotation was available at question-construction time.",
    "The identity origin note states the accession was inferred from dataset image-path metadata, not from the evaluated model's input.",
    "EC 2.4.1.261 and 2.4.1.391 are both in the glycosyltransferase (2.4.1.x) subclass; their distinction is at the level of glycosidic linkage specificity, which is not reliably predictable from primary sequence for novel enzymes.",
    "The elimination of options C (hydrolase) and D (sulfurtransferase) is more straightforward from general biological reasoning, but the critical discrimination is between A and B."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Without structural or functional knowledge specific to this protein, both 2.4.1.261 and 2.4.1.391 are plausible glycosyltransferase assignments. The sequence provides no obvious motif that distinguishes 1,2-linkage from 1,3-linkage specificity. A model lacking specific knowledge of I0AIT9 could reasonably select either A or B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0083",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry I0AIT9 (716 AA, SHA256 confirmed). UniProt annotates this protein as Beta-1,2-glucosyltransferase with EC 2.4.1.391, assigned with evidence code ECO:0000269 (direct assay evidence) from PubMed:35065074 (Kobayashi et al., 2022, J. Biol. Chem.). The characterization included X-ray crystallography at 1.56 Å in complexes with beta-D-glucose, sophorose, and alternative substrates, plus mutagenesis of active-site Glu-176 and Glu-343. The catalytic reaction (a D-glucoside + [(1->2)-beta-D-glucosyl](n) → a beta-D-glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1)) confirms the EC assignment. This is experimental, not merely computational or similarity-based annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One could potentially eliminate C (EC 3.2.1.8, endo-1,4-beta-xylanase, a hydrolase) and D (EC 2.8.1.7, a sulfurtransferase) by noting the absence of typical hydrolase or sulfurtransferase catalytic motifs and the overall size/composition suggesting a transferase. However, distinguishing A (EC 2.4.1.261) from B (EC 2.4.1.391) requires knowing the specific glycosidic linkage formed (1,3 vs 1,2), which depends on active-site geometry determined by X-ray crystallography and enzymatic assays, not on recognizable sequence motifs.",
    "missing_item_specific_fact": "The specific linkage specificity (beta-1,2 vs beta-1,3 or other) of this particular glycosyltransferase from Ignavibacterium album, which was characterized as a 'novel' enzyme in 2022 and cannot be inferred from sequence motifs alone. The protein lacks well-known GT-A/GT-B fold signatures that would allow confident linkage prediction from primary sequence.",
    "reason": "Both A and B are glycosyltransferases in the 2.4.1.x subclass. The distinction between beta-1,2 and beta-1,3 (or other) glucosyltransferase activity depends on precise active-site architecture revealed only by structural and enzymatic characterization. This enzyme was described as 'novel' in its 2022 publication, meaning no well-established sequence-to-linkage heuristic exists. A model would need to recognize this specific sequence (or its close homologs) and recall its database annotation. Eliminating C and D through general enzyme-class reasoning is possible, but the critical A-vs-B discrimination is item-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Without structural or functional knowledge specific to this protein, both 2.4.1.261 and 2.4.1.391 are plausible glycosyltransferase assignments. The sequence provides no obvious motif that distinguishes 1,2-linkage from 1,3-linkage specificity. A model lacking specific knowledge of I0AIT9 could reasonably select either A or B."
  },
  "important_caveats": [
    "The UniProt entry was first publicly released in April 2025; the underlying paper is from 2022. The benchmark's author source snapshot is unknown, so it is unclear whether the annotation was available at question-construction time.",
    "The identity origin note states the accession was inferred from dataset image-path metadata, not from the evaluated model's input.",
    "EC 2.4.1.261 and 2.4.1.391 are both in the glycosyltransferase (2.4.1.x) subclass; their distinction is at the level of glycosidic linkage specificity, which is not reliably predictable from primary sequence for novel enzymes.",
    "The elimination of options C (hydrolase) and D (sulfurtransferase) is more straightforward from general biological reasoning, but the critical discrimination is between A and B."
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

**Accession:** `I0AIT9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 55. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
"I0AIT9"
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35065074","source":"PubMed"}],"value":"Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35065074","source":"PubMed"}],"value":"IaSGT"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"value":"2.4.1.391"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35065074","source":"PubMed"}],"value":"Beta-1,2-glucosyltransferase"}}}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"2.4.1.391","evidences":[{"evidenceCode":"ECO:0000269","id":"35065074","source":"PubMed"}],"name":"a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:78691"},{"database":"Rhea","id":"RHEA-COMP:11881"},{"database":"Rhea","id":"RHEA-COMP:11882"},{"database":"ChEBI","id":"CHEBI:27517"},{"database":"ChEBI","id":"CHEBI:35436"},{"database":"ChEBI","id":"CHEBI:229541"}]}}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"citation":{"authors":["Kobayashi K.","Shimizu H.","Tanaka N.","Kuramochi K.","Nakai H.","Nakajima M.","Taguchi H."],"citationCrossReferences":[{"database":"PubMed","id":"35065074"},{"database":"DOI","id":"10.1016/j.jbc.2022.101606"}],"citationType":"journal article","firstPage":"101606","id":"35065074","journal":"J. Biol. Chem.","lastPage":"101606","publicationDate":"2022","title":"Characterization and structural analyses of a novel glycosyltransferase acting on the beta-1,2-glucosidic linkages.","volume":"298"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7VKW","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKX","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKY","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL0","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL1","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL2","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL3","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL4","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL5","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL6","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE; SOPHOROSE AND ALTERNATIVE SUBSTRATES","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","ACTIVE SITE","MUTAGENESIS OF GLU-176 AND GLU-343"]}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 1-15`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
ID   B12GT_IGNAJ             Reviewed;         716 AA.
AC   I0AIT9;
DT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.
DT   13-JUN-2012, sequence version 1.
DT   28-JAN-2026, entry version 55.
DE   RecName: Full=Beta-1,2-glucosyltransferase {ECO:0000303|PubMed:35065074};
DE            EC=2.4.1.391 {ECO:0000269|PubMed:35065074};
DE   AltName: Full=Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase {ECO:0000303|PubMed:35065074};
DE   AltName: Full=IaSGT {ECO:0000303|PubMed:35065074};
GN   OrderedLocusNames=IALB_1185 {ECO:0000312|EMBL:AFH48896.1};
OS   Ignavibacterium album (strain DSM 19864 / JCM 16511 / NBRC 101810 /
OS   Mat9-16).
OC   Bacteria; Pseudomonadati; Ignavibacteriota; Ignavibacteria;
OC   Ignavibacteriales; Ignavibacteriaceae; Ignavibacterium.
OX   NCBI_TaxID=945713;
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 6-9`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
DE   RecName: Full=Beta-1,2-glucosyltransferase {ECO:0000303|PubMed:35065074};
DE            EC=2.4.1.391 {ECO:0000269|PubMed:35065074};
DE   AltName: Full=Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase {ECO:0000303|PubMed:35065074};
DE   AltName: Full=IaSGT {ECO:0000303|PubMed:35065074};
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 25-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
RN   [2] {ECO:0007744|PDB:7VKW, ECO:0007744|PDB:7VKX, ECO:0007744|PDB:7VKY, ECO:0007744|PDB:7VKZ, ECO:0007744|PDB:7VL0, ECO:0007744|PDB:7VL1, ECO:0007744|PDB:7VL2, ECO:0007744|PDB:7VL3, ECO:0007744|PDB:7VL4, ECO:0007744|PDB:7VL5, ECO:0007744|PDB:7VL6}
RP   X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE;
RP   SOPHOROSE AND ALTERNATIVE SUBSTRATES, FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF
RP   GLU-176 AND GLU-343.
RC   STRAIN=DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16;
RX   PubMed=35065074; DOI=10.1016/j.jbc.2022.101606;
RA   Kobayashi K., Shimizu H., Tanaka N., Kuramochi K., Nakai H., Nakajima M.,
RA   Taguchi H.;
RT   "Characterization and structural analyses of a novel glycosyltransferase
RT   acting on the beta-1,2-glucosidic linkages.";
RL   J. Biol. Chem. 298:101606-101606(2022).
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 46-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-
CC         glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1);
CC         Xref=Rhea:RHEA:78691, Rhea:RHEA-COMP:11881, Rhea:RHEA-COMP:11882,
CC         ChEBI:CHEBI:27517, ChEBI:CHEBI:35436, ChEBI:CHEBI:229541;
CC         EC=2.4.1.391; Evidence={ECO:0000269|PubMed:35065074};
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 83. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
