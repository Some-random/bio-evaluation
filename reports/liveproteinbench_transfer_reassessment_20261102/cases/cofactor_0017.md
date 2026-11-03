# cofactor_0017: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/cofactor_0017.txt)

**Task:** `cofactor`  
**Author key, unchanged:** **A** — FAD

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
MTKIAEKSKQEYGDLLKEKDHLQDMEQLEMTIVSIQTPYPSIVRIQGKINTLQPELWQAPNLAIRLIVSNPPEGQPISRVYTVRSFNPINAQIEIDFVKHEDLSPAMEWLNSAQVGTKIGLIGPRPHFIPNFTAKKHVVMFADDTAVPALYSILKQWELGISADIFIESFEKDIASQLPELEHVKIHSFHKEHHTSQKGLLLKAAFALEHYENITIWAACERNEARALRQFFLEDQQLNKNDVRIAGYWRDGVSSSELDKLRAQHYQEHIQQGKTLNEYDDLDLAN

[Multiple Choices]
A. FAD
B. [2Fe-2S] cluster
C. Fe cation
D. Na(+)
```

<details>
<summary>Complete original system instructions</summary>

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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches the historical UniProt record for ferric acinetobactin reductase, which annotates FAD as its cofactor with experimental evidence. The cited structural study also reports the protein crystallized in complex with FAD. This supports choice A, while noting the primary study was not independently reviewed here.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence and choices provide no unambiguous basis for identifying the required cofactor. The protein-specific functional or cofactor annotation is needed to distinguish FAD from the alternatives.


**Missing item-specific fact**

> That this exact protein is ferric acinetobactin reductase and uses FAD as a cofactor.


**Reason**

> The reviewer evidence supports the key, but that evidence was not supplied to the evaluated model. Inferring a precise cofactor from this sequence alone would require protein-specific knowledge or external annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The evidence supports FAD as the cofactor; the other choices are not supported as required cofactors for this protein.


### Important caveats

- The sequence matches both current and historical UniProt records, including a record available by the approximate benchmark cutoff.
- The cofactor annotation cites experimental evidence and a structure in complex with FAD, but the cited primary paper was not independently validated here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence and choices provide no unambiguous basis for identifying the required cofactor. The protein-specific functional or cofactor annotation is needed to distinguish FAD from the alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this exact protein is ferric acinetobactin reductase and uses FAD as a cofactor.",
    "reason": "The reviewer evidence supports the key, but that evidence was not supplied to the evaluated model. Inferring a precise cofactor from this sequence alone would require protein-specific knowledge or external annotation."
  },
  "case_id": "cofactor_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the historical UniProt record for ferric acinetobactin reductase, which annotates FAD as its cofactor with experimental evidence. The cited structural study also reports the protein crystallized in complex with FAD. This supports choice A, while noting the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence matches both current and historical UniProt records, including a record available by the approximate benchmark cutoff.",
    "The cofactor annotation cites experimental evidence and a structure in complex with FAD, but the cited primary paper was not independently validated here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports FAD as the cofactor; the other choices are not supported as required cofactors for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the historical UniProt record for ferric acinetobactin reductase, which annotates FAD as its cofactor with experimental evidence. The cited structural study also reports the protein crystallized in complex with FAD. This supports choice A, while noting the primary study was not independently reviewed here.",
    "evidence_ids": ["H3", "H4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence and choices provide no unambiguous basis for identifying the required cofactor. The protein-specific functional or cofactor annotation is needed to distinguish FAD from the alternatives.",
    "missing_item_specific_fact": "That this exact protein is ferric acinetobactin reductase and uses FAD as a cofactor.",
    "reason": "The reviewer evidence supports the key, but that evidence was not supplied to the evaluated model. Inferring a precise cofactor from this sequence alone would require protein-specific knowledge or external annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The evidence supports FAD as the cofactor; the other choices are not supported as required cofactors for this protein."
  },
  "important_caveats": [
    "The sequence matches both current and historical UniProt records, including a record available by the approximate benchmark cutoff.",
    "The cofactor annotation cites experimental evidence and a structure in complex with FAD, but the cited primary paper was not independently validated here."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A1E3M8P2 (Ferric acinetobactin reductase / Flavin-dependent SIP from Acinetobacter baumannii) explicitly annotates FAD as the cofactor with experimental evidence code ECO:0000269|PubMed:34308084. This is corroborated by X-ray crystallography at 2.85 Å in complex with FAD (PDB: 7LRN). The protein's alternative name literally includes 'Flavin-dependent.' The sequence matches the benchmark sequence exactly (SHA-256 confirmed). Both current and historical (entry v35) annotations agree.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence provides a concrete, multi-step elimination pathway. (1) Na+ (D) is eliminated because sodium ions serve structural or transport roles, not as catalytic electron-transfer cofactors in reductase enzymes. (2) Fe cation (C) is eliminated because in a ferric reductase, iron(III) is the substrate being reduced; the enzyme's own electron-transfer cofactor is distinct from the substrate. (3) The decisive discriminator between &#91;2Fe-2S&#93; (B) and FAD (A): a &#91;2Fe-2S&#93; cluster requires four cysteine ligands (or 2 Cys + 2 His) at defined spacings (e.g., CxxC…CxxC). The 286-residue sequence contains only two cysteines, which are adjacent ('AACER' near residue 247-248), making &#91;2Fe-2S&#93; coordination essentially impossible. FAD, a flavin electron-transfer cofactor, does not require cysteine ligation and is the dominant cofactor in small bacterial reductases of this size. The glycine-rich stretches (e.g., 'GKINTL', 'GPRPHFIPNF') and aromatic residues are broadly consistent with a flavin-binding environment, though no canonical GxGxxG Rossmann motif is perfectly present.


**Missing item-specific fact**

> None critical. The cysteine-count argument and standard biochemistry of reductase cofactors provide sufficient grounds. A model would not need to recognize the exact SIP family or the specific UniProt annotation to arrive at FAD by elimination.


**Reason**

> The sequence itself contains the key discriminating feature (near-absence of cysteines ruling out &#91;2Fe-2S&#93;), and general biochemistry eliminates Na+ and Fe cation. The positive identification of FAD is supported by the overall architecture being consistent with a small flavoprotein reductase, even without a textbook-perfect Rossmann motif. This constitutes a defensible reasoning chain from sequence features and general biological knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated by the elimination logic. Na+ and Fe cation are eliminated by standard biochemistry of reductases. &#91;2Fe-2S&#93; is eliminated by the cysteine-count argument. FAD remains as the only viable electron-transfer cofactor for a ~286-residue reductase with only two adjacent cysteines. No other option is defensible.


### Important caveats

- The sequence lacks a canonical GxGxxG Rossmann motif, so positive FAD identification relies more on elimination of alternatives than on a clear positive binding-site signature. The reasoning is primarily subtractive.
- The protein belongs to the siderophore-interacting protein (SIP) family, which is known in the literature to be flavoproteins. A model with family-level knowledge would recognize this, but the cysteine argument provides an independent, sequence-based path.
- The FAD annotation is experimentally supported (X-ray crystallography, PDB 7LRN), not merely computational inference.
- The benchmark sequence matches the UniProt entry exactly (SHA-256 confirmed for both current and historical v35 records).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence provides a concrete, multi-step elimination pathway. (1) Na+ (D) is eliminated because sodium ions serve structural or transport roles, not as catalytic electron-transfer cofactors in reductase enzymes. (2) Fe cation (C) is eliminated because in a ferric reductase, iron(III) is the substrate being reduced; the enzyme's own electron-transfer cofactor is distinct from the substrate. (3) The decisive discriminator between [2Fe-2S] (B) and FAD (A): a [2Fe-2S] cluster requires four cysteine ligands (or 2 Cys + 2 His) at defined spacings (e.g., CxxC…CxxC). The 286-residue sequence contains only two cysteines, which are adjacent ('AACER' near residue 247-248), making [2Fe-2S] coordination essentially impossible. FAD, a flavin electron-transfer cofactor, does not require cysteine ligation and is the dominant cofactor in small bacterial reductases of this size. The glycine-rich stretches (e.g., 'GKINTL', 'GPRPHFIPNF') and aromatic residues are broadly consistent with a flavin-binding environment, though no canonical GxGxxG Rossmann motif is perfectly present.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. The cysteine-count argument and standard biochemistry of reductase cofactors provide sufficient grounds. A model would not need to recognize the exact SIP family or the specific UniProt annotation to arrive at FAD by elimination.",
    "reason": "The sequence itself contains the key discriminating feature (near-absence of cysteines ruling out [2Fe-2S]), and general biochemistry eliminates Na+ and Fe cation. The positive identification of FAD is supported by the overall architecture being consistent with a small flavoprotein reductase, even without a textbook-perfect Rossmann motif. This constitutes a defensible reasoning chain from sequence features and general biological knowledge."
  },
  "case_id": "cofactor_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A1E3M8P2 (Ferric acinetobactin reductase / Flavin-dependent SIP from Acinetobacter baumannii) explicitly annotates FAD as the cofactor with experimental evidence code ECO:0000269|PubMed:34308084. This is corroborated by X-ray crystallography at 2.85 Å in complex with FAD (PDB: 7LRN). The protein's alternative name literally includes 'Flavin-dependent.' The sequence matches the benchmark sequence exactly (SHA-256 confirmed). Both current and historical (entry v35) annotations agree."
  },
  "important_caveats": [
    "The sequence lacks a canonical GxGxxG Rossmann motif, so positive FAD identification relies more on elimination of alternatives than on a clear positive binding-site signature. The reasoning is primarily subtractive.",
    "The protein belongs to the siderophore-interacting protein (SIP) family, which is known in the literature to be flavoproteins. A model with family-level knowledge would recognize this, but the cysteine argument provides an independent, sequence-based path.",
    "The FAD annotation is experimentally supported (X-ray crystallography, PDB 7LRN), not merely computational inference.",
    "The benchmark sequence matches the UniProt entry exactly (SHA-256 confirmed for both current and historical v35 records)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by the elimination logic. Na+ and Fe cation are eliminated by standard biochemistry of reductases. [2Fe-2S] is eliminated by the cysteine-count argument. FAD remains as the only viable electron-transfer cofactor for a ~286-residue reductase with only two adjacent cysteines. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A1E3M8P2 (Ferric acinetobactin reductase / Flavin-dependent SIP from Acinetobacter baumannii) explicitly annotates FAD as the cofactor with experimental evidence code ECO:0000269|PubMed:34308084. This is corroborated by X-ray crystallography at 2.85 Å in complex with FAD (PDB: 7LRN). The protein's alternative name literally includes 'Flavin-dependent.' The sequence matches the benchmark sequence exactly (SHA-256 confirmed). Both current and historical (entry v35) annotations agree.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence provides a concrete, multi-step elimination pathway. (1) Na+ (D) is eliminated because sodium ions serve structural or transport roles, not as catalytic electron-transfer cofactors in reductase enzymes. (2) Fe cation (C) is eliminated because in a ferric reductase, iron(III) is the substrate being reduced; the enzyme's own electron-transfer cofactor is distinct from the substrate. (3) The decisive discriminator between [2Fe-2S] (B) and FAD (A): a [2Fe-2S] cluster requires four cysteine ligands (or 2 Cys + 2 His) at defined spacings (e.g., CxxC…CxxC). The 286-residue sequence contains only two cysteines, which are adjacent ('AACER' near residue 247-248), making [2Fe-2S] coordination essentially impossible. FAD, a flavin electron-transfer cofactor, does not require cysteine ligation and is the dominant cofactor in small bacterial reductases of this size. The glycine-rich stretches (e.g., 'GKINTL', 'GPRPHFIPNF') and aromatic residues are broadly consistent with a flavin-binding environment, though no canonical GxGxxG Rossmann motif is perfectly present.",
    "missing_item_specific_fact": "None critical. The cysteine-count argument and standard biochemistry of reductase cofactors provide sufficient grounds. A model would not need to recognize the exact SIP family or the specific UniProt annotation to arrive at FAD by elimination.",
    "reason": "The sequence itself contains the key discriminating feature (near-absence of cysteines ruling out [2Fe-2S]), and general biochemistry eliminates Na+ and Fe cation. The positive identification of FAD is supported by the overall architecture being consistent with a small flavoprotein reductase, even without a textbook-perfect Rossmann motif. This constitutes a defensible reasoning chain from sequence features and general biological knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by the elimination logic. Na+ and Fe cation are eliminated by standard biochemistry of reductases. [2Fe-2S] is eliminated by the cysteine-count argument. FAD remains as the only viable electron-transfer cofactor for a ~286-residue reductase with only two adjacent cysteines. No other option is defensible."
  },
  "important_caveats": [
    "The sequence lacks a canonical GxGxxG Rossmann motif, so positive FAD identification relies more on elimination of alternatives than on a clear positive binding-site signature. The reasoning is primarily subtractive.",
    "The protein belongs to the siderophore-interacting protein (SIP) family, which is known in the literature to be flavoproteins. A model with family-level knowledge would recognize this, but the cysteine argument provides an independent, sequence-based path.",
    "The FAD annotation is experimentally supported (X-ray crystallography, PDB 7LRN), not merely computational inference.",
    "The benchmark sequence matches the UniProt entry exactly (SHA-256 confirmed for both current and historical v35 records)."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates FAD as the cofactor with experimental evidence; the cited structure was also determined in complex with FAD. This supports choice A for the supplied sequence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a compact soluble oxidoreductase, and its glycine-rich segment (GTKIGLIG) is a plausible nucleotide/flavin-binding feature. Transferable knowledge of flavin-dependent oxidoreductases makes FAD a meaningful choice over the alternatives; the sequence has no conspicuous cysteine-rich motif supporting an iron-sulfur cluster, and sodium is not a usual catalytic cofactor for this kind of soluble enzyme.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> These sequence and family-level clues provide a probabilistic basis for distinguishing FAD among the offered choices, although they do not establish the exact cofactor experimentally.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence supports FAD as the most defensible offered choice; no alternative is comparably supported.


### Important caveats

- The reviewer-only evidence supports the key but was not available as input to the evaluated model.
- The sequence-based cofactor inference is probabilistic; the source record provides the target-specific experimental support.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a compact soluble oxidoreductase, and its glycine-rich segment (GTKIGLIG) is a plausible nucleotide/flavin-binding feature. Transferable knowledge of flavin-dependent oxidoreductases makes FAD a meaningful choice over the alternatives; the sequence has no conspicuous cysteine-rich motif supporting an iron-sulfur cluster, and sodium is not a usual catalytic cofactor for this kind of soluble enzyme.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "These sequence and family-level clues provide a probabilistic basis for distinguishing FAD among the offered choices, although they do not establish the exact cofactor experimentally."
  },
  "case_id": "cofactor_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates FAD as the cofactor with experimental evidence; the cited structure was also determined in complex with FAD. This supports choice A for the supplied sequence."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key but was not available as input to the evaluated model.",
    "The sequence-based cofactor inference is probabilistic; the source record provides the target-specific experimental support."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence supports FAD as the most defensible offered choice; no alternative is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates FAD as the cofactor with experimental evidence; the cited structure was also determined in complex with FAD. This supports choice A for the supplied sequence.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a compact soluble oxidoreductase, and its glycine-rich segment (GTKIGLIG) is a plausible nucleotide/flavin-binding feature. Transferable knowledge of flavin-dependent oxidoreductases makes FAD a meaningful choice over the alternatives; the sequence has no conspicuous cysteine-rich motif supporting an iron-sulfur cluster, and sodium is not a usual catalytic cofactor for this kind of soluble enzyme.",
    "missing_item_specific_fact": "",
    "reason": "These sequence and family-level clues provide a probabilistic basis for distinguishing FAD among the offered choices, although they do not establish the exact cofactor experimentally."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence supports FAD as the most defensible offered choice; no alternative is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key but was not available as input to the evaluated model.",
    "The sequence-based cofactor inference is probabilistic; the source record provides the target-specific experimental support."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A1E3M8P2) explicitly annotates FAD as the cofactor with direct experimental evidence (ECO:0000269, PubMed:34308084). The X-ray crystallography structure (PDB 7LRN) confirms the protein in complex with FAD. The protein is named 'Flavin-dependent siderophore-interacting protein' and the alternative name explicitly includes 'Flavin-dependent SIP.' The EC number 1.16.1.10 (ferric reductase) is consistent with FAD-dependent electron transfer.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple transferable arguments distinguish FAD from the other choices. (1) Process of elimination: &#91;2Fe-2S&#93; clusters require Cys-rich motifs (e.g., CxxCxxC...C patterns typical of ferredoxins); this 286-AA sequence lacks such Cys clusters. Fe cation cofactors typically involve His/Asp/Glu triads or tetrad clusters; no obvious canonical iron-binding motif is present. Na(+) is an extraordinarily rare catalytic cofactor and is essentially never the primary cofactor for an oxidoreductase. (2) Family-level knowledge: The sequence length (~286 AA), bacterial origin, and overall hydrophobic-core composition are consistent with the siderophore-interacting protein (SIP) family, which is a well-characterized class of FAD-dependent flavoproteins in microbiology literature. SIPs (e.g., IsdG-like proteins, BauF homologs) universally use FAD for ferric-reductase electron transfer. (3) The presence of a degenerate Rossmann-like motif (e.g., 'GKINTL' near position 30, 'GTKIGL' near position 120) is consistent with flavin-binding folds found in many FAD-dependent oxidoreductases. Together, these arguments meaningfully favor FAD over the three distractors.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question can be answered by combining process-of-elimination reasoning (absence of Cys clusters, absence of metal-binding motifs, implausibility of Na+) with family-level knowledge that SIPs are FAD-dependent flavoproteins. The sequence features (size, hydrophobic composition, degenerate Rossmann-like motifs) are consistent with FAD-dependent oxidoreductases broadly, and the SIP family association is well-established transferable knowledge from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The distractors are clearly eliminable: &#91;2Fe-2S&#93; requires Cys-rich motifs absent here; Fe cation lacks a matching binding motif; Na(+) is not a plausible catalytic cofactor for a reductase. FAD is the only biochemically reasonable choice.


### Important caveats

- The Rossmann-like motifs in this sequence are degenerate and not canonical GxGxxG; family-level SIP knowledge strengthens the FAD assignment beyond what sequence motifs alone provide.
- The reviewer-only evidence confirms FAD experimentally (X-ray crystallography, PDB 7LRN), but this was not available to the evaluated model.
- The SIP family is well-known in microbiology, but a model without specific exposure to SIP literature would rely more heavily on the elimination argument.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple transferable arguments distinguish FAD from the other choices. (1) Process of elimination: [2Fe-2S] clusters require Cys-rich motifs (e.g., CxxCxxC...C patterns typical of ferredoxins); this 286-AA sequence lacks such Cys clusters. Fe cation cofactors typically involve His/Asp/Glu triads or tetrad clusters; no obvious canonical iron-binding motif is present. Na(+) is an extraordinarily rare catalytic cofactor and is essentially never the primary cofactor for an oxidoreductase. (2) Family-level knowledge: The sequence length (~286 AA), bacterial origin, and overall hydrophobic-core composition are consistent with the siderophore-interacting protein (SIP) family, which is a well-characterized class of FAD-dependent flavoproteins in microbiology literature. SIPs (e.g., IsdG-like proteins, BauF homologs) universally use FAD for ferric-reductase electron transfer. (3) The presence of a degenerate Rossmann-like motif (e.g., 'GKINTL' near position 30, 'GTKIGL' near position 120) is consistent with flavin-binding folds found in many FAD-dependent oxidoreductases. Together, these arguments meaningfully favor FAD over the three distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question can be answered by combining process-of-elimination reasoning (absence of Cys clusters, absence of metal-binding motifs, implausibility of Na+) with family-level knowledge that SIPs are FAD-dependent flavoproteins. The sequence features (size, hydrophobic composition, degenerate Rossmann-like motifs) are consistent with FAD-dependent oxidoreductases broadly, and the SIP family association is well-established transferable knowledge from other proteins."
  },
  "case_id": "cofactor_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A1E3M8P2) explicitly annotates FAD as the cofactor with direct experimental evidence (ECO:0000269, PubMed:34308084). The X-ray crystallography structure (PDB 7LRN) confirms the protein in complex with FAD. The protein is named 'Flavin-dependent siderophore-interacting protein' and the alternative name explicitly includes 'Flavin-dependent SIP.' The EC number 1.16.1.10 (ferric reductase) is consistent with FAD-dependent electron transfer."
  },
  "important_caveats": [
    "The Rossmann-like motifs in this sequence are degenerate and not canonical GxGxxG; family-level SIP knowledge strengthens the FAD assignment beyond what sequence motifs alone provide.",
    "The reviewer-only evidence confirms FAD experimentally (X-ray crystallography, PDB 7LRN), but this was not available to the evaluated model.",
    "The SIP family is well-known in microbiology, but a model without specific exposure to SIP literature would rely more heavily on the elimination argument."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors are clearly eliminable: [2Fe-2S] requires Cys-rich motifs absent here; Fe cation lacks a matching binding motif; Na(+) is not a plausible catalytic cofactor for a reductase. FAD is the only biochemically reasonable choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A1E3M8P2) explicitly annotates FAD as the cofactor with direct experimental evidence (ECO:0000269, PubMed:34308084). The X-ray crystallography structure (PDB 7LRN) confirms the protein in complex with FAD. The protein is named 'Flavin-dependent siderophore-interacting protein' and the alternative name explicitly includes 'Flavin-dependent SIP.' The EC number 1.16.1.10 (ferric reductase) is consistent with FAD-dependent electron transfer.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple transferable arguments distinguish FAD from the other choices. (1) Process of elimination: [2Fe-2S] clusters require Cys-rich motifs (e.g., CxxCxxC...C patterns typical of ferredoxins); this 286-AA sequence lacks such Cys clusters. Fe cation cofactors typically involve His/Asp/Glu triads or tetrad clusters; no obvious canonical iron-binding motif is present. Na(+) is an extraordinarily rare catalytic cofactor and is essentially never the primary cofactor for an oxidoreductase. (2) Family-level knowledge: The sequence length (~286 AA), bacterial origin, and overall hydrophobic-core composition are consistent with the siderophore-interacting protein (SIP) family, which is a well-characterized class of FAD-dependent flavoproteins in microbiology literature. SIPs (e.g., IsdG-like proteins, BauF homologs) universally use FAD for ferric-reductase electron transfer. (3) The presence of a degenerate Rossmann-like motif (e.g., 'GKINTL' near position 30, 'GTKIGL' near position 120) is consistent with flavin-binding folds found in many FAD-dependent oxidoreductases. Together, these arguments meaningfully favor FAD over the three distractors.",
    "missing_item_specific_fact": "",
    "reason": "The question can be answered by combining process-of-elimination reasoning (absence of Cys clusters, absence of metal-binding motifs, implausibility of Na+) with family-level knowledge that SIPs are FAD-dependent flavoproteins. The sequence features (size, hydrophobic composition, degenerate Rossmann-like motifs) are consistent with FAD-dependent oxidoreductases broadly, and the SIP family association is well-established transferable knowledge from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors are clearly eliminable: [2Fe-2S] requires Cys-rich motifs absent here; Fe cation lacks a matching binding motif; Na(+) is not a plausible catalytic cofactor for a reductase. FAD is the only biochemically reasonable choice."
  },
  "important_caveats": [
    "The Rossmann-like motifs in this sequence are degenerate and not canonical GxGxxG; family-level SIP knowledge strengthens the FAD assignment beyond what sequence motifs alone provide.",
    "The reviewer-only evidence confirms FAD experimentally (X-ray crystallography, PDB 7LRN), but this was not available to the evaluated model.",
    "The SIP family is well-known in microbiology, but a model without specific exposure to SIP literature would rely more heavily on the elimination argument."
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
  "requested_accession": "A0A1E3M8P2",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "69db519277a1b220b6f5ad165e8b2558cee0754be3f6745d9bf8c017a90dd9e3",
  "benchmark_sequence_length": 286,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 37,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-01-18",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "current_source_sequence_sha256": "69db519277a1b220b6f5ad165e8b2558cee0754be3f6745d9bf8c017a90dd9e3",
  "current_source_sequence_length": 286,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 35,
  "selected_historical_version": {
    "accession": "A0A1E3M8P2",
    "database": "Swiss-Prot",
    "entryVersion": 35,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BAUF_ACIBA",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746",
  "selected_historical_source_sequence_sha256": "69db519277a1b220b6f5ad165e8b2558cee0754be3f6745d9bf8c017a90dd9e3",
  "selected_historical_source_sequence_length": 286,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 35,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json",
  "source_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "retrieved_utc": "2026-11-02T04:24:33.445950+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A1E3M8P2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json",
  "source_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "retrieved_utc": "2026-11-02T04:24:33.445950+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":37,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-01-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json",
  "source_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "retrieved_utc": "2026-11-02T04:24:33.445950+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Moraxellales\",\"Moraxellaceae\",\"Acinetobacter\",\"Acinetobacter calcoaceticus/baumannii complex\"],\"scientificName\":\"Acinetobacter baumannii\",\"taxonId\":470}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json",
  "source_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "retrieved_utc": "2026-11-02T04:24:33.445950+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34308084\",\"source\":\"PubMed\"}],\"value\":\"Flavin-dependent siderophore-interacting protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34308084\",\"source\":\"PubMed\"}],\"value\":\"Flavin-dependent SIP\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34308084\",\"source\":\"PubMed\"}],\"value\":\"1.16.1.10\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Ferric acinetobactin reductase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json",
  "source_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "retrieved_utc": "2026-11-02T04:24:33.445950+00:00",
  "json_pointer": "/comments/3",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34308084\",\"source\":\"PubMed\"}],\"name\":\"FAD\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json",
  "source_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "retrieved_utc": "2026-11-02T04:24:33.445950+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Valentino H.\",\"Korasick D.A.\",\"Bohac T.J.\",\"Shapiro J.A.\",\"Wencewicz T.A.\",\"Tanner J.J.\",\"Sobrado P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34308084\"},{\"database\":\"DOI\",\"id\":\"10.1021/acsomega.1c03047\"}],\"citationType\":\"journal article\",\"firstPage\":\"18537\",\"id\":\"34308084\",\"journal\":\"ACS Omega\",\"lastPage\":\"18547\",\"publicationDate\":\"2021\",\"title\":\"Structural and Biochemical Characterization of the Flavin-Dependent Siderophore-Interacting Protein from Acinetobacter baumannii.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7LRN\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 17978 / DSM 105126 / CIP 53.77 / LMG 1025 / NCDC KC755 / 5377\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.85 ANGSTROMS) IN COMPLEX WITH FAD\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35",
  "source_sha256": "21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746",
  "retrieved_utc": "2026-11-02T04:24:37.007835+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   BAUF_ACIBA              Reviewed;         286 AA.\nAC   A0A1E3M8P2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JAN-2017, sequence version 1.\nDT   28-JAN-2026, entry version 35.\nDE   RecName: Full=Ferric acinetobactin reductase {ECO:0000305};\nDE            EC=1.16.1.10 {ECO:0000269|PubMed:34308084};\nDE   AltName: Full=Flavin-dependent siderophore-interacting protein {ECO:0000303|PubMed:34308084};\nDE            Short=Flavin-dependent SIP {ECO:0000303|PubMed:34308084};\nGN   Name=bauF {ECO:0000303|PubMed:34308084};\nGN   ORFNames=AUO97_00860 {ECO:0000312|EMBL:APP29445.1};\nOS   Acinetobacter baumannii.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Moraxellales; Moraxellaceae; Acinetobacter;\nOC   Acinetobacter calcoaceticus/baumannii complex.\nOX   NCBI_TaxID=470;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 35,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35",
  "source_sha256": "21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746",
  "retrieved_utc": "2026-11-02T04:24:37.007835+00:00",
  "source_locator": "lines 6-9",
  "excerpt": "DE   RecName: Full=Ferric acinetobactin reductase {ECO:0000305};\nDE            EC=1.16.1.10 {ECO:0000269|PubMed:34308084};\nDE   AltName: Full=Flavin-dependent siderophore-interacting protein {ECO:0000303|PubMed:34308084};\nDE            Short=Flavin-dependent SIP {ECO:0000303|PubMed:34308084};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 35,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35",
  "source_sha256": "21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746",
  "retrieved_utc": "2026-11-02T04:24:37.007835+00:00",
  "source_locator": "lines 22-31",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7LRN}\nRP   X-RAY CRYSTALLOGRAPHY (2.85 ANGSTROMS) IN COMPLEX WITH FAD, FUNCTION,\nRP   CATALYTIC ACTIVITY, AND COFACTOR.\nRC   STRAIN=ATCC 17978 / DSM 105126 / CIP 53.77 / LMG 1025 / NCDC KC755 / 5377;\nRX   PubMed=34308084; DOI=10.1021/acsomega.1c03047;\nRA   Valentino H., Korasick D.A., Bohac T.J., Shapiro J.A., Wencewicz T.A.,\nRA   Tanner J.J., Sobrado P.;\nRT   \"Structural and Biochemical Characterization of the Flavin-Dependent\nRT   Siderophore-Interacting Protein from Acinetobacter baumannii.\";\nRL   ACS Omega 6:18537-18547(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 35,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35",
  "source_sha256": "21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746",
  "retrieved_utc": "2026-11-02T04:24:37.007835+00:00",
  "source_locator": "lines 59-61",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FAD; Xref=ChEBI:CHEBI:57692;\nCC         Evidence={ECO:0000269|PubMed:34308084};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 35,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
