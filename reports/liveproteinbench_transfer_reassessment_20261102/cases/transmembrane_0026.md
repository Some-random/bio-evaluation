# transmembrane_0026: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/transmembrane_0026.txt)

**Task:** `transmembrane`  
**Author key, unchanged:** **B** — 1404..1424

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
MAAKAIQYNIKVDLHEVKDLSFREAAGEKEIVPNPYIEVTVNGVTKTTIQKTQVVSATFNTSFNFTAYLTPDEFARSYVEVAVLHKYMLIGGVGLQSAVIGKYVFSFAYVYTKSQHWIYRQWVTLRNLDQPQDETGLLLITVGVFGPGDAMPVVDETVCVVNEGERTSTDVNVKLTHYSLSVNIFKGQDIPSVAGQFSTVLEPYVKVKHGGAELQTRPLPDSNPDWLASISIPACVPCFDGNVLVELWNGQDSSTAAGTLMGTVVLDYFQLIKNDLPPRWFNFYWRPPAEGLLGAVTDMMASAELREPIAYGGRILLSASAAKVQTPLPLGVRSARPIPDPATQECVWWLDLYEMTSATGYTSELRIEIAFGPHVIKTASLEANALGTYVIGDNLGRLPEMKIFAPVDEVQVWDVMMYVCSPPATTVAAGIADISNWFSGWGGSPTATQNTPEPAETPWTRLAWVRIPYDSRQFQNGKPQWYSLRSLDGSGTDMFSVLLGMEMFPTKAGKQRAPRLEYKLARFYFRALIYEGLHLPAVGYDVFPDPYIQVELASKTLRTSTIRQTLNPSYYEAYEIEIRLPENISLAPDINVEVISESNSLLSSDVVLGSVQYPIQKVPKEWTKAPVWLQLHSKAYPRCKARVLVAFELVPAEKAEDDTYPFYDDIRPSTKEGNIRLFLVGVRLFKPITQPFVTVCFGRDVENTAEPLWSQESSAPRTGEGGNWNFLEEFTVSVSLPKRMQHHSFLEVKIQDRTQGIGGESNVDVGMAYITLNPLLPWLDSRERAESLETFRLQMLEEVLIEDAENARRSADGGLAARTGGGSFDEDATKKKEMLAAERSRKMAIPYNDPDMANLKIEEVDDYVSFKVAPRPQASRLSREGTSRDERGKAPGKSLSGMPGPVARASPGAGEETEKKGDPVAEKKEGGAQAAPPVAPSAHQREALAASPEEETYGFTPEQLNFVLADLEEDDAEEMTRDEVPYELEADFTVDDLPYLRTPIFRPTDAGVPETVGYLKYVCRVFQSTDEDEGAEMDAVCKSLIETYNSTRDLVVRAYVLAARGLVPPSGASDIQTYVWIQDSENAATLPGGLSYNIRDTGYTKKQGFKPEFNRCYTLACSLPENSIVQIAVMNMGRLTDECIGRTYLDVEDRFFNKKVEQMVIEESTPIELRTLKNEGSTVSHGSLRGFFEIMRADYAQLHPPYTLASAEPDEYQLRVVIWRVKAVPLDDNSSISLFVRTIYQLEDSSEIVKDTDTHYNSTDGTAVYNWRMVFDVLIPAQIPVLKLQIWNYALLSSTEPIGEANFDLTADFFRARKRQQHYRVPRMWVRCSHPAHKGKLRGTIEIEASILPREEAEYTPVGNGRDEPNRDPFLPAVTTNRTYIDWQQIGETVGAASSAIMSGLKWTGVWMTVAGIIALVIFVMFLLK

[Multiple Choices]
A. 35..55
B. 1404..1424
C. 1408..1423
D. 1404..1424; 199..217
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry annotates residues 1404–1424 as a helical transmembrane region. This is computational annotation, not direct experimental confirmation.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The strongly hydrophobic C-terminal stretch supports a membrane-spanning helix and rules against the nonhydrophobic N-terminal option; it does not establish the exact annotated boundaries over the overlapping shorter choice.


**Missing item-specific fact**

> The protein-specific transmembrane boundaries, particularly whether the region begins at 1404 rather than 1408 and ends at 1424 rather than 1423.


**Reason**

