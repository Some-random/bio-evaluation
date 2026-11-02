# catalytic_activity_0094

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `catalytic_activity`  
**Author expected answer:** **B** — desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol + S-adenosyl-L-homocysteine + H(+)

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MTLQPTAADVGAMYDQYTSLLTDVMAGFIHVGYWEDPSSEETMEVATERMTREVGARLSSSAGQHILDVGCGTGKSAVQIANTHGVQITGITVSKSQIEEAQALYGSAVQAGQVSYQFANAMDLPFADASFDGAYAIESLVHMDDRRTALQNIARVLRPGSRLAIADLCLDAHCPNPEALARFHELFQVPPMSSGEELQELLRETGFRVLEFTDIRDNVRPVCKFLEKKALSLEGEVGEKLLEIATSMATLKELGYAFITAERI

[Multiple Choices]
A. UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate
B. desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol + S-adenosyl-L-homocysteine + H(+)
C. a cytidine in mRNA + acetyl-CoA + ATP + H2O = an N(4)-acetylcytidine in mRNA + ADP + phosphate + CoA + H(+)
D. Fe(2+)(in) = Fe(2+)(out)
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

> The supplied sequence exactly matches the UniProt entry annotated as O-methyltransferase ResE, whose catalytic-activity annotation gives choice B. The annotation cites a 2024 paper reporting function and pathway work. This supports the key, though the excerpts alone do not independently establish the experimental details behind that annotation.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a soluble enzyme, which makes the iron-transport option less plausible, and choice B is a SAM-dependent methylation reaction. But the sequence and choices do not establish that this protein acts on desmethylrestrictinol rather than another substrate.


**Missing item-specific fact**

> The protein-specific functional assignment linking this sequence to ResE and the methylation of desmethylrestrictinol to restrictinol.


**Reason**

> General sequence reasoning may help distinguish broad enzyme classes, but selecting the exact substrate and products in B requires a protein-specific annotation or experimental result absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices describe distinct reactions, and the available reviewer evidence supports B for the sequence-matched protein; the lack of enough input information for a solver to infer that fact does not make another choice equally defensible.


### Important caveats

