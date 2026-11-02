# EC_number_0188

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 1.2.1.11

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MATPSKKRCGVLGATGAVGTRFILLLSQHPLLELVAVGASDRSSGKKYRDAVRWKQSAPMPAKVADLTVRCCDPAEFSDCDIIFSGLDPDAAGEIEMAFLKANFAVFSNAKNYRLDPMVPLVVPLVNAGHIDVIPAQRKHFGLDKGMLVCNSNCAVVGLVVPAKALIQKFGPIESVSMVTMQAVSGAGYPGVSSMDIFDNIVPYIPGEEGKISSEARKILGDLNSDLAGFSDQKPLQISVACNRVPVLDGHTVCASLRFVNRPPPTASQVREALREYKPEVQTLGCPSAPKMSIHVMDEVDRPQPRLDRETEGGYACTVGRIREDDSDVFDIQFVALSHNTVLGASGSSILNAESAILKGFV

[Multiple Choices]
A. 1.2.1.11
B. 1.2.1.46
C. 3.1.3.112
D. 6.3.2.35
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

> The exact sequence matches a UniProt entry annotated as aspartate-semialdehyde dehydrogenase, EC 1.2.1.11. Its catalytic reaction is also assigned that EC number with ECO:0000269 evidence linked to a publication, supporting the author's key for this sequence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may support an enzyme-family inference, but the input alone does not establish the substrate-specific catalytic reaction needed to distinguish a complete EC number among these options.


**Missing item-specific fact**

> The protein-specific functional annotation or experimental identification of its catalytic reaction as aspartate-semialdehyde dehydrogenase activity.


**Reason**

> The matching, publication-backed annotation supports the answer in reviewer evidence, but that annotation and source identity were not supplied to the evaluated model. Choosing the precise EC number therefore depends on an item-specific functional fact, not merely on general biological reasoning from the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence specifically supports EC 1.2.1.11 for the sequence-matched protein; no supplied evidence supports another listed option.


### Important caveats

