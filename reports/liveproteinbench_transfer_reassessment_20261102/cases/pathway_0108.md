# pathway_0108: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/pathway_0108.txt)

**Task:** `pathway`  
**Author key, unchanged:** **A** — Metabolic intermediate biosynthesis

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MSTYGTLLKVTSYGESHGKAIGCVIDGFLSNIEINFDLIQKQLDRRRPNQSKLTSNRNEKDKLVILSGFDENKTLGTPITFLIYNEDIKKEDYNSFINIPRPGHGDYTYFMKYHVKNKSGSSRFSGRETATRVAAGACIEQWLYKSYNCSIVSYVHSVGNIKIPEQVSKELENKNPPSRDLVDSYGTVRYNEKEKIFMDCFNRIYDMNASMLKTDEYNKNTLTIPSIDNTYINVKTNECNINQVDNNHNNYINDKDNTFNNSEKSDEWIYLQTRCPHPYTAVQICSYILKLKNKGDSVGGIATCIIQNPPIGIGEPIFDKLEAELAKMILSIPAVKGIEFGSGFNGTYMFGSMHNDIFIPVENMSTKKESDLLYDDKGECKNMSYHSTIQNNEDQILNSTKGFMPPKNDKNFNNIDDYNVTFNNNEEKLLITKTNNCGGILAGISTGNNIVFRSAIKPVSSIQIEKETSDFYGNMCNLKVQGRHDSCILPRLPPIIEASSSMVIGDLILRQISKYGDKKLPTLFRNM

[Multiple Choices]
A. Metabolic intermediate biosynthesis
B. Amino-acid degradation
C. protein glycosylation. .
D. chorismate biosynthesis
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches a Plasmodium falciparum UniProt entry annotated as chorismate synthase, with a pathway annotation placing it in metabolic intermediate biosynthesis, specifically chorismate biosynthesis. The pathway annotation is transferred by similarity (ECO:0000250), while cited studies support the enzyme’s identity and catalytic activity; this supports A without making the pathway annotation itself direct experimental evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The options do not provide enough context to infer the protein’s specific function from general pathway knowledge alone. Identifying chorismate synthase would distinguish the relevant pathway, but that requires a protein-specific functional identification.


**Missing item-specific fact**

> That this sequence encodes chorismate synthase, an enzyme functioning in chorismate biosynthesis.


**Reason**

> The input supplies only the sequence and broad pathway choices. Recognizing or recalling this particular protein’s annotation is an item-specific fact, not a pathway distinction established by the supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> The annotated pathway is chorismate biosynthesis, which is a type of metabolic intermediate biosynthesis. Thus A is the broader pathway category and D names the specific pathway; the choices do not make those levels mutually exclusive.


### Important caveats

