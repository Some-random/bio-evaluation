# active_site_0093

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `active_site`  
**Author expected answer:** **C** — Position 176 (Proton donor/acceptor)

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
A. Position 359 (For beta-ketoacyl synthase activity)
B. Position 2056 (For beta-ketoacyl synthase 2 activity)
C. Position 176 (Proton donor/acceptor)
D. Position 662 (For acyltransferase activity of LM)
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the 716-residue UniProt entry for this glucosyltransferase, which annotates residue 176 as the proton donor/acceptor. This supports choice C. The UniProt feature is a curator inference citing a paper, not itself direct experimental evidence; the cited paper is identified as covering active-site analysis and mutagenesis of Glu-176 and Glu-343.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C26](#evidence-c26), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence length rules out position 2056, and the unrelated activity labels may help reject some distractors, but the input gives no enzyme identity or functional context that establishes the catalytic role of residue 176.


**Missing item-specific fact**

> The protein-specific annotation or experimental characterization assigning residue 176 as the proton donor/acceptor is needed to select C.


**Reason**

> Knowing which exact residue performs this catalytic role requires an item-specific active-site assignment; it is not meaningfully derivable from the bare sequence and choices by general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports C among the listed choices; no other option is supported as the proton donor/acceptor for this sequence.


### Important caveats

- The reviewer-only UniProt records match the input sequence, but the author's exact source snapshot is unknown.
- The database annotation cites a publication that includes structural work and mutagenesis, but the supplied evidence does not independently establish the paper's experimental results.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence length rules out position 2056, and the unrelated activity labels may help reject some distractors, but the input gives no enzyme identity or functional context that establishes the catalytic role of residue 176.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation or experimental characterization assigning residue 176 as the proton donor/acceptor is needed to select C.",
    "reason": "Knowing which exact residue performs this catalytic role requires an item-specific active-site assignment; it is not meaningfully derivable from the bare sequence and choices by general biological reasoning."
  },
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C26",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 716-residue UniProt entry for this glucosyltransferase, which annotates residue 176 as the proton donor/acceptor. This supports choice C. The UniProt feature is a curator inference citing a paper, not itself direct experimental evidence; the cited paper is identified as covering active-site analysis and mutagenesis of Glu-176 and Glu-343."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the input sequence, but the author's exact source snapshot is unknown.",
    "The database annotation cites a publication that includes structural work and mutagenesis, but the supplied evidence does not independently establish the paper's experimental results."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports C among the listed choices; no other option is supported as the proton donor/acceptor for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the 716-residue UniProt entry for this glucosyltransferase, which annotates residue 176 as the proton donor/acceptor. This supports choice C. The UniProt feature is a curator inference citing a paper, not itself direct experimental evidence; the cited paper is identified as covering active-site analysis and mutagenesis of Glu-176 and Glu-343.",
    "evidence_ids": ["C1", "C4", "C5", "C26", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence length rules out position 2056, and the unrelated activity labels may help reject some distractors, but the input gives no enzyme identity or functional context that establishes the catalytic role of residue 176.",
    "missing_item_specific_fact": "The protein-specific annotation or experimental characterization assigning residue 176 as the proton donor/acceptor is needed to select C.",
    "reason": "Knowing which exact residue performs this catalytic role requires an item-specific active-site assignment; it is not meaningfully derivable from the bare sequence and choices by general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports C among the listed choices; no other option is supported as the proton donor/acceptor for this sequence."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the input sequence, but the author's exact source snapshot is unknown.",
    "The database annotation cites a publication that includes structural work and mutagenesis, but the supplied evidence does not independently establish the paper's experimental results."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry I0AIT9 (Beta-1,2-glucosyltransferase, EC 2.4.1.391, Ignavibacterium album) explicitly annotates an Active site at position 176 with description 'Proton donor/acceptor' (evidence ECO:0000305|PubMed:35065074, corroborated by X-ray crystallography and mutagenesis of Glu-176 and Glu-343 in PDB structures 7VKX/7VKY). The sequence matches the benchmark sequence exactly (716 residues, SHA-256 match). The distractors are clearly wrong: position 2056 exceeds the 716-residue sequence; 'beta-ketoacyl synthase' and 'acyltransferase of LM' describe entirely different enzyme classes irrelevant to this glycosyltransferase.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C26](#evidence-c26), [H3](#evidence-h3), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option B (position 2056) can be eliminated by simple arithmetic since the sequence is only 716 residues long. However, distinguishing C from A and D requires knowing that this protein is a glycosyltransferase (EC 2.4.1.391) rather than a beta-ketoacyl synthase or acyltransferase. Identifying the protein's function from a 716-residue sequence without database access is not feasible through general reasoning; recognizing GT-B fold motifs from sequence alone does not yield the specific catalytic residue at position 176. The precise assignment of Glu-176 as proton donor/acceptor was determined experimentally via X-ray crystallography and site-directed mutagenesis (PubMed 35065074).


**Missing item-specific fact**

> The identity of the protein as a beta-1,2-glucosyltransferase (EC 2.4.1.391) and the experimentally determined annotation that Glu-176 serves as the proton donor/acceptor in the catalytic mechanism. Without this item-specific knowledge, the functional descriptions in options A and D cannot be ruled out, and the specific position 176 cannot be identified from sequence alone.


**Reason**

> While B is eliminable by arithmetic (position exceeds sequence length), the discrimination among A, C, and D hinges on knowing the protein's actual enzymatic class and the experimentally determined active-site residue. This is a protein-specific annotation derived from a 2022 crystallographic/mutagenesis study, not derivable from general biological reasoning applied to the raw sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The UniProt entry annotates two active sites (position 176 as proton donor/acceptor and position 343 as nucleophile), but only position 176 appears among the options. The other three options reference entirely different enzyme classes or an impossible position, leaving no genuine ambiguity among the provided choices.


### Important caveats

- The UniProt annotation for position 176 carries evidence code ECO:0000305 (inferred from direct assay / published experiment), supported by X-ray crystallography (PDB 7VKX, 7VKY) and mutagenesis of Glu-176 and Glu-343. This is experimental evidence, not mere computational prediction.
- The entry was first publicly released 2025-04-09; the author's data-construction snapshot is unknown. Sequence match is confirmed across historical (entry v55) and current (v57) versions.
- The protein also has a second annotated active site (position 343, Nucleophile), which is not offered as a choice; the question's phrasing 'the enzyme's catalytic center' could in principle encompass both sites, but the answer options constrain the task to selecting among the four given choices.
- The identity of the protein (accession I0AIT9) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option B (position 2056) can be eliminated by simple arithmetic since the sequence is only 716 residues long. However, distinguishing C from A and D requires knowing that this protein is a glycosyltransferase (EC 2.4.1.391) rather than a beta-ketoacyl synthase or acyltransferase. Identifying the protein's function from a 716-residue sequence without database access is not feasible through general reasoning; recognizing GT-B fold motifs from sequence alone does not yield the specific catalytic residue at position 176. The precise assignment of Glu-176 as proton donor/acceptor was determined experimentally via X-ray crystallography and site-directed mutagenesis (PubMed 35065074).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of the protein as a beta-1,2-glucosyltransferase (EC 2.4.1.391) and the experimentally determined annotation that Glu-176 serves as the proton donor/acceptor in the catalytic mechanism. Without this item-specific knowledge, the functional descriptions in options A and D cannot be ruled out, and the specific position 176 cannot be identified from sequence alone.",
    "reason": "While B is eliminable by arithmetic (position exceeds sequence length), the discrimination among A, C, and D hinges on knowing the protein's actual enzymatic class and the experimentally determined active-site residue. This is a protein-specific annotation derived from a 2022 crystallographic/mutagenesis study, not derivable from general biological reasoning applied to the raw sequence."
  },
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C26",
      "H3",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry I0AIT9 (Beta-1,2-glucosyltransferase, EC 2.4.1.391, Ignavibacterium album) explicitly annotates an Active site at position 176 with description 'Proton donor/acceptor' (evidence ECO:0000305|PubMed:35065074, corroborated by X-ray crystallography and mutagenesis of Glu-176 and Glu-343 in PDB structures 7VKX/7VKY). The sequence matches the benchmark sequence exactly (716 residues, SHA-256 match). The distractors are clearly wrong: position 2056 exceeds the 716-residue sequence; 'beta-ketoacyl synthase' and 'acyltransferase of LM' describe entirely different enzyme classes irrelevant to this glycosyltransferase."
  },
  "important_caveats": [
    "The UniProt annotation for position 176 carries evidence code ECO:0000305 (inferred from direct assay / published experiment), supported by X-ray crystallography (PDB 7VKX, 7VKY) and mutagenesis of Glu-176 and Glu-343. This is experimental evidence, not mere computational prediction.",
    "The entry was first publicly released 2025-04-09; the author's data-construction snapshot is unknown. Sequence match is confirmed across historical (entry v55) and current (v57) versions.",
    "The protein also has a second annotated active site (position 343, Nucleophile), which is not offered as a choice; the question's phrasing 'the enzyme's catalytic center' could in principle encompass both sites, but the answer options constrain the task to selecting among the four given choices.",
    "The identity of the protein (accession I0AIT9) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry annotates two active sites (position 176 as proton donor/acceptor and position 343 as nucleophile), but only position 176 appears among the options. The other three options reference entirely different enzyme classes or an impossible position, leaving no genuine ambiguity among the provided choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0093",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry I0AIT9 (Beta-1,2-glucosyltransferase, EC 2.4.1.391, Ignavibacterium album) explicitly annotates an Active site at position 176 with description 'Proton donor/acceptor' (evidence ECO:0000305|PubMed:35065074, corroborated by X-ray crystallography and mutagenesis of Glu-176 and Glu-343 in PDB structures 7VKX/7VKY). The sequence matches the benchmark sequence exactly (716 residues, SHA-256 match). The distractors are clearly wrong: position 2056 exceeds the 716-residue sequence; 'beta-ketoacyl synthase' and 'acyltransferase of LM' describe entirely different enzyme classes irrelevant to this glycosyltransferase.",
    "evidence_ids": ["C5", "C6", "C26", "H3", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Option B (position 2056) can be eliminated by simple arithmetic since the sequence is only 716 residues long. However, distinguishing C from A and D requires knowing that this protein is a glycosyltransferase (EC 2.4.1.391) rather than a beta-ketoacyl synthase or acyltransferase. Identifying the protein's function from a 716-residue sequence without database access is not feasible through general reasoning; recognizing GT-B fold motifs from sequence alone does not yield the specific catalytic residue at position 176. The precise assignment of Glu-176 as proton donor/acceptor was determined experimentally via X-ray crystallography and site-directed mutagenesis (PubMed 35065074).",
    "missing_item_specific_fact": "The identity of the protein as a beta-1,2-glucosyltransferase (EC 2.4.1.391) and the experimentally determined annotation that Glu-176 serves as the proton donor/acceptor in the catalytic mechanism. Without this item-specific knowledge, the functional descriptions in options A and D cannot be ruled out, and the specific position 176 cannot be identified from sequence alone.",
    "reason": "While B is eliminable by arithmetic (position exceeds sequence length), the discrimination among A, C, and D hinges on knowing the protein's actual enzymatic class and the experimentally determined active-site residue. This is a protein-specific annotation derived from a 2022 crystallographic/mutagenesis study, not derivable from general biological reasoning applied to the raw sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry annotates two active sites (position 176 as proton donor/acceptor and position 343 as nucleophile), but only position 176 appears among the options. The other three options reference entirely different enzyme classes or an impossible position, leaving no genuine ambiguity among the provided choices."
  },
  "important_caveats": [
    "The UniProt annotation for position 176 carries evidence code ECO:0000305 (inferred from direct assay / published experiment), supported by X-ray crystallography (PDB 7VKX, 7VKY) and mutagenesis of Glu-176 and Glu-343. This is experimental evidence, not mere computational prediction.",
    "The entry was first publicly released 2025-04-09; the author's data-construction snapshot is unknown. Sequence match is confirmed across historical (entry v55) and current (v57) versions.",
    "The protein also has a second annotated active site (position 343, Nucleophile), which is not offered as a choice; the question's phrasing 'the enzyme's catalytic center' could in principle encompass both sites, but the answer options constrain the task to selecting among the four given choices.",
    "The identity of the protein (accession I0AIT9) was inferred by the reviewer from dataset metadata and was not provided to the evaluated model."
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
**Locator:** `/features/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"description":"Proton donor/acceptor","evidences":[{"evidenceCode":"ECO:0000305","id":"35065074","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":176},"start":{"modifier":"EXACT","value":176}},"type":"Active site"}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/features/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"description":"Nucleophile","evidences":[{"evidenceCode":"ECO:0000305","id":"35065074","source":"PubMed"}],"location":{"end":{"modifier":"EXACT","value":343},"start":{"modifier":"EXACT","value":343}},"type":"Active site"}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence C26

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:10.515356+00:00.  

```json
{"citation":{"authors":["Kobayashi K.","Shimizu H.","Tanaka N.","Kuramochi K.","Nakai H.","Nakajima M.","Taguchi H."],"citationCrossReferences":[{"database":"PubMed","id":"35065074"},{"database":"DOI","id":"10.1016/j.jbc.2022.101606"}],"citationType":"journal article","firstPage":"101606","id":"35065074","journal":"J. Biol. Chem.","lastPage":"101606","publicationDate":"2022","title":"Characterization and structural analyses of a novel glycosyltransferase acting on the beta-1,2-glucosidic linkages.","volume":"298"},"evidences":[{"evidenceCode":"ECO:0007744","id":"7VKW","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKX","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKY","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VKZ","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL0","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL1","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL2","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL3","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL4","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL5","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"7VL6","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE; SOPHOROSE AND ALTERNATIVE SUBSTRATES","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","ACTIVE SITE","MUTAGENESIS OF GLU-176 AND GLU-343"]}
```

Source SHA-256: `0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032`.

### Evidence H2

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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 159-161`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
FT   ACT_SITE        176
FT                   /note="Proton donor/acceptor"
FT                   /evidence="ECO:0000305|PubMed:35065074"
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)  
**Locator:** `lines 162-164`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:09.687306+00:00.  

```text
FT   ACT_SITE        343
FT                   /note="Nucleophile"
FT                   /evidence="ECO:0000305|PubMed:35065074"
```

Source SHA-256: `5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 93. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
