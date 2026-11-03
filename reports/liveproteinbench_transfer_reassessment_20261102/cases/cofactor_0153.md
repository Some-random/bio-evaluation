# cofactor_0153: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/cofactor_0153.txt)

**Task:** `cofactor`  
**Author key, unchanged:** **D** — NAD(+)

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
MFMREIELKGHIIDSFILAKVFDRTLELGGDYKVLEFDIGKKKIDTSYAKLLISGDTQQHLDQILEELQNVGANIPEIENANLKPALKDSVLPDGFYSTTNHPTHVKVNDEWIEVANPKMDAVIVVYPEEKRAETKVIRKVKKGDFVLIGHNGIRVMPPEKSREAGQLFEFMNSEVSSEKPKEAIIKRIAKEMHEIREEYKKTGTGGIAIVGGPAIIHTGGGPALAKMVELGYIQAILAGNALATHDIESALYGTSLGVNIKTAKPVTGGHKHHIYAINAINDAGNIKNAVESGVLKEGIMYQCIKNNIPYVLAGSIRDDGPIPDVITDSMVAQDKMRTTVMDKKMVIMLSTLLHSVATGNLMPSYIKTVCVDIQPSTVTKLMDRGTSQAIGVVTDVGVFLVLLLKELERLELQE

[Multiple Choices]
A. Co(2+)
B. [2Fe-2S] cluster
C. heme b
D. NAD(+)
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

> The supplied sequence exactly matches the UniProt entry annotated as ornithine cyclodeaminase, and that entry lists NAD(+) as a cofactor. However, the cofactor annotation is transferred by similarity from Q8YMD9 (ECO:0000250), not shown here as a direct experimental measurement on this exact protein.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a soluble enzyme, but its motifs do not uniquely establish NAD(+) rather than the other listed cofactors. Excluding an obvious membrane or iron-sulfur signature would not distinguish NAD(+) from Co(2+).


**Missing item-specific fact**

> The identity of this sequence as ornithine cyclodeaminase and the enzyme-specific NAD(+) cofactor assignment are not provided in the question.


**Reason**

> Selecting NAD(+) requires identifying the protein or knowing its specific cofactor annotation; generic sequence inspection does not meaningfully resolve the remaining choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The available sequence-specific annotation supports NAD(+), though the cited cofactor evidence is transferred from a homolog rather than directly established here.


### Important caveats