- The sequence matches the cited UniProt record, but the pathway annotation is similarity-transferred rather than presented as direct experimental pathway evidence.
- The cited characterization includes a Plasmodium falciparum strain; it should not be treated as proof that this exact sequence was the experimentally tested construct.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The options do not provide enough context to infer the protein’s specific function from general pathway knowledge alone. Identifying chorismate synthase would distinguish the relevant pathway, but that requires a protein-specific functional identification.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this sequence encodes chorismate synthase, an enzyme functioning in chorismate biosynthesis.",
    "reason": "The input supplies only the sequence and broad pathway choices. Recognizing or recalling this particular protein’s annotation is an item-specific fact, not a pathway distinction established by the supplied context."
  },
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a Plasmodium falciparum UniProt entry annotated as chorismate synthase, with a pathway annotation placing it in metabolic intermediate biosynthesis, specifically chorismate biosynthesis. The pathway annotation is transferred by similarity (ECO:0000250), while cited studies support the enzyme’s identity and catalytic activity; this supports A without making the pathway annotation itself direct experimental evidence."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the pathway annotation is similarity-transferred rather than presented as direct experimental pathway evidence.",
    "The cited characterization includes a Plasmodium falciparum strain; it should not be treated as proof that this exact sequence was the experimentally tested construct."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "The annotated pathway is chorismate biosynthesis, which is a type of metabolic intermediate biosynthesis. Thus A is the broader pathway category and D names the specific pathway; the choices do not make those levels mutually exclusive."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a Plasmodium falciparum UniProt entry annotated as chorismate synthase, with a pathway annotation placing it in metabolic intermediate biosynthesis, specifically chorismate biosynthesis. The pathway annotation is transferred by similarity (ECO:0000250), while cited studies support the enzyme’s identity and catalytic activity; this supports A without making the pathway annotation itself direct experimental evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The options do not provide enough context to infer the protein’s specific function from general pathway knowledge alone. Identifying chorismate synthase would distinguish the relevant pathway, but that requires a protein-specific functional identification.",
    "missing_item_specific_fact": "That this sequence encodes chorismate synthase, an enzyme functioning in chorismate biosynthesis.",
    "reason": "The input supplies only the sequence and broad pathway choices. Recognizing or recalling this particular protein’s annotation is an item-specific fact, not a pathway distinction established by the supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "The annotated pathway is chorismate biosynthesis, which is a type of metabolic intermediate biosynthesis. Thus A is the broader pathway category and D names the specific pathway; the choices do not make those levels mutually exclusive."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the pathway annotation is similarity-transferred rather than presented as direct experimental pathway evidence.",
    "The cited characterization includes a Plasmodium falciparum strain; it should not be treated as proof that this exact sequence was the experimentally tested construct."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt pathway annotation for C6KT66 (AROC_PLAF7, chorismate synthase from P. falciparum) explicitly states: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' Option A ('Metabolic intermediate biosynthesis') is the top-level super-pathway listed in this annotation, so it is technically present. However, option D ('chorismate biosynthesis') is the more specific and functionally precise pathway designation also explicitly stated in the same annotation. The key is supported but arguably imprecise relative to D.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> No concrete sequence-derived argument from the 527-aa sequence alone meaningfully distinguishes chorismate synthase (and thus chorismate biosynthesis) from the other options. Chorismate synthase is a flavin-dependent enzyme with a specific structural fold, but recognizing this from raw sequence without database lookup requires specialized prior knowledge of the exact protein identity. None of the four options can be eliminated or confirmed through general biological reasoning applied to the sequence features visible in the input.


**Missing item-specific fact**

> The specific identity of this sequence as Plasmodium falciparum chorismate synthase (C6KT66/AROC_PLAF7) and its UniProt pathway annotation. Without knowing the protein's identity, a model cannot determine which of the four pathways it participates in.


**Reason**

> The question requires recognizing an exact 527-aa sequence and recalling its database pathway annotation. No general biological reasoning from sequence motifs, composition, or length reliably distinguishes chorismate synthase from a generic metabolic enzyme, a glycosylation factor, or an amino-acid degradation enzyme. This is a protein-identification lookup task dressed as a pathway-prediction task.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> The UniProt pathway annotation is hierarchical: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; …step 7/7.' Both A (the super-pathway) and D (the specific pathway) are explicitly stated. The question asks for the 'primary metabolic or signaling pathway,' which could reasonably refer to either the broad category (A) or the specific pathway (D). In standard biochemical usage, 'chorismate biosynthesis' (D) is the more precise and commonly cited pathway name for this enzyme, making D arguably the better answer. The author's selection of A over D is defensible only if one interprets 'primary' as the top-level UniProt category, but this is not clearly indicated in the question.


### Important caveats

