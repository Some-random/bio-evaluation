# pathway_0161

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **B** — Alkaloid biosynthesis. .

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
METVESSSSAELLRAQTHFSRQVFSFQNFAALKCALQLGIPDAIKQHGKPMNLSELTSALPINPSKAPCIHRLMRLLVNAGYFAQENECFALTSLGRLLLKDDPLHIRALVLSEFHTALVMPWFALSEWFKNDDVAPFATAHGKSFWDYTSCDPELRNVFDGAMACDSHLIAKALVTEFKYLFEGLKSLVDVGGGNGTLARSIAKAFTNLKCTVCDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKSILHDWSDENCVKILKNCKRAISGKDKGGKVIVIDGVVELQKKAGNDDPGLDNMDMQMLVLFNSKERNEKEWAKLFSDAGFSDYGIVRTFGWWCIMELSP

[Multiple Choices]
A. Lipid metabolism. .
B. Alkaloid biosynthesis. .
C. L-methionine biosynthesis via de novo pathway. .
D. CoA from (R)-pantothenate: step 3/5. .
```

<details>
<summary>Original system instructions, verbatim</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact 350-aa sequence matches the UniProt entry for IpeOMT1. Its pathway annotation is alkaloid biosynthesis and is linked to a cited experimental-evidence code; the referenced study concerns O-methylation reactions in ipecac alkaloid biosynthesis.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with an enzyme, but the supplied input provides no biological source or substrate context that specifically connects it to alkaloid biosynthesis rather than the other listed pathways.


**Missing item-specific fact**

> The protein-specific identity and experimentally characterized substrate/function of IpeOMT1, including its role in ipecac alkaloid O-methylation.


**Reason**

> Identifying the pathway requires a protein-specific functional annotation or equivalent external knowledge. Generic sequence features of a methyltransferase would not establish this pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation and cited functional study support choice B; the evidence does not identify another listed pathway as a competing function.


### Important caveats

- The UniProt pathway annotation is evidence-linked to a cited publication, but the primary paper was not independently retrieved or validated here.
- Reviewer-only accession and annotation evidence were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with an enzyme, but the supplied input provides no biological source or substrate context that specifically connects it to alkaloid biosynthesis rather than the other listed pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity and experimentally characterized substrate/function of IpeOMT1, including its role in ipecac alkaloid O-methylation.",
    "reason": "Identifying the pathway requires a protein-specific functional annotation or equivalent external knowledge. Generic sequence features of a methyltransferase would not establish this pathway."
  },
  "case_id": "pathway_0161",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact 350-aa sequence matches the UniProt entry for IpeOMT1. Its pathway annotation is alkaloid biosynthesis and is linked to a cited experimental-evidence code; the referenced study concerns O-methylation reactions in ipecac alkaloid biosynthesis."
  },
  "important_caveats": [
    "The UniProt pathway annotation is evidence-linked to a cited publication, but the primary paper was not independently retrieved or validated here.",
    "Reviewer-only accession and annotation evidence were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and cited functional study support choice B; the evidence does not identify another listed pathway as a competing function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 350-aa sequence matches the UniProt entry for IpeOMT1. Its pathway annotation is alkaloid biosynthesis and is linked to a cited experimental-evidence code; the referenced study concerns O-methylation reactions in ipecac alkaloid biosynthesis.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with an enzyme, but the supplied input provides no biological source or substrate context that specifically connects it to alkaloid biosynthesis rather than the other listed pathways.",
    "missing_item_specific_fact": "The protein-specific identity and experimentally characterized substrate/function of IpeOMT1, including its role in ipecac alkaloid O-methylation.",
    "reason": "Identifying the pathway requires a protein-specific functional annotation or equivalent external knowledge. Generic sequence features of a methyltransferase would not establish this pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation and cited functional study support choice B; the evidence does not identify another listed pathway as a competing function."
  },
  "important_caveats": [
    "The UniProt pathway annotation is evidence-linked to a cited publication, but the primary paper was not independently retrieved or validated here.",
    "Reviewer-only accession and annotation evidence were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry D3KY98 (OMT1_CARIP, Cephaeline 6'-O-methyltransferase IpeOMT1 from Carapichea ipecacuanha) explicitly annotates PATHWAY: Alkaloid biosynthesis with experimental evidence code ECO:0000269 (PubMed:20061395, Nomura & Kutchan 2010 JBC). The protein catalyzes O-methylation reactions in ipecac/benzylisoquinoline alkaloid biosynthesis. The expected answer B is directly and experimentally supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The ~350 aa sequence contains motifs consistent with a plant SAM-dependent O-methyltransferase fold (e.g., the GDKGGKVIVIDGVVELQ region resembling catalytic/SAM-binding motifs of class I plant OMTs). Plant O-methyltransferases function predominantly in secondary metabolite biosynthesis (alkaloids, lignins, flavonoids). Among the four choices, only B (alkaloid biosynthesis) is a secondary metabolite pathway involving O-methyltransferases. Choices C (L-methionine biosynthesis) and D (CoA from pantothenate step 3/5) involve fundamentally different enzyme classes (homoserine O-succinyltransferase/cystathionine gamma-synthase; phosphopantothenoylcysteine synthetase/decarboxylase), not O-methyltransferases. Choice A (lipid metabolism) does not typically employ O-methyltransferases as pathway-defining enzymes. Thus, identifying the OMT fold and applying general knowledge of plant OMT pathway distribution meaningfully distinguishes B from the distractors.


**Missing item-specific fact**

> None critical. The specific substrate (cephaline, norcoclaurine) and the exact ipecac pathway position would require database lookup, but the pathway-level assignment is reachable via the OMT-fold → plant secondary metabolism → alkaloid biosynthesis reasoning chain.


**Reason**

> A model can (a) recognize methyltransferase sequence motifs and length, (b) eliminate C and D because their pathway-defining enzymes are not methyltransferases, (c) eliminate A because lipid metabolism does not center on O-methyltransferases, and (d) select B because plant OMTs are overwhelmingly associated with alkaloid/secondary metabolite biosynthesis. This is a general biological reasoning chain, not an item-specific database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices C and D involve enzymes of entirely different mechanistic classes (ligases, transferases of non-methyl groups) incompatible with an OMT fold. Choice A (lipid metabolism) is not a recognized pathway for plant O-methyltransferases. Only B is consistent with both the identified enzyme class and the plant context. No other option is defensible given the sequence features.


### Important caveats

- The OMT motif identification from this particular sequence is not trivially obvious to all models; the conserved GxGxG/VLDVG motifs are somewhat degenerate in this entry.
- The reasoning chain (OMT → plant secondary metabolism → alkaloids) is probabilistic rather than deductive; a model might hesitate between B and a hypothetical 'lignin biosynthesis' option if one were present, but no such option is offered here.
- The UniProt annotation carries experimental evidence (ECO:0000269), making the key well-grounded, but the model at test time has no access to this annotation.
- The source is a plant (Carapichea ipecacuanha, Rubiaceae); this organismal context is not stated in the question but can be weakly inferred from sequence composition.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The ~350 aa sequence contains motifs consistent with a plant SAM-dependent O-methyltransferase fold (e.g., the GDKGGKVIVIDGVVELQ region resembling catalytic/SAM-binding motifs of class I plant OMTs). Plant O-methyltransferases function predominantly in secondary metabolite biosynthesis (alkaloids, lignins, flavonoids). Among the four choices, only B (alkaloid biosynthesis) is a secondary metabolite pathway involving O-methyltransferases. Choices C (L-methionine biosynthesis) and D (CoA from pantothenate step 3/5) involve fundamentally different enzyme classes (homoserine O-succinyltransferase/cystathionine gamma-synthase; phosphopantothenoylcysteine synthetase/decarboxylase), not O-methyltransferases. Choice A (lipid metabolism) does not typically employ O-methyltransferases as pathway-defining enzymes. Thus, identifying the OMT fold and applying general knowledge of plant OMT pathway distribution meaningfully distinguishes B from the distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The specific substrate (cephaline, norcoclaurine) and the exact ipecac pathway position would require database lookup, but the pathway-level assignment is reachable via the OMT-fold → plant secondary metabolism → alkaloid biosynthesis reasoning chain.",
    "reason": "A model can (a) recognize methyltransferase sequence motifs and length, (b) eliminate C and D because their pathway-defining enzymes are not methyltransferases, (c) eliminate A because lipid metabolism does not center on O-methyltransferases, and (d) select B because plant OMTs are overwhelmingly associated with alkaloid/secondary metabolite biosynthesis. This is a general biological reasoning chain, not an item-specific database lookup."
  },
  "case_id": "pathway_0161",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry D3KY98 (OMT1_CARIP, Cephaeline 6'-O-methyltransferase IpeOMT1 from Carapichea ipecacuanha) explicitly annotates PATHWAY: Alkaloid biosynthesis with experimental evidence code ECO:0000269 (PubMed:20061395, Nomura & Kutchan 2010 JBC). The protein catalyzes O-methylation reactions in ipecac/benzylisoquinoline alkaloid biosynthesis. The expected answer B is directly and experimentally supported."
  },
  "important_caveats": [
    "The OMT motif identification from this particular sequence is not trivially obvious to all models; the conserved GxGxG/VLDVG motifs are somewhat degenerate in this entry.",
    "The reasoning chain (OMT → plant secondary metabolism → alkaloids) is probabilistic rather than deductive; a model might hesitate between B and a hypothetical 'lignin biosynthesis' option if one were present, but no such option is offered here.",
    "The UniProt annotation carries experimental evidence (ECO:0000269), making the key well-grounded, but the model at test time has no access to this annotation.",
    "The source is a plant (Carapichea ipecacuanha, Rubiaceae); this organismal context is not stated in the question but can be weakly inferred from sequence composition."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices C and D involve enzymes of entirely different mechanistic classes (ligases, transferases of non-methyl groups) incompatible with an OMT fold. Choice A (lipid metabolism) is not a recognized pathway for plant O-methyltransferases. Only B is consistent with both the identified enzyme class and the plant context. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0161",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry D3KY98 (OMT1_CARIP, Cephaeline 6'-O-methyltransferase IpeOMT1 from Carapichea ipecacuanha) explicitly annotates PATHWAY: Alkaloid biosynthesis with experimental evidence code ECO:0000269 (PubMed:20061395, Nomura & Kutchan 2010 JBC). The protein catalyzes O-methylation reactions in ipecac/benzylisoquinoline alkaloid biosynthesis. The expected answer B is directly and experimentally supported.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The ~350 aa sequence contains motifs consistent with a plant SAM-dependent O-methyltransferase fold (e.g., the GDKGGKVIVIDGVVELQ region resembling catalytic/SAM-binding motifs of class I plant OMTs). Plant O-methyltransferases function predominantly in secondary metabolite biosynthesis (alkaloids, lignins, flavonoids). Among the four choices, only B (alkaloid biosynthesis) is a secondary metabolite pathway involving O-methyltransferases. Choices C (L-methionine biosynthesis) and D (CoA from pantothenate step 3/5) involve fundamentally different enzyme classes (homoserine O-succinyltransferase/cystathionine gamma-synthase; phosphopantothenoylcysteine synthetase/decarboxylase), not O-methyltransferases. Choice A (lipid metabolism) does not typically employ O-methyltransferases as pathway-defining enzymes. Thus, identifying the OMT fold and applying general knowledge of plant OMT pathway distribution meaningfully distinguishes B from the distractors.",
    "missing_item_specific_fact": "None critical. The specific substrate (cephaline, norcoclaurine) and the exact ipecac pathway position would require database lookup, but the pathway-level assignment is reachable via the OMT-fold → plant secondary metabolism → alkaloid biosynthesis reasoning chain.",
    "reason": "A model can (a) recognize methyltransferase sequence motifs and length, (b) eliminate C and D because their pathway-defining enzymes are not methyltransferases, (c) eliminate A because lipid metabolism does not center on O-methyltransferases, and (d) select B because plant OMTs are overwhelmingly associated with alkaloid/secondary metabolite biosynthesis. This is a general biological reasoning chain, not an item-specific database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices C and D involve enzymes of entirely different mechanistic classes (ligases, transferases of non-methyl groups) incompatible with an OMT fold. Choice A (lipid metabolism) is not a recognized pathway for plant O-methyltransferases. Only B is consistent with both the identified enzyme class and the plant context. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The OMT motif identification from this particular sequence is not trivially obvious to all models; the conserved GxGxG/VLDVG motifs are somewhat degenerate in this entry.",
    "The reasoning chain (OMT → plant secondary metabolism → alkaloids) is probabilistic rather than deductive; a model might hesitate between B and a hypothetical 'lignin biosynthesis' option if one were present, but no such option is offered here.",
    "The UniProt annotation carries experimental evidence (ECO:0000269), making the key well-grounded, but the model at test time has no access to this annotation.",
    "The source is a plant (Carapichea ipecacuanha, Rubiaceae); this organismal context is not stated in the question but can be weakly inferred from sequence composition."
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

**Accession:** `D3KY98` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 56. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:02.422509+00:00.  

```json
"D3KY98"
```

Source SHA-256: `19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:02.422509+00:00.  

