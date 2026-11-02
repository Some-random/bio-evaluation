# cofactor_0012

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MAGKSPEEQHPVKAYGWAARDSSGILSPFKFSRRATGDHDVRVKILYAGVCHSDLQSARNEMGCFTYPLVPGFETVGIATEVGSKVTKMKVGDKVAVGIMVGSCGKCDDCVNDRECYCPEVITSYGRIDHDGTPTYGGFSNETVANEKFVFRFPEKLPMAAGAPLLNAGVSVYSPMRFYGLDKPGMHLGVVGLGGLGHLAVKFAKAFGVKVTVISTSSIKKGEAINDLGADAFLVSTDAKQMQAGSGTLDGILDTVPVVHPIEPLLGLLKNHTKLVLVGATMGSFELPILPLGVGRKSVASTVGGSTTEAQEMLDFAAEHNITANVEIIPMDYINTAMERIEKNDVRYRFVIDVGNTLTPPES

[Multiple Choices]
A. pantetheine 4'-phosphate
B. Zn(2+)
C. NAD(+)
D. Fe cation
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated as binding Zn(2+), two ions per subunit. This supports choice B, though the annotation is transferred by similarity rather than direct evidence shown here for this protein.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The cysteine-rich region may suggest metal binding, but sequence composition alone does not establish that zinc is the required cofactor or distinguish it reliably from the listed alternatives.


**Missing item-specific fact**

> The protein-specific cofactor annotation or experimental characterization establishing zinc binding is absent from the input.


**Reason**

> Identifying the zinc-dependent enzyme and its cofactor requires protein-specific information not supplied in the question; recognizing the sequence from a database would be lookup, not reasoning from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Of the listed options, Zn(2+) is supported by the matching entry's cofactor annotation. The evidence does not establish that other cofactors are absent, but NAD(+) is not the same as the NAD(P) coenzyme often relevant to reductases.


### Important caveats

