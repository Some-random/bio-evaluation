# GO_molecular_function_0069

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0069.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — FMN binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDNSSRLFSPLRLGKCQLRHRVAMSPLTRFRADDLSVQMPFAKEYYAQRASVPGTFLVSEATSISRESVGFSNVPGIWNAEQVRAWKEIADDVHCKGSFLFLQLWATGRSATPERLQSGDFDFASSSAVPMEPGGAVPRELTEEDIHDLIARFAEAARRAIDAGMDGIELHAANGYLIDQFTQASCNQRTDRWGGSIENRARFAIEVTRSVVAAVGADRVGVKLSPWGKIQGMGTMQDLVPQFQYLVSELRDMGLAYLRLSNSRWIDGVPQEEEDNSIYVHTWGASRPVLLEGGYDPISAQKEADIRFNGYDAVIAFGRFFISNPDLPFRIKAGVDLQKYNRDTFYTPISEKGYIDYPFSTAFLEEHSSKASLKL

[Multiple Choices]
A. peptide binding
B. FMN binding
C. amidophosphoribosyltransferase activity
D. flavin adenine dinucleotide binding
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The matched-sequence record annotates FMN binding by IEA:InterPro (C7, H5). Separately, source-linked functional evidence identifies FrzD as a flavin-dependent reductase, supporting a flavin cofactor role, though the supplied experimental function and reaction do not themselves specify FMN rather than FAD.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 375-residue sequence is compatible with a soluble flavin-dependent oxidoreductase, and its OYE-like family pattern can be recognized through transferable sequence-family knowledge. Old-yellow-enzyme-family reductases characteristically use FMN; that family-level regularity favors FMN binding (B) over FAD binding (D), while the other choices describe unrelated binding or catalytic functions.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence can meaningfully distinguish FMN from FAD without knowing this protein's recorded annotation. It is probabilistic: sequence recognition alone does not establish direct cofactor-binding measurements or rule out every unusual family member.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options are meaningfully distinguished by the inferred OYE-like flavoprotein family; no second choice is comparably supported by the sequence and transferable family knowledge.


### Important caveats

