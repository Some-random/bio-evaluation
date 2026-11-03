# pathway_0149: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/pathway_0149.txt)

**Task:** `pathway`  
**Author key, unchanged:** **D** — Cofactor biosynthesis

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
MHYLDNLLLNTDSYKASHWLQYPPGTDASFFYVESRGGVYDQTAFFGLQSILKEAINRPVTHADIDDAKALLAAHGEPFNEAGWRDIVDRLGGQLPIRIRAVPEGCVVPTHNVLMTIESTDAKAFWVPSYLETLLLRVWYPVTVATVSWQVKQIVRDFLQRTSDDPEGQLPFKLHDFGARGVSSLGSAALGGAAHLVNFLGTDTLSALLLARAHYHTPVAGYSIPAAEHSTITSWGREREVDAYRNMLTQFARPGAIVAVVSDSYDIYRAIREHWGTTLREEIIASGATVVIRPDSGDPVDVVEQCLLLLDEAFGHQVNGKGYKVLNHVRVIQGDGINPQSLRAILERITAAGYAADNVAFGMGGALLQKVDRDTQKFALKCSAVRVDGAWIDVYKDPITDQGKQSKRGRLTLLRDRATGQYRSALLDEVATHAGDSDDALVTVWENGQMLREWTLEQVRAHADAARL

[Multiple Choices]
A. Antifungal biosynthesis. .
B. protein ubiquitination. .
C. IMP biosynthesis via de novo pathway
D. Cofactor biosynthesis
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

> The supplied sequence exactly matches the annotated 468-aa Xanthomonas campestris NAMPT. The entry identifies it as nicotinamide phosphoribosyltransferase and assigns it to NAD(+) cofactor biosynthesis; the pathway annotation cites experimental evidence.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is a soluble enzyme, which makes the signaling and ubiquitination options less plausible, but that broad observation does not distinguish cofactor biosynthesis from other metabolic pathways.


**Missing item-specific fact**

> Identifying this sequence as nicotinamide phosphoribosyltransferase, which catalyzes a step in NAD(+) biosynthesis.


**Reason**

> The sequence and choices do not provide a sufficiently specific, readily interpretable motif or context to establish its pathway without protein-specific identification or equivalent annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the matched NAMPT annotation and its NAD(+) biosynthesis role, cofactor biosynthesis is the clear listed choice.


### Important caveats