- The reviewer-only accession and annotations were not supplied to the evaluated model.
- The sequence match is exact, but the cited cofactor evidence is similarity-based; the excerpts do not independently verify NAD(+) experimentally for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a soluble enzyme, but its motifs do not uniquely establish NAD(+) rather than the other listed cofactors. Excluding an obvious membrane or iron-sulfur signature would not distinguish NAD(+) from Co(2+).",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The identity of this sequence as ornithine cyclodeaminase and the enzyme-specific NAD(+) cofactor assignment are not provided in the question.",
    "reason": "Selecting NAD(+) requires identifying the protein or knowing its specific cofactor annotation; generic sequence inspection does not meaningfully resolve the remaining choices."
  },
  "case_id": "cofactor_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as ornithine cyclodeaminase, and that entry lists NAD(+) as a cofactor. However, the cofactor annotation is transferred by similarity from Q8YMD9 (ECO:0000250), not shown here as a direct experimental measurement on this exact protein."
  },
  "important_caveats": [
    "The reviewer-only accession and annotations were not supplied to the evaluated model.",
    "The sequence match is exact, but the cited cofactor evidence is similarity-based; the excerpts do not independently verify NAD(+) experimentally for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available sequence-specific annotation supports NAD(+), though the cited cofactor evidence is transferred from a homolog rather than directly established here."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the UniProt entry annotated as ornithine cyclodeaminase, and that entry lists NAD(+) as a cofactor. However, the cofactor annotation is transferred by similarity from Q8YMD9 (ECO:0000250), not shown here as a direct experimental measurement on this exact protein.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a soluble enzyme, but its motifs do not uniquely establish NAD(+) rather than the other listed cofactors. Excluding an obvious membrane or iron-sulfur signature would not distinguish NAD(+) from Co(2+).",
    "missing_item_specific_fact": "The identity of this sequence as ornithine cyclodeaminase and the enzyme-specific NAD(+) cofactor assignment are not provided in the question.",
    "reason": "Selecting NAD(+) requires identifying the protein or knowing its specific cofactor annotation; generic sequence inspection does not meaningfully resolve the remaining choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available sequence-specific annotation supports NAD(+), though the cited cofactor evidence is transferred from a homolog rather than directly established here."
  },
  "important_caveats": [
    "The reviewer-only accession and annotations were not supplied to the evaluated model.",
    "The sequence match is exact, but the cited cofactor evidence is similarity-based; the excerpts do not independently verify NAD(+) experimentally for this exact protein."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt annotates this protein (Q6LXX7, ornithine cyclodeaminase, EC 4.3.1.12, Methanococcus maripaludis) with cofactor NAD(+) (CHEBI:57540). The evidence code is ECO:0000250 (inferred by similarity to Q8YMD9, the well-characterized E. coli OCD), but the biochemistry of ornithine cyclodeaminase is universally NAD+-dependent across all characterized organisms. The EC number 4.3.1.12 is itself defined as an NAD+-requiring reaction (L-ornithine → L-proline + NH3). The answer is strongly supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable Rossmann-fold dinucleotide-binding motif in the region 'GGPAIIHTGGGPALAK' (the GGxGxxG / GxGxxG pattern characteristic of NAD+/NADP+ binding). This motif is absent from proteins requiring Co2+, &#91;2Fe-2S&#93; clusters, or heme b. Furthermore, the sequence lacks the Cys-rich clusters typical of &#91;2Fe-2S&#93; coordination, the proximal/distal His pairs or Cys-His motifs for heme b ligation, and the specific tetrahedral His/Cys/Asp arrangements for Co2+ sites. A model applying general knowledge of Rossmann-fold cofactor specificity (predominantly NAD+/NADP+) can reason toward NAD+ without memorizing this specific entry.


**Missing item-specific fact**

> None strictly required; however, recognizing the protein as ornithine cyclodeaminase (EC 4.3.1.12) would make the answer trivially obvious, and the Rossmann motif in this particular sequence is somewhat degenerate compared to textbook GxGxxG examples.


**Reason**

> The Rossmann-fold motif is identifiable at the sequence level and constitutes a concrete, general biological argument linking the protein to dinucleotide (NAD+) binding rather than to metal ions, iron-sulfur clusters, or porphyrins. This is general biochemistry knowledge, not an item-specific lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent structurally and mechanistically distinct cofactor classes (metal ion, iron-sulfur cluster, porphyrin, dinucleotide). The presence of a Rossmann-fold motif and the absence of metal/heme/Fe-S coordination motifs cleanly discriminate NAD+ from the other three options.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity to Q8YMD9), not direct experimental evidence on this specific archaeal protein. However, the NAD+ dependence of EC 4.3.1.12 is textbook biochemistry.
- The Rossmann-fold motif in this sequence is somewhat degenerate (GGP…GGP rather than a canonical GxGxxG); a model relying solely on motif regex might miss it, though structural and functional reasoning still applies.
- The accession Q6LXX7 and its annotations were not available to the evaluated model; they are reviewer-only context.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable Rossmann-fold dinucleotide-binding motif in the region 'GGPAIIHTGGGPALAK' (the GGxGxxG / GxGxxG pattern characteristic of NAD+/NADP+ binding). This motif is absent from proteins requiring Co2+, [2Fe-2S] clusters, or heme b. Furthermore, the sequence lacks the Cys-rich clusters typical of [2Fe-2S] coordination, the proximal/distal His pairs or Cys-His motifs for heme b ligation, and the specific tetrahedral His/Cys/Asp arrangements for Co2+ sites. A model applying general knowledge of Rossmann-fold cofactor specificity (predominantly NAD+/NADP+) can reason toward NAD+ without memorizing this specific entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None strictly required; however, recognizing the protein as ornithine cyclodeaminase (EC 4.3.1.12) would make the answer trivially obvious, and the Rossmann motif in this particular sequence is somewhat degenerate compared to textbook GxGxxG examples.",
    "reason": "The Rossmann-fold motif is identifiable at the sequence level and constitutes a concrete, general biological argument linking the protein to dinucleotide (NAD+) binding rather than to metal ions, iron-sulfur clusters, or porphyrins. This is general biochemistry knowledge, not an item-specific lookup."
  },
  "case_id": "cofactor_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt annotates this protein (Q6LXX7, ornithine cyclodeaminase, EC 4.3.1.12, Methanococcus maripaludis) with cofactor NAD(+) (CHEBI:57540). The evidence code is ECO:0000250 (inferred by similarity to Q8YMD9, the well-characterized E. coli OCD), but the biochemistry of ornithine cyclodeaminase is universally NAD+-dependent across all characterized organisms. The EC number 4.3.1.12 is itself defined as an NAD+-requiring reaction (L-ornithine → L-proline + NH3). The answer is strongly supported."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity to Q8YMD9), not direct experimental evidence on this specific archaeal protein. However, the NAD+ dependence of EC 4.3.1.12 is textbook biochemistry.",
    "The Rossmann-fold motif in this sequence is somewhat degenerate (GGP…GGP rather than a canonical GxGxxG); a model relying solely on motif regex might miss it, though structural and functional reasoning still applies.",
    "The accession Q6LXX7 and its annotations were not available to the evaluated model; they are reviewer-only context."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent structurally and mechanistically distinct cofactor classes (metal ion, iron-sulfur cluster, porphyrin, dinucleotide). The presence of a Rossmann-fold motif and the absence of metal/heme/Fe-S coordination motifs cleanly discriminate NAD+ from the other three options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt annotates this protein (Q6LXX7, ornithine cyclodeaminase, EC 4.3.1.12, Methanococcus maripaludis) with cofactor NAD(+) (CHEBI:57540). The evidence code is ECO:0000250 (inferred by similarity to Q8YMD9, the well-characterized E. coli OCD), but the biochemistry of ornithine cyclodeaminase is universally NAD+-dependent across all characterized organisms. The EC number 4.3.1.12 is itself defined as an NAD+-requiring reaction (L-ornithine → L-proline + NH3). The answer is strongly supported.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable Rossmann-fold dinucleotide-binding motif in the region 'GGPAIIHTGGGPALAK' (the GGxGxxG / GxGxxG pattern characteristic of NAD+/NADP+ binding). This motif is absent from proteins requiring Co2+, [2Fe-2S] clusters, or heme b. Furthermore, the sequence lacks the Cys-rich clusters typical of [2Fe-2S] coordination, the proximal/distal His pairs or Cys-His motifs for heme b ligation, and the specific tetrahedral His/Cys/Asp arrangements for Co2+ sites. A model applying general knowledge of Rossmann-fold cofactor specificity (predominantly NAD+/NADP+) can reason toward NAD+ without memorizing this specific entry.",
    "missing_item_specific_fact": "None strictly required; however, recognizing the protein as ornithine cyclodeaminase (EC 4.3.1.12) would make the answer trivially obvious, and the Rossmann motif in this particular sequence is somewhat degenerate compared to textbook GxGxxG examples.",
    "reason": "The Rossmann-fold motif is identifiable at the sequence level and constitutes a concrete, general biological argument linking the protein to dinucleotide (NAD+) binding rather than to metal ions, iron-sulfur clusters, or porphyrins. This is general biochemistry knowledge, not an item-specific lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent structurally and mechanistically distinct cofactor classes (metal ion, iron-sulfur cluster, porphyrin, dinucleotide). The presence of a Rossmann-fold motif and the absence of metal/heme/Fe-S coordination motifs cleanly discriminate NAD+ from the other three options."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000250 (inferred by similarity to Q8YMD9), not direct experimental evidence on this specific archaeal protein. However, the NAD+ dependence of EC 4.3.1.12 is textbook biochemistry.",
    "The Rossmann-fold motif in this sequence is somewhat degenerate (GGP…GGP rather than a canonical GxGxxG); a model relying solely on motif regex might miss it, though structural and functional reasoning still applies.",
    "The accession Q6LXX7 and its annotations were not available to the evaluated model; they are reviewer-only context."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates NAD(+) as the cofactor, but the evidence is transferred from another UniProt entry (ECO:0000250), not direct experimental evidence for this exact protein. This supports the key while leaving that qualification.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a glycine-rich region around “TGTGGIAIVGGPA,” consistent with a dinucleotide-binding fold, and the sequence is compatible with the ornithine-cyclodeaminase family, whose transferable cofactor knowledge supports NAD(+). Among these choices, that points to D rather than a metal, iron-sulfur cluster, or heme cofactor.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A nucleotide-binding sequence pattern and family-level knowledge provide a meaningful basis to distinguish NAD(+) from the offered alternatives without knowing this protein’s recorded annotation. The sequence pattern alone is not definitive, and the source annotation itself is similarity-transferred.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice has comparable support as the cofactor.


