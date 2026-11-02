# EC_number_0079

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **C** — 5.1.3.14

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MVKKILIVFGTRPEAIKMAPLVKIMENRNDVNFRVCVTGQHRQMLDQILNIFDIKPDYDLNIMQENQDLYDITLKILCGMKNVLNDFKPNIVLVHGDTTTASVTALAAFYQKIKIAHVEAGLRTYNICNPWPEEANRQIIGVLANIHFTPTVKSAENLIKEGKNKEGIFITGNTVIDALFYMTEKIKNDKTFKIKVLSSIGNEYKINDNKKFILVTGHRRENFGEGFLQICEALKIIAINNPDIDIVYPVHLNPNVQKPVKMLLLNISNIYLINPLKYEEFIYLMSKSYFIITDSGGIQEEAPSLGKPILVMRETTERPEAVEAGVVKLVGACKQNIIRESQKLIDDQDEYEKMSKAYNPYGDGRACEKIINILIKGKNNESI

[Multiple Choices]
A. 5.1.1.24
B. 3.1.1.4
C. 5.1.3.14
D. 4.4.1.11
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

> The exact sequence matches the UniProt entry annotated as EC 5.1.3.14. Its catalytic-activity annotation assigns that EC number to UDP-N-acetylglucosamine 2-epimerization and cites experimental evidence (ECO:0000269, PubMed 38382015).

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone may suggest an enzyme, but the input gives no organism, pathway, substrate, reaction, or experimental result that establishes this protein's specific catalytic activity and complete EC number.


**Missing item-specific fact**

> The protein-specific identification as UDP-N-acetylglucosamine 2-epimerase catalyzing the reaction assigned EC 5.1.3.14.


**Reason**

> Selecting the exact EC number requires a protein-specific functional annotation or experimental reaction assignment not supplied in the question; recognizing the sequence or retrieving its database record would be lookup, not reasoning from the provided input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation and cited catalytic activity support option C; the supplied evidence does not support another listed EC number.


### Important caveats

