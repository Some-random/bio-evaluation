# pathway_0130

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0130.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFASRIRSRALGLHPRARFENTRLPASTTGRRYKSDETLNRVSSKITQPKSQGASQAMLYATGLTEEDMSKPQVGISSVWFEGNPCNMHLHDLSAIVRDSVHRAGLVPMRFNSVGVSDGISMGTKGMRYSLQSRELIADGIETVMNAQWYDANVSLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDEKERFDIIRNACPGRGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKTMLREDIKPRDVLTRQAFENAMIVVNILGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYNIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIRPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEERVVDLDIPTEELEKRRKEWKAPPLRYQKGTLKKYCTLVSDASHGCVTDGPI

[Multiple Choices]
A. ubiquinone biosynthesis. .
B. peptidoglycan degradation. .
C. Amino-acid biosynthesis
D. L-valine biosynthesis
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

## Reviewer assessments

## GPT-6 Luna

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched record annotates this protein in amino-acid biosynthesis, including both L-isoleucine and L-valine biosynthesis. The pathway annotations cite experimental evidence, so the broad keyed choice is supported, although the evidence also supports the more specific valine option.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the conserved dihydroxy-acid dehydratase (IlvD/DHAD) family. Knowledge of this family transfers to a role in branched-chain amino-acid biosynthesis, distinguishing the amino-acid pathway choices from ubiquinone biosynthesis and peptidoglycan degradation. The family-level inference supports amino-acid biosynthesis and can also support the offered valine pathway, but does not make valine the enzyme's only pathway.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A recognizable enzyme-family inference provides a meaningful basis for choosing among these options without needing the exact protein's database record. It supports the broad amino-acid category, while the choices' different levels of specificity leave some ambiguity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The protein is annotated in both broad amino-acid biosynthesis and specifically L-valine biosynthesis. Thus C is supported as the broader category and D as a specific pathway; the wording does not clarify whether it wants the broad category or the most specific applicable pathway.


### Important caveats