### Important caveats

- The reviewer-only record matches the supplied sequence.
- The cited cofactor evidence is transferred by similarity; it does not establish direct experimental verification for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a glycine-rich region around “TGTGGIAIVGGPA,” consistent with a dinucleotide-binding fold, and the sequence is compatible with the ornithine-cyclodeaminase family, whose transferable cofactor knowledge supports NAD(+). Among these choices, that points to D rather than a metal, iron-sulfur cluster, or heme cofactor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A nucleotide-binding sequence pattern and family-level knowledge provide a meaningful basis to distinguish NAD(+) from the offered alternatives without knowing this protein’s recorded annotation. The sequence pattern alone is not definitive, and the source annotation itself is similarity-transferred."
  },
  "case_id": "cofactor_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates NAD(+) as the cofactor, but the evidence is transferred from another UniProt entry (ECO:0000250), not direct experimental evidence for this exact protein. This supports the key while leaving that qualification."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence.",
    "The cited cofactor evidence is transferred by similarity; it does not establish direct experimental verification for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice has comparable support as the cofactor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates NAD(+) as the cofactor, but the evidence is transferred from another UniProt entry (ECO:0000250), not direct experimental evidence for this exact protein. This supports the key while leaving that qualification.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a glycine-rich region around “TGTGGIAIVGGPA,” consistent with a dinucleotide-binding fold, and the sequence is compatible with the ornithine-cyclodeaminase family, whose transferable cofactor knowledge supports NAD(+). Among these choices, that points to D rather than a metal, iron-sulfur cluster, or heme cofactor.",
    "missing_item_specific_fact": "",
    "reason": "A nucleotide-binding sequence pattern and family-level knowledge provide a meaningful basis to distinguish NAD(+) from the offered alternatives without knowing this protein’s recorded annotation. The sequence pattern alone is not definitive, and the source annotation itself is similarity-transferred."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice has comparable support as the cofactor."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence.",
    "The cited cofactor evidence is transferred by similarity; it does not establish direct experimental verification for this exact protein."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q6LXX7 (exact sequence match) annotates the cofactor as NAD(+) (CHEBI:57540) with evidence code ECO:0000250 (inferred by similarity from Q8YMD9, the well-characterized bacterial ornithine cyclodeaminase). The protein is annotated as Ornithine cyclodeaminase (EC 4.3.1.12, experimentally supported by ECO:0000269/PubMed:30636068). The OCD family's NAD(+) dependence is well-established from the extensively studied bacterial enzyme. The cofactor assignment for this specific archaeal protein is by similarity rather than direct experiment, but it is consistent with the family-level biochemistry and the EC number assignment.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable Rossmann-fold-like NAD(P)-binding motif: 'GGPAIIHTGGGPALAK' within a hydrophobic stretch, which is characteristic of the GxGxxG-type dinucleotide-binding domain found in NAD-dependent enzymes. Ornithine cyclodeaminase (EC 4.3.1.12) is a well-studied family (bacterial OCD from Pseudomonas putida is the paradigm) that uses NAD(+) as a catalytic cofactor via a Rossmann-fold domain; the sequence's overall architecture and these GG-motif features are consistent with this family. The alternatives can be meaningfully excluded: (A) Co(2+) (cobalamin) enzymes have distinct RxxHx cobalamin-binding motifs absent here; (B) &#91;2Fe-2S&#93; clusters require Cys-rich motifs (CxxCxxC patterns) not present in this sequence; (C) heme b binding requires specific His/Cys residues in defined structural contexts not evident here. The combination of Rossmann-fold sequence features and OCD-family homology (learned from bacterial homologs) provides a concrete, transferable inference favoring NAD(+).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the Rossmann-fold GG motifs in the sequence, associate them with NAD(P)-binding domains, and use family-level knowledge of ornithine cyclodeaminase (well-characterized in bacteria) to identify NAD(+) as the cofactor. The three distractors lack their characteristic sequence signatures in this protein, allowing meaningful elimination.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Rossmann-fold motifs and OCD-family context point specifically to NAD(+). The other three cofactors (Co2+/cobalamin, &#91;2Fe-2S&#93;, heme b) require distinctive sequence features (cobalamin-binding motifs, Cys-rich cluster motifs, heme-ligating residues in specific geometry) that are absent from this sequence. No genuine ambiguity exists among the offered choices.


