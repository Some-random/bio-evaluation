# GO_cellular_component_0117

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `GO_cellular_component`  
**Author expected answer:** **B** — endoplasmic reticulum membrane

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATTLTPTQRYAAGALLALALRQAQIHQSVLLGAHHHHDDDDEEQGRTSTSSGGGGGSSSSSSNSGAGADADLWTHDSHGLLRPVFRFLEIDPKAWSGLEETAASSEAKHHIGAFLRIIFEEDGESSSDRSVQELALAKGVDVMVMSLGNDSEVGNTIKGGDQDALPSSSGTDKSPGESSHDDQLGINKLTLDDIPANNHRKMALLFALLSACVADKPVSQEEEDRKSTRFRKGYDARHRVALRLLSTWLDVKWIKMEAIEVMVACSAMAAAKEQEQSQESASPKSKWEKWKRGGIIGAAALTGGALLAITGGLAAPAIAAGFGALAPTLGTLVPVIGASGFAAMATAAGSVAGSVAVAASFGAAGAGLTGSKMARRIGSVKEFEFKPIGENHNQGRLAVGILISGFAFDEDDFCRPWEGWQDNLERYILQWESKHIIAVSTAIQDWLTSRLAMELMKQGAMRTVLSGLLAAFAWPATLLAATDFIDSKWSVAIDRSDKAGKMLAEVLLKGLQGNRPVTLIGFSLGARVIFKCLQELALSSDNEGLVERVVLLGAPVSVKGERWEAARKMVAGRFVNVYSTDDWILGVTFRASLLTQGLAGIQAIDVPGVENVDVTELVDGHSSYLSAAQQILEHLELNTYYPVFVPLSAANEETDGTVAQ

[Multiple Choices]
A. kinetoplast
B. endoplasmic reticulum membrane
C. glutamatergic synapse
D. collagen-containing extracellular matrix
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The exact sequence matches the rice STS1 protein, and its UniProt entry assigns it to the endoplasmic reticulum membrane. The annotation cites experimental evidence (IDA) from two publications; this supports the key, though the primary studies were not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal segment and multiple hydrophobic regions consistent with a multipass membrane protein, which makes membrane-associated choices more plausible than collagen-containing extracellular matrix. These features do not identify the ER as its final location.


**Missing item-specific fact**

> The protein-specific localization to the ER membrane, established by the cited localization evidence, is not supplied in the question.


**Reason**

> Sequence features support membrane association but do not distinguish ER from other cellular membranes or establish the protein's primary compartment. Selecting B over other membrane-protein possibilities requires the protein-specific localization fact, rather than recognition of a general targeting principle.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports B, and no other listed choice is independently supported. However, the sequence alone does not establish the precise ER localization.


### Important caveats