- The zinc annotation is supported by similarity evidence to UniProtKB:P06525, not direct experimental evidence for this exact protein in the supplied excerpts.
- The annotation says two Zn(2+) ions bind per subunit; binding alone does not independently prove their necessity for catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The cysteine-rich region may suggest metal binding, but sequence composition alone does not establish that zinc is the required cofactor or distinguish it reliably from the listed alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific cofactor annotation or experimental characterization establishing zinc binding is absent from the input.",
    "reason": "Identifying the zinc-dependent enzyme and its cofactor requires protein-specific information not supplied in the question; recognizing the sequence from a database would be lookup, not reasoning from the input."
  },
  "case_id": "cofactor_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as binding Zn(2+), two ions per subunit. This supports choice B, though the annotation is transferred by similarity rather than direct evidence shown here for this protein."
  },
  "important_caveats": [
    "The zinc annotation is supported by similarity evidence to UniProtKB:P06525, not direct experimental evidence for this exact protein in the supplied excerpts.",
    "The annotation says two Zn(2+) ions bind per subunit; binding alone does not independently prove their necessity for catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Of the listed options, Zn(2+) is supported by the matching entry's cofactor annotation. The evidence does not establish that other cofactors are absent, but NAD(+) is not the same as the NAD(P) coenzyme often relevant to reductases."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as binding Zn(2+), two ions per subunit. This supports choice B, though the annotation is transferred by similarity rather than direct evidence shown here for this protein.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The cysteine-rich region may suggest metal binding, but sequence composition alone does not establish that zinc is the required cofactor or distinguish it reliably from the listed alternatives.",
    "missing_item_specific_fact": "The protein-specific cofactor annotation or experimental characterization establishing zinc binding is absent from the input.",
    "reason": "Identifying the zinc-dependent enzyme and its cofactor requires protein-specific information not supplied in the question; recognizing the sequence from a database would be lookup, not reasoning from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Of the listed options, Zn(2+) is supported by the matching entry's cofactor annotation. The evidence does not establish that other cofactors are absent, but NAD(+) is not the same as the NAD(P) coenzyme often relevant to reductases."
  },
  "important_caveats": [
    "The zinc annotation is supported by similarity evidence to UniProtKB:P06525, not direct experimental evidence for this exact protein in the supplied excerpts.",
    "The annotation says two Zn(2+) ions bind per subunit; binding alone does not independently prove their necessity for catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A0U4BHM2 (1,2-Dihydrovomilenine reductase, EC 1.3.1.73, a CAD-like reductase from Rauvolfia tetraphylla) annotates the cofactor as Zn(2+) with the note 'Binds 2 Zn(2+) ions per subunit.' The annotation is by similarity (ECO:0000250) to P06525, a well-characterized Zn-dependent cinnamyl alcohol dehydrogenase. CAD-family enzymes are established Zn(2+)-dependent oxidoreductases, making the transferred annotation biologically reasonable. The original publication (PubMed:26715562) characterized catalytic activity and biophysical properties, providing experimental context for the enzyme's function, though the Zn assignment itself is inferred by homology rather than directly measured on this protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A knowledgeable student could note: (1) the sequence contains a Rossmann-fold NAD(P)-binding motif (GATMGS), which is a co-substrate/coenzyme feature rather than a metal cofactor; (2) clustered Cys and His residues (e.g., GSCGKCD, CYCP, GDHD) are consistent with a Zn-binding site typical of dehydrogenases; (3) strict biochemical terminology distinguishes a metal 'cofactor' (Zn²⁺) from a redox 'co-substrate' (NAD⁺/NADH), helping eliminate C; (4) pantetheine 4'-phosphate is a prosthetic group of acyl-carrier proteins (option A) and Fe cations require distinct heme/non-heme motifs absent here (option D). However, these arguments are suggestive rather than decisive.


**Missing item-specific fact**

> Definitively assigning Zn(2+) as THE catalytic cofactor (rather than NAD⁺ as the relevant redox partner) requires recognizing this protein as a cinnamyl alcohol dehydrogenase (CAD)-family enzyme, for which Zn(2+) is the essential catalytic metal. The sequence's most prominent and unambiguous motif is the Rossmann-fold NAD-binding signature (GATMGS), which would actually mislead a sequence-only analysis toward NAD⁺. The Zn-binding site in CAD enzymes is embedded in a less conspicuous Cys/His arrangement that is not uniquely identifiable without prior knowledge of the CAD fold and its two-Zn active site architecture.


**Reason**

> While general biochemical reasoning (cofactor vs. co-substrate terminology, elimination of pantetheine and Fe) narrows the field, the critical step—identifying the protein as a CAD-family Zn-dependent enzyme—depends on recognizing a specific protein family and its metal-cofactor requirement. The dominant sequence signature (Rossmann fold) points toward NAD⁺, making Zn(2+) selection reliant on item-specific knowledge of CAD-family cofactor dependence rather than on a clearly readable Zn-binding motif in the provided sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> NAD⁺/NADH is directly involved in the catalytic mechanism of EC 1.3.1.73 (the enzyme uses NADH as the electron donor for the reduction). In many biochemistry textbooks, NAD⁺ is loosely called a 'cofactor' or 'coenzyme.' A student who interprets 'cofactor' broadly could reasonably select C, especially given the prominent Rossmann-fold motif in the sequence. The strict definition (cofactor = metal ion or tightly bound prosthetic group; co-substrate = freely diffusing redox partner like NAD⁺) is needed to eliminate C, but this terminological boundary is not universally enforced in all curricula.


### Important caveats

- The Zn(2+) annotation is by similarity (ECO:0000250) to P06525, not from direct experimental measurement on A0A0U4BHM2 itself. The original paper characterized function and biophysical properties but the cofactor assignment is a transferred annotation.
- The protein also carries an alternative EC annotation (1.5.1.-) from the primary publication, reflecting some uncertainty in the exact reaction mechanism as originally reported.
- The sequence contains a clear NAD(P)-binding Rossmann fold (GATMGS), meaning NAD(P)H is genuinely involved in catalysis; the question's use of 'cofactor' must be read in the narrow metal-ion sense to make B uniquely correct.
- The UniProt accession was inferred from dataset metadata and was not provided to the evaluated model; the model sees only the raw sequence and four choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable student could note: (1) the sequence contains a Rossmann-fold NAD(P)-binding motif (GATMGS), which is a co-substrate/coenzyme feature rather than a metal cofactor; (2) clustered Cys and His residues (e.g., GSCGKCD, CYCP, GDHD) are consistent with a Zn-binding site typical of dehydrogenases; (3) strict biochemical terminology distinguishes a metal 'cofactor' (Zn²⁺) from a redox 'co-substrate' (NAD⁺/NADH), helping eliminate C; (4) pantetheine 4'-phosphate is a prosthetic group of acyl-carrier proteins (option A) and Fe cations require distinct heme/non-heme motifs absent here (option D). However, these arguments are suggestive rather than decisive.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Definitively assigning Zn(2+) as THE catalytic cofactor (rather than NAD⁺ as the relevant redox partner) requires recognizing this protein as a cinnamyl alcohol dehydrogenase (CAD)-family enzyme, for which Zn(2+) is the essential catalytic metal. The sequence's most prominent and unambiguous motif is the Rossmann-fold NAD-binding signature (GATMGS), which would actually mislead a sequence-only analysis toward NAD⁺. The Zn-binding site in CAD enzymes is embedded in a less conspicuous Cys/His arrangement that is not uniquely identifiable without prior knowledge of the CAD fold and its two-Zn active site architecture.",
    "reason": "While general biochemical reasoning (cofactor vs. co-substrate terminology, elimination of pantetheine and Fe) narrows the field, the critical step—identifying the protein as a CAD-family Zn-dependent enzyme—depends on recognizing a specific protein family and its metal-cofactor requirement. The dominant sequence signature (Rossmann fold) points toward NAD⁺, making Zn(2+) selection reliant on item-specific knowledge of CAD-family cofactor dependence rather than on a clearly readable Zn-binding motif in the provided sequence."
  },
  "case_id": "cofactor_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2",
      "C6"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A0U4BHM2 (1,2-Dihydrovomilenine reductase, EC 1.3.1.73, a CAD-like reductase from Rauvolfia tetraphylla) annotates the cofactor as Zn(2+) with the note 'Binds 2 Zn(2+) ions per subunit.' The annotation is by similarity (ECO:0000250) to P06525, a well-characterized Zn-dependent cinnamyl alcohol dehydrogenase. CAD-family enzymes are established Zn(2+)-dependent oxidoreductases, making the transferred annotation biologically reasonable. The original publication (PubMed:26715562) characterized catalytic activity and biophysical properties, providing experimental context for the enzyme's function, though the Zn assignment itself is inferred by homology rather than directly measured on this protein."
  },
  "important_caveats": [
    "The Zn(2+) annotation is by similarity (ECO:0000250) to P06525, not from direct experimental measurement on A0A0U4BHM2 itself. The original paper characterized function and biophysical properties but the cofactor assignment is a transferred annotation.",
    "The protein also carries an alternative EC annotation (1.5.1.-) from the primary publication, reflecting some uncertainty in the exact reaction mechanism as originally reported.",
    "The sequence contains a clear NAD(P)-binding Rossmann fold (GATMGS), meaning NAD(P)H is genuinely involved in catalysis; the question's use of 'cofactor' must be read in the narrow metal-ion sense to make B uniquely correct.",
    "The UniProt accession was inferred from dataset metadata and was not provided to the evaluated model; the model sees only the raw sequence and four choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "NAD⁺/NADH is directly involved in the catalytic mechanism of EC 1.3.1.73 (the enzyme uses NADH as the electron donor for the reduction). In many biochemistry textbooks, NAD⁺ is loosely called a 'cofactor' or 'coenzyme.' A student who interprets 'cofactor' broadly could reasonably select C, especially given the prominent Rossmann-fold motif in the sequence. The strict definition (cofactor = metal ion or tightly bound prosthetic group; co-substrate = freely diffusing redox partner like NAD⁺) is needed to eliminate C, but this terminological boundary is not universally enforced in all curricula."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A0U4BHM2 (1,2-Dihydrovomilenine reductase, EC 1.3.1.73, a CAD-like reductase from Rauvolfia tetraphylla) annotates the cofactor as Zn(2+) with the note 'Binds 2 Zn(2+) ions per subunit.' The annotation is by similarity (ECO:0000250) to P06525, a well-characterized Zn-dependent cinnamyl alcohol dehydrogenase. CAD-family enzymes are established Zn(2+)-dependent oxidoreductases, making the transferred annotation biologically reasonable. The original publication (PubMed:26715562) characterized catalytic activity and biophysical properties, providing experimental context for the enzyme's function, though the Zn assignment itself is inferred by homology rather than directly measured on this protein.",
    "evidence_ids": ["C5", "H4", "C4", "H2", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A knowledgeable student could note: (1) the sequence contains a Rossmann-fold NAD(P)-binding motif (GATMGS), which is a co-substrate/coenzyme feature rather than a metal cofactor; (2) clustered Cys and His residues (e.g., GSCGKCD, CYCP, GDHD) are consistent with a Zn-binding site typical of dehydrogenases; (3) strict biochemical terminology distinguishes a metal 'cofactor' (Zn²⁺) from a redox 'co-substrate' (NAD⁺/NADH), helping eliminate C; (4) pantetheine 4'-phosphate is a prosthetic group of acyl-carrier proteins (option A) and Fe cations require distinct heme/non-heme motifs absent here (option D). However, these arguments are suggestive rather than decisive.",
    "missing_item_specific_fact": "Definitively assigning Zn(2+) as THE catalytic cofactor (rather than NAD⁺ as the relevant redox partner) requires recognizing this protein as a cinnamyl alcohol dehydrogenase (CAD)-family enzyme, for which Zn(2+) is the essential catalytic metal. The sequence's most prominent and unambiguous motif is the Rossmann-fold NAD-binding signature (GATMGS), which would actually mislead a sequence-only analysis toward NAD⁺. The Zn-binding site in CAD enzymes is embedded in a less conspicuous Cys/His arrangement that is not uniquely identifiable without prior knowledge of the CAD fold and its two-Zn active site architecture.",
    "reason": "While general biochemical reasoning (cofactor vs. co-substrate terminology, elimination of pantetheine and Fe) narrows the field, the critical step—identifying the protein as a CAD-family Zn-dependent enzyme—depends on recognizing a specific protein family and its metal-cofactor requirement. The dominant sequence signature (Rossmann fold) points toward NAD⁺, making Zn(2+) selection reliant on item-specific knowledge of CAD-family cofactor dependence rather than on a clearly readable Zn-binding motif in the provided sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "NAD⁺/NADH is directly involved in the catalytic mechanism of EC 1.3.1.73 (the enzyme uses NADH as the electron donor for the reduction). In many biochemistry textbooks, NAD⁺ is loosely called a 'cofactor' or 'coenzyme.' A student who interprets 'cofactor' broadly could reasonably select C, especially given the prominent Rossmann-fold motif in the sequence. The strict definition (cofactor = metal ion or tightly bound prosthetic group; co-substrate = freely diffusing redox partner like NAD⁺) is needed to eliminate C, but this terminological boundary is not universally enforced in all curricula."
  },
  "important_caveats": [
    "The Zn(2+) annotation is by similarity (ECO:0000250) to P06525, not from direct experimental measurement on A0A0U4BHM2 itself. The original paper characterized function and biophysical properties but the cofactor assignment is a transferred annotation.",
    "The protein also carries an alternative EC annotation (1.5.1.-) from the primary publication, reflecting some uncertainty in the exact reaction mechanism as originally reported.",
    "The sequence contains a clear NAD(P)-binding Rossmann fold (GATMGS), meaning NAD(P)H is genuinely involved in catalysis; the question's use of 'cofactor' must be read in the narrow metal-ion sense to make B uniquely correct.",
    "The UniProt accession was inferred from dataset metadata and was not provided to the evaluated model; the model sees only the raw sequence and four choices."
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

**Accession:** `A0A0U4BHM2` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 30. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.340033+00:00.  

```json
"A0A0U4BHM2"
```

Source SHA-256: `c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.340033+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Protein RR2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RtRR2"}]},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26715562","source":"PubMed"}],"value":"1.5.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"Vomilenine reductase 2"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RtVR2"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"A0A0U3S9Q3","source":"UniProtKB"}],"value":"1.3.1.73"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"1,2-Dihydrovomilenine reductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26715562","source":"PubMed"}],"value":"RtDHVR"}]}}
```

Source SHA-256: `c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)  
**Locator:** `/comments/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.340033+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29105"},"evidences":[{"evidenceCode":"ECO:0000250","id":"P06525","source":"UniProtKB"}],"name":"Zn(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"P06525","source":"UniProtKB"}],"value":"Binds 2 Zn(2+) ions per subunit."}]}}
```

Source SHA-256: `c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:23.340033+00:00.  

