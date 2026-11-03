# catalytic_activity_0005: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0005.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **B** — S-ubiquitinyl-&#91;E2 ubiquitin-conjugating enzyme&#93;-L-cysteine + &#91;acceptor protein&#93;-L-lysine = &#91;E2 ubiquitin-conjugating enzyme&#93;-L-cysteine + N(6)-ubiquitinyl-&#91;acceptor protein&#93;-L-lysine.

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
MPIMLNFSNGRILPESEVEALRNVARSNQSDVLLVGSRSLRLHHISFMDGFSVEPIPGSFLDRIGERRHRRLAESLERQLNGGSSFLQAFSQYIEQTSSAPPLQESVRNEVQSRVNSYAFSVNPGDFPCSVLHLSCPITLCVPETGVFVKNARCSKVCSLYDISALTEMLRRNASHPLSREAFTPGMIVHKEECNFNTTEQHFCILPRSDTRL

[Multiple Choices]
A. (1S,3S,6S,7S,8R)-7-hydroxy-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecan-9-one + NADPH + H(+) = (1S,3S,6S,7S,8S,9S)-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecane-7,9-diol + NADP(+)
B. S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.
C. 3-methoxytyramine + S-adenosyl-L-methionine = N-methyl-3-methoxytyramine + S-adenosyl-L-homocysteine + H(+)
D. dTMP + ATP = dTDP + ADP
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

> The exact 213-aa sequence matches the UniProt entry annotated as E3 ubiquitin-protein ligase NleG8, whose catalytic-activity annotation gives choice B. The annotation cites experimental evidence (ECO:0000269, PubMed 36511702), though the primary study was not independently reviewed here.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The choices describe distinct enzyme activities, but the supplied sequence and context do not provide a clear, general biological feature that identifies this protein's specific reaction as ubiquitin transfer from E2 to a lysine acceptor.


**Missing item-specific fact**

> The protein-specific identity or functional annotation as NleG8, an E3 ubiquitin-protein ligase catalyzing the reaction in choice B.


**Reason**

> Selecting B depends on knowing or retrieving the function of this particular protein; recognizing the sequence or invoking a predictor would not constitute reasoning from information supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices specify distinct reactions, and the matched protein annotation supports B.


### Important caveats

