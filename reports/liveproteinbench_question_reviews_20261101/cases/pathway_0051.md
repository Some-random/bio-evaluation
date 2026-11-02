# pathway_0051

[All questions and paired results](../README.md) · [Method](../METHOD.md) · [Source credits](../THIRD_PARTY_NOTICES.md)

**Task:** `pathway`  
**Author expected answer:** **C** — Cofactor biosynthesis

| Reviewer | Expected-answer support | Reasoning / lookup | Validity |
|---|---|---|---|
| GPT-6 Luna | supported | lookup-dependent | valid_review |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | valid_review |

**Paired comparison:** key agree; reasoning differ. Agreement is not proof of correctness. These are separate AI judgments, with no forced consensus or changed key.

## Complete original question

```text
[Protein Sequence]
MMESAVTAHTLRIAMAQFDFPVGAVTQNTDRIIEYIAAARDEFEADIVLFPELAISGYPPEDLLLRPGFLAHCEQALARIAAATRGIVAVVGWPQSAGSVVYNAASVLREGRIEATYRKRELPNYAVFDERRYFDVDPDGDNCVVTVKGVQVGVVICEDLWFAEPLAKTVQAGAELVLVPNASPYERGKHAQRDALLAERTRESGAAIAYLNVVGGQDALVFDGASVVADGDGTVHPAAAAFVDQWLVVDYAAGERSFTPVVWVDDGDESMDALAWRAVVRGLKDYCGKNGFRKVWLGLSGGIDSALVLAMAVDALGGENVTAVRLPSRYTAGLSNDLADEQCRALGVKLETIAIEPAFEGLLAALGPLFADTQPDITEENLQSRSRGVILMALSNKFGGLVLTTGNKSEYAVGYATIYGDMCGGYAPLKDLYKTEVFGLAKWRNTVGGAPVIPPAVISRPPSAELRDNQTDQDSLPPYDVLDGILYRYVDQEQSRDDIVAAGYAADTVEHVLRLVRLNEWKRHQAAPGPKVSRRAFGRERRYPITNGYSGQ

[Multiple Choices]
A. Antifungal biosynthesis. .
B. L-cystathionine from O-succinyl-L-homoserine: step 1/1. .
C. Cofactor biosynthesis
D. Membrane lipid metabolism. .
```

<details>
<summary>Original system instructions, verbatim</summary>

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

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The exact sequence matches a UniProt entry annotated as glutamine-dependent NAD(+) synthetase, with a pathway annotation placing it in NAD(+) biosynthesis under cofactor biosynthesis. The enzyme annotation and pathway assignment are supported by a computational HAMAP rule; the supplied excerpts do not independently establish an experimental assay of the enzyme's activity.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence alone does not provide a readily interpretable clue that distinguishes NAD(+) biosynthesis from the listed alternatives without identifying its specific enzyme family and function.


**Missing item-specific fact**

> That this particular sequence is a glutamine-dependent NAD(+) synthetase functioning in NAD(+) biosynthesis.


**Reason**

> Choosing C depends on a protein-specific functional assignment absent from the input. Recognizing the sequence or obtaining its annotation through an external homology or database lookup would not make the question reasoning-supported.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Given the supported NAD(+) biosynthesis assignment, cofactor biosynthesis is the matching listed category; the other choices do not describe that pathway.


### Important caveats