- The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.
- The sequence-based family inference is transferable; the specific dual pathway annotations come from reviewer-only evidence and were not part of the original input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the conserved dihydroxy-acid dehydratase (IlvD/DHAD) family. Knowledge of this family transfers to a role in branched-chain amino-acid biosynthesis, distinguishing the amino-acid pathway choices from ubiquinone biosynthesis and peptidoglycan degradation. The family-level inference supports amino-acid biosynthesis and can also support the offered valine pathway, but does not make valine the enzyme's only pathway.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A recognizable enzyme-family inference provides a meaningful basis for choosing among these options without needing the exact protein's database record. It supports the broad amino-acid category, while the choices' different levels of specificity leave some ambiguity."
  },
  "case_id": "pathway_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record annotates this protein in amino-acid biosynthesis, including both L-isoleucine and L-valine biosynthesis. The pathway annotations cite experimental evidence, so the broad keyed choice is supported, although the evidence also supports the more specific valine option."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The sequence-based family inference is transferable; the specific dual pathway annotations come from reviewer-only evidence and were not part of the original input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The protein is annotated in both broad amino-acid biosynthesis and specifically L-valine biosynthesis. Thus C is supported as the broader category and D as a specific pathway; the wording does not clarify whether it wants the broad category or the most specific applicable pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record annotates this protein in amino-acid biosynthesis, including both L-isoleucine and L-valine biosynthesis. The pathway annotations cite experimental evidence, so the broad keyed choice is supported, although the evidence also supports the more specific valine option.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the conserved dihydroxy-acid dehydratase (IlvD/DHAD) family. Knowledge of this family transfers to a role in branched-chain amino-acid biosynthesis, distinguishing the amino-acid pathway choices from ubiquinone biosynthesis and peptidoglycan degradation. The family-level inference supports amino-acid biosynthesis and can also support the offered valine pathway, but does not make valine the enzyme's only pathway.",
    "missing_item_specific_fact": "",
    "reason": "A recognizable enzyme-family inference provides a meaningful basis for choosing among these options without needing the exact protein's database record. It supports the broad amino-acid category, while the choices' different levels of specificity leave some ambiguity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The protein is annotated in both broad amino-acid biosynthesis and specifically L-valine biosynthesis. Thus C is supported as the broader category and D as a specific pathway; the wording does not clarify whether it wants the broad category or the most specific applicable pathway."
  },
  "important_caveats": [
    "The reviewer-only evidence matches the supplied sequence, but the author's exact source snapshot is unknown.",
    "The sequence-based family inference is transferable; the specific dual pathway annotations come from reviewer-only evidence and were not part of the original input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry annotates this protein (Dihydroxy-acid dehydratase astD, EC 4.2.1.9) in two pathways both under the umbrella 'Amino-acid biosynthesis': L-isoleucine biosynthesis (step 3/4) and L-valine biosynthesis (step 3/4). Option C 'Amino-acid biosynthesis' is the parent category encompassing both annotated pathways, making it a supported answer. However, option D 'L-valine biosynthesis' is also directly annotated, so D is not contradicted either.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable motifs of the dihydroxy-acid dehydratase (DHAD/IlvD) family, including the conserved C-terminal region with 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPE' and the iron-sulfur cluster-binding 'CxxC...CxxC' motifs. DHAD (EC 4.2.1.9) is a well-characterized enzyme across many organisms that catalyzes the same dehydration reaction in BOTH the valine and isoleucine branched-chain amino acid biosynthesis pathways. A model recognizing the DHAD family would know this enzyme serves multiple amino acid pathways simultaneously, making the broader umbrella 'Amino-acid biosynthesis' (C) a more complete and accurate 'primary pathway' answer than the single specific pathway 'L-valine biosynthesis' (D). Options A (ubiquinone biosynthesis) and B (peptidoglycan degradation) are unrelated to DHAD chemistry and are easily eliminated.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The DHAD family is extensively characterized across bacteria, fungi, and plants. The well-known fact that a single DHAD enzyme serves both valine and isoleucine pathways is transferable family-level knowledge. Recognizing the DHAD motifs in the sequence and applying this family knowledge allows a model to prefer the broader 'Amino-acid biosynthesis' over the narrower 'L-valine biosynthesis' because the enzyme is not exclusive to one pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "C",
  "D"
]
```

> The UniProt entry explicitly annotates this protein in both 'Amino-acid biosynthesis; L-isoleucine biosynthesis' and 'Amino-acid biosynthesis; L-valine biosynthesis.' Option C is the parent umbrella of both, while option D is one of the two specific sub-pathways directly annotated. A model that recognizes DHAD and knows it participates in valine biosynthesis could reasonably select D. The preference for C over D rests on the argument that the protein serves multiple amino acid pathways, making the broader term more appropriate, but D is not incorrect—only less complete.


### Important caveats

- Both C and D are directly annotated in the UniProt entry (ECO:0000269|PubMed:29995859). The choice of C over D is a matter of specificity level, not correctness.
- The protein also has an alternative name 'Aspterric acid biosynthesis cluster protein D,' suggesting a specialized biosynthetic role beyond canonical amino acid pathways, but this is not among the options.
- The DHAD family recognition argument depends on the model identifying conserved motifs in a 598-residue sequence; fungal DHADs may have additional domains (mitochondrial targeting, regulatory insertions) that could obscure motif recognition.
- The reviewer-only evidence confirms the sequence matches UniProt Q0CPG9 exactly, but this accession was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable motifs of the dihydroxy-acid dehydratase (DHAD/IlvD) family, including the conserved C-terminal region with 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPE' and the iron-sulfur cluster-binding 'CxxC...CxxC' motifs. DHAD (EC 4.2.1.9) is a well-characterized enzyme across many organisms that catalyzes the same dehydration reaction in BOTH the valine and isoleucine branched-chain amino acid biosynthesis pathways. A model recognizing the DHAD family would know this enzyme serves multiple amino acid pathways simultaneously, making the broader umbrella 'Amino-acid biosynthesis' (C) a more complete and accurate 'primary pathway' answer than the single specific pathway 'L-valine biosynthesis' (D). Options A (ubiquinone biosynthesis) and B (peptidoglycan degradation) are unrelated to DHAD chemistry and are easily eliminated.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The DHAD family is extensively characterized across bacteria, fungi, and plants. The well-known fact that a single DHAD enzyme serves both valine and isoleucine pathways is transferable family-level knowledge. Recognizing the DHAD motifs in the sequence and applying this family knowledge allows a model to prefer the broader 'Amino-acid biosynthesis' over the narrower 'L-valine biosynthesis' because the enzyme is not exclusive to one pathway."
  },
  "case_id": "pathway_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (Dihydroxy-acid dehydratase astD, EC 4.2.1.9) in two pathways both under the umbrella 'Amino-acid biosynthesis': L-isoleucine biosynthesis (step 3/4) and L-valine biosynthesis (step 3/4). Option C 'Amino-acid biosynthesis' is the parent category encompassing both annotated pathways, making it a supported answer. However, option D 'L-valine biosynthesis' is also directly annotated, so D is not contradicted either."
  },
  "important_caveats": [
    "Both C and D are directly annotated in the UniProt entry (ECO:0000269|PubMed:29995859). The choice of C over D is a matter of specificity level, not correctness.",
    "The protein also has an alternative name 'Aspterric acid biosynthesis cluster protein D,' suggesting a specialized biosynthetic role beyond canonical amino acid pathways, but this is not among the options.",
    "The DHAD family recognition argument depends on the model identifying conserved motifs in a 598-residue sequence; fungal DHADs may have additional domains (mitochondrial targeting, regulatory insertions) that could obscure motif recognition.",
    "The reviewer-only evidence confirms the sequence matches UniProt Q0CPG9 exactly, but this accession was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "C",
      "D"
    ],
    "reason": "The UniProt entry explicitly annotates this protein in both 'Amino-acid biosynthesis; L-isoleucine biosynthesis' and 'Amino-acid biosynthesis; L-valine biosynthesis.' Option C is the parent umbrella of both, while option D is one of the two specific sub-pathways directly annotated. A model that recognizes DHAD and knows it participates in valine biosynthesis could reasonably select D. The preference for C over D rests on the argument that the protein serves multiple amino acid pathways, making the broader term more appropriate, but D is not incorrect—only less complete."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry annotates this protein (Dihydroxy-acid dehydratase astD, EC 4.2.1.9) in two pathways both under the umbrella 'Amino-acid biosynthesis': L-isoleucine biosynthesis (step 3/4) and L-valine biosynthesis (step 3/4). Option C 'Amino-acid biosynthesis' is the parent category encompassing both annotated pathways, making it a supported answer. However, option D 'L-valine biosynthesis' is also directly annotated, so D is not contradicted either.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable motifs of the dihydroxy-acid dehydratase (DHAD/IlvD) family, including the conserved C-terminal region with 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPE' and the iron-sulfur cluster-binding 'CxxC...CxxC' motifs. DHAD (EC 4.2.1.9) is a well-characterized enzyme across many organisms that catalyzes the same dehydration reaction in BOTH the valine and isoleucine branched-chain amino acid biosynthesis pathways. A model recognizing the DHAD family would know this enzyme serves multiple amino acid pathways simultaneously, making the broader umbrella 'Amino-acid biosynthesis' (C) a more complete and accurate 'primary pathway' answer than the single specific pathway 'L-valine biosynthesis' (D). Options A (ubiquinone biosynthesis) and B (peptidoglycan degradation) are unrelated to DHAD chemistry and are easily eliminated.",
    "missing_item_specific_fact": "",
    "reason": "The DHAD family is extensively characterized across bacteria, fungi, and plants. The well-known fact that a single DHAD enzyme serves both valine and isoleucine pathways is transferable family-level knowledge. Recognizing the DHAD motifs in the sequence and applying this family knowledge allows a model to prefer the broader 'Amino-acid biosynthesis' over the narrower 'L-valine biosynthesis' because the enzyme is not exclusive to one pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["C", "D"],
    "reason": "The UniProt entry explicitly annotates this protein in both 'Amino-acid biosynthesis; L-isoleucine biosynthesis' and 'Amino-acid biosynthesis; L-valine biosynthesis.' Option C is the parent umbrella of both, while option D is one of the two specific sub-pathways directly annotated. A model that recognizes DHAD and knows it participates in valine biosynthesis could reasonably select D. The preference for C over D rests on the argument that the protein serves multiple amino acid pathways, making the broader term more appropriate, but D is not incorrect—only less complete."
  },
  "important_caveats": [
    "Both C and D are directly annotated in the UniProt entry (ECO:0000269|PubMed:29995859). The choice of C over D is a matter of specificity level, not correctness.",
    "The protein also has an alternative name 'Aspterric acid biosynthesis cluster protein D,' suggesting a specialized biosynthetic role beyond canonical amino acid pathways, but this is not among the options.",
    "The DHAD family recognition argument depends on the model identifying conserved motifs in a 598-residue sequence; fungal DHADs may have additional domains (mitochondrial targeting, regulatory insertions) that could obscure motif recognition.",
    "The reviewer-only evidence confirms the sequence matches UniProt Q0CPG9 exactly, but this accession was not available to the evaluated model."
  ]
}
```