```json
{"citation":{"authors":["Geissler M.","Burghard M.","Volk J.","Staniek A.","Warzecha H."],"citationCrossReferences":[{"database":"PubMed","id":"26715562"},{"database":"DOI","id":"10.1007/s00425-015-2446-6"}],"citationType":"journal article","firstPage":"813","id":"26715562","journal":"Planta","lastPage":"824","publicationDate":"2016","title":"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.","volume":"243"},"evidences":[{"evidenceCode":"ECO:0000312","id":"ALW82982.1","source":"EMBL"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","PROTEIN SEQUENCE OF 14-26 AND 149-156","FUNCTION","CATALYTIC ACTIVITY","PATHWAY","BIOPHYSICOCHEMICAL PROPERTIES"]}
```

Source SHA-256: `c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)  
**Locator:** `lines 6-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:25.840272+00:00.  

```text
DE   RecName: Full=1,2-Dihydrovomilenine reductase {ECO:0000303|PubMed:26715562};
DE            Short=RtDHVR {ECO:0000303|PubMed:26715562};
DE            EC=1.3.1.73 {ECO:0000250|UniProtKB:A0A0U3S9Q3};
DE   AltName: Full=Protein RR2 {ECO:0000303|PubMed:26715562};
DE            Short=RtRR2 {ECO:0000303|PubMed:26715562};
DE   AltName: Full=Vomilenine reductase 2 {ECO:0000303|PubMed:26715562};
DE            Short=RtVR2 {ECO:0000303|PubMed:26715562};
DE            EC=1.5.1.- {ECO:0000269|PubMed:26715562};
```

Source SHA-256: `f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)  
**Locator:** `lines 54-57`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 30 / 1.  
**Retrieved:** 2026-11-02T04:24:25.840272+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;
CC         Evidence={ECO:0000250|UniProtKB:P06525};
CC       Note=Binds 2 Zn(2+) ions per subunit. {ECO:0000250|UniProtKB:P06525};
```

Source SHA-256: `f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 12. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