- The pathway annotation and experimental support are reviewer-only evidence, not information supplied to the evaluated model.
- The exact author source snapshot is unknown, although the sequence matches both the current entry and a historical entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a soluble enzyme, which makes the signaling and ubiquitination options less plausible, but that broad observation does not distinguish cofactor biosynthesis from other metabolic pathways.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Identifying this sequence as nicotinamide phosphoribosyltransferase, which catalyzes a step in NAD(+) biosynthesis.",
    "reason": "The sequence and choices do not provide a sufficiently specific, readily interpretable motif or context to establish its pathway without protein-specific identification or equivalent annotation."
  },
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated 468-aa Xanthomonas campestris NAMPT. The entry identifies it as nicotinamide phosphoribosyltransferase and assigns it to NAD(+) cofactor biosynthesis; the pathway annotation cites experimental evidence."
  },
  "important_caveats": [
    "The pathway annotation and experimental support are reviewer-only evidence, not information supplied to the evaluated model.",
    "The exact author source snapshot is unknown, although the sequence matches both the current entry and a historical entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched NAMPT annotation and its NAD(+) biosynthesis role, cofactor biosynthesis is the clear listed choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the annotated 468-aa Xanthomonas campestris NAMPT. The entry identifies it as nicotinamide phosphoribosyltransferase and assigns it to NAD(+) cofactor biosynthesis; the pathway annotation cites experimental evidence.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is a soluble enzyme, which makes the signaling and ubiquitination options less plausible, but that broad observation does not distinguish cofactor biosynthesis from other metabolic pathways.",
    "missing_item_specific_fact": "Identifying this sequence as nicotinamide phosphoribosyltransferase, which catalyzes a step in NAD(+) biosynthesis.",
    "reason": "The sequence and choices do not provide a sufficiently specific, readily interpretable motif or context to establish its pathway without protein-specific identification or equivalent annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the matched NAMPT annotation and its NAD(+) biosynthesis role, cofactor biosynthesis is the clear listed choice."
  },
  "important_caveats": [
    "The pathway annotation and experimental support are reviewer-only evidence, not information supplied to the evaluated model.",
    "The exact author source snapshot is unknown, although the sequence matches both the current entry and a historical entry."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence (468 aa, SHA256 matched) corresponds to UniProt A0A0H2X5R2, annotated as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) from Xanthomonas campestris pv. campestris 8004. The UniProt PATHWAY comment reads: 'Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1' (ECO:0000269, PubMed:38429435). This is backed by X-ray crystallography (PDB: 7YQO, 7YQP, 7YQQ, 7YQR, 8IGZ) and enzymatic characterization. The expected answer 'Cofactor biosynthesis' directly matches the top-level pathway category.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark PRTase (phosphoribosyltransferase) superfamily motifs: the 'HDFGARGVSSLGSAALGGAAHLVNFLGTDTLSALLLARAHYHT' block, the 'VSDSYDIY' SD-motif, and 'GAWIDVYKDP' — diagnostic of the Type I PRTase fold. This immediately eliminates B (protein ubiquitination: no E2/E3 ligase, RING, or UBA motifs) and A (antifungal biosynthesis: no PKS, NRPS, or terpene cyclase features). Between C and D: the de novo IMP biosynthesis pathway proceeds through amidotransferases, formyltransferases, synthetases, and lyases (e.g., PRPP amidotransferase, GAR synthetase, FGAM synthetase, AIR carboxylase, SAICAR synthetase) and does not employ Type I PRTases. In contrast, NAD+ biosynthesis via the NAM salvage pathway is catalyzed by NAMPT, a canonical Type I PRTase, and NAD+ is universally classified as a cofactor. Thus, identifying the protein as a Type I PRTase and applying standard pathway biochemistry (IMP de novo lacks PRTases; NAD+ is a cofactor) provides a concrete chain of reasoning that selects D over C.


**Missing item-specific fact**

> Precise subfamily assignment (NAMPT vs. HGPRT vs. other Type I PRTases) from sequence alone requires detailed knowledge of substrate-binding-site residues; however, the pathway-level distinction (cofactor vs. nucleotide de novo) is resolvable without that specificity because IMP de novo does not use PRTases at all.


**Reason**

> The PRTase fold identification narrows the choices from four to two (C vs. D), and standard biochemistry knowledge that the de novo purine pathway does not employ PRTases while NAD+ biosynthesis does eliminates C. The remaining choice D is supported by the general classification of NAD+ as a cofactor. This constitutes a meaningful biological reasoning chain rather than pure database lookup.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are eliminated by absence of any relevant enzymatic motifs. Option C (IMP de novo) is eliminated because that pathway does not utilize Type I PRTases. Option D (Cofactor biosynthesis) is the only pathway among the four that employs a Type I PRTase. No other option is defensible given the PRTase identification.


### Important caveats