- The pathway annotation is transferred by similarity (ECO:0000250|UniProtKB:Q12640), not independently experimentally verified for this specific Plasmodium entry, though the protein's chorismate synthase function is experimentally confirmed (PubMed 11298276, 31381947).
- The protein also has a second EC number (1.5.1.38, a bifunctional activity per PubMed 31381947), but this does not change the pathway assignment.
- The author key (A) is the super-pathway label; D (chorismate biosynthesis) is the specific pathway and is the more natural answer to 'primary pathway' in most biochemical contexts. This creates a genuine ambiguity that could mislead a well-reasoning model.
- All reviewer evidence is from UniProt annotations; the evaluated model had access only to the raw sequence and the four options.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "No concrete sequence-derived argument from the 527-aa sequence alone meaningfully distinguishes chorismate synthase (and thus chorismate biosynthesis) from the other options. Chorismate synthase is a flavin-dependent enzyme with a specific structural fold, but recognizing this from raw sequence without database lookup requires specialized prior knowledge of the exact protein identity. None of the four options can be eliminated or confirmed through general biological reasoning applied to the sequence features visible in the input.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this sequence as Plasmodium falciparum chorismate synthase (C6KT66/AROC_PLAF7) and its UniProt pathway annotation. Without knowing the protein's identity, a model cannot determine which of the four pathways it participates in.",
    "reason": "The question requires recognizing an exact 527-aa sequence and recalling its database pathway annotation. No general biological reasoning from sequence motifs, composition, or length reliably distinguishes chorismate synthase from a generic metabolic enzyme, a glycosylation factor, or an amino-acid degradation enzyme. This is a protein-identification lookup task dressed as a pathway-prediction task."
  },
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt pathway annotation for C6KT66 (AROC_PLAF7, chorismate synthase from P. falciparum) explicitly states: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' Option A ('Metabolic intermediate biosynthesis') is the top-level super-pathway listed in this annotation, so it is technically present. However, option D ('chorismate biosynthesis') is the more specific and functionally precise pathway designation also explicitly stated in the same annotation. The key is supported but arguably imprecise relative to D."
  },
  "important_caveats": [
    "The pathway annotation is transferred by similarity (ECO:0000250|UniProtKB:Q12640), not independently experimentally verified for this specific Plasmodium entry, though the protein's chorismate synthase function is experimentally confirmed (PubMed 11298276, 31381947).",
    "The protein also has a second EC number (1.5.1.38, a bifunctional activity per PubMed 31381947), but this does not change the pathway assignment.",
    "The author key (A) is the super-pathway label; D (chorismate biosynthesis) is the specific pathway and is the more natural answer to 'primary pathway' in most biochemical contexts. This creates a genuine ambiguity that could mislead a well-reasoning model.",
    "All reviewer evidence is from UniProt annotations; the evaluated model had access only to the raw sequence and the four options."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "The UniProt pathway annotation is hierarchical: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; …step 7/7.' Both A (the super-pathway) and D (the specific pathway) are explicitly stated. The question asks for the 'primary metabolic or signaling pathway,' which could reasonably refer to either the broad category (A) or the specific pathway (D). In standard biochemical usage, 'chorismate biosynthesis' (D) is the more precise and commonly cited pathway name for this enzyme, making D arguably the better answer. The author's selection of A over D is defensible only if one interprets 'primary' as the top-level UniProt category, but this is not clearly indicated in the question."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt pathway annotation for C6KT66 (AROC_PLAF7, chorismate synthase from P. falciparum) explicitly states: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' Option A ('Metabolic intermediate biosynthesis') is the top-level super-pathway listed in this annotation, so it is technically present. However, option D ('chorismate biosynthesis') is the more specific and functionally precise pathway designation also explicitly stated in the same annotation. The key is supported but arguably imprecise relative to D.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "No concrete sequence-derived argument from the 527-aa sequence alone meaningfully distinguishes chorismate synthase (and thus chorismate biosynthesis) from the other options. Chorismate synthase is a flavin-dependent enzyme with a specific structural fold, but recognizing this from raw sequence without database lookup requires specialized prior knowledge of the exact protein identity. None of the four options can be eliminated or confirmed through general biological reasoning applied to the sequence features visible in the input.",
    "missing_item_specific_fact": "The specific identity of this sequence as Plasmodium falciparum chorismate synthase (C6KT66/AROC_PLAF7) and its UniProt pathway annotation. Without knowing the protein's identity, a model cannot determine which of the four pathways it participates in.",
    "reason": "The question requires recognizing an exact 527-aa sequence and recalling its database pathway annotation. No general biological reasoning from sequence motifs, composition, or length reliably distinguishes chorismate synthase from a generic metabolic enzyme, a glycosylation factor, or an amino-acid degradation enzyme. This is a protein-identification lookup task dressed as a pathway-prediction task."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "The UniProt pathway annotation is hierarchical: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; …step 7/7.' Both A (the super-pathway) and D (the specific pathway) are explicitly stated. The question asks for the 'primary metabolic or signaling pathway,' which could reasonably refer to either the broad category (A) or the specific pathway (D). In standard biochemical usage, 'chorismate biosynthesis' (D) is the more precise and commonly cited pathway name for this enzyme, making D arguably the better answer. The author's selection of A over D is defensible only if one interprets 'primary' as the top-level UniProt category, but this is not clearly indicated in the question."
  },
  "important_caveats": [
    "The pathway annotation is transferred by similarity (ECO:0000250|UniProtKB:Q12640), not independently experimentally verified for this specific Plasmodium entry, though the protein's chorismate synthase function is experimentally confirmed (PubMed 11298276, 31381947).",
    "The protein also has a second EC number (1.5.1.38, a bifunctional activity per PubMed 31381947), but this does not change the pathway assignment.",
    "The author key (A) is the super-pathway label; D (chorismate biosynthesis) is the specific pathway and is the more natural answer to 'primary pathway' in most biochemical contexts. This creates a genuine ambiguity that could mislead a well-reasoning model.",
    "All reviewer evidence is from UniProt annotations; the evaluated model had access only to the raw sequence and the four options."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched sequence is annotated as chorismate synthase, with a pathway annotation placing it in metabolic intermediate biosynthesis and specifically chorismate biosynthesis. Thus A is scientifically supported, although D is a more specific description of the same pathway. The pathway annotation is transferred by similarity, while the enzyme-name annotation has cited experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A sequence recognizable as belonging to the conserved chorismate-synthase family supports a role in chorismate production, a biosynthetic route for metabolic intermediates. That makes A and especially the more specific D more plausible than amino-acid degradation or protein glycosylation. This uses family-level sequence knowledge and pathway biology, not knowledge of this exact protein's record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable recognition of chorismate-synthase homologs can meaningfully distinguish the biosynthetic choices from B and C. It does not uniquely select A over D because the two choices describe nested levels of the same pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Chorismate biosynthesis is a specific form of metabolic intermediate biosynthesis. The question does not specify whether to choose the broad pathway category or the most specific pathway offered, so both A and D are defensible.


### Important caveats

- The reviewer-only sequence-matched record supports the expected answer, but its pathway annotation is transferred by similarity rather than presented as direct experimental pathway evidence.
- The exact organism and target-specific annotations were not part of the original input and are not needed for the family-level inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A sequence recognizable as belonging to the conserved chorismate-synthase family supports a role in chorismate production, a biosynthetic route for metabolic intermediates. That makes A and especially the more specific D more plausible than amino-acid degradation or protein glycosylation. This uses family-level sequence knowledge and pathway biology, not knowledge of this exact protein's record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of chorismate-synthase homologs can meaningfully distinguish the biosynthetic choices from B and C. It does not uniquely select A over D because the two choices describe nested levels of the same pathway."
  },
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as chorismate synthase, with a pathway annotation placing it in metabolic intermediate biosynthesis and specifically chorismate biosynthesis. Thus A is scientifically supported, although D is a more specific description of the same pathway. The pathway annotation is transferred by similarity, while the enzyme-name annotation has cited experimental evidence."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched record supports the expected answer, but its pathway annotation is transferred by similarity rather than presented as direct experimental pathway evidence.",
    "The exact organism and target-specific annotations were not part of the original input and are not needed for the family-level inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Chorismate biosynthesis is a specific form of metabolic intermediate biosynthesis. The question does not specify whether to choose the broad pathway category or the most specific pathway offered, so both A and D are defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as chorismate synthase, with a pathway annotation placing it in metabolic intermediate biosynthesis and specifically chorismate biosynthesis. Thus A is scientifically supported, although D is a more specific description of the same pathway. The pathway annotation is transferred by similarity, while the enzyme-name annotation has cited experimental evidence.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A sequence recognizable as belonging to the conserved chorismate-synthase family supports a role in chorismate production, a biosynthetic route for metabolic intermediates. That makes A and especially the more specific D more plausible than amino-acid degradation or protein glycosylation. This uses family-level sequence knowledge and pathway biology, not knowledge of this exact protein's record.",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of chorismate-synthase homologs can meaningfully distinguish the biosynthetic choices from B and C. It does not uniquely select A over D because the two choices describe nested levels of the same pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Chorismate biosynthesis is a specific form of metabolic intermediate biosynthesis. The question does not specify whether to choose the broad pathway category or the most specific pathway offered, so both A and D are defensible."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched record supports the expected answer, but its pathway annotation is transferred by similarity rather than presented as direct experimental pathway evidence.",
    "The exact organism and target-specific annotations were not part of the original input and are not needed for the family-level inference."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt pathway annotation for C6KT66 (chorismate synthase from P. falciparum) reads: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' The phrase 'Metabolic intermediate biosynthesis' appears verbatim as the top-level pathway category, supporting choice A. However, 'chorismate biosynthesis' (choice D) also appears verbatim in the same annotation as the sub-pathway, so D is equally supported by the annotation.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> A model recognizing the sequence as chorismate synthase (via the FMN-binding domain motifs, ~527 aa length, and characteristic sequence patterns shared with other chorismate synthases) would identify the enzyme's primary biochemical function as catalyzing the final step of chorismate biosynthesis (the shikimate pathway). This naturally maps to option D. Choosing A ('Metabolic intermediate biosynthesis') over D requires knowing that UniProt's hierarchical pathway annotation places 'chorismate biosynthesis' as a sub-pathway under the superpathway 'Metabolic intermediate biosynthesis,' and that the question intends the superpathway as the 'primary' pathway. This is an annotation-taxonomy convention, not a transferable biological inference.


