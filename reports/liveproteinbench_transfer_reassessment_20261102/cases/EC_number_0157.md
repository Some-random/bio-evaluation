# EC_number_0157: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/EC_number_0157.txt)

**Task:** `EC_number`  
**Author key, unchanged:** **B** — 3.1.1.80

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MGFAARPFHIVFSLFVLAGATQALIICPFDSIYQFGDSISDTGNYIRILPNGPAAAAANFPYGITFPGIPTGRFSDGRLIVDFIARVLGLPLLNPYLQQNASFKNGVNFAVGGATALNSSVLAAAGVQIPDIYLIPLSTQLNWFQTYLRSNCSSPTECSKKVQNSLFLIGNIGNNDVNYALPYRTIQEIEAYVPSIAKAVANATREIIRLGGRRIIVPGTFPFGCLPRNLYLFPNGDKDDLGCLRRLNDLSIYFNNLFQQALNSLRIEFPQAVIIYADYYNAFRFLLRNARALGFTSTLQSCCGIGGPYNFDLNRLCGFPGVPVCRNPREYIQWDGFHYTEAAHRHIVQYLIPDILKELKCS

[Multiple Choices]
A. 3.1.3.16
B. 3.1.1.80
C. 1.1.1.12
D. 6.3.5.1
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

> The supplied sequence exactly matches the UniProtKB entry for acetylajmalan esterase 2, which assigns EC 3.1.1.80 and annotates its catalytic reaction with ECO:0000269 evidence linked to a publication. The historical entry also matches the sequence and records the same EC assignment. This supports choice B, though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest an enzyme with hydrolase-like properties, but the choices include distinct catalytic classes and the sequence alone does not establish the substrate-specific reaction needed to identify EC 3.1.1.80.


**Missing item-specific fact**

> The protein's identity and experimentally characterized activity as an acetylajmalan esterase, including its substrate-specific deacetylation reaction.


**Reason**

> The exact EC assignment depends on protein-specific functional annotation or experimental characterization absent from the prompt. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from supplied context.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports choice B; no other listed EC number is supported for this sequence.


### Important caveats

- The reviewer-only UniProt records match the supplied sequence; those records were not available to the evaluated model.
- The curated annotation cites experimental evidence, but the cited primary paper was not independently retrieved or validated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest an enzyme with hydrolase-like properties, but the choices include distinct catalytic classes and the sequence alone does not establish the substrate-specific reaction needed to identify EC 3.1.1.80.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's identity and experimentally characterized activity as an acetylajmalan esterase, including its substrate-specific deacetylation reaction.",
    "reason": "The exact EC assignment depends on protein-specific functional annotation or experimental characterization absent from the prompt. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from supplied context."
  },
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProtKB entry for acetylajmalan esterase 2, which assigns EC 3.1.1.80 and annotates its catalytic reaction with ECO:0000269 evidence linked to a publication. The historical entry also matches the sequence and records the same EC assignment. This supports choice B, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied sequence; those records were not available to the evaluated model.",
    "The curated annotation cites experimental evidence, but the cited primary paper was not independently retrieved or validated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports choice B; no other listed EC number is supported for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProtKB entry for acetylajmalan esterase 2, which assigns EC 3.1.1.80 and annotates its catalytic reaction with ECO:0000269 evidence linked to a publication. The historical entry also matches the sequence and records the same EC assignment. This supports choice B, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest an enzyme with hydrolase-like properties, but the choices include distinct catalytic classes and the sequence alone does not establish the substrate-specific reaction needed to identify EC 3.1.1.80.",
    "missing_item_specific_fact": "The protein's identity and experimentally characterized activity as an acetylajmalan esterase, including its substrate-specific deacetylation reaction.",
    "reason": "The exact EC assignment depends on protein-specific functional annotation or experimental characterization absent from the prompt. Recognizing the sequence or recalling its database record would be lookup or memorization, not reasoning from supplied context."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports choice B; no other listed EC number is supported for this sequence."
  },
  "important_caveats": [
    "The reviewer-only UniProt records match the supplied sequence; those records were not available to the evaluated model.",
    "The curated annotation cites experimental evidence, but the cited primary paper was not independently retrieved or validated."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXJ5 (sequence SHA256 matched) annotates this protein as Acetylajmalan esterase 2 (RsAAE2) with EC 3.1.1.80, supported by experimental evidence (ECO:0000269) from PubMed:38212296 (Guo et al., Nat. Commun. 2024). The catalytic reaction 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+) is experimentally confirmed. The sequence in the question matches the canonical entry exactly (362 aa, precursor).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> One can argue from general sequence features that the protein lacks Rossmann-fold characteristics (eliminating C, L-lactate dehydrogenase) and lacks glutamine synthetase motifs (eliminating D). The presence of a signal peptide and cysteine-rich C-terminal region is broadly consistent with a secreted hydrolase. However, distinguishing EC 3.1.1.80 (acetylajmalan esterase) from EC 3.1.3.16 (phosphoserine phosphatase) requires knowing the specific substrate (acetylated alkaloid vs. phosphoserine), which is not inferable from sequence architecture alone. No canonical GxSxG nucleophile-elbow motif is clearly identifiable, and the overall fold does not uniquely specify carboxylesterase over phosphatase activity.