- The UniProt sequence match is exact, and the archived annotation available by the stated historical cutoff also records choice B.
- The evidence excerpts report a database annotation citing a paper; the primary study was not independently retrieved or validated here.
- Reviewer-only accession and annotation evidence were not supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme, which makes the iron-transport option less plausible, and choice B is a SAM-dependent methylation reaction. But the sequence and choices do not establish that this protein acts on desmethylrestrictinol rather than another substrate.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment linking this sequence to ResE and the methylation of desmethylrestrictinol to restrictinol.",
    "reason": "General sequence reasoning may help distinguish broad enzyme classes, but selecting the exact substrate and products in B requires a protein-specific annotation or experimental result absent from the input."
  },
  "case_id": "catalytic_activity_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as O-methyltransferase ResE, whose catalytic-activity annotation gives choice B. The annotation cites a 2024 paper reporting function and pathway work. This supports the key, though the excerpts alone do not independently establish the experimental details behind that annotation."
  },
  "important_caveats": [
    "The UniProt sequence match is exact, and the archived annotation available by the stated historical cutoff also records choice B.",
    "The evidence excerpts report a database annotation citing a paper; the primary study was not independently retrieved or validated here.",
    "Reviewer-only accession and annotation evidence were not supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reactions, and the available reviewer evidence supports B for the sequence-matched protein; the lack of enough input information for a solver to infer that fact does not make another choice equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as O-methyltransferase ResE, whose catalytic-activity annotation gives choice B. The annotation cites a 2024 paper reporting function and pathway work. This supports the key, though the excerpts alone do not independently establish the experimental details behind that annotation.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme, which makes the iron-transport option less plausible, and choice B is a SAM-dependent methylation reaction. But the sequence and choices do not establish that this protein acts on desmethylrestrictinol rather than another substrate.",
    "missing_item_specific_fact": "The protein-specific functional assignment linking this sequence to ResE and the methylation of desmethylrestrictinol to restrictinol.",
    "reason": "General sequence reasoning may help distinguish broad enzyme classes, but selecting the exact substrate and products in B requires a protein-specific annotation or experimental result absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices describe distinct reactions, and the available reviewer evidence supports B for the sequence-matched protein; the lack of enough input information for a solver to infer that fact does not make another choice equally defensible."
  },
  "important_caveats": [
    "The UniProt sequence match is exact, and the archived annotation available by the stated historical cutoff also records choice B.",
    "The evidence excerpts report a database annotation citing a paper; the primary study was not independently retrieved or validated here.",
    "Reviewer-only accession and annotation evidence were not supplied to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt P0DXV1 (RESE_ASPSL, 264 AA, SHA256 confirmed). The entry is annotated as 'O-methyltransferase resE' (EC 2.1.1.-) with the catalytic activity 'desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol + S-adenosyl-L-homocysteine + H(+)' (RHEA:81531), matching choice B verbatim. The evidence code ECO:0000305 indicates inference by similarity from PubMed:39105744, a computational/annotation inference rather than direct experimental characterization, but the annotation is consistent with the protein's O-methyltransferase classification.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the motif 'GCGTGK' (positions ~78-83), a canonical GxGxxG Rossmann-fold nucleotide-binding signature. In a ~264-residue protein, this motif is the hallmark of a Class I SAM-dependent methyltransferase fold. Among the four choices: (A) is an epimerase/aldose mutase (no nucleotide-binding Rossmann fold expected), (C) is an acetyl-CoA-dependent acetyltransferase (uses acetyl-CoA, not SAM; NAT-type enzymes have a distinct GNAT fold, not a Rossmann fold), (D) is a membrane transporter (no catalytic methyl-transfer reaction). Only (B) describes a SAM-dependent O-methyltransferase reaction, which is the unique match for a protein bearing a Rossmann-fold SAM-binding motif. Thus the fold-level inference eliminates A, C, and D without requiring knowledge of the specific substrate name.


**Missing item-specific fact**

> The specific substrate identity 'desmethylrestrictinol' and the product 'restrictinol' are item-specific facts that cannot be derived from sequence alone; however, they are not needed to select B because B is the only SAM-dependent methyltransferase among the four options.


**Reason**

> The GCGTGK Rossmann motif provides a concrete, general-biochemistry argument that the enzyme is a SAM-dependent methyltransferase. Only choice B involves SAM as a co-substrate, making it the uniquely consistent option. The unusual substrate name is a distractor detail that does not need to be predicted; the enzyme-class identification suffices to discriminate among the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span distinct enzyme classes (epimerase, SAM-methyltransferase, acetyl-CoA acetyltransferase, transporter). The Rossmann-fold motif cleanly selects the methyltransferase class, leaving B as the sole consistent answer. No other choice involves SAM or a Rossmann-type fold.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the specific catalytic activity assignment is a computational/annotation inference from the 2024 J. Agric. Food Chem. paper, not a direct in vitro kinetic characterization of this exact enzyme.
- The protein was first released in UniProt in February 2025; depending on the benchmark construction date, this entry may or may not have been available in databases accessible to the evaluated model.
- The reasoning path relies on recognizing the GxGxxG motif as a SAM-binding Rossmann fold. A model that misses this motif or misattributes it to a generic nucleotide-binding domain could still select an incorrect answer, but the biological argument is valid and general.
- The specific substrate name 'desmethylrestrictinol' is an obscure fungal secondary-metabolite intermediate; the question's answerability rests on enzyme-class discrimination, not substrate-name recall.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the motif 'GCGTGK' (positions ~78-83), a canonical GxGxxG Rossmann-fold nucleotide-binding signature. In a ~264-residue protein, this motif is the hallmark of a Class I SAM-dependent methyltransferase fold. Among the four choices: (A) is an epimerase/aldose mutase (no nucleotide-binding Rossmann fold expected), (C) is an acetyl-CoA-dependent acetyltransferase (uses acetyl-CoA, not SAM; NAT-type enzymes have a distinct GNAT fold, not a Rossmann fold), (D) is a membrane transporter (no catalytic methyl-transfer reaction). Only (B) describes a SAM-dependent O-methyltransferase reaction, which is the unique match for a protein bearing a Rossmann-fold SAM-binding motif. Thus the fold-level inference eliminates A, C, and D without requiring knowledge of the specific substrate name.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The specific substrate identity 'desmethylrestrictinol' and the product 'restrictinol' are item-specific facts that cannot be derived from sequence alone; however, they are not needed to select B because B is the only SAM-dependent methyltransferase among the four options.",
    "reason": "The GCGTGK Rossmann motif provides a concrete, general-biochemistry argument that the enzyme is a SAM-dependent methyltransferase. Only choice B involves SAM as a co-substrate, making it the uniquely consistent option. The unusual substrate name is a distractor detail that does not need to be predicted; the enzyme-class identification suffices to discriminate among the choices."
  },
  "case_id": "catalytic_activity_0094",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt P0DXV1 (RESE_ASPSL, 264 AA, SHA256 confirmed). The entry is annotated as 'O-methyltransferase resE' (EC 2.1.1.-) with the catalytic activity 'desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol + S-adenosyl-L-homocysteine + H(+)' (RHEA:81531), matching choice B verbatim. The evidence code ECO:0000305 indicates inference by similarity from PubMed:39105744, a computational/annotation inference rather than direct experimental characterization, but the annotation is consistent with the protein's O-methyltransferase classification."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the specific catalytic activity assignment is a computational/annotation inference from the 2024 J. Agric. Food Chem. paper, not a direct in vitro kinetic characterization of this exact enzyme.",
    "The protein was first released in UniProt in February 2025; depending on the benchmark construction date, this entry may or may not have been available in databases accessible to the evaluated model.",
    "The reasoning path relies on recognizing the GxGxxG motif as a SAM-binding Rossmann fold. A model that misses this motif or misattributes it to a generic nucleotide-binding domain could still select an incorrect answer, but the biological argument is valid and general.",
    "The specific substrate name 'desmethylrestrictinol' is an obscure fungal secondary-metabolite intermediate; the question's answerability rests on enzyme-class discrimination, not substrate-name recall."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span distinct enzyme classes (epimerase, SAM-methyltransferase, acetyl-CoA acetyltransferase, transporter). The Rossmann-fold motif cleanly selects the methyltransferase class, leaving B as the sole consistent answer. No other choice involves SAM or a Rossmann-type fold."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0094",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt P0DXV1 (RESE_ASPSL, 264 AA, SHA256 confirmed). The entry is annotated as 'O-methyltransferase resE' (EC 2.1.1.-) with the catalytic activity 'desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol + S-adenosyl-L-homocysteine + H(+)' (RHEA:81531), matching choice B verbatim. The evidence code ECO:0000305 indicates inference by similarity from PubMed:39105744, a computational/annotation inference rather than direct experimental characterization, but the annotation is consistent with the protein's O-methyltransferase classification.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the motif 'GCGTGK' (positions ~78-83), a canonical GxGxxG Rossmann-fold nucleotide-binding signature. In a ~264-residue protein, this motif is the hallmark of a Class I SAM-dependent methyltransferase fold. Among the four choices: (A) is an epimerase/aldose mutase (no nucleotide-binding Rossmann fold expected), (C) is an acetyl-CoA-dependent acetyltransferase (uses acetyl-CoA, not SAM; NAT-type enzymes have a distinct GNAT fold, not a Rossmann fold), (D) is a membrane transporter (no catalytic methyl-transfer reaction). Only (B) describes a SAM-dependent O-methyltransferase reaction, which is the unique match for a protein bearing a Rossmann-fold SAM-binding motif. Thus the fold-level inference eliminates A, C, and D without requiring knowledge of the specific substrate name.",
    "missing_item_specific_fact": "The specific substrate identity 'desmethylrestrictinol' and the product 'restrictinol' are item-specific facts that cannot be derived from sequence alone; however, they are not needed to select B because B is the only SAM-dependent methyltransferase among the four options.",
    "reason": "The GCGTGK Rossmann motif provides a concrete, general-biochemistry argument that the enzyme is a SAM-dependent methyltransferase. Only choice B involves SAM as a co-substrate, making it the uniquely consistent option. The unusual substrate name is a distractor detail that does not need to be predicted; the enzyme-class identification suffices to discriminate among the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span distinct enzyme classes (epimerase, SAM-methyltransferase, acetyl-CoA acetyltransferase, transporter). The Rossmann-fold motif cleanly selects the methyltransferase class, leaving B as the sole consistent answer. No other choice involves SAM or a Rossmann-type fold."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the specific catalytic activity assignment is a computational/annotation inference from the 2024 J. Agric. Food Chem. paper, not a direct in vitro kinetic characterization of this exact enzyme.",
    "The protein was first released in UniProt in February 2025; depending on the benchmark construction date, this entry may or may not have been available in databases accessible to the evaluated model.",
    "The reasoning path relies on recognizing the GxGxxG motif as a SAM-binding Rossmann fold. A model that misses this motif or misattributes it to a generic nucleotide-binding domain could still select an incorrect answer, but the biological argument is valid and general.",
    "The specific substrate name 'desmethylrestrictinol' is an obscure fungal secondary-metabolite intermediate; the question's answerability rests on enzyme-class discrimination, not substrate-name recall."
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