- The UniProt annotation matches the supplied sequence and cites experimental evidence, but the primary publication was not independently validated here.
- Reviewer-only database evidence supports the key but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The choices describe distinct enzyme activities, but the supplied sequence and context do not provide a clear, general biological feature that identifies this protein's specific reaction as ubiquitin transfer from E2 to a lysine acceptor.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific identity or functional annotation as NleG8, an E3 ubiquitin-protein ligase catalyzing the reaction in choice B.",
    "reason": "Selecting B depends on knowing or retrieving the function of this particular protein; recognizing the sequence or invoking a predictor would not constitute reasoning from information supplied in the question."
  },
  "case_id": "catalytic_activity_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact 213-aa sequence matches the UniProt entry annotated as E3 ubiquitin-protein ligase NleG8, whose catalytic-activity annotation gives choice B. The annotation cites experimental evidence (ECO:0000269, PubMed 36511702), though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The UniProt annotation matches the supplied sequence and cites experimental evidence, but the primary publication was not independently validated here.",
    "Reviewer-only database evidence supports the key but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct reactions, and the matched protein annotation supports B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact 213-aa sequence matches the UniProt entry annotated as E3 ubiquitin-protein ligase NleG8, whose catalytic-activity annotation gives choice B. The annotation cites experimental evidence (ECO:0000269, PubMed 36511702), though the primary study was not independently reviewed here.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The choices describe distinct enzyme activities, but the supplied sequence and context do not provide a clear, general biological feature that identifies this protein's specific reaction as ubiquitin transfer from E2 to a lysine acceptor.",
    "missing_item_specific_fact": "The protein-specific identity or functional annotation as NleG8, an E3 ubiquitin-protein ligase catalyzing the reaction in choice B.",
    "reason": "Selecting B depends on knowing or retrieving the function of this particular protein; recognizing the sequence or invoking a predictor would not constitute reasoning from information supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices specify distinct reactions, and the matched protein annotation supports B."
  },
  "important_caveats": [
    "The UniProt annotation matches the supplied sequence and cites experimental evidence, but the primary publication was not independently validated here.",
    "Reviewer-only database evidence supports the key but was not available to the evaluated model."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence exactly matches UniProt entry A0A482PJY4 (NLEG8_CITRO, 213 aa, SHA256 match). The entry is annotated as E3 ubiquitin-protein ligase NleG8 with EC 2.3.2.27, and the catalytic activity annotation (evidence code ECO:0000269, experimental, from PubMed 36511702) states exactly the reaction in choice B: S-ubiquitinyl-&#91;E2 ubiquitin-conjugating enzyme&#93;-L-cysteine + &#91;acceptor protein&#93;-L-lysine = &#91;E2 ubiquitin-conjugating enzyme&#93;-L-cysteine + N(6)-ubiquitinyl-&#91;acceptor protein&#93;-L-lysine.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The C-terminal region contains a cysteine-rich pattern (CPITLCVPETGVFVKNARCSKVCSLYDISALTEMLRRNASHPLSREAFTPGMIVHKEECNFNTTEQHFCILPRSDTRL) that could in principle be recognized as a U-box domain fold, which is characteristic of E3 ubiquitin ligases. However, recognizing this specific cysteine arrangement as a U-box (rather than a RING or other zinc-binding motif) from a raw 213-aa bacterial sequence without organism or structural context requires specialized domain-architecture knowledge. The four choices span very different enzyme classes (oxidoreductase, ubiquitin ligase, methyltransferase, kinase), but no obvious positive or negative motifs in the sequence definitively eliminate A, C, or D through general reasoning alone.


**Missing item-specific fact**

> The specific identification of this sequence as an NleG-family U-box E3 ligase from Citrobacter rodentium, or the ability to recognize the U-box domain fold from this particular cysteine spacing pattern without prior knowledge of the NleG protein family, is not derivable from general biological reasoning applied to the bare sequence.


**Reason**

> The input provides only a 213-aa sequence with no organism, gene name, or functional context. While the four choices represent different enzyme classes, the sequence does not contain widely recognizable motifs (e.g., a canonical kinase catalytic loop, a methyltransferase Rossmann fold, or a clear NADPH-binding site) that would allow confident elimination of distractors through general reasoning. Correct identification depends on recognizing the U-box domain architecture specific to the NleG family, which is specialized structural biology knowledge rather than general biological inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent clearly distinct enzyme classes (oxidoreductase, ubiquitin ligase, methyltransferase, kinase), so they are not ambiguous with respect to each other. The question is well-formed in that only one answer is correct per the database annotation.


### Important caveats

- The UniProt annotation carries experimental evidence (ECO:0000269, PubMed 36511702), strengthening the key beyond mere computational annotation.
- The sequence is from Citrobacter rodentium (a bacterial pathogen), making the NleG effector family context important but absent from the model input.
- The reviewer-only accession (A0A482PJY4) was inferred from dataset metadata and was not available to the evaluated model.
- The U-box domain in NleG proteins is structurally validated (PDB structures exist for family members), but this structural knowledge is not provided in the question input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region contains a cysteine-rich pattern (CPITLCVPETGVFVKNARCSKVCSLYDISALTEMLRRNASHPLSREAFTPGMIVHKEECNFNTTEQHFCILPRSDTRL) that could in principle be recognized as a U-box domain fold, which is characteristic of E3 ubiquitin ligases. However, recognizing this specific cysteine arrangement as a U-box (rather than a RING or other zinc-binding motif) from a raw 213-aa bacterial sequence without organism or structural context requires specialized domain-architecture knowledge. The four choices span very different enzyme classes (oxidoreductase, ubiquitin ligase, methyltransferase, kinase), but no obvious positive or negative motifs in the sequence definitively eliminate A, C, or D through general reasoning alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific identification of this sequence as an NleG-family U-box E3 ligase from Citrobacter rodentium, or the ability to recognize the U-box domain fold from this particular cysteine spacing pattern without prior knowledge of the NleG protein family, is not derivable from general biological reasoning applied to the bare sequence.",
    "reason": "The input provides only a 213-aa sequence with no organism, gene name, or functional context. While the four choices represent different enzyme classes, the sequence does not contain widely recognizable motifs (e.g., a canonical kinase catalytic loop, a methyltransferase Rossmann fold, or a clear NADPH-binding site) that would allow confident elimination of distractors through general reasoning. Correct identification depends on recognizing the U-box domain architecture specific to the NleG family, which is specialized structural biology knowledge rather than general biological inference."
  },
  "case_id": "catalytic_activity_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry A0A482PJY4 (NLEG8_CITRO, 213 aa, SHA256 match). The entry is annotated as E3 ubiquitin-protein ligase NleG8 with EC 2.3.2.27, and the catalytic activity annotation (evidence code ECO:0000269, experimental, from PubMed 36511702) states exactly the reaction in choice B: S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269, PubMed 36511702), strengthening the key beyond mere computational annotation.",
    "The sequence is from Citrobacter rodentium (a bacterial pathogen), making the NleG effector family context important but absent from the model input.",
    "The reviewer-only accession (A0A482PJY4) was inferred from dataset metadata and was not available to the evaluated model.",
    "The U-box domain in NleG proteins is structurally validated (PDB structures exist for family members), but this structural knowledge is not provided in the question input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent clearly distinct enzyme classes (oxidoreductase, ubiquitin ligase, methyltransferase, kinase), so they are not ambiguous with respect to each other. The question is well-formed in that only one answer is correct per the database annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches UniProt entry A0A482PJY4 (NLEG8_CITRO, 213 aa, SHA256 match). The entry is annotated as E3 ubiquitin-protein ligase NleG8 with EC 2.3.2.27, and the catalytic activity annotation (evidence code ECO:0000269, experimental, from PubMed 36511702) states exactly the reaction in choice B: S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The C-terminal region contains a cysteine-rich pattern (CPITLCVPETGVFVKNARCSKVCSLYDISALTEMLRRNASHPLSREAFTPGMIVHKEECNFNTTEQHFCILPRSDTRL) that could in principle be recognized as a U-box domain fold, which is characteristic of E3 ubiquitin ligases. However, recognizing this specific cysteine arrangement as a U-box (rather than a RING or other zinc-binding motif) from a raw 213-aa bacterial sequence without organism or structural context requires specialized domain-architecture knowledge. The four choices span very different enzyme classes (oxidoreductase, ubiquitin ligase, methyltransferase, kinase), but no obvious positive or negative motifs in the sequence definitively eliminate A, C, or D through general reasoning alone.",
    "missing_item_specific_fact": "The specific identification of this sequence as an NleG-family U-box E3 ligase from Citrobacter rodentium, or the ability to recognize the U-box domain fold from this particular cysteine spacing pattern without prior knowledge of the NleG protein family, is not derivable from general biological reasoning applied to the bare sequence.",
    "reason": "The input provides only a 213-aa sequence with no organism, gene name, or functional context. While the four choices represent different enzyme classes, the sequence does not contain widely recognizable motifs (e.g., a canonical kinase catalytic loop, a methyltransferase Rossmann fold, or a clear NADPH-binding site) that would allow confident elimination of distractors through general reasoning. Correct identification depends on recognizing the U-box domain architecture specific to the NleG family, which is specialized structural biology knowledge rather than general biological inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent clearly distinct enzyme classes (oxidoreductase, ubiquitin ligase, methyltransferase, kinase), so they are not ambiguous with respect to each other. The question is well-formed in that only one answer is correct per the database annotation."
  },
  "important_caveats": [
    "The UniProt annotation carries experimental evidence (ECO:0000269, PubMed 36511702), strengthening the key beyond mere computational annotation.",
    "The sequence is from Citrobacter rodentium (a bacterial pathogen), making the NleG effector family context important but absent from the model input.",
    "The reviewer-only accession (A0A482PJY4) was inferred from dataset metadata and was not available to the evaluated model.",
    "The U-box domain in NleG proteins is structurally validated (PDB structures exist for family members), but this structural knowledge is not provided in the question input."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt records annotate the protein with EC 2.3.2.27 and the reaction in choice B. The annotation carries an experimental evidence code linked to a publication, though the underlying study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence's compact length and domain pattern can support family-level recognition as an NleG/U-box-like bacterial effector. Knowledge transferable from that family is that these proteins act as E3 ubiquitin ligases, promoting transfer of ubiquitin from an E2-linked cysteine to a lysine on an acceptor protein, matching B. This distinguishes B from the unrelated reduction, methylation, and nucleotide-phosphorylation reactions in the other choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference gives a meaningful basis for choosing B without recalling this exact protein's database annotation. The sequence does not itself make the family assignment certain, so the inference is probabilistic; the annotation provides corroboration rather than being necessary to distinguish the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices describe distinct reaction classes, and the family-level inference points specifically to the ubiquitin-transfer reaction in B.


### Important caveats

- The reviewer-only source records match the supplied sequence, but the author's exact source snapshot is unknown.
- The experimental evidence code and linked publication are reported by the database; the primary study was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's compact length and domain pattern can support family-level recognition as an NleG/U-box-like bacterial effector. Knowledge transferable from that family is that these proteins act as E3 ubiquitin ligases, promoting transfer of ubiquitin from an E2-linked cysteine to a lysine on an acceptor protein, matching B. This distinguishes B from the unrelated reduction, methylation, and nucleotide-phosphorylation reactions in the other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference gives a meaningful basis for choosing B without recalling this exact protein's database annotation. The sequence does not itself make the family assignment certain, so the inference is probabilistic; the annotation provides corroboration rather than being necessary to distinguish the offered alternatives."
  },
  "case_id": "catalytic_activity_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate the protein with EC 2.3.2.27 and the reaction in choice B. The annotation carries an experimental evidence code linked to a publication, though the underlying study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only source records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The experimental evidence code and linked publication are reported by the database; the primary study was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe distinct reaction classes, and the family-level inference points specifically to the ubiquitin-transfer reaction in B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate the protein with EC 2.3.2.27 and the reaction in choice B. The annotation carries an experimental evidence code linked to a publication, though the underlying study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence's compact length and domain pattern can support family-level recognition as an NleG/U-box-like bacterial effector. Knowledge transferable from that family is that these proteins act as E3 ubiquitin ligases, promoting transfer of ubiquitin from an E2-linked cysteine to a lysine on an acceptor protein, matching B. This distinguishes B from the unrelated reduction, methylation, and nucleotide-phosphorylation reactions in the other choices.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference gives a meaningful basis for choosing B without recalling this exact protein's database annotation. The sequence does not itself make the family assignment certain, so the inference is probabilistic; the annotation provides corroboration rather than being necessary to distinguish the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe distinct reaction classes, and the family-level inference points specifically to the ubiquitin-transfer reaction in B."
  },
  "important_caveats": [
    "The reviewer-only source records match the supplied sequence, but the author's exact source snapshot is unknown.",
    "The experimental evidence code and linked publication are reported by the database; the primary study was not independently assessed."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer-only evidence confirms the sequence (213 AA, SHA256 match) corresponds to NleG8 from Citrobacter rodentium (A0A482PJY4), annotated as E3 ubiquitin-protein ligase (EC 2.3.2.27) with experimental evidence (ECO:0000269, PubMed:36511702). The catalytic activity annotation in the source matches option B verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a cysteine-rich motif in the C-terminal region: 'PCSVLHLSCPITLCVPETGVFVKNARCSKVCSLYDIS' showing a C-x(7)-C-x(5)-C-x(5)-C pattern consistent with a RING/U-box zinc-binding domain. U-box domains are a well-characterized variant of RING finger domains found across many E3 ubiquitin ligases (e.g., TRIM proteins, U-box E3s like CHIP, and bacterial NleG-family effectors). Recognizing this zinc-binding cysteine cluster as a RING/U-box-type domain is transferable knowledge from numerous other E3 ligase families and directly points to ubiquitin-transfer activity. The distractors require entirely different structural motifs: option A (NADPH-dependent reductase) would need a Rossmann-fold or FAD/NADPH-binding motif; option C (SAM-dependent methyltransferase) would require a conserved methyltransferase fold (e.g., VLDLGCG motif); option D (nucleotide kinase) would require Walker A/B or P-loop motifs. None of these are present. The cysteine-rich zinc-binding domain is the dominant recognizable feature and uniquely aligns with E3 ubiquitin ligase function among the four choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The U-box/RING zinc-binding motif is a well-established, transferable structural feature recognized across hundreds of E3 ubiquitin ligase families. A model trained on general protein biology can identify the C-x-C-x-C-x-C pattern as a zinc-binding RING/U-box domain and associate it with E3 ubiquitin ligase activity, while simultaneously ruling out reductase, methyltransferase, and kinase activities due to absence of their characteristic motifs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The cysteine-rich zinc-binding motif uniquely points to E3 ubiquitin ligase activity. The other three options require structurally distinct catalytic domains (Rossmann fold, methyltransferase fold, kinase P-loop) that are absent from this sequence. No alternative is defensible.


### Important caveats

- The cysteine spacing in this sequence (C-x7-C-x5-C-x5-C) is somewhat compressed compared to canonical RING domains but is consistent with U-box domain variants found in NleG-family bacterial effectors.
- The evidence for the expected answer is experimental (ECO:0000269, PubMed:36511702), not merely computational annotation.
- The U-box/RING recognition argument is probabilistic and pattern-based; it does not constitute a rigorous proof of catalytic mechanism from sequence alone, but it meaningfully distinguishes the correct choice from the offered alternatives.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a cysteine-rich motif in the C-terminal region: 'PCSVLHLSCPITLCVPETGVFVKNARCSKVCSLYDIS' showing a C-x(7)-C-x(5)-C-x(5)-C pattern consistent with a RING/U-box zinc-binding domain. U-box domains are a well-characterized variant of RING finger domains found across many E3 ubiquitin ligases (e.g., TRIM proteins, U-box E3s like CHIP, and bacterial NleG-family effectors). Recognizing this zinc-binding cysteine cluster as a RING/U-box-type domain is transferable knowledge from numerous other E3 ligase families and directly points to ubiquitin-transfer activity. The distractors require entirely different structural motifs: option A (NADPH-dependent reductase) would need a Rossmann-fold or FAD/NADPH-binding motif; option C (SAM-dependent methyltransferase) would require a conserved methyltransferase fold (e.g., VLDLGCG motif); option D (nucleotide kinase) would require Walker A/B or P-loop motifs. None of these are present. The cysteine-rich zinc-binding domain is the dominant recognizable feature and uniquely aligns with E3 ubiquitin ligase function among the four choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The U-box/RING zinc-binding motif is a well-established, transferable structural feature recognized across hundreds of E3 ubiquitin ligase families. A model trained on general protein biology can identify the C-x-C-x-C-x-C pattern as a zinc-binding RING/U-box domain and associate it with E3 ubiquitin ligase activity, while simultaneously ruling out reductase, methyltransferase, and kinase activities due to absence of their characteristic motifs."
  },
  "case_id": "catalytic_activity_0005",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer-only evidence confirms the sequence (213 AA, SHA256 match) corresponds to NleG8 from Citrobacter rodentium (A0A482PJY4), annotated as E3 ubiquitin-protein ligase (EC 2.3.2.27) with experimental evidence (ECO:0000269, PubMed:36511702). The catalytic activity annotation in the source matches option B verbatim."
  },
  "important_caveats": [
    "The cysteine spacing in this sequence (C-x7-C-x5-C-x5-C) is somewhat compressed compared to canonical RING domains but is consistent with U-box domain variants found in NleG-family bacterial effectors.",
    "The evidence for the expected answer is experimental (ECO:0000269, PubMed:36511702), not merely computational annotation.",
    "The U-box/RING recognition argument is probabilistic and pattern-based; it does not constitute a rigorous proof of catalytic mechanism from sequence alone, but it meaningfully distinguishes the correct choice from the offered alternatives."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cysteine-rich zinc-binding motif uniquely points to E3 ubiquitin ligase activity. The other three options require structurally distinct catalytic domains (Rossmann fold, methyltransferase fold, kinase P-loop) that are absent from this sequence. No alternative is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0005",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer-only evidence confirms the sequence (213 AA, SHA256 match) corresponds to NleG8 from Citrobacter rodentium (A0A482PJY4), annotated as E3 ubiquitin-protein ligase (EC 2.3.2.27) with experimental evidence (ECO:0000269, PubMed:36511702). The catalytic activity annotation in the source matches option B verbatim.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a cysteine-rich motif in the C-terminal region: 'PCSVLHLSCPITLCVPETGVFVKNARCSKVCSLYDIS' showing a C-x(7)-C-x(5)-C-x(5)-C pattern consistent with a RING/U-box zinc-binding domain. U-box domains are a well-characterized variant of RING finger domains found across many E3 ubiquitin ligases (e.g., TRIM proteins, U-box E3s like CHIP, and bacterial NleG-family effectors). Recognizing this zinc-binding cysteine cluster as a RING/U-box-type domain is transferable knowledge from numerous other E3 ligase families and directly points to ubiquitin-transfer activity. The distractors require entirely different structural motifs: option A (NADPH-dependent reductase) would need a Rossmann-fold or FAD/NADPH-binding motif; option C (SAM-dependent methyltransferase) would require a conserved methyltransferase fold (e.g., VLDLGCG motif); option D (nucleotide kinase) would require Walker A/B or P-loop motifs. None of these are present. The cysteine-rich zinc-binding domain is the dominant recognizable feature and uniquely aligns with E3 ubiquitin ligase function among the four choices.",
    "missing_item_specific_fact": "",
    "reason": "The U-box/RING zinc-binding motif is a well-established, transferable structural feature recognized across hundreds of E3 ubiquitin ligase families. A model trained on general protein biology can identify the C-x-C-x-C-x-C pattern as a zinc-binding RING/U-box domain and associate it with E3 ubiquitin ligase activity, while simultaneously ruling out reductase, methyltransferase, and kinase activities due to absence of their characteristic motifs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The cysteine-rich zinc-binding motif uniquely points to E3 ubiquitin ligase activity. The other three options require structurally distinct catalytic domains (Rossmann fold, methyltransferase fold, kinase P-loop) that are absent from this sequence. No alternative is defensible."
  },
  "important_caveats": [
    "The cysteine spacing in this sequence (C-x7-C-x5-C-x5-C) is somewhat compressed compared to canonical RING domains but is consistent with U-box domain variants found in NleG-family bacterial effectors.",
    "The evidence for the expected answer is experimental (ECO:0000269, PubMed:36511702), not merely computational annotation.",
    "The U-box/RING recognition argument is probabilistic and pattern-based; it does not constitute a rigorous proof of catalytic mechanism from sequence alone, but it meaningfully distinguishes the correct choice from the offered alternatives."
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
  "requested_accession": "A0A482PJY4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "16612f731de98766170a931a61e51f7339aa7a0030ef42fd419a95fcd5450328",
  "benchmark_sequence_length": 213,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 13,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "current_source_sequence_sha256": "16612f731de98766170a931a61e51f7339aa7a0030ef42fd419a95fcd5450328",
  "current_source_sequence_length": 213,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 12,
  "selected_historical_version": {
    "accession": "A0A482PJY4",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "NLEG8_CITRO",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "2f8dd60cce61af465e470b41f23916871a38e1f05591e27b38d55d36f789fe0f",
  "selected_historical_source_sequence_sha256": "16612f731de98766170a931a61e51f7339aa7a0030ef42fd419a95fcd5450328",
  "selected_historical_source_sequence_length": 213,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJY4.json",
  "source_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "retrieved_utc": "2026-11-02T04:25:20.391051+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A482PJY4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJY4.json",
  "source_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "retrieved_utc": "2026-11-02T04:25:20.391051+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":13,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJY4.json",
  "source_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "retrieved_utc": "2026-11-02T04:25:20.391051+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Citrobacter\"],\"scientificName\":\"Citrobacter rodentium\",\"taxonId\":67825}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJY4.json",
  "source_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "retrieved_utc": "2026-11-02T04:25:20.391051+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36511702\",\"source\":\"PubMed\"}],\"value\":\"2.3.2.27\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"E3 ubiquitin-protein ligase NleG8\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJY4.json",
  "source_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "retrieved_utc": "2026-11-02T04:25:20.391051+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.2.27\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36511702\",\"source\":\"PubMed\"}],\"name\":\"S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A482PJY4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A482PJY4.json",
  "source_sha256": "b176c5d7843bb2158bb3c5a2a514a885071317c4b9557576ac536b564e4dd58b",
  "retrieved_utc": "2026-11-02T04:25:20.391051+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Popov G.\",\"Fiebig-Comyn A.\",\"Syriste L.\",\"Little D.J.\",\"Skarina T.\",\"Stogios P.J.\",\"Birstonas S.\",\"Coombes B.K.\",\"Savchenko A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36511702\"},{\"database\":\"DOI\",\"id\":\"10.1128/iai.00505-22\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0050522\",\"id\":\"36511702\",\"journal\":\"Infect. Immun.\",\"lastPage\":\"e0050522\",\"publicationDate\":\"2023\",\"title\":\"Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for Different Roles during Citrobacter rodentium Infection in Mice.\",\"volume\":\"91\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DBS100\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"SUBUNIT\",\"INTERACTION WITH HOST GOPC\",\"SUBCELLULAR LOCATION\",\"INDUCTION\",\"DOMAIN\",\"DISRUPTION PHENOTYPE\",\"MOTIF\",\"MUTAGENESIS OF ILE-138 AND 210-ASP--LEU-213\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12",
  "source_sha256": "2f8dd60cce61af465e470b41f23916871a38e1f05591e27b38d55d36f789fe0f",
  "retrieved_utc": "2026-11-02T04:25:23.897522+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   NLEG8_CITRO             Reviewed;         213 AA.\nAC   A0A482PJY4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=E3 ubiquitin-protein ligase NleG8 {ECO:0000305};\nDE            EC=2.3.2.27 {ECO:0000269|PubMed:36511702};\nGN   Name=nleG8 {ECO:0000303|PubMed:36511702};\nGN   ORFNames=E2R62_17250 {ECO:0000312|EMBL:QBY30403.1};\nOS   Citrobacter rodentium.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Citrobacter.\nOX   NCBI_TaxID=67825;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12",
  "source_sha256": "2f8dd60cce61af465e470b41f23916871a38e1f05591e27b38d55d36f789fe0f",
  "retrieved_utc": "2026-11-02T04:25:23.897522+00:00",
  "source_locator": "lines 6-7",
  "excerpt": "DE   RecName: Full=E3 ubiquitin-protein ligase NleG8 {ECO:0000305};\nDE            EC=2.3.2.27 {ECO:0000269|PubMed:36511702};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12",
  "source_sha256": "2f8dd60cce61af465e470b41f23916871a38e1f05591e27b38d55d36f789fe0f",
  "retrieved_utc": "2026-11-02T04:25:23.897522+00:00",
  "source_locator": "lines 21-31",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, SUBUNIT, INTERACTION WITH HOST GOPC,\nRP   SUBCELLULAR LOCATION, INDUCTION, DOMAIN, DISRUPTION PHENOTYPE, MOTIF, AND\nRP   MUTAGENESIS OF ILE-138 AND 210-ASP--LEU-213.\nRC   STRAIN=DBS100;\nRX   PubMed=36511702; DOI=10.1128/iai.00505-22;\nRA   Popov G., Fiebig-Comyn A., Syriste L., Little D.J., Skarina T.,\nRA   Stogios P.J., Birstonas S., Coombes B.K., Savchenko A.;\nRT   \"Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for\nRT   Different Roles during Citrobacter rodentium Infection in Mice.\";\nRL   Infect. Immun. 91:e0050522-e0050522(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A482PJY4?format=txt&versions=12",
  "source_sha256": "2f8dd60cce61af465e470b41f23916871a38e1f05591e27b38d55d36f789fe0f",
  "retrieved_utc": "2026-11-02T04:25:23.897522+00:00",
  "source_locator": "lines 47-51",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine +\nCC         [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-\nCC         cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.;\nCC         EC=2.3.2.27; Evidence={ECO:0000269|PubMed:36511702};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 12,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 5. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