- The sequence match applies to both the current and retrieved historical UniProt record, but the author's exact source snapshot is unknown.
- The pathway annotation is computationally supported by HAMAP; the cited publication excerpt concerns NAD(+) biosynthesis and a disruption phenotype, not a directly shown enzyme assay.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence alone does not provide a readily interpretable clue that distinguishes NAD(+) biosynthesis from the listed alternatives without identifying its specific enzyme family and function.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular sequence is a glutamine-dependent NAD(+) synthetase functioning in NAD(+) biosynthesis.",
    "reason": "Choosing C depends on a protein-specific functional assignment absent from the input. Recognizing the sequence or obtaining its annotation through an external homology or database lookup would not make the question reasoning-supported."
  },
  "case_id": "pathway_0051",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as glutamine-dependent NAD(+) synthetase, with a pathway annotation placing it in NAD(+) biosynthesis under cofactor biosynthesis. The enzyme annotation and pathway assignment are supported by a computational HAMAP rule; the supplied excerpts do not independently establish an experimental assay of the enzyme's activity."
  },
  "important_caveats": [
    "The sequence match applies to both the current and retrieved historical UniProt record, but the author's exact source snapshot is unknown.",
    "The pathway annotation is computationally supported by HAMAP; the cited publication excerpt concerns NAD(+) biosynthesis and a disruption phenotype, not a directly shown enzyme assay."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the supported NAD(+) biosynthesis assignment, cofactor biosynthesis is the matching listed category; the other choices do not describe that pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0051",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as glutamine-dependent NAD(+) synthetase, with a pathway annotation placing it in NAD(+) biosynthesis under cofactor biosynthesis. The enzyme annotation and pathway assignment are supported by a computational HAMAP rule; the supplied excerpts do not independently establish an experimental assay of the enzyme's activity.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence alone does not provide a readily interpretable clue that distinguishes NAD(+) biosynthesis from the listed alternatives without identifying its specific enzyme family and function.",
    "missing_item_specific_fact": "That this particular sequence is a glutamine-dependent NAD(+) synthetase functioning in NAD(+) biosynthesis.",
    "reason": "Choosing C depends on a protein-specific functional assignment absent from the input. Recognizing the sequence or obtaining its annotation through an external homology or database lookup would not make the question reasoning-supported."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Given the supported NAD(+) biosynthesis assignment, cofactor biosynthesis is the matching listed category; the other choices do not describe that pathway."
  },
  "important_caveats": [
    "The sequence match applies to both the current and retrieved historical UniProt record, but the author's exact source snapshot is unknown.",
    "The pathway annotation is computationally supported by HAMAP; the cited publication excerpt concerns NAD(+) biosynthesis and a disruption phenotype, not a directly shown enzyme assay."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence matches UniProt entry A0A0H2X6L3 (NADE_XANC8), annotated as Glutamine-dependent NAD(+) synthetase (EC 6.3.5.1). The UniProt PATHWAY comment explicitly states 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1,' directly supporting Choice C. The annotation is based on HAMAP-Rule MF_02090 (ECO:0000255, computational/curated), with additional support from a 2024 disruption phenotype study (PubMed 38429435). The other options (antifungal biosynthesis, cystathionine synthesis, membrane lipid metabolism) are unrelated to NAD+ synthetase.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region contains a glutaminase domain with a recognizable Cys-His-Asp catalytic triad motif (e.g., 'CEQ' near position 65, conserved 'W' residues in the oxyanion hole region), and the C-terminal region displays a synthetase domain with ATP-binding 'G' motifs. This two-domain glutaminase + synthetase architecture is characteristic of glutamine-dependent amidotransferases, which are predominantly involved in cofactor biosynthesis (NAD+, NADP+, folate, etc.). The other three options are clearly inconsistent: antifungal biosynthesis implies NRPS/PKS features absent here; cystathionine gamma-synthase is a PLP-dependent enzyme with entirely different fold; membrane lipid metabolism enzymes lack this amidotransferase architecture. The broad pathway category 'Cofactor biosynthesis' is reachable from recognizing the glutamine amidotransferase fold without needing the exact enzyme name.


**Missing item-specific fact**

> Precisely distinguishing NAD+ synthetase from other glutamine amidotransferases (e.g., GMP synthetase, folate synthetase) from sequence alone would require specialized fold recognition or database lookup, but the answer category 'Cofactor biosynthesis' is broad enough that the amidotransferase architecture reasoning suffices.


**Reason**

> The glutaminase + synthetase domain architecture is identifiable from sequence motifs and is strongly associated with cofactor biosynthesis. The three distractors describe pathways catalyzed by structurally unrelated enzymes (NRPS/PKS, PLP-dependent synthase, lipid-modifying enzymes), making them eliminable by general biological reasoning. The broad pathway label 'Cofactor biosynthesis' does not require pinpointing the exact enzyme.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The glutaminase + synthetase architecture is incompatible with antifungal biosynthesis (A), cystathionine gamma-synthase (B, PLP-dependent), or membrane lipid metabolism (D). Only 'Cofactor biosynthesis' (C) is consistent with a glutamine-dependent amidotransferase involved in NAD+ biosynthesis. No other option is defensible.


### Important caveats

- The UniProt pathway annotation is based on HAMAP-Rule MF_02090 (ECO:0000255), a computational/curated assignment, not direct enzymatic assay evidence for this specific protein. However, a 2024 disruption phenotype study (PubMed 38429435) provides experimental support for NAD+ biosynthesis function in this organism.
- The reviewer identified the accession from dataset metadata; the evaluated model received only the raw sequence and four pathway labels.
- The pathway annotation is a broad category ('Cofactor biosynthesis'); the full UniProt line specifies the sub-pathway 'NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1,' but the question only asks for the top-level pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region contains a glutaminase domain with a recognizable Cys-His-Asp catalytic triad motif (e.g., 'CEQ' near position 65, conserved 'W' residues in the oxyanion hole region), and the C-terminal region displays a synthetase domain with ATP-binding 'G' motifs. This two-domain glutaminase + synthetase architecture is characteristic of glutamine-dependent amidotransferases, which are predominantly involved in cofactor biosynthesis (NAD+, NADP+, folate, etc.). The other three options are clearly inconsistent: antifungal biosynthesis implies NRPS/PKS features absent here; cystathionine gamma-synthase is a PLP-dependent enzyme with entirely different fold; membrane lipid metabolism enzymes lack this amidotransferase architecture. The broad pathway category 'Cofactor biosynthesis' is reachable from recognizing the glutamine amidotransferase fold without needing the exact enzyme name.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Precisely distinguishing NAD+ synthetase from other glutamine amidotransferases (e.g., GMP synthetase, folate synthetase) from sequence alone would require specialized fold recognition or database lookup, but the answer category 'Cofactor biosynthesis' is broad enough that the amidotransferase architecture reasoning suffices.",
    "reason": "The glutaminase + synthetase domain architecture is identifiable from sequence motifs and is strongly associated with cofactor biosynthesis. The three distractors describe pathways catalyzed by structurally unrelated enzymes (NRPS/PKS, PLP-dependent synthase, lipid-modifying enzymes), making them eliminable by general biological reasoning. The broad pathway label 'Cofactor biosynthesis' does not require pinpointing the exact enzyme."
  },
  "case_id": "pathway_0051",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A0H2X6L3 (NADE_XANC8), annotated as Glutamine-dependent NAD(+) synthetase (EC 6.3.5.1). The UniProt PATHWAY comment explicitly states 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1,' directly supporting Choice C. The annotation is based on HAMAP-Rule MF_02090 (ECO:0000255, computational/curated), with additional support from a 2024 disruption phenotype study (PubMed 38429435). The other options (antifungal biosynthesis, cystathionine synthesis, membrane lipid metabolism) are unrelated to NAD+ synthetase."
  },
  "important_caveats": [
    "The UniProt pathway annotation is based on HAMAP-Rule MF_02090 (ECO:0000255), a computational/curated assignment, not direct enzymatic assay evidence for this specific protein. However, a 2024 disruption phenotype study (PubMed 38429435) provides experimental support for NAD+ biosynthesis function in this organism.",
    "The reviewer identified the accession from dataset metadata; the evaluated model received only the raw sequence and four pathway labels.",
    "The pathway annotation is a broad category ('Cofactor biosynthesis'); the full UniProt line specifies the sub-pathway 'NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1,' but the question only asks for the top-level pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The glutaminase + synthetase architecture is incompatible with antifungal biosynthesis (A), cystathionine gamma-synthase (B, PLP-dependent), or membrane lipid metabolism (D). Only 'Cofactor biosynthesis' (C) is consistent with a glutamine-dependent amidotransferase involved in NAD+ biosynthesis. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0051",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches UniProt entry A0A0H2X6L3 (NADE_XANC8), annotated as Glutamine-dependent NAD(+) synthetase (EC 6.3.5.1). The UniProt PATHWAY comment explicitly states 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1,' directly supporting Choice C. The annotation is based on HAMAP-Rule MF_02090 (ECO:0000255, computational/curated), with additional support from a 2024 disruption phenotype study (PubMed 38429435). The other options (antifungal biosynthesis, cystathionine synthesis, membrane lipid metabolism) are unrelated to NAD+ synthetase.",
    "evidence_ids": ["C1", "C4", "C5", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region contains a glutaminase domain with a recognizable Cys-His-Asp catalytic triad motif (e.g., 'CEQ' near position 65, conserved 'W' residues in the oxyanion hole region), and the C-terminal region displays a synthetase domain with ATP-binding 'G' motifs. This two-domain glutaminase + synthetase architecture is characteristic of glutamine-dependent amidotransferases, which are predominantly involved in cofactor biosynthesis (NAD+, NADP+, folate, etc.). The other three options are clearly inconsistent: antifungal biosynthesis implies NRPS/PKS features absent here; cystathionine gamma-synthase is a PLP-dependent enzyme with entirely different fold; membrane lipid metabolism enzymes lack this amidotransferase architecture. The broad pathway category 'Cofactor biosynthesis' is reachable from recognizing the glutamine amidotransferase fold without needing the exact enzyme name.",
    "missing_item_specific_fact": "Precisely distinguishing NAD+ synthetase from other glutamine amidotransferases (e.g., GMP synthetase, folate synthetase) from sequence alone would require specialized fold recognition or database lookup, but the answer category 'Cofactor biosynthesis' is broad enough that the amidotransferase architecture reasoning suffices.",
    "reason": "The glutaminase + synthetase domain architecture is identifiable from sequence motifs and is strongly associated with cofactor biosynthesis. The three distractors describe pathways catalyzed by structurally unrelated enzymes (NRPS/PKS, PLP-dependent synthase, lipid-modifying enzymes), making them eliminable by general biological reasoning. The broad pathway label 'Cofactor biosynthesis' does not require pinpointing the exact enzyme."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The glutaminase + synthetase architecture is incompatible with antifungal biosynthesis (A), cystathionine gamma-synthase (B, PLP-dependent), or membrane lipid metabolism (D). Only 'Cofactor biosynthesis' (C) is consistent with a glutamine-dependent amidotransferase involved in NAD+ biosynthesis. No other option is defensible."
  },
  "important_caveats": [
    "The UniProt pathway annotation is based on HAMAP-Rule MF_02090 (ECO:0000255), a computational/curated assignment, not direct enzymatic assay evidence for this specific protein. However, a 2024 disruption phenotype study (PubMed 38429435) provides experimental support for NAD+ biosynthesis function in this organism.",
    "The reviewer identified the accession from dataset metadata; the evaluated model received only the raw sequence and four pathway labels.",
    "The pathway annotation is a broad category ('Cofactor biosynthesis'); the full UniProt line specifies the sub-pathway 'NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1,' but the question only asks for the top-level pathway."
  ]
}
```

</details>

## Existing project source checks of Luna’s review

The notes below were prepared for specific claims in the Luna review. They are not independent validation of Qwen’s claims, expert adjudication, or replacement verdicts.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Reviewer-only source evidence

**Both reviewers received this source evidence separately from the original question. It was not available to the original evaluated model.** Source support and reasoning from the original sequence/choices are distinct assessments.

**Accession:** `A0A0H2X6L3` (recovered from dataset image-path metadata, not original question text).  
**Sequence applicability:** historical matched; current matched.  
**Historical cutoff:** 2026-05-07; archived entry version 49. Exact author snapshot unknown.

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/primaryAccession`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
"A0A0H2X6L3"
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/proteinDescription`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
{"alternativeNames":[{"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"NAD(+) synthase [glutamine-hydrolyzing]"}},{"fullName":{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"NAD(+) synthetase"},"shortNames":[{"evidences":[{"evidenceCode":"ECO:0000303","id":"38429435","source":"PubMed"}],"value":"NADS"}]}],"recommendedName":{"ecNumbers":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"6.3.5.1"}],"fullName":{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"Glutamine-dependent NAD(+) synthetase"}}}
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)  
**Locator:** `/comments/2`  
**Scope:** current snapshot; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Retrieved:** 2026-11-02T04:24:06.673007+00:00.  

```json
{"commentType":"PATHWAY","texts":[{"evidences":[{"evidenceCode":"ECO:0000255","id":"MF_02090","source":"HAMAP-Rule"}],"value":"Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1"}]}
```

Source SHA-256: `c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79`.

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 1-16`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
ID   NADE_XANC8              Reviewed;         552 AA.
AC   A0A0H2X6L3;
DT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.
DT   16-SEP-2015, sequence version 1.
DT   28-JAN-2026, entry version 49.
DE   RecName: Full=Glutamine-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_02090};
DE            EC=6.3.5.1 {ECO:0000255|HAMAP-Rule:MF_02090};
DE   AltName: Full=NAD(+) synthase [glutamine-hydrolyzing] {ECO:0000255|HAMAP-Rule:MF_02090};
DE   AltName: Full=NAD(+) synthetase {ECO:0000303|PubMed:38429435};
DE            Short=NADS {ECO:0000303|PubMed:38429435};
GN   Name=nadE {ECO:0000255|HAMAP-Rule:MF_02090};
GN   OrderedLocusNames=XC_1067 {ECO:0000312|EMBL:AAY48137.1};
OS   Xanthomonas campestris pv. campestris (strain 8004).
OC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;
OC   Lysobacterales; Lysobacteraceae; Xanthomonas.
OX   NCBI_TaxID=314565;
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)  
**Locator:** `lines 47-49`  
**Scope:** record released no later than 2026-05-07; actual author source snapshot unknown.  
**Sequence comparison:** matched.  
**Entry / sequence version:** 49 / 1.  
**Retrieved:** 2026-11-02T04:24:10.555808+00:00.  

```text
CC   -!- PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from
CC       deamido-NAD(+) (L-Gln route): step 1/1. {ECO:0000255|HAMAP-
CC       Rule:MF_02090}.
```

Source SHA-256: `fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41`.

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 51. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). UniProt and Gene Ontology credits are retained in [source notices](../THIRD_PARTY_NOTICES.md).