**Missing item-specific fact**

> The specific identity of this protein as Acetylajmalan esterase 2 from Rauvolfia serpentina, and the experimental demonstration that it hydrolyzes 17-O-acetylnorajmaline (EC 3.1.1.80), are item-specific facts not derivable from the sequence alone. EC 3.1.1.80 is an extremely obscure, recently characterized EC number (first annotated 2025) that cannot be predicted by general enzymology reasoning.


**Reason**

> While options C and D can be eliminated by general biological reasoning (absence of dehydrogenase or ligase structural features), the critical discrimination between A (3.1.3.16, phosphoserine phosphatase) and B (3.1.1.80, acetylajmalan esterase) depends on knowing this protein's specific substrate specificity, which is an experimental finding from a 2024 paper. No sequence motif, domain architecture, or general biological principle uniquely identifies this as an acetylajmalan esterase rather than a phosphatase without database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although both A and B are esterases (EC 3.1.x.x), the question asks for the complete 4-digit EC number. Without organism context or substrate information, a model cannot definitively choose between a phosphoserine phosphatase and a carboxylesterase acting on an acetylated alkaloid. However, the expected answer B is the only one experimentally validated for this exact sequence, so no other option is actually correct.


### Important caveats

- EC 3.1.1.80 was first annotated in UniProt on 2025-06-18 based on a 2024 Nature Communications paper; this is an extremely recent and obscure EC number unlikely to be in most training data.
- The second catalytic activity (17-O-acetylajmaline → ajmaline) is annotated by similarity (ECO:0000250) from Q3MKY2, not directly demonstrated for P0DXJ5.
- The identity of the protein (P0DXJ5) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence with no accession or organism context.
- The sequence lacks a clearly identifiable canonical GxSxG serine hydrolase motif, making even broad esterase classification from sequence difficult.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "One can argue from general sequence features that the protein lacks Rossmann-fold characteristics (eliminating C, L-lactate dehydrogenase) and lacks glutamine synthetase motifs (eliminating D). The presence of a signal peptide and cysteine-rich C-terminal region is broadly consistent with a secreted hydrolase. However, distinguishing EC 3.1.1.80 (acetylajmalan esterase) from EC 3.1.3.16 (phosphoserine phosphatase) requires knowing the specific substrate (acetylated alkaloid vs. phosphoserine), which is not inferable from sequence architecture alone. No canonical GxSxG nucleophile-elbow motif is clearly identifiable, and the overall fold does not uniquely specify carboxylesterase over phosphatase activity.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identity of this protein as Acetylajmalan esterase 2 from Rauvolfia serpentina, and the experimental demonstration that it hydrolyzes 17-O-acetylnorajmaline (EC 3.1.1.80), are item-specific facts not derivable from the sequence alone. EC 3.1.1.80 is an extremely obscure, recently characterized EC number (first annotated 2025) that cannot be predicted by general enzymology reasoning.",
    "reason": "While options C and D can be eliminated by general biological reasoning (absence of dehydrogenase or ligase structural features), the critical discrimination between A (3.1.3.16, phosphoserine phosphatase) and B (3.1.1.80, acetylajmalan esterase) depends on knowing this protein's specific substrate specificity, which is an experimental finding from a 2024 paper. No sequence motif, domain architecture, or general biological principle uniquely identifies this as an acetylajmalan esterase rather than a phosphatase without database lookup."
  },
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H1",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ5 (sequence SHA256 matched) annotates this protein as Acetylajmalan esterase 2 (RsAAE2) with EC 3.1.1.80, supported by experimental evidence (ECO:0000269) from PubMed:38212296 (Guo et al., Nat. Commun. 2024). The catalytic reaction 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+) is experimentally confirmed. The sequence in the question matches the canonical entry exactly (362 aa, precursor)."
  },
  "important_caveats": [
    "EC 3.1.1.80 was first annotated in UniProt on 2025-06-18 based on a 2024 Nature Communications paper; this is an extremely recent and obscure EC number unlikely to be in most training data.",
    "The second catalytic activity (17-O-acetylajmaline → ajmaline) is annotated by similarity (ECO:0000250) from Q3MKY2, not directly demonstrated for P0DXJ5.",
    "The identity of the protein (P0DXJ5) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence with no accession or organism context.",
    "The sequence lacks a clearly identifiable canonical GxSxG serine hydrolase motif, making even broad esterase classification from sequence difficult."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although both A and B are esterases (EC 3.1.x.x), the question asks for the complete 4-digit EC number. Without organism context or substrate information, a model cannot definitively choose between a phosphoserine phosphatase and a carboxylesterase acting on an acetylated alkaloid. However, the expected answer B is the only one experimentally validated for this exact sequence, so no other option is actually correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXJ5 (sequence SHA256 matched) annotates this protein as Acetylajmalan esterase 2 (RsAAE2) with EC 3.1.1.80, supported by experimental evidence (ECO:0000269) from PubMed:38212296 (Guo et al., Nat. Commun. 2024). The catalytic reaction 17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+) is experimentally confirmed. The sequence in the question matches the canonical entry exactly (362 aa, precursor).",
    "evidence_ids": ["C4", "C5", "C7", "H1", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "One can argue from general sequence features that the protein lacks Rossmann-fold characteristics (eliminating C, L-lactate dehydrogenase) and lacks glutamine synthetase motifs (eliminating D). The presence of a signal peptide and cysteine-rich C-terminal region is broadly consistent with a secreted hydrolase. However, distinguishing EC 3.1.1.80 (acetylajmalan esterase) from EC 3.1.3.16 (phosphoserine phosphatase) requires knowing the specific substrate (acetylated alkaloid vs. phosphoserine), which is not inferable from sequence architecture alone. No canonical GxSxG nucleophile-elbow motif is clearly identifiable, and the overall fold does not uniquely specify carboxylesterase over phosphatase activity.",
    "missing_item_specific_fact": "The specific identity of this protein as Acetylajmalan esterase 2 from Rauvolfia serpentina, and the experimental demonstration that it hydrolyzes 17-O-acetylnorajmaline (EC 3.1.1.80), are item-specific facts not derivable from the sequence alone. EC 3.1.1.80 is an extremely obscure, recently characterized EC number (first annotated 2025) that cannot be predicted by general enzymology reasoning.",
    "reason": "While options C and D can be eliminated by general biological reasoning (absence of dehydrogenase or ligase structural features), the critical discrimination between A (3.1.3.16, phosphoserine phosphatase) and B (3.1.1.80, acetylajmalan esterase) depends on knowing this protein's specific substrate specificity, which is an experimental finding from a 2024 paper. No sequence motif, domain architecture, or general biological principle uniquely identifies this as an acetylajmalan esterase rather than a phosphatase without database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although both A and B are esterases (EC 3.1.x.x), the question asks for the complete 4-digit EC number. Without organism context or substrate information, a model cannot definitively choose between a phosphoserine phosphatase and a carboxylesterase acting on an acetylated alkaloid. However, the expected answer B is the only one experimentally validated for this exact sequence, so no other option is actually correct."
  },
  "important_caveats": [
    "EC 3.1.1.80 was first annotated in UniProt on 2025-06-18 based on a 2024 Nature Communications paper; this is an extremely recent and obscure EC number unlikely to be in most training data.",
    "The second catalytic activity (17-O-acetylajmaline → ajmaline) is annotated by similarity (ECO:0000250) from Q3MKY2, not directly demonstrated for P0DXJ5.",
    "The identity of the protein (P0DXJ5) was inferred by the reviewer from dataset metadata; the evaluated model received only the raw sequence with no accession or organism context.",
    "The sequence lacks a clearly identifiable canonical GxSxG serine hydrolase motif, making even broad esterase classification from sequence difficult."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The matched-sequence UniProt annotation assigns EC 3.1.1.80 and records the ester-hydrolysis reaction for that EC with ECO:0000269 evidence linked to a publication. This supports the key, though the primary paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a GDSIS segment matching the common GxSxG nucleophile motif of serine hydrolases, making hydrolysis of an ester a credible family-level inference. That points toward the EC 3.1.1 hydrolase option B over the phosphatase, dehydrogenase, and ligase alternatives. The motif does not by itself establish the precise substrate or EC subclass.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about serine-hydrolase motifs meaningfully distinguishes the offered ester-hydrolase choice from the alternatives, even though exact EC 3.1.1.80 activity would require more specific evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-based inference favors B among the listed choices; no other offered option is comparably supported.


### Important caveats

- A serine-hydrolase motif supports an enzyme-class inference, not the exact substrate specificity or full four-digit EC assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a GDSIS segment matching the common GxSxG nucleophile motif of serine hydrolases, making hydrolysis of an ester a credible family-level inference. That points toward the EC 3.1.1 hydrolase option B over the phosphatase, dehydrogenase, and ligase alternatives. The motif does not by itself establish the precise substrate or EC subclass.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about serine-hydrolase motifs meaningfully distinguishes the offered ester-hydrolase choice from the alternatives, even though exact EC 3.1.1.80 activity would require more specific evidence."
  },
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 3.1.1.80 and records the ester-hydrolysis reaction for that EC with ECO:0000269 evidence linked to a publication. This supports the key, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "A serine-hydrolase motif supports an enzyme-class inference, not the exact substrate specificity or full four-digit EC assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based inference favors B among the listed choices; no other offered option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation assigns EC 3.1.1.80 and records the ester-hydrolysis reaction for that EC with ECO:0000269 evidence linked to a publication. This supports the key, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a GDSIS segment matching the common GxSxG nucleophile motif of serine hydrolases, making hydrolysis of an ester a credible family-level inference. That points toward the EC 3.1.1 hydrolase option B over the phosphatase, dehydrogenase, and ligase alternatives. The motif does not by itself establish the precise substrate or EC subclass.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about serine-hydrolase motifs meaningfully distinguishes the offered ester-hydrolase choice from the alternatives, even though exact EC 3.1.1.80 activity would require more specific evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-based inference favors B among the listed choices; no other offered option is comparably supported."
  },
  "important_caveats": [
    "A serine-hydrolase motif supports an enzyme-class inference, not the exact substrate specificity or full four-digit EC assignment."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence (C4, C5, H2, H4) confirms that P0DXJ5 is annotated as 'Acetylajmalan esterase 2' with EC 3.1.1.80, supported by experimental evidence (ECO:0000269|PubMed:38212296, Nat. Commun. 2024). The catalytic reaction (17-O-acetylnorajmaline + H2O = norajmaline + acetate + H+) is a carboxylesterase reaction consistent with EC 3.1.1.80. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options span three distinct EC major classes (1=oxidoreductase, 3=hydrolase, 6=ligase) and two hydrolase subclasses (3.1.1=carboxylesterase, 3.1.3=phosphatase). Transferable reasoning: (1) Option C (1.1.1.12, alcohol dehydrogenase NADP+) requires a Rossmann-fold nucleotide-binding motif (GxGxG) and typically a zinc-binding Cys-X2-His-X3-His site; neither is present in this sequence, and the N-terminal signal peptide is atypical for cytoplasmic ADHs. (2) Option D (6.3.5.1, glutamine synthetase) requires distinctive ATP-binding motifs, a GS-like fold, and metal-coordinating residues; none are recognizable, and GS is cytoplasmic. (3) Between A (3.1.3.16, phosphatase) and B (3.1.1.80, carboxylesterase): the clear N-terminal signal peptide (MGFAARPFHIVFSLFVLAGATQALIIC) indicates a secreted/membrane-targeted protein. Plant phosphatases (EC 3.1.3.x) are overwhelmingly intracellular, whereas plant esterases involved in alkaloid/terpenoid secondary metabolism are frequently secreted or ER-localized. The ~362-aa size, hydrophobic core architecture, and absence of canonical phosphatase metal-binding motifs (DXDXD, alkaline phosphatase His/Asp clusters) further favor an α/β-hydrolase esterase over a phosphatase. While a perfect GXSXG motif is not unambiguously identifiable in this sequence, the overall domain architecture and cellular-localization logic learned from other plant secondary-metabolism esterases meaningfully favor B over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate C (no Rossmann fold, no ADH motifs) and D (no GS/ligase motifs) by absence of required functional motifs. The signal-peptide-to-plant-secondary-metabolism-esterase correlation and absence of phosphatase metal-binding motifs provide a probabilistic but meaningful preference for B over A. This is a legitimate family-level and localization-pattern inference transferable from other plant esterases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span different EC major classes and subclasses. The elimination of C and D is straightforward by absence of required motifs. The A-vs-B distinction is supported by the signal peptide and absence of phosphatase motifs, though not absolutely airtight; B remains the most defensible choice given the offered alternatives.


### Important caveats

- The GXSXG catalytic motif typical of α/β-hydrolases is not unambiguously identifiable in this sequence, weakening the direct structural argument for esterase activity, though overall architecture and localization logic remain supportive.
- EC 3.1.1.80 is a highly specific 4th-digit designation (acetylajmalan esterase); however, since only one 3.1.1.x option is offered, the task effectively reduces to identifying the EC class/subclass, which is more achievable through transferable reasoning.
- The signal-peptide-to-secreted-plant-esterase correlation is a statistical/family-level pattern, not a universal rule; some phosphatases are secreted, and not all plant esterases are secreted.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options span three distinct EC major classes (1=oxidoreductase, 3=hydrolase, 6=ligase) and two hydrolase subclasses (3.1.1=carboxylesterase, 3.1.3=phosphatase). Transferable reasoning: (1) Option C (1.1.1.12, alcohol dehydrogenase NADP+) requires a Rossmann-fold nucleotide-binding motif (GxGxG) and typically a zinc-binding Cys-X2-His-X3-His site; neither is present in this sequence, and the N-terminal signal peptide is atypical for cytoplasmic ADHs. (2) Option D (6.3.5.1, glutamine synthetase) requires distinctive ATP-binding motifs, a GS-like fold, and metal-coordinating residues; none are recognizable, and GS is cytoplasmic. (3) Between A (3.1.3.16, phosphatase) and B (3.1.1.80, carboxylesterase): the clear N-terminal signal peptide (MGFAARPFHIVFSLFVLAGATQALIIC) indicates a secreted/membrane-targeted protein. Plant phosphatases (EC 3.1.3.x) are overwhelmingly intracellular, whereas plant esterases involved in alkaloid/terpenoid secondary metabolism are frequently secreted or ER-localized. The ~362-aa size, hydrophobic core architecture, and absence of canonical phosphatase metal-binding motifs (DXDXD, alkaline phosphatase His/Asp clusters) further favor an α/β-hydrolase esterase over a phosphatase. While a perfect GXSXG motif is not unambiguously identifiable in this sequence, the overall domain architecture and cellular-localization logic learned from other plant secondary-metabolism esterases meaningfully favor B over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C (no Rossmann fold, no ADH motifs) and D (no GS/ligase motifs) by absence of required functional motifs. The signal-peptide-to-plant-secondary-metabolism-esterase correlation and absence of phosphatase metal-binding motifs provide a probabilistic but meaningful preference for B over A. This is a legitimate family-level and localization-pattern inference transferable from other plant esterases."
  },
  "case_id": "EC_number_0157",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence (C4, C5, H2, H4) confirms that P0DXJ5 is annotated as 'Acetylajmalan esterase 2' with EC 3.1.1.80, supported by experimental evidence (ECO:0000269|PubMed:38212296, Nat. Commun. 2024). The catalytic reaction (17-O-acetylnorajmaline + H2O = norajmaline + acetate + H+) is a carboxylesterase reaction consistent with EC 3.1.1.80. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The GXSXG catalytic motif typical of α/β-hydrolases is not unambiguously identifiable in this sequence, weakening the direct structural argument for esterase activity, though overall architecture and localization logic remain supportive.",
    "EC 3.1.1.80 is a highly specific 4th-digit designation (acetylajmalan esterase); however, since only one 3.1.1.x option is offered, the task effectively reduces to identifying the EC class/subclass, which is more achievable through transferable reasoning.",
    "The signal-peptide-to-secreted-plant-esterase correlation is a statistical/family-level pattern, not a universal rule; some phosphatases are secreted, and not all plant esterases are secreted."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span different EC major classes and subclasses. The elimination of C and D is straightforward by absence of required motifs. The A-vs-B distinction is supported by the signal peptide and absence of phosphatase motifs, though not absolutely airtight; B remains the most defensible choice given the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{"case_id":"EC_number_0157","expected_answer_check":{"judgment":"supported","reason":"The reviewer evidence (C4, C5, H2, H4) confirms that P0DXJ5 is annotated as 'Acetylajmalan esterase 2' with EC 3.1.1.80, supported by experimental evidence (ECO:0000269|PubMed:38212296, Nat. Commun. 2024). The catalytic reaction (17-O-acetylnorajmaline + H2O = norajmaline + acetate + H+) is a carboxylesterase reaction consistent with EC 3.1.1.80. The sequence matches the benchmark input exactly.","evidence_ids":["C4","C5","H2","H4"]},"answerability_check":{"judgment":"reasoning_supported","discriminating_biological_argument":"The four options span three distinct EC major classes (1=oxidoreductase, 3=hydrolase, 6=ligase) and two hydrolase subclasses (3.1.1=carboxylesterase, 3.1.3=phosphatase). Transferable reasoning: (1) Option C (1.1.1.12, alcohol dehydrogenase NADP+) requires a Rossmann-fold nucleotide-binding motif (GxGxG) and typically a zinc-binding Cys-X2-His-X3-His site; neither is present in this sequence, and the N-terminal signal peptide is atypical for cytoplasmic ADHs. (2) Option D (6.3.5.1, glutamine synthetase) requires distinctive ATP-binding motifs, a GS-like fold, and metal-coordinating residues; none are recognizable, and GS is cytoplasmic. (3) Between A (3.1.3.16, phosphatase) and B (3.1.1.80, carboxylesterase): the clear N-terminal signal peptide (MGFAARPFHIVFSLFVLAGATQALIIC) indicates a secreted/membrane-targeted protein. Plant phosphatases (EC 3.1.3.x) are overwhelmingly intracellular, whereas plant esterases involved in alkaloid/terpenoid secondary metabolism are frequently secreted or ER-localized. The ~362-aa size, hydrophobic core architecture, and absence of canonical phosphatase metal-binding motifs (DXDXD, alkaline phosphatase His/Asp clusters) further favor an α/β-hydrolase esterase over a phosphatase. While a perfect GXSXG motif is not unambiguously identifiable in this sequence, the overall domain architecture and cellular-localization logic learned from other plant secondary-metabolism esterases meaningfully favor B over A.","missing_item_specific_fact":"","reason":"A knowledgeable model can eliminate C (no Rossmann fold, no ADH motifs) and D (no GS/ligase motifs) by absence of required functional motifs. The signal-peptide-to-plant-secondary-metabolism-esterase correlation and absence of phosphatase metal-binding motifs provide a probabilistic but meaningful preference for B over A. This is a legitimate family-level and localization-pattern inference transferable from other plant esterases."},"question_ambiguity":{"multiple_defensible_options":[],"reason":"The four options span different EC major classes and subclasses. The elimination of C and D is straightforward by absence of required motifs. The A-vs-B distinction is supported by the signal peptide and absence of phosphatase motifs, though not absolutely airtight; B remains the most defensible choice given the offered alternatives."},"important_caveats":["The GXSXG catalytic motif typical of α/β-hydrolases is not unambiguously identifiable in this sequence, weakening the direct structural argument for esterase activity, though overall architecture and localization logic remain supportive.","EC 3.1.1.80 is a highly specific 4th-digit designation (acetylajmalan esterase); however, since only one 3.1.1.x option is offered, the task effectively reduces to identifying the EC class/subclass, which is more achievable through transferable reasoning.","The signal-peptide-to-secreted-plant-esterase correlation is a statistical/family-level pattern, not a universal rule; some phosphatases are secreted, and not all plant esterases are secreted."]}
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
  "requested_accession": "P0DXJ5",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "d8e428e5582a9f9deeaba106d2f89f040034c96a765f282c6106bf8a9dc8a981",
  "benchmark_sequence_length": 362,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "current_source_sequence_sha256": "d8e428e5582a9f9deeaba106d2f89f040034c96a765f282c6106bf8a9dc8a981",
  "current_source_sequence_length": 362,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 2,
  "selected_historical_version": {
    "accession": "P0DXJ5",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AAE2_RAUSE",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "selected_historical_source_sequence_sha256": "d8e428e5582a9f9deeaba106d2f89f040034c96a765f282c6106bf8a9dc8a981",
  "selected_historical_source_sequence_length": 362,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"P0DXJ5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"3.1.1.80\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Acetylajmalan esterase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsAAE2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:23797\"}}],\"reaction\":{\"ecNumber\":\"3.1.1.80\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"name\":\"17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:23796\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:77618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:77725\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3MKY2\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:22125\"}}],\"reaction\":{\"ecNumber\":\"3.1.1.80\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3MKY2\",\"source\":\"UniProtKB\"}],\"name\":\"17-O-acetylajmaline + H2O = ajmaline + acetate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:22124\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58567\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58679\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   AAE2_RAUSE              Reviewed;         362 AA.\nAC   P0DXJ5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Acetylajmalan esterase 2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsAAE2 {ECO:0000303|PubMed:38212296};\nDE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};\nDE   Flags: Precursor;\nGN   Name=AAE2 {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=Acetylajmalan esterase 2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsAAE2 {ECO:0000303|PubMed:38212296};\nDE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "source_locator": "lines 17-23",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE\nRP   SPECIFICITY, AND BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "source_locator": "lines 31-37",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=17-O-acetylnorajmaline + H2O = norajmaline + acetate + H(+);\nCC         Xref=Rhea:RHEA:23796, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30089, ChEBI:CHEBI:77618, ChEBI:CHEBI:77725; EC=3.1.1.80;\nCC         Evidence={ECO:0000269|PubMed:38212296};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23797;\nCC         Evidence={ECO:0000269|PubMed:38212296};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "evidence_id": "H5",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "source_locator": "lines 38-44",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=17-O-acetylajmaline + H2O = ajmaline + acetate + H(+);\nCC         Xref=Rhea:RHEA:22124, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:30089, ChEBI:CHEBI:58567, ChEBI:CHEBI:58679; EC=3.1.1.80;\nCC         Evidence={ECO:0000250|UniProtKB:Q3MKY2};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:22125;\nCC         Evidence={ECO:0000250|UniProtKB:Q3MKY2};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 2,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 157. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
