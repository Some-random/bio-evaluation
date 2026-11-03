# cofactor_0043: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/cofactor_0043.txt)

**Task:** `cofactor`  
**Author key, unchanged:** **C** — pantetheine 4&#x27;-phosphate

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
MPSHTFNPQAGYDLAVDRNLGLGEIFYNRAQKSHQAIAVCDGGAVLTYGQLHAKAYRLAQELSQWLRLTEKPVGIVVQHGMADVVAQMAVIYAGGSCAPMDPTLPDNQIQGRLKRLDAVCVLTDQANRHRDLGADVLCIDDFDIADLAPEDTLYPVATNLEHCAYLIHTSGTTAEPKAVQIAARSILHVAFYAPLEPVYDTDVVAHANNSSFDVSLFDIWVPLLRGAQIAVINKAVLLDPPMMAREIDRLGITVMATTTAVLNLAAFIYPKAFAKLRLVTIGGEAANVAAIRIILKNGPPAMLFNAYGPTECCVFCLAHQITPADVEHGSIGVSIGKPVGRTITYIAGDEGGESDQGELWIGGPGVSPGYFRQPEKNLAAFSDLGEAMTSLENPVRFYRTGDIVRRRPNGALEYVGRRDHQVKVRGFRIELEAVEAGLLKTGLFSDAVAMRIEMPQNGAGSILAAYVVPTDVSKPPTMDEALESAKSILPHYMVPQLELVPRLPLNRHLKVDRKQLAELFGRRWEDVSPAQPENASQDVRSALVSLWATVLASPLSTYGDDDDFLHLGGTSLQAAMLINQIRHKFDIEVSLLTLYDNTTLGALTSIIKQRLSGQSETLHNEKDSWVADSEIADDLSCPLDRPIDWCRDTEGRVFLTGGTGFVGAFLLADLLHMPQTSQVRCLVRATDAAVGQERLRAALDKYGLWEDGFADKLVAIAGLLEDDYLGMGREQFEEAASWASVVFHLGARVNYAQPYSLHRASNTLGTRNMVRFACAGRTKAIHYVSSIGCFGPTGSILGTTSVREDEPLLPHITALPYDHGYAQSQWVADALLRRLMDRGFPIAIYRPGFIVGHSQTGACNPDDFLSRLIDACREIGCYPQLPNQRKEFVPVDYVNAAILHIAASPASLGHAYHIVPPTRAVSIDMDNSMALVDRAGNSPMRPVSYKEWVERLAATSPKRLLPLQPMLAERVKDGLTRWELYENMPVYETTNTARALQNYPGGLQFPVLDTSLMKRYLDFLEAKG

[Multiple Choices]
A. Mg(2+)
B. NAD(+)
C. pantetheine 4'-phosphate
D. Fe(2+)
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

> The exact sequence matches a UniProt entry annotated with pantetheine 4'-phosphate as a cofactor. The annotation is computational, based on a PROSITE-ProRule, rather than direct experimental evidence in the supplied excerpts.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide clear, readily interpretable evidence that distinguishes pantetheine 4'-phosphate from the other listed cofactors; doing so requires identifying its specific protein function or domain features.


**Missing item-specific fact**

> The sequence's association with FrzA and the annotation of a phosphopantetheine-bearing carrier-protein feature are not stated in the question.


**Reason**

> The correct choice is supported by a sequence-matched protein annotation, but the input supplies no functional or domain context that makes this specific cofactor inferable by general biological reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The available evidence specifically supports choice C; it does not establish another listed option as an alternative answer.


### Important caveats

