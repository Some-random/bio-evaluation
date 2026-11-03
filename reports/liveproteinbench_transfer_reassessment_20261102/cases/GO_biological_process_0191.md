# GO_biological_process_0191: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/GO_biological_process_0191.txt)

**Task:** `GO_biological_process`  
**Author key, unchanged:** **D** — steroid metabolic process

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | contradicted | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | contradicted | lookup-dependent | usable output (valid_review) |
| after | GPT-6 Luna | contradicted | lookup-dependent | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MTRKSILVTGASSGLGYAAVQKLAENGFYVFAAVREIRGMFSNIKNIKELKLDLANEQSIEELFIYIEATQKDYPLWGLVNNAGICVPSPLELLREFDLRQQLDTNVIGQLLVTQFALPFIRKSKGRIINITSGLGSIAVPYLGAYSIAQFAKMAFTDVLRRELKHSGVTVSVVQPGAIYTPIWDKFLVTGQEILDNSLDEKRKIYERSFIEFLKASQIGVNSVKTTRNDFAKVILDIFKAEIPETHYYVGDDAKNFSNKSKILTVTEIDEWFDLQSPTESEFKKI

[Multiple Choices]
A. appressorium formation
B. oocyte localization involved in germarium-derived egg chamber formation
C. lipid metabolic process
D. steroid metabolic process
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

### Expected-answer support: contradicted

> The matched protein has an experimentally supported function in pyrrolizwilline alkaloid biosynthesis: it reduces a pyrrolizinone intermediate. That does not support steroid metabolism. The steroid-process annotation is present, but its evidence is computational (IEA:TreeGrafter), not experimental, and appears inconsistent with the reported substrate and pathway.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence offers no clear basis for identifying a steroid-metabolizing enzyme rather than an enzyme in another small-molecule pathway; the choices do not disclose its substrate or pathway.


**Missing item-specific fact**

> The protein-specific substrate and pathway, or a GO annotation for this sequence, would be needed to choose among the metabolic options.


**Reason**

> Choosing D depends on an item-specific annotation or functional fact absent from the input. The sequence alone does not meaningfully distinguish steroid metabolism from other metabolism, and the available specific functional evidence does not support D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The supplied GO annotation assigns D, and the ontology places steroid metabolic process under lipid metabolic process, so C is also a broader term entailed by that annotation. However, the experimentally reported pathway supports neither option as a description of this enzyme's demonstrated function.


### Important caveats