- The UniProt annotation is Swiss-Prot (manually curated) with experimental evidence codes (ECO:0000269, X-ray crystallography), providing strong support for the pathway assignment.
- The entry was first released in 2025-02-05; if the benchmark was constructed before that date, the annotation may have been derived from computational inference or transferred annotation rather than the 2024 experimental paper.
- The reasoning chain relies on the examinee recognizing PRTase motifs and knowing that IMP de novo does not use PRTases — this is standard biochemistry but still requires specific pathway-level knowledge beyond generic sequence analysis.
- The sequence-match is exact (SHA256 identical) between the benchmark input and the UniProt entry, confirming applicability of the annotation to this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark PRTase (phosphoribosyltransferase) superfamily motifs: the 'HDFGARGVSSLGSAALGGAAHLVNFLGTDTLSALLLARAHYHT' block, the 'VSDSYDIY' SD-motif, and 'GAWIDVYKDP' — diagnostic of the Type I PRTase fold. This immediately eliminates B (protein ubiquitination: no E2/E3 ligase, RING, or UBA motifs) and A (antifungal biosynthesis: no PKS, NRPS, or terpene cyclase features). Between C and D: the de novo IMP biosynthesis pathway proceeds through amidotransferases, formyltransferases, synthetases, and lyases (e.g., PRPP amidotransferase, GAR synthetase, FGAM synthetase, AIR carboxylase, SAICAR synthetase) and does not employ Type I PRTases. In contrast, NAD+ biosynthesis via the NAM salvage pathway is catalyzed by NAMPT, a canonical Type I PRTase, and NAD+ is universally classified as a cofactor. Thus, identifying the protein as a Type I PRTase and applying standard pathway biochemistry (IMP de novo lacks PRTases; NAD+ is a cofactor) provides a concrete chain of reasoning that selects D over C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precise subfamily assignment (NAMPT vs. HGPRT vs. other Type I PRTases) from sequence alone requires detailed knowledge of substrate-binding-site residues; however, the pathway-level distinction (cofactor vs. nucleotide de novo) is resolvable without that specificity because IMP de novo does not use PRTases at all.",
    "reason": "The PRTase fold identification narrows the choices from four to two (C vs. D), and standard biochemistry knowledge that the de novo purine pathway does not employ PRTases while NAD+ biosynthesis does eliminates C. The remaining choice D is supported by the general classification of NAD+ as a cofactor. This constitutes a meaningful biological reasoning chain rather than pure database lookup."
  },
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence (468 aa, SHA256 matched) corresponds to UniProt A0A0H2X5R2, annotated as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) from Xanthomonas campestris pv. campestris 8004. The UniProt PATHWAY comment reads: 'Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1' (ECO:0000269, PubMed:38429435). This is backed by X-ray crystallography (PDB: 7YQO, 7YQP, 7YQQ, 7YQR, 8IGZ) and enzymatic characterization. The expected answer 'Cofactor biosynthesis' directly matches the top-level pathway category."
  },
  "important_caveats": [
    "The UniProt annotation is Swiss-Prot (manually curated) with experimental evidence codes (ECO:0000269, X-ray crystallography), providing strong support for the pathway assignment.",
    "The entry was first released in 2025-02-05; if the benchmark was constructed before that date, the annotation may have been derived from computational inference or transferred annotation rather than the 2024 experimental paper.",
    "The reasoning chain relies on the examinee recognizing PRTase motifs and knowing that IMP de novo does not use PRTases — this is standard biochemistry but still requires specific pathway-level knowledge beyond generic sequence analysis.",
    "The sequence-match is exact (SHA256 identical) between the benchmark input and the UniProt entry, confirming applicability of the annotation to this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are eliminated by absence of any relevant enzymatic motifs. Option C (IMP de novo) is eliminated because that pathway does not utilize Type I PRTases. Option D (Cofactor biosynthesis) is the only pathway among the four that employs a Type I PRTase. No other option is defensible given the PRTase identification."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence (468 aa, SHA256 matched) corresponds to UniProt A0A0H2X5R2, annotated as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) from Xanthomonas campestris pv. campestris 8004. The UniProt PATHWAY comment reads: 'Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1' (ECO:0000269, PubMed:38429435). This is backed by X-ray crystallography (PDB: 7YQO, 7YQP, 7YQQ, 7YQR, 8IGZ) and enzymatic characterization. The expected answer 'Cofactor biosynthesis' directly matches the top-level pathway category.",
    "evidence_ids": ["C1", "C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark PRTase (phosphoribosyltransferase) superfamily motifs: the 'HDFGARGVSSLGSAALGGAAHLVNFLGTDTLSALLLARAHYHT' block, the 'VSDSYDIY' SD-motif, and 'GAWIDVYKDP' — diagnostic of the Type I PRTase fold. This immediately eliminates B (protein ubiquitination: no E2/E3 ligase, RING, or UBA motifs) and A (antifungal biosynthesis: no PKS, NRPS, or terpene cyclase features). Between C and D: the de novo IMP biosynthesis pathway proceeds through amidotransferases, formyltransferases, synthetases, and lyases (e.g., PRPP amidotransferase, GAR synthetase, FGAM synthetase, AIR carboxylase, SAICAR synthetase) and does not employ Type I PRTases. In contrast, NAD+ biosynthesis via the NAM salvage pathway is catalyzed by NAMPT, a canonical Type I PRTase, and NAD+ is universally classified as a cofactor. Thus, identifying the protein as a Type I PRTase and applying standard pathway biochemistry (IMP de novo lacks PRTases; NAD+ is a cofactor) provides a concrete chain of reasoning that selects D over C.",
    "missing_item_specific_fact": "Precise subfamily assignment (NAMPT vs. HGPRT vs. other Type I PRTases) from sequence alone requires detailed knowledge of substrate-binding-site residues; however, the pathway-level distinction (cofactor vs. nucleotide de novo) is resolvable without that specificity because IMP de novo does not use PRTases at all.",
    "reason": "The PRTase fold identification narrows the choices from four to two (C vs. D), and standard biochemistry knowledge that the de novo purine pathway does not employ PRTases while NAD+ biosynthesis does eliminates C. The remaining choice D is supported by the general classification of NAD+ as a cofactor. This constitutes a meaningful biological reasoning chain rather than pure database lookup."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are eliminated by absence of any relevant enzymatic motifs. Option C (IMP de novo) is eliminated because that pathway does not utilize Type I PRTases. Option D (Cofactor biosynthesis) is the only pathway among the four that employs a Type I PRTase. No other option is defensible given the PRTase identification."
  },
  "important_caveats": [
    "The UniProt annotation is Swiss-Prot (manually curated) with experimental evidence codes (ECO:0000269, X-ray crystallography), providing strong support for the pathway assignment.",
    "The entry was first released in 2025-02-05; if the benchmark was constructed before that date, the annotation may have been derived from computational inference or transferred annotation rather than the 2024 experimental paper.",
    "The reasoning chain relies on the examinee recognizing PRTase motifs and knowing that IMP de novo does not use PRTases — this is standard biochemistry but still requires specific pathway-level knowledge beyond generic sequence analysis.",
    "The sequence-match is exact (SHA256 identical) between the benchmark input and the UniProt entry, confirming applicability of the annotation to this exact protein."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation identifies the protein as nicotinamide phosphoribosyltransferase and places it in NAD(+) cofactor biosynthesis via the nicotinamide salvage pathway. The pathway annotation cites experimental evidence, although the underlying study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 468-residue sequence is consistent with the NAMPT family. Transferable knowledge of this enzyme family connects nicotinamide phosphoribosyltransferase activity to NAD biosynthesis, a cofactor-biosynthesis pathway. That distinguishes D from protein ubiquitination and antifungal biosynthesis; it also distinguishes D from de novo IMP biosynthesis, which is a different nucleotide-synthesis route.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family recognition from the sequence, together with the known role of NAMPT homologs in NAD cofactor biosynthesis, provides a meaningful basis for choosing among these options without recalling this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices distinguish cofactor biosynthesis from the other listed pathways, and the supported NAMPT-family inference points to D.


### Important caveats

- The source annotation is reviewer-only evidence, not an original input; the answerability judgment relies on transferable NAMPT-family knowledge.
- The cited experimental basis is represented in the supplied annotation, but the primary study was not independently evaluated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 468-residue sequence is consistent with the NAMPT family. Transferable knowledge of this enzyme family connects nicotinamide phosphoribosyltransferase activity to NAD biosynthesis, a cofactor-biosynthesis pathway. That distinguishes D from protein ubiquitination and antifungal biosynthesis; it also distinguishes D from de novo IMP biosynthesis, which is a different nucleotide-synthesis route.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family recognition from the sequence, together with the known role of NAMPT homologs in NAD cofactor biosynthesis, provides a meaningful basis for choosing among these options without recalling this exact protein's database record."
  },
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as nicotinamide phosphoribosyltransferase and places it in NAD(+) cofactor biosynthesis via the nicotinamide salvage pathway. The pathway annotation cites experimental evidence, although the underlying study was not independently reviewed here."
  },
  "important_caveats": [
    "The source annotation is reviewer-only evidence, not an original input; the answerability judgment relies on transferable NAMPT-family knowledge.",
    "The cited experimental basis is represented in the supplied annotation, but the primary study was not independently evaluated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish cofactor biosynthesis from the other listed pathways, and the supported NAMPT-family inference points to D."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as nicotinamide phosphoribosyltransferase and places it in NAD(+) cofactor biosynthesis via the nicotinamide salvage pathway. The pathway annotation cites experimental evidence, although the underlying study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 468-residue sequence is consistent with the NAMPT family. Transferable knowledge of this enzyme family connects nicotinamide phosphoribosyltransferase activity to NAD biosynthesis, a cofactor-biosynthesis pathway. That distinguishes D from protein ubiquitination and antifungal biosynthesis; it also distinguishes D from de novo IMP biosynthesis, which is a different nucleotide-synthesis route.",
    "missing_item_specific_fact": "",
    "reason": "Family recognition from the sequence, together with the known role of NAMPT homologs in NAD cofactor biosynthesis, provides a meaningful basis for choosing among these options without recalling this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish cofactor biosynthesis from the other listed pathways, and the supported NAMPT-family inference points to D."
  },
  "important_caveats": [
    "The source annotation is reviewer-only evidence, not an original input; the answerability judgment relies on transferable NAMPT-family knowledge.",
    "The cited experimental basis is represented in the supplied annotation, but the primary study was not independently evaluated."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0H2X5R2) annotates this protein as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) with pathway 'Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1,' supported by experimental evidence (ECO:0000269, PubMed:38429435) including X-ray crystallography and functional assays. The answer D (Cofactor biosynthesis) is directly confirmed.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved 'GEP' motif (around residue 70: 'AKALLAAHGEPFNEAGWRDIVDRLGG') and the 'GWR' motif immediately following, which are hallmark signatures of NAMPT identified across human, yeast, and bacterial NAMPT proteins. The overall ~468 aa length and PRTase (phosphoribosyltransferase) fold architecture (central β-sheet flanked by α-helices, with the characteristic GEP-GWR catalytic region) are consistent with NAMPT. The PRTase fold with GEP motif is associated with nucleotide/cofactor salvage enzymes (NAMPT, HGPRT, APRT, UPP, TrpD), not with de novo purine biosynthesis enzymes (PurF uses a glutamine amidotransferase fold; PurL/PurM/PurH use formyltransferase or synthetase folds). The sequence lacks RING/HECT/U-box motifs (ruling out ubiquitination), lacks polyketide synthase or NRPS domains (ruling out antifungal biosynthesis), and lacks the glutamine amidotransferase Cys-His catalytic dyad and large multi-domain architecture of Pur enzymes (ruling out IMP de novo biosynthesis). The GEP motif specifically identifies NAMPT among PRTases, pointing to NAD+ biosynthesis, which UniProt classifies under 'Cofactor biosynthesis.'


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GEP-GWR motif and PRTase fold are well-known transferable features from human NAMPT (P30431), yeast Pnc1, and other characterized NAMPT orthologs. A model familiar with these motifs can recognize the protein as a NAMPT-family phosphoribosyltransferase and, knowing that NAMPT catalyzes the rate-limiting step of NAD+ salvage (classified under cofactor biosynthesis), distinguish D from the other three options. The absence of purine-pathway enzyme features, ubiquitin-ligase domains, and antifungal biosynthetic machinery further eliminates alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent distinct pathway categories with no overlap. The GEP motif and PRTase fold unambiguously point to NAMPT/NAD+ biosynthesis (cofactor biosynthesis) rather than ubiquitination, antifungal biosynthesis, or de novo IMP biosynthesis.