- The cofactor annotation is computational (PROSITE-ProRule), not direct experimental confirmation in the supplied evidence.
- The sequence match is exact in both the current and archived UniProt records; the record's cofactor annotation should not be mistaken for information supplied to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide clear, readily interpretable evidence that distinguishes pantetheine 4'-phosphate from the other listed cofactors; doing so requires identifying its specific protein function or domain features.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence's association with FrzA and the annotation of a phosphopantetheine-bearing carrier-protein feature are not stated in the question.",
    "reason": "The correct choice is supported by a sequence-matched protein annotation, but the input supplies no functional or domain context that makes this specific cofactor inferable by general biological reasoning."
  },
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with pantetheine 4'-phosphate as a cofactor. The annotation is computational, based on a PROSITE-ProRule, rather than direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The cofactor annotation is computational (PROSITE-ProRule), not direct experimental confirmation in the supplied evidence.",
    "The sequence match is exact in both the current and archived UniProt records; the record's cofactor annotation should not be mistaken for information supplied to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available evidence specifically supports choice C; it does not establish another listed option as an alternative answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated with pantetheine 4'-phosphate as a cofactor. The annotation is computational, based on a PROSITE-ProRule, rather than direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C1", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide clear, readily interpretable evidence that distinguishes pantetheine 4'-phosphate from the other listed cofactors; doing so requires identifying its specific protein function or domain features.",
    "missing_item_specific_fact": "The sequence's association with FrzA and the annotation of a phosphopantetheine-bearing carrier-protein feature are not stated in the question.",
    "reason": "The correct choice is supported by a sequence-matched protein annotation, but the input supplies no functional or domain context that makes this specific cofactor inferable by general biological reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The available evidence specifically supports choice C; it does not establish another listed option as an alternative answer."
  },
  "important_caveats": [
    "The cofactor annotation is computational (PROSITE-ProRule), not direct experimental confirmation in the supplied evidence.",
    "The sequence match is exact in both the current and archived UniProt records; the record's cofactor annotation should not be mistaken for information supplied to the evaluated model."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry A0A7T8F1L4 (sequence matched, 1024 aa) annotates the cofactor as pantetheine 4'-phosphate (ChEBI:CHEBI:47942) with evidence code ECO:0000255|PROSITE-ProRule:PRU00258. The protein is a non-canonical nonribosomal peptide synthetase (FrzA, EC 1.2.1.101) from Cladobotryum sp. NRPS enzymes universally require pantetheine 4'-phosphate as the phosphopantetheinyl prosthetic group on the peptidyl carrier protein (PCP/T) domain. While the annotation evidence is computational (PROSITE pattern matching), the biological rationale is well-established general biochemistry for NRPS enzymes.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable NRPS multi-domain architecture signatures: (1) an adenylation (A) domain motif region including 'GDEGGESDQGELWIGGPGVSPGYFRQ' with the characteristic GGPG/A7 motif; (2) a condensation (C) domain motif 'GGTGFVGAFLL' with the classic C-domain glycine-rich flanking; (3) a PCP/thiolation (T) domain motif 'GGSCAPMDPT' containing the conserved serine in a GxxS context that serves as the phosphopantetheinylation site. NRPS enzymes universally require pantetheine 4'-phosphate covalently attached to the T-domain serine to carry activated amino acid intermediates. The distractors (Mg2+, NAD+, Fe2+) are common cofactors for other enzyme classes (kinases, dehydrogenases, oxygenases respectively) and are not associated with NRPS catalytic mechanisms.


**Missing item-specific fact**

> None critical. Recognition of the NRPS domain architecture from sequence motifs and the general biochemical fact that NRPS enzymes require pantetheine 4'-phosphate are both within the scope of general enzymology knowledge.


**Reason**

> A model with knowledge of NRPS domain architecture can identify the A, C, and T domain motifs in the sequence, conclude the protein is a nonribosomal peptide synthetase, and apply the well-known general fact that NRPS enzymes require pantetheine 4'-phosphate as their defining prosthetic group. This does not require recalling a specific database entry for FrzA.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The distractors Mg2+, NAD+, and Fe2+ are not cofactors of NRPS enzymes. Pantetheine 4'-phosphate is the unique and defining cofactor/prosthetic group of the thiolation domain in NRPS systems. No other listed option is defensible for an NRPS.


### Important caveats

- The UniProt cofactor annotation uses ECO:0000255 (PROSITE-ProRule computational inference), not direct experimental measurement of phosphopantetheinylation on this specific protein. However, the NRPS-cofactor relationship is textbook biochemistry.
- The protein is described as 'non-canonical' NRPS (EC 1.2.1.101, an aldehyde reductase-like function), but the presence of T-domain motifs and the PROSITE annotation still support pantetheine 4'-phosphate as the cofactor.
- Identification of NRPS domain motifs from raw sequence requires specialized domain-architecture knowledge; a model without this training would likely default to a generic cofactor guess.
- The sequence is from Cladobotryum sp. (a mycoparasitic fungus), and the protein participates in FR901483 immunosuppressant biosynthesis per the cited 2021 JACS paper.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable NRPS multi-domain architecture signatures: (1) an adenylation (A) domain motif region including 'GDEGGESDQGELWIGGPGVSPGYFRQ' with the characteristic GGPG/A7 motif; (2) a condensation (C) domain motif 'GGTGFVGAFLL' with the classic C-domain glycine-rich flanking; (3) a PCP/thiolation (T) domain motif 'GGSCAPMDPT' containing the conserved serine in a GxxS context that serves as the phosphopantetheinylation site. NRPS enzymes universally require pantetheine 4'-phosphate covalently attached to the T-domain serine to carry activated amino acid intermediates. The distractors (Mg2+, NAD+, Fe2+) are common cofactors for other enzyme classes (kinases, dehydrogenases, oxygenases respectively) and are not associated with NRPS catalytic mechanisms.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "None critical. Recognition of the NRPS domain architecture from sequence motifs and the general biochemical fact that NRPS enzymes require pantetheine 4'-phosphate are both within the scope of general enzymology knowledge.",
    "reason": "A model with knowledge of NRPS domain architecture can identify the A, C, and T domain motifs in the sequence, conclude the protein is a nonribosomal peptide synthetase, and apply the well-known general fact that NRPS enzymes require pantetheine 4'-phosphate as their defining prosthetic group. This does not require recalling a specific database entry for FrzA."
  },
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8F1L4 (sequence matched, 1024 aa) annotates the cofactor as pantetheine 4'-phosphate (ChEBI:CHEBI:47942) with evidence code ECO:0000255|PROSITE-ProRule:PRU00258. The protein is a non-canonical nonribosomal peptide synthetase (FrzA, EC 1.2.1.101) from Cladobotryum sp. NRPS enzymes universally require pantetheine 4'-phosphate as the phosphopantetheinyl prosthetic group on the peptidyl carrier protein (PCP/T) domain. While the annotation evidence is computational (PROSITE pattern matching), the biological rationale is well-established general biochemistry for NRPS enzymes."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000255 (PROSITE-ProRule computational inference), not direct experimental measurement of phosphopantetheinylation on this specific protein. However, the NRPS-cofactor relationship is textbook biochemistry.",
    "The protein is described as 'non-canonical' NRPS (EC 1.2.1.101, an aldehyde reductase-like function), but the presence of T-domain motifs and the PROSITE annotation still support pantetheine 4'-phosphate as the cofactor.",
    "Identification of NRPS domain motifs from raw sequence requires specialized domain-architecture knowledge; a model without this training would likely default to a generic cofactor guess.",
    "The sequence is from Cladobotryum sp. (a mycoparasitic fungus), and the protein participates in FR901483 immunosuppressant biosynthesis per the cited 2021 JACS paper."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors Mg2+, NAD+, and Fe2+ are not cofactors of NRPS enzymes. Pantetheine 4'-phosphate is the unique and defining cofactor/prosthetic group of the thiolation domain in NRPS systems. No other listed option is defensible for an NRPS."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry A0A7T8F1L4 (sequence matched, 1024 aa) annotates the cofactor as pantetheine 4'-phosphate (ChEBI:CHEBI:47942) with evidence code ECO:0000255|PROSITE-ProRule:PRU00258. The protein is a non-canonical nonribosomal peptide synthetase (FrzA, EC 1.2.1.101) from Cladobotryum sp. NRPS enzymes universally require pantetheine 4'-phosphate as the phosphopantetheinyl prosthetic group on the peptidyl carrier protein (PCP/T) domain. While the annotation evidence is computational (PROSITE pattern matching), the biological rationale is well-established general biochemistry for NRPS enzymes.",
    "evidence_ids": ["C1", "C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable NRPS multi-domain architecture signatures: (1) an adenylation (A) domain motif region including 'GDEGGESDQGELWIGGPGVSPGYFRQ' with the characteristic GGPG/A7 motif; (2) a condensation (C) domain motif 'GGTGFVGAFLL' with the classic C-domain glycine-rich flanking; (3) a PCP/thiolation (T) domain motif 'GGSCAPMDPT' containing the conserved serine in a GxxS context that serves as the phosphopantetheinylation site. NRPS enzymes universally require pantetheine 4'-phosphate covalently attached to the T-domain serine to carry activated amino acid intermediates. The distractors (Mg2+, NAD+, Fe2+) are common cofactors for other enzyme classes (kinases, dehydrogenases, oxygenases respectively) and are not associated with NRPS catalytic mechanisms.",
    "missing_item_specific_fact": "None critical. Recognition of the NRPS domain architecture from sequence motifs and the general biochemical fact that NRPS enzymes require pantetheine 4'-phosphate are both within the scope of general enzymology knowledge.",
    "reason": "A model with knowledge of NRPS domain architecture can identify the A, C, and T domain motifs in the sequence, conclude the protein is a nonribosomal peptide synthetase, and apply the well-known general fact that NRPS enzymes require pantetheine 4'-phosphate as their defining prosthetic group. This does not require recalling a specific database entry for FrzA."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors Mg2+, NAD+, and Fe2+ are not cofactors of NRPS enzymes. Pantetheine 4'-phosphate is the unique and defining cofactor/prosthetic group of the thiolation domain in NRPS systems. No other listed option is defensible for an NRPS."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses ECO:0000255 (PROSITE-ProRule computational inference), not direct experimental measurement of phosphopantetheinylation on this specific protein. However, the NRPS-cofactor relationship is textbook biochemistry.",
    "The protein is described as 'non-canonical' NRPS (EC 1.2.1.101, an aldehyde reductase-like function), but the presence of T-domain motifs and the PROSITE annotation still support pantetheine 4'-phosphate as the cofactor.",
    "Identification of NRPS domain motifs from raw sequence requires specialized domain-architecture knowledge; a model without this training would likely default to a generic cofactor guess.",
    "The sequence is from Cladobotryum sp. (a mycoparasitic fungus), and the protein participates in FR901483 immunosuppressant biosynthesis per the cited 2021 JACS paper."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt record annotates pantetheine 4'-phosphate as the cofactor. The annotation is supported by a PROSITE rule, so it is computational evidence rather than direct experimental confirmation of cofactor dependence.

Citations as saved: [H4](#evidence-h4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, multidomain sequence includes a serine-containing DSL-like motif consistent with a nonribosomal peptide synthetase carrier-protein domain. Transferable knowledge of these domains predicts attachment of 4'-phosphopantetheine to a conserved serine, providing a swinging arm for substrate handling. That gives a meaningful basis for choice C over the metal-ion and NAD(+) options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A carrier-protein-domain inference from sequence features and general NRPS biology can distinguish the offered choice without requiring the exact protein's database annotation. This supports a probabilistic inference, not proof from sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed choices, the carrier-protein phosphopantetheine group is the distinct fit; the supplied evidence does not identify another listed option as equally defensible.


### Important caveats

- The cited cofactor annotation is rule-based computational evidence, not direct experimental validation.
- The sequence supports a transferable family/domain inference, but does not by itself establish every detail of cofactor dependence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, multidomain sequence includes a serine-containing DSL-like motif consistent with a nonribosomal peptide synthetase carrier-protein domain. Transferable knowledge of these domains predicts attachment of 4'-phosphopantetheine to a conserved serine, providing a swinging arm for substrate handling. That gives a meaningful basis for choice C over the metal-ion and NAD(+) options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A carrier-protein-domain inference from sequence features and general NRPS biology can distinguish the offered choice without requiring the exact protein's database annotation. This supports a probabilistic inference, not proof from sequence alone."
  },
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates pantetheine 4'-phosphate as the cofactor. The annotation is supported by a PROSITE rule, so it is computational evidence rather than direct experimental confirmation of cofactor dependence."
  },
  "important_caveats": [
    "The cited cofactor annotation is rule-based computational evidence, not direct experimental validation.",
    "The sequence supports a transferable family/domain inference, but does not by itself establish every detail of cofactor dependence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the carrier-protein phosphopantetheine group is the distinct fit; the supplied evidence does not identify another listed option as equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates pantetheine 4'-phosphate as the cofactor. The annotation is supported by a PROSITE rule, so it is computational evidence rather than direct experimental confirmation of cofactor dependence.",
    "evidence_ids": ["H4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, multidomain sequence includes a serine-containing DSL-like motif consistent with a nonribosomal peptide synthetase carrier-protein domain. Transferable knowledge of these domains predicts attachment of 4'-phosphopantetheine to a conserved serine, providing a swinging arm for substrate handling. That gives a meaningful basis for choice C over the metal-ion and NAD(+) options.",
    "missing_item_specific_fact": "",
    "reason": "A carrier-protein-domain inference from sequence features and general NRPS biology can distinguish the offered choice without requiring the exact protein's database annotation. This supports a probabilistic inference, not proof from sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed choices, the carrier-protein phosphopantetheine group is the distinct fit; the supplied evidence does not identify another listed option as equally defensible."
  },
  "important_caveats": [
    "The cited cofactor annotation is rule-based computational evidence, not direct experimental validation.",
    "The sequence supports a transferable family/domain inference, but does not by itself establish every detail of cofactor dependence."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H4) explicitly lists pantetheine 4'-phosphate as the cofactor, with evidence code ECO:0000255|PROSITE-ProRule:PRU00258. This is a computational/PROSITE-pattern-based annotation rather than a direct experimental cofactor measurement. However, the protein is annotated as a nonribosomal peptide synthetase (EC 1.2.1.101, FrzA), and NRPS enzymes require pantetheine 4'-phosphate for their peptidyl carrier protein (PCP) domains. The PROSITE PP-binding pattern detection is consistent with the known biochemistry of NRPS systems. The annotation is supported but rests on pattern recognition rather than a direct biochemical assay of the cofactor.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable features of a nonribosomal peptide synthetase (NRPS): (1) A phosphopantetheine (PP) binding motif is present — the stretch 'GGTGFVGAFL' and 'GGSCAPMDP' contain GxS/GGDS-type motifs characteristic of peptidyl carrier protein (PCP) domains, where a conserved serine is post-translationally modified with pantetheine 4'-phosphate. This PP-binding motif is one of the most well-known, transferable sequence signatures across the entire NRPS and fatty-acid synthase (FAS) superfamily. (2) Adenylation (A) domain motifs are also discernible (e.g., 'GGEAANVAAIRIILKNGPPAMLFNAYGPTECC' region resembles the C3/C4 adenylation domain motifs). Recognizing these NRPS domain signatures from general family knowledge (learned from hundreds of characterized NRPS proteins like gramicidin S synthetase, surfactin synthetase, etc.) leads directly to pantetheine 4'-phosphate as the required cofactor, because the PCP domain's catalytic function depends on the PP arm carrying the growing peptide chain. The distractors are readily excluded: Mg(2+) is a general metal cofactor for kinases/polymerases, NAD(+) is for dehydrogenases, and Fe(2+) is for dioxygenases/oxidases — none of which match the NRPS/PCP cofactor requirement. This is a standard family-level inference, not a lookup of this specific protein's record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the PP-binding motif and adenylation domain architecture from general NRPS/FAS family knowledge, which is broadly transferable across hundreds of characterized NRPS proteins. This family-level pattern meaningfully distinguishes pantetheine 4'-phosphate (C) from the three distractors without needing the specific annotation of this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The PP-binding motif and NRPS domain architecture point unambiguously to pantetheine 4'-phosphate. The distractors (Mg2+, NAD+, Fe2+) correspond to entirely different enzyme classes and are not plausible cofactors for an NRPS PCP domain. No other option is defensible given the sequence features.


### Important caveats

- The UniProt cofactor annotation uses evidence code ECO:0000255 (PROSITE-ProRule), which is computational pattern-based rather than a direct experimental cofactor measurement. The annotation is consistent with NRPS biochemistry but is not an independent experimental determination of the cofactor for this specific enzyme.
- The protein is described as a 'non-canonical' NRPS, which could in principle imply unusual cofactor requirements, but the presence of the PP-binding motif in the sequence supports the standard NRPS cofactor assignment.
- The PP-binding motif in this sequence ('GGTGFVGA', 'GGSCAPMDP') is a variant of the canonical 'GxDSL' motif; recognizing these variants requires familiarity with the diversity of PP-binding motifs across NRPS/FAS families.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable features of a nonribosomal peptide synthetase (NRPS): (1) A phosphopantetheine (PP) binding motif is present — the stretch 'GGTGFVGAFL' and 'GGSCAPMDP' contain GxS/GGDS-type motifs characteristic of peptidyl carrier protein (PCP) domains, where a conserved serine is post-translationally modified with pantetheine 4'-phosphate. This PP-binding motif is one of the most well-known, transferable sequence signatures across the entire NRPS and fatty-acid synthase (FAS) superfamily. (2) Adenylation (A) domain motifs are also discernible (e.g., 'GGEAANVAAIRIILKNGPPAMLFNAYGPTECC' region resembles the C3/C4 adenylation domain motifs). Recognizing these NRPS domain signatures from general family knowledge (learned from hundreds of characterized NRPS proteins like gramicidin S synthetase, surfactin synthetase, etc.) leads directly to pantetheine 4'-phosphate as the required cofactor, because the PCP domain's catalytic function depends on the PP arm carrying the growing peptide chain. The distractors are readily excluded: Mg(2+) is a general metal cofactor for kinases/polymerases, NAD(+) is for dehydrogenases, and Fe(2+) is for dioxygenases/oxidases — none of which match the NRPS/PCP cofactor requirement. This is a standard family-level inference, not a lookup of this specific protein's record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the PP-binding motif and adenylation domain architecture from general NRPS/FAS family knowledge, which is broadly transferable across hundreds of characterized NRPS proteins. This family-level pattern meaningfully distinguishes pantetheine 4'-phosphate (C) from the three distractors without needing the specific annotation of this exact protein."
  },
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists pantetheine 4'-phosphate as the cofactor, with evidence code ECO:0000255|PROSITE-ProRule:PRU00258. This is a computational/PROSITE-pattern-based annotation rather than a direct experimental cofactor measurement. However, the protein is annotated as a nonribosomal peptide synthetase (EC 1.2.1.101, FrzA), and NRPS enzymes require pantetheine 4'-phosphate for their peptidyl carrier protein (PCP) domains. The PROSITE PP-binding pattern detection is consistent with the known biochemistry of NRPS systems. The annotation is supported but rests on pattern recognition rather than a direct biochemical assay of the cofactor."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses evidence code ECO:0000255 (PROSITE-ProRule), which is computational pattern-based rather than a direct experimental cofactor measurement. The annotation is consistent with NRPS biochemistry but is not an independent experimental determination of the cofactor for this specific enzyme.",
    "The protein is described as a 'non-canonical' NRPS, which could in principle imply unusual cofactor requirements, but the presence of the PP-binding motif in the sequence supports the standard NRPS cofactor assignment.",
    "The PP-binding motif in this sequence ('GGTGFVGA', 'GGSCAPMDP') is a variant of the canonical 'GxDSL' motif; recognizing these variants requires familiarity with the diversity of PP-binding motifs across NRPS/FAS families."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PP-binding motif and NRPS domain architecture point unambiguously to pantetheine 4'-phosphate. The distractors (Mg2+, NAD+, Fe2+) correspond to entirely different enzyme classes and are not plausible cofactors for an NRPS PCP domain. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0043",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists pantetheine 4'-phosphate as the cofactor, with evidence code ECO:0000255|PROSITE-ProRule:PRU00258. This is a computational/PROSITE-pattern-based annotation rather than a direct experimental cofactor measurement. However, the protein is annotated as a nonribosomal peptide synthetase (EC 1.2.1.101, FrzA), and NRPS enzymes require pantetheine 4'-phosphate for their peptidyl carrier protein (PCP) domains. The PROSITE PP-binding pattern detection is consistent with the known biochemistry of NRPS systems. The annotation is supported but rests on pattern recognition rather than a direct biochemical assay of the cofactor.",
    "evidence_ids": ["C5", "H4", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable features of a nonribosomal peptide synthetase (NRPS): (1) A phosphopantetheine (PP) binding motif is present — the stretch 'GGTGFVGAFL' and 'GGSCAPMDP' contain GxS/GGDS-type motifs characteristic of peptidyl carrier protein (PCP) domains, where a conserved serine is post-translationally modified with pantetheine 4'-phosphate. This PP-binding motif is one of the most well-known, transferable sequence signatures across the entire NRPS and fatty-acid synthase (FAS) superfamily. (2) Adenylation (A) domain motifs are also discernible (e.g., 'GGEAANVAAIRIILKNGPPAMLFNAYGPTECC' region resembles the C3/C4 adenylation domain motifs). Recognizing these NRPS domain signatures from general family knowledge (learned from hundreds of characterized NRPS proteins like gramicidin S synthetase, surfactin synthetase, etc.) leads directly to pantetheine 4'-phosphate as the required cofactor, because the PCP domain's catalytic function depends on the PP arm carrying the growing peptide chain. The distractors are readily excluded: Mg(2+) is a general metal cofactor for kinases/polymerases, NAD(+) is for dehydrogenases, and Fe(2+) is for dioxygenases/oxidases — none of which match the NRPS/PCP cofactor requirement. This is a standard family-level inference, not a lookup of this specific protein's record.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the PP-binding motif and adenylation domain architecture from general NRPS/FAS family knowledge, which is broadly transferable across hundreds of characterized NRPS proteins. This family-level pattern meaningfully distinguishes pantetheine 4'-phosphate (C) from the three distractors without needing the specific annotation of this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The PP-binding motif and NRPS domain architecture point unambiguously to pantetheine 4'-phosphate. The distractors (Mg2+, NAD+, Fe2+) correspond to entirely different enzyme classes and are not plausible cofactors for an NRPS PCP domain. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The UniProt cofactor annotation uses evidence code ECO:0000255 (PROSITE-ProRule), which is computational pattern-based rather than a direct experimental cofactor measurement. The annotation is consistent with NRPS biochemistry but is not an independent experimental determination of the cofactor for this specific enzyme.",
    "The protein is described as a 'non-canonical' NRPS, which could in principle imply unusual cofactor requirements, but the presence of the PP-binding motif in the sequence supports the standard NRPS cofactor assignment.",
    "The PP-binding motif in this sequence ('GGTGFVGA', 'GGSCAPMDP') is a variant of the canonical 'GxDSL' motif; recognizing these variants requires familiarity with the diversity of PP-binding motifs across NRPS/FAS families."
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
  "requested_accession": "A0A7T8F1L4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "78903b102e2259d837b80ac44bcf15e6ae1534722167cff1a23d530bb0db74e0",
  "benchmark_sequence_length": 1024,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 20,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "current_source_sequence_sha256": "78903b102e2259d837b80ac44bcf15e6ae1534722167cff1a23d530bb0db74e0",
  "current_source_sequence_length": 1024,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 18,
  "selected_historical_version": {
    "accession": "A0A7T8F1L4",
    "database": "Swiss-Prot",
    "entryVersion": 18,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZA_CLASX",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "selected_historical_source_sequence_sha256": "78903b102e2259d837b80ac44bcf15e6ae1534722167cff1a23d530bb0db74e0",
  "selected_historical_source_sequence_length": 1024,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 18,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A7T8F1L4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":20,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis cluster protein A\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"1.2.1.101\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Non-canonical nonribosomal peptide synthetase FrzA\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "json_pointer": "/comments/2",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:47942\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00258\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"pantetheine 4'-phosphate\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1L4.json",
  "source_sha256": "4cf4e4af61e7d91300bdd1c46dcd31d2e7126d4631315e40df3061127135d0fb",
  "retrieved_utc": "2026-11-02T04:25:48.509506+00:00",
  "json_pointer": "/references/0",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18",
  "source_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "retrieved_utc": "2026-11-02T04:25:50.375049+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   FRZA_CLASX              Reviewed;        1024 AA.\nAC   A0A7T8F1L4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 18.\nDE   RecName: Full=Non-canonical nonribosomal peptide synthetase FrzA {ECO:0000303|PubMed:33372776};\nDE            EC=1.2.1.101 {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein A {ECO:0000303|PubMed:33372776};\nGN   Name=FrzA {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18",
  "source_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "retrieved_utc": "2026-11-02T04:25:50.375049+00:00",
  "source_locator": "lines 6-8",
  "excerpt": "DE   RecName: Full=Non-canonical nonribosomal peptide synthetase FrzA {ECO:0000303|PubMed:33372776};\nDE            EC=1.2.1.101 {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein A {ECO:0000303|PubMed:33372776};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18",
  "source_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "retrieved_utc": "2026-11-02T04:25:50.375049+00:00",
  "source_locator": "lines 14-22",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1L4?format=txt&versions=18",
  "source_sha256": "dc244e3d4206d7a97707ec88200b44521e519f3504ebcf6f0cd7d074b3fd2c4b",
  "retrieved_utc": "2026-11-02T04:25:50.375049+00:00",
  "source_locator": "lines 62-64",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=pantetheine 4'-phosphate; Xref=ChEBI:CHEBI:47942;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00258};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 18,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 43. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
