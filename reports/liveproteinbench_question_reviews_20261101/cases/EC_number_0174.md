# EC_number_0174

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `EC_number`  
**Author expected answer:** **A** — 1.97.1.13

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | valid_review |

**Paired comparison:** key agree; reasoning agree. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MYAYNGKLLDVDLTREKVKEVELSEDVLKKFYGGRGLGTYILWKELGEKWEKVDPLGEENLLLILTGPLTGYYPGMKTSIVSKSPESNGVVGSVLSSELGLELKAAGYDGIIIRGKAKSPVYLFIHNDTVEIRDATKYWGMGGIELYKTLLKEVHEEIRKKEKLKGVPKEPAMIYIGKGGENKVRFAAIMTKLMHAAGYGGYGAVMGSKNLKAVIAKGSGPLPEVYDKEKMKVLLREFWKELFSMTTFREWGTGAGGYSVGHDRSSEPIRNWQEEYHDNEEISVVNFENRTWIKKYWADYGCPVNCMKISYLRYGPYKGSISDAPDYELQAYMGTNLGIFEPEKIVYLSYLVDELGLDGINTGNILGFAAELYQRGILTKEDLGFELNWGDEKAFAKLLHLIVEKEGIGKILAEGTYRAALKISEIKGIDVTKYAVHVKGIAVGAHGIRSELDYTKDISYAVSVQGGDHTSTAALPAKGYTGELVEAFYDSAVICNFVTKPGFEKIIEFGNALSGFNITPEQWLNEIGLRIIHLQRILLLLGGPDVYWDPRKDDDNPPRFYEPLPSGPVKGKAPNREDIKAKVKQYYEEIGYDEHGIPKEEVLEELGIGEAKREVKRIKKRLNL

[Multiple Choices]
A. 1.97.1.13
B. 1.97.1.14
C. 2.7.1.39
D. 1.16.1.10
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

> The sequence matches the UniProt entry for this protein, whose EC 1.97.1.13 annotation is supported by cited experimental evidence. The annotated reaction is an aliphatic sulfonate oxidation, consistent with choice A.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an oxidoreductase, but the input gives no substrate or reaction context that distinguishes the exact EC number from the alternatives.


**Missing item-specific fact**

> The specific experimentally characterized activity of this protein, including its aliphatic-sulfonate oxidation, is needed to assign EC 1.97.1.13.


**Reason**

> Selecting among these precise EC numbers depends on a protein-specific functional annotation or experimental reaction assignment absent from the question. Recognizing the sequence or its database record would be lookup, not reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-matched annotation supports A; the supplied reviewer evidence does not establish another listed EC number for this protein.


### Important caveats

