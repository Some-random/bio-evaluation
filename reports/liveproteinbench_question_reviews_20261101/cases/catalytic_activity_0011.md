# catalytic_activity_0011

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides.

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MRFSVFTAAIAAAFSACCATASPAVNYVNSLILQRADPHIVKHTDGWYYFTATVPEYDRIVLRRAQTIQGLQSAPETVIWRRKAFGVGSGQVWAPELHYIDGRWYIYVALGVSGQWRIRAFVLEGVGANPLTASWTEKGIIQTNWDTFSLDATTFVANGTRYLVWAQQDPSRNGENSSLFIAPLQNPWTIRGPAVAISHPDLSWERIGYKVNEGPAVIQRNGRIFLTYSASATDHNYCMGLLTARADANLMNPASWVKSQQPIFVSNAATNQWGPGHNQFTVSEDGLSDILVYHDRGYRDINGDPLNDPNRRTRVQKLYWRDDGTPDFGIPVPDGPTPVRLRVAANGASSNGAYVRFYTTTGSGNLTGTAALPDTQFKLVSPGLSGGDSVSLESTSNPGTYVRRVSGSTAVQFERGTALNTAALRASASFRRVPGLSDSGGAVSFESVESPGQYLRLDPNGRLSVASVAEGTQGRSTFYLE

[Multiple Choices]
A. deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose
B. Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides.
C. UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-mannosamine
D. ipecoside + H2O = ipecoside aglycone + D-glucose
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

> The sequence matches the UniProt entry for this protein, which identifies it as alpha-L-arabinofuranosidase 43 and assigns the exact reaction in choice B. The catalytic-activity annotation cites experimental evidence (ECO:0000269) and a biochemical characterization paper.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a secreted fungal enzyme, but that broad context does not establish which specific glycosidic bond or substrate it acts on. It does not meaningfully distinguish choice B from the other enzyme reactions.


**Missing item-specific fact**

> The protein-specific catalytic annotation or experimental substrate-activity characterization identifying this sequence as an alpha-L-arabinofuranosidase.


**Reason**

> Selecting B requires knowing the function of this particular protein; the supplied sequence and choices alone provide no sufficiently discriminating biological argument.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cited catalytic-activity annotation matches choice B specifically; the other choices describe different reactions.


### Important caveats