### Important caveats

- The cofactor annotation for this specific archaeal protein carries evidence code ECO:0000250 (inferred by similarity from Q8YMD9), not direct experimental measurement on this enzyme. However, the EC assignment (4.3.1.12) is experimentally supported (ECO:0000269), and the OCD family's NAD(+) dependence is well-established.
- The sequence-match to UniProt Q6LXX7 is exact (SHA256 confirmed), confirming the protein identity.
- The Rossmann-fold motif in this sequence ('GGPAIIHTGGGPALAK') is somewhat degenerate compared to the canonical GxGxxG consensus, but it falls within the range of NAD-binding motifs observed in the OCD/glutamate-synthase superfamily.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable Rossmann-fold-like NAD(P)-binding motif: 'GGPAIIHTGGGPALAK' within a hydrophobic stretch, which is characteristic of the GxGxxG-type dinucleotide-binding domain found in NAD-dependent enzymes. Ornithine cyclodeaminase (EC 4.3.1.12) is a well-studied family (bacterial OCD from Pseudomonas putida is the paradigm) that uses NAD(+) as a catalytic cofactor via a Rossmann-fold domain; the sequence's overall architecture and these GG-motif features are consistent with this family. The alternatives can be meaningfully excluded: (A) Co(2+) (cobalamin) enzymes have distinct RxxHx cobalamin-binding motifs absent here; (B) [2Fe-2S] clusters require Cys-rich motifs (CxxCxxC patterns) not present in this sequence; (C) heme b binding requires specific His/Cys residues in defined structural contexts not evident here. The combination of Rossmann-fold sequence features and OCD-family homology (learned from bacterial homologs) provides a concrete, transferable inference favoring NAD(+).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the Rossmann-fold GG motifs in the sequence, associate them with NAD(P)-binding domains, and use family-level knowledge of ornithine cyclodeaminase (well-characterized in bacteria) to identify NAD(+) as the cofactor. The three distractors lack their characteristic sequence signatures in this protein, allowing meaningful elimination."
  },
  "case_id": "cofactor_0153",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q6LXX7 (exact sequence match) annotates the cofactor as NAD(+) (CHEBI:57540) with evidence code ECO:0000250 (inferred by similarity from Q8YMD9, the well-characterized bacterial ornithine cyclodeaminase). The protein is annotated as Ornithine cyclodeaminase (EC 4.3.1.12, experimentally supported by ECO:0000269/PubMed:30636068). The OCD family's NAD(+) dependence is well-established from the extensively studied bacterial enzyme. The cofactor assignment for this specific archaeal protein is by similarity rather than direct experiment, but it is consistent with the family-level biochemistry and the EC number assignment."
  },
  "important_caveats": [
    "The cofactor annotation for this specific archaeal protein carries evidence code ECO:0000250 (inferred by similarity from Q8YMD9), not direct experimental measurement on this enzyme. However, the EC assignment (4.3.1.12) is experimentally supported (ECO:0000269), and the OCD family's NAD(+) dependence is well-established.",
    "The sequence-match to UniProt Q6LXX7 is exact (SHA256 confirmed), confirming the protein identity.",
    "The Rossmann-fold motif in this sequence ('GGPAIIHTGGGPALAK') is somewhat degenerate compared to the canonical GxGxxG consensus, but it falls within the range of NAD-binding motifs observed in the OCD/glutamate-synthase superfamily."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann-fold motifs and OCD-family context point specifically to NAD(+). The other three cofactors (Co2+/cobalamin, [2Fe-2S], heme b) require distinctive sequence features (cobalamin-binding motifs, Cys-rich cluster motifs, heme-ligating residues in specific geometry) that are absent from this sequence. No genuine ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0153",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q6LXX7 (exact sequence match) annotates the cofactor as NAD(+) (CHEBI:57540) with evidence code ECO:0000250 (inferred by similarity from Q8YMD9, the well-characterized bacterial ornithine cyclodeaminase). The protein is annotated as Ornithine cyclodeaminase (EC 4.3.1.12, experimentally supported by ECO:0000269/PubMed:30636068). The OCD family's NAD(+) dependence is well-established from the extensively studied bacterial enzyme. The cofactor assignment for this specific archaeal protein is by similarity rather than direct experiment, but it is consistent with the family-level biochemistry and the EC number assignment.",
    "evidence_ids": ["C5", "H4", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable Rossmann-fold-like NAD(P)-binding motif: 'GGPAIIHTGGGPALAK' within a hydrophobic stretch, which is characteristic of the GxGxxG-type dinucleotide-binding domain found in NAD-dependent enzymes. Ornithine cyclodeaminase (EC 4.3.1.12) is a well-studied family (bacterial OCD from Pseudomonas putida is the paradigm) that uses NAD(+) as a catalytic cofactor via a Rossmann-fold domain; the sequence's overall architecture and these GG-motif features are consistent with this family. The alternatives can be meaningfully excluded: (A) Co(2+) (cobalamin) enzymes have distinct RxxHx cobalamin-binding motifs absent here; (B) [2Fe-2S] clusters require Cys-rich motifs (CxxCxxC patterns) not present in this sequence; (C) heme b binding requires specific His/Cys residues in defined structural contexts not evident here. The combination of Rossmann-fold sequence features and OCD-family homology (learned from bacterial homologs) provides a concrete, transferable inference favoring NAD(+).",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the Rossmann-fold GG motifs in the sequence, associate them with NAD(P)-binding domains, and use family-level knowledge of ornithine cyclodeaminase (well-characterized in bacteria) to identify NAD(+) as the cofactor. The three distractors lack their characteristic sequence signatures in this protein, allowing meaningful elimination."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann-fold motifs and OCD-family context point specifically to NAD(+). The other three cofactors (Co2+/cobalamin, [2Fe-2S], heme b) require distinctive sequence features (cobalamin-binding motifs, Cys-rich cluster motifs, heme-ligating residues in specific geometry) that are absent from this sequence. No genuine ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The cofactor annotation for this specific archaeal protein carries evidence code ECO:0000250 (inferred by similarity from Q8YMD9), not direct experimental measurement on this enzyme. However, the EC assignment (4.3.1.12) is experimentally supported (ECO:0000269), and the OCD family's NAD(+) dependence is well-established.",
    "The sequence-match to UniProt Q6LXX7 is exact (SHA256 confirmed), confirming the protein identity.",
    "The Rossmann-fold motif in this sequence ('GGPAIIHTGGGPALAK') is somewhat degenerate compared to the canonical GxGxxG consensus, but it falls within the range of NAD-binding motifs observed in the OCD/glutamate-synthase superfamily."
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
  "requested_accession": "Q6LXX7",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "355b4d824ba114e0b6eb06dbc86bbba020b6e400b3af07fafa23ce7ab0b5684b",
  "benchmark_sequence_length": 415,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 102,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-07-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "current_source_sequence_sha256": "355b4d824ba114e0b6eb06dbc86bbba020b6e400b3af07fafa23ce7ab0b5684b",
  "current_source_sequence_length": 415,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 100,
  "selected_historical_version": {
    "accession": "Q6LXX7",
    "database": "Swiss-Prot",
    "entryVersion": 100,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AOCD_METMP",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "selected_historical_source_sequence_sha256": "355b4d824ba114e0b6eb06dbc86bbba020b6e400b3af07fafa23ce7ab0b5684b",
  "selected_historical_source_sequence_length": 415,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 100,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"Q6LXX7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":102,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Archaea\",\"Methanobacteriati\",\"Methanobacteriota\",\"Methanomada group\",\"Methanococci\",\"Methanococcales\",\"Methanococcaceae\",\"Methanococcus\"],\"scientificName\":\"Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL)\",\"taxonId\":267377}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30636068\",\"source\":\"PubMed\"}],\"value\":\"Archaeal ornithine cyclodeaminase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30636068\",\"source\":\"PubMed\"}],\"value\":\"Mls2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30636068\",\"source\":\"PubMed\"}],\"value\":\"4.3.1.12\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30636068\",\"source\":\"PubMed\"}],\"value\":\"Ornithine cyclodeaminase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"OCD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8YMD9\",\"source\":\"UniProtKB\"}],\"name\":\"NAD(+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q6LXX7.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/Q6LXX7.json",
  "source_sha256": "3e88c87b8e607d8f9da2f5b9ef0b835869c5da2ca430a53bbee11e2710822d63",
  "retrieved_utc": "2026-11-02T04:31:35.053650+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Burnat M.\",\"Picossi S.\",\"Valladares A.\",\"Herrero A.\",\"Flores E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30636068\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.14203\"}],\"citationType\":\"journal article\",\"firstPage\":\"883\",\"id\":\"30636068\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"897\",\"publicationDate\":\"2019\",\"title\":\"Catabolic pathway of arginine in Anabaena involves a novel bifunctional enzyme that produces proline from arginine.\",\"volume\":\"111\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100",
  "source_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "retrieved_utc": "2026-11-02T04:31:37.153182+00:00",
  "source_locator": "lines 1-16",
  "excerpt": "ID   AOCD_METMP              Reviewed;         415 AA.\nAC   Q6LXX7;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2004, sequence version 1.\nDT   28-JAN-2026, entry version 100.\nDE   RecName: Full=Ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};\nDE            Short=OCD {ECO:0000305};\nDE            EC=4.3.1.12 {ECO:0000269|PubMed:30636068};\nDE   AltName: Full=Archaeal ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};\nDE   AltName: Full=Mls2 {ECO:0000303|PubMed:30636068};\nGN   OrderedLocusNames=MMP1218 {ECO:0000312|EMBL:CAF30774.1};\nOS   Methanococcus maripaludis (strain DSM 14266 / JCM 13030 / NBRC 101832 / S2\nOS   / LL).\nOC   Archaea; Methanobacteriati; Methanobacteriota; Methanomada group;\nOC   Methanococci; Methanococcales; Methanococcaceae; Methanococcus.\nOX   NCBI_TaxID=267377;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100",
  "source_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "retrieved_utc": "2026-11-02T04:31:37.153182+00:00",
  "source_locator": "lines 6-10",
  "excerpt": "DE   RecName: Full=Ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};\nDE            Short=OCD {ECO:0000305};\nDE            EC=4.3.1.12 {ECO:0000269|PubMed:30636068};\nDE   AltName: Full=Archaeal ornithine cyclodeaminase {ECO:0000303|PubMed:30636068};\nDE   AltName: Full=Mls2 {ECO:0000303|PubMed:30636068};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100",
  "source_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "retrieved_utc": "2026-11-02T04:31:37.153182+00:00",
  "source_locator": "lines 30-37",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=DSM 14266 / JCM 13030 / NBRC 101832 / S2 / LL;\nRX   PubMed=30636068; DOI=10.1111/mmi.14203;\nRA   Burnat M., Picossi S., Valladares A., Herrero A., Flores E.;\nRT   \"Catabolic pathway of arginine in Anabaena involves a novel bifunctional\nRT   enzyme that produces proline from arginine.\";\nRL   Mol. Microbiol. 111:883-897(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/Q6LXX7?format=txt&versions=100",
  "source_sha256": "fb75c52fd5da78db70bc1f15507ff585eec805f8d1c74be8d2e60b19ae2897fb",
  "retrieved_utc": "2026-11-02T04:31:37.153182+00:00",
  "source_locator": "lines 50-52",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=NAD(+); Xref=ChEBI:CHEBI:57540;\nCC         Evidence={ECO:0000250|UniProtKB:Q8YMD9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 100,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 153. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
