# EC_number_0100

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 2.1.1.348

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | invalid_review |

**Paired comparison:** not comparable: one or both reviews invalid or missing. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTAATLFESTDGTVVLLDLPRSIEDAQQHPAAVTLPEAPSLVTNSCRDGTSWTRRLISSPPPETPFVTPEPKNGPSPLPAAAQVAQLMIQASVTGALEELRTNYSGPYLLPRQLSPQRMIADGGKAVDDYKSPHACDLESCSTTAEDATKGRYYFPPESHHVLGTIQETKTLLLQSAPNFNVIVLDPPWPNRSAKRKKGGYKVATTTDDIRALLSDVPIPSLLARDGLVAIWVTNKPAFLDMLTSPRDGILSEWGLELVGEWSWLKITTSAEPILPIDSAHRKPWEPLLIAQRKGSKRVFPPFWRRRVIVSVPDTHSRKPNIRDLVNPMLPPRSRGLEIFARNLTAGWWAWGDDVLHFQERSNWVMAESKSPATGC

[Multiple Choices]
A. 2.1.1.395
B. 3.1.3.112
C. 2.1.1.348
D. 3.2.1.183
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

> The supplied sequence matches the annotated MTA1 protein. UniProt assigns it EC 2.1.1.348 and records the corresponding mRNA adenosine N6-methylation reaction with experimental evidence codes citing publications. This supports choice C, while the excerpts do not independently validate the underlying experiments.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support a broad inference of methyltransferase activity, but it does not by itself establish the specific substrate and reaction needed to distinguish EC 2.1.1.348 from another methyltransferase option.


**Missing item-specific fact**

> The protein-specific annotation or experimental finding that this protein methylates adenosine at N6 in mRNA.


**Reason**

> The exact EC assignment depends on substrate and reaction specificity absent from the prompt. Recognizing the sequence or retrieving its database annotation would provide that missing fact, but would be lookup rather than reasoning from the supplied input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices specify distinct EC numbers, and the matched-sequence annotation supports C; no alternative is supported by the supplied reviewer evidence.


### Important caveats

