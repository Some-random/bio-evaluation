# pathway_0125

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0125.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGTTERESDPIAALILDRLSCTEYACSSLSRVNGGLMNFIYRGTLSRPLPDGATTVIVKHAEEYLSGIEGLSLSTYRSVIAAITLSFGYCVMDVESVQTNRYCVALDEVEVAVPRVYKFDAESNTQILEDITGYITVCEFLTSRCTQSTSPAFTTRLGFRLGSWLGGLHAWGEGRSPAEIIGGVEENQEAQDGSFDFFYGNPVRRVEQFPHLLGDCKEVLEQIRDRAAREQKSRTGEKFGFVHGDILSRKSVLIPGDSVTRDQHLRFVIIDWELSQYECHFRECGEVLGDLYLLKRFQDIDGAMSIIQGFLEGYPPLNEDAIFRTAIYLGLFLLANEVTLSTDYPKQQIEDFVILARDLVLAGWHKDRETLAKTVFGPVFFRAMN

[Multiple Choices]
A. Alkaloid biosynthesis
B. Secondary metabolite biosynthesis. .
C. xylan degradation. .
D. Capsule biogenesis
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

> The sequence-matched UniProt entry assigns this protein to secondary metabolite biosynthesis, with experimental-evidence code ECO:0000269 linked to the cited FR901483 biosynthesis study. The archived entry available by the historical cutoff gives the same pathway annotation. This supports B as the recorded pathway, though the excerpts do not independently establish every aspect of the study's experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein's association with the FR901483 biosynthetic cluster, or equivalent target-specific pathway evidence, is needed to assign it to this natural-product pathway from the supplied sequence.


**Reason**

> The sequence alone provides no clear pathway-specific signature that distinguishes secondary-metabolite biosynthesis from alkaloid biosynthesis, xylan degradation, or capsule biogenesis. A pathway assignment here depends on knowing the protein's role in its biosynthetic context; recognizing this exact protein or recalling its annotation would be target-specific lookup, not transferable inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The source supports the broad category B, but the protein is annotated as part of FR901483 biosynthesis, and FR901483 is an alkaloid. Thus A can also describe the pathway at a more specific level; the options do not say whether the broad or specific category is preferred.


### Important caveats

