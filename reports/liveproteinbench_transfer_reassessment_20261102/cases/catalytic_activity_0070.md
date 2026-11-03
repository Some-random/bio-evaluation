# catalytic_activity_0070: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0070.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **C** — (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. 3 malonyl-CoA + acetyl-CoA + 2 S-adenosyl-L-methionine = 3,5-dimethylorsellinate + 2 S-adenosyl-L-homocysteine + 3 CO2 + 4 CoA
B. 2-hydroxyspirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
C. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
D. a (3E,5Z)-dienoyl-CoA = a (2E,4E)-(5,6-saturated)-dienoyl-CoA
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the annotated Aspergillus terreus protein, whose catalytic-activity record gives the reaction in choice C with ECO:0000269 evidence. The archived entry available by the historical cutoff records the same reaction.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a long soluble enzyme and does not, from general biochemical principles alone, establish which precise reaction among these choices it catalyzes.


**Missing item-specific fact**

> The protein-specific functional assignment as dihydroxy-acid dehydratase, or equivalent sequence-homology/functional annotation, is needed to select the reaction in C.


**Reason**

> The reviewer-only annotation supports the key, but was not provided to the evaluated model. Inferring the particular catalytic reaction would require protein-specific identification rather than a sufficiently discriminating argument from the input alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supported annotation matches choice C; the other options describe different reactions.


### Important caveats

- The evidence is a database annotation carrying experimental evidence code ECO:0000269 and a PubMed citation; the primary paper was not independently reviewed here.
- The exact sequence matches both the current and historical database records, but the author's precise source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a long soluble enzyme and does not, from general biochemical principles alone, establish which precise reaction among these choices it catalyzes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific functional assignment as dihydroxy-acid dehydratase, or equivalent sequence-homology/functional annotation, is needed to select the reaction in C.",
    "reason": "The reviewer-only annotation supports the key, but was not provided to the evaluated model. Inferring the particular catalytic reaction would require protein-specific identification rather than a sufficiently discriminating argument from the input alone."
  },
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Aspergillus terreus protein, whose catalytic-activity record gives the reaction in choice C with ECO:0000269 evidence. The archived entry available by the historical cutoff records the same reaction."
  },
  "important_caveats": [
    "The evidence is a database annotation carrying experimental evidence code ECO:0000269 and a PubMed citation; the primary paper was not independently reviewed here.",
    "The exact sequence matches both the current and historical database records, but the author's precise source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported annotation matches choice C; the other options describe different reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the annotated Aspergillus terreus protein, whose catalytic-activity record gives the reaction in choice C with ECO:0000269 evidence. The archived entry available by the historical cutoff records the same reaction.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a long soluble enzyme and does not, from general biochemical principles alone, establish which precise reaction among these choices it catalyzes.",
    "missing_item_specific_fact": "The protein-specific functional assignment as dihydroxy-acid dehydratase, or equivalent sequence-homology/functional annotation, is needed to select the reaction in C.",
    "reason": "The reviewer-only annotation supports the key, but was not provided to the evaluated model. Inferring the particular catalytic reaction would require protein-specific identification rather than a sufficiently discriminating argument from the input alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supported annotation matches choice C; the other options describe different reactions."
  },
  "important_caveats": [
    "The evidence is a database annotation carrying experimental evidence code ECO:0000269 and a PubMed citation; the primary paper was not independently reviewed here.",
    "The exact sequence matches both the current and historical database records, but the author's precise source snapshot is unknown."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied 598-aa sequence matches UniProt entry Q0CPG9 (ASTD_ASPTN, Aspergillus terreus) exactly (SHA256 confirmed). The UniProt annotation lists EC 4.2.1.9 (dihydroxy-acid dehydratase astD) with the catalytic reaction '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O', supported by experimental evidence (ECO:0000269, PubMed:29995859, Nature 2018). This matches Choice C verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~598 aa) exhibits the two-domain architecture characteristic of the ILV3/DHAD enzyme family, with a C-terminal domain containing cysteine residues in a pattern consistent with 4Fe-4S cluster coordination (a hallmark of DHAD enzymes). Among the four choices, only DHAD (Choice C) requires a 4Fe-4S cluster. Choice A (polyketide synthase) would require acyltransferase, ketosynthase, and ACP domains absent here. Choice B (carotenoid hydroxylase) would require di-iron or Rieske-type motifs and membrane association. Choice D (enoyl-CoA isomerase) is typically a small (~200–300 aa) protein without metal clusters. The combination of the 4Fe-4S cluster-binding cysteine pattern, the ~600-aa two-domain architecture, and the absence of PKS/carotenoid-hydroxylase/isomerase signatures provides a concrete biological argument favoring DHAD.


