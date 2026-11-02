# catalytic_activity_0087

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **D** — 4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MSSTAPEDVARPLLALPAIEAFDAIVRGRRSVRSYADVQVPRRTVRDVLELAARAPSNSNVQPWHTYVLTGRHKRALTDSVLRYYDTIGRTVREFDYQPGPDGWEEPYKERRESFGEGLYGRALGLSLADVDDREFYHRRNYDFFAAPVGLIVTVARNPRLSALIDAGAYIQTILLSARSRGLSTCAQASFLDFHPAVRECLAIPTHRTIVCGISLGYEDAQHPIASNATTREPVDRHVTFLWDDDD

[Multiple Choices]
A. 3alpha(S)-strictosidine + H2O = strictosidine aglycone + D-glucose
B. L-galactose + NAD(+) = L-galactono-1,5-lactone + NADH + H(+)
C. 3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-glucuronate + alpha-D-glucose 1-phosphate
D. 4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The supplied sequence exactly matches the sequence in the UniProt entry annotated with reaction D. The catalytic-activity annotation cites experimental evidence (ECO:0000269) linked to PubMed 34554625; the archived entry available by the historical cutoff also records reaction D.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The options describe distinct enzyme chemistries, but the sequence alone offers no sufficiently specific, general argument for the particular 4-nitrobenzoate substrate and hydroxylaminobenzoate product in D. At most, sequence-based family recognition might suggest a broad enzyme class, not establish this precise reaction.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental substrate/product evidence identifying this enzyme as a 4-nitrobenzoate reductase.


**Reason**

> Distinguishing D requires protein-specific substrate specificity not supplied in the question. The matching annotation and its experimental evidence support the key for this audit, but they were reviewer-only information and do not make the answer inferable from the model input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices state chemically distinct reactions, and the sequence-matched annotation supports D; no alternative choice is supported by the supplied reviewer evidence.


### Important caveats