- The source annotation applies to an exact sequence match, but the author's source snapshot is unknown.
- The supplied excerpts support the pathway annotation; they do not provide a direct experimental protocol or independently audited primary-paper results.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's association with the FR901483 biosynthetic cluster, or equivalent target-specific pathway evidence, is needed to assign it to this natural-product pathway from the supplied sequence.",
    "reason": "The sequence alone provides no clear pathway-specific signature that distinguishes secondary-metabolite biosynthesis from alkaloid biosynthesis, xylan degradation, or capsule biogenesis. A pathway assignment here depends on knowing the protein's role in its biosynthetic context; recognizing this exact protein or recalling its annotation would be target-specific lookup, not transferable inference."
  },
  "case_id": "pathway_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns this protein to secondary metabolite biosynthesis, with experimental-evidence code ECO:0000269 linked to the cited FR901483 biosynthesis study. The archived entry available by the historical cutoff gives the same pathway annotation. This supports B as the recorded pathway, though the excerpts do not independently establish every aspect of the study's experimental evidence."
  },
  "important_caveats": [
    "The source annotation applies to an exact sequence match, but the author's source snapshot is unknown.",
    "The supplied excerpts support the pathway annotation; they do not provide a direct experimental protocol or independently audited primary-paper results."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The source supports the broad category B, but the protein is annotated as part of FR901483 biosynthesis, and FR901483 is an alkaloid. Thus A can also describe the pathway at a more specific level; the options do not say whether the broad or specific category is preferred."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns this protein to secondary metabolite biosynthesis, with experimental-evidence code ECO:0000269 linked to the cited FR901483 biosynthesis study. The archived entry available by the historical cutoff gives the same pathway annotation. This supports B as the recorded pathway, though the excerpts do not independently establish every aspect of the study's experimental evidence.",
    "evidence_ids": ["C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein's association with the FR901483 biosynthetic cluster, or equivalent target-specific pathway evidence, is needed to assign it to this natural-product pathway from the supplied sequence.",
    "reason": "The sequence alone provides no clear pathway-specific signature that distinguishes secondary-metabolite biosynthesis from alkaloid biosynthesis, xylan degradation, or capsule biogenesis. A pathway assignment here depends on knowing the protein's role in its biosynthetic context; recognizing this exact protein or recalling its annotation would be target-specific lookup, not transferable inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The source supports the broad category B, but the protein is annotated as part of FR901483 biosynthesis, and FR901483 is an alkaloid. Thus A can also describe the pathway at a more specific level; the options do not say whether the broad or specific category is preferred."
  },
  "important_caveats": [
    "The source annotation applies to an exact sequence match, but the author's source snapshot is unknown.",
    "The supplied excerpts support the pathway annotation; they do not provide a direct experimental protocol or independently audited primary-paper results."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7T8F1J6, sequence match confirmed) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269) from PubMed:33372776 (Zhang et al., JACS 2021, on FR901483 biosynthesis). The protein is identified as Phosphotransferase FrzJ (EC 2.7.1.-), a component of the FR901483 biosynthetic gene cluster in Cladobotryum sp. The sequence is a perfect match (385 aa, SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C6](#evidence-c6), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence can be analyzed for enzymatic class and pathway context. (1) Elimination of C (xylan degradation): Xylanases (GH10, GH11) have well-characterized β-jellyroll folds with conserved catalytic Glu/Asp pairs and compact ~200-aa domains; this 385-aa protein shows no such motifs. (2) Elimination of D (capsule biogenesis): Capsule enzymes are typically glycosyltransferases or polysaccharide synthases with GT-B/GT-A folds and conserved DXD/GXXGD motifs; absent here. (3) Distinguishing A (alkaloid biosynthesis) from B (secondary metabolite biosynthesis): The sequence contains a 'GDSVTRD' region consistent with a P-loop/nucleotide-binding phosphotransferase domain. In fungal biosynthetic gene clusters, phosphotransferases are most commonly tailoring enzymes in NRPS/PKS/hybrid secondary metabolite pathways (activating or modifying intermediates), whereas fungal alkaloid biosynthesis relies on distinct enzyme classes (tryptophan decarboxylases, strictosidine synthases, specific P450s). A phosphotransferase in a fungal biosynthetic context is more parsimoniously assigned to the broader secondary metabolite category. Additionally, 'secondary metabolite biosynthesis' is the standard umbrella pathway annotation used in databases for fungal biosynthetic cluster enzymes, making it the default when the specific sub-pathway (alkaloid vs. peptide vs. polyketide) is not evident from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate C and D with high confidence from the absence of xylanase and glycosyltransferase features. The A-vs-B distinction is probabilistic but supported by the phosphotransferase domain architecture being more characteristic of NRPS/PKS tailoring steps than alkaloid-specific enzymes, and by the convention that broad 'secondary metabolite biosynthesis' is the default pathway annotation for fungal cluster enzymes whose specific compound class is not identifiable from sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Alkaloid biosynthesis is technically a subset of secondary metabolite biosynthesis. Without knowing the specific compound (FR901483, a non-alkaloid cyclic peptide), a model might argue that a phosphotransferase in a fungal biosynthetic cluster could participate in alkaloid tailoring. However, the sequence lacks features of classic alkaloid-biosynthetic enzymes, and the broader category B is the more defensible default for a fungal phosphotransferase in a biosynthetic cluster context. The distinction is probabilistic rather than categorical.


### Important caveats

- The A-vs-B distinction relies on probabilistic enzyme-class-to-pathway associations rather than a definitive sequence signature unique to secondary metabolite (non-alkaloid) biosynthesis.
- The model does not receive organism identity; fungal context is inferred from sequence composition and the general pattern of biosynthetic cluster proteins.
- The phosphotransferase annotation (EC 2.7.1.-) is broad; the specific substrate and role in FR901483 biosynthesis required experimental validation (PubMed:33372776).
- Options B and D have trailing periods in the original text, likely a formatting artifact and not a meaningful distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence can be analyzed for enzymatic class and pathway context. (1) Elimination of C (xylan degradation): Xylanases (GH10, GH11) have well-characterized β-jellyroll folds with conserved catalytic Glu/Asp pairs and compact ~200-aa domains; this 385-aa protein shows no such motifs. (2) Elimination of D (capsule biogenesis): Capsule enzymes are typically glycosyltransferases or polysaccharide synthases with GT-B/GT-A folds and conserved DXD/GXXGD motifs; absent here. (3) Distinguishing A (alkaloid biosynthesis) from B (secondary metabolite biosynthesis): The sequence contains a 'GDSVTRD' region consistent with a P-loop/nucleotide-binding phosphotransferase domain. In fungal biosynthetic gene clusters, phosphotransferases are most commonly tailoring enzymes in NRPS/PKS/hybrid secondary metabolite pathways (activating or modifying intermediates), whereas fungal alkaloid biosynthesis relies on distinct enzyme classes (tryptophan decarboxylases, strictosidine synthases, specific P450s). A phosphotransferase in a fungal biosynthetic context is more parsimoniously assigned to the broader secondary metabolite category. Additionally, 'secondary metabolite biosynthesis' is the standard umbrella pathway annotation used in databases for fungal biosynthetic cluster enzymes, making it the default when the specific sub-pathway (alkaloid vs. peptide vs. polyketide) is not evident from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C and D with high confidence from the absence of xylanase and glycosyltransferase features. The A-vs-B distinction is probabilistic but supported by the phosphotransferase domain architecture being more characteristic of NRPS/PKS tailoring steps than alkaloid-specific enzymes, and by the convention that broad 'secondary metabolite biosynthesis' is the default pathway annotation for fungal cluster enzymes whose specific compound class is not identifiable from sequence."
  },
  "case_id": "pathway_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C6",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8F1J6, sequence match confirmed) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269) from PubMed:33372776 (Zhang et al., JACS 2021, on FR901483 biosynthesis). The protein is identified as Phosphotransferase FrzJ (EC 2.7.1.-), a component of the FR901483 biosynthetic gene cluster in Cladobotryum sp. The sequence is a perfect match (385 aa, SHA-256 confirmed)."
  },
  "important_caveats": [
    "The A-vs-B distinction relies on probabilistic enzyme-class-to-pathway associations rather than a definitive sequence signature unique to secondary metabolite (non-alkaloid) biosynthesis.",
    "The model does not receive organism identity; fungal context is inferred from sequence composition and the general pattern of biosynthetic cluster proteins.",
    "The phosphotransferase annotation (EC 2.7.1.-) is broad; the specific substrate and role in FR901483 biosynthesis required experimental validation (PubMed:33372776).",
    "Options B and D have trailing periods in the original text, likely a formatting artifact and not a meaningful distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Alkaloid biosynthesis is technically a subset of secondary metabolite biosynthesis. Without knowing the specific compound (FR901483, a non-alkaloid cyclic peptide), a model might argue that a phosphotransferase in a fungal biosynthetic cluster could participate in alkaloid tailoring. However, the sequence lacks features of classic alkaloid-biosynthetic enzymes, and the broader category B is the more defensible default for a fungal phosphotransferase in a biosynthetic cluster context. The distinction is probabilistic rather than categorical."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8F1J6, sequence match confirmed) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269) from PubMed:33372776 (Zhang et al., JACS 2021, on FR901483 biosynthesis). The protein is identified as Phosphotransferase FrzJ (EC 2.7.1.-), a component of the FR901483 biosynthetic gene cluster in Cladobotryum sp. The sequence is a perfect match (385 aa, SHA-256 confirmed).",
    "evidence_ids": ["C5", "C4", "C6", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence can be analyzed for enzymatic class and pathway context. (1) Elimination of C (xylan degradation): Xylanases (GH10, GH11) have well-characterized β-jellyroll folds with conserved catalytic Glu/Asp pairs and compact ~200-aa domains; this 385-aa protein shows no such motifs. (2) Elimination of D (capsule biogenesis): Capsule enzymes are typically glycosyltransferases or polysaccharide synthases with GT-B/GT-A folds and conserved DXD/GXXGD motifs; absent here. (3) Distinguishing A (alkaloid biosynthesis) from B (secondary metabolite biosynthesis): The sequence contains a 'GDSVTRD' region consistent with a P-loop/nucleotide-binding phosphotransferase domain. In fungal biosynthetic gene clusters, phosphotransferases are most commonly tailoring enzymes in NRPS/PKS/hybrid secondary metabolite pathways (activating or modifying intermediates), whereas fungal alkaloid biosynthesis relies on distinct enzyme classes (tryptophan decarboxylases, strictosidine synthases, specific P450s). A phosphotransferase in a fungal biosynthetic context is more parsimoniously assigned to the broader secondary metabolite category. Additionally, 'secondary metabolite biosynthesis' is the standard umbrella pathway annotation used in databases for fungal biosynthetic cluster enzymes, making it the default when the specific sub-pathway (alkaloid vs. peptide vs. polyketide) is not evident from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate C and D with high confidence from the absence of xylanase and glycosyltransferase features. The A-vs-B distinction is probabilistic but supported by the phosphotransferase domain architecture being more characteristic of NRPS/PKS tailoring steps than alkaloid-specific enzymes, and by the convention that broad 'secondary metabolite biosynthesis' is the default pathway annotation for fungal cluster enzymes whose specific compound class is not identifiable from sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Alkaloid biosynthesis is technically a subset of secondary metabolite biosynthesis. Without knowing the specific compound (FR901483, a non-alkaloid cyclic peptide), a model might argue that a phosphotransferase in a fungal biosynthetic cluster could participate in alkaloid tailoring. However, the sequence lacks features of classic alkaloid-biosynthetic enzymes, and the broader category B is the more defensible default for a fungal phosphotransferase in a biosynthetic cluster context. The distinction is probabilistic rather than categorical."
  },
  "important_caveats": [
    "The A-vs-B distinction relies on probabilistic enzyme-class-to-pathway associations rather than a definitive sequence signature unique to secondary metabolite (non-alkaloid) biosynthesis.",
    "The model does not receive organism identity; fungal context is inferred from sequence composition and the general pattern of biosynthetic cluster proteins.",
    "The phosphotransferase annotation (EC 2.7.1.-) is broad; the specific substrate and role in FR901483 biosynthesis required experimental validation (PubMed:33372776).",
    "Options B and D have trailing periods in the original text, likely a formatting artifact and not a meaningful distinction."
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
  "benchmark_sequence_length": 385,
  "benchmark_sequence_sha256": "c12954e7dfb6e61db6f47103df90fa231f2f74664773e0f3f3cd83cda3251164",
  "current_entry_audit": {
    "entryVersion": 8,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c8973cce1ed0e2fab533a94cb1b8b2dc4cfa81417a13963fef0bf5204d549a83",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 385,
  "current_source_sequence_sha256": "c12954e7dfb6e61db6f47103df90fa231f2f74664773e0f3f3cd83cda3251164",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 6,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8F1J6",
  "selected_historical_entry_version": 6,
  "selected_historical_record_sha256": "a3c8964073737ce02aefe4d7b1c7dc5803711f2bade9edceed980e3bae3f99f8",
  "selected_historical_source_sequence_length": 385,
  "selected_historical_source_sequence_sha256": "c12954e7dfb6e61db6f47103df90fa231f2f74664773e0f3f3cd83cda3251164",
  "selected_historical_version": {
    "accession": "A0A7T8F1J6",
    "database": "Swiss-Prot",
    "entryVersion": 6,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZJ_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8F1J6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:50.675828+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8973cce1ed0e2fab533a94cb1b8b2dc4cfa81417a13963fef0bf5204d549a83",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":8,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:50.675828+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8973cce1ed0e2fab533a94cb1b8b2dc4cfa81417a13963fef0bf5204d549a83",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:50.675828+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8973cce1ed0e2fab533a94cb1b8b2dc4cfa81417a13963fef0bf5204d549a83",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis clusters protein J\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"2.7.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Phosphotransferase FrzJ\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:50.675828+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8973cce1ed0e2fab533a94cb1b8b2dc4cfa81417a13963fef0bf5204d549a83",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:50.675828+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8973cce1ed0e2fab533a94cb1b8b2dc4cfa81417a13963fef0bf5204d549a83",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:50.675828+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c8973cce1ed0e2fab533a94cb1b8b2dc4cfa81417a13963fef0bf5204d549a83",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1J6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1J6?format=txt&versions=6)

```json
{
  "entry_version": 6,
  "evidence_id": "H1",
  "excerpt": "ID   FRZJ_CLASX              Reviewed;         385 AA.\nAC   A0A7T8F1J6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 6.\nDE   RecName: Full=Phosphotransferase FrzJ {ECO:0000303|PubMed:33372776};\nDE            EC=2.7.1.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis clusters protein J {ECO:0000303|PubMed:33372776};\nGN   Name=FrzJ {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.489845+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a3c8964073737ce02aefe4d7b1c7dc5803711f2bade9edceed980e3bae3f99f8",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1J6?format=txt&versions=6"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1J6?format=txt&versions=6)

```json
{
  "entry_version": 6,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.489845+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a3c8964073737ce02aefe4d7b1c7dc5803711f2bade9edceed980e3bae3f99f8",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1J6?format=txt&versions=6"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1J6?format=txt&versions=6)

```json
{
  "entry_version": 6,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis.\nCC       {ECO:0000269|PubMed:33372776}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:33.489845+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "a3c8964073737ce02aefe4d7b1c7dc5803711f2bade9edceed980e3bae3f99f8",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1J6?format=txt&versions=6"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 125. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