**Missing item-specific fact**

> None strictly required; however, recognizing the DHAD-specific 4Fe-4S cluster motif (CX2CX2C) in a fungal DHAD sequence requires specialized enzyme-family knowledge beyond generic sequence heuristics.


**Reason**

> The 4Fe-4S cluster coordination motif and the overall two-domain DHAD architecture are general, teachable features of the ILV3 enzyme family. A knowledgeable reader can eliminate the other three choices by noting the absence of PKS catalytic domains, carotenoid-hydroxylase di-iron motifs, and the atypical size for an enoyl-CoA isomerase. This constitutes a concrete biological reasoning path, though it demands specialized enzyme-family knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Each distractor corresponds to a structurally and mechanistically distinct enzyme class (PKS, carotenoid hydroxylase, DHAD, enoyl-CoA isomerase). The 4Fe-4S cluster motif and two-domain architecture uniquely point to DHAD among the four choices. No other option is defensible given the sequence features.


### Important caveats

- The 4Fe-4S cluster CX2CX2C motif is not trivially identifiable by a naive pattern scan in this fungal DHAD sequence; expert recognition of the DHAD C-terminal domain architecture is needed.
- The experimental evidence (ECO:0000269, Nature 2018) confirms the DHAD activity, but the annotation also lists a second, broader-specificity reaction (C6) with only similarity-based evidence (ECO:0000250); this does not affect the correctness of Choice C.
- The reviewer-only UniProt accession and annotation were absent from the evaluated model input; the reasoning assessment is based solely on what a model could extract from the raw sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~598 aa) exhibits the two-domain architecture characteristic of the ILV3/DHAD enzyme family, with a C-terminal domain containing cysteine residues in a pattern consistent with 4Fe-4S cluster coordination (a hallmark of DHAD enzymes). Among the four choices, only DHAD (Choice C) requires a 4Fe-4S cluster. Choice A (polyketide synthase) would require acyltransferase, ketosynthase, and ACP domains absent here. Choice B (carotenoid hydroxylase) would require di-iron or Rieske-type motifs and membrane association. Choice D (enoyl-CoA isomerase) is typically a small (~200–300 aa) protein without metal clusters. The combination of the 4Fe-4S cluster-binding cysteine pattern, the ~600-aa two-domain architecture, and the absence of PKS/carotenoid-hydroxylase/isomerase signatures provides a concrete biological argument favoring DHAD.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; however, recognizing the DHAD-specific 4Fe-4S cluster motif (CX2CX2C) in a fungal DHAD sequence requires specialized enzyme-family knowledge beyond generic sequence heuristics.",
    "reason": "The 4Fe-4S cluster coordination motif and the overall two-domain DHAD architecture are general, teachable features of the ILV3 enzyme family. A knowledgeable reader can eliminate the other three choices by noting the absence of PKS catalytic domains, carotenoid-hydroxylase di-iron motifs, and the atypical size for an enoyl-CoA isomerase. This constitutes a concrete biological reasoning path, though it demands specialized enzyme-family knowledge."
  },
  "case_id": "catalytic_activity_0070",
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
    "reason": "The supplied 598-aa sequence matches UniProt entry Q0CPG9 (ASTD_ASPTN, Aspergillus terreus) exactly (SHA256 confirmed). The UniProt annotation lists EC 4.2.1.9 (dihydroxy-acid dehydratase astD) with the catalytic reaction '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O', supported by experimental evidence (ECO:0000269, PubMed:29995859, Nature 2018). This matches Choice C verbatim."
  },
  "important_caveats": [
    "The 4Fe-4S cluster CX2CX2C motif is not trivially identifiable by a naive pattern scan in this fungal DHAD sequence; expert recognition of the DHAD C-terminal domain architecture is needed.",
    "The experimental evidence (ECO:0000269, Nature 2018) confirms the DHAD activity, but the annotation also lists a second, broader-specificity reaction (C6) with only similarity-based evidence (ECO:0000250); this does not affect the correctness of Choice C.",
    "The reviewer-only UniProt accession and annotation were absent from the evaluated model input; the reasoning assessment is based solely on what a model could extract from the raw sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor corresponds to a structurally and mechanistically distinct enzyme class (PKS, carotenoid hydroxylase, DHAD, enoyl-CoA isomerase). The 4Fe-4S cluster motif and two-domain architecture uniquely point to DHAD among the four choices. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied 598-aa sequence matches UniProt entry Q0CPG9 (ASTD_ASPTN, Aspergillus terreus) exactly (SHA256 confirmed). The UniProt annotation lists EC 4.2.1.9 (dihydroxy-acid dehydratase astD) with the catalytic reaction '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O', supported by experimental evidence (ECO:0000269, PubMed:29995859, Nature 2018). This matches Choice C verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~598 aa) exhibits the two-domain architecture characteristic of the ILV3/DHAD enzyme family, with a C-terminal domain containing cysteine residues in a pattern consistent with 4Fe-4S cluster coordination (a hallmark of DHAD enzymes). Among the four choices, only DHAD (Choice C) requires a 4Fe-4S cluster. Choice A (polyketide synthase) would require acyltransferase, ketosynthase, and ACP domains absent here. Choice B (carotenoid hydroxylase) would require di-iron or Rieske-type motifs and membrane association. Choice D (enoyl-CoA isomerase) is typically a small (~200–300 aa) protein without metal clusters. The combination of the 4Fe-4S cluster-binding cysteine pattern, the ~600-aa two-domain architecture, and the absence of PKS/carotenoid-hydroxylase/isomerase signatures provides a concrete biological argument favoring DHAD.",
    "missing_item_specific_fact": "None strictly required; however, recognizing the DHAD-specific 4Fe-4S cluster motif (CX2CX2C) in a fungal DHAD sequence requires specialized enzyme-family knowledge beyond generic sequence heuristics.",
    "reason": "The 4Fe-4S cluster coordination motif and the overall two-domain DHAD architecture are general, teachable features of the ILV3 enzyme family. A knowledgeable reader can eliminate the other three choices by noting the absence of PKS catalytic domains, carotenoid-hydroxylase di-iron motifs, and the atypical size for an enoyl-CoA isomerase. This constitutes a concrete biological reasoning path, though it demands specialized enzyme-family knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor corresponds to a structurally and mechanistically distinct enzyme class (PKS, carotenoid hydroxylase, DHAD, enoyl-CoA isomerase). The 4Fe-4S cluster motif and two-domain architecture uniquely point to DHAD among the four choices. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The 4Fe-4S cluster CX2CX2C motif is not trivially identifiable by a naive pattern scan in this fungal DHAD sequence; expert recognition of the DHAD C-terminal domain architecture is needed.",
    "The experimental evidence (ECO:0000269, Nature 2018) confirms the DHAD activity, but the annotation also lists a second, broader-specificity reaction (C6) with only similarity-based evidence (ECO:0000250); this does not affect the correctness of Choice C.",
    "The reviewer-only UniProt accession and annotation were absent from the evaluated model input; the reasoning assessment is based solely on what a model could extract from the raw sequence."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation identifies the catalytic reaction as option C and cites experimental evidence (ECO:0000269).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 598-residue sequence is consistent with the IlvD/dihydroxy-acid dehydratase family, whose members dehydrate branched-chain amino-acid-pathway dihydroxy acids. That family-level activity points to option C, unlike the polyketide synthesis, carotenoid oxidation, or enoyl-CoA transformation in the other choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable family knowledge provides a meaningful basis for distinguishing C from the offered alternatives; recalling this exact protein's annotation is not required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered reactions describe distinct enzyme activities, and the dihydroxy-acid dehydratase family supports C.


### Important caveats

- The family assignment is an inference from sequence and transferable knowledge; the reviewer-only annotation corroborates the keyed reaction but was not part of the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 598-residue sequence is consistent with the IlvD/dihydroxy-acid dehydratase family, whose members dehydrate branched-chain amino-acid-pathway dihydroxy acids. That family-level activity points to option C, unlike the polyketide synthesis, carotenoid oxidation, or enoyl-CoA transformation in the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable family knowledge provides a meaningful basis for distinguishing C from the offered alternatives; recalling this exact protein's annotation is not required."
  },
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the catalytic reaction as option C and cites experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The family assignment is an inference from sequence and transferable knowledge; the reviewer-only annotation corroborates the keyed reaction but was not part of the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions describe distinct enzyme activities, and the dihydroxy-acid dehydratase family supports C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the catalytic reaction as option C and cites experimental evidence (ECO:0000269).",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 598-residue sequence is consistent with the IlvD/dihydroxy-acid dehydratase family, whose members dehydrate branched-chain amino-acid-pathway dihydroxy acids. That family-level activity points to option C, unlike the polyketide synthesis, carotenoid oxidation, or enoyl-CoA transformation in the other choices.",
    "missing_item_specific_fact": "",
    "reason": "Transferable family knowledge provides a meaningful basis for distinguishing C from the offered alternatives; recalling this exact protein's annotation is not required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions describe distinct enzyme activities, and the dihydroxy-acid dehydratase family supports C."
  },
  "important_caveats": [
    "The family assignment is an inference from sequence and transferable knowledge; the reviewer-only annotation corroborates the keyed reaction but was not part of the original input."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q0CPG9 (ASTD_ASPTN) is explicitly annotated with EC 4.2.1.9 and the catalytic activity '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O' (evidence C5, H4), supported by experimental evidence (ECO:0000269|PubMed:29995859, Yan et al. Nature 2018). The sequence in the question matches the source record exactly (598 aa, sha256 match). The expected answer C is directly the annotated primary catalytic reaction.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark &#91;2Fe-2S&#93; cluster-binding motifs of the dihydroxy-acid dehydratase (DHAD/IlvD/DipD/Mai) family, most notably the 'CPGRGACGG' motif and the 'SSSCPADDPKKL' cysteine-rich segment, which are well-characterized family-level signatures shared across bacterial IlvD and fungal DHAD enzymes. The N-terminal basic residue-rich stretch (MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQ...) is a mitochondrial targeting presequence, consistent with fungal DHAD (~598 aa total). Critically, the other three choices require structural features clearly absent here: (A) a polyketide synthase requires a multi-domain architecture (>1000 aa with KS, AT, ACP, KR, ER, DH domains); (B) a carotenoid hydroxylase requires transmembrane helices and cytochrome P450 heme-binding or Rieske-type motifs; (D) a dienoyl-CoA reductase requires a Rossmann-fold FAD/NAD-binding motif. None of these are present. The combination of Fe-S cysteine motifs, TIM-barrel-like catalytic domain architecture, mitochondrial targeting, and absence of features for the distractors allows a knowledgeable model to select C via family-level inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The DHAD/IlvD family has well-documented sequence signatures (CPGRGACGG Fe-S binding motif, characteristic cysteine spacing) that are transferable knowledge from bacterial IlvD and other fungal DHAD enzymes. Combined with elimination of the other choices based on their required but absent structural features (multi-domain PKS, TM helices, FAD-binding Rossmann fold), the answer is reachable without memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent fundamentally different enzyme classes with incompatible structural requirements. Only DHAD (C) is consistent with the observed Fe-S cluster motifs, soluble mitochondrial architecture, and absence of PKS domains, TM helices, or FAD-binding motifs.


### Important caveats

- The protein also has a second EC 4.2.1.9 activity (pentanoate substrate) annotated by similarity to P05791 (ECO:0000250), but this does not affect the answer since only the methylbutanoate reaction is offered among choices.
- The 'CPGRGACGG' motif is strongly suggestive but not absolutely unique to DHAD; however, in the context of the four offered choices and the overall domain architecture, it is sufficiently discriminating.
- The annotation is supported by experimental evidence (PubMed 29995859, Nature 2018) for the primary reaction, not merely computational transfer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark [2Fe-2S] cluster-binding motifs of the dihydroxy-acid dehydratase (DHAD/IlvD/DipD/Mai) family, most notably the 'CPGRGACGG' motif and the 'SSSCPADDPKKL' cysteine-rich segment, which are well-characterized family-level signatures shared across bacterial IlvD and fungal DHAD enzymes. The N-terminal basic residue-rich stretch (MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQ...) is a mitochondrial targeting presequence, consistent with fungal DHAD (~598 aa total). Critically, the other three choices require structural features clearly absent here: (A) a polyketide synthase requires a multi-domain architecture (>1000 aa with KS, AT, ACP, KR, ER, DH domains); (B) a carotenoid hydroxylase requires transmembrane helices and cytochrome P450 heme-binding or Rieske-type motifs; (D) a dienoyl-CoA reductase requires a Rossmann-fold FAD/NAD-binding motif. None of these are present. The combination of Fe-S cysteine motifs, TIM-barrel-like catalytic domain architecture, mitochondrial targeting, and absence of features for the distractors allows a knowledgeable model to select C via family-level inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The DHAD/IlvD family has well-documented sequence signatures (CPGRGACGG Fe-S binding motif, characteristic cysteine spacing) that are transferable knowledge from bacterial IlvD and other fungal DHAD enzymes. Combined with elimination of the other choices based on their required but absent structural features (multi-domain PKS, TM helices, FAD-binding Rossmann fold), the answer is reachable without memorizing this specific protein's annotation."
  },
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG9 (ASTD_ASPTN) is explicitly annotated with EC 4.2.1.9 and the catalytic activity '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O' (evidence C5, H4), supported by experimental evidence (ECO:0000269|PubMed:29995859, Yan et al. Nature 2018). The sequence in the question matches the source record exactly (598 aa, sha256 match). The expected answer C is directly the annotated primary catalytic reaction."
  },
  "important_caveats": [
    "The protein also has a second EC 4.2.1.9 activity (pentanoate substrate) annotated by similarity to P05791 (ECO:0000250), but this does not affect the answer since only the methylbutanoate reaction is offered among choices.",
    "The 'CPGRGACGG' motif is strongly suggestive but not absolutely unique to DHAD; however, in the context of the four offered choices and the overall domain architecture, it is sufficiently discriminating.",
    "The annotation is supported by experimental evidence (PubMed 29995859, Nature 2018) for the primary reaction, not merely computational transfer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes with incompatible structural requirements. Only DHAD (C) is consistent with the observed Fe-S cluster motifs, soluble mitochondrial architecture, and absence of PKS domains, TM helices, or FAD-binding motifs."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0070",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q0CPG9 (ASTD_ASPTN) is explicitly annotated with EC 4.2.1.9 and the catalytic activity '(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O' (evidence C5, H4), supported by experimental evidence (ECO:0000269|PubMed:29995859, Yan et al. Nature 2018). The sequence in the question matches the source record exactly (598 aa, sha256 match). The expected answer C is directly the annotated primary catalytic reaction.",
    "evidence_ids": ["C5", "C4", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark [2Fe-2S] cluster-binding motifs of the dihydroxy-acid dehydratase (DHAD/IlvD/DipD/Mai) family, most notably the 'CPGRGACGG' motif and the 'SSSCPADDPKKL' cysteine-rich segment, which are well-characterized family-level signatures shared across bacterial IlvD and fungal DHAD enzymes. The N-terminal basic residue-rich stretch (MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQ...) is a mitochondrial targeting presequence, consistent with fungal DHAD (~598 aa total). Critically, the other three choices require structural features clearly absent here: (A) a polyketide synthase requires a multi-domain architecture (>1000 aa with KS, AT, ACP, KR, ER, DH domains); (B) a carotenoid hydroxylase requires transmembrane helices and cytochrome P450 heme-binding or Rieske-type motifs; (D) a dienoyl-CoA reductase requires a Rossmann-fold FAD/NAD-binding motif. None of these are present. The combination of Fe-S cysteine motifs, TIM-barrel-like catalytic domain architecture, mitochondrial targeting, and absence of features for the distractors allows a knowledgeable model to select C via family-level inference.",
    "missing_item_specific_fact": "",
    "reason": "The DHAD/IlvD family has well-documented sequence signatures (CPGRGACGG Fe-S binding motif, characteristic cysteine spacing) that are transferable knowledge from bacterial IlvD and other fungal DHAD enzymes. Combined with elimination of the other choices based on their required but absent structural features (multi-domain PKS, TM helices, FAD-binding Rossmann fold), the answer is reachable without memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes with incompatible structural requirements. Only DHAD (C) is consistent with the observed Fe-S cluster motifs, soluble mitochondrial architecture, and absence of PKS domains, TM helices, or FAD-binding motifs."
  },
  "important_caveats": [
    "The protein also has a second EC 4.2.1.9 activity (pentanoate substrate) annotated by similarity to P05791 (ECO:0000250), but this does not affect the answer since only the methylbutanoate reaction is offered among choices.",
    "The 'CPGRGACGG' motif is strongly suggestive but not absolutely unique to DHAD; however, in the context of the four offered choices and the overall domain architecture, it is sufficiently discriminating.",
    "The annotation is supported by experimental evidence (PubMed 29995859, Nature 2018) for the primary reaction, not merely computational transfer."
  ]
}
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
  "requested_accession": "Q0CPG9",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "benchmark_sequence_length": 598,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 92,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "current_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_source_sequence_length": 598,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 90,
  "selected_historical_version": {
    "accession": "Q0CPG9",
    "database": "Swiss-Prot",
    "entryVersion": 90,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTD_ASPTN",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "selected_historical_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "selected_historical_source_sequence_length": 598,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 90,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q0CPG9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":92,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein D\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Dihydroxy-acid dehydratase astD, mitochondrial\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"DHAD astD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:24810\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"name\":\"(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24809\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:11851\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49072\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:27695\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"name\":\"(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:27694\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35146\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49258\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DOMAIN\",\"ACTIVITY REGULATION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   ASTD_ASPTN              Reviewed;         598 AA.\nAC   Q0CPG9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 90.\nDE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\nGN   Name=astD {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04415;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 6-10",
  "excerpt": "DE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 29-37",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, DOMAIN,\nRP   ACTIVITY REGULATION, AND PATHWAY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 52-58",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate\nCC         + H2O; Xref=Rhea:RHEA:24809, ChEBI:CHEBI:11851, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:49072; EC=4.2.1.9;\nCC         Evidence={ECO:0000269|PubMed:29995859};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:24810;\nCC         Evidence={ECO:0000269|PubMed:29995859};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "source_locator": "lines 59-65",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-\nCC         oxopentanoate + H2O; Xref=Rhea:RHEA:27694, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:35146, ChEBI:CHEBI:49258; EC=4.2.1.9;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:27695;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 90,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 70. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