- The reviewer-only sequence match is exact, but the accession and database annotation were not supplied to the evaluated model.
- The experimental evidence is reported in UniProt with IDA codes and cited publications; the studies were not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal segment and multiple hydrophobic regions consistent with a multipass membrane protein, which makes membrane-associated choices more plausible than collagen-containing extracellular matrix. These features do not identify the ER as its final location.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific localization to the ER membrane, established by the cited localization evidence, is not supplied in the question.",
    "reason": "Sequence features support membrane association but do not distinguish ER from other cellular membranes or establish the protein's primary compartment. Selecting B over other membrane-protein possibilities requires the protein-specific localization fact, rather than recognition of a general targeting principle."
  },
  "case_id": "GO_cellular_component_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the rice STS1 protein, and its UniProt entry assigns it to the endoplasmic reticulum membrane. The annotation cites experimental evidence (IDA) from two publications; this supports the key, though the primary studies were not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only sequence match is exact, but the accession and database annotation were not supplied to the evaluated model.",
    "The experimental evidence is reported in UniProt with IDA codes and cited publications; the studies were not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B, and no other listed choice is independently supported. However, the sequence alone does not establish the precise ER localization."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the rice STS1 protein, and its UniProt entry assigns it to the endoplasmic reticulum membrane. The annotation cites experimental evidence (IDA) from two publications; this supports the key, though the primary studies were not independently reviewed here.",
    "evidence_ids": ["C1", "C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal segment and multiple hydrophobic regions consistent with a multipass membrane protein, which makes membrane-associated choices more plausible than collagen-containing extracellular matrix. These features do not identify the ER as its final location.",
    "missing_item_specific_fact": "The protein-specific localization to the ER membrane, established by the cited localization evidence, is not supplied in the question.",
    "reason": "Sequence features support membrane association but do not distinguish ER from other cellular membranes or establish the protein's primary compartment. Selecting B over other membrane-protein possibilities requires the protein-specific localization fact, rather than recognition of a general targeting principle."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B, and no other listed choice is independently supported. However, the sequence alone does not establish the precise ER localization."
  },
  "important_caveats": [
    "The reviewer-only sequence match is exact, but the accession and database annotation were not supplied to the evaluated model.",
    "The experimental evidence is reported in UniProt with IDA codes and cited publications; the studies were not independently validated here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q10SS2 (STS1_ORYSJ) annotates this protein as 'Endoplasmic reticulum membrane' with GO:0005789, evidence code IDA (Inferred from Direct Assay), supported by two independent experimental studies (PubMed:35748750, 2022 Plant Physiol; PubMed:36657664, 2023 Plant Sci). The protein is also annotated as a multi-pass membrane protein. The sequence (661 AA, SHA256-matched) contains multiple hydrophobic transmembrane stretches consistent with multi-pass topology. The expected answer B is directly supported by experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [H4](#evidence-h4), [H5](#evidence-h5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence composition (poly-G/poly-S stretches, Ala/Gly/Ser/Pro-rich overall composition, plant-typical signal peptide-like N-terminus) suggests a plant protein. Three distractors are categorically incompatible with any plant organism: (A) kinetoplast exists only in kinetoplastid parasites (Trypanosoma, Leishmania); (C) glutamatergic synapses are animal neuronal structures absent in plants; (D) collagen-containing extracellular matrix is an animal-specific structure (plants lack collagen). This leaves B as the only viable option. The multi-pass transmembrane topology visible in the sequence (multiple hydrophobic stretches ~20-25 residues) is consistent with an integral membrane protein, and ER membrane is the only membrane compartment offered.


**Missing item-specific fact**

> Precise sub-compartment assignment among membrane organelles (ER vs. Golgi vs. plasma membrane) would require experimental localization data not derivable from sequence alone. However, this distinction is moot because the other three options are categorically impossible for a plant protein, making B the sole remaining choice by elimination.


**Reason**

> The question is answerable through general biological reasoning: recognizing the organism as a plant (from sequence composition features) and applying knowledge that kinetoplasts, glutamatergic synapses, and collagen ECM are incompatible with plant biology. The multi-pass transmembrane nature visible in the sequence supports a membrane compartment assignment. The specific ER vs. other-membrane distinction is not required because no competing membrane option is offered.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> All three distractors (A, C, D) are categorically incompatible with a plant protein. Kinetoplasts exist only in kinetoplastid protists, glutamatergic synapses are animal neuronal structures, and collagen-containing ECM is animal-specific. No ambiguity exists among the four choices for a plant-derived protein.


### Important caveats

- The organism (Oryza sativa) is not explicitly stated in the model input; identification relies on sequence composition inference (poly-G/poly-S stretches, overall AA composition). A model failing to recognize plant origin might struggle with elimination.
- The specific ER membrane assignment among membrane compartments (ER vs. Golgi vs. plasma membrane) was established experimentally (IDA evidence from two independent studies) and is not derivable from sequence features alone, but this is irrelevant here since no competing membrane option is offered.
- The protein is annotated as a multi-pass membrane protein (ECO:0000255, inferred from similarity), while the ER localization itself is experimentally determined (ECO:0000269, direct assay).
- Accession Q10SS2 was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence without organism or accession information.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence composition (poly-G/poly-S stretches, Ala/Gly/Ser/Pro-rich overall composition, plant-typical signal peptide-like N-terminus) suggests a plant protein. Three distractors are categorically incompatible with any plant organism: (A) kinetoplast exists only in kinetoplastid parasites (Trypanosoma, Leishmania); (C) glutamatergic synapses are animal neuronal structures absent in plants; (D) collagen-containing extracellular matrix is an animal-specific structure (plants lack collagen). This leaves B as the only viable option. The multi-pass transmembrane topology visible in the sequence (multiple hydrophobic stretches ~20-25 residues) is consistent with an integral membrane protein, and ER membrane is the only membrane compartment offered.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise sub-compartment assignment among membrane organelles (ER vs. Golgi vs. plasma membrane) would require experimental localization data not derivable from sequence alone. However, this distinction is moot because the other three options are categorically impossible for a plant protein, making B the sole remaining choice by elimination.",
    "reason": "The question is answerable through general biological reasoning: recognizing the organism as a plant (from sequence composition features) and applying knowledge that kinetoplasts, glutamatergic synapses, and collagen ECM are incompatible with plant biology. The multi-pass transmembrane nature visible in the sequence supports a membrane compartment assignment. The specific ER vs. other-membrane distinction is not required because no competing membrane option is offered."
  },
  "case_id": "GO_cellular_component_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8",
      "H4",
      "H5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q10SS2 (STS1_ORYSJ) annotates this protein as 'Endoplasmic reticulum membrane' with GO:0005789, evidence code IDA (Inferred from Direct Assay), supported by two independent experimental studies (PubMed:35748750, 2022 Plant Physiol; PubMed:36657664, 2023 Plant Sci). The protein is also annotated as a multi-pass membrane protein. The sequence (661 AA, SHA256-matched) contains multiple hydrophobic transmembrane stretches consistent with multi-pass topology. The expected answer B is directly supported by experimental evidence."
  },
  "important_caveats": [
    "The organism (Oryza sativa) is not explicitly stated in the model input; identification relies on sequence composition inference (poly-G/poly-S stretches, overall AA composition). A model failing to recognize plant origin might struggle with elimination.",
    "The specific ER membrane assignment among membrane compartments (ER vs. Golgi vs. plasma membrane) was established experimentally (IDA evidence from two independent studies) and is not derivable from sequence features alone, but this is irrelevant here since no competing membrane option is offered.",
    "The protein is annotated as a multi-pass membrane protein (ECO:0000255, inferred from similarity), while the ER localization itself is experimentally determined (ECO:0000269, direct assay).",
    "Accession Q10SS2 was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence without organism or accession information."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "All three distractors (A, C, D) are categorically incompatible with a plant protein. Kinetoplasts exist only in kinetoplastid protists, glutamatergic synapses are animal neuronal structures, and collagen-containing ECM is animal-specific. No ambiguity exists among the four choices for a plant-derived protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q10SS2 (STS1_ORYSJ) annotates this protein as 'Endoplasmic reticulum membrane' with GO:0005789, evidence code IDA (Inferred from Direct Assay), supported by two independent experimental studies (PubMed:35748750, 2022 Plant Physiol; PubMed:36657664, 2023 Plant Sci). The protein is also annotated as a multi-pass membrane protein. The sequence (661 AA, SHA256-matched) contains multiple hydrophobic transmembrane stretches consistent with multi-pass topology. The expected answer B is directly supported by experimental evidence.",
    "evidence_ids": ["C5", "C6", "C7", "C8", "H4", "H5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence composition (poly-G/poly-S stretches, Ala/Gly/Ser/Pro-rich overall composition, plant-typical signal peptide-like N-terminus) suggests a plant protein. Three distractors are categorically incompatible with any plant organism: (A) kinetoplast exists only in kinetoplastid parasites (Trypanosoma, Leishmania); (C) glutamatergic synapses are animal neuronal structures absent in plants; (D) collagen-containing extracellular matrix is an animal-specific structure (plants lack collagen). This leaves B as the only viable option. The multi-pass transmembrane topology visible in the sequence (multiple hydrophobic stretches ~20-25 residues) is consistent with an integral membrane protein, and ER membrane is the only membrane compartment offered.",
    "missing_item_specific_fact": "Precise sub-compartment assignment among membrane organelles (ER vs. Golgi vs. plasma membrane) would require experimental localization data not derivable from sequence alone. However, this distinction is moot because the other three options are categorically impossible for a plant protein, making B the sole remaining choice by elimination.",
    "reason": "The question is answerable through general biological reasoning: recognizing the organism as a plant (from sequence composition features) and applying knowledge that kinetoplasts, glutamatergic synapses, and collagen ECM are incompatible with plant biology. The multi-pass transmembrane nature visible in the sequence supports a membrane compartment assignment. The specific ER vs. other-membrane distinction is not required because no competing membrane option is offered."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "All three distractors (A, C, D) are categorically incompatible with a plant protein. Kinetoplasts exist only in kinetoplastid protists, glutamatergic synapses are animal neuronal structures, and collagen-containing ECM is animal-specific. No ambiguity exists among the four choices for a plant-derived protein."
  },
  "important_caveats": [
    "The organism (Oryza sativa) is not explicitly stated in the model input; identification relies on sequence composition inference (poly-G/poly-S stretches, overall AA composition). A model failing to recognize plant origin might struggle with elimination.",
    "The specific ER membrane assignment among membrane compartments (ER vs. Golgi vs. plasma membrane) was established experimentally (IDA evidence from two independent studies) and is not derivable from sequence features alone, but this is irrelevant here since no competing membrane option is offered.",
    "The protein is annotated as a multi-pass membrane protein (ECO:0000255, inferred from similarity), while the ER localization itself is experimentally determined (ECO:0000269, direct assay).",
    "Accession Q10SS2 was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence without organism or accession information."
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

**Accession:** `Q10SS2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 121. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:29.234158+00:00.  

```json
"Q10SS2"
```

Source SHA-256: `0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:29.234158+00:00.  

```json
{"commentType":"SUBCELLULAR LOCATION","subcellularLocations":[{"location":{"evidences":[{"evidenceCode":"ECO:0000269","id":"35748750","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36657664","source":"PubMed"}],"id":"SL-0097","value":"Endoplasmic reticulum membrane"},"topology":{"evidences":[{"evidenceCode":"ECO:0000255"}],"id":"SL-9909","value":"Multi-pass membrane protein"}}]}
```

Source SHA-256: `0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)  
**Locator:** `/uniProtKBCrossReferences/19`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:29.234158+00:00.  

```json
{"database":"GO","evidences":[{"evidenceCode":"ECO:0000314","id":"35748750","source":"PubMed"},{"evidenceCode":"ECO:0000314","id":"36657664","source":"PubMed"}],"id":"GO:0005789","properties":[{"key":"GoTerm","value":"C:endoplasmic reticulum membrane"},{"key":"GoEvidenceType","value":"IDA:UniProtKB"}]}
```

Source SHA-256: `0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27`.

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)  
**Locator:** `/references/6`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:29.234158+00:00.  

```json
{"citation":{"authors":["Yuan G.","Zou T.","He Z.","Xiao Q.","Li G.","Liu S.","Xiong P.","Chen H.","Peng K.","Zhang X.","Luo T.","Zhou D.","Yang S.","Zhou F.","Zhang K.","Zheng K.","Han Y.","Zhu J.","Liang Y.","Deng Q.","Wang S.","Sun C.","Yu X.","Liu H.","Wang L.","Li P.","Li S."],"citationCrossReferences":[{"database":"PubMed","id":"35748750"},{"database":"DOI","id":"10.1093/plphys/kiac307"}],"citationType":"journal article","firstPage":"352","id":"35748750","journal":"Plant Physiol.","lastPage":"370","publicationDate":"2022","title":"SWOLLEN TAPETUM AND STERILITY 1 is required for tapetum degeneration and pollen wall formation in rice.","volume":"190"},"referenceNumber":7,"referencePositions":["FUNCTION","CATALYTIC ACTIVITY","SUBCELLULAR LOCATION","INTERACTION WITH PKS10/PKS2 AND 4CLL9/ACOS12","DEVELOPMENTAL STAGE","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27`.

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q10SS2.json)  
**Locator:** `/references/7`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:30:29.234158+00:00.  

```json
{"citation":{"authors":["Sun Z.","Liu K.","Chen C.","Chen D.","Peng Z.","Zhou R.","Liu L.","He D.","Duan W.","Chen H.","Huang C.","Ruan Z.","Zhang Y.","Cao L.","Zhan X.","Cheng S.","Sun L."],"citationCrossReferences":[{"database":"PubMed","id":"36657664"},{"database":"DOI","id":"10.1016/j.plantsci.2023.111596"}],"citationType":"journal article","firstPage":"111596","id":"36657664","journal":"Plant Sci.","lastPage":"111596","publicationDate":"2023","title":"OsLDDT1, encoding a transmembrane structural DUF726 family protein, is essential for tapetum degradation and pollen formation in rice.","volume":"329"},"referenceNumber":8,"referencePositions":["FUNCTION","SUBCELLULAR LOCATION","DEVELOPMENTAL STAGE","DISRUPTION PHENOTYPE"]}
```

Source SHA-256: `0a6a8d6a3c909a1dbd7c765a1a1d325767f551df7a3b5795f41c6d5c449c4e27`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)  
**Locator:** `lines 94-104`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:30:34.944114+00:00.  

```text
RN   [7]
RP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, INTERACTION WITH
RP   PKS10/PKS2 AND 4CLL9/ACOS12, DEVELOPMENTAL STAGE, AND DISRUPTION PHENOTYPE.
RX   PubMed=35748750; DOI=10.1093/plphys/kiac307;
RA   Yuan G., Zou T., He Z., Xiao Q., Li G., Liu S., Xiong P., Chen H., Peng K.,
RA   Zhang X., Luo T., Zhou D., Yang S., Zhou F., Zhang K., Zheng K., Han Y.,
RA   Zhu J., Liang Y., Deng Q., Wang S., Sun C., Yu X., Liu H., Wang L., Li P.,
RA   Li S.;
RT   "SWOLLEN TAPETUM AND STERILITY 1 is required for tapetum degeneration and
RT   pollen wall formation in rice.";
RL   Plant Physiol. 190:352-370(2022).
```

Source SHA-256: `acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)  
**Locator:** `lines 105-113`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:30:34.944114+00:00.  

```text
RN   [8]
RP   FUNCTION, SUBCELLULAR LOCATION, DEVELOPMENTAL STAGE, AND DISRUPTION
RP   PHENOTYPE.
RX   PubMed=36657664; DOI=10.1016/j.plantsci.2023.111596;
RA   Sun Z., Liu K., Chen C., Chen D., Peng Z., Zhou R., Liu L., He D., Duan W.,
RA   Chen H., Huang C., Ruan Z., Zhang Y., Cao L., Zhan X., Cheng S., Sun L.;
RT   "OsLDDT1, encoding a transmembrane structural DUF726 family protein, is
RT   essential for tapetum degradation and pollen formation in rice.";
RL   Plant Sci. 329:111596-111596(2023).
```

Source SHA-256: `acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)  
**Locator:** `lines 123-125`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:30:34.944114+00:00.  

```text
CC   -!- SUBCELLULAR LOCATION: Endoplasmic reticulum membrane
CC       {ECO:0000269|PubMed:35748750, ECO:0000269|PubMed:36657664}; Multi-pass
CC       membrane protein {ECO:0000255}.
```

Source SHA-256: `acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q10SS2?format=txt&versions=121)  
**Locator:** `lines 161-161`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 121 / 1.  
**Retrieved:** 2026-11-02T04:30:34.944114+00:00.  

```text
DR   GO; GO:0005789; C:endoplasmic reticulum membrane; IDA:UniProtKB.
```

Source SHA-256: `acc4e547beb155cdd1e60fb276d5cc6296693b0794b6f3a69d9c2d66a4f46eda`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 117. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