- The cited UniProt annotation is linked to publication evidence, but the primary paper was not independently reviewed here.
- Reviewer-only sequence identification and annotations establish support for the key; they were absent from the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may support an enzyme-family inference, but the input alone does not establish the substrate-specific catalytic reaction needed to distinguish a complete EC number among these options.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification of its catalytic reaction as aspartate-semialdehyde dehydrogenase activity.",
    "reason": "The matching, publication-backed annotation supports the answer in reviewer evidence, but that annotation and source identity were not supplied to the evaluated model. Choosing the precise EC number therefore depends on an item-specific functional fact, not merely on general biological reasoning from the sequence."
  },
  "case_id": "EC_number_0188",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as aspartate-semialdehyde dehydrogenase, EC 1.2.1.11. Its catalytic reaction is also assigned that EC number with ECO:0000269 evidence linked to a publication, supporting the author's key for this sequence."
  },
  "important_caveats": [
    "The cited UniProt annotation is linked to publication evidence, but the primary paper was not independently reviewed here.",
    "Reviewer-only sequence identification and annotations establish support for the key; they were absent from the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence specifically supports EC 1.2.1.11 for the sequence-matched protein; no supplied evidence supports another listed option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0188",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as aspartate-semialdehyde dehydrogenase, EC 1.2.1.11. Its catalytic reaction is also assigned that EC number with ECO:0000269 evidence linked to a publication, supporting the author's key for this sequence.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may support an enzyme-family inference, but the input alone does not establish the substrate-specific catalytic reaction needed to distinguish a complete EC number among these options.",
    "missing_item_specific_fact": "The protein-specific functional annotation or experimental identification of its catalytic reaction as aspartate-semialdehyde dehydrogenase activity.",
    "reason": "The matching, publication-backed annotation supports the answer in reviewer evidence, but that annotation and source identity were not supplied to the evaluated model. Choosing the precise EC number therefore depends on an item-specific functional fact, not merely on general biological reasoning from the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence specifically supports EC 1.2.1.11 for the sequence-matched protein; no supplied evidence supports another listed option."
  },
  "important_caveats": [
    "The cited UniProt annotation is linked to publication evidence, but the primary paper was not independently reviewed here.",
    "Reviewer-only sequence identification and annotations establish support for the key; they were absent from the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A080WMA9 (sequence SHA256 matched) annotates this 362-aa protein from Trichophyton rubrum as Aspartate-semialdehyde dehydrogenase with EC 1.2.1.11, supported by experimental evidence (ECO:0000269, PubMed:26869335; X-ray crystallography PDB:4ZHS/4ZIC in complex with NADP+). The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is experimentally characterized. The expected answer A (1.2.1.11) is well-supported by structural and biochemical evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple biological arguments allow elimination: (1) Size: 362 aa is consistent with ASADH (~330-370 aa) but far too small for EC 1.2.1.46 (formyltetrahydrofolate dehydrogenase, typically 800+ aa as part of a trifunctional MTHFD enzyme). (2) The sequence lacks canonical phosphatase motifs (DXD, HxH, or the HAD/CP-type fold of EC 3.1.3.112), ruling out a hydrolase. (3) The sequence lacks ligase hallmarks (e.g., ATP-grasp, synthetase adenylation domains) expected for EC 6.3.2.35. (4) The sequence contains a Rossmann-fold-like nucleotide-binding region (e.g., 'VSGAGYPGV' resembling GxGxxG) and multiple cysteines (e.g., 'CNSNCAVV', 'CCDPAEFSDCD') consistent with NADP-dependent oxidoreductase catalysis via a thiohemiacetal intermediate, characteristic of ASADH. By elimination within the four choices, 1.2.1.11 is the most consistent answer.


**Missing item-specific fact**

> Precise identification of the aspartate-semialdehyde substrate specificity (vs other 1.2.1.x aldehyde dehydrogenases) from sequence alone requires knowledge of the active-site architecture (catalytic Cys, Arg residues for phosphate binding, NADP vs NAD selectivity determinants) that is not trivially readable from primary sequence without structural context.


**Reason**

> The four choices span three different EC main classes (1, 3, 6) and two sub-options within class 1.2.1. General biological reasoning—protein size, absence of hydrolase/ligase motifs, presence of NADP-binding and catalytic Cys features—meaningfully eliminates B, C, and D, leaving A. The residual step of confirming ASADH specifically among 1.2.1.x enzymes is aided by the size constraint and known ASADH fold features, making the question answerable by reasoning, though not with absolute certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span sufficiently different enzyme classes and sizes that general biological reasoning (size, motif absence/presence) provides a clear path to A. No alternative option is defensible given the 362-aa length, lack of phosphatase/ligase signatures, and presence of oxidoreductase-consistent motifs.


### Important caveats

- The sequence-to-ASADH identification relies on general fold recognition and elimination; a model lacking training on ASADH structural biology may still struggle to confirm 1.2.1.11 over other hypothetical 1.2.1.x enzymes not listed.
- The UniProt annotation is Swiss-Prot reviewed with experimental evidence (X-ray crystallography), lending high confidence to the key.
- The identity of this sequence was inferred from reviewer-only metadata (accession A0A080WMA9); the evaluated model received only the raw sequence with no organism or annotation context.
- The entry was first released in Swiss-Prot in February 2025; depending on the benchmark construction date, this annotation may or may not have been available in training data.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple biological arguments allow elimination: (1) Size: 362 aa is consistent with ASADH (~330-370 aa) but far too small for EC 1.2.1.46 (formyltetrahydrofolate dehydrogenase, typically 800+ aa as part of a trifunctional MTHFD enzyme). (2) The sequence lacks canonical phosphatase motifs (DXD, HxH, or the HAD/CP-type fold of EC 3.1.3.112), ruling out a hydrolase. (3) The sequence lacks ligase hallmarks (e.g., ATP-grasp, synthetase adenylation domains) expected for EC 6.3.2.35. (4) The sequence contains a Rossmann-fold-like nucleotide-binding region (e.g., 'VSGAGYPGV' resembling GxGxxG) and multiple cysteines (e.g., 'CNSNCAVV', 'CCDPAEFSDCD') consistent with NADP-dependent oxidoreductase catalysis via a thiohemiacetal intermediate, characteristic of ASADH. By elimination within the four choices, 1.2.1.11 is the most consistent answer.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise identification of the aspartate-semialdehyde substrate specificity (vs other 1.2.1.x aldehyde dehydrogenases) from sequence alone requires knowledge of the active-site architecture (catalytic Cys, Arg residues for phosphate binding, NADP vs NAD selectivity determinants) that is not trivially readable from primary sequence without structural context.",
    "reason": "The four choices span three different EC main classes (1, 3, 6) and two sub-options within class 1.2.1. General biological reasoning—protein size, absence of hydrolase/ligase motifs, presence of NADP-binding and catalytic Cys features—meaningfully eliminates B, C, and D, leaving A. The residual step of confirming ASADH specifically among 1.2.1.x enzymes is aided by the size constraint and known ASADH fold features, making the question answerable by reasoning, though not with absolute certainty."
  },
  "case_id": "EC_number_0188",
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
    "reason": "UniProt entry A0A080WMA9 (sequence SHA256 matched) annotates this 362-aa protein from Trichophyton rubrum as Aspartate-semialdehyde dehydrogenase with EC 1.2.1.11, supported by experimental evidence (ECO:0000269, PubMed:26869335; X-ray crystallography PDB:4ZHS/4ZIC in complex with NADP+). The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is experimentally characterized. The expected answer A (1.2.1.11) is well-supported by structural and biochemical evidence."
  },
  "important_caveats": [
    "The sequence-to-ASADH identification relies on general fold recognition and elimination; a model lacking training on ASADH structural biology may still struggle to confirm 1.2.1.11 over other hypothetical 1.2.1.x enzymes not listed.",
    "The UniProt annotation is Swiss-Prot reviewed with experimental evidence (X-ray crystallography), lending high confidence to the key.",
    "The identity of this sequence was inferred from reviewer-only metadata (accession A0A080WMA9); the evaluated model received only the raw sequence with no organism or annotation context.",
    "The entry was first released in Swiss-Prot in February 2025; depending on the benchmark construction date, this annotation may or may not have been available in training data."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span sufficiently different enzyme classes and sizes that general biological reasoning (size, motif absence/presence) provides a clear path to A. No alternative option is defensible given the 362-aa length, lack of phosphatase/ligase signatures, and presence of oxidoreductase-consistent motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0188",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A080WMA9 (sequence SHA256 matched) annotates this 362-aa protein from Trichophyton rubrum as Aspartate-semialdehyde dehydrogenase with EC 1.2.1.11, supported by experimental evidence (ECO:0000269, PubMed:26869335; X-ray crystallography PDB:4ZHS/4ZIC in complex with NADP+). The catalytic reaction (L-aspartate 4-semialdehyde + phosphate + NADP+ = 4-phospho-L-aspartate + NADPH + H+) is experimentally characterized. The expected answer A (1.2.1.11) is well-supported by structural and biochemical evidence.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple biological arguments allow elimination: (1) Size: 362 aa is consistent with ASADH (~330-370 aa) but far too small for EC 1.2.1.46 (formyltetrahydrofolate dehydrogenase, typically 800+ aa as part of a trifunctional MTHFD enzyme). (2) The sequence lacks canonical phosphatase motifs (DXD, HxH, or the HAD/CP-type fold of EC 3.1.3.112), ruling out a hydrolase. (3) The sequence lacks ligase hallmarks (e.g., ATP-grasp, synthetase adenylation domains) expected for EC 6.3.2.35. (4) The sequence contains a Rossmann-fold-like nucleotide-binding region (e.g., 'VSGAGYPGV' resembling GxGxxG) and multiple cysteines (e.g., 'CNSNCAVV', 'CCDPAEFSDCD') consistent with NADP-dependent oxidoreductase catalysis via a thiohemiacetal intermediate, characteristic of ASADH. By elimination within the four choices, 1.2.1.11 is the most consistent answer.",
    "missing_item_specific_fact": "Precise identification of the aspartate-semialdehyde substrate specificity (vs other 1.2.1.x aldehyde dehydrogenases) from sequence alone requires knowledge of the active-site architecture (catalytic Cys, Arg residues for phosphate binding, NADP vs NAD selectivity determinants) that is not trivially readable from primary sequence without structural context.",
    "reason": "The four choices span three different EC main classes (1, 3, 6) and two sub-options within class 1.2.1. General biological reasoning—protein size, absence of hydrolase/ligase motifs, presence of NADP-binding and catalytic Cys features—meaningfully eliminates B, C, and D, leaving A. The residual step of confirming ASADH specifically among 1.2.1.x enzymes is aided by the size constraint and known ASADH fold features, making the question answerable by reasoning, though not with absolute certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span sufficiently different enzyme classes and sizes that general biological reasoning (size, motif absence/presence) provides a clear path to A. No alternative option is defensible given the 362-aa length, lack of phosphatase/ligase signatures, and presence of oxidoreductase-consistent motifs."
  },
  "important_caveats": [
    "The sequence-to-ASADH identification relies on general fold recognition and elimination; a model lacking training on ASADH structural biology may still struggle to confirm 1.2.1.11 over other hypothetical 1.2.1.x enzymes not listed.",
    "The UniProt annotation is Swiss-Prot reviewed with experimental evidence (X-ray crystallography), lending high confidence to the key.",
    "The identity of this sequence was inferred from reviewer-only metadata (accession A0A080WMA9); the evaluated model received only the raw sequence with no organism or annotation context.",
    "The entry was first released in Swiss-Prot in February 2025; depending on the benchmark construction date, this annotation may or may not have been available in training data."
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

**Accession:** `A0A080WMA9` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 38. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.783847+00:00.  

```json
"A0A080WMA9"
```

Source SHA-256: `bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.783847+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"26869335","source":"PubMed"}],"value":"TrASADH"}}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"26869335","source":"PubMed"}],"value":"1.2.1.11"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aspartate-semialdehyde dehydrogenase"}}}
```

Source SHA-256: `bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.783847+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","physiologicalReactions":[{"directionType":"right-to-left","evidences":[{"evidenceCode":"ECO:0000269","id":"26869335","source":"PubMed"}],"reactionCrossReference":{"database":"Rhea","id":"RHEA:24286"}}],"reaction":{"ecNumber":"1.2.1.11","evidences":[{"evidenceCode":"ECO:0000269","id":"26869335","source":"PubMed"}],"name":"L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-L-aspartate + NADPH + H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:24284"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:43474"},{"database":"ChEBI","id":"CHEBI:57535"},{"database":"ChEBI","id":"CHEBI:57783"},{"database":"ChEBI","id":"CHEBI:58349"},{"database":"ChEBI","id":"CHEBI:537519"}]}}
```

Source SHA-256: `bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e`.

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A080WMA9.json)  
**Locator:** `/references/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:23:53.783847+00:00.  

```json
{"citation":{"authors":["Li Q.","Mu Z.","Zhao R.","Dahal G.","Viola R.E.","Liu T.","Jin Q.","Cui S."],"citationCrossReferences":[{"database":"PubMed","id":"26869335"},{"database":"DOI","id":"10.1038/srep21067"}],"citationType":"journal article","firstPage":"21067","id":"26869335","journal":"Sci. Rep.","lastPage":"21067","publicationDate":"2016","title":"Structural Insights into the Tetrameric State of Aspartate-beta-semialdehyde Dehydrogenases from Fungal Species.","volume":"6"},"evidences":[{"evidenceCode":"ECO:0007744","id":"4ZHS","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"4ZIC","source":"PDB"}],"referenceComments":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"26869335","source":"PubMed"}],"type":"STRAIN","value":"BMU01672"}],"referenceNumber":2,"referencePositions":["X-RAY CRYSTALLOGRAPHY (2.55 ANGSTROMS) IN COMPLEX WITH NADP(+)","FUNCTION","CATALYTIC ACTIVITY","BIOPHYSICOCHEMICAL PROPERTIES","PATHWAY","SUBUNIT","MUTAGENESIS OF 196-ASP--PHE-198 AND ARG-309"]}
```

Source SHA-256: `bf278bc137aa3857c873dcee85929131e2e626bb23054806edb11415af48ec0e`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)  
**Locator:** `lines 6-8`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:57.418115+00:00.  

```text
DE   RecName: Full=Aspartate-semialdehyde dehydrogenase {ECO:0000305};
DE            EC=1.2.1.11 {ECO:0000269|PubMed:26869335};
DE   AltName: Full=TrASADH {ECO:0000303|PubMed:26869335};
```

Source SHA-256: `319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)  
**Locator:** `lines 27-36`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:57.418115+00:00.  

```text
RN   [2] {ECO:0007744|PDB:4ZHS, ECO:0007744|PDB:4ZIC}
RP   X-RAY CRYSTALLOGRAPHY (2.55 ANGSTROMS) IN COMPLEX WITH NADP(+), FUNCTION,
RP   CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, SUBUNIT, AND
RP   MUTAGENESIS OF 196-ASP--PHE-198 AND ARG-309.
RC   STRAIN=BMU01672 {ECO:0000303|PubMed:26869335};
RX   PubMed=26869335; DOI=10.1038/srep21067;
RA   Li Q., Mu Z., Zhao R., Dahal G., Viola R.E., Liu T., Jin Q., Cui S.;
RT   "Structural Insights into the Tetrameric State of Aspartate-beta-
RT   semialdehyde Dehydrogenases from Fungal Species.";
RL   Sci. Rep. 6:21067-21067(2016).
```

Source SHA-256: `319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A080WMA9?format=txt&versions=38)  
**Locator:** `lines 44-51`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 38 / 1.  
**Retrieved:** 2026-11-02T04:23:57.418115+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=L-aspartate 4-semialdehyde + phosphate + NADP(+) = 4-phospho-
CC         L-aspartate + NADPH + H(+); Xref=Rhea:RHEA:24284, ChEBI:CHEBI:15378,
CC         ChEBI:CHEBI:43474, ChEBI:CHEBI:57535, ChEBI:CHEBI:57783,
CC         ChEBI:CHEBI:58349, ChEBI:CHEBI:537519; EC=1.2.1.11;
CC         Evidence={ECO:0000269|PubMed:26869335};
CC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:24286;
CC         Evidence={ECO:0000269|PubMed:26869335};
```

Source SHA-256: `319e2a6ea09f79026f215490dfab47119b95e8f6a8e21b934e31e170e04fc34f`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 188. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