> General sequence reasoning identifies the likely C-terminal transmembrane region, but selecting the exact coordinates requires an item-specific boundary annotation or measurement absent from the input. The reviewer-only database annotation cannot count as information supplied to the model.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B matches the annotated 1404–1424 span. C is a shorter, overlapping hydrophobic segment that could also be regarded as membrane-spanning under a broad region-prediction wording; no boundary convention is given to distinguish them.


### Important caveats

- The supplied sequence exactly matches the historical and current UniProt sequence, but the author’s source snapshot is unknown.
- The cited transmembrane annotation carries computational evidence code ECO:0000255; it should not be presented as an experimental measurement.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The strongly hydrophobic C-terminal stretch supports a membrane-spanning helix and rules against the nonhydrophobic N-terminal option; it does not establish the exact annotated boundaries over the overlapping shorter choice.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific transmembrane boundaries, particularly whether the region begins at 1404 rather than 1408 and ends at 1424 rather than 1423.",
    "reason": "General sequence reasoning identifies the likely C-terminal transmembrane region, but selecting the exact coordinates requires an item-specific boundary annotation or measurement absent from the input. The reviewer-only database annotation cannot count as information supplied to the model."
  },
  "case_id": "transmembrane_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates residues 1404–1424 as a helical transmembrane region. This is computational annotation, not direct experimental confirmation."
  },
  "important_caveats": [
    "The supplied sequence exactly matches the historical and current UniProt sequence, but the author’s source snapshot is unknown.",
    "The cited transmembrane annotation carries computational evidence code ECO:0000255; it should not be presented as an experimental measurement."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B matches the annotated 1404–1424 span. C is a shorter, overlapping hydrophobic segment that could also be regarded as membrane-spanning under a broad region-prediction wording; no boundary convention is given to distinguish them."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates residues 1404–1424 as a helical transmembrane region. This is computational annotation, not direct experimental confirmation.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The strongly hydrophobic C-terminal stretch supports a membrane-spanning helix and rules against the nonhydrophobic N-terminal option; it does not establish the exact annotated boundaries over the overlapping shorter choice.",
    "missing_item_specific_fact": "The protein-specific transmembrane boundaries, particularly whether the region begins at 1404 rather than 1408 and ends at 1424 rather than 1423.",
    "reason": "General sequence reasoning identifies the likely C-terminal transmembrane region, but selecting the exact coordinates requires an item-specific boundary annotation or measurement absent from the input. The reviewer-only database annotation cannot count as information supplied to the model."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B matches the annotated 1404–1424 span. C is a shorter, overlapping hydrophobic segment that could also be regarded as membrane-spanning under a broad region-prediction wording; no boundary convention is given to distinguish them."
  },
  "important_caveats": [
    "The supplied sequence exactly matches the historical and current UniProt sequence, but the author’s source snapshot is unknown.",
    "The cited transmembrane annotation carries computational evidence code ECO:0000255; it should not be presented as an experimental measurement."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A7J6JXB6 (FER1_TOXGO, Toxoplasma gondii Ferlin 1, 1425 AA, sequence matched exactly) annotates a single transmembrane helix at positions 1404..1424 with evidence code ECO:0000255 (inferred by similarity). The sequence at 1404-1424 (TGVWMTVAGIIALVIFVMFLL) contains a clear hydrophobic core (WMTVAGIIALVIFVMFLL, ~18 residues) consistent with a single-pass TM helix. The annotation is computational/automatic rather than experimentally validated, but it is the authoritative database annotation supporting the key.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C1](#evidence-c1), [C2](#evidence-c2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Choice A (35..55) falls in a polar/charged N-terminal region (EKEIVPNPYIEVTVNGVTKTT) with no hydrophobic stretch—eliminated by hydrophobicity reasoning. Choice D adds a second TM at 199..217 (TVLEPYVKVKHGGAELQTR), which is dominated by charged/polar residues (E, K, K, H, Q, R)—clearly not a TM helix, eliminable by reasoning. The remaining B vs C distinction: the full ~21-residue hydrophobic stretch at the C-terminus (TGVWMTVAGIIALVIFVMFLL) matches the canonical 18-25 residue single-pass TM helix length, with Trp at position 1407 serving as a membrane-interface anchor. The broader definition (B, 1404-1424) captures the full helix including interface residues, while C (1408-1423, 16 residues) truncates the helix below the canonical minimum. A hydrophobicity window analysis of the C-terminal 25 residues identifies a ~20-residue hydrophobic segment consistent with B.


**Missing item-specific fact**

> The exact boundary between B (1404..1424) and C (1408..1423) is algorithm-dependent (ECO:0000255 = inferred by similarity). A different TM predictor might place the boundary at 1406 or 1407 rather than 1404. However, the broader 21-residue definition is defensible by canonical TM helix length arguments.


**Reason**

> A model can eliminate A and D by straightforward hydrophobicity reasoning (charged/polar regions cannot span a lipid bilayer). The B vs C distinction is fine but a reasonable biological argument exists: the 21-residue predominantly hydrophobic stretch at the C-terminus is the canonical TM helix length, and the Trp anchor at position 1407 supports including residues from 1404. The question is answerable by general membrane-biophysics reasoning, though the precise boundary is somewhat algorithm-sensitive.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> The hydrophobic core (WMTVAGIIALVIFVMFLL, positions ~1407-1424) is unambiguous. The exact N-terminal boundary (whether to include T and G at 1404-1405, which are not strongly hydrophobic) is a matter of prediction-algorithm threshold. Both B and C capture the TM core; B is slightly more generous. The UniProt annotation favors B, but a strict hydrophobicity cutoff might yield something closer to C. This is a fine boundary issue, not a fundamental ambiguity about whether a TM exists.


### Important caveats

- The transmembrane annotation carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational prediction, not experimentally validated.
- The UniProt entry was first released 2025-02-05; the author's source snapshot is unknown but the sequence version (1) has been unchanged since 2021-04-07.
- The B/C boundary distinction is algorithm-sensitive; the question is answerable by reasoning but the precise residue-level boundary is not uniquely determined by biophysics alone.
- Choice D's second segment (199..217) is clearly non-hydrophobic and serves as an effective distractor eliminable by reasoning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Choice A (35..55) falls in a polar/charged N-terminal region (EKEIVPNPYIEVTVNGVTKTT) with no hydrophobic stretch—eliminated by hydrophobicity reasoning. Choice D adds a second TM at 199..217 (TVLEPYVKVKHGGAELQTR), which is dominated by charged/polar residues (E, K, K, H, Q, R)—clearly not a TM helix, eliminable by reasoning. The remaining B vs C distinction: the full ~21-residue hydrophobic stretch at the C-terminus (TGVWMTVAGIIALVIFVMFLL) matches the canonical 18-25 residue single-pass TM helix length, with Trp at position 1407 serving as a membrane-interface anchor. The broader definition (B, 1404-1424) captures the full helix including interface residues, while C (1408-1423, 16 residues) truncates the helix below the canonical minimum. A hydrophobicity window analysis of the C-terminal 25 residues identifies a ~20-residue hydrophobic segment consistent with B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "The exact boundary between B (1404..1424) and C (1408..1423) is algorithm-dependent (ECO:0000255 = inferred by similarity). A different TM predictor might place the boundary at 1406 or 1407 rather than 1404. However, the broader 21-residue definition is defensible by canonical TM helix length arguments.",
    "reason": "A model can eliminate A and D by straightforward hydrophobicity reasoning (charged/polar regions cannot span a lipid bilayer). The B vs C distinction is fine but a reasonable biological argument exists: the 21-residue predominantly hydrophobic stretch at the C-terminus is the canonical TM helix length, and the Trp anchor at position 1407 supports including residues from 1404. The question is answerable by general membrane-biophysics reasoning, though the precise boundary is somewhat algorithm-sensitive."
  },
  "case_id": "transmembrane_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C1",
      "C2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A7J6JXB6 (FER1_TOXGO, Toxoplasma gondii Ferlin 1, 1425 AA, sequence matched exactly) annotates a single transmembrane helix at positions 1404..1424 with evidence code ECO:0000255 (inferred by similarity). The sequence at 1404-1424 (TGVWMTVAGIIALVIFVMFLL) contains a clear hydrophobic core (WMTVAGIIALVIFVMFLL, ~18 residues) consistent with a single-pass TM helix. The annotation is computational/automatic rather than experimentally validated, but it is the authoritative database annotation supporting the key."
  },
  "important_caveats": [
    "The transmembrane annotation carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational prediction, not experimentally validated.",
    "The UniProt entry was first released 2025-02-05; the author's source snapshot is unknown but the sequence version (1) has been unchanged since 2021-04-07.",
    "The B/C boundary distinction is algorithm-sensitive; the question is answerable by reasoning but the precise residue-level boundary is not uniquely determined by biophysics alone.",
    "Choice D's second segment (199..217) is clearly non-hydrophobic and serves as an effective distractor eliminable by reasoning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "The hydrophobic core (WMTVAGIIALVIFVMFLL, positions ~1407-1424) is unambiguous. The exact N-terminal boundary (whether to include T and G at 1404-1405, which are not strongly hydrophobic) is a matter of prediction-algorithm threshold. Both B and C capture the TM core; B is slightly more generous. The UniProt annotation favors B, but a strict hydrophobicity cutoff might yield something closer to C. This is a fine boundary issue, not a fundamental ambiguity about whether a TM exists."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A7J6JXB6 (FER1_TOXGO, Toxoplasma gondii Ferlin 1, 1425 AA, sequence matched exactly) annotates a single transmembrane helix at positions 1404..1424 with evidence code ECO:0000255 (inferred by similarity). The sequence at 1404-1424 (TGVWMTVAGIIALVIFVMFLL) contains a clear hydrophobic core (WMTVAGIIALVIFVMFLL, ~18 residues) consistent with a single-pass TM helix. The annotation is computational/automatic rather than experimentally validated, but it is the authoritative database annotation supporting the key.",
    "evidence_ids": ["C5", "H4", "C1", "C2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Choice A (35..55) falls in a polar/charged N-terminal region (EKEIVPNPYIEVTVNGVTKTT) with no hydrophobic stretch—eliminated by hydrophobicity reasoning. Choice D adds a second TM at 199..217 (TVLEPYVKVKHGGAELQTR), which is dominated by charged/polar residues (E, K, K, H, Q, R)—clearly not a TM helix, eliminable by reasoning. The remaining B vs C distinction: the full ~21-residue hydrophobic stretch at the C-terminus (TGVWMTVAGIIALVIFVMFLL) matches the canonical 18-25 residue single-pass TM helix length, with Trp at position 1407 serving as a membrane-interface anchor. The broader definition (B, 1404-1424) captures the full helix including interface residues, while C (1408-1423, 16 residues) truncates the helix below the canonical minimum. A hydrophobicity window analysis of the C-terminal 25 residues identifies a ~20-residue hydrophobic segment consistent with B.",
    "missing_item_specific_fact": "The exact boundary between B (1404..1424) and C (1408..1423) is algorithm-dependent (ECO:0000255 = inferred by similarity). A different TM predictor might place the boundary at 1406 or 1407 rather than 1404. However, the broader 21-residue definition is defensible by canonical TM helix length arguments.",
    "reason": "A model can eliminate A and D by straightforward hydrophobicity reasoning (charged/polar regions cannot span a lipid bilayer). The B vs C distinction is fine but a reasonable biological argument exists: the 21-residue predominantly hydrophobic stretch at the C-terminus is the canonical TM helix length, and the Trp anchor at position 1407 supports including residues from 1404. The question is answerable by general membrane-biophysics reasoning, though the precise boundary is somewhat algorithm-sensitive."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "The hydrophobic core (WMTVAGIIALVIFVMFLL, positions ~1407-1424) is unambiguous. The exact N-terminal boundary (whether to include T and G at 1404-1405, which are not strongly hydrophobic) is a matter of prediction-algorithm threshold. Both B and C capture the TM core; B is slightly more generous. The UniProt annotation favors B, but a strict hydrophobicity cutoff might yield something closer to C. This is a fine boundary issue, not a fundamental ambiguity about whether a TM exists."
  },
  "important_caveats": [
    "The transmembrane annotation carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational prediction, not experimentally validated.",
    "The UniProt entry was first released 2025-02-05; the author's source snapshot is unknown but the sequence version (1) has been unchanged since 2021-04-07.",
    "The B/C boundary distinction is algorithm-sensitive; the question is answerable by reasoning but the precise residue-level boundary is not uniquely determined by biophysics alone.",
    "Choice D's second segment (199..217) is clearly non-hydrophobic and serves as an effective distractor eliminable by reasoning."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence match has a UniProt annotation for a helical transmembrane region at 1404..1424. This is computational evidence (ECO:0000255), not experimental confirmation, but it supports the keyed region.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a strongly hydrophobic stretch near its C-terminus, consistent with a membrane-spanning helix. Its roughly 21-residue length in B is typical for a transmembrane helix, making B a reasonable choice over the non-hydrophobic N-terminal option A and D's additional segment. C covers the hydrophobic core of the same stretch but is shorter.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge about the length and hydrophobicity of membrane-spanning helices meaningfully points to the C-terminal segment and favors B's fuller span, without needing the target's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> B and C both specify segments within the same strongly hydrophobic C-terminal stretch. C is shorter, but it still identifies a plausible portion of the membrane-spanning helix; sequence alone does not sharply establish the precise boundary.


### Important caveats

- The supporting database feature is computational rather than experimental.
- The exact start and end of a transmembrane helix can be uncertain from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic stretch near its C-terminus, consistent with a membrane-spanning helix. Its roughly 21-residue length in B is typical for a transmembrane helix, making B a reasonable choice over the non-hydrophobic N-terminal option A and D's additional segment. C covers the hydrophobic core of the same stretch but is shorter.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about the length and hydrophobicity of membrane-spanning helices meaningfully points to the C-terminal segment and favors B's fuller span, without needing the target's database record."
  },
  "case_id": "transmembrane_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match has a UniProt annotation for a helical transmembrane region at 1404..1424. This is computational evidence (ECO:0000255), not experimental confirmation, but it supports the keyed region."
  },
  "important_caveats": [
    "The supporting database feature is computational rather than experimental.",
    "The exact start and end of a transmembrane helix can be uncertain from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "B and C both specify segments within the same strongly hydrophobic C-terminal stretch. C is shorter, but it still identifies a plausible portion of the membrane-spanning helix; sequence alone does not sharply establish the precise boundary."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match has a UniProt annotation for a helical transmembrane region at 1404..1424. This is computational evidence (ECO:0000255), not experimental confirmation, but it supports the keyed region.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a strongly hydrophobic stretch near its C-terminus, consistent with a membrane-spanning helix. Its roughly 21-residue length in B is typical for a transmembrane helix, making B a reasonable choice over the non-hydrophobic N-terminal option A and D's additional segment. C covers the hydrophobic core of the same stretch but is shorter.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge about the length and hydrophobicity of membrane-spanning helices meaningfully points to the C-terminal segment and favors B's fuller span, without needing the target's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "B and C both specify segments within the same strongly hydrophobic C-terminal stretch. C is shorter, but it still identifies a plausible portion of the membrane-spanning helix; sequence alone does not sharply establish the precise boundary."
  },
  "important_caveats": [
    "The supporting database feature is computational rather than experimental.",
    "The exact start and end of a transmembrane helix can be uncertain from sequence alone."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence code ECO:0000255, 'by similarity') records a helical transmembrane region at positions 1404-1424. The sequence at these positions (TGVWMTVAGIIALVIFVMFLL) is predominantly hydrophobic (V, W, M, A, I, L, F dominate), consistent with a single-pass transmembrane alpha-helix at the C-terminus. While the evidence code indicates computational inference rather than experimental validation, the hydrophobic character of the sequence is directly observable and strongly supports the annotation.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal 21 residues (positions ~1405-1425: TGVWMTVAGIIALVIFVMFLLK) form a clearly hydrophobic stretch at the extreme C-terminus, a hallmark of single-pass type-I membrane protein anchoring. Option A (35-55) falls in a polar/charged N-terminal region (PYIEVTVNGVTKTTIQKTQVV) with no hydrophobic character, easily eliminated. The critical distinction between B (1404-1424, 21 residues) and C (1408-1423, 16 residues) rests on standard TM helix geometry: the lipid bilayer hydrophobic core is ~30 Å, requiring ~18-22 residues in an alpha-helix to span it. 16 residues (option C) is below the typical minimum, while 21 residues (option B) is squarely in the canonical range. Option D adds a second TM at 199-217; however, Ferlin-family proteins (recognizable by their C2 domain architecture visible in the long middle region of this ~1425-residue protein) are classically cytoplasmic proteins with at most a single C-terminal TM anchor, making a mid-chain second TM atypical. The hydrophobicity of the C-terminal segment is directly readable from the sequence, and the length criterion plus family-level knowledge of ferlin topology distinguish B from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can (1) visually identify the hydrophobic C-terminal stretch, (2) apply the standard ~20-residue TM helix length to prefer B over C, (3) recognize that the N-terminal region in option A lacks hydrophobic character, and (4) use ferlin-family knowledge (single-pass, C-terminal TM anchor) to reject the multi-TM option D. These are all transferable inferences from sequence features and family-level biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both B (1404-1424) and C (1408-1423) describe overlapping hydrophobic segments in the C-terminal TM region. The distinction depends on whether one includes the marginally hydrophobic T-G-V-W residues at 1404-1407 and the final L at 1424. While 21 residues is the more standard TM length, 16 residues is not strictly impossible for a TM helix. However, the full hydrophobic extent clearly begins around 1404-1405, and the annotation supports the longer definition. This is a minor boundary ambiguity rather than a fundamental ambiguity.