- The experimental evidence and database records are reviewer-only and were not available to the evaluated model.
- The actual author source snapshot is unknown, although a historical record with the matching sequence also supports the EC assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an oxidoreductase, but the input gives no substrate or reaction context that distinguishes the exact EC number from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific experimentally characterized activity of this protein, including its aliphatic-sulfonate oxidation, is needed to assign EC 1.97.1.13.",
    "reason": "Selecting among these precise EC numbers depends on a protein-specific functional annotation or experimental reaction assignment absent from the question. Recognizing the sequence or its database record would be lookup, not reasoning from supplied context."
  },
  "case_id": "EC_number_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for this protein, whose EC 1.97.1.13 annotation is supported by cited experimental evidence. The annotated reaction is an aliphatic sulfonate oxidation, consistent with choice A."
  },
  "important_caveats": [
    "The experimental evidence and database records are reviewer-only and were not available to the evaluated model.",
    "The actual author source snapshot is unknown, although a historical record with the matching sequence also supports the EC assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports A; the supplied reviewer evidence does not establish another listed EC number for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry for this protein, whose EC 1.97.1.13 annotation is supported by cited experimental evidence. The annotated reaction is an aliphatic sulfonate oxidation, consistent with choice A.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an oxidoreductase, but the input gives no substrate or reaction context that distinguishes the exact EC number from the alternatives.",
    "missing_item_specific_fact": "The specific experimentally characterized activity of this protein, including its aliphatic-sulfonate oxidation, is needed to assign EC 1.97.1.13.",
    "reason": "Selecting among these precise EC numbers depends on a protein-specific functional annotation or experimental reaction assignment absent from the question. Recognizing the sequence or its database record would be lookup, not reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-matched annotation supports A; the supplied reviewer evidence does not establish another listed EC number for this protein."
  },
  "important_caveats": [
    "The experimental evidence and database records are reviewer-only and were not available to the evaluated model.",
    "The actual author source snapshot is unknown, although a historical record with the matching sequence also supports the EC assignment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry E7FHH1 (ASOR_PYRFU) from Pyrococcus furiosus, whose sequence matches the supplied 624-aa sequence exactly (SHA256 confirmed), is annotated with EC 1.97.1.13 (Aliphatic sulfonate oxidoreductase, WOR-like subunit) with experimental evidence (ECO:0000269) from PubMed:16199576 and PubMed:36269456. The catalytic activity comment (C5/H5) explicitly assigns EC 1.97.1.13 to the reaction: an aliphatic sulfonate + 4 oxidized &#91;4Fe-4S&#93;-ferredoxin + 2 H2O → 4 reduced ferredoxin + carboxylate + sulfite + 6 H+. This is corroborated by X-ray crystallography (PDB 6X1O, 6X6U) showing tungstopterin and 4Fe-4S clusters.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H5](#evidence-h5), [C12](#evidence-c12), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains recognizable tungsten-containing aldehyde oxidoreductase (AOR/WOR) family motifs (e.g., 'GAGGYSVG' tungstopterin-binding motif, 'GKGGENKVRFAAIMTKLMHAAGYGGYGAVMGSKNLKAVIAKGSGPLPE' conserved AOR segment) and putative 4Fe-4S cluster-binding cysteine motifs. These features allow a knowledgeable model to infer membership in the tungsten/iron-sulfur oxidoreductase superfamily and eliminate transferase (C, 2.7.1.39) and metal-ion oxidoreductase (D, 1.16.1.10) options. However, distinguishing EC 1.97.1.13 (aliphatic sulfonate oxidoreductase) from EC 1.97.1.14 (a closely related entry in the same 1.97.1 sub-subclass) requires knowing the specific substrate specificity experimentally determined for this particular enzyme (sulfonate vs. another substrate), which is an item-specific experimental fact from the 2022 Mathew et al. study.


**Missing item-specific fact**

> The specific EC sub-number (.13 vs .14) assignment depends on the experimentally determined substrate specificity of this exact enzyme (aliphatic sulfonate oxidation, discovered in 2022), and on knowing what EC 1.97.1.14 designates (if it exists as a valid entry). No sequence motif uniquely encodes 'sulfonate' vs. another 1.97.1 substrate.


**Reason**

> While the protein family (tungsten-containing oxidoreductase with Fe-S clusters) can be inferred from sequence motifs, narrowing from the 1.97.1.x class to the exact terminal digit .13 requires memorization of the EC classification and the specific experimental substrate data for this enzyme. The A-vs-B distinction is not derivable from general biological reasoning about the sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> C (2.7.1.39, a transferase) and D (1.16.1.10, a metal-ion oxidoreductase) are clearly incompatible with the tungsten/ferredoxin oxidoreductase architecture evident in the sequence. Between A and B, the evidence supports A uniquely; however, if EC 1.97.1.14 does not exist as a valid EC number, B is a fabricated distractor, making the question somewhat easier but still dependent on knowing valid EC entries.


### Important caveats

- The EC 1.97.1.13 annotation for this enzyme was assigned only in 2022 (PubMed:36269456); before that, the enzyme was characterized as a generic tungsten-containing aldehyde oxidoreductase (WOR5, 2005). The benchmark question's validity depends on the author's data-construction date relative to this annotation.
- EC 1.97.1.14 may not be a currently valid EC number; if fabricated, it is trivially eliminable but still requires awareness of valid EC entries in the 1.97.1 class.
- The sequence-match is exact (SHA256 confirmed), so the annotation applies directly to the supplied sequence.
- The enzyme's dual activity (sulfonate oxidoreductase AND aldehyde oxidoreductase) is documented; the EC assignment reflects the sulfonate activity specifically.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable tungsten-containing aldehyde oxidoreductase (AOR/WOR) family motifs (e.g., 'GAGGYSVG' tungstopterin-binding motif, 'GKGGENKVRFAAIMTKLMHAAGYGGYGAVMGSKNLKAVIAKGSGPLPE' conserved AOR segment) and putative 4Fe-4S cluster-binding cysteine motifs. These features allow a knowledgeable model to infer membership in the tungsten/iron-sulfur oxidoreductase superfamily and eliminate transferase (C, 2.7.1.39) and metal-ion oxidoreductase (D, 1.16.1.10) options. However, distinguishing EC 1.97.1.13 (aliphatic sulfonate oxidoreductase) from EC 1.97.1.14 (a closely related entry in the same 1.97.1 sub-subclass) requires knowing the specific substrate specificity experimentally determined for this particular enzyme (sulfonate vs. another substrate), which is an item-specific experimental fact from the 2022 Mathew et al. study.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific EC sub-number (.13 vs .14) assignment depends on the experimentally determined substrate specificity of this exact enzyme (aliphatic sulfonate oxidation, discovered in 2022), and on knowing what EC 1.97.1.14 designates (if it exists as a valid entry). No sequence motif uniquely encodes 'sulfonate' vs. another 1.97.1 substrate.",
    "reason": "While the protein family (tungsten-containing oxidoreductase with Fe-S clusters) can be inferred from sequence motifs, narrowing from the 1.97.1.x class to the exact terminal digit .13 requires memorization of the EC classification and the specific experimental substrate data for this enzyme. The A-vs-B distinction is not derivable from general biological reasoning about the sequence."
  },
  "case_id": "EC_number_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H5",
      "C12",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry E7FHH1 (ASOR_PYRFU) from Pyrococcus furiosus, whose sequence matches the supplied 624-aa sequence exactly (SHA256 confirmed), is annotated with EC 1.97.1.13 (Aliphatic sulfonate oxidoreductase, WOR-like subunit) with experimental evidence (ECO:0000269) from PubMed:16199576 and PubMed:36269456. The catalytic activity comment (C5/H5) explicitly assigns EC 1.97.1.13 to the reaction: an aliphatic sulfonate + 4 oxidized [4Fe-4S]-ferredoxin + 2 H2O → 4 reduced ferredoxin + carboxylate + sulfite + 6 H+. This is corroborated by X-ray crystallography (PDB 6X1O, 6X6U) showing tungstopterin and 4Fe-4S clusters."
  },
  "important_caveats": [
    "The EC 1.97.1.13 annotation for this enzyme was assigned only in 2022 (PubMed:36269456); before that, the enzyme was characterized as a generic tungsten-containing aldehyde oxidoreductase (WOR5, 2005). The benchmark question's validity depends on the author's data-construction date relative to this annotation.",
    "EC 1.97.1.14 may not be a currently valid EC number; if fabricated, it is trivially eliminable but still requires awareness of valid EC entries in the 1.97.1 class.",
    "The sequence-match is exact (SHA256 confirmed), so the annotation applies directly to the supplied sequence.",
    "The enzyme's dual activity (sulfonate oxidoreductase AND aldehyde oxidoreductase) is documented; the EC assignment reflects the sulfonate activity specifically."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C (2.7.1.39, a transferase) and D (1.16.1.10, a metal-ion oxidoreductase) are clearly incompatible with the tungsten/ferredoxin oxidoreductase architecture evident in the sequence. Between A and B, the evidence supports A uniquely; however, if EC 1.97.1.14 does not exist as a valid EC number, B is a fabricated distractor, making the question somewhat easier but still dependent on knowing valid EC entries."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0174",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry E7FHH1 (ASOR_PYRFU) from Pyrococcus furiosus, whose sequence matches the supplied 624-aa sequence exactly (SHA256 confirmed), is annotated with EC 1.97.1.13 (Aliphatic sulfonate oxidoreductase, WOR-like subunit) with experimental evidence (ECO:0000269) from PubMed:16199576 and PubMed:36269456. The catalytic activity comment (C5/H5) explicitly assigns EC 1.97.1.13 to the reaction: an aliphatic sulfonate + 4 oxidized [4Fe-4S]-ferredoxin + 2 H2O → 4 reduced ferredoxin + carboxylate + sulfite + 6 H+. This is corroborated by X-ray crystallography (PDB 6X1O, 6X6U) showing tungstopterin and 4Fe-4S clusters.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H5", "C12", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains recognizable tungsten-containing aldehyde oxidoreductase (AOR/WOR) family motifs (e.g., 'GAGGYSVG' tungstopterin-binding motif, 'GKGGENKVRFAAIMTKLMHAAGYGGYGAVMGSKNLKAVIAKGSGPLPE' conserved AOR segment) and putative 4Fe-4S cluster-binding cysteine motifs. These features allow a knowledgeable model to infer membership in the tungsten/iron-sulfur oxidoreductase superfamily and eliminate transferase (C, 2.7.1.39) and metal-ion oxidoreductase (D, 1.16.1.10) options. However, distinguishing EC 1.97.1.13 (aliphatic sulfonate oxidoreductase) from EC 1.97.1.14 (a closely related entry in the same 1.97.1 sub-subclass) requires knowing the specific substrate specificity experimentally determined for this particular enzyme (sulfonate vs. another substrate), which is an item-specific experimental fact from the 2022 Mathew et al. study.",
    "missing_item_specific_fact": "The specific EC sub-number (.13 vs .14) assignment depends on the experimentally determined substrate specificity of this exact enzyme (aliphatic sulfonate oxidation, discovered in 2022), and on knowing what EC 1.97.1.14 designates (if it exists as a valid entry). No sequence motif uniquely encodes 'sulfonate' vs. another 1.97.1 substrate.",
    "reason": "While the protein family (tungsten-containing oxidoreductase with Fe-S clusters) can be inferred from sequence motifs, narrowing from the 1.97.1.x class to the exact terminal digit .13 requires memorization of the EC classification and the specific experimental substrate data for this enzyme. The A-vs-B distinction is not derivable from general biological reasoning about the sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "C (2.7.1.39, a transferase) and D (1.16.1.10, a metal-ion oxidoreductase) are clearly incompatible with the tungsten/ferredoxin oxidoreductase architecture evident in the sequence. Between A and B, the evidence supports A uniquely; however, if EC 1.97.1.14 does not exist as a valid EC number, B is a fabricated distractor, making the question somewhat easier but still dependent on knowing valid EC entries."
  },
  "important_caveats": [
    "The EC 1.97.1.13 annotation for this enzyme was assigned only in 2022 (PubMed:36269456); before that, the enzyme was characterized as a generic tungsten-containing aldehyde oxidoreductase (WOR5, 2005). The benchmark question's validity depends on the author's data-construction date relative to this annotation.",
    "EC 1.97.1.14 may not be a currently valid EC number; if fabricated, it is trivially eliminable but still requires awareness of valid EC entries in the 1.97.1 class.",
    "The sequence-match is exact (SHA256 confirmed), so the annotation applies directly to the supplied sequence.",
    "The enzyme's dual activity (sulfonate oxidoreductase AND aldehyde oxidoreductase) is documented; the EC assignment reflects the sulfonate activity specifically."
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

**Accession:** `E7FHH1` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 59. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.760844+00:00.  

```json
"E7FHH1"
```

Source SHA-256: `18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.760844+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36269456","source":"PubMed"}],"value":"Aliphatic sulfonate ferredoxin oxidoreductase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36269456","source":"PubMed"}],"value":"ASOR"}]},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16199576","source":"PubMed"}],"value":"Tungsten-containing aldehyde oxidoreductase"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"16199576","source":"PubMed"}],"value":"WOR5"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"36269456","source":"PubMed"}],"value":"WOR5 large subunit"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"36269456","source":"PubMed"}],"value":"WOR5-L"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"value":"1.97.1.13"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000305"}],"value":"Aliphatic sulfonate oxidoreductase, WOR-like subunit"}}}
```

Source SHA-256: `18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)  
**Locator:** `/comments/1`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.760844+00:00.  

```json
{"commentType":"CATALYTIC ACTIVITY","reaction":{"ecNumber":"1.97.1.13","evidences":[{"evidenceCode":"ECO:0000269","id":"16199576","source":"PubMed"},{"evidenceCode":"ECO:0000269","id":"36269456","source":"PubMed"}],"name":"an aliphatic sulfonate + 4 oxidized [4Fe-4S]-[ferredoxin] + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + sulfite + 6 H(+)","reactionCrossReferences":[{"database":"Rhea","id":"RHEA:80643"},{"database":"Rhea","id":"RHEA-COMP:18797"},{"database":"Rhea","id":"RHEA-COMP:18798"},{"database":"ChEBI","id":"CHEBI:15377"},{"database":"ChEBI","id":"CHEBI:15378"},{"database":"ChEBI","id":"CHEBI:17359"},{"database":"ChEBI","id":"CHEBI:29067"},{"database":"ChEBI","id":"CHEBI:33722"},{"database":"ChEBI","id":"CHEBI:33723"},{"database":"ChEBI","id":"CHEBI:231625"}]}}
```

Source SHA-256: `18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0`.

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)  
**Locator:** `/references/3`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-01T06:25:05.760844+00:00.  

```json
{"citation":{"authors":["Mathew L.G.","Haja D.K.","Pritchett C.","McCormick W.","Zeineddine R.","Fontenot L.S.","Rivera M.E.","Glushka J.","Adams M.W.W.","Lanzilotta W.N."],"citationCrossReferences":[{"database":"PubMed","id":"36269456"},{"database":"DOI","id":"10.1007/s00775-022-01965-0"}],"citationType":"journal article","firstPage":"747","id":"36269456","journal":"J. Biol. Inorg. Chem.","lastPage":"758","publicationDate":"2022","title":"An unprecedented function for a tungsten-containing oxidoreductase.","volume":"27"},"evidences":[{"evidenceCode":"ECO:0007744","id":"6X1O","source":"PDB"},{"evidenceCode":"ECO:0007744","id":"6X6U","source":"PDB"}],"referenceComments":[{"type":"STRAIN","value":"COM1"}],"referenceNumber":4,"referencePositions":["X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR (4FE-4S) CLUSTER AND TUNGSTOPTERIN","FUNCTION","CATALYTIC ACTIVITY","COFACTOR","BIOPHYSICOCHEMICAL PROPERTIES","SUBUNIT","SUBCELLULAR LOCATION"]}
```

Source SHA-256: `18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)  
**Locator:** `lines 1-20`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 2.  
**Retrieved:** 2026-11-01T06:27:59.835252+00:00.  

