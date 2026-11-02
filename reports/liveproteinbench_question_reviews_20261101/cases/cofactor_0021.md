# cofactor_0021

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `cofactor`  
**Author expected answer:** **B** — Cu(2+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MKTRQNVYELKDDTLSWYSRAVEEMKSRDINDPTSWWYQGAIHGYATYPSALTYWHDATGYPPSQQTVNSGFWNRCQHGTWYFLPWHRMYLFYFEEIVAKAIRDMGGPADWTLPYWNYCEAYNTSASPSNQQQALQIPPEFGSSQGPNADFASLWIKNRRNYVLNKNNVNPWPAMNEAEFTNSGGDISFGGGVTGFAHSGGQTGQLESLPHNVVHTDINGAMGNPDTAALDPIFWLHHANIDRLWQVWLAQAGRSNPVVNAWKDFRFKFHDANGQPVEIAVKDVETTQLLGYVYTPAFPLSSTTPARRSVPAMDVVGATSASFSVGDHMAPLDLTMVPQPARGARLLAARGGDEKRTILRISNVKGKGATSPIDLFITNRDNEEGNEENFVGCIGLFGLENASTPSVESDGSGLNFAIDISDTINKLRQRDDWDEDNIRVQLIPQSKQDSDVEINVGRVSLHSEID

[Multiple Choices]
A. pantetheine 4'-phosphate
B. Cu(2+)
C. Fe(2+)
D. heme
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

> The exact sequence matches UniProt entry A0A261GRE4, annotated as tyrosinase HcTyr1. Its Cu(2+) cofactor annotation cites experimental evidence from PubMed 39382070 and notes two copper ions per subunit. The cited paper covers cofactor and catalytic activity, though the supplied excerpts do not independently detail the assay.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Tyrosinases are copper-dependent enzymes, and the sequence has multiple histidines compatible with metal binding. But the input does not establish that this protein is a tyrosinase; histidines alone do not uniquely distinguish copper from the other choices.


**Missing item-specific fact**

> The protein's identity/function as tyrosinase HcTyr1, or an equivalent protein-specific cofactor annotation or experimental result.


**Reason**

> Choosing Cu(2+) is supported once the protein is identified as a tyrosinase, but that identity and the experimentally reported cofactor are not supplied. Inferring them requires protein-specific recognition or external annotation, rather than a decisive argument from the provided sequence and choices alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports Cu(2+); the evidence does not support another listed choice.


### Important caveats

- Reviewer-only database and publication evidence was not available to the evaluated model.
- The cofactor assertion is experimental-evidence-coded in UniProt, but the primary study was not independently retrieved or fully assessed here.
- The historical UniProt sequence match is exact; the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Tyrosinases are copper-dependent enzymes, and the sequence has multiple histidines compatible with metal binding. But the input does not establish that this protein is a tyrosinase; histidines alone do not uniquely distinguish copper from the other choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity/function as tyrosinase HcTyr1, or an equivalent protein-specific cofactor annotation or experimental result.",
    "reason": "Choosing Cu(2+) is supported once the protein is identified as a tyrosinase, but that identity and the experimentally reported cofactor are not supplied. Inferring them requires protein-specific recognition or external annotation, rather than a decisive argument from the provided sequence and choices alone."
  },
  "case_id": "cofactor_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry A0A261GRE4, annotated as tyrosinase HcTyr1. Its Cu(2+) cofactor annotation cites experimental evidence from PubMed 39382070 and notes two copper ions per subunit. The cited paper covers cofactor and catalytic activity, though the supplied excerpts do not independently detail the assay."
  },
  "important_caveats": [
    "Reviewer-only database and publication evidence was not available to the evaluated model.",
    "The cofactor assertion is experimental-evidence-coded in UniProt, but the primary study was not independently retrieved or fully assessed here.",
    "The historical UniProt sequence match is exact; the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports Cu(2+); the evidence does not support another listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches UniProt entry A0A261GRE4, annotated as tyrosinase HcTyr1. Its Cu(2+) cofactor annotation cites experimental evidence from PubMed 39382070 and notes two copper ions per subunit. The cited paper covers cofactor and catalytic activity, though the supplied excerpts do not independently detail the assay.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Tyrosinases are copper-dependent enzymes, and the sequence has multiple histidines compatible with metal binding. But the input does not establish that this protein is a tyrosinase; histidines alone do not uniquely distinguish copper from the other choices.",
    "missing_item_specific_fact": "The protein's identity/function as tyrosinase HcTyr1, or an equivalent protein-specific cofactor annotation or experimental result.",
    "reason": "Choosing Cu(2+) is supported once the protein is identified as a tyrosinase, but that identity and the experimentally reported cofactor are not supplied. Inferring them requires protein-specific recognition or external annotation, rather than a decisive argument from the provided sequence and choices alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports Cu(2+); the evidence does not support another listed choice."
  },
  "important_caveats": [
    "Reviewer-only database and publication evidence was not available to the evaluated model.",
    "The cofactor assertion is experimental-evidence-coded in UniProt, but the primary study was not independently retrieved or fully assessed here.",
    "The historical UniProt sequence match is exact; the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A261GRE4 (Tyrosinase HcTyr1, EC 1.14.18.1) from Hahella sp. CCB-MM4 explicitly annotates Cu(2+) (ChEBI:29036) as the cofactor, with direct experimental evidence (ECO:0000269, PubMed:39382070) and X-ray crystallography at 1.97 Å (PDB:8B74). The note states 'Binds 2 copper ions per subunit.' Tyrosinases (EC 1.14.18.1) are a well-established binuclear copper enzyme class. The sequence in the question matches the UniProt entry exactly (466 aa, SHA-256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains multiple histidine-rich regions (e.g., 'HGYATY', 'HGY' motifs, 'HSEID') that are consistent with copper-coordinating sites in binuclear copper oxidases. Tyrosinases are textbook copper-dependent enzymes with a binuclear CuA/CuB center coordinated by six histidines. One could argue that histidine-dense motifs and the absence of heme-binding motifs (no CXXCH) or acyltransferase signatures narrow the choices. However, histidine-rich coordination is equally common in Fe(2+)-dependent enzymes (e.g., Fe(II)/α-ketoglutarate dioxygenases, catechol dioxygenases), so the histidine pattern alone does not definitively distinguish Cu(2+) from Fe(2+).


**Missing item-specific fact**

> Confident identification of this specific 466-aa sequence as a tyrosinase (EC 1.14.18.1) — and therefore as a copper-dependent enzyme — requires either recognition of the tyrosinase protein family from sequence motifs or a database lookup. The linear sequence does not provide a unique, unambiguous signature that separates tyrosinase-type binuclear copper coordination from other histidine-coordinated metal centers (especially Fe(2+)) without family-level identification.


**Reason**

> While the histidine-rich regions and absence of heme/pantetheine motifs allow elimination of choices A and D through general reasoning, the critical Cu(2+) vs Fe(2+) distinction depends on recognizing this protein as a tyrosinase. Tyrosinase identity from a 466-aa bacterial sequence is not reliably deducible from generic sequence heuristics alone; it requires either memorization of the tyrosinase sequence family or database annotation. The well-known copper dependence of tyrosinases is textbook knowledge, but applying it here presupposes correctly identifying the enzyme family from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Without family-level identification, a histidine-rich metalloprotein of ~466 aa could plausibly be an Fe(2+)-dependent enzyme (e.g., a catechol dioxygenase or Fe(II)/αKG oxidase), making choice C (Fe(2+)) a defensible alternative based on sequence features alone. The question's wording does not provide functional context (e.g., 'this protein oxidizes tyrosine') that would unambiguously select tyrosinase over other histidine-coordinated metal enzymes.


### Important caveats

- The sequence-to-accession mapping (A0A261GRE4) was inferred by the reviewer from dataset metadata, not from the evaluated model's input; the model received only the raw sequence.
- The cofactor annotation carries evidence code ECO:0000269 (direct assay) from PubMed:39382070, indicating experimental verification rather than computational prediction.
- The binuclear copper center detail ('Binds 2 copper ions per subunit') is partially transferred by similarity (ECO:0000250, UniProtKB:Q9ZP19), though the primary cofactor assignment is experimentally supported.
- The protein was first publicly released in UniProt on 2025-02-05; the author's source snapshot date is unknown, so the annotation may or may not have been available at question-construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple histidine-rich regions (e.g., 'HGYATY', 'HGY' motifs, 'HSEID') that are consistent with copper-coordinating sites in binuclear copper oxidases. Tyrosinases are textbook copper-dependent enzymes with a binuclear CuA/CuB center coordinated by six histidines. One could argue that histidine-dense motifs and the absence of heme-binding motifs (no CXXCH) or acyltransferase signatures narrow the choices. However, histidine-rich coordination is equally common in Fe(2+)-dependent enzymes (e.g., Fe(II)/α-ketoglutarate dioxygenases, catechol dioxygenases), so the histidine pattern alone does not definitively distinguish Cu(2+) from Fe(2+).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Confident identification of this specific 466-aa sequence as a tyrosinase (EC 1.14.18.1) — and therefore as a copper-dependent enzyme — requires either recognition of the tyrosinase protein family from sequence motifs or a database lookup. The linear sequence does not provide a unique, unambiguous signature that separates tyrosinase-type binuclear copper coordination from other histidine-coordinated metal centers (especially Fe(2+)) without family-level identification.",
    "reason": "While the histidine-rich regions and absence of heme/pantetheine motifs allow elimination of choices A and D through general reasoning, the critical Cu(2+) vs Fe(2+) distinction depends on recognizing this protein as a tyrosinase. Tyrosinase identity from a 466-aa bacterial sequence is not reliably deducible from generic sequence heuristics alone; it requires either memorization of the tyrosinase sequence family or database annotation. The well-known copper dependence of tyrosinases is textbook knowledge, but applying it here presupposes correctly identifying the enzyme family from the sequence."
  },
  "case_id": "cofactor_0021",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A261GRE4 (Tyrosinase HcTyr1, EC 1.14.18.1) from Hahella sp. CCB-MM4 explicitly annotates Cu(2+) (ChEBI:29036) as the cofactor, with direct experimental evidence (ECO:0000269, PubMed:39382070) and X-ray crystallography at 1.97 Å (PDB:8B74). The note states 'Binds 2 copper ions per subunit.' Tyrosinases (EC 1.14.18.1) are a well-established binuclear copper enzyme class. The sequence in the question matches the UniProt entry exactly (466 aa, SHA-256 confirmed)."
  },
  "important_caveats": [
    "The sequence-to-accession mapping (A0A261GRE4) was inferred by the reviewer from dataset metadata, not from the evaluated model's input; the model received only the raw sequence.",
    "The cofactor annotation carries evidence code ECO:0000269 (direct assay) from PubMed:39382070, indicating experimental verification rather than computational prediction.",
    "The binuclear copper center detail ('Binds 2 copper ions per subunit') is partially transferred by similarity (ECO:0000250, UniProtKB:Q9ZP19), though the primary cofactor assignment is experimentally supported.",
    "The protein was first publicly released in UniProt on 2025-02-05; the author's source snapshot date is unknown, so the annotation may or may not have been available at question-construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Without family-level identification, a histidine-rich metalloprotein of ~466 aa could plausibly be an Fe(2+)-dependent enzyme (e.g., a catechol dioxygenase or Fe(II)/αKG oxidase), making choice C (Fe(2+)) a defensible alternative based on sequence features alone. The question's wording does not provide functional context (e.g., 'this protein oxidizes tyrosine') that would unambiguously select tyrosinase over other histidine-coordinated metal enzymes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0021",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A261GRE4 (Tyrosinase HcTyr1, EC 1.14.18.1) from Hahella sp. CCB-MM4 explicitly annotates Cu(2+) (ChEBI:29036) as the cofactor, with direct experimental evidence (ECO:0000269, PubMed:39382070) and X-ray crystallography at 1.97 Å (PDB:8B74). The note states 'Binds 2 copper ions per subunit.' Tyrosinases (EC 1.14.18.1) are a well-established binuclear copper enzyme class. The sequence in the question matches the UniProt entry exactly (466 aa, SHA-256 confirmed).",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains multiple histidine-rich regions (e.g., 'HGYATY', 'HGY' motifs, 'HSEID') that are consistent with copper-coordinating sites in binuclear copper oxidases. Tyrosinases are textbook copper-dependent enzymes with a binuclear CuA/CuB center coordinated by six histidines. One could argue that histidine-dense motifs and the absence of heme-binding motifs (no CXXCH) or acyltransferase signatures narrow the choices. However, histidine-rich coordination is equally common in Fe(2+)-dependent enzymes (e.g., Fe(II)/α-ketoglutarate dioxygenases, catechol dioxygenases), so the histidine pattern alone does not definitively distinguish Cu(2+) from Fe(2+).",
    "missing_item_specific_fact": "Confident identification of this specific 466-aa sequence as a tyrosinase (EC 1.14.18.1) — and therefore as a copper-dependent enzyme — requires either recognition of the tyrosinase protein family from sequence motifs or a database lookup. The linear sequence does not provide a unique, unambiguous signature that separates tyrosinase-type binuclear copper coordination from other histidine-coordinated metal centers (especially Fe(2+)) without family-level identification.",
    "reason": "While the histidine-rich regions and absence of heme/pantetheine motifs allow elimination of choices A and D through general reasoning, the critical Cu(2+) vs Fe(2+) distinction depends on recognizing this protein as a tyrosinase. Tyrosinase identity from a 466-aa bacterial sequence is not reliably deducible from generic sequence heuristics alone; it requires either memorization of the tyrosinase sequence family or database annotation. The well-known copper dependence of tyrosinases is textbook knowledge, but applying it here presupposes correctly identifying the enzyme family from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Without family-level identification, a histidine-rich metalloprotein of ~466 aa could plausibly be an Fe(2+)-dependent enzyme (e.g., a catechol dioxygenase or Fe(II)/αKG oxidase), making choice C (Fe(2+)) a defensible alternative based on sequence features alone. The question's wording does not provide functional context (e.g., 'this protein oxidizes tyrosine') that would unambiguously select tyrosinase over other histidine-coordinated metal enzymes."
  },
  "important_caveats": [
    "The sequence-to-accession mapping (A0A261GRE4) was inferred by the reviewer from dataset metadata, not from the evaluated model's input; the model received only the raw sequence.",
    "The cofactor annotation carries evidence code ECO:0000269 (direct assay) from PubMed:39382070, indicating experimental verification rather than computational prediction.",
    "The binuclear copper center detail ('Binds 2 copper ions per subunit') is partially transferred by similarity (ECO:0000250, UniProtKB:Q9ZP19), though the primary cofactor assignment is experimentally supported.",
    "The protein was first publicly released in UniProt on 2025-02-05; the author's source snapshot date is unknown, so the annotation may or may not have been available at question-construction time."
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

**Accession:** `A0A261GRE4` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 24. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.415551+00:00.  

```json
"A0A261GRE4"
```

Source SHA-256: `00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.415551+00:00.  

```json
{"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"39382070","source":"PubMed"}],"value":"1.14.18.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39382070","source":"PubMed"}],"value":"Tyrosinase HcTyr1"}}}
```

Source SHA-256: `00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)  
**Locator:** `/comments/4`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.415551+00:00.  

```json
{"cofactors":[{"cofactorCrossReference":{"database":"ChEBI","id":"CHEBI:29036"},"evidences":[{"evidenceCode":"ECO:0000269","id":"39382070","source":"PubMed"}],"name":"Cu(2+)"}],"commentType":"COFACTOR","note":{"texts":[{"evidences":[{"evidenceCode":"ECO:0000250","id":"Q9ZP19","source":"UniProtKB"}],"value":"Binds 2 copper ions per subunit."}]}}
```

Source SHA-256: `00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A261GRE4.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:24:44.415551+00:00.  

```json
{"citation":{"authors":["de Almeida Santos G.","Englund A.N.B.","Dalleywater E.L.","Roehr A.K."],"citationCrossReferences":[{"database":"PubMed","id":"39382070"},{"database":"DOI","id":"10.1002/2211-5463.13906"}],"citationType":"journal article","firstPage":"0","id":"39382070","journal":"FEBS Open Bio","lastPage":"0","publicationDate":"2024","title":"Characterization of two bacterial tyrosinases from the halophilic bacterium Hahella sp. CCB MM4 relevant for phenolic compounds oxidation in wetlands.","volume":"0"},"evidences":[{"evidenceCode":"ECO:0007744","id":"8B74","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"CCB-MM4"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.97 ANGSTROMS)","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","ACTIVITY REGULATION","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","DOMAIN","AUTO-CLEAVAGE"]}
```

Source SHA-256: `00e853efb86efbba5cdbab717d33f340d1b016940ad494e620198c6b6fe6926b`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)  
**Locator:** `lines 1-12`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 24 / 1.  
**Retrieved:** 2026-11-01T06:27:24.781945+00:00.  

```text
ID   TYR1_HAHS4              Reviewed;         466 AA.
AC   A0A261GRE4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   20-DEC-2017, sequence version 1.
DT   28-JAN-2026, entry version 24.
DE   RecName: Full=Tyrosinase HcTyr1 {ECO:0000303|PubMed:39382070};
DE            EC=1.14.18.1 {ECO:0000269|PubMed:39382070};
GN   ORFNames=BTA51_09820 {ECO:0000312|EMBL:OZG74058.1};
OS   Hahella sp. (strain CCB-MM4).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Oceanospirillales; Hahellaceae; Hahella.
OX   NCBI_TaxID=1926491;
```

Source SHA-256: `68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)  
**Locator:** `lines 6-7`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 24 / 1.  
**Retrieved:** 2026-11-01T06:27:24.781945+00:00.  

```text
DE   RecName: Full=Tyrosinase HcTyr1 {ECO:0000303|PubMed:39382070};
DE            EC=1.14.18.1 {ECO:0000269|PubMed:39382070};
```

Source SHA-256: `68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)  
**Locator:** `lines 21-31`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 24 / 1.  
**Retrieved:** 2026-11-01T06:27:24.781945+00:00.  

```text
RN   [2] {ECO:0007744|PDB:8B74}
RP   X-RAY CRYSTALLOGRAPHY (1.97 ANGSTROMS), FUNCTION, CATALYTIC ACTIVITY,
RP   COFACTOR, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT,
RP   DOMAIN, AND AUTO-CLEAVAGE.
RC   STRAIN=CCB-MM4;
RX   PubMed=39382070; DOI=10.1002/2211-5463.13906;
RA   de Almeida Santos G., Englund A.N.B., Dalleywater E.L., Roehr A.K.;
RT   "Characterization of two bacterial tyrosinases from the halophilic
RT   bacterium Hahella sp. CCB MM4 relevant for phenolic compounds oxidation in
RT   wetlands.";
RL   FEBS Open Bio 0:0-0(2024).
```

Source SHA-256: `68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A261GRE4?format=txt&versions=24)  
**Locator:** `lines 52-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 24 / 1.  
**Retrieved:** 2026-11-01T06:27:24.781945+00:00.  

```text
CC   -!- COFACTOR:
CC       Name=Cu(2+); Xref=ChEBI:CHEBI:29036;
CC         Evidence={ECO:0000269|PubMed:39382070};
CC       Note=Binds 2 copper ions per subunit. {ECO:0000250|UniProtKB:Q9ZP19};
```

Source SHA-256: `68a25263649df9c2d086d0a4f0628b7a3aea5833d736f28bc21ffa7fac2f002c`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 21. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