- The experimental-evidence designation is reported by UniProt and linked to the cited publication; the primary paper was not independently reviewed here.
- The actual author source snapshot is unknown, although a historical sequence-matched entry available by the stated cutoff contains the same reaction annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The options describe distinct enzyme chemistries, but the sequence alone offers no sufficiently specific, general argument for the particular 4-nitrobenzoate substrate and hydroxylaminobenzoate product in D. At most, sequence-based family recognition might suggest a broad enzyme class, not establish this precise reaction.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental substrate/product evidence identifying this enzyme as a 4-nitrobenzoate reductase.",
    "reason": "Distinguishing D requires protein-specific substrate specificity not supplied in the question. The matching annotation and its experimental evidence support the key for this audit, but they were reviewer-only information and do not make the answer inferable from the model input."
  },
  "case_id": "catalytic_activity_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the UniProt entry annotated with reaction D. The catalytic-activity annotation cites experimental evidence (ECO:0000269) linked to PubMed 34554625; the archived entry available by the historical cutoff also records reaction D."
  },
  "important_caveats": [
    "The experimental-evidence designation is reported by UniProt and linked to the cited publication; the primary paper was not independently reviewed here.",
    "The actual author source snapshot is unknown, although a historical sequence-matched entry available by the stated cutoff contains the same reaction annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices state chemically distinct reactions, and the sequence-matched annotation supports D; no alternative choice is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the sequence in the UniProt entry annotated with reaction D. The catalytic-activity annotation cites experimental evidence (ECO:0000269) linked to PubMed 34554625; the archived entry available by the historical cutoff also records reaction D.",
    "evidence_ids": ["C1", "C5", "C6", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The options describe distinct enzyme chemistries, but the sequence alone offers no sufficiently specific, general argument for the particular 4-nitrobenzoate substrate and hydroxylaminobenzoate product in D. At most, sequence-based family recognition might suggest a broad enzyme class, not establish this precise reaction.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental substrate/product evidence identifying this enzyme as a 4-nitrobenzoate reductase.",
    "reason": "Distinguishing D requires protein-specific substrate specificity not supplied in the question. The matching annotation and its experimental evidence support the key for this audit, but they were reviewer-only information and do not make the answer inferable from the model input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices state chemically distinct reactions, and the sequence-matched annotation supports D; no alternative choice is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The experimental-evidence designation is reported by UniProt and linked to the cited publication; the primary paper was not independently reviewed here.",
    "The actual author source snapshot is unknown, although a historical sequence-matched entry available by the stated cutoff contains the same reaction annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt P0DXG6 (247 AA, exact SHA-256 match). The UniProt entry annotates this protein as 4-nitrobenzoate reductase (EC 1.7.1.-) with the catalytic reaction '4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O' (RHEA:80195), supported by experimental evidence (ECO:0000269, PubMed:34554625, Cheng et al. 2021, Environ. Microbiol.). This matches choice D exactly.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The protein's small size (247 AA) is broadly consistent with a nitroreductase (typically 200–300 AA) and less consistent with the other options (strictosidine β-glucosidases, L-galactose dehydrogenases, and phosphorylases are typically 350–500+ AA). However, this size heuristic only weakly narrows the class to 'small oxidoreductase' and does not identify the specific substrate (4-nitrobenzoate) or the two-electron reduction product (4-hydroxylaminobenzoate). No canonical FMN-binding or NADPH-binding Rossmann motif (GxGxxG) is clearly identifiable in the sequence that would specifically point to 4-nitrobenzoate reductase over other small oxidoreductases.


**Missing item-specific fact**

> The specific substrate identity (4-nitrobenzoate) and product (4-hydroxylaminobenzoate) are item-specific annotations from the 2021 experimental characterization (PubMed:34554625). No general sequence motif or structural feature in the 247-aa sequence uniquely encodes 4-nitrobenzoate specificity versus, e.g., generic nitroaromatic reduction or other small-molecule oxidoreductase activity.


**Reason**

> While protein size weakly disfavors choices A, B, and C, identifying the precise substrate as 4-nitrobenzoate and the reaction stoichiometry (2 NADPH, 2 H+) requires knowledge of this particular enzyme's experimentally determined specificity. The sequence lacks a recognizable motif that would allow a model to deduce '4-nitrobenzoate' specifically through general biochemical reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The small size of the protein (247 AA) makes choices A (glycosidase), B (sugar dehydrogenase), and C (phosphorylase) less plausible on size grounds, and the other three reactions involve substrate classes (glycosides, sugars, phosphorylases) with no obvious sequence-level support. Among the four choices, D is the most defensible even with limited reasoning, though the specific substrate identification still requires lookup.


### Important caveats

- The UniProt entry P0DXG6 was first released in February 2025; the evaluated model's training cutoff is unknown, so this annotation may or may not have been available at training time.
- The evidence code ECO:0000269 indicates protein-level experimental evidence (from the 2021 Cheng et al. study), not purely computational prediction.
- The reviewer-only accession was inferred from dataset metadata; the evaluated model received only the raw sequence and choices.
- The EC number is listed as 1.7.1.- (unspecified sub-subclass), indicating the exact EC classification was not finalized at annotation time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein's small size (247 AA) is broadly consistent with a nitroreductase (typically 200–300 AA) and less consistent with the other options (strictosidine β-glucosidases, L-galactose dehydrogenases, and phosphorylases are typically 350–500+ AA). However, this size heuristic only weakly narrows the class to 'small oxidoreductase' and does not identify the specific substrate (4-nitrobenzoate) or the two-electron reduction product (4-hydroxylaminobenzoate). No canonical FMN-binding or NADPH-binding Rossmann motif (GxGxxG) is clearly identifiable in the sequence that would specifically point to 4-nitrobenzoate reductase over other small oxidoreductases.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (4-nitrobenzoate) and product (4-hydroxylaminobenzoate) are item-specific annotations from the 2021 experimental characterization (PubMed:34554625). No general sequence motif or structural feature in the 247-aa sequence uniquely encodes 4-nitrobenzoate specificity versus, e.g., generic nitroaromatic reduction or other small-molecule oxidoreductase activity.",
    "reason": "While protein size weakly disfavors choices A, B, and C, identifying the precise substrate as 4-nitrobenzoate and the reaction stoichiometry (2 NADPH, 2 H+) requires knowledge of this particular enzyme's experimentally determined specificity. The sequence lacks a recognizable motif that would allow a model to deduce '4-nitrobenzoate' specifically through general biochemical reasoning."
  },
  "case_id": "catalytic_activity_0087",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt P0DXG6 (247 AA, exact SHA-256 match). The UniProt entry annotates this protein as 4-nitrobenzoate reductase (EC 1.7.1.-) with the catalytic reaction '4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O' (RHEA:80195), supported by experimental evidence (ECO:0000269, PubMed:34554625, Cheng et al. 2021, Environ. Microbiol.). This matches choice D exactly."
  },
  "important_caveats": [
    "The UniProt entry P0DXG6 was first released in February 2025; the evaluated model's training cutoff is unknown, so this annotation may or may not have been available at training time.",
    "The evidence code ECO:0000269 indicates protein-level experimental evidence (from the 2021 Cheng et al. study), not purely computational prediction.",
    "The reviewer-only accession was inferred from dataset metadata; the evaluated model received only the raw sequence and choices.",
    "The EC number is listed as 1.7.1.- (unspecified sub-subclass), indicating the exact EC classification was not finalized at annotation time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The small size of the protein (247 AA) makes choices A (glycosidase), B (sugar dehydrogenase), and C (phosphorylase) less plausible on size grounds, and the other three reactions involve substrate classes (glycosides, sugars, phosphorylases) with no obvious sequence-level support. Among the four choices, D is the most defensible even with limited reasoning, though the specific substrate identification still requires lookup."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0087",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt P0DXG6 (247 AA, exact SHA-256 match). The UniProt entry annotates this protein as 4-nitrobenzoate reductase (EC 1.7.1.-) with the catalytic reaction '4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O' (RHEA:80195), supported by experimental evidence (ECO:0000269, PubMed:34554625, Cheng et al. 2021, Environ. Microbiol.). This matches choice D exactly.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The protein's small size (247 AA) is broadly consistent with a nitroreductase (typically 200–300 AA) and less consistent with the other options (strictosidine β-glucosidases, L-galactose dehydrogenases, and phosphorylases are typically 350–500+ AA). However, this size heuristic only weakly narrows the class to 'small oxidoreductase' and does not identify the specific substrate (4-nitrobenzoate) or the two-electron reduction product (4-hydroxylaminobenzoate). No canonical FMN-binding or NADPH-binding Rossmann motif (GxGxxG) is clearly identifiable in the sequence that would specifically point to 4-nitrobenzoate reductase over other small oxidoreductases.",
    "missing_item_specific_fact": "The specific substrate identity (4-nitrobenzoate) and product (4-hydroxylaminobenzoate) are item-specific annotations from the 2021 experimental characterization (PubMed:34554625). No general sequence motif or structural feature in the 247-aa sequence uniquely encodes 4-nitrobenzoate specificity versus, e.g., generic nitroaromatic reduction or other small-molecule oxidoreductase activity.",
    "reason": "While protein size weakly disfavors choices A, B, and C, identifying the precise substrate as 4-nitrobenzoate and the reaction stoichiometry (2 NADPH, 2 H+) requires knowledge of this particular enzyme's experimentally determined specificity. The sequence lacks a recognizable motif that would allow a model to deduce '4-nitrobenzoate' specifically through general biochemical reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The small size of the protein (247 AA) makes choices A (glycosidase), B (sugar dehydrogenase), and C (phosphorylase) less plausible on size grounds, and the other three reactions involve substrate classes (glycosides, sugars, phosphorylases) with no obvious sequence-level support. Among the four choices, D is the most defensible even with limited reasoning, though the specific substrate identification still requires lookup."
  },
  "important_caveats": [
    "The UniProt entry P0DXG6 was first released in February 2025; the evaluated model's training cutoff is unknown, so this annotation may or may not have been available at training time.",
    "The evidence code ECO:0000269 indicates protein-level experimental evidence (from the 2021 Cheng et al. study), not purely computational prediction.",
    "The reviewer-only accession was inferred from dataset metadata; the evaluated model received only the raw sequence and choices.",
    "The EC number is listed as 1.7.1.- (unspecified sub-subclass), indicating the exact EC classification was not finalized at annotation time."
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

**Accession:** `P0DXG6` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 3. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.531539+00:00.  

```json
"P0DXG6"
```

Source SHA-256: `adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.531539+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34554625","source":"PubMed"}],"value":"4-nitrobenzoate nitroreductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34554625","source":"PubMed"}],"value":"4-NBA nitroreductase"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"34554625","source":"PubMed"}],"value":"1.7.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"34554625","source":"PubMed"}],"value":"4-nitrobenzoate reductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"34554625","source":"PubMed"}],"value":"4-NBA reductase"}]}}
```

Source SHA-256: `adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.531539+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"34554625","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:80196"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000269","id":"34554625","source":"PubMed"}],"name":"4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate + 2 NADP(+) + H2O","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:80195"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:142863"},{"database":"ChEBI","id":"CHEBI:231457"}]}}
```

Source SHA-256: `adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXG6.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:26.531539+00:00.  

```json
{"citation":{"authors":["Cheng M.","Qian Y.","Xing Z.","Zylstra G.J.","Huang X."],"citationCrossReferences":[{"database":"PubMed","id":"34554625"},{"database":"DOI","id":"10.1111/1462-2920.15787"}],"citationType":"journal article","firstPage":"7028","id":"34554625","journal":"Environ. Microbiol.","lastPage":"7041","publicationDate":"2021","title":"The low-nanomolar 4-nitrobenzoate-responsive repressor PnbX negatively regulates the actinomycete-derived 4-nitrobenzoate-degrading pnb locus.","volume":"23"},"referenceComments":[{"type":"STRAIN","value":"LMS-CY"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [LARGE SCALE GENOMIC DNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","INDUCTION"]}
```

Source SHA-256: `adb8135fbe43dc6d05fa848fc357b229a5a07072499f7104d6191c232bd5c429`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:31.939265+00:00.  

```text
ID   PNBA_NOCS0              Reviewed;         247 AA.
AC   P0DXG6;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 3.
DE   RecName: Full=4-nitrobenzoate reductase {ECO:0000303|PubMed:34554625};
DE            Short=4-NBA reductase {ECO:0000303|PubMed:34554625};
DE            EC=1.7.1.- {ECO:0000269|PubMed:34554625};
DE   AltName: Full=4-nitrobenzoate nitroreductase {ECO:0000303|PubMed:34554625};
DE            Short=4-NBA nitroreductase {ECO:0000303|PubMed:34554625};
GN   Name=pnbA {ECO:0000303|PubMed:34554625};
GN   ORFNames=KM427_00695 {ECO:0000312|EMBL:QWF22307.1};
OS   Nocardioides sp. (strain LMS-CY).
OC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Propionibacteriales;
OC   Nocardioidaceae; Nocardioides.
OX   NCBI_TaxID=2840457;
```

Source SHA-256: `6bf7ac47ab7367bc964f268ea8c8b2cfa06e184e9dfb134015fe0af0dcebef36`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXG6?format=txt&versions=3)  
**Locator:** `lines 30-37`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 3 / 1.  
**Retrieved:** 2026-11-02T04:29:31.939265+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=4-nitrobenzoate + 2 NADPH + 2 H(+) = 4-hydroxylaminobenzoate +
CC         2 NADP(+) + H2O; Xref=Rhea:RHEA:80195, ChEBI:CHEBI:15377,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349,
CC         ChEBI:CHEBI:142863, ChEBI:CHEBI:231457;
CC         Evidence={ECO:0000269|PubMed:34554625};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80196;
CC         Evidence={ECO:0000269|PubMed:34554625};
```

Source SHA-256: `6bf7ac47ab7367bc964f268ea8c8b2cfa06e184e9dfb134015fe0af0dcebef36`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 87. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