- The explicit FMN-binding annotation supplied here is computational (IEA:InterPro), not direct experimental evidence of FMN binding.
- Reviewer-only source identity and annotations were not part of the original model input and are not used as the basis for the transferability judgment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 375-residue sequence is compatible with a soluble flavin-dependent oxidoreductase, and its OYE-like family pattern can be recognized through transferable sequence-family knowledge. Old-yellow-enzyme-family reductases characteristically use FMN; that family-level regularity favors FMN binding (B) over FAD binding (D), while the other choices describe unrelated binding or catalytic functions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can meaningfully distinguish FMN from FAD without knowing this protein's recorded annotation. It is probabilistic: sequence recognition alone does not establish direct cofactor-binding measurements or rule out every unusual family member."
  },
  "case_id": "GO_molecular_function_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence record annotates FMN binding by IEA:InterPro (C7, H5). Separately, source-linked functional evidence identifies FrzD as a flavin-dependent reductase, supporting a flavin cofactor role, though the supplied experimental function and reaction do not themselves specify FMN rather than FAD."
  },
  "important_caveats": [
    "The explicit FMN-binding annotation supplied here is computational (IEA:InterPro), not direct experimental evidence of FMN binding.",
    "Reviewer-only source identity and annotations were not part of the original model input and are not used as the basis for the transferability judgment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are meaningfully distinguished by the inferred OYE-like flavoprotein family; no second choice is comparably supported by the sequence and transferable family knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence record annotates FMN binding by IEA:InterPro (C7, H5). Separately, source-linked functional evidence identifies FrzD as a flavin-dependent reductase, supporting a flavin cofactor role, though the supplied experimental function and reaction do not themselves specify FMN rather than FAD.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 375-residue sequence is compatible with a soluble flavin-dependent oxidoreductase, and its OYE-like family pattern can be recognized through transferable sequence-family knowledge. Old-yellow-enzyme-family reductases characteristically use FMN; that family-level regularity favors FMN binding (B) over FAD binding (D), while the other choices describe unrelated binding or catalytic functions.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can meaningfully distinguish FMN from FAD without knowing this protein's recorded annotation. It is probabilistic: sequence recognition alone does not establish direct cofactor-binding measurements or rule out every unusual family member."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options are meaningfully distinguished by the inferred OYE-like flavoprotein family; no second choice is comparably supported by the sequence and transferable family knowledge."
  },
  "important_caveats": [
    "The explicit FMN-binding annotation supplied here is computational (IEA:InterPro), not direct experimental evidence of FMN binding.",
    "Reviewer-only source identity and annotations were not part of the original model input and are not used as the basis for the transferability judgment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7T8F1M9, FRZD_CLASX) is experimentally confirmed as a 'Flavin-dependent old-yellow enzyme FrzD' (Flavin-dependent OYE) with ECO:0000269 (PubMed:33372776). The GO annotation GO:0010181 (FMN binding) is present, though via IEA:InterPro (computational). The OYE family is universally FMN-dependent as a defining family characteristic, and the experimental data confirm both flavin dependence and OYE family membership. The catalytic reaction uses NADPH as electron donor, consistent with FMN-mediated hydride transfer in OYE enzymes. The answer is supported by the combination of experimental family assignment and the well-established FMN-dependence of the OYE family.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein sequence (~375 aa) contains motifs characteristic of the Old Yellow Enzyme (OYE) family, including the conserved 'WGASRP...GYDP' region (residues ~280-300: 'WGASRPVLLEGGYDP') and a His-containing FMN-binding region ('HCKGS'). The OYE family is one of the most well-characterized FMN-dependent enzyme families; its very name derives from the yellow FMN prosthetic group. Critically, the OYE family uses FMN, NOT FAD—this is a defining family-level distinction. FAD-dependent flavoproteins typically employ Rossmann folds (GxGxxG motifs) and different structural architectures, neither of which is present here. The ~375 aa length is also characteristic of OYE (FAD-dependent flavoproteins tend to be larger or have different domain organization). Options A (peptide binding) and C (amidophosphoribosyltransferase activity) are mechanistically incompatible with a flavin-dependent oxidoreductase. The B-vs-D distinction (FMN vs FAD) is resolved by recognizing the OYE family fold and motifs, which are transferable knowledge from the well-studied yeast OYE1 and related bacterial OYEs.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The OYE family is extensively characterized across multiple organisms. The conserved 'WGASRP' and 'GYDP' motifs, the ~375 aa length, and the overall fold architecture are recognizable family signatures. A model trained on protein families can identify OYE membership from these sequence features and apply the well-known rule that OYE enzymes bind FMN (not FAD). This is legitimate family-level transfer from other OYE proteins (yeast OYE1, bacterial OYEs, etc.), not memorization of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While both B (FMN) and D (FAD) are 'flavin binding,' the OYE family distinction is well-established: OYE enzymes are FMN-dependent, not FAD-dependent. The sequence motifs and family architecture clearly point to OYE rather than a FAD-binding flavoprotein. Options A and C are mechanistically incompatible with the observed oxidoreductase features. No genuine ambiguity among the offered choices.


### Important caveats

- The GO FMN-binding annotation is IEA:InterPro (computational inference from domain matching), not direct experimental FMN-binding measurement. However, the OYE family's FMN dependence is a defining and experimentally validated family characteristic.
- The experimental evidence (PubMed:33372776) confirms flavin dependence and OYE family membership but does not independently demonstrate FMN vs FAD in a binding assay for this specific protein.
- The 'WGASRP' and 'GYDP' motifs are OYE-family conserved regions; recognition of these as OYE signatures requires familiarity with the family but is legitimate transferable knowledge.
- The sequence is 375 aa, consistent with OYE family size. FAD-dependent flavoproteins with Rossmann folds are structurally distinct.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein sequence (~375 aa) contains motifs characteristic of the Old Yellow Enzyme (OYE) family, including the conserved 'WGASRP...GYDP' region (residues ~280-300: 'WGASRPVLLEGGYDP') and a His-containing FMN-binding region ('HCKGS'). The OYE family is one of the most well-characterized FMN-dependent enzyme families; its very name derives from the yellow FMN prosthetic group. Critically, the OYE family uses FMN, NOT FAD—this is a defining family-level distinction. FAD-dependent flavoproteins typically employ Rossmann folds (GxGxxG motifs) and different structural architectures, neither of which is present here. The ~375 aa length is also characteristic of OYE (FAD-dependent flavoproteins tend to be larger or have different domain organization). Options A (peptide binding) and C (amidophosphoribosyltransferase activity) are mechanistically incompatible with a flavin-dependent oxidoreductase. The B-vs-D distinction (FMN vs FAD) is resolved by recognizing the OYE family fold and motifs, which are transferable knowledge from the well-studied yeast OYE1 and related bacterial OYEs.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The OYE family is extensively characterized across multiple organisms. The conserved 'WGASRP' and 'GYDP' motifs, the ~375 aa length, and the overall fold architecture are recognizable family signatures. A model trained on protein families can identify OYE membership from these sequence features and apply the well-known rule that OYE enzymes bind FMN (not FAD). This is legitimate family-level transfer from other OYE proteins (yeast OYE1, bacterial OYEs, etc.), not memorization of this specific protein's annotation."
  },
  "case_id": "GO_molecular_function_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H1",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8F1M9, FRZD_CLASX) is experimentally confirmed as a 'Flavin-dependent old-yellow enzyme FrzD' (Flavin-dependent OYE) with ECO:0000269 (PubMed:33372776). The GO annotation GO:0010181 (FMN binding) is present, though via IEA:InterPro (computational). The OYE family is universally FMN-dependent as a defining family characteristic, and the experimental data confirm both flavin dependence and OYE family membership. The catalytic reaction uses NADPH as electron donor, consistent with FMN-mediated hydride transfer in OYE enzymes. The answer is supported by the combination of experimental family assignment and the well-established FMN-dependence of the OYE family."
  },
  "important_caveats": [
    "The GO FMN-binding annotation is IEA:InterPro (computational inference from domain matching), not direct experimental FMN-binding measurement. However, the OYE family's FMN dependence is a defining and experimentally validated family characteristic.",
    "The experimental evidence (PubMed:33372776) confirms flavin dependence and OYE family membership but does not independently demonstrate FMN vs FAD in a binding assay for this specific protein.",
    "The 'WGASRP' and 'GYDP' motifs are OYE-family conserved regions; recognition of these as OYE signatures requires familiarity with the family but is legitimate transferable knowledge.",
    "The sequence is 375 aa, consistent with OYE family size. FAD-dependent flavoproteins with Rossmann folds are structurally distinct."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While both B (FMN) and D (FAD) are 'flavin binding,' the OYE family distinction is well-established: OYE enzymes are FMN-dependent, not FAD-dependent. The sequence motifs and family architecture clearly point to OYE rather than a FAD-binding flavoprotein. Options A and C are mechanistically incompatible with the observed oxidoreductase features. No genuine ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8F1M9, FRZD_CLASX) is experimentally confirmed as a 'Flavin-dependent old-yellow enzyme FrzD' (Flavin-dependent OYE) with ECO:0000269 (PubMed:33372776). The GO annotation GO:0010181 (FMN binding) is present, though via IEA:InterPro (computational). The OYE family is universally FMN-dependent as a defining family characteristic, and the experimental data confirm both flavin dependence and OYE family membership. The catalytic reaction uses NADPH as electron donor, consistent with FMN-mediated hydride transfer in OYE enzymes. The answer is supported by the combination of experimental family assignment and the well-established FMN-dependence of the OYE family.",
    "evidence_ids": ["C4", "C5", "C7", "H1", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein sequence (~375 aa) contains motifs characteristic of the Old Yellow Enzyme (OYE) family, including the conserved 'WGASRP...GYDP' region (residues ~280-300: 'WGASRPVLLEGGYDP') and a His-containing FMN-binding region ('HCKGS'). The OYE family is one of the most well-characterized FMN-dependent enzyme families; its very name derives from the yellow FMN prosthetic group. Critically, the OYE family uses FMN, NOT FAD—this is a defining family-level distinction. FAD-dependent flavoproteins typically employ Rossmann folds (GxGxxG motifs) and different structural architectures, neither of which is present here. The ~375 aa length is also characteristic of OYE (FAD-dependent flavoproteins tend to be larger or have different domain organization). Options A (peptide binding) and C (amidophosphoribosyltransferase activity) are mechanistically incompatible with a flavin-dependent oxidoreductase. The B-vs-D distinction (FMN vs FAD) is resolved by recognizing the OYE family fold and motifs, which are transferable knowledge from the well-studied yeast OYE1 and related bacterial OYEs.",
    "missing_item_specific_fact": "",
    "reason": "The OYE family is extensively characterized across multiple organisms. The conserved 'WGASRP' and 'GYDP' motifs, the ~375 aa length, and the overall fold architecture are recognizable family signatures. A model trained on protein families can identify OYE membership from these sequence features and apply the well-known rule that OYE enzymes bind FMN (not FAD). This is legitimate family-level transfer from other OYE proteins (yeast OYE1, bacterial OYEs, etc.), not memorization of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While both B (FMN) and D (FAD) are 'flavin binding,' the OYE family distinction is well-established: OYE enzymes are FMN-dependent, not FAD-dependent. The sequence motifs and family architecture clearly point to OYE rather than a FAD-binding flavoprotein. Options A and C are mechanistically incompatible with the observed oxidoreductase features. No genuine ambiguity among the offered choices."
  },
  "important_caveats": [
    "The GO FMN-binding annotation is IEA:InterPro (computational inference from domain matching), not direct experimental FMN-binding measurement. However, the OYE family's FMN dependence is a defining and experimentally validated family characteristic.",
    "The experimental evidence (PubMed:33372776) confirms flavin dependence and OYE family membership but does not independently demonstrate FMN vs FAD in a binding assay for this specific protein.",
    "The 'WGASRP' and 'GYDP' motifs are OYE-family conserved regions; recognition of these as OYE signatures requires familiarity with the family but is legitimate transferable knowledge.",
    "The sequence is 375 aa, consistent with OYE family size. FAD-dependent flavoproteins with Rossmann folds are structurally distinct."
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
  "benchmark_sequence_length": 375,
  "benchmark_sequence_sha256": "48d35685f95428a133d889977d9437954326f248d7bbb25058ab859a2c365157",
  "current_entry_audit": {
    "entryVersion": 13,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 375,
  "current_source_sequence_sha256": "48d35685f95428a133d889977d9437954326f248d7bbb25058ab859a2c365157",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 11,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8F1M9",
  "selected_historical_entry_version": 11,
  "selected_historical_record_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "selected_historical_source_sequence_length": 375,
  "selected_historical_source_sequence_sha256": "48d35685f95428a133d889977d9437954326f248d7bbb25058ab859a2c365157",
  "selected_historical_version": {
    "accession": "A0A7T8F1M9",
    "database": "Swiss-Prot",
    "entryVersion": 11,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZD_CLASX",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8F1M9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":13,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis cluster protein D\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Flavin-dependent old-yellow enzyme FrzD\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Flavin-dependent OYE\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"1.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Aldehyde reductase FrzD\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Aldehyde reductase; part of the gene cluster that mediates the biosynthesis of the alkaloid (-)-FR901483, a potent immunosuppressant that shows efficacy in animal models and a probable inhibitor of purine nucleotide biosynthesis by targeting phosphoribosylpyrophosphate amidotransferase (PPAT) (PubMed:33372776). Within the pathway, FrzD reduces the dienone portion of the pathway intermediates to cyclohexanone (PubMed:33372776). The biosynthesis of (-)-FR901483 starts with the condensation of two L-tyrosines to yield (S,S)-dityrosyl-piperazine. This process occurs in 3 steps with the non-canonical nonribosomal peptide synthetase FrzA catalyzing the reduction of L-tyrosine into L-tyrosinal, the spontaneous condensation of 2 L-tyrosinal units, and the subsequent reduction by the NmrA-like family domain-containing oxidoreductase FrzB. The cytochrome P450 monooxygenase FrzC then performs coupling between N10 and C1' to morph the piperazine into a 1,4-diazabicyclo[3.2.1]octane spiro-fused to a 2,5-cyclohexadienone. The dienone portion is further reduced to cyclohexanone by the flavin-dependent reductase FrzD. The methyltranserases (MTs) FrzE and FrzF are then involved in the methylation at the C10' amine and the C4 phenolic oxygen, respectively. The order of the two MTs appear to be interchangeable. Cleavage of the C9-N10' bond by the dioxygenase FrzG then leads to formation of a conjugated iminium. In addition to the oxidation of C9, an additional dehydrogenation between C7 and C8 can occur to give a likely shunt product. The next biosynthetic step is the intramolecular aldol condensation catalyzed by the newly identified aldolase FrzH to yield an aza-tricyclic product with the formation of a C9-C3' bond (PubMed:33372776). The short-chain dehydrogenase/reductase FrzI then produces dephospho-(-)-FR901483 that is phosphorylated at C4'-OH into (-)-FR901483 by the phosphotransferase FrzJ (PubMed:33372776). The only unassigned enzyme in the cluster is the second cytochrome P450 monooxygenase FrzL (PubMed:33372776)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:83584\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"name\":\"(1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexane]-2',5'-dien-4'-one + 2 NADPH + 2 H(+) = (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + 2 NADP(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:83583\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:233174\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:233175\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0010181\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:FMN binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0003959\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:NADPH dehydrogenase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:51.159757+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c38628844912ac2c4aa489f4067b5327e7aad3e6384ffb308551b50b6f0b30ee",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H1",
  "excerpt": "ID   FRZD_CLASX              Reviewed;         375 AA.\nAC   A0A7T8F1M9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   18-JUN-2025, entry version 11.\nDE   RecName: Full=Aldehyde reductase FrzD {ECO:0000303|PubMed:33372776};\nDE            EC=1.3.1.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein D {ECO:0000303|PubMed:33372776};\nDE   AltName: Full=Flavin-dependent old-yellow enzyme FrzD {ECO:0000303|PubMed:33372776};\nDE            Short=Flavin-dependent OYE {ECO:0000303|PubMed:33372776};\nGN   Name=FrzD {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Aldehyde reductase; part of the gene cluster that mediates\nCC       the biosynthesis of the alkaloid (-)-FR901483, a potent\nCC       immunosuppressant that shows efficacy in animal models and a probable\nCC       inhibitor of purine nucleotide biosynthesis by targeting\nCC       phosphoribosylpyrophosphate amidotransferase (PPAT) (PubMed:33372776).\nCC       Within the pathway, FrzD reduces the dienone portion of the pathway\nCC       intermediates to cyclohexanone (PubMed:33372776). The biosynthesis of\nCC       (-)-FR901483 starts with the condensation of two L-tyrosines to yield\nCC       (S,S)-dityrosyl-piperazine. This process occurs in 3 steps with the\nCC       non-canonical nonribosomal peptide synthetase FrzA catalyzing the\nCC       reduction of L-tyrosine into L-tyrosinal, the spontaneous condensation\nCC       of 2 L-tyrosinal units, and the subsequent reduction by the NmrA-like\nCC       family domain-containing oxidoreductase FrzB. The cytochrome P450\nCC       monooxygenase FrzC then performs coupling between N10 and C1' to morph\nCC       the piperazine into a 1,4-diazabicyclo[3.2.1]octane spiro-fused to a\nCC       2,5-cyclohexadienone. The dienone portion is further reduced to\nCC       cyclohexanone by the flavin-dependent reductase FrzD. The\nCC       methyltranserases (MTs) FrzE and FrzF are then involved in the\nCC       methylation at the C10' amine and the C4 phenolic oxygen, respectively.\nCC       The order of the two MTs appear to be interchangeable. Cleavage of the\nCC       C9-N10' bond by the dioxygenase FrzG then leads to formation of a\nCC       conjugated iminium. In addition to the oxidation of C9, an additional\nCC       dehydrogenation between C7 and C8 can occur to give a likely shunt\nCC       product. The next biosynthetic step is the intramolecular aldol\nCC       condensation catalyzed by the newly identified aldolase FrzH to yield\nCC       an aza-tricyclic product with the formation of a C9-C3' bond\nCC       (PubMed:33372776). The short-chain dehydrogenase/reductase FrzI then\nCC       produces dephospho-(-)-FR901483 that is phosphorylated at C4'-OH into\nCC       (-)-FR901483 by the phosphotransferase FrzJ (PubMed:33372776). The only\nCC       unassigned enzyme in the cluster is the second cytochrome P450\nCC       monooxygenase FrzL (PubMed:33372776). {ECO:0000269|PubMed:33372776}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-\nCC         diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexane]-2',5'-dien-4'-one +\nCC         2 NADPH + 2 H(+) = (1S,4S)-4-[(4-hydroxyphenyl)methyl]-2,5-\nCC         diazaspiro[bicyclo[3.2.1]octane-6,1'-cyclohexan]-4'-one + 2 NADP(+);\nCC         Xref=Rhea:RHEA:83583, ChEBI:CHEBI:15378, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:233174, ChEBI:CHEBI:233175;\nCC         Evidence={ECO:0000269|PubMed:33372776};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:83584;\nCC         Evidence={ECO:0000269|PubMed:33372776};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0010181; F:FMN binding; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 80-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11)

```json
{
  "entry_version": 11,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0003959; F:NADPH dehydrogenase activity; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:35.126419+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd48d108f45a92963462c2f0a750dcecfac5cc36c43941b4ca5d31b971333839",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M9?format=txt&versions=11"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004044\nname: amidophosphoribosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: 5-phospho-beta-D-ribosylamine + L-glutamate + diphosphate = 5-phospho-alpha-D-ribose 1-diphosphate + L-glutamine + H2O.\" [EC:2.4.2.14, RHEA:14905]\nsynonym: \"5'-phosphoribosylpyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"5-phosphoribosyl-1-pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"5-phosphoribosylamine:diphosphate phospho-alpha-D-ribosyltransferase (glutamate-amidating)\" RELATED [EC:2.4.2.14]\nsynonym: \"5-phosphororibosyl-1-pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"alpha-5-phosphoribosyl-1-pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"glutamine 5-phosphoribosylpyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"glutamine phosphoribosyldiphosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"glutamine phosphoribosylpyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"glutamine ribosylpyrophosphate 5-phosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"phosphoribose pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"phosphoribosyl pyrophosphate amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"phosphoribosyldiphosphate 5-amidotransferase activity\" RELATED [EC:2.4.2.14]\nsynonym: \"phosphoribosylpyrophosphate glutamyl amidotransferase activity\" RELATED [EC:2.4.2.14]\nxref: EC:2.4.2.14\nxref: KEGG_REACTION:R01072\nxref: MetaCyc:PRPPAMIDOTRANS-RXN\nxref: Reactome:R-HSA-73815 \"5-phospho-alpha-D-ribose 1-diphosphate (PRPP) + H2O + L-glutamine <=> 5-phosphoribosylamine + L-glutamate +pyrophosphate\"\nxref: RHEA:14905\nis_a: GO:0016763 ! pentosyltransferase activity\nproperty_value: skos:exactMatch EC:2.4.2.14\nproperty_value: skos:exactMatch RHEA:14905\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004044",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 34028-34054",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0010181\nname: FMN binding\nnamespace: molecular_function\ndef: \"Binding to flavin mono nucleotide. Flavin mono nucleotide (FMN) is the coenzyme or the prosthetic group of various flavoprotein oxidoreductase enzymes.\" [GOC:tb]\nsynonym: \"flavin mononucleotide binding\" EXACT []\nis_a: GO:0032553 ! ribonucleotide binding\nis_a: GO:0043168 ! anion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0010181",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 103623-103631",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0042277\nname: peptide binding\nnamespace: molecular_function\ndef: \"Binding to a peptide, an organic compound comprising two or more amino acids linked by peptide bonds.\" [GOC:jl]\nsubset: goslim_chembl\nsubset: goslim_pir\nis_a: GO:0005488 ! binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042277",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 235888-235896",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0050660\nname: flavin adenine dinucleotide binding\nnamespace: molecular_function\ndef: \"Binding to FAD, flavin-adenine dinucleotide, the coenzyme or the prosthetic group of various flavoprotein oxidoreductase enzymes, in either the oxidized form, FAD, or the reduced form, FADH2.\" [GOC:ai, GOC:imk, ISBN:0198506732]\nsynonym: \"FAD or FADH2 binding\" EXACT []\nsynonym: \"flavine-adenine dinucleotide binding\" EXACT []\nis_a: GO:0000166 ! nucleotide binding\nis_a: GO:0043168 ! anion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0050660",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 318393-318402",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 69. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