- The UniProt sequence match and experimental evidence cited in the annotation are reviewer-only information, not information supplied to the evaluated model.
- The exact author-side source snapshot is unknown; the archived annotation available by the stated historical cutoff also matches the sequence and assigns EC 2.1.1.348.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support a broad inference of methyltransferase activity, but it does not by itself establish the specific substrate and reaction needed to distinguish EC 2.1.1.348 from another methyltransferase option.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific annotation or experimental finding that this protein methylates adenosine at N6 in mRNA.",
    "reason": "The exact EC assignment depends on substrate and reaction specificity absent from the prompt. Recognizing the sequence or retrieving its database annotation would provide that missing fact, but would be lookup rather than reasoning from the supplied input."
  },
  "case_id": "EC_number_0100",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated MTA1 protein. UniProt assigns it EC 2.1.1.348 and records the corresponding mRNA adenosine N6-methylation reaction with experimental evidence codes citing publications. This supports choice C, while the excerpts do not independently validate the underlying experiments."
  },
  "important_caveats": [
    "The UniProt sequence match and experimental evidence cited in the annotation are reviewer-only information, not information supplied to the evaluated model.",
    "The exact author-side source snapshot is unknown; the archived annotation available by the stated historical cutoff also matches the sequence and assigns EC 2.1.1.348."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct EC numbers, and the matched-sequence annotation supports C; no alternative is supported by the supplied reviewer evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence matches the annotated MTA1 protein. UniProt assigns it EC 2.1.1.348 and records the corresponding mRNA adenosine N6-methylation reaction with experimental evidence codes citing publications. This supports choice C, while the excerpts do not independently validate the underlying experiments.",
    "evidence_ids": ["C1", "C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support a broad inference of methyltransferase activity, but it does not by itself establish the specific substrate and reaction needed to distinguish EC 2.1.1.348 from another methyltransferase option.",
    "missing_item_specific_fact": "The protein-specific annotation or experimental finding that this protein methylates adenosine at N6 in mRNA.",
    "reason": "The exact EC assignment depends on substrate and reaction specificity absent from the prompt. Recognizing the sequence or retrieving its database annotation would provide that missing fact, but would be lookup rather than reasoning from the supplied input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct EC numbers, and the matched-sequence annotation supports C; no alternative is supported by the supplied reviewer evidence."
  },
  "important_caveats": [
    "The UniProt sequence match and experimental evidence cited in the annotation are reviewer-only information, not information supplied to the evaluated model.",
    "The exact author-side source snapshot is unknown; the archived annotation available by the stated historical cutoff also matches the sequence and assigns EC 2.1.1.348."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `invalid_review`.

**This result is not a valid structured review.** Any saved labels below remain the model’s original values; they are excluded from label distributions and paired agreement. No field or option ID has been repaired.

**Validation errors:** `question_ambiguity:invalid_option_ids`.

### Expected-answer support: supported

> The UniProt entry G4MSY9 (MTA1_PYRO7) matches the supplied 376-aa sequence exactly (SHA256 confirmed). The entry assigns EC 2.1.1.348 (N6-methyladenosine RNA methyltransferase MTA1) with experimental evidence codes ECO:0000269 from two independent publications (PubMed:30535195, 2019 FEMS Microbiol Lett; PubMed:35338654, 2022 New Phytol). The catalytic activity (adenosine in mRNA + SAM → N6-methyladenosine in mRNA + SAH + H+) is experimentally validated. The expected answer C (2.1.1.348) is directly and experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices span two EC top-level classes: transferases (2.1.1.348 and 2.1.1.395) versus hydrolases (3.1.3.112 and 3.2.1.183). In principle, one might attempt to eliminate hydrolases by noting the absence of canonical phosphatase or glycosidase catalytic motifs in the sequence. However, distinguishing between the two methyltransferase options (A: 2.1.1.395 vs C: 2.1.1.348) requires knowing the specific substrate (mRNA adenosine for m6A methylation) and the precise enzyme identity (MTA1/IME4 homolog). No obvious, universally recognized catalytic motif in the raw 376-aa sequence uniquely identifies this as an m6A writer rather than another 2.1.1.x methyltransferase. The protein name 'MTA1' is not provided in the input.


**Missing item-specific fact**

> The specific identity of the protein as MTA1 (an m6A RNA methyltransferase) and the distinction between its exact EC number (2.1.1.348) and the other methyltransferase EC number offered (2.1.1.395). This requires either recognition of the exact sequence or knowledge of the specific enzyme's substrate specificity, neither of which is derivable from general biological reasoning on the raw sequence alone.


**Reason**

> While the broad class (transferase vs hydrolase) might be partially inferable from sequence features, the critical discrimination between 2.1.1.348 and 2.1.1.395 depends on knowing the exact enzyme identity and its specific substrate (mRNA adenosine N6-methylation). This is an item-specific annotation fact not derivable from the sequence by general reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A (2.1.1.395)",
  "C (2.1.1.348)"
]
```

> Both options A and C belong to EC class 2.1.1.x (methyltransferases). Without the protein name, organism context, or a recognizable catalytic motif unique to m6A writers, a solver cannot definitively distinguish between these two methyltransferase EC numbers from the raw sequence. The two hydrolase options (B and D) are in a different top-level class and are more readily eliminable, but the transferase pair remains ambiguous without specific knowledge.


### Important caveats

- The UniProt annotation for EC 2.1.1.348 is supported by experimental evidence (ECO:0000269) from two independent publications, not merely by computational prediction.
- The sequence match is exact (SHA256 identical) between the benchmark input and UniProt G4MSY9.
- The entry was first publicly released in April 2025; the author's source snapshot date is unknown, so the annotation may not have been available at benchmark construction time.
- The identity of EC 2.1.1.395 (option A) was not independently verified in the reviewer evidence; it is assumed to be a valid but different methyltransferase EC number.
- Reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices span two EC top-level classes: transferases (2.1.1.348 and 2.1.1.395) versus hydrolases (3.1.3.112 and 3.2.1.183). In principle, one might attempt to eliminate hydrolases by noting the absence of canonical phosphatase or glycosidase catalytic motifs in the sequence. However, distinguishing between the two methyltransferase options (A: 2.1.1.395 vs C: 2.1.1.348) requires knowing the specific substrate (mRNA adenosine for m6A methylation) and the precise enzyme identity (MTA1/IME4 homolog). No obvious, universally recognized catalytic motif in the raw 376-aa sequence uniquely identifies this as an m6A writer rather than another 2.1.1.x methyltransferase. The protein name 'MTA1' is not provided in the input.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of the protein as MTA1 (an m6A RNA methyltransferase) and the distinction between its exact EC number (2.1.1.348) and the other methyltransferase EC number offered (2.1.1.395). This requires either recognition of the exact sequence or knowledge of the specific enzyme's substrate specificity, neither of which is derivable from general biological reasoning on the raw sequence alone.",
    "reason": "While the broad class (transferase vs hydrolase) might be partially inferable from sequence features, the critical discrimination between 2.1.1.348 and 2.1.1.395 depends on knowing the exact enzyme identity and its specific substrate (mRNA adenosine N6-methylation). This is an item-specific annotation fact not derivable from the sequence by general reasoning."
  },
  "case_id": "EC_number_0100",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G4MSY9 (MTA1_PYRO7) matches the supplied 376-aa sequence exactly (SHA256 confirmed). The entry assigns EC 2.1.1.348 (N6-methyladenosine RNA methyltransferase MTA1) with experimental evidence codes ECO:0000269 from two independent publications (PubMed:30535195, 2019 FEMS Microbiol Lett; PubMed:35338654, 2022 New Phytol). The catalytic activity (adenosine in mRNA + SAM → N6-methyladenosine in mRNA + SAH + H+) is experimentally validated. The expected answer C (2.1.1.348) is directly and experimentally supported."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.1.1.348 is supported by experimental evidence (ECO:0000269) from two independent publications, not merely by computational prediction.",
    "The sequence match is exact (SHA256 identical) between the benchmark input and UniProt G4MSY9.",
    "The entry was first publicly released in April 2025; the author's source snapshot date is unknown, so the annotation may not have been available at benchmark construction time.",
    "The identity of EC 2.1.1.395 (option A) was not independently verified in the reviewer evidence; it is assumed to be a valid but different methyltransferase EC number.",
    "Reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A (2.1.1.395)",
      "C (2.1.1.348)"
    ],
    "reason": "Both options A and C belong to EC class 2.1.1.x (methyltransferases). Without the protein name, organism context, or a recognizable catalytic motif unique to m6A writers, a solver cannot definitively distinguish between these two methyltransferase EC numbers from the raw sequence. The two hydrolase options (B and D) are in a different top-level class and are more readily eliminable, but the transferase pair remains ambiguous without specific knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0100",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G4MSY9 (MTA1_PYRO7) matches the supplied 376-aa sequence exactly (SHA256 confirmed). The entry assigns EC 2.1.1.348 (N6-methyladenosine RNA methyltransferase MTA1) with experimental evidence codes ECO:0000269 from two independent publications (PubMed:30535195, 2019 FEMS Microbiol Lett; PubMed:35338654, 2022 New Phytol). The catalytic activity (adenosine in mRNA + SAM → N6-methyladenosine in mRNA + SAH + H+) is experimentally validated. The expected answer C (2.1.1.348) is directly and experimentally supported.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices span two EC top-level classes: transferases (2.1.1.348 and 2.1.1.395) versus hydrolases (3.1.3.112 and 3.2.1.183). In principle, one might attempt to eliminate hydrolases by noting the absence of canonical phosphatase or glycosidase catalytic motifs in the sequence. However, distinguishing between the two methyltransferase options (A: 2.1.1.395 vs C: 2.1.1.348) requires knowing the specific substrate (mRNA adenosine for m6A methylation) and the precise enzyme identity (MTA1/IME4 homolog). No obvious, universally recognized catalytic motif in the raw 376-aa sequence uniquely identifies this as an m6A writer rather than another 2.1.1.x methyltransferase. The protein name 'MTA1' is not provided in the input.",
    "missing_item_specific_fact": "The specific identity of the protein as MTA1 (an m6A RNA methyltransferase) and the distinction between its exact EC number (2.1.1.348) and the other methyltransferase EC number offered (2.1.1.395). This requires either recognition of the exact sequence or knowledge of the specific enzyme's substrate specificity, neither of which is derivable from general biological reasoning on the raw sequence alone.",
    "reason": "While the broad class (transferase vs hydrolase) might be partially inferable from sequence features, the critical discrimination between 2.1.1.348 and 2.1.1.395 depends on knowing the exact enzyme identity and its specific substrate (mRNA adenosine N6-methylation). This is an item-specific annotation fact not derivable from the sequence by general reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A (2.1.1.395)", "C (2.1.1.348)"],
    "reason": "Both options A and C belong to EC class 2.1.1.x (methyltransferases). Without the protein name, organism context, or a recognizable catalytic motif unique to m6A writers, a solver cannot definitively distinguish between these two methyltransferase EC numbers from the raw sequence. The two hydrolase options (B and D) are in a different top-level class and are more readily eliminable, but the transferase pair remains ambiguous without specific knowledge."
  },
  "important_caveats": [
    "The UniProt annotation for EC 2.1.1.348 is supported by experimental evidence (ECO:0000269) from two independent publications, not merely by computational prediction.",
    "The sequence match is exact (SHA256 identical) between the benchmark input and UniProt G4MSY9.",
    "The entry was first publicly released in April 2025; the author's source snapshot date is unknown, so the annotation may not have been available at benchmark construction time.",
    "The identity of EC 2.1.1.395 (option A) was not independently verified in the reviewer evidence; it is assumed to be a valid but different methyltransferase EC number.",
    "Reviewer-only evidence (UniProt accession, annotation) was not available to the evaluated model."
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

**Accession:** `G4MSY9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 55. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:07.225373+00:00.  

```json
"G4MSY9"
```

Source SHA-256: `af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:07.225373+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"M6A writer MTA1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"35338654","source":"PubMed"}],"value":"2.1.1.348"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"35338654","source":"PubMed"}],"value":"N6-methyladenosine RNA methyltransferase MTA1"}}}
```

Source SHA-256: `af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:07.225373+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"30535195","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"35338654","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:55585"}}],"reaction":{"ecNumber":"2.1.1.348","evidences":[{"evidenceCode":"ECO:0000269","id":"30535195","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"35338654","source":"PubMed"}],"name":"an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:55584"},{"database":"Rhea","id":"RHEA-COMP:12414"},{"database":"Rhea","id":"RHEA-COMP:12417"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:74411"},{"database":"ChEBI","id":"CHEBI:74449"}]}}
```

Source SHA-256: `af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:07.225373+00:00.  

```json
{"citation":{"authors":["Shi Y.","Wang H.","Wang J.","Liu X.","Lin F.","Lu J."],"citationCrossReferences":[{"database":"PubMed","id":"30535195"},{"database":"DOI","id":"10.1093/femsle/fny286"}],"citationType":"journal article","firstPage":"0","id":"30535195","journal":"FEMS Microbiol. Lett.","lastPage":"0","publicationDate":"2019","title":"N6-methyladenosine RNA methylation is involved in virulence of the rice blast fungus Pyricularia oryzae (syn. Magnaporthe oryzae).","volume":"366"},"referenceNumber":2,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G4MSY9.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:07.225373+00:00.  

```json
{"citation":{"authors":["Ren Z.","Tang B.","Xing J.","Liu C.","Cai X.","Hendy A.","Kamran M.","Liu H.","Zheng L.","Huang J.","Chen X.L."],"citationCrossReferences":[{"database":"PubMed","id":"35338654"},{"database":"DOI","id":"10.1111/nph.18117"}],"citationType":"journal article","firstPage":"247","id":"35338654","journal":"New Phytol.","lastPage":"262","publicationDate":"2022","title":"MTA1-mediated RNA m6 A modification regulates autophagy and is required for infection of the rice blast fungus.","volume":"235"},"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `af5f7ddb5dd26192f049b7c05939301c3519f53a3079b4c9594790fa73a52834`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:05.307350+00:00.  

```text
DE   RecName: Full=N6-methyladenosine RNA methyltransferase MTA1 {ECO:0000303|PubMed:35338654};
DE            EC=2.1.1.348 {ECO:0000269|PubMed:35338654};
DE   AltName: Full=M6A writer MTA1 {ECO:0000305};
```

Source SHA-256: `b275ec7910713716d97392bf383b7660d72ce4671194eb9bcfb8eaa327534aaa`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G4MSY9?format=txt&versions=55)  
**Locator:** `lines 55-63`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 55 / 1.  
**Retrieved:** 2026-11-01T06:28:05.307350+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an adenosine in mRNA + S-adenosyl-L-methionine = an N(6)-
CC         methyladenosine in mRNA + S-adenosyl-L-homocysteine + H(+);
CC         Xref=Rhea:RHEA:55584, Rhea:RHEA-COMP:12414, Rhea:RHEA-COMP:12417,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:74411, ChEBI:CHEBI:74449; EC=2.1.1.348;
CC         Evidence={ECO:0000269|PubMed:30535195, ECO:0000269|PubMed:35338654};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:55585;
CC         Evidence={ECO:0000269|PubMed:30535195, ECO:0000269|PubMed:35338654};
```

Source SHA-256: `b275ec7910713716d97392bf383b7660d72ce4671194eb9bcfb8eaa327534aaa`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 100. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
