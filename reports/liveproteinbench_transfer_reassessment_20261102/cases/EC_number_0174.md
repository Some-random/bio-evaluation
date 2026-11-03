# EC_number_0174: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0174.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **A** — 1.97.1.13

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

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
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

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

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record assigns EC 1.97.1.13, and its catalytic-activity annotation cites experimental evidence from two publications. The annotated reaction is oxidation of an aliphatic sulfonate with ferredoxin, supporting the keyed EC number.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The long sequence and cysteine-rich features may support recognition as a tungsten/iron-sulfur oxidoreductase, making the kinase option and some unrelated oxidoreductases less plausible. But that broad family-level inference does not meaningfully distinguish the closely related EC 1.97.1.13 and 1.97.1.14 alternatives.


**Missing item-specific fact**

> The enzyme's specific substrate and reaction classification, needed to distinguish EC 1.97.1.13 from EC 1.97.1.14.


**Reason**

> The choices include closely related EC numbers for which general recognition of an oxidoreductase family is insufficient. The supplied sequence alone does not establish the substrate specificity that selects the keyed number; doing so would require target-specific functional evidence or an annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports the keyed EC number; no alternative is identified as equally defensible.


### Important caveats

- The source evidence is reviewer-only and was not part of the original model input.
- The sequence matches the cited UniProt entry, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence and cysteine-rich features may support recognition as a tungsten/iron-sulfur oxidoreductase, making the kinase option and some unrelated oxidoreductases less plausible. But that broad family-level inference does not meaningfully distinguish the closely related EC 1.97.1.13 and 1.97.1.14 alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's specific substrate and reaction classification, needed to distinguish EC 1.97.1.13 from EC 1.97.1.14.",
    "reason": "The choices include closely related EC numbers for which general recognition of an oxidoreductase family is insufficient. The supplied sequence alone does not establish the substrate specificity that selects the keyed number; doing so would require target-specific functional evidence or an annotation."
  },
  "case_id": "EC_number_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.97.1.13, and its catalytic-activity annotation cites experimental evidence from two publications. The annotated reaction is oxidation of an aliphatic sulfonate with ferredoxin, supporting the keyed EC number."
  },
  "important_caveats": [
    "The source evidence is reviewer-only and was not part of the original model input.",
    "The sequence matches the cited UniProt entry, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports the keyed EC number; no alternative is identified as equally defensible."
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
    "reason": "The sequence-matched UniProt record assigns EC 1.97.1.13, and its catalytic-activity annotation cites experimental evidence from two publications. The annotated reaction is oxidation of an aliphatic sulfonate with ferredoxin, supporting the keyed EC number.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The long sequence and cysteine-rich features may support recognition as a tungsten/iron-sulfur oxidoreductase, making the kinase option and some unrelated oxidoreductases less plausible. But that broad family-level inference does not meaningfully distinguish the closely related EC 1.97.1.13 and 1.97.1.14 alternatives.",
    "missing_item_specific_fact": "The enzyme's specific substrate and reaction classification, needed to distinguish EC 1.97.1.13 from EC 1.97.1.14.",
    "reason": "The choices include closely related EC numbers for which general recognition of an oxidoreductase family is insufficient. The supplied sequence alone does not establish the substrate specificity that selects the keyed number; doing so would require target-specific functional evidence or an annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports the keyed EC number; no alternative is identified as equally defensible."
  },
  "important_caveats": [
    "The source evidence is reviewer-only and was not part of the original model input.",
    "The sequence matches the cited UniProt entry, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProtKB entry E7FHH1 (ASOR_PYRFU, Pyrococcus furiosus) carries EC 1.97.1.13 with experimental evidence codes (ECO:0000269) from PubMed:16199576 and PubMed:36269456. The catalytic reaction (aliphatic sulfonate + 4 oxidized ferredoxin + 2 H2O → 4 reduced ferredoxin + carboxylate + sulfite + 6H+) is supported by X-ray crystallography (PDB 6X1O, 6X6U) and biochemical characterization. The benchmark sequence SHA256 matches the source entry exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C11](#evidence-c11), [C12](#evidence-c12), [H2](#evidence-h2), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model can eliminate C (2.7.1.39, a kinase/transferase) and D (1.16.1.10, an Fe(II) oxidoreductase) using family-level knowledge: the GADHT motif and overall fold identify this as a tungsten-containing oxidoreductase (WOR/AOR family) that uses ferredoxin as electron acceptor (EC 1.97.x.x), not a transferase or an iron-donor enzyme. However, distinguishing A (1.97.1.13, aliphatic sulfonate oxidoreductase) from B (1.97.1.14) requires knowing the specific experimental substrate-specificity data for THIS protein. The GADHT motif and W/Mo cofactor binding residues are shared across the entire WOR family and do not encode which particular substrate (sulfonate vs. the substrate of 1.97.1.14) is acted upon. The 1.97.1.13 assignment was made in 2022 based on novel experimental characterization (PubMed:36269456) showing sulfonate desulfonation; prior to that, this protein was annotated as a generic aldehyde oxidoreductase. No sequence motif or family-level inference distinguishes the sulfonate desulfonase activity from other 1.97.1.x reactions.


**Missing item-specific fact**

> The experimental demonstration (PubMed:36269456, 2022) that this specific protein catalyzes aliphatic sulfonate desulfonation (rather than the reaction assigned to EC 1.97.1.14), including the identification of active-site residues conferring sulfonate specificity, which is not derivable from sequence-level family motifs alone.


**Reason**

> While family-level knowledge eliminates options C and D, the critical A-vs-B distinction (1.97.1.13 vs 1.97.1.14) requires the specific experimental characterization of this protein's substrate specificity published in 2022. The shared GADHT/WOR-family motifs do not encode the precise 4th-digit EC assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Once the experimental data for 1.97.1.13 is known, only A is correct. C and D are clearly wrong by EC class. B (1.97.1.14) would only be defensible if one knew it applied to a different reaction/protein.


### Important caveats

- The protein was originally characterized as WOR5 (tungsten-containing aldehyde oxidoreductase) in 2005; the sulfonate desulfonase EC assignment came only in 2022. Models trained on earlier data might have a different annotation.
- The existence and exact definition of EC 1.97.1.14 could not be independently verified from the supplied evidence; if it is a non-existent or fabricated EC number, option B would be trivially eliminable, making the question more answerable.
- The GADHT motif confirms WOR-family membership but is shared with AOR, FOR, POR, and other family members, so it cannot resolve the 4th-digit EC assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model can eliminate C (2.7.1.39, a kinase/transferase) and D (1.16.1.10, an Fe(II) oxidoreductase) using family-level knowledge: the GADHT motif and overall fold identify this as a tungsten-containing oxidoreductase (WOR/AOR family) that uses ferredoxin as electron acceptor (EC 1.97.x.x), not a transferase or an iron-donor enzyme. However, distinguishing A (1.97.1.13, aliphatic sulfonate oxidoreductase) from B (1.97.1.14) requires knowing the specific experimental substrate-specificity data for THIS protein. The GADHT motif and W/Mo cofactor binding residues are shared across the entire WOR family and do not encode which particular substrate (sulfonate vs. the substrate of 1.97.1.14) is acted upon. The 1.97.1.13 assignment was made in 2022 based on novel experimental characterization (PubMed:36269456) showing sulfonate desulfonation; prior to that, this protein was annotated as a generic aldehyde oxidoreductase. No sequence motif or family-level inference distinguishes the sulfonate desulfonase activity from other 1.97.1.x reactions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The experimental demonstration (PubMed:36269456, 2022) that this specific protein catalyzes aliphatic sulfonate desulfonation (rather than the reaction assigned to EC 1.97.1.14), including the identification of active-site residues conferring sulfonate specificity, which is not derivable from sequence-level family motifs alone.",
    "reason": "While family-level knowledge eliminates options C and D, the critical A-vs-B distinction (1.97.1.13 vs 1.97.1.14) requires the specific experimental characterization of this protein's substrate specificity published in 2022. The shared GADHT/WOR-family motifs do not encode the precise 4th-digit EC assignment."
  },
  "case_id": "EC_number_0174",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C11",
      "C12",
      "H2",
      "H5"
    ],
    "judgment": "supported",
    "reason": "UniProtKB entry E7FHH1 (ASOR_PYRFU, Pyrococcus furiosus) carries EC 1.97.1.13 with experimental evidence codes (ECO:0000269) from PubMed:16199576 and PubMed:36269456. The catalytic reaction (aliphatic sulfonate + 4 oxidized ferredoxin + 2 H2O → 4 reduced ferredoxin + carboxylate + sulfite + 6H+) is supported by X-ray crystallography (PDB 6X1O, 6X6U) and biochemical characterization. The benchmark sequence SHA256 matches the source entry exactly."
  },
  "important_caveats": [
    "The protein was originally characterized as WOR5 (tungsten-containing aldehyde oxidoreductase) in 2005; the sulfonate desulfonase EC assignment came only in 2022. Models trained on earlier data might have a different annotation.",
    "The existence and exact definition of EC 1.97.1.14 could not be independently verified from the supplied evidence; if it is a non-existent or fabricated EC number, option B would be trivially eliminable, making the question more answerable.",
    "The GADHT motif confirms WOR-family membership but is shared with AOR, FOR, POR, and other family members, so it cannot resolve the 4th-digit EC assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Once the experimental data for 1.97.1.13 is known, only A is correct. C and D are clearly wrong by EC class. B (1.97.1.14) would only be defensible if one knew it applied to a different reaction/protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"EC_number_0174","expected_answer_check":{"judgment":"supported","reason":"UniProtKB entry E7FHH1 (ASOR_PYRFU, Pyrococcus furiosus) carries EC 1.97.1.13 with experimental evidence codes (ECO:0000269) from PubMed:16199576 and PubMed:36269456. The catalytic reaction (aliphatic sulfonate + 4 oxidized ferredoxin + 2 H2O → 4 reduced ferredoxin + carboxylate + sulfite + 6H+) is supported by X-ray crystallography (PDB 6X1O, 6X6U) and biochemical characterization. The benchmark sequence SHA256 matches the source entry exactly.","evidence_ids":["C4","C5","C11","C12","H2","H5"]},"answerability_check":{"judgment":"lookup_or_memorization_dependent","discriminating_biological_argument":"A model can eliminate C (2.7.1.39, a kinase/transferase) and D (1.16.1.10, an Fe(II) oxidoreductase) using family-level knowledge: the GADHT motif and overall fold identify this as a tungsten-containing oxidoreductase (WOR/AOR family) that uses ferredoxin as electron acceptor (EC 1.97.x.x), not a transferase or an iron-donor enzyme. However, distinguishing A (1.97.1.13, aliphatic sulfonate oxidoreductase) from B (1.97.1.14) requires knowing the specific experimental substrate-specificity data for THIS protein. The GADHT motif and W/Mo cofactor binding residues are shared across the entire WOR family and do not encode which particular substrate (sulfonate vs. the substrate of 1.97.1.14) is acted upon. The 1.97.1.13 assignment was made in 2022 based on novel experimental characterization (PubMed:36269456) showing sulfonate desulfonation; prior to that, this protein was annotated as a generic aldehyde oxidoreductase. No sequence motif or family-level inference distinguishes the sulfonate desulfonase activity from other 1.97.1.x reactions.","missing_item_specific_fact":"The experimental demonstration (PubMed:36269456, 2022) that this specific protein catalyzes aliphatic sulfonate desulfonation (rather than the reaction assigned to EC 1.97.1.14), including the identification of active-site residues conferring sulfonate specificity, which is not derivable from sequence-level family motifs alone.","reason":"While family-level knowledge eliminates options C and D, the critical A-vs-B distinction (1.97.1.13 vs 1.97.1.14) requires the specific experimental characterization of this protein's substrate specificity published in 2022. The shared GADHT/WOR-family motifs do not encode the precise 4th-digit EC assignment."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"Once the experimental data for 1.97.1.13 is known, only A is correct. C and D are clearly wrong by EC class. B (1.97.1.14) would only be defensible if one knew it applied to a different reaction/protein."},"important_caveats":["The protein was originally characterized as WOR5 (tungsten-containing aldehyde oxidoreductase) in 2005; the sulfonate desulfonase EC assignment came only in 2022. Models trained on earlier data might have a different annotation.","The existence and exact definition of EC 1.97.1.14 could not be independently verified from the supplied evidence; if it is a non-existent or fabricated EC number, option B would be trivially eliminable, making the question more answerable.","The GADHT motif confirms WOR-family membership but is shared with AOR, FOR, POR, and other family members, so it cannot resolve the 4th-digit EC assignment."]}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "E7FHH1",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "benchmark_sequence_length": 624,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 61,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 2
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "current_source_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "current_source_sequence_length": 624,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 59,
  "selected_historical_version": {
    "accession": "E7FHH1",
    "database": "Swiss-Prot",
    "entryVersion": 59,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASOR_PYRFU",
    "sequenceVersion": 2
  },
  "selected_historical_record_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "selected_historical_source_sequence_sha256": "cdd9efa32fedb169eca6fa61e600f4ffe6a40328239667fbfaa7097b0896c0e6",
  "selected_historical_source_sequence_length": 624,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 59,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"E7FHH1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":61,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Thermococci\",\"Thermococcales\",\"Thermococcaceae\",\"Pyrococcus\"],\"scientificName\":\"Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1)\",\"taxonId\":186497}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"Aliphatic sulfonate ferredoxin oxidoreductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"ASOR\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"value\":\"Tungsten-containing aldehyde oxidoreductase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16199576\",\"source\":\"PubMed\"}],\"value\":\"WOR5\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"WOR5 large subunit\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"WOR5-L\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"value\":\"1.97.1.13\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Aliphatic sulfonate oxidoreductase, WOR-like subunit\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.97.1.13\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16199576\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"an aliphatic sulfonate + 4 oxidized [4Fe-4S]-[ferredoxin] + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + sulfite + 6 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80643\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29067\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231625\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"an aliphatic sulfonate + 2 oxidized [4Fe-4S]-[ferredoxin] + H2O = 2 reduced [4Fe-4S]-[ferredoxin] + an aldehyde + sulfite + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80647\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17478\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231625\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"2 oxidized [4Fe-4S]-[ferredoxin] + an aldehyde + H2O = 2 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80651\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17478\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29067\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C8",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"4 oxidized [4Fe-4S]-[ferredoxin] + taurine + 2 H2O = 4 reduced [4Fe-4S]-[ferredoxin] + sulfite + glycine + 6 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80087\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57305\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:507393\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C9",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/comments/5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"2 oxidized [4Fe-4S]-[ferredoxin] + taurine + H2O = aminoacetaldehyde + 2 reduced [4Fe-4S]-[ferredoxin] + sulfite + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80635\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17359\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58213\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:507393\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C10",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/comments/6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36269456\",\"source\":\"PubMed\"}],\"name\":\"aminoacetaldehyde + 2 oxidized [4Fe-4S]-[ferredoxin] + H2O = 2 reduced [4Fe-4S]-[ferredoxin] + glycine + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80639\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18797\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:18798\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33722\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33723\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57305\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58213\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C11",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Bevers L.E.\",\"Bol E.\",\"Hagedoorn P.L.\",\"Hagen W.R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16199576\"},{\"database\":\"DOI\",\"id\":\"10.1128/jb.187.20.7056-7061.2005\"}],\"citationType\":\"journal article\",\"firstPage\":\"7056\",\"id\":\"16199576\",\"journal\":\"J. Bacteriol.\",\"lastPage\":\"7061\",\"publicationDate\":\"2005\",\"title\":\"WOR5, a novel tungsten-containing aldehyde oxidoreductase from Pyrococcus furiosus with a broad substrate specificity.\",\"volume\":\"187\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 43587 / DSM 3638 / JCM 8422 / Vc1\"}],\"referenceNumber\":3,\"referencePositions\":[\"PROTEIN SEQUENCE OF 1-21\",\"FUNCTION AS AN ALDEHYDE OXIDOREDUCTASE\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FHH1.json)

```json
{
  "evidence_id": "C12",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/E7FHH1.json",
  "source_sha256": "18eefea7678f1f3cf63a5cf78340505deedf16e8073c0bcbf55c97830efe8da0",
  "retrieved_utc": "2026-11-01T06:25:05.760844+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Mathew L.G.\",\"Haja D.K.\",\"Pritchett C.\",\"McCormick W.\",\"Zeineddine R.\",\"Fontenot L.S.\",\"Rivera M.E.\",\"Glushka J.\",\"Adams M.W.W.\",\"Lanzilotta W.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36269456\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00775-022-01965-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"747\",\"id\":\"36269456\",\"journal\":\"J. Biol. Inorg. Chem.\",\"lastPage\":\"758\",\"publicationDate\":\"2022\",\"title\":\"An unprecedented function for a tungsten-containing oxidoreductase.\",\"volume\":\"27\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6X1O\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6X6U\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"COM1\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR (4FE-4S) CLUSTER AND TUNGSTOPTERIN\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 1-20",
  "excerpt": "ID   ASOR_PYRFU              Reviewed;         624 AA.\nAC   E7FHH1; A0A5C0XQU4;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 2.\nDT   28-JAN-2026, entry version 59.\nDE   RecName: Full=Aliphatic sulfonate oxidoreductase, WOR-like subunit {ECO:0000305};\nDE            EC=1.97.1.13 {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\nDE   AltName: Full=Aliphatic sulfonate ferredoxin oxidoreductase {ECO:0000303|PubMed:36269456};\nDE            Short=ASOR {ECO:0000303|PubMed:36269456};\nDE   AltName: Full=Tungsten-containing aldehyde oxidoreductase {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 large subunit {ECO:0000303|PubMed:36269456};\nDE            Short=WOR5-L {ECO:0000303|PubMed:36269456};\nGN   Name=wor5 {ECO:0000303|PubMed:16199576};\nGN   OrderedLocusNames=PF1480 {ECO:0000312|EMBL:AAL81604.1};\nGN   ORFNames=PFDSM3638_07420 {ECO:0000312|EMBL:QEK79109.1};\nOS   Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Thermococci; Thermococcales;\nOC   Thermococcaceae; Pyrococcus.\nOX   NCBI_TaxID=186497;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 6-13",
  "excerpt": "DE   RecName: Full=Aliphatic sulfonate oxidoreductase, WOR-like subunit {ECO:0000305};\nDE            EC=1.97.1.13 {ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\nDE   AltName: Full=Aliphatic sulfonate ferredoxin oxidoreductase {ECO:0000303|PubMed:36269456};\nDE            Short=ASOR {ECO:0000303|PubMed:36269456};\nDE   AltName: Full=Tungsten-containing aldehyde oxidoreductase {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 {ECO:0000303|PubMed:16199576};\nDE   AltName: Full=WOR5 large subunit {ECO:0000303|PubMed:36269456};\nDE            Short=WOR5-L {ECO:0000303|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 37-45",
  "excerpt": "RN   [3]\nRP   PROTEIN SEQUENCE OF 1-21, FUNCTION AS AN ALDEHYDE OXIDOREDUCTASE, COFACTOR,\nRP   AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=ATCC 43587 / DSM 3638 / JCM 8422 / Vc1;\nRX   PubMed=16199576; DOI=10.1128/jb.187.20.7056-7061.2005;\nRA   Bevers L.E., Bol E., Hagedoorn P.L., Hagen W.R.;\nRT   \"WOR5, a novel tungsten-containing aldehyde oxidoreductase from Pyrococcus\nRT   furiosus with a broad substrate specificity.\";\nRL   J. Bacteriol. 187:7056-7061(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 46-55",
  "excerpt": "RN   [4] {ECO:0007744|PDB:6X1O, ECO:0007744|PDB:6X6U}\nRP   X-RAY CRYSTALLOGRAPHY (1.94 ANGSTROMS) OF 1-623 IN COMPLEX WITH IRON-SULFUR\nRP   (4FE-4S) CLUSTER AND TUNGSTOPTERIN, FUNCTION, CATALYTIC ACTIVITY, COFACTOR,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, AND SUBCELLULAR LOCATION.\nRC   STRAIN=COM1;\nRX   PubMed=36269456; DOI=10.1007/s00775-022-01965-0;\nRA   Mathew L.G., Haja D.K., Pritchett C., McCormick W., Zeineddine R.,\nRA   Fontenot L.S., Rivera M.E., Glushka J., Adams M.W.W., Lanzilotta W.N.;\nRT   \"An unprecedented function for a tungsten-containing oxidoreductase.\";\nRL   J. Biol. Inorg. Chem. 27:747-758(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 69-76",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an aliphatic sulfonate + 4 oxidized [4Fe-4S]-[ferredoxin] + 2\nCC         H2O = 4 reduced [4Fe-4S]-[ferredoxin] + a carboxylate + sulfite + 6\nCC         H(+); Xref=Rhea:RHEA:80643, Rhea:RHEA-COMP:18797, Rhea:RHEA-\nCC         COMP:18798, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,\nCC         ChEBI:CHEBI:29067, ChEBI:CHEBI:33722, ChEBI:CHEBI:33723,\nCC         ChEBI:CHEBI:231625; EC=1.97.1.13;\nCC         Evidence={ECO:0000269|PubMed:16199576, ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H6",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 77-83",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an aliphatic sulfonate + 2 oxidized [4Fe-4S]-[ferredoxin] +\nCC         H2O = 2 reduced [4Fe-4S]-[ferredoxin] + an aldehyde + sulfite + 3\nCC         H(+); Xref=Rhea:RHEA:80647, Rhea:RHEA-COMP:18797, Rhea:RHEA-\nCC         COMP:18798, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,\nCC         ChEBI:CHEBI:17478, ChEBI:CHEBI:33722, ChEBI:CHEBI:33723,\nCC         ChEBI:CHEBI:231625; Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H7",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 84-90",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 oxidized [4Fe-4S]-[ferredoxin] + an aldehyde + H2O = 2\nCC         reduced [4Fe-4S]-[ferredoxin] + a carboxylate + 3 H(+);\nCC         Xref=Rhea:RHEA:80651, Rhea:RHEA-COMP:18797, Rhea:RHEA-COMP:18798,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17478,\nCC         ChEBI:CHEBI:29067, ChEBI:CHEBI:33722, ChEBI:CHEBI:33723;\nCC         Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H8",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 91-97",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4 oxidized [4Fe-4S]-[ferredoxin] + taurine + 2 H2O = 4 reduced\nCC         [4Fe-4S]-[ferredoxin] + sulfite + glycine + 6 H(+);\nCC         Xref=Rhea:RHEA:80087, Rhea:RHEA-COMP:18797, Rhea:RHEA-COMP:18798,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,\nCC         ChEBI:CHEBI:33722, ChEBI:CHEBI:33723, ChEBI:CHEBI:57305,\nCC         ChEBI:CHEBI:507393; Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H9",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 98-104",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 oxidized [4Fe-4S]-[ferredoxin] + taurine + H2O =\nCC         aminoacetaldehyde + 2 reduced [4Fe-4S]-[ferredoxin] + sulfite + 3\nCC         H(+); Xref=Rhea:RHEA:80635, Rhea:RHEA-COMP:18797, Rhea:RHEA-\nCC         COMP:18798, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:17359,\nCC         ChEBI:CHEBI:33722, ChEBI:CHEBI:33723, ChEBI:CHEBI:58213,\nCC         ChEBI:CHEBI:507393; Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59)

```json
{
  "evidence_id": "H10",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/E7FHH1?format=txt&versions=59",
  "source_sha256": "b8bea7a93c8150663d2ff8b25043a208a1f3bfca9375a258f4fedc3d60a4b70a",
  "retrieved_utc": "2026-11-01T06:27:59.835252+00:00",
  "source_locator": "lines 105-111",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=aminoacetaldehyde + 2 oxidized [4Fe-4S]-[ferredoxin] + H2O = 2\nCC         reduced [4Fe-4S]-[ferredoxin] + glycine + 3 H(+);\nCC         Xref=Rhea:RHEA:80639, Rhea:RHEA-COMP:18797, Rhea:RHEA-COMP:18798,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:33722,\nCC         ChEBI:CHEBI:33723, ChEBI:CHEBI:57305, ChEBI:CHEBI:58213;\nCC         Evidence={ECO:0000269|PubMed:36269456};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 59,
  "sequence_version": 2,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 174. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