- The sequence matches the protein in the reviewer-only UniProt evidence, including the historical record.
- The D annotation is computational; the cited function is supported by experimental evidence, though the primary paper was not independently reviewed here.
- Pyrrolizwilline is described as an alkaloid, not a steroid.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence offers no clear basis for identifying a steroid-metabolizing enzyme rather than an enzyme in another small-molecule pathway; the choices do not disclose its substrate or pathway.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific substrate and pathway, or a GO annotation for this sequence, would be needed to choose among the metabolic options.",
    "reason": "Choosing D depends on an item-specific annotation or functional fact absent from the input. The sequence alone does not meaningfully distinguish steroid metabolism from other metabolism, and the available specific functional evidence does not support D."
  },
  "case_id": "GO_biological_process_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "contradicted",
    "reason": "The matched protein has an experimentally supported function in pyrrolizwilline alkaloid biosynthesis: it reduces a pyrrolizinone intermediate. That does not support steroid metabolism. The steroid-process annotation is present, but its evidence is computational (IEA:TreeGrafter), not experimental, and appears inconsistent with the reported substrate and pathway."
  },
  "important_caveats": [
    "The sequence matches the protein in the reviewer-only UniProt evidence, including the historical record.",
    "The D annotation is computational; the cited function is supported by experimental evidence, though the primary paper was not independently reviewed here.",
    "Pyrrolizwilline is described as an alkaloid, not a steroid."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The supplied GO annotation assigns D, and the ontology places steroid metabolic process under lipid metabolic process, so C is also a broader term entailed by that annotation. However, the experimentally reported pathway supports neither option as a description of this enzyme's demonstrated function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0191",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The matched protein has an experimentally supported function in pyrrolizwilline alkaloid biosynthesis: it reduces a pyrrolizinone intermediate. That does not support steroid metabolism. The steroid-process annotation is present, but its evidence is computational (IEA:TreeGrafter), not experimental, and appears inconsistent with the reported substrate and pathway.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence offers no clear basis for identifying a steroid-metabolizing enzyme rather than an enzyme in another small-molecule pathway; the choices do not disclose its substrate or pathway.",
    "missing_item_specific_fact": "The protein-specific substrate and pathway, or a GO annotation for this sequence, would be needed to choose among the metabolic options.",
    "reason": "Choosing D depends on an item-specific annotation or functional fact absent from the input. The sequence alone does not meaningfully distinguish steroid metabolism from other metabolism, and the available specific functional evidence does not support D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The supplied GO annotation assigns D, and the ontology places steroid metabolic process under lipid metabolic process, so C is also a broader term entailed by that annotation. However, the experimentally reported pathway supports neither option as a description of this enzyme's demonstrated function."
  },
  "important_caveats": [
    "The sequence matches the protein in the reviewer-only UniProt evidence, including the historical record.",
    "The D annotation is computational; the cited function is supported by experimental evidence, though the primary paper was not independently reviewed here.",
    "Pyrrolizwilline is described as an alkaloid, not a steroid."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> The GO:0008202 'steroid metabolic process' annotation (C6, H4) carries only evidence code IEA:TreeGrafter — a purely computational sequence-similarity transfer, not experimental evidence. The experimental characterization (ECO:0000269, PubMed:39428351; C5, H3) explicitly states the protein 'catalyzes the reduction of 3-amino-tetrahydro-pyrrolizinone to 3-amino-tetrahydro-pyrrolizinol' as part of 'the biosynthetic pathway of pyrrolizwilline, a pyrrolizidine alkaloid.' Pyrrolizidine alkaloids contain a fused pyrrolizidine ring system (two five-membered N-containing rings), not the cyclopentanoperhydrophenanthrene nucleus required by the GO:0008202 definition (GO2). The TreeGrafter annotation appears to be a false positive from oxidoreductase-family similarity and is contradicted by the primary experimental data.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence (286 aa, N-terminal Rossmann-like motif 'TGASSGLGY') suggests an NAD(P)-dependent oxidoreductase, which is broadly consistent with metabolic processes. Options A (appressorium formation) and B (oocyte localization) are eukaryotic/fungal processes irrelevant to a bacterial protein, so they can be eliminated by general knowledge. However, distinguishing C (lipid metabolic process, GO:0006629) from D (steroid metabolic process, GO:0008202) requires knowing the specific substrate class. No sequence motif in the provided 286-aa sequence identifies a steroid nucleus or a lipid substrate. The actual substrate (3-amino-tetrahydro-pyrrolizinone, a pyrrolizidine alkaloid) fits neither C nor D, so no sequence-based argument can favor D over C.


**Missing item-specific fact**

> The specific UniProt GO annotation GO:0008202 (IEA:TreeGrafter) for this exact accession, or equivalently knowledge that TreeGrafter assigned this protein to the steroid-metabolism branch — an item-specific database lookup with no sequence-level justification.


**Reason**

> Eliminating A and B uses general biology (bacterial protein cannot form appressoria or localize oocytes). Choosing between C and D requires the specific database annotation, which is itself a computational inference likely incorrect. No motif, domain architecture, or catalytic-residue pattern in the supplied sequence distinguishes steroid from lipid metabolism.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> GO:0008202 (steroid metabolic process) is_a GO:0006629 (lipid metabolic process) per GO2. If D were accepted as the annotation, C is automatically true as the parent term, making both defensible under standard GO semantics. More fundamentally, the experimentally verified function (pyrrolizidine alkaloid biosynthesis) matches neither C nor D, so the 'correct' answer rests entirely on a likely-erroneous IEA annotation.


### Important caveats

- The only GO:0008202 annotation is IEA:TreeGrafter (automated, not curated or experimental); the experimental evidence (ECO:0000269) describes pyrrolizidine alkaloid biosynthesis, not steroid metabolism.
- Pyrrolizidine alkaloids are not steroids (no cyclopentanoperhydrophenanthrene nucleus) and are not lipids; neither C nor D accurately describes the protein's verified biological role.
- The identity of the protein (UniProt A0A2G0QDN4) was inferred reviewer-only from dataset metadata; the evaluated model received only the raw 286-aa sequence.
- The benchmark ontology snapshot may differ from the current GO release, though the steroid/lipid is_a relationship is long-standing.
- The question's expected answer relies on a database annotation that the primary literature contradicts, raising concerns about benchmark key validity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (286 aa, N-terminal Rossmann-like motif 'TGASSGLGY') suggests an NAD(P)-dependent oxidoreductase, which is broadly consistent with metabolic processes. Options A (appressorium formation) and B (oocyte localization) are eukaryotic/fungal processes irrelevant to a bacterial protein, so they can be eliminated by general knowledge. However, distinguishing C (lipid metabolic process, GO:0006629) from D (steroid metabolic process, GO:0008202) requires knowing the specific substrate class. No sequence motif in the provided 286-aa sequence identifies a steroid nucleus or a lipid substrate. The actual substrate (3-amino-tetrahydro-pyrrolizinone, a pyrrolizidine alkaloid) fits neither C nor D, so no sequence-based argument can favor D over C.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific UniProt GO annotation GO:0008202 (IEA:TreeGrafter) for this exact accession, or equivalently knowledge that TreeGrafter assigned this protein to the steroid-metabolism branch — an item-specific database lookup with no sequence-level justification.",
    "reason": "Eliminating A and B uses general biology (bacterial protein cannot form appressoria or localize oocytes). Choosing between C and D requires the specific database annotation, which is itself a computational inference likely incorrect. No motif, domain architecture, or catalytic-residue pattern in the supplied sequence distinguishes steroid from lipid metabolism."
  },
  "case_id": "GO_biological_process_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "GO2"
    ],
    "judgment": "contradicted",
    "reason": "The GO:0008202 'steroid metabolic process' annotation (C6, H4) carries only evidence code IEA:TreeGrafter — a purely computational sequence-similarity transfer, not experimental evidence. The experimental characterization (ECO:0000269, PubMed:39428351; C5, H3) explicitly states the protein 'catalyzes the reduction of 3-amino-tetrahydro-pyrrolizinone to 3-amino-tetrahydro-pyrrolizinol' as part of 'the biosynthetic pathway of pyrrolizwilline, a pyrrolizidine alkaloid.' Pyrrolizidine alkaloids contain a fused pyrrolizidine ring system (two five-membered N-containing rings), not the cyclopentanoperhydrophenanthrene nucleus required by the GO:0008202 definition (GO2). The TreeGrafter annotation appears to be a false positive from oxidoreductase-family similarity and is contradicted by the primary experimental data."
  },
  "important_caveats": [
    "The only GO:0008202 annotation is IEA:TreeGrafter (automated, not curated or experimental); the experimental evidence (ECO:0000269) describes pyrrolizidine alkaloid biosynthesis, not steroid metabolism.",
    "Pyrrolizidine alkaloids are not steroids (no cyclopentanoperhydrophenanthrene nucleus) and are not lipids; neither C nor D accurately describes the protein's verified biological role.",
    "The identity of the protein (UniProt A0A2G0QDN4) was inferred reviewer-only from dataset metadata; the evaluated model received only the raw 286-aa sequence.",
    "The benchmark ontology snapshot may differ from the current GO release, though the steroid/lipid is_a relationship is long-standing.",
    "The question's expected answer relies on a database annotation that the primary literature contradicts, raising concerns about benchmark key validity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "GO:0008202 (steroid metabolic process) is_a GO:0006629 (lipid metabolic process) per GO2. If D were accepted as the annotation, C is automatically true as the parent term, making both defensible under standard GO semantics. More fundamentally, the experimentally verified function (pyrrolizidine alkaloid biosynthesis) matches neither C nor D, so the 'correct' answer rests entirely on a likely-erroneous IEA annotation."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0191",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The GO:0008202 'steroid metabolic process' annotation (C6, H4) carries only evidence code IEA:TreeGrafter — a purely computational sequence-similarity transfer, not experimental evidence. The experimental characterization (ECO:0000269, PubMed:39428351; C5, H3) explicitly states the protein 'catalyzes the reduction of 3-amino-tetrahydro-pyrrolizinone to 3-amino-tetrahydro-pyrrolizinol' as part of 'the biosynthetic pathway of pyrrolizwilline, a pyrrolizidine alkaloid.' Pyrrolizidine alkaloids contain a fused pyrrolizidine ring system (two five-membered N-containing rings), not the cyclopentanoperhydrophenanthrene nucleus required by the GO:0008202 definition (GO2). The TreeGrafter annotation appears to be a false positive from oxidoreductase-family similarity and is contradicted by the primary experimental data.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence (286 aa, N-terminal Rossmann-like motif 'TGASSGLGY') suggests an NAD(P)-dependent oxidoreductase, which is broadly consistent with metabolic processes. Options A (appressorium formation) and B (oocyte localization) are eukaryotic/fungal processes irrelevant to a bacterial protein, so they can be eliminated by general knowledge. However, distinguishing C (lipid metabolic process, GO:0006629) from D (steroid metabolic process, GO:0008202) requires knowing the specific substrate class. No sequence motif in the provided 286-aa sequence identifies a steroid nucleus or a lipid substrate. The actual substrate (3-amino-tetrahydro-pyrrolizinone, a pyrrolizidine alkaloid) fits neither C nor D, so no sequence-based argument can favor D over C.",
    "missing_item_specific_fact": "The specific UniProt GO annotation GO:0008202 (IEA:TreeGrafter) for this exact accession, or equivalently knowledge that TreeGrafter assigned this protein to the steroid-metabolism branch — an item-specific database lookup with no sequence-level justification.",
    "reason": "Eliminating A and B uses general biology (bacterial protein cannot form appressoria or localize oocytes). Choosing between C and D requires the specific database annotation, which is itself a computational inference likely incorrect. No motif, domain architecture, or catalytic-residue pattern in the supplied sequence distinguishes steroid from lipid metabolism."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "GO:0008202 (steroid metabolic process) is_a GO:0006629 (lipid metabolic process) per GO2. If D were accepted as the annotation, C is automatically true as the parent term, making both defensible under standard GO semantics. More fundamentally, the experimentally verified function (pyrrolizidine alkaloid biosynthesis) matches neither C nor D, so the 'correct' answer rests entirely on a likely-erroneous IEA annotation."
  },
  "important_caveats": [
    "The only GO:0008202 annotation is IEA:TreeGrafter (automated, not curated or experimental); the experimental evidence (ECO:0000269) describes pyrrolizidine alkaloid biosynthesis, not steroid metabolism.",
    "Pyrrolizidine alkaloids are not steroids (no cyclopentanoperhydrophenanthrene nucleus) and are not lipids; neither C nor D accurately describes the protein's verified biological role.",
    "The identity of the protein (UniProt A0A2G0QDN4) was inferred reviewer-only from dataset metadata; the evaluated model received only the raw 286-aa sequence.",
    "The benchmark ontology snapshot may differ from the current GO release, though the steroid/lipid is_a relationship is long-standing.",
    "The question's expected answer relies on a database annotation that the primary literature contradicts, raising concerns about benchmark key validity."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: contradicted

> The matched sequence is experimentally annotated as a reductase in pyrrolizwilline alkaloid biosynthesis, acting on a pyrrolizinone intermediate, not as a steroid-metabolism enzyme. The steroid-process annotation is explicitly computational (IEA:TreeGrafter), so it does not outweigh the substrate-specific function evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has features consistent with an oxidoreductase, but that broad enzyme class does not identify its substrate or distinguish steroid metabolism from other metabolic chemistry. The eukaryote-specific alternatives are poor fits for a standalone enzyme-like sequence, but transferable general knowledge does not establish either lipid or steroid metabolism.


**Missing item-specific fact**

> The exact enzyme's substrate and pathway assignment—reduction of a pyrrolizidine-alkaloid intermediate in pyrrolizwilline biosynthesis—is needed to recognize that the listed steroid and lipid processes do not describe its characterized role.


**Reason**

> No clear sequence feature in the supplied input specifies steroid substrates or a steroid pathway, and the sequence alone provides no meaningful basis for selecting D over the broader metabolic distractor C. Recognizing the exact protein's experimentally characterized role would require item-specific information; the reviewer-only annotation cannot be treated as original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The characterized alkaloid-biosynthesis process is not among the choices. Although steroid metabolism is an ontology subclass of lipid metabolism, the evidence does not establish that this enzyme participates in either process.


### Important caveats

- The sequence matches the cited UniProt record, but the author’s exact source snapshot is unknown.
- The steroid-process annotation is computational; the functional evidence cited for the enzyme is experimental.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has features consistent with an oxidoreductase, but that broad enzyme class does not identify its substrate or distinguish steroid metabolism from other metabolic chemistry. The eukaryote-specific alternatives are poor fits for a standalone enzyme-like sequence, but transferable general knowledge does not establish either lipid or steroid metabolism.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact enzyme's substrate and pathway assignment—reduction of a pyrrolizidine-alkaloid intermediate in pyrrolizwilline biosynthesis—is needed to recognize that the listed steroid and lipid processes do not describe its characterized role.",
    "reason": "No clear sequence feature in the supplied input specifies steroid substrates or a steroid pathway, and the sequence alone provides no meaningful basis for selecting D over the broader metabolic distractor C. Recognizing the exact protein's experimentally characterized role would require item-specific information; the reviewer-only annotation cannot be treated as original input."
  },
  "case_id": "GO_biological_process_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "contradicted",
    "reason": "The matched sequence is experimentally annotated as a reductase in pyrrolizwilline alkaloid biosynthesis, acting on a pyrrolizinone intermediate, not as a steroid-metabolism enzyme. The steroid-process annotation is explicitly computational (IEA:TreeGrafter), so it does not outweigh the substrate-specific function evidence."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the author’s exact source snapshot is unknown.",
    "The steroid-process annotation is computational; the functional evidence cited for the enzyme is experimental."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The characterized alkaloid-biosynthesis process is not among the choices. Although steroid metabolism is an ontology subclass of lipid metabolism, the evidence does not establish that this enzyme participates in either process."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0191",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The matched sequence is experimentally annotated as a reductase in pyrrolizwilline alkaloid biosynthesis, acting on a pyrrolizinone intermediate, not as a steroid-metabolism enzyme. The steroid-process annotation is explicitly computational (IEA:TreeGrafter), so it does not outweigh the substrate-specific function evidence.",
    "evidence_ids": ["C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has features consistent with an oxidoreductase, but that broad enzyme class does not identify its substrate or distinguish steroid metabolism from other metabolic chemistry. The eukaryote-specific alternatives are poor fits for a standalone enzyme-like sequence, but transferable general knowledge does not establish either lipid or steroid metabolism.",
    "missing_item_specific_fact": "The exact enzyme's substrate and pathway assignment—reduction of a pyrrolizidine-alkaloid intermediate in pyrrolizwilline biosynthesis—is needed to recognize that the listed steroid and lipid processes do not describe its characterized role.",
    "reason": "No clear sequence feature in the supplied input specifies steroid substrates or a steroid pathway, and the sequence alone provides no meaningful basis for selecting D over the broader metabolic distractor C. Recognizing the exact protein's experimentally characterized role would require item-specific information; the reviewer-only annotation cannot be treated as original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The characterized alkaloid-biosynthesis process is not among the choices. Although steroid metabolism is an ontology subclass of lipid metabolism, the evidence does not establish that this enzyme participates in either process."
  },
  "important_caveats": [
    "The sequence matches the cited UniProt record, but the author’s exact source snapshot is unknown.",
    "The steroid-process annotation is computational; the functional evidence cited for the enzyme is experimental."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (A0A2G0QDN4) contains the GO annotation GO:0008202 (steroid metabolic process), which matches option D exactly. However, this annotation carries evidence code IEA:TreeGrafter, indicating it was assigned by automated similarity-based inference rather than experimental evidence. The actual experimental evidence (PubMed:39428351) describes the protein's function as involvement in pyrrolizidine alkaloid biosynthesis (reduction of 3-amino-tetrahydro-pyrrolizinone to 3-amino-tetrahydro-pyrrolizinol), which is NOT steroid metabolism (GO:0008202 requires a 1,2-cyclopentanoperhydrophenanthrene nucleus per the ontology definition). The annotation is present in the database and thus 'supported' in the narrow sense of database annotation, but is scientifically questionable given the actual characterized function.

Citations as saved: [C6](#evidence-c6), [C4](#evidence-c4), [C5](#evidence-c5), [GO2](#evidence-go2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The specific IEA:TreeGrafter annotation of GO:0008202 for this exact protein. The actual experimentally-verified function (pyrrolizidine alkaloid biosynthesis, EC 1.1.-.-) matches neither 'lipid metabolic process' (C) nor 'steroid metabolic process' (D) in a mechanistically specific way. The protein is an oxidoreductase with possible SDR-family features (Rossmann-like TGASSGLGY motif, ~286 aa length), but the SDR superfamily is enormously diverse and includes enzymes metabolizing steroids, sugars, alcohols, and many other substrates. Sequence-level SDR features do not reliably distinguish steroid-metabolizing members from non-steroid members without detailed subfamily assignment, which for this recently characterized (2024) alkaloid biosynthesis enzyme does not map to a steroid-metabolizing subfamily.


**Reason**

> Options A (appressorium formation, fungal) and B (oocyte localization, animal developmental) can be eliminated as irrelevant to a bacterial oxidoreductase. The critical distinction is between C (lipid metabolic process) and D (steroid metabolic process). Since GO:0008202 is_a GO:0006629, if D is correct then C is also technically true as a parent term. The actual protein function (pyrrolizidine alkaloid biosynthesis) is not steroid metabolism and is only loosely related to lipid metabolism. The database annotation assigning D is an automated inference (IEA:TreeGrafter) that appears to be a mis-assignment based on general oxidoreductase similarity. Transferable knowledge about SDR/oxidoreductase families does not reliably point to steroid metabolism for this specific protein, as the SDR superfamily encompasses many non-steroid functions. Distinguishing C from D requires knowing the specific database annotation for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> GO:0008202 (steroid metabolic process, option D) is_a GO:0006629 (lipid metabolic process, option C) per the ontology hierarchy. If D is the annotated answer, C is also technically true as the parent term. The question asks for the 'primary biological process' which conventionally means the most specific annotation, but a model could reasonably argue C is correct (or at least not wrong) since the actual function (alkaloid biosynthesis) is more accurately described as a general metabolic/lipid-related process than specifically as steroid metabolism. Additionally, the actual function (pyrrolizidine alkaloid biosynthesis) matches neither C nor D mechanistically, making both choices defensible as 'closest available' options.


### Important caveats

- The GO:0008202 annotation is IEA:TreeGrafter (automated inference), not experimental. The experimentally verified function (PubMed:39428351) is pyrrolizidine alkaloid biosynthesis, which does not involve a steroid nucleus.
- The protein was characterized in 2024; the benchmark may have used an earlier annotation snapshot where the function was unknown and only the automated GO assignment existed.
- The protein sequence shows possible SDR/oxidoreductase family features, but family-level knowledge does not reliably distinguish steroid-metabolizing from non-steroid-metabolizing members of this large superfamily.
- Options A and B are clearly irrelevant (fungal and animal developmental processes for a bacterial oxidoreductase), making the effective choice a binary between C and D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific IEA:TreeGrafter annotation of GO:0008202 for this exact protein. The actual experimentally-verified function (pyrrolizidine alkaloid biosynthesis, EC 1.1.-.-) matches neither 'lipid metabolic process' (C) nor 'steroid metabolic process' (D) in a mechanistically specific way. The protein is an oxidoreductase with possible SDR-family features (Rossmann-like TGASSGLGY motif, ~286 aa length), but the SDR superfamily is enormously diverse and includes enzymes metabolizing steroids, sugars, alcohols, and many other substrates. Sequence-level SDR features do not reliably distinguish steroid-metabolizing members from non-steroid members without detailed subfamily assignment, which for this recently characterized (2024) alkaloid biosynthesis enzyme does not map to a steroid-metabolizing subfamily.",
    "reason": "Options A (appressorium formation, fungal) and B (oocyte localization, animal developmental) can be eliminated as irrelevant to a bacterial oxidoreductase. The critical distinction is between C (lipid metabolic process) and D (steroid metabolic process). Since GO:0008202 is_a GO:0006629, if D is correct then C is also technically true as a parent term. The actual protein function (pyrrolizidine alkaloid biosynthesis) is not steroid metabolism and is only loosely related to lipid metabolism. The database annotation assigning D is an automated inference (IEA:TreeGrafter) that appears to be a mis-assignment based on general oxidoreductase similarity. Transferable knowledge about SDR/oxidoreductase families does not reliably point to steroid metabolism for this specific protein, as the SDR superfamily encompasses many non-steroid functions. Distinguishing C from D requires knowing the specific database annotation for this protein."
  },
  "case_id": "GO_biological_process_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "C6",
      "C4",
      "C5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (A0A2G0QDN4) contains the GO annotation GO:0008202 (steroid metabolic process), which matches option D exactly. However, this annotation carries evidence code IEA:TreeGrafter, indicating it was assigned by automated similarity-based inference rather than experimental evidence. The actual experimental evidence (PubMed:39428351) describes the protein's function as involvement in pyrrolizidine alkaloid biosynthesis (reduction of 3-amino-tetrahydro-pyrrolizinone to 3-amino-tetrahydro-pyrrolizinol), which is NOT steroid metabolism (GO:0008202 requires a 1,2-cyclopentanoperhydrophenanthrene nucleus per the ontology definition). The annotation is present in the database and thus 'supported' in the narrow sense of database annotation, but is scientifically questionable given the actual characterized function."
  },
  "important_caveats": [
    "The GO:0008202 annotation is IEA:TreeGrafter (automated inference), not experimental. The experimentally verified function (PubMed:39428351) is pyrrolizidine alkaloid biosynthesis, which does not involve a steroid nucleus.",
    "The protein was characterized in 2024; the benchmark may have used an earlier annotation snapshot where the function was unknown and only the automated GO assignment existed.",
    "The protein sequence shows possible SDR/oxidoreductase family features, but family-level knowledge does not reliably distinguish steroid-metabolizing from non-steroid-metabolizing members of this large superfamily.",
    "Options A and B are clearly irrelevant (fungal and animal developmental processes for a bacterial oxidoreductase), making the effective choice a binary between C and D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "GO:0008202 (steroid metabolic process, option D) is_a GO:0006629 (lipid metabolic process, option C) per the ontology hierarchy. If D is the annotated answer, C is also technically true as the parent term. The question asks for the 'primary biological process' which conventionally means the most specific annotation, but a model could reasonably argue C is correct (or at least not wrong) since the actual function (alkaloid biosynthesis) is more accurately described as a general metabolic/lipid-related process than specifically as steroid metabolism. Additionally, the actual function (pyrrolizidine alkaloid biosynthesis) matches neither C nor D mechanistically, making both choices defensible as 'closest available' options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0191",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (A0A2G0QDN4) contains the GO annotation GO:0008202 (steroid metabolic process), which matches option D exactly. However, this annotation carries evidence code IEA:TreeGrafter, indicating it was assigned by automated similarity-based inference rather than experimental evidence. The actual experimental evidence (PubMed:39428351) describes the protein's function as involvement in pyrrolizidine alkaloid biosynthesis (reduction of 3-amino-tetrahydro-pyrrolizinone to 3-amino-tetrahydro-pyrrolizinol), which is NOT steroid metabolism (GO:0008202 requires a 1,2-cyclopentanoperhydrophenanthrene nucleus per the ontology definition). The annotation is present in the database and thus 'supported' in the narrow sense of database annotation, but is scientifically questionable given the actual characterized function.",
    "evidence_ids": ["C6", "C4", "C5", "GO2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The specific IEA:TreeGrafter annotation of GO:0008202 for this exact protein. The actual experimentally-verified function (pyrrolizidine alkaloid biosynthesis, EC 1.1.-.-) matches neither 'lipid metabolic process' (C) nor 'steroid metabolic process' (D) in a mechanistically specific way. The protein is an oxidoreductase with possible SDR-family features (Rossmann-like TGASSGLGY motif, ~286 aa length), but the SDR superfamily is enormously diverse and includes enzymes metabolizing steroids, sugars, alcohols, and many other substrates. Sequence-level SDR features do not reliably distinguish steroid-metabolizing members from non-steroid members without detailed subfamily assignment, which for this recently characterized (2024) alkaloid biosynthesis enzyme does not map to a steroid-metabolizing subfamily.",
    "reason": "Options A (appressorium formation, fungal) and B (oocyte localization, animal developmental) can be eliminated as irrelevant to a bacterial oxidoreductase. The critical distinction is between C (lipid metabolic process) and D (steroid metabolic process). Since GO:0008202 is_a GO:0006629, if D is correct then C is also technically true as a parent term. The actual protein function (pyrrolizidine alkaloid biosynthesis) is not steroid metabolism and is only loosely related to lipid metabolism. The database annotation assigning D is an automated inference (IEA:TreeGrafter) that appears to be a mis-assignment based on general oxidoreductase similarity. Transferable knowledge about SDR/oxidoreductase families does not reliably point to steroid metabolism for this specific protein, as the SDR superfamily encompasses many non-steroid functions. Distinguishing C from D requires knowing the specific database annotation for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "GO:0008202 (steroid metabolic process, option D) is_a GO:0006629 (lipid metabolic process, option C) per the ontology hierarchy. If D is the annotated answer, C is also technically true as the parent term. The question asks for the 'primary biological process' which conventionally means the most specific annotation, but a model could reasonably argue C is correct (or at least not wrong) since the actual function (alkaloid biosynthesis) is more accurately described as a general metabolic/lipid-related process than specifically as steroid metabolism. Additionally, the actual function (pyrrolizidine alkaloid biosynthesis) matches neither C nor D mechanistically, making both choices defensible as 'closest available' options."
  },
  "important_caveats": [
    "The GO:0008202 annotation is IEA:TreeGrafter (automated inference), not experimental. The experimentally verified function (PubMed:39428351) is pyrrolizidine alkaloid biosynthesis, which does not involve a steroid nucleus.",
    "The protein was characterized in 2024; the benchmark may have used an earlier annotation snapshot where the function was unknown and only the automated GO assignment existed.",
    "The protein sequence shows possible SDR/oxidoreductase family features, but family-level knowledge does not reliably distinguish steroid-metabolizing from non-steroid-metabolizing members of this large superfamily.",
    "Options A and B are clearly irrelevant (fungal and animal developmental processes for a bacterial oxidoreductase), making the effective choice a binary between C and D."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

### Source check 1

**Check:** `mixed_annotations_require_qualification`.

> C5/H3 describe pyrrolizwilline alkaloid biosynthesis and pyrrolizinone reduction with ECO:0000269; C6/H4 separately carry the keyed steroid-metabolism term as IEA:TreeGrafter.

**Remaining uncertainty:** The mismatch is real at the annotation-description level; possible additional substrate/pathway roles remain untested in these excerpts.

Evidence checked: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "A0A2G0QDN4",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "5ac667f5b9af33314dc3039989b8675644797300210825d6858552c1a9de52cb",
  "benchmark_sequence_length": 286,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 30,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-01-31",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "current_source_sequence_sha256": "5ac667f5b9af33314dc3039989b8675644797300210825d6858552c1a9de52cb",
  "current_source_sequence_length": 286,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 28,
  "selected_historical_version": {
    "accession": "A0A2G0QDN4",
    "database": "Swiss-Prot",
    "entryVersion": 28,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "XHPD_XENHO",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29",
  "selected_historical_source_sequence_sha256": "5ac667f5b9af33314dc3039989b8675644797300210825d6858552c1a9de52cb",
  "selected_historical_source_sequence_length": 286,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 28,
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json",
  "source_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "retrieved_utc": "2026-11-02T04:24:47.620054+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A2G0QDN4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json",
  "source_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "retrieved_utc": "2026-11-02T04:24:47.620054+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":30,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-01-31\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json",
  "source_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "retrieved_utc": "2026-11-02T04:24:47.620054+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Morganellaceae\",\"Xenorhabdus\"],\"scientificName\":\"Xenorhabdus hominickii\",\"taxonId\":351679}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json",
  "source_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "retrieved_utc": "2026-11-02T04:24:47.620054+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"value\":\"1.1.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"value\":\"3-amino-tetrahydro-pyrrolizinone reductase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json",
  "source_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "retrieved_utc": "2026-11-02T04:24:47.620054+00:00",
  "json_pointer": "/comments/0",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39428351\",\"source\":\"PubMed\"}],\"value\":\"Involved in the biosynthetic pathway of pyrrolizwilline, a pyrrolizidine alkaloid. Catalyzes the reduction of 3-amino-tetrahydro-pyrrolizinone to 3-amino-tetrahydro-pyrrolizinol\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json",
  "source_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "retrieved_utc": "2026-11-02T04:24:47.620054+00:00",
  "json_pointer": "/uniProtKBCrossReferences/7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0008202\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:steroid metabolic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json)

```json
{
  "evidence_id": "C7",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A2G0QDN4.json",
  "source_sha256": "5510f043b076696b57f87efa7739b48cfedb1b8f19f87a14fd6d5a4d3624e099",
  "retrieved_utc": "2026-11-02T04:24:47.620054+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Effert J.\",\"Westphalen M.\",\"Calderari A.\",\"Shi Y.M.\",\"Elamri I.\",\"Najah S.\",\"Gruen P.\",\"Li Y.\",\"Gruez A.\",\"Weissman K.J.\",\"Bode H.B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39428351\"},{\"database\":\"DOI\",\"id\":\"10.1002/anie.202411258\"}],\"citationType\":\"journal article\",\"firstPage\":\"e202411258\",\"id\":\"39428351\",\"journal\":\"Angew. Chem. Int. Ed.\",\"lastPage\":\"e202411258\",\"publicationDate\":\"2024\",\"title\":\"Pyrrolizwilline, a unique bacterial alkaloid assembled by a nonribosomal peptide synthetase and non-enzymatic dimerization.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 17903 / CIP 109072 / KE01\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28",
  "source_sha256": "e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29",
  "retrieved_utc": "2026-11-02T04:24:49.959850+00:00",
  "source_locator": "lines 1-12",
  "excerpt": "ID   XHPD_XENHO              Reviewed;         286 AA.\nAC   A0A2G0QDN4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   31-JAN-2018, sequence version 1.\nDT   28-JAN-2026, entry version 28.\nDE   RecName: Full=3-amino-tetrahydro-pyrrolizinone reductase {ECO:0000305|PubMed:39428351};\nDE            EC=1.1.-.- {ECO:0000269|PubMed:39428351};\nGN   Name=xhpD; ORFNames=Xhom_00313 {ECO:0000312|EMBL:PHM57347.1};\nOS   Xenorhabdus hominickii.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Morganellaceae; Xenorhabdus.\nOX   NCBI_TaxID=351679;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28",
  "source_sha256": "e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29",
  "retrieved_utc": "2026-11-02T04:24:49.959850+00:00",
  "source_locator": "lines 23-31",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRC   STRAIN=DSM 17903 / CIP 109072 / KE01;\nRX   PubMed=39428351; DOI=10.1002/anie.202411258;\nRA   Effert J., Westphalen M., Calderari A., Shi Y.M., Elamri I., Najah S.,\nRA   Gruen P., Li Y., Gruez A., Weissman K.J., Bode H.B.;\nRT   \"Pyrrolizwilline, a unique bacterial alkaloid assembled by a nonribosomal\nRT   peptide synthetase and non-enzymatic dimerization.\";\nRL   Angew. Chem. Int. Ed. 63:e202411258-e202411258(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28",
  "source_sha256": "e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29",
  "retrieved_utc": "2026-11-02T04:24:49.959850+00:00",
  "source_locator": "lines 32-35",
  "excerpt": "CC   -!- FUNCTION: Involved in the biosynthetic pathway of pyrrolizwilline, a\nCC       pyrrolizidine alkaloid. Catalyzes the reduction of 3-amino-tetrahydro-\nCC       pyrrolizinone to 3-amino-tetrahydro-pyrrolizinol.\nCC       {ECO:0000269|PubMed:39428351}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A2G0QDN4?format=txt&versions=28",
  "source_sha256": "e9a43167d987f4d30c210cf3857bc305e9fa0ec071e154f20f0d529315825c29",
  "retrieved_utc": "2026-11-02T04:24:49.959850+00:00",
  "source_locator": "lines 58-58",
  "excerpt": "DR   GO; GO:0008202; P:steroid metabolic process; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 28,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 68491-68515",
  "excerpt": "[Term]\nid: GO:0006629\nname: lipid metabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways involving lipids, compounds soluble in an organic solvent but not, or sparingly, in an aqueous solvent. Includes fatty acids; neutral fats, other fatty-acid esters, and soaps; long-chain (fatty) alcohols and waxes; sphingoids and other long-chain bases; glycolipids, phospholipids and sphingolipids; and carotenes, polyprenols, sterols, terpenes and other isoprenoids.\" [GOC:ma]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_pombe\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"lipid metabolism\" EXACT []\nxref: Reactome:R-HSA-556833 \"Metabolism of lipids\"\nxref: Wikipedia:Lipid_metabolism\nis_a: GO:0044238 ! primary metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0006629"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 80627-80636",
  "excerpt": "[Term]\nid: GO:0008202\nname: steroid metabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways involving steroids, compounds with a 1,2,cyclopentanoperhydrophenanthrene nucleus.\" [ISBN:0198547684]\nsynonym: \"steroid metabolism\" EXACT []\nxref: Reactome:R-HSA-8957322 \"Metabolism of steroids\"\nxref: Wikipedia:Steroid_metabolism\nis_a: GO:0006629 ! lipid metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0008202"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 168846-168861",
  "excerpt": "[Term]\nid: GO:0030720\nname: oocyte localization involved in germarium-derived egg chamber formation\nnamespace: biological_process\ndef: \"Directed movement of the oocyte, following its specification, from its original central position in the cyst to a posterior position relative to the nurse cells of the egg chamber, and its maintenance in this posterior location. This is the first sign of anterior-posterior asymmetry in the developing egg chamber.\" [GOC:mtg_sensu, PMID:10449356]\nsynonym: \"establishment and maintenance of oocyte localization in egg chamber\" EXACT []\nsynonym: \"establishment and maintenance of oocyte position during oogenesis\" EXACT []\nsynonym: \"oocyte localisation involved in germarium-derived egg chamber formation\" EXACT [GOC:mah]\nsynonym: \"oocyte localization during germarium-derived egg chamber formation\" RELATED [GOC:dph, GOC:tb]\nsynonym: \"oocyte localization during oogenesis\" RELATED []\nsynonym: \"oocyte positioning during oogenesis\" NARROW []\nsynonym: \"oogenesis, establishment and maintenance of oocyte localization\" EXACT []\nsynonym: \"oogenesis, oocyte localization\" EXACT []\nis_a: GO:0051674 ! localization of cell\nrelationship: part_of GO:0007293 ! germarium-derived egg chamber formation\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0030720"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "source": "Gene Ontology current ontology",
  "url": "https://current.geneontology.org/ontology/go-basic.obo",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source_locator": "lines 388677-388686",
  "excerpt": "[Term]\nid: GO:0075016\nname: appressorium formation\nnamespace: biological_process\ndef: \"The process in which a swollen, flattened portion of a symbiont filament is formed on or near its host organism, to adhere to and for the purpose of penetrating the host surface.\" [GOC:pamgo_curators]\nsynonym: \"appressorium formation for entry into host, on or near host\" EXACT []\nsynonym: \"appressorium formation on or near host\" RELATED []\nsynonym: \"formation of an appressorium by symbiont on or near host\" EXACT []\nis_a: GO:0075015 ! formation of infection structure\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "go_id": "GO:0075016"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 191. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