- The UniProt annotation cites experimental evidence, but the primary paper was not independently reviewed here.
- The historical and current UniProt records match the sequence; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone may suggest an enzyme, but the input gives no organism, pathway, substrate, reaction, or experimental result that establishes this protein's specific catalytic activity and complete EC number.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identification as UDP-N-acetylglucosamine 2-epimerase catalyzing the reaction assigned EC 5.1.3.14.",
    "reason": "Selecting the exact EC number requires a protein-specific functional annotation or experimental reaction assignment not supplied in the question; recognizing the sequence or retrieving its database record would be lookup, not reasoning from the provided input."
  },
  "case_id": "EC_number_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as EC 5.1.3.14. Its catalytic-activity annotation assigns that EC number to UDP-N-acetylglucosamine 2-epimerization and cites experimental evidence (ECO:0000269, PubMed 38382015)."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the primary paper was not independently reviewed here.",
    "The historical and current UniProt records match the sequence; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and cited catalytic activity support option C; the supplied evidence does not support another listed EC number."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry annotated as EC 5.1.3.14. Its catalytic-activity annotation assigns that EC number to UDP-N-acetylglucosamine 2-epimerization and cites experimental evidence (ECO:0000269, PubMed 38382015).",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone may suggest an enzyme, but the input gives no organism, pathway, substrate, reaction, or experimental result that establishes this protein's specific catalytic activity and complete EC number.",
    "missing_item_specific_fact": "The protein-specific identification as UDP-N-acetylglucosamine 2-epimerase catalyzing the reaction assigned EC 5.1.3.14.",
    "reason": "Selecting the exact EC number requires a protein-specific functional annotation or experimental reaction assignment not supplied in the question; recognizing the sequence or retrieving its database record would be lookup, not reasoning from the provided input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and cited catalytic activity support option C; the supplied evidence does not support another listed EC number."
  },
  "important_caveats": [
    "The UniProt annotation cites experimental evidence, but the primary paper was not independently reviewed here.",
    "The historical and current UniProt records match the sequence; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence (383 AA) matches UniProt entry A0A0U3CEN8 exactly. The entry is annotated as UDP-N-acetylglucosamine 2-epimerase with EC=5.1.3.14, supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic activity (UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-mannosamine) confirms the epimerase classification. Both current (entry v21) and historical (entry v19) records agree.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One might eliminate B (3.1.1.4, carboxylesterase) and D (4.4.1.11, C-S lyase) as belonging to entirely different EC classes (hydrolase, lyase) since the sequence lacks obvious lipase/esterase catalytic triads or C-S lyase motifs. However, distinguishing A (5.1.1.24, amino-acid racemase) from C (5.1.3.14, UDP-N-acetylglucosamine 2-epimerase) requires knowing the specific substrate: this protein is a non-hydrolyzing UDP-sugar epimerase, mechanistically distinct from classic hydrolyzing epimerases and lacking the canonical Rossmann-fold NAD-binding motif (GxGxxG) of well-known UDP-sugar epimerases. The sequence provides no clear diagnostic motif that identifies it as acting on UDP-sugars rather than amino acids.


**Missing item-specific fact**

> The specific identity of this protein as the Campylobacter jejuni non-hydrolyzing UDP-GlcNAc 2-epimerase (AGEP/HS11.17), characterized experimentally in 2024, and its substrate specificity for UDP-N-acetylglucosamine. Without recognizing this exact protein or its database annotation, the sequence alone does not provide grounds to select 5.1.3.14 over 5.1.1.24.


**Reason**

> The sequence lacks recognizable catalytic motifs diagnostic of UDP-sugar epimerase activity. The non-hydrolyzing AGEP family is mechanistically unusual (no NAD cofactor, no classic epimerase fold), making sequence-based reasoning to 5.1.3.14 unreliable. Selection of the correct 4-digit EC number depends on knowing this specific protein's experimentally determined substrate and mechanism.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While B and D can be eliminated by EC class reasoning, and A vs C both fall under EC 5.1 (racemases/epimerases), the specific 4-digit numbers are mutually exclusive and only C is experimentally correct. No other option is defensible given the actual protein identity, though from sequence alone the A vs C distinction is not resolvable by reasoning.


### Important caveats

- The annotation evidence (ECO:0000269) is from a 2024 publication (Ghosh & Raushel, Biochemistry 63:688-698), meaning this protein's function was experimentally characterized very recently. The Swiss-Prot entry was first integrated in June 2025.
- The reviewer-only evidence confirms the answer but was not available to the evaluated model. The model sees only the raw sequence and four EC number options.
- The non-hydrolyzing UDP-GlcNAc 2-epimerase (AGEP) is mechanistically distinct from classic hydrolyzing epimerases (NeuB, GalE), lacking NAD-binding motifs, making sequence-based homology reasoning particularly unreliable for this enzyme class.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One might eliminate B (3.1.1.4, carboxylesterase) and D (4.4.1.11, C-S lyase) as belonging to entirely different EC classes (hydrolase, lyase) since the sequence lacks obvious lipase/esterase catalytic triads or C-S lyase motifs. However, distinguishing A (5.1.1.24, amino-acid racemase) from C (5.1.3.14, UDP-N-acetylglucosamine 2-epimerase) requires knowing the specific substrate: this protein is a non-hydrolyzing UDP-sugar epimerase, mechanistically distinct from classic hydrolyzing epimerases and lacking the canonical Rossmann-fold NAD-binding motif (GxGxxG) of well-known UDP-sugar epimerases. The sequence provides no clear diagnostic motif that identifies it as acting on UDP-sugars rather than amino acids.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as the Campylobacter jejuni non-hydrolyzing UDP-GlcNAc 2-epimerase (AGEP/HS11.17), characterized experimentally in 2024, and its substrate specificity for UDP-N-acetylglucosamine. Without recognizing this exact protein or its database annotation, the sequence alone does not provide grounds to select 5.1.3.14 over 5.1.1.24.",
    "reason": "The sequence lacks recognizable catalytic motifs diagnostic of UDP-sugar epimerase activity. The non-hydrolyzing AGEP family is mechanistically unusual (no NAD cofactor, no classic epimerase fold), making sequence-based reasoning to 5.1.3.14 unreliable. Selection of the correct 4-digit EC number depends on knowing this specific protein's experimentally determined substrate and mechanism."
  },
  "case_id": "EC_number_0079",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The protein sequence (383 AA) matches UniProt entry A0A0U3CEN8 exactly. The entry is annotated as UDP-N-acetylglucosamine 2-epimerase with EC=5.1.3.14, supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic activity (UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-mannosamine) confirms the epimerase classification. Both current (entry v21) and historical (entry v19) records agree."
  },
  "important_caveats": [
    "The annotation evidence (ECO:0000269) is from a 2024 publication (Ghosh & Raushel, Biochemistry 63:688-698), meaning this protein's function was experimentally characterized very recently. The Swiss-Prot entry was first integrated in June 2025.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model. The model sees only the raw sequence and four EC number options.",
    "The non-hydrolyzing UDP-GlcNAc 2-epimerase (AGEP) is mechanistically distinct from classic hydrolyzing epimerases (NeuB, GalE), lacking NAD-binding motifs, making sequence-based homology reasoning particularly unreliable for this enzyme class."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B and D can be eliminated by EC class reasoning, and A vs C both fall under EC 5.1 (racemases/epimerases), the specific 4-digit numbers are mutually exclusive and only C is experimentally correct. No other option is defensible given the actual protein identity, though from sequence alone the A vs C distinction is not resolvable by reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0079",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence (383 AA) matches UniProt entry A0A0U3CEN8 exactly. The entry is annotated as UDP-N-acetylglucosamine 2-epimerase with EC=5.1.3.14, supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic activity (UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-mannosamine) confirms the epimerase classification. Both current (entry v21) and historical (entry v19) records agree.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One might eliminate B (3.1.1.4, carboxylesterase) and D (4.4.1.11, C-S lyase) as belonging to entirely different EC classes (hydrolase, lyase) since the sequence lacks obvious lipase/esterase catalytic triads or C-S lyase motifs. However, distinguishing A (5.1.1.24, amino-acid racemase) from C (5.1.3.14, UDP-N-acetylglucosamine 2-epimerase) requires knowing the specific substrate: this protein is a non-hydrolyzing UDP-sugar epimerase, mechanistically distinct from classic hydrolyzing epimerases and lacking the canonical Rossmann-fold NAD-binding motif (GxGxxG) of well-known UDP-sugar epimerases. The sequence provides no clear diagnostic motif that identifies it as acting on UDP-sugars rather than amino acids.",
    "missing_item_specific_fact": "The specific identity of this protein as the Campylobacter jejuni non-hydrolyzing UDP-GlcNAc 2-epimerase (AGEP/HS11.17), characterized experimentally in 2024, and its substrate specificity for UDP-N-acetylglucosamine. Without recognizing this exact protein or its database annotation, the sequence alone does not provide grounds to select 5.1.3.14 over 5.1.1.24.",
    "reason": "The sequence lacks recognizable catalytic motifs diagnostic of UDP-sugar epimerase activity. The non-hydrolyzing AGEP family is mechanistically unusual (no NAD cofactor, no classic epimerase fold), making sequence-based reasoning to 5.1.3.14 unreliable. Selection of the correct 4-digit EC number depends on knowing this specific protein's experimentally determined substrate and mechanism."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B and D can be eliminated by EC class reasoning, and A vs C both fall under EC 5.1 (racemases/epimerases), the specific 4-digit numbers are mutually exclusive and only C is experimentally correct. No other option is defensible given the actual protein identity, though from sequence alone the A vs C distinction is not resolvable by reasoning."
  },
  "important_caveats": [
    "The annotation evidence (ECO:0000269) is from a 2024 publication (Ghosh & Raushel, Biochemistry 63:688-698), meaning this protein's function was experimentally characterized very recently. The Swiss-Prot entry was first integrated in June 2025.",
    "The reviewer-only evidence confirms the answer but was not available to the evaluated model. The model sees only the raw sequence and four EC number options.",
    "The non-hydrolyzing UDP-GlcNAc 2-epimerase (AGEP) is mechanistically distinct from classic hydrolyzing epimerases (NeuB, GalE), lacking NAD-binding motifs, making sequence-based homology reasoning particularly unreliable for this enzyme class."
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

**Accession:** `A0A0U3CEN8` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 19. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:21.799773+00:00.  

```json
"A0A0U3CEN8"
```

Source SHA-256: `79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:21.799773+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38382015","source":"PubMed"}],"value":"Non-hydrolyzing UDP-GlcNAc 2-epimerase"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"value":"5.1.3.14"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"UDP-N-acetylglucosamine 2-epimerase"}}}
```

Source SHA-256: `79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:21.799773+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:17214"}}],"reaction":{"ecNumber":"5.1.3.14","evidences":[{"evidenceCode":"ECO:0000269","id":"38382015","source":"PubMed"}],"name":"UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-mannosamine","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:17213"},{"database":"ChEBI","id":"CHEBI:57705"},{"database":"ChEBI","id":"CHEBI:68623"}]}}
```

Source SHA-256: `79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3CEN8.json)  
**Locator:** `/references/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:21.799773+00:00.  

```json
{"citation":{"authors":["Ghosh M.K.","Raushel F.M."],"citationCrossReferences":[{"database":"PubMed","id":"38382015"},{"database":"DOI","id":"10.1021/acs.biochem.3c00664"}],"citationType":"journal article","firstPage":"688","id":"38382015","journal":"Biochemistry","lastPage":"698","publicationDate":"2024","title":"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.","volume":"63"},"referenceComments":[{"type":"STRAIN","value":"HS:11"}],"referenceNumber":3,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY"]}
```

Source SHA-256: `79cec39f8af13d58c2f3eacbeec9904c65a82d2ceedf2c1bacc9916abbc9faf0`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3CEN8?format=txt&versions=19)  
**Locator:** `lines 1-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:24:23.855684+00:00.  

```text
ID   UAGEP_CAMJU             Reviewed;         383 AA.
AC   A0A0U3CEN8;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-MAR-2016, sequence version 1.
DT   28-JAN-2026, entry version 19.
DE   RecName: Full=UDP-N-acetylglucosamine 2-epimerase {ECO:0000305};
DE            EC=5.1.3.14 {ECO:0000269|PubMed:38382015};
DE   AltName: Full=Non-hydrolyzing UDP-GlcNAc 2-epimerase {ECO:0000303|PubMed:38382015};
GN   Name=HS11.17 {ECO:0000303|PubMed:38382015};
OS   Campylobacter jejuni.
OC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;
OC   Campylobacterales; Campylobacteraceae; Campylobacter.
OX   NCBI_TaxID=197;
```

Source SHA-256: `ab154b9f6d4f7d6da6b610c345b588d7236e7842a8415b0bb9cb9fac2fce5141`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3CEN8?format=txt&versions=19)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:24:23.855684+00:00.  

```text
DE   RecName: Full=UDP-N-acetylglucosamine 2-epimerase {ECO:0000305};
DE            EC=5.1.3.14 {ECO:0000269|PubMed:38382015};
DE   AltName: Full=Non-hydrolyzing UDP-GlcNAc 2-epimerase {ECO:0000303|PubMed:38382015};
```

Source SHA-256: `ab154b9f6d4f7d6da6b610c345b588d7236e7842a8415b0bb9cb9fac2fce5141`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3CEN8?format=txt&versions=19)  
**Locator:** `lines 43-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 19 / 1.  
**Retrieved:** 2026-11-02T04:24:23.855684+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-
CC         mannosamine; Xref=Rhea:RHEA:17213, ChEBI:CHEBI:57705,
CC         ChEBI:CHEBI:68623; EC=5.1.3.14;
CC         Evidence={ECO:0000269|PubMed:38382015};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:17214;
CC         Evidence={ECO:0000269|PubMed:38382015};
```

Source SHA-256: `ab154b9f6d4f7d6da6b610c345b588d7236e7842a8415b0bb9cb9fac2fce5141`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 79. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