- The supporting UniProt evidence is reviewer-only and was not supplied to the evaluated model.
- The sequence match establishes applicability of the annotation to the supplied sequence, but the underlying primary paper was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a secreted fungal enzyme, but that broad context does not establish which specific glycosidic bond or substrate it acts on. It does not meaningfully distinguish choice B from the other enzyme reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental substrate-activity characterization identifying this sequence as an alpha-L-arabinofuranosidase.",
    "reason": "Selecting B requires knowing the function of this particular protein; the supplied sequence and choices alone provide no sufficiently discriminating biological argument."
  },
  "case_id": "catalytic_activity_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for this protein, which identifies it as alpha-L-arabinofuranosidase 43 and assigns the exact reaction in choice B. The catalytic-activity annotation cites experimental evidence (ECO:0000269) and a biochemical characterization paper."
  },
  "important_caveats": [
    "The supporting UniProt evidence is reviewer-only and was not supplied to the evaluated model.",
    "The sequence match establishes applicability of the annotation to the supplied sequence, but the underlying primary paper was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited catalytic-activity annotation matches choice B specifically; the other choices describe different reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for this protein, which identifies it as alpha-L-arabinofuranosidase 43 and assigns the exact reaction in choice B. The catalytic-activity annotation cites experimental evidence (ECO:0000269) and a biochemical characterization paper.",
    "evidence_ids": ["C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a secreted fungal enzyme, but that broad context does not establish which specific glycosidic bond or substrate it acts on. It does not meaningfully distinguish choice B from the other enzyme reactions.",
    "missing_item_specific_fact": "The protein-specific catalytic annotation or experimental substrate-activity characterization identifying this sequence as an alpha-L-arabinofuranosidase.",
    "reason": "Selecting B requires knowing the function of this particular protein; the supplied sequence and choices alone provide no sufficiently discriminating biological argument."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cited catalytic-activity annotation matches choice B specifically; the other choices describe different reactions."
  },
  "important_caveats": [
    "The supporting UniProt evidence is reviewer-only and was not supplied to the evaluated model.",
    "The sequence match establishes applicability of the annotation to the supplied sequence, but the underlying primary paper was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0F6NRE2 (sequence SHA256 matches exactly) is annotated as Alpha-L-arabinofuranosidase 43, EC 3.2.1.55, with catalytic activity 'Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides.' The annotation is backed by experimental evidence (ECO:0000269, PubMed:25432346 — a 2015 biochemical characterization paper reporting FUNCTION, CATALYTIC ACTIVITY, and SUBSTRATE SPECIFICITY). The expected answer B matches the UniProt catalytic activity comment verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Option C (epimerase reaction) can be eliminated by general reasoning since it is an isomerization, not a hydrolysis, and the protein has a signal peptide suggesting a secreted hydrolase. However, distinguishing option B (alpha-L-arabinofuranosidase, GH43 family, beta-propeller fold) from options A/D (beta-glucosidase, GH1/GH3 families, TIM-barrel fold) from primary sequence alone requires identifying the specific glycoside hydrolase family and its substrate specificity. The linear sequence does not contain an obvious, universally-recognized motif that unambiguously separates a GH43 arabinofuranosidase from a GH1/GH3 glucosidase without specialized family-motif knowledge or database search.


**Missing item-specific fact**

> The specific GH family assignment (GH43 vs GH1/GH3) and the experimentally determined substrate preference (alpha-L-arabinofuranoside vs beta-glucoside) for this particular protein. This is recorded in UniProt as EC 3.2.1.55 with experimental evidence from PubMed:25432346, but is not derivable from the linear sequence by general biological reasoning alone.


**Reason**

> While a knowledgeable model might note the protein is a secreted fungal glycoside hydrolase (eliminating C), the critical choice between arabinofuranosidase (B) and glucosidase (A/D) depends on recognizing GH43-specific sequence signatures or recalling the database annotation. The sequence lacks a single, general-knowledge-derivable feature that cleanly separates these two enzyme classes without specialized family-level motif knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Option C is clearly eliminable (isomerization vs. hydrolysis). Options A and D are both beta-glucosidase activities differing only in substrate (deacetylipecoside vs. ipecoside); if the enzyme were a glucosidase, further specificity would be needed, but since the correct answer is an arabinofuranosidase, A and D are both wrong for the same fundamental reason (wrong sugar specificity). No two options are equally defensible given the experimental annotation.


### Important caveats

- The UniProt annotation is backed by direct experimental evidence (ECO:0000269), not merely computational inference, strengthening the key's validity.
- The sequence match is exact (SHA256 confirmed), so the annotation applies directly to the supplied sequence.
- Options A and D are near-duplicates differing only in substrate name; this redundancy slightly reduces the effective number of distinct choices but does not affect the correctness of B.
- The reviewer-only evidence was not available to the evaluated model; the model must rely solely on the 481-aa sequence and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Option C (epimerase reaction) can be eliminated by general reasoning since it is an isomerization, not a hydrolysis, and the protein has a signal peptide suggesting a secreted hydrolase. However, distinguishing option B (alpha-L-arabinofuranosidase, GH43 family, beta-propeller fold) from options A/D (beta-glucosidase, GH1/GH3 families, TIM-barrel fold) from primary sequence alone requires identifying the specific glycoside hydrolase family and its substrate specificity. The linear sequence does not contain an obvious, universally-recognized motif that unambiguously separates a GH43 arabinofuranosidase from a GH1/GH3 glucosidase without specialized family-motif knowledge or database search.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific GH family assignment (GH43 vs GH1/GH3) and the experimentally determined substrate preference (alpha-L-arabinofuranoside vs beta-glucoside) for this particular protein. This is recorded in UniProt as EC 3.2.1.55 with experimental evidence from PubMed:25432346, but is not derivable from the linear sequence by general biological reasoning alone.",
    "reason": "While a knowledgeable model might note the protein is a secreted fungal glycoside hydrolase (eliminating C), the critical choice between arabinofuranosidase (B) and glucosidase (A/D) depends on recognizing GH43-specific sequence signatures or recalling the database annotation. The sequence lacks a single, general-knowledge-derivable feature that cleanly separates these two enzyme classes without specialized family-level motif knowledge."
  },
  "case_id": "catalytic_activity_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F6NRE2 (sequence SHA256 matches exactly) is annotated as Alpha-L-arabinofuranosidase 43, EC 3.2.1.55, with catalytic activity 'Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides.' The annotation is backed by experimental evidence (ECO:0000269, PubMed:25432346 — a 2015 biochemical characterization paper reporting FUNCTION, CATALYTIC ACTIVITY, and SUBSTRATE SPECIFICITY). The expected answer B matches the UniProt catalytic activity comment verbatim."
  },
  "important_caveats": [
    "The UniProt annotation is backed by direct experimental evidence (ECO:0000269), not merely computational inference, strengthening the key's validity.",
    "The sequence match is exact (SHA256 confirmed), so the annotation applies directly to the supplied sequence.",
    "Options A and D are near-duplicates differing only in substrate name; this redundancy slightly reduces the effective number of distinct choices but does not affect the correctness of B.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely solely on the 481-aa sequence and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is clearly eliminable (isomerization vs. hydrolysis). Options A and D are both beta-glucosidase activities differing only in substrate (deacetylipecoside vs. ipecoside); if the enzyme were a glucosidase, further specificity would be needed, but since the correct answer is an arabinofuranosidase, A and D are both wrong for the same fundamental reason (wrong sugar specificity). No two options are equally defensible given the experimental annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F6NRE2 (sequence SHA256 matches exactly) is annotated as Alpha-L-arabinofuranosidase 43, EC 3.2.1.55, with catalytic activity 'Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides.' The annotation is backed by experimental evidence (ECO:0000269, PubMed:25432346 — a 2015 biochemical characterization paper reporting FUNCTION, CATALYTIC ACTIVITY, and SUBSTRATE SPECIFICITY). The expected answer B matches the UniProt catalytic activity comment verbatim.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Option C (epimerase reaction) can be eliminated by general reasoning since it is an isomerization, not a hydrolysis, and the protein has a signal peptide suggesting a secreted hydrolase. However, distinguishing option B (alpha-L-arabinofuranosidase, GH43 family, beta-propeller fold) from options A/D (beta-glucosidase, GH1/GH3 families, TIM-barrel fold) from primary sequence alone requires identifying the specific glycoside hydrolase family and its substrate specificity. The linear sequence does not contain an obvious, universally-recognized motif that unambiguously separates a GH43 arabinofuranosidase from a GH1/GH3 glucosidase without specialized family-motif knowledge or database search.",
    "missing_item_specific_fact": "The specific GH family assignment (GH43 vs GH1/GH3) and the experimentally determined substrate preference (alpha-L-arabinofuranoside vs beta-glucoside) for this particular protein. This is recorded in UniProt as EC 3.2.1.55 with experimental evidence from PubMed:25432346, but is not derivable from the linear sequence by general biological reasoning alone.",
    "reason": "While a knowledgeable model might note the protein is a secreted fungal glycoside hydrolase (eliminating C), the critical choice between arabinofuranosidase (B) and glucosidase (A/D) depends on recognizing GH43-specific sequence signatures or recalling the database annotation. The sequence lacks a single, general-knowledge-derivable feature that cleanly separates these two enzyme classes without specialized family-level motif knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Option C is clearly eliminable (isomerization vs. hydrolysis). Options A and D are both beta-glucosidase activities differing only in substrate (deacetylipecoside vs. ipecoside); if the enzyme were a glucosidase, further specificity would be needed, but since the correct answer is an arabinofuranosidase, A and D are both wrong for the same fundamental reason (wrong sugar specificity). No two options are equally defensible given the experimental annotation."
  },
  "important_caveats": [
    "The UniProt annotation is backed by direct experimental evidence (ECO:0000269), not merely computational inference, strengthening the key's validity.",
    "The sequence match is exact (SHA256 confirmed), so the annotation applies directly to the supplied sequence.",
    "Options A and D are near-duplicates differing only in substrate name; this redundancy slightly reduces the effective number of distinct choices but does not affect the correctness of B.",
    "The reviewer-only evidence was not available to the evaluated model; the model must rely solely on the 481-aa sequence and general biological knowledge."
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

**Accession:** `A0A0F6NRE2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 16. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6NRE2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.416033+00:00.  

```json
{"flag":"Precursor","recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"25432346","source":"PubMed"}],"value":"3.2.1.55"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"25432346","source":"PubMed"}],"value":"Alpha-L-arabinofuranosidase 43"}}}
```

Source SHA-256: `1e5d7a5da3b1ff99ca8b412999f2a1323097b0d9e9e57580eff71e52a00dd55d`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6NRE2.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.416033+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"3.2.1.55","evidences":[{"evidenceCode":"ECO:0000269","id":"25432346","source":"PubMed"}],"name":"Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside residues in alpha-L-arabinosides."}}
```

Source SHA-256: `1e5d7a5da3b1ff99ca8b412999f2a1323097b0d9e9e57580eff71e52a00dd55d`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F6NRE2.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:39.416033+00:00.  

```json
{"citation":{"authors":["Yang X.","Shi P.","Ma R.","Luo H.","Huang H.","Yang P.","Yao B."],"citationCrossReferences":[{"database":"PubMed","id":"25432346"},{"database":"DOI","id":"10.1007/s12010-014-1416-y"}],"citationType":"journal article","firstPage":"1960","id":"25432346","journal":"Appl. Biochem. Biotechnol.","lastPage":"1970","publicationDate":"2015","title":"A new GH43 alpha-arabinofuranosidase from Humicola insolens Y1: biochemical characterization and synergistic action with a xylanase on xylan degradation.","volume":"175"},"referenceComments":[{"type":"STRAIN","value":"Y1"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBSTRATE SPECIFICITY","ACTIVITY REGULATION","BIOTECHNOLOGY"]}
```

Source SHA-256: `1e5d7a5da3b1ff99ca8b412999f2a1323097b0d9e9e57580eff71e52a00dd55d`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6NRE2?format=txt&versions=16)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:19.078830+00:00.  

```text
DE   RecName: Full=Alpha-L-arabinofuranosidase 43 {ECO:0000303|PubMed:25432346};
DE            EC=3.2.1.55 {ECO:0000269|PubMed:25432346};
DE   Flags: Precursor;
```

Source SHA-256: `2af4853fef65af58c3afa6566598fc0146a0bf2f1579d5b2b0a183cc992d117c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6NRE2?format=txt&versions=16)  
**Locator:** `lines 14-24`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:19.078830+00:00.  

```text
RN   [1]
RP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBSTRATE SPECIFICITY, ACTIVITY REGULATION,
RP   AND BIOTECHNOLOGY.
RC   STRAIN=Y1;
RX   PubMed=25432346; DOI=10.1007/s12010-014-1416-y;
RA   Yang X., Shi P., Ma R., Luo H., Huang H., Yang P., Yao B.;
RT   "A new GH43 alpha-arabinofuranosidase from Humicola insolens Y1:
RT   biochemical characterization and synergistic action with a xylanase on
RT   xylan degradation.";
RL   Appl. Biochem. Biotechnol. 175:1960-1970(2015).
```

Source SHA-256: `2af4853fef65af58c3afa6566598fc0146a0bf2f1579d5b2b0a183cc992d117c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F6NRE2?format=txt&versions=16)  
**Locator:** `lines 29-32`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 16 / 1.  
**Retrieved:** 2026-11-01T06:27:19.078830+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=Hydrolysis of terminal non-reducing alpha-L-arabinofuranoside
CC         residues in alpha-L-arabinosides.; EC=3.2.1.55;
CC         Evidence={ECO:0000269|PubMed:25432346};
```

Source SHA-256: `2af4853fef65af58c3afa6566598fc0146a0bf2f1579d5b2b0a183cc992d117c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 11. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