### Important caveats

- The UniProt transmembrane annotation carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational annotation rather than experimentally determined. However, the hydrophobicity of the sequence at 1404-1424 independently supports the assignment.
- The boundary between options B and C (21 vs 16 residues) is a minor precision issue; both describe the same TM region with slightly different boundaries. The 21-residue span is more consistent with canonical TM helix length.
- The protein is Toxoplasma gondii Ferlin 1 (FER1), a single-pass membrane protein with a C-terminal TM anchor, consistent with the ferlin family architecture.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal 21 residues (positions ~1405-1425: TGVWMTVAGIIALVIFVMFLLK) form a clearly hydrophobic stretch at the extreme C-terminus, a hallmark of single-pass type-I membrane protein anchoring. Option A (35-55) falls in a polar/charged N-terminal region (PYIEVTVNGVTKTTIQKTQVV) with no hydrophobic character, easily eliminated. The critical distinction between B (1404-1424, 21 residues) and C (1408-1423, 16 residues) rests on standard TM helix geometry: the lipid bilayer hydrophobic core is ~30 Å, requiring ~18-22 residues in an alpha-helix to span it. 16 residues (option C) is below the typical minimum, while 21 residues (option B) is squarely in the canonical range. Option D adds a second TM at 199-217; however, Ferlin-family proteins (recognizable by their C2 domain architecture visible in the long middle region of this ~1425-residue protein) are classically cytoplasmic proteins with at most a single C-terminal TM anchor, making a mid-chain second TM atypical. The hydrophobicity of the C-terminal segment is directly readable from the sequence, and the length criterion plus family-level knowledge of ferlin topology distinguish B from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) visually identify the hydrophobic C-terminal stretch, (2) apply the standard ~20-residue TM helix length to prefer B over C, (3) recognize that the N-terminal region in option A lacks hydrophobic character, and (4) use ferlin-family knowledge (single-pass, C-terminal TM anchor) to reject the multi-TM option D. These are all transferable inferences from sequence features and family-level biology."
  },
  "case_id": "transmembrane_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, 'by similarity') records a helical transmembrane region at positions 1404-1424. The sequence at these positions (TGVWMTVAGIIALVIFVMFLL) is predominantly hydrophobic (V, W, M, A, I, L, F dominate), consistent with a single-pass transmembrane alpha-helix at the C-terminus. While the evidence code indicates computational inference rather than experimental validation, the hydrophobic character of the sequence is directly observable and strongly supports the annotation."
  },
  "important_caveats": [
    "The UniProt transmembrane annotation carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational annotation rather than experimentally determined. However, the hydrophobicity of the sequence at 1404-1424 independently supports the assignment.",
    "The boundary between options B and C (21 vs 16 residues) is a minor precision issue; both describe the same TM region with slightly different boundaries. The 21-residue span is more consistent with canonical TM helix length.",
    "The protein is Toxoplasma gondii Ferlin 1 (FER1), a single-pass membrane protein with a C-terminal TM anchor, consistent with the ferlin family architecture."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both B (1404-1424) and C (1408-1423) describe overlapping hydrophobic segments in the C-terminal TM region. The distinction depends on whether one includes the marginally hydrophobic T-G-V-W residues at 1404-1407 and the final L at 1424. While 21 residues is the more standard TM length, 16 residues is not strictly impossible for a TM helix. However, the full hydrophobic extent clearly begins around 1404-1405, and the annotation supports the longer definition. This is a minor boundary ambiguity rather than a fundamental ambiguity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence code ECO:0000255, 'by similarity') records a helical transmembrane region at positions 1404-1424. The sequence at these positions (TGVWMTVAGIIALVIFVMFLL) is predominantly hydrophobic (V, W, M, A, I, L, F dominate), consistent with a single-pass transmembrane alpha-helix at the C-terminus. While the evidence code indicates computational inference rather than experimental validation, the hydrophobic character of the sequence is directly observable and strongly supports the annotation.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal 21 residues (positions ~1405-1425: TGVWMTVAGIIALVIFVMFLLK) form a clearly hydrophobic stretch at the extreme C-terminus, a hallmark of single-pass type-I membrane protein anchoring. Option A (35-55) falls in a polar/charged N-terminal region (PYIEVTVNGVTKTTIQKTQVV) with no hydrophobic character, easily eliminated. The critical distinction between B (1404-1424, 21 residues) and C (1408-1423, 16 residues) rests on standard TM helix geometry: the lipid bilayer hydrophobic core is ~30 Å, requiring ~18-22 residues in an alpha-helix to span it. 16 residues (option C) is below the typical minimum, while 21 residues (option B) is squarely in the canonical range. Option D adds a second TM at 199-217; however, Ferlin-family proteins (recognizable by their C2 domain architecture visible in the long middle region of this ~1425-residue protein) are classically cytoplasmic proteins with at most a single C-terminal TM anchor, making a mid-chain second TM atypical. The hydrophobicity of the C-terminal segment is directly readable from the sequence, and the length criterion plus family-level knowledge of ferlin topology distinguish B from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) visually identify the hydrophobic C-terminal stretch, (2) apply the standard ~20-residue TM helix length to prefer B over C, (3) recognize that the N-terminal region in option A lacks hydrophobic character, and (4) use ferlin-family knowledge (single-pass, C-terminal TM anchor) to reject the multi-TM option D. These are all transferable inferences from sequence features and family-level biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both B (1404-1424) and C (1408-1423) describe overlapping hydrophobic segments in the C-terminal TM region. The distinction depends on whether one includes the marginally hydrophobic T-G-V-W residues at 1404-1407 and the final L at 1424. While 21 residues is the more standard TM length, 16 residues is not strictly impossible for a TM helix. However, the full hydrophobic extent clearly begins around 1404-1405, and the annotation supports the longer definition. This is a minor boundary ambiguity rather than a fundamental ambiguity."
  },
  "important_caveats": [
    "The UniProt transmembrane annotation carries evidence code ECO:0000255 (inferred by similarity), meaning it is a computational annotation rather than experimentally determined. However, the hydrophobicity of the sequence at 1404-1424 independently supports the assignment.",
    "The boundary between options B and C (21 vs 16 residues) is a minor precision issue; both describe the same TM region with slightly different boundaries. The 21-residue span is more consistent with canonical TM helix length.",
    "The protein is Toxoplasma gondii Ferlin 1 (FER1), a single-pass membrane protein with a C-terminal TM anchor, consistent with the ferlin family architecture."
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
  "requested_accession": "A0A7J6JXB6",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "52e74cdb194f08163ff8762cfb045f3776dcaa62e2d92f292853eb1c2d7ca5a8",
  "benchmark_sequence_length": 1425,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 15,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2021-04-07",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "current_source_sequence_sha256": "52e74cdb194f08163ff8762cfb045f3776dcaa62e2d92f292853eb1c2d7ca5a8",
  "current_source_sequence_length": 1425,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 14,
  "selected_historical_version": {
    "accession": "A0A7J6JXB6",
    "database": "Swiss-Prot",
    "entryVersion": 14,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FER1_TOXGO",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896",
  "selected_historical_source_sequence_sha256": "52e74cdb194f08163ff8762cfb045f3776dcaa62e2d92f292853eb1c2d7ca5a8",
  "selected_historical_source_sequence_length": 1425,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 14,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A7J6JXB6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":15,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2021-04-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000557509\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Conoidasida\",\"Coccidia\",\"Eucoccidiorida\",\"Eimeriorina\",\"Sarcocystidae\",\"Toxoplasma\"],\"scientificName\":\"Toxoplasma gondii\",\"taxonId\":5811}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294204\",\"source\":\"PubMed\"}],\"value\":\"Ferlin 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294204\",\"source\":\"PubMed\"}],\"value\":\"FER1\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"value\":\"TgFER1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "json_pointer": "/features/1",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":1424},\"start\":{\"modifier\":\"EXACT\",\"value\":1404}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Tagoe D.N.A.\",\"Drozda A.A.\",\"Falco J.A.\",\"Bechtel T.J.\",\"Weerapana E.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33803212\"},{\"database\":\"DOI\",\"id\":\"10.3390/life11030217\"}],\"citationType\":\"journal article\",\"firstPage\":\"0\",\"id\":\"33803212\",\"journal\":\"Life\",\"lastPage\":\"0\",\"publicationDate\":\"2021\",\"title\":\"Ferlins and TgDOC2 in Toxoplasma Microneme, Rhoptry and Dense Granule Secretion.\",\"volume\":\"11\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33803212\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"RH\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7J6JXB6.json",
  "source_sha256": "d5befe804c26fab56edf39c586daba5f720cd241343442356618c084bd358d1d",
  "retrieved_utc": "2026-11-02T04:25:36.132368+00:00",
  "json_pointer": "/references/2",
  "excerpt": "{\"citation\":{\"authors\":[\"Tagoe D.N.A.\",\"Ribeiro E Silva A.\",\"Drozda A.A.\",\"Coppens I.\",\"Coleman B.I.\",\"Gubbels M.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39294204\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41598-024-72628-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"21819\",\"id\":\"39294204\",\"journal\":\"Sci. Rep.\",\"lastPage\":\"21819\",\"publicationDate\":\"2024\",\"title\":\"Toxoplasma FER1 is a versatile and dynamic mediator of differential microneme trafficking and microneme exocytosis.\",\"volume\":\"14\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39294204\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"RH\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"DISRUPTION PHENOTYPE\",\"PUTATIVE CA(2+)-BINDING RESIDUES\",\"MUTAGENESIS OF ASP-541; ASP-545 AND ASP-605\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14",
  "source_sha256": "11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896",
  "retrieved_utc": "2026-11-02T04:25:38.159549+00:00",
  "source_locator": "lines 1-13",
  "excerpt": "ID   FER1_TOXGO              Reviewed;        1425 AA.\nAC   A0A7J6JXB6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-APR-2021, sequence version 1.\nDT   28-JAN-2026, entry version 14.\nDE   RecName: Full=Ferlin 1 {ECO:0000303|PubMed:33803212, ECO:0000303|PubMed:39294204};\nDE            Short=FER1 {ECO:0000303|PubMed:33803212, ECO:0000303|PubMed:39294204};\nDE            Short=TgFER1 {ECO:0000303|PubMed:33803212};\nGN   ORFNames=TGRH88_049110 {ECO:0000312|EMBL:KAF4639140.1};\nOS   Toxoplasma gondii.\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Conoidasida; Coccidia;\nOC   Eucoccidiorida; Eimeriorina; Sarcocystidae; Toxoplasma.\nOX   NCBI_TaxID=5811 {ECO:0000312|Proteomes:UP000557509};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 14,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14",
  "source_sha256": "11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896",
  "retrieved_utc": "2026-11-02T04:25:38.159549+00:00",
  "source_locator": "lines 20-28",
  "excerpt": "RN   [2] {ECO:0000305}\nRP   FUNCTION.\nRC   STRAIN=RH {ECO:0000303|PubMed:33803212};\nRX   PubMed=33803212; DOI=10.3390/life11030217;\nRA   Tagoe D.N.A., Drozda A.A., Falco J.A., Bechtel T.J., Weerapana E.,\nRA   Gubbels M.J.;\nRT   \"Ferlins and TgDOC2 in Toxoplasma Microneme, Rhoptry and Dense Granule\nRT   Secretion.\";\nRL   Life 11:0-0(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 14,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14",
  "source_sha256": "11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896",
  "retrieved_utc": "2026-11-02T04:25:38.159549+00:00",
  "source_locator": "lines 29-38",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, SUBCELLULAR LOCATION, DISRUPTION PHENOTYPE, PUTATIVE\nRP   CA(2+)-BINDING RESIDUES, AND MUTAGENESIS OF ASP-541; ASP-545 AND ASP-605.\nRC   STRAIN=RH {ECO:0000303|PubMed:39294204};\nRX   PubMed=39294204; DOI=10.1038/s41598-024-72628-0;\nRA   Tagoe D.N.A., Ribeiro E Silva A., Drozda A.A., Coppens I., Coleman B.I.,\nRA   Gubbels M.J.;\nRT   \"Toxoplasma FER1 is a versatile and dynamic mediator of differential\nRT   microneme trafficking and microneme exocytosis.\";\nRL   Sci. Rep. 14:21819-21819(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 14,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A7J6JXB6?format=txt&versions=14",
  "source_sha256": "11d8ed5ec426735c426554897d60e1ea7c9e47e812c06d40cae5228ba7f46896",
  "retrieved_utc": "2026-11-02T04:25:38.159549+00:00",
  "source_locator": "lines 95-97",
  "excerpt": "FT   TRANSMEM        1404..1424\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 14,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 26. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