```text
ID   ASOR_PYRFU              Reviewed;         624 AA.
AC   E7FHH1; A0A5C0XQU4;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   05-FEB-2025, sequence version 2.
DT   28-JAN-2026, entry version 59.
DE   RecName: Full=Aliphatic sulfonate oxidoreductase, WOR-like subunit {ECO:0000305};
DE            EC=1.97.1.13 {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};
DE   AltName: Full=Aliphatic sulfonate ferredoxin oxidoreductase {ECO:0000303|PubMed:36269456};
DE            Short=ASOR {ECO:0000303|PubMed:36269456};
DE   AltName: Full=Tungsten-containing aldehyde oxidoreductase {ECO:0000303|PubMed:16199576};
DE   AltName: Full=WOR5 {ECO:0000303|PubMed:16199576};
DE   AltName: Full=WOR5 large subunit {ECO:0000303|PubMed:36269456};
DE            Short=WOR5-L {ECO:0000303|PubMed:36269456};
GN   Name=wor5 {ECO:0000303|PubMed:16199576};
GN   OrderedLocusNames=PF1480 {ECO:0000312|EMBL:AAL81604.1};
GN   ORFNames=PFDSM3638_07420 {ECO:0000312|EMBL:QEK79109.1};
OS   Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1).
OC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;
OC   Thermococcaceae; Pyrococcus.
OX   NCBI_TaxID=186497;
```