### Important caveats

- The N-terminal ~90 residues of this sequence are identical to human NAMPT (P30431), which is unusual for a bacterial protein; this may reflect extremely high conservation in this region or a database annotation artifact. The UniProt entry was only made public in February 2025.
- The reviewer-only evidence confirms the annotation via a 2024 crystallographic study (PDB 7YQO-7YQR, 8IGZ) with experimental evidence codes, but this information was not available to the evaluated model.
- The PRTase fold is shared among several enzyme families; the GEP motif is the key discriminator for NAMPT specifically within that fold.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved 'GEP' motif (around residue 70: 'AKALLAAHGEPFNEAGWRDIVDRLGG') and the 'GWR' motif immediately following, which are hallmark signatures of NAMPT identified across human, yeast, and bacterial NAMPT proteins. The overall ~468 aa length and PRTase (phosphoribosyltransferase) fold architecture (central β-sheet flanked by α-helices, with the characteristic GEP-GWR catalytic region) are consistent with NAMPT. The PRTase fold with GEP motif is associated with nucleotide/cofactor salvage enzymes (NAMPT, HGPRT, APRT, UPP, TrpD), not with de novo purine biosynthesis enzymes (PurF uses a glutamine amidotransferase fold; PurL/PurM/PurH use formyltransferase or synthetase folds). The sequence lacks RING/HECT/U-box motifs (ruling out ubiquitination), lacks polyketide synthase or NRPS domains (ruling out antifungal biosynthesis), and lacks the glutamine amidotransferase Cys-His catalytic dyad and large multi-domain architecture of Pur enzymes (ruling out IMP de novo biosynthesis). The GEP motif specifically identifies NAMPT among PRTases, pointing to NAD+ biosynthesis, which UniProt classifies under 'Cofactor biosynthesis.'",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GEP-GWR motif and PRTase fold are well-known transferable features from human NAMPT (P30431), yeast Pnc1, and other characterized NAMPT orthologs. A model familiar with these motifs can recognize the protein as a NAMPT-family phosphoribosyltransferase and, knowing that NAMPT catalyzes the rate-limiting step of NAD+ salvage (classified under cofactor biosynthesis), distinguish D from the other three options. The absence of purine-pathway enzyme features, ubiquitin-ligase domains, and antifungal biosynthetic machinery further eliminates alternatives."
  },
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0H2X5R2) annotates this protein as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) with pathway 'Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1,' supported by experimental evidence (ECO:0000269, PubMed:38429435) including X-ray crystallography and functional assays. The answer D (Cofactor biosynthesis) is directly confirmed."
  },
  "important_caveats": [
    "The N-terminal ~90 residues of this sequence are identical to human NAMPT (P30431), which is unusual for a bacterial protein; this may reflect extremely high conservation in this region or a database annotation artifact. The UniProt entry was only made public in February 2025.",
    "The reviewer-only evidence confirms the annotation via a 2024 crystallographic study (PDB 7YQO-7YQR, 8IGZ) with experimental evidence codes, but this information was not available to the evaluated model.",
    "The PRTase fold is shared among several enzyme families; the GEP motif is the key discriminator for NAMPT specifically within that fold."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct pathway categories with no overlap. The GEP motif and PRTase fold unambiguously point to NAMPT/NAD+ biosynthesis (cofactor biosynthesis) rather than ubiquitination, antifungal biosynthesis, or de novo IMP biosynthesis."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0H2X5R2) annotates this protein as Nicotinamide phosphoribosyltransferase (NAMPT, EC 2.4.2.12) with pathway 'Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1,' supported by experimental evidence (ECO:0000269, PubMed:38429435) including X-ray crystallography and functional assays. The answer D (Cofactor biosynthesis) is directly confirmed.",
    "evidence_ids": ["C5", "C4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved 'GEP' motif (around residue 70: 'AKALLAAHGEPFNEAGWRDIVDRLGG') and the 'GWR' motif immediately following, which are hallmark signatures of NAMPT identified across human, yeast, and bacterial NAMPT proteins. The overall ~468 aa length and PRTase (phosphoribosyltransferase) fold architecture (central β-sheet flanked by α-helices, with the characteristic GEP-GWR catalytic region) are consistent with NAMPT. The PRTase fold with GEP motif is associated with nucleotide/cofactor salvage enzymes (NAMPT, HGPRT, APRT, UPP, TrpD), not with de novo purine biosynthesis enzymes (PurF uses a glutamine amidotransferase fold; PurL/PurM/PurH use formyltransferase or synthetase folds). The sequence lacks RING/HECT/U-box motifs (ruling out ubiquitination), lacks polyketide synthase or NRPS domains (ruling out antifungal biosynthesis), and lacks the glutamine amidotransferase Cys-His catalytic dyad and large multi-domain architecture of Pur enzymes (ruling out IMP de novo biosynthesis). The GEP motif specifically identifies NAMPT among PRTases, pointing to NAD+ biosynthesis, which UniProt classifies under 'Cofactor biosynthesis.'",
    "missing_item_specific_fact": "",
    "reason": "The GEP-GWR motif and PRTase fold are well-known transferable features from human NAMPT (P30431), yeast Pnc1, and other characterized NAMPT orthologs. A model familiar with these motifs can recognize the protein as a NAMPT-family phosphoribosyltransferase and, knowing that NAMPT catalyzes the rate-limiting step of NAD+ salvage (classified under cofactor biosynthesis), distinguish D from the other three options. The absence of purine-pathway enzyme features, ubiquitin-ligase domains, and antifungal biosynthetic machinery further eliminates alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent distinct pathway categories with no overlap. The GEP motif and PRTase fold unambiguously point to NAMPT/NAD+ biosynthesis (cofactor biosynthesis) rather than ubiquitination, antifungal biosynthesis, or de novo IMP biosynthesis."
  },
  "important_caveats": [
    "The N-terminal ~90 residues of this sequence are identical to human NAMPT (P30431), which is unusual for a bacterial protein; this may reflect extremely high conservation in this region or a database annotation artifact. The UniProt entry was only made public in February 2025.",
    "The reviewer-only evidence confirms the annotation via a 2024 crystallographic study (PDB 7YQO-7YQR, 8IGZ) with experimental evidence codes, but this information was not available to the evaluated model.",
    "The PRTase fold is shared among several enzyme families; the GEP motif is the key discriminator for NAMPT specifically within that fold."
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
  "requested_accession": "A0A0H2X5R2",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "c9ee286b6dffa262b90f67a1a22d051bc2b6beed528f7f4ef5e12e3af3684da3",
  "benchmark_sequence_length": 468,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 47,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2015-09-16",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "current_source_sequence_sha256": "c9ee286b6dffa262b90f67a1a22d051bc2b6beed528f7f4ef5e12e3af3684da3",
  "current_source_sequence_length": 468,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 45,
  "selected_historical_version": {
    "accession": "A0A0H2X5R2",
    "database": "Swiss-Prot",
    "entryVersion": 45,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NAMPT_XANC8",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "selected_historical_source_sequence_sha256": "c9ee286b6dffa262b90f67a1a22d051bc2b6beed528f7f4ef5e12e3af3684da3",
  "selected_historical_source_sequence_length": 468,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 45,
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A0H2X5R2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":47,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2015-09-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Lysobacterales\",\"Lysobacteraceae\",\"Xanthomonas\"],\"scientificName\":\"Xanthomonas campestris pv. campestris (strain 8004)\",\"taxonId\":314565}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"2.4.2.12\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"Nicotinamide phosphoribosyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"NAM phosphoribosyltransferase\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"NAMPT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "json_pointer": "/comments/4",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and nicotinamide: step 1/1\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X5R2.json",
  "source_sha256": "b27e2ead98a0950f8f9b318beba504515805b54f2fc34834409f729c307077ba",
  "retrieved_utc": "2026-11-02T04:24:06.426700+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Xu G.\",\"Ma J.\",\"Fang Q.\",\"Peng Q.\",\"Jiao X.\",\"Hu W.\",\"Zhao Q.\",\"Kong Y.\",\"Liu F.\",\"Shi X.\",\"Tang D.J.\",\"Tang J.L.\",\"Ming Z.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38429435\"},{\"database\":\"DOI\",\"id\":\"10.1038/s42003-024-05921-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"255\",\"id\":\"38429435\",\"journal\":\"Commun. Biol.\",\"lastPage\":\"255\",\"publicationDate\":\"2024\",\"title\":\"Structural insights into Xanthomonas campestris pv. campestris NAD+ biosynthesis via the NAM salvage pathway.\",\"volume\":\"7\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YQO\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YQP\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YQQ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7YQR\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8IGZ\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"8004\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.79 ANGSTROMS) OF APOENZYME; WILD-TYPE IN COMPLEXES WITH NICOTINAMIDE AND BETA-NICOTINAMIDE D-RIBONUCLEOTIDE AND QUADRUPLE MUTANT PHE-175/PHE-224/PHE-291/PHE-332\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"SUBUNIT\",\"DOMAIN\",\"PHOSPHORYLATION AT HIS-229\",\"DISRUPTION PHENOTYPE\",\"MUTAGENESIS OF HIS-175; ARG-180; ASP-203; ILE-224; HIS-229; VAL-291; ARG-293; ILE-332; ASP-335 AND ARG-373\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45",
  "source_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "retrieved_utc": "2026-11-02T04:24:08.378348+00:00",
  "source_locator": "lines 1-14",
  "excerpt": "ID   NAMPT_XANC8             Reviewed;         468 AA.\nAC   A0A0H2X5R2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-SEP-2015, sequence version 1.\nDT   28-JAN-2026, entry version 45.\nDE   RecName: Full=Nicotinamide phosphoribosyltransferase {ECO:0000303|PubMed:38429435};\nDE            Short=NAM phosphoribosyltransferase {ECO:0000303|PubMed:38429435};\nDE            Short=NAMPT {ECO:0000303|PubMed:38429435};\nDE            EC=2.4.2.12 {ECO:0000269|PubMed:38429435};\nGN   OrderedLocusNames=XC_0719 {ECO:0000312|EMBL:AAY47797.1};\nOS   Xanthomonas campestris pv. campestris (strain 8004).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Lysobacterales; Lysobacteraceae; Xanthomonas.\nOX   NCBI_TaxID=314565;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45",
  "source_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "retrieved_utc": "2026-11-02T04:24:08.378348+00:00",
  "source_locator": "lines 26-40",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7YQO, ECO:0007744|PDB:7YQP, ECO:0007744|PDB:7YQQ, ECO:0007744|PDB:7YQR, ECO:0007744|PDB:8IGZ}\nRP   X-RAY CRYSTALLOGRAPHY (1.79 ANGSTROMS) OF APOENZYME; WILD-TYPE IN COMPLEXES\nRP   WITH NICOTINAMIDE AND BETA-NICOTINAMIDE D-RIBONUCLEOTIDE AND QUADRUPLE\nRP   MUTANT PHE-175/PHE-224/PHE-291/PHE-332, FUNCTION, CATALYTIC ACTIVITY,\nRP   ACTIVITY REGULATION, BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, SUBUNIT,\nRP   DOMAIN, PHOSPHORYLATION AT HIS-229, DISRUPTION PHENOTYPE, AND MUTAGENESIS\nRP   OF HIS-175; ARG-180; ASP-203; ILE-224; HIS-229; VAL-291; ARG-293; ILE-332;\nRP   ASP-335 AND ARG-373.\nRC   STRAIN=8004;\nRX   PubMed=38429435; DOI=10.1038/s42003-024-05921-3;\nRA   Xu G., Ma J., Fang Q., Peng Q., Jiao X., Hu W., Zhao Q., Kong Y., Liu F.,\nRA   Shi X., Tang D.J., Tang J.L., Ming Z.;\nRT   \"Structural insights into Xanthomonas campestris pv. campestris NAD+\nRT   biosynthesis via the NAM salvage pathway.\";\nRL   Commun. Biol. 7:255-255(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X5R2?format=txt&versions=45",
  "source_sha256": "9a75b45b0cf9f2f82d4758fbdd5a527427ddd0af614a46403ba19d96e4883de1",
  "retrieved_utc": "2026-11-02T04:24:08.378348+00:00",
  "source_locator": "lines 70-72",
  "excerpt": "CC   -!- PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis; nicotinamide D-\nCC       ribonucleotide from 5-phospho-alpha-D-ribose 1-diphosphate and\nCC       nicotinamide: step 1/1. {ECO:0000269|PubMed:38429435}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 45,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 149. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