**Missing item-specific fact**

> The specific UniProt pathway annotation hierarchy convention that designates 'Metabolic intermediate biosynthesis' as the top-level 'primary pathway' while treating 'chorismate biosynthesis' as a sub-pathway, and the benchmark's convention of selecting the top-level category as the correct answer rather than the more specific sub-pathway.


**Reason**

> Biological reasoning from the sequence (recognizing chorismate synthase via conserved FMN-binding motifs and family features) leads most naturally to 'chorismate biosynthesis' (D) as the primary pathway. Distinguishing A from D requires knowledge of UniProt's specific pathway annotation hierarchy and the benchmark's convention of selecting the superpathway. This is an annotation-convention fact specific to how UniProt structures pathway names, not a transferable biological principle.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "D"
]
```

> Both 'Metabolic intermediate biosynthesis' (A) and 'chorismate biosynthesis' (D) appear verbatim in the same UniProt pathway annotation string. The question asks for the 'primary metabolic or signaling pathway,' but the annotation is hierarchical ('Metabolic intermediate biosynthesis; chorismate biosynthesis; ...'), making it ambiguous whether 'primary' refers to the top-level superpathway (A) or the specific sub-pathway (D). From standard biochemical usage, D is the more natural and specific answer for chorismate synthase; A is the broader UniProt category.


### Important caveats

- Both A and D appear in the same UniProt annotation; the question's wording 'primary pathway' does not unambiguously select between the superpathway and sub-pathway levels.
- The sequence is recognizable as chorismate synthase from conserved FMN-binding domain motifs shared with homologs in other organisms, making family-level identification feasible.
- The author's choice of A follows UniProt's top-level pathway category convention, but this is an annotation taxonomy choice rather than a biological fact that would override the more specific pathway name D.
- The pathway annotation evidence code is ECO:0000250 (similarity to Q12640, a bacterial chorismate synthase), indicating the pathway assignment is by similarity rather than direct experimental pathway tracing in P. falciparum.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A model recognizing the sequence as chorismate synthase (via the FMN-binding domain motifs, ~527 aa length, and characteristic sequence patterns shared with other chorismate synthases) would identify the enzyme's primary biochemical function as catalyzing the final step of chorismate biosynthesis (the shikimate pathway). This naturally maps to option D. Choosing A ('Metabolic intermediate biosynthesis') over D requires knowing that UniProt's hierarchical pathway annotation places 'chorismate biosynthesis' as a sub-pathway under the superpathway 'Metabolic intermediate biosynthesis,' and that the question intends the superpathway as the 'primary' pathway. This is an annotation-taxonomy convention, not a transferable biological inference.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt pathway annotation hierarchy convention that designates 'Metabolic intermediate biosynthesis' as the top-level 'primary pathway' while treating 'chorismate biosynthesis' as a sub-pathway, and the benchmark's convention of selecting the top-level category as the correct answer rather than the more specific sub-pathway.",
    "reason": "Biological reasoning from the sequence (recognizing chorismate synthase via conserved FMN-binding motifs and family features) leads most naturally to 'chorismate biosynthesis' (D) as the primary pathway. Distinguishing A from D requires knowledge of UniProt's specific pathway annotation hierarchy and the benchmark's convention of selecting the superpathway. This is an annotation-convention fact specific to how UniProt structures pathway names, not a transferable biological principle."
  },
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt pathway annotation for C6KT66 (chorismate synthase from P. falciparum) reads: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' The phrase 'Metabolic intermediate biosynthesis' appears verbatim as the top-level pathway category, supporting choice A. However, 'chorismate biosynthesis' (choice D) also appears verbatim in the same annotation as the sub-pathway, so D is equally supported by the annotation."
  },
  "important_caveats": [
    "Both A and D appear in the same UniProt annotation; the question's wording 'primary pathway' does not unambiguously select between the superpathway and sub-pathway levels.",
    "The sequence is recognizable as chorismate synthase from conserved FMN-binding domain motifs shared with homologs in other organisms, making family-level identification feasible.",
    "The author's choice of A follows UniProt's top-level pathway category convention, but this is an annotation taxonomy choice rather than a biological fact that would override the more specific pathway name D.",
    "The pathway annotation evidence code is ECO:0000250 (similarity to Q12640, a bacterial chorismate synthase), indicating the pathway assignment is by similarity rather than direct experimental pathway tracing in P. falciparum."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "D"
    ],
    "reason": "Both 'Metabolic intermediate biosynthesis' (A) and 'chorismate biosynthesis' (D) appear verbatim in the same UniProt pathway annotation string. The question asks for the 'primary metabolic or signaling pathway,' but the annotation is hierarchical ('Metabolic intermediate biosynthesis; chorismate biosynthesis; ...'), making it ambiguous whether 'primary' refers to the top-level superpathway (A) or the specific sub-pathway (D). From standard biochemical usage, D is the more natural and specific answer for chorismate synthase; A is the broader UniProt category."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0108",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt pathway annotation for C6KT66 (chorismate synthase from P. falciparum) reads: 'Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7.' The phrase 'Metabolic intermediate biosynthesis' appears verbatim as the top-level pathway category, supporting choice A. However, 'chorismate biosynthesis' (choice D) also appears verbatim in the same annotation as the sub-pathway, so D is equally supported by the annotation.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "A model recognizing the sequence as chorismate synthase (via the FMN-binding domain motifs, ~527 aa length, and characteristic sequence patterns shared with other chorismate synthases) would identify the enzyme's primary biochemical function as catalyzing the final step of chorismate biosynthesis (the shikimate pathway). This naturally maps to option D. Choosing A ('Metabolic intermediate biosynthesis') over D requires knowing that UniProt's hierarchical pathway annotation places 'chorismate biosynthesis' as a sub-pathway under the superpathway 'Metabolic intermediate biosynthesis,' and that the question intends the superpathway as the 'primary' pathway. This is an annotation-taxonomy convention, not a transferable biological inference.",
    "missing_item_specific_fact": "The specific UniProt pathway annotation hierarchy convention that designates 'Metabolic intermediate biosynthesis' as the top-level 'primary pathway' while treating 'chorismate biosynthesis' as a sub-pathway, and the benchmark's convention of selecting the top-level category as the correct answer rather than the more specific sub-pathway.",
    "reason": "Biological reasoning from the sequence (recognizing chorismate synthase via conserved FMN-binding motifs and family features) leads most naturally to 'chorismate biosynthesis' (D) as the primary pathway. Distinguishing A from D requires knowledge of UniProt's specific pathway annotation hierarchy and the benchmark's convention of selecting the superpathway. This is an annotation-convention fact specific to how UniProt structures pathway names, not a transferable biological principle."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "D"],
    "reason": "Both 'Metabolic intermediate biosynthesis' (A) and 'chorismate biosynthesis' (D) appear verbatim in the same UniProt pathway annotation string. The question asks for the 'primary metabolic or signaling pathway,' but the annotation is hierarchical ('Metabolic intermediate biosynthesis; chorismate biosynthesis; ...'), making it ambiguous whether 'primary' refers to the top-level superpathway (A) or the specific sub-pathway (D). From standard biochemical usage, D is the more natural and specific answer for chorismate synthase; A is the broader UniProt category."
  },
  "important_caveats": [
    "Both A and D appear in the same UniProt annotation; the question's wording 'primary pathway' does not unambiguously select between the superpathway and sub-pathway levels.",
    "The sequence is recognizable as chorismate synthase from conserved FMN-binding domain motifs shared with homologs in other organisms, making family-level identification feasible.",
    "The author's choice of A follows UniProt's top-level pathway category convention, but this is an annotation taxonomy choice rather than a biological fact that would override the more specific pathway name D.",
    "The pathway annotation evidence code is ECO:0000250 (similarity to Q12640, a bacterial chorismate synthase), indicating the pathway assignment is by similarity rather than direct experimental pathway tracing in P. falciparum."
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
  "requested_accession": "C6KT66",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "benchmark_sequence_length": 527,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 91,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-09-01",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "current_source_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "current_source_sequence_length": 527,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 89,
  "selected_historical_version": {
    "accession": "C6KT66",
    "database": "Swiss-Prot",
    "entryVersion": 89,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AROC_PLAF7",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "selected_historical_source_sequence_sha256": "fe5eb10add0487313022107f5b8f7a01b13d2045fba1e86358f100bf68ffcc0d",
  "selected_historical_source_sequence_length": 527,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 89,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"C6KT66\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":91,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-09-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.38\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11298276\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"4.2.3.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"31381947\",\"source\":\"PubMed\"}],\"value\":\"Chorismate synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"}],\"value\":\"PfCS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q12640\",\"source\":\"UniProtKB\"}],\"value\":\"Metabolic intermediate biosynthesis; chorismate biosynthesis; chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Fitzpatrick T.\",\"Ricken S.\",\"Lanzer M.\",\"Amrhein N.\",\"Macheroux P.\",\"Kappes B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11298276\"},{\"database\":\"DOI\",\"id\":\"10.1046/j.1365-2958.2001.02366.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"65\",\"id\":\"11298276\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"75\",\"publicationDate\":\"2001\",\"title\":\"Subcellular localization and characterization of chorismate synthase in the apicomplexan Plasmodium falciparum.\",\"volume\":\"40\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"11298276\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"DD2\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBCELLULAR LOCATION\",\"DEVELOPMENTAL STAGE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/C6KT66.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/C6KT66.json",
  "source_sha256": "b6ae207868ea88bb5964ba12c0f98a873e25a94ca43881742871c2ccf03a8e83",
  "retrieved_utc": "2026-11-02T04:27:31.463877+00:00",
  "json_pointer": "/references/3",
  "excerpt": "{\"citation\":{\"authors\":[\"Khera H.K.\",\"Singh S.K.\",\"Singh S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"31381947\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molbiopara.2019.111202\"}],\"citationType\":\"journal article\",\"firstPage\":\"111202\",\"id\":\"31381947\",\"journal\":\"Mol. Biochem. Parasitol.\",\"lastPage\":\"111202\",\"publicationDate\":\"2019\",\"title\":\"Chorismate synthase from malaria parasites is bifunctional enzyme.\",\"volume\":\"233\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "source_locator": "lines 1-15",
  "excerpt": "ID   AROC_PLAF7              Reviewed;         527 AA.\nAC   C6KT66;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-SEP-2009, sequence version 1.\nDT   28-JAN-2026, entry version 89.\nDE   RecName: Full=Chorismate synthase {ECO:0000303|PubMed:11298276, ECO:0000303|PubMed:31381947};\nDE            Short=PfCS {ECO:0000303|PubMed:11298276};\nDE            EC=1.5.1.38 {ECO:0000305|PubMed:31381947};\nDE            EC=4.2.3.5 {ECO:0000269|PubMed:11298276, ECO:0000269|PubMed:31381947};\nGN   Name=CS {ECO:0000305}; Synonyms=AROC {ECO:0000303|PubMed:11298276};\nGN   ORFNames=PF3D7_0623000 {ECO:0000312|EMBL:CAG25042.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "source_locator": "lines 50-58",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION, AND DEVELOPMENTAL\nRP   STAGE.\nRC   STRAIN=DD2 {ECO:0000303|PubMed:11298276};\nRX   PubMed=11298276; DOI=10.1046/j.1365-2958.2001.02366.x;\nRA   Fitzpatrick T., Ricken S., Lanzer M., Amrhein N., Macheroux P., Kappes B.;\nRT   \"Subcellular localization and characterization of chorismate synthase in\nRT   the apicomplexan Plasmodium falciparum.\";\nRL   Mol. Microbiol. 40:65-75(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "source_locator": "lines 59-64",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=31381947; DOI=10.1016/j.molbiopara.2019.111202;\nRA   Khera H.K., Singh S.K., Singh S.;\nRT   \"Chorismate synthase from malaria parasites is bifunctional enzyme.\";\nRL   Mol. Biochem. Parasitol. 233:111202-111202(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/C6KT66?format=txt&versions=89",
  "source_sha256": "a21a25bc44bf029252f986ed96532642a07f6208fc629be2d9c836438bd38e9b",
  "retrieved_utc": "2026-11-02T04:27:34.407274+00:00",
  "source_locator": "lines 86-88",
  "excerpt": "CC   -!- PATHWAY: Metabolic intermediate biosynthesis; chorismate biosynthesis;\nCC       chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step\nCC       7/7. {ECO:0000250|UniProtKB:Q12640}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 89,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 108. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