**Accession:** `P0DXV1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 4. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.952467+00:00.  

```json
"P0DXV1"
```

Source SHA-256: `28f2208ebdc3c58c28d8c0bd9978354bcb775822363a3845e9d7dffaefd695cd`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.952467+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"Restricticin biosynthesis cluster protein E"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000305","id":"39105744","source":"PubMed"}],"value":"2.1.1.-"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"39105744","source":"PubMed"}],"value":"O-methyltransferase resE"}}}
```

Source SHA-256: `28f2208ebdc3c58c28d8c0bd9978354bcb775822363a3845e9d7dffaefd695cd`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.952467+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"left-to-right","evidences":[{"evidenceCode":"ECO:0000305","id":"39105744","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:81532"}}],"reaction":{"evidences":[{"evidenceCode":"ECO:0000305","id":"39105744","source":"PubMed"}],"name":"desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol + S-adenosyl-L-homocysteine + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:81531"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:57856"},{"database":"ChEBI","id":"CHEBI:59789"},{"database":"ChEBI","id":"CHEBI:231922"},{"database":"ChEBI","id":"CHEBI:231923"}]}}
```

Source SHA-256: `28f2208ebdc3c58c28d8c0bd9978354bcb775822363a3845e9d7dffaefd695cd`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV1.json)  
**Locator:** `/references/0`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:29:42.952467+00:00.  

```json
{"citation":{"authors":["Lu Y.","Li Y.","Dou M.","Liu D.","Lin W.","Fan A."],"citationCrossReferences":[{"database":"PubMed","id":"39105744"},{"database":"DOI","id":"10.1021/acs.jafc.4c04244"}],"citationType":"journal article","firstPage":"18520","id":"39105744","journal":"J. Agric. Food Chem.","lastPage":"18527","publicationDate":"2024","title":"Discovery of a hybrid molecule with phytotoxic activity by genome mining, heterologous expression, and OSMAC strategy.","volume":"72"},"referenceNumber":1,"referencePositions":["NUCLEOTIDE SEQUENCE [GENOMIC DNA]","FUNCTION","PATHWAY"]}
```

Source SHA-256: `28f2208ebdc3c58c28d8c0bd9978354bcb775822363a3845e9d7dffaefd695cd`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV1?format=txt&versions=4)  
**Locator:** `lines 1-14`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.445708+00:00.  

```text
ID   RESE_ASPSL              Reviewed;         264 AA.
AC   P0DXV1;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 1.
DT   28-JAN-2026, entry version 4.
DE   RecName: Full=O-methyltransferase resE {ECO:0000303|PubMed:39105744};
DE            EC=2.1.1.- {ECO:0000305|PubMed:39105744};
DE   AltName: Full=Restricticin biosynthesis cluster protein E {ECO:0000303|PubMed:39105744};
GN   Name=resE {ECO:0000303|PubMed:39105744};
OS   Aspergillus sclerotiorum.
OC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;
OC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;
OC   Aspergillus subgen. Circumdati.
OX   NCBI_TaxID=138282;
```

Source SHA-256: `cd2e82952af8d3844a3a9c286440d6c646ca7af305696f06813c85a3b4406cf2`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV1?format=txt&versions=4)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.445708+00:00.  

```text
DE   RecName: Full=O-methyltransferase resE {ECO:0000303|PubMed:39105744};
DE            EC=2.1.1.- {ECO:0000305|PubMed:39105744};
DE   AltName: Full=Restricticin biosynthesis cluster protein E {ECO:0000303|PubMed:39105744};
```

Source SHA-256: `cd2e82952af8d3844a3a9c286440d6c646ca7af305696f06813c85a3b4406cf2`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV1?format=txt&versions=4)  
**Locator:** `lines 40-47`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 4 / 1.  
**Retrieved:** 2026-11-02T04:29:45.445708+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=desmethylrestrictinol + S-adenosyl-L-methionine = restrictinol
CC         + S-adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81531,
CC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,
CC         ChEBI:CHEBI:231922, ChEBI:CHEBI:231923;
CC         Evidence={ECO:0000305|PubMed:39105744};
CC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81532;
CC         Evidence={ECO:0000305|PubMed:39105744};
```

Source SHA-256: `cd2e82952af8d3844a3a9c286440d6c646ca7af305696f06813c85a3b4406cf2`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 94. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