```json
{"alternativeNames":[{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.128"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"(R,S)-norcoclaurine 6-O-methyltransferase IpeOMT1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"Coclaurine synthase IpeOMT1"}]},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"(R,S)-norprotosinomenine 6-O-methyltransferase IpeOMT1"}},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"7-O-methyl-N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1"}},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"Ipecac/benzylisoquinoline alkaloid O-methyltransferase 1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"},{"evidenceCode":"ECO:0000312","id":"BAI79243.1","source":"EMBL"}],"value":"IpeOMT1"}]},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"Isococlaurine 6-O-methyltransferase IpeOMT1"}},{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"2.1.1.396"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"Cephaeline 6'-O-methyltransferase IpeOMT1"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"20061395","source":"PubMed"}],"value":"Emetine synthase IpeOMT1"}]}}
```

Source SHA-256: `19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)  
**Locator:** `/comments/8`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:02.422509+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"20061395","source":"PubMed"}],"value":"Alkaloid biosynthesis"}]}
```

Source SHA-256: `19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D3KY98.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:02.422509+00:00.  

```json
{"citation":{"authors":["Nomura T.","Kutchan T.M."],"citationCrossReferences":[{"database":"PubMed","id":"20061395"},{"database":"DOI","id":"10.1074/jbc.m109.086157"}],"citationType":"journal article","firstPage":"7722","id":"20061395","journal":"J. Biol. Chem.","lastPage":"7738","publicationDate":"2010","title":"Three new O-methyltransferases are sufficient for all O-methylation reactions of ipecac alkaloid biosynthesis in root culture of Psychotria ipecacuanha.","volume":"285"},"evidences":[{"evidenceCode":"ECO:0000312","id":"BAI79243.1","source":"EMBL"}],"referenceComments":[{"type":"TISSUE","value":"Root"}],"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [MRNA]","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","SUBCELLULAR LOCATION","PATHWAY","TISSUE SPECIFICITY"]}
```

Source SHA-256: `19b6f572b17e083c89247122e314ad458ae0c6830eb2f6fd9037dae0b0ba85fb`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)  
**Locator:** `lines 1-29`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 56 / 1.  
**Retrieved:** 2026-11-01T06:27:56.372657+00:00.  

```text
ID   OMT1_CARIP              Reviewed;         350 AA.
AC   D3KY98;
DT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.
DT   20-APR-2010, sequence version 1.
DT   28-JAN-2026, entry version 56.
DE   RecName: Full=Cephaeline 6'-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            Short=Emetine synthase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            EC=2.1.1.396 {ECO:0000269|PubMed:20061395};
DE   AltName: Full=(R,S)-norcoclaurine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            Short=Coclaurine synthase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            EC=2.1.1.128 {ECO:0000269|PubMed:20061395};
DE   AltName: Full=(R,S)-norprotosinomenine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};
DE   AltName: Full=7-O-methyl-N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};
DE   AltName: Full=Ipecac/benzylisoquinoline alkaloid O-methyltransferase 1 {ECO:0000303|PubMed:20061395};
DE            Short=IpeOMT1 {ECO:0000303|PubMed:20061395, ECO:0000312|EMBL:BAI79243.1};
DE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};
DE   AltName: Full=Isococlaurine 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};
DE   AltName: Full=N-deacetylisoipecoside 6-O-methyltransferase IpeOMT1 {ECO:0000303|PubMed:20061395};
DE            EC=2.1.1.- {ECO:0000269|PubMed:20061395};
GN   Name=OMT1 {ECO:0000303|PubMed:20061395};
OS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).
OC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
OC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;
OC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;
OC   Carapichea.
OX   NCBI_TaxID=77880;
```

Source SHA-256: `249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D3KY98?format=txt&versions=56)  
**Locator:** `lines 129-129`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 56 / 1.  
**Retrieved:** 2026-11-01T06:27:56.372657+00:00.  

```text
CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:20061395}.
```

Source SHA-256: `249d7589109d17284287fa739c8c561ac8c25a9cbe30bbf7a2f9eff0d76959bb`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 161. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