Source SHA-256: `b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a`.

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)  
**Locator:** `lines 6-13`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 2.  
**Retrieved:** 2026-11-01T06:27:59.835252+00:00.  

```text
DE   RecName: Full=Aliphatic sulfonate oxidoreductase, WOR-like subunit {ECO:0000305};
DE            EC=1.97.1.13 {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};
DE   AltName: Full=Aliphatic sulfonate ferredoxin oxidoreductase {ECO:0000303|PubMed:36269456};
DE            Short=ASOR {ECO:0000303|PubMed:36269456};
DE   AltName: Full=Tungsten-containing aldehyde oxidoreductase {ECO:0000303|PubMed:16199576};
DE   AltName: Full=WOR5 {ECO:0000303|PubMed:16199576};
DE   AltName: Full=WOR5 large subunit {ECO:0000303|PubMed:36269456};
DE            Short=WOR5-L {ECO:0000303|PubMed:36269456};
```

Source SHA-256: `b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a`.

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)  
**Locator:** `lines 46-55`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 2.  
**Retrieved:** 2026-11-01T06:27:59.835252+00:00.  

```text
RN   [4] {ECO:0007744|PDB:6X1O, ECO:0007744|PDB:6X6U}
RP   X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR
RP   (4FE-4S) CLUSTER AND TUNGSTOPTERIN, FUNCTION, CATALYTIC ACTIVITY, COFACTOR,
RP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND SUBCELLULAR LOCATION.
RC   STRAIN=COM1;
RX   PubMed=36269456; DOI=10.1007/s00775-022-01965-0;
RA   Mathew L.G., Haja D.K., Pritchett C., McCormick W., Zeineddine R.,
RA   Fontenot L.S., Rivera M.E., Glushka J., Adams M.W.W., Lanzilotta W.N.;
RT   "An unprecedented function for a tungsten-containing oxidoreductase.";
RL   J. Biol. Inorg. Chem. 27:747-758(2022).
```

Source SHA-256: `b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a`.

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)  
**Locator:** `lines 69-76`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 59 / 2.  
**Retrieved:** 2026-11-01T06:27:59.835252+00:00.  

```text
CC   -!- CATALYTIC ACTIVITY:
CC       Reaction=an aliphatic sulfonate + 4 oxidized [4Fe-4S]-[ferredoxin] + 2
CC         H2O = 4 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + sulfite + 6
CC         H(+); Xref=Rhea:RHEA:80643, Rhea:RHEA-COMP:18797, Rhea:RHEA-
CC         COMP:18798, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,
CC         ChEBI:CHEBI:29067, ChEBI:CHEBI:33722, ChEBI:CHEBI:33723,
CC         ChEBI:CHEBI:231625; EC=1.97.1.13;
CC         Evidence={ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};
```

Source SHA-256: `b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 174. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