</details>

## Complete reviewer-only evidence and qualifications

These source excerpts were available to the reviewers. They were not included in the original benchmark-solving input.

**Source applicability:**

```json
{
  "actual_author_source_snapshot": "unknown",
  "benchmark_sequence_length": 598,
  "benchmark_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_entry_audit": {
    "entryVersion": 92,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-10-17",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 598,
  "current_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 90,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q0CPG9",
  "selected_historical_entry_version": 90,
  "selected_historical_record_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "selected_historical_source_sequence_length": 598,
  "selected_historical_source_sequence_sha256": "fa9e543b4d22dcd970aea00f48d66772e78eab78d909318baa5438958e06b376",
  "selected_historical_version": {
    "accession": "Q0CPG9",
    "database": "Swiss-Prot",
    "entryVersion": 90,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ASTD_ASPTN",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q0CPG9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":92,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-10-17\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus terreus (strain NIH 2624 / FGSC A1156)\",\"taxonId\":341663}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein D\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Dihydroxy-acid dehydratase astD, mitochondrial\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"DHAD astD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"29995859\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-valine biosynthesis; L-valine from pyruvate: step 3/4\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/7",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q0CPG9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Yan Y.\",\"Liu Q.\",\"Zang X.\",\"Yuan S.\",\"Bat-Erdene U.\",\"Nguyen C.\",\"Gan J.\",\"Zhou J.\",\"Jacobsen S.E.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"29995859\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-018-0319-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"415\",\"id\":\"29995859\",\"journal\":\"Nature\",\"lastPage\":\"418\",\"publicationDate\":\"2018\",\"title\":\"Resistance-gene-directed discovery of a natural-product herbicide with a new mode of action.\",\"volume\":\"559\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DOMAIN\",\"ACTIVITY REGULATION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:26.147110+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0169738886e0171e22cde2617027b82282487f67fb596ca539c3fec457997b4a",
  "url": "https://rest.uniprot.org/uniprotkb/Q0CPG9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H1",
  "excerpt": "ID   ASTD_ASPTN              Reviewed;         598 AA.\nAC   Q0CPG9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   17-OCT-2006, sequence version 1.\nDT   28-JAN-2026, entry version 90.\nDE   RecName: Full=Dihydroxy-acid dehydratase astD, mitochondrial {ECO:0000303|PubMed:29995859};\nDE            Short=DHAD astD {ECO:0000303|PubMed:29995859};\nDE            EC=4.2.1.9 {ECO:0000269|PubMed:29995859};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:29995859};\nDE   Flags: Precursor;\nGN   Name=astD {ECO:0000303|PubMed:29995859}; ORFNames=ATEG_04415;\nOS   Aspergillus terreus (strain NIH 2624 / FGSC A1156).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=341663;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, DOMAIN,\nRP   ACTIVITY REGULATION, AND PATHWAY.\nRX   PubMed=29995859; DOI=10.1038/s41586-018-0319-4;\nRA   Yan Y., Liu Q., Zang X., Yuan S., Bat-Erdene U., Nguyen C., Gan J.,\nRA   Zhou J., Jacobsen S.E., Tang Y.;\nRT   \"Resistance-gene-directed discovery of a natural-product herbicide with a\nRT   new mode of action.\";\nRL   Nature 559:415-418(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-isoleucine biosynthesis; L-\nCC       isoleucine from 2-oxobutanoate: step 3/4.\nCC       {ECO:0000269|PubMed:29995859}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-79",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90)

```json
{
  "entry_version": 90,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-valine biosynthesis; L-valine from\nCC       pyruvate: step 3/4. {ECO:0000269|PubMed:29995859}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:28.917378+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9bf655407cf1951ee3eade3f48f59afe8492d4b13add34fd5d783ee9fb63fb58",
  "url": "https://rest.uniprot.org/unisave/Q0CPG9?format=txt&versions=90"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
