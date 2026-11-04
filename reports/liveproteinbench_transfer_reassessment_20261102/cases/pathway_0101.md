# pathway_0101

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0101.txt)

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
MTFIIAVVGATGNQGGSVARSLVQNPSFSVRAITRSPDSQASRSLLSAGAEVVKADGFNGEEMLAAFQGAWGAFVNLNSDDPIWRQPGGPTEFDLGKTIVDAAAGAGVKHLVFSSGPPCVEMTGGKVNMKAMEMKYKIEQYARKLGSFETLTPINPAWYLENFLAEEVAPIFGGFPYFPDEEGYLTFRVPHWAGPGGDNRVPFLGIRDDFGDIIHGIFLNPERYNGRVIHGVSQLRGFDELVADFEQVTGKKCRYEPVLPSWEAFDIHGIPELEDVKLMFAFTQTTGGRYFAPEPSEADTAAELKRTTAVALGKPEPEQHTLRTKDFFRKHFATEK

[Multiple Choices]
A. Polyketide biosynthesis. .
B. Secondary metabolite biosynthesis. .
C. Pigment biosynthesis. .
D. 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2. .
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

> The sequence-matched UniProt record annotates this protein's pathway as secondary metabolite biosynthesis and attributes that annotation to a publication with experimental evidence. This supports the author's key, though the excerpt does not independently establish the underlying experiments.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> Whether this particular oxidoreductase participates in a secondary-metabolite biosynthetic pathway, rather than another pathway or a more specific pathway such as polyketide or pigment biosynthesis.


**Reason**

> The sequence is compatible with an oxidoreductase, but its enzyme-family features do not meaningfully identify the pathway among these choices. In particular, a general oxidoreductase fold does not establish participation in secondary-metabolite biosynthesis; that distinction depends on the protein's specific biological role or pathway context, absent from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices include broad and more specific pathway categories, but the sequence alone does not establish that the protein belongs to either specific category. The supplied pathway annotation supports B.


### Important caveats

- The reviewer-only evidence supports the key but was not available to the model.
- The annotation's experimental evidence attribution is reported in the source record; the underlying publication was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular oxidoreductase participates in a secondary-metabolite biosynthetic pathway, rather than another pathway or a more specific pathway such as polyketide or pigment biosynthesis.",
    "reason": "The sequence is compatible with an oxidoreductase, but its enzyme-family features do not meaningfully identify the pathway among these choices. In particular, a general oxidoreductase fold does not establish participation in secondary-metabolite biosynthesis; that distinction depends on the protein's specific biological role or pathway context, absent from the input."
  },
  "case_id": "pathway_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein's pathway as secondary metabolite biosynthesis and attributes that annotation to a publication with experimental evidence. This supports the author's key, though the excerpt does not independently establish the underlying experiments."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key but was not available to the model.",
    "The annotation's experimental evidence attribution is reported in the source record; the underlying publication was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices include broad and more specific pathway categories, but the sequence alone does not establish that the protein belongs to either specific category. The supplied pathway annotation supports B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates this protein's pathway as secondary metabolite biosynthesis and attributes that annotation to a publication with experimental evidence. This supports the author's key, though the excerpt does not independently establish the underlying experiments.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "Whether this particular oxidoreductase participates in a secondary-metabolite biosynthetic pathway, rather than another pathway or a more specific pathway such as polyketide or pigment biosynthesis.",
    "reason": "The sequence is compatible with an oxidoreductase, but its enzyme-family features do not meaningfully identify the pathway among these choices. In particular, a general oxidoreductase fold does not establish participation in secondary-metabolite biosynthesis; that distinction depends on the protein's specific biological role or pathway context, absent from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices include broad and more specific pathway categories, but the sequence alone does not establish that the protein belongs to either specific category. The supplied pathway annotation supports B."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key but was not available to the model.",
    "The annotation's experimental evidence attribution is reported in the source record; the underlying publication was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (A0A7T8F1M6, FrzB from Cladobotryum sp.) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with ECO:0000269 (inferred from direct assay) evidence from PubMed:33372776 (Zhang et al., JACS 2021, 'Biosynthesis of the Immunosuppressant (-)-FR901483'). The protein is an NmrA-like oxidoreductase in the FR901483 NRPS biosynthetic gene cluster. FR901483 is an immunosuppressant secondary metabolite, not a polyketide, pigment, or folate-pathway intermediate. The expected answer B is directly supported by experimental evidence.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal region 'MTFIIAVVGATGNQGG' contains a canonical Rossmann-fold NAD(P)-binding motif (GxGxxG), identifying this as an oxidoreductase. The overall domain architecture is consistent with an NmrA-like family oxidoreductase, a well-characterized component of fungal secondary metabolite biosynthetic gene clusters. Knowledge from many other fungal proteins (e.g., NmrA in Aspergillus nidulans, NmrA-like proteins in the gliotoxin and beauvericin NRPS clusters of Aspergillus and Beauveria, and numerous other Hypocreales secondary metabolite clusters) establishes that NmrA-like oxidoreductases are hallmarks of fungal secondary metabolite gene clusters. This family-level pattern strongly supports 'Secondary metabolite biosynthesis' (B) over 'Folate biosynthesis' (D, which requires a dihydropteroate synthase fold entirely different from a Rossmann-fold oxidoreductase) and 'Pigment biosynthesis' (C, not a recognized pathway category associated with NmrA-like domains). Distinguishing B from A (Polyketide biosynthesis): NmrA-like oxidoreductases are found in both PKS and NRPS clusters, but in Hypocreales fungi they are particularly prevalent in NRPS-derived metabolite clusters (gliotoxin, beauvericin, etc.). Since the domain itself is not a PKS-specific catalytic component (no acyltransferase, ketosynthase, or acyl-carrier-protein features), the more general 'Secondary metabolite biosynthesis' is the appropriate and defensible annotation level. A knowledgeable model recognizing the NmrA-like oxidoreductase from other fungal secondary metabolite clusters would select B as the best-supported general pathway category.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The NmrA-like oxidoreductase domain is a well-established family-level marker of fungal secondary metabolite gene clusters, learned from many other proteins (NmrA, gliotoxin cluster proteins, beauvericin cluster proteins, etc.). This transferable knowledge meaningfully eliminates D (folate/DHPS fold mismatch) and C (no pigment-specific association), and supports B over A because the domain is a general secondary metabolite cluster component rather than a PKS-specific enzyme. The inference is probabilistic but well-grounded in family-level biology.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While NmrA-like domains appear in both PKS and NRPS clusters, the absence of any PKS-specific catalytic features and the strong association of NmrA-like oxidoreductases with NRPS clusters in Hypocreales makes B the clearly preferred answer over A. Options C and D are readily eliminated by fold and domain analysis. No other option is genuinely defensible.


### Important caveats

- The NmrA-like domain is found in both PKS and NRPS fungal clusters, so the distinction between A and B relies on the domain being a general cluster component rather than a PKS-specific enzyme, plus the Hypocreales NRPS-cluster prevalence pattern.
- The UniProt pathway annotation 'Secondary metabolite biosynthesis' is the general UniProt pathway term; the specific compound (FR901483) is an NRPS-derived immunosuppressant, not a polyketide.
- The reviewer-only evidence confirms the sequence matches A0A7T8F1M6 (FrzB) exactly, but this accession and organism identity were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal region 'MTFIIAVVGATGNQGG' contains a canonical Rossmann-fold NAD(P)-binding motif (GxGxxG), identifying this as an oxidoreductase. The overall domain architecture is consistent with an NmrA-like family oxidoreductase, a well-characterized component of fungal secondary metabolite biosynthetic gene clusters. Knowledge from many other fungal proteins (e.g., NmrA in Aspergillus nidulans, NmrA-like proteins in the gliotoxin and beauvericin NRPS clusters of Aspergillus and Beauveria, and numerous other Hypocreales secondary metabolite clusters) establishes that NmrA-like oxidoreductases are hallmarks of fungal secondary metabolite gene clusters. This family-level pattern strongly supports 'Secondary metabolite biosynthesis' (B) over 'Folate biosynthesis' (D, which requires a dihydropteroate synthase fold entirely different from a Rossmann-fold oxidoreductase) and 'Pigment biosynthesis' (C, not a recognized pathway category associated with NmrA-like domains). Distinguishing B from A (Polyketide biosynthesis): NmrA-like oxidoreductases are found in both PKS and NRPS clusters, but in Hypocreales fungi they are particularly prevalent in NRPS-derived metabolite clusters (gliotoxin, beauvericin, etc.). Since the domain itself is not a PKS-specific catalytic component (no acyltransferase, ketosynthase, or acyl-carrier-protein features), the more general 'Secondary metabolite biosynthesis' is the appropriate and defensible annotation level. A knowledgeable model recognizing the NmrA-like oxidoreductase from other fungal secondary metabolite clusters would select B as the best-supported general pathway category.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The NmrA-like oxidoreductase domain is a well-established family-level marker of fungal secondary metabolite gene clusters, learned from many other proteins (NmrA, gliotoxin cluster proteins, beauvericin cluster proteins, etc.). This transferable knowledge meaningfully eliminates D (folate/DHPS fold mismatch) and C (no pigment-specific association), and supports B over A because the domain is a general secondary metabolite cluster component rather than a PKS-specific enzyme. The inference is probabilistic but well-grounded in family-level biology."
  },
  "case_id": "pathway_0101",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (A0A7T8F1M6, FrzB from Cladobotryum sp.) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with ECO:0000269 (inferred from direct assay) evidence from PubMed:33372776 (Zhang et al., JACS 2021, 'Biosynthesis of the Immunosuppressant (-)-FR901483'). The protein is an NmrA-like oxidoreductase in the FR901483 NRPS biosynthetic gene cluster. FR901483 is an immunosuppressant secondary metabolite, not a polyketide, pigment, or folate-pathway intermediate. The expected answer B is directly supported by experimental evidence."
  },
  "important_caveats": [
    "The NmrA-like domain is found in both PKS and NRPS fungal clusters, so the distinction between A and B relies on the domain being a general cluster component rather than a PKS-specific enzyme, plus the Hypocreales NRPS-cluster prevalence pattern.",
    "The UniProt pathway annotation 'Secondary metabolite biosynthesis' is the general UniProt pathway term; the specific compound (FR901483) is an NRPS-derived immunosuppressant, not a polyketide.",
    "The reviewer-only evidence confirms the sequence matches A0A7T8F1M6 (FrzB) exactly, but this accession and organism identity were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While NmrA-like domains appear in both PKS and NRPS clusters, the absence of any PKS-specific catalytic features and the strong association of NmrA-like oxidoreductases with NRPS clusters in Hypocreales makes B the clearly preferred answer over A. Options C and D are readily eliminated by fold and domain analysis. No other option is genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0101",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (A0A7T8F1M6, FrzB from Cladobotryum sp.) explicitly annotates the pathway as 'Secondary metabolite biosynthesis' with ECO:0000269 (inferred from direct assay) evidence from PubMed:33372776 (Zhang et al., JACS 2021, 'Biosynthesis of the Immunosuppressant (-)-FR901483'). The protein is an NmrA-like oxidoreductase in the FR901483 NRPS biosynthetic gene cluster. FR901483 is an immunosuppressant secondary metabolite, not a polyketide, pigment, or folate-pathway intermediate. The expected answer B is directly supported by experimental evidence.",
    "evidence_ids": ["C5", "C4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal region 'MTFIIAVVGATGNQGG' contains a canonical Rossmann-fold NAD(P)-binding motif (GxGxxG), identifying this as an oxidoreductase. The overall domain architecture is consistent with an NmrA-like family oxidoreductase, a well-characterized component of fungal secondary metabolite biosynthetic gene clusters. Knowledge from many other fungal proteins (e.g., NmrA in Aspergillus nidulans, NmrA-like proteins in the gliotoxin and beauvericin NRPS clusters of Aspergillus and Beauveria, and numerous other Hypocreales secondary metabolite clusters) establishes that NmrA-like oxidoreductases are hallmarks of fungal secondary metabolite gene clusters. This family-level pattern strongly supports 'Secondary metabolite biosynthesis' (B) over 'Folate biosynthesis' (D, which requires a dihydropteroate synthase fold entirely different from a Rossmann-fold oxidoreductase) and 'Pigment biosynthesis' (C, not a recognized pathway category associated with NmrA-like domains). Distinguishing B from A (Polyketide biosynthesis): NmrA-like oxidoreductases are found in both PKS and NRPS clusters, but in Hypocreales fungi they are particularly prevalent in NRPS-derived metabolite clusters (gliotoxin, beauvericin, etc.). Since the domain itself is not a PKS-specific catalytic component (no acyltransferase, ketosynthase, or acyl-carrier-protein features), the more general 'Secondary metabolite biosynthesis' is the appropriate and defensible annotation level. A knowledgeable model recognizing the NmrA-like oxidoreductase from other fungal secondary metabolite clusters would select B as the best-supported general pathway category.",
    "missing_item_specific_fact": "",
    "reason": "The NmrA-like oxidoreductase domain is a well-established family-level marker of fungal secondary metabolite gene clusters, learned from many other proteins (NmrA, gliotoxin cluster proteins, beauvericin cluster proteins, etc.). This transferable knowledge meaningfully eliminates D (folate/DHPS fold mismatch) and C (no pigment-specific association), and supports B over A because the domain is a general secondary metabolite cluster component rather than a PKS-specific enzyme. The inference is probabilistic but well-grounded in family-level biology."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While NmrA-like domains appear in both PKS and NRPS clusters, the absence of any PKS-specific catalytic features and the strong association of NmrA-like oxidoreductases with NRPS clusters in Hypocreales makes B the clearly preferred answer over A. Options C and D are readily eliminated by fold and domain analysis. No other option is genuinely defensible."
  },
  "important_caveats": [
    "The NmrA-like domain is found in both PKS and NRPS fungal clusters, so the distinction between A and B relies on the domain being a general cluster component rather than a PKS-specific enzyme, plus the Hypocreales NRPS-cluster prevalence pattern.",
    "The UniProt pathway annotation 'Secondary metabolite biosynthesis' is the general UniProt pathway term; the specific compound (FR901483) is an NRPS-derived immunosuppressant, not a polyketide.",
    "The reviewer-only evidence confirms the sequence matches A0A7T8F1M6 (FrzB) exactly, but this accession and organism identity were not available to the evaluated model."
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
  "benchmark_sequence_length": 336,
  "benchmark_sequence_sha256": "cd7d98c2695ebfbc0768a64c07bd3d81f4926c10b4da52ae5cfb6c37c20c331b",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "26631434aec4fabf8eb05f0a928e2ab6e7506f73e2486f63ad06a9a7ab4d6c22",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 336,
  "current_source_sequence_sha256": "cd7d98c2695ebfbc0768a64c07bd3d81f4926c10b4da52ae5cfb6c37c20c331b",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8F1M6",
  "selected_historical_entry_version": 12,
  "selected_historical_record_sha256": "ee1a2be9be3ccf677aecb6332a99ec11ea500e17cc26c192f117732e78966d27",
  "selected_historical_source_sequence_length": 336,
  "selected_historical_source_sequence_sha256": "cd7d98c2695ebfbc0768a64c07bd3d81f4926c10b4da52ae5cfb6c37c20c331b",
  "selected_historical_version": {
    "accession": "A0A7T8F1M6",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZB_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8F1M6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:48.906105+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26631434aec4fabf8eb05f0a928e2ab6e7506f73e2486f63ad06a9a7ab4d6c22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:48.906105+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26631434aec4fabf8eb05f0a928e2ab6e7506f73e2486f63ad06a9a7ab4d6c22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:48.906105+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26631434aec4fabf8eb05f0a928e2ab6e7506f73e2486f63ad06a9a7ab4d6c22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis cluster protein B\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"NmrA-like family domain-containing oxidoreductase FrzB\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:48.906105+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26631434aec4fabf8eb05f0a928e2ab6e7506f73e2486f63ad06a9a7ab4d6c22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:25:48.906105+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26631434aec4fabf8eb05f0a928e2ab6e7506f73e2486f63ad06a9a7ab4d6c22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1M6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:48.906105+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "26631434aec4fabf8eb05f0a928e2ab6e7506f73e2486f63ad06a9a7ab4d6c22",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1M6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M6?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H1",
  "excerpt": "ID   FRZB_CLASX              Reviewed;         336 AA.\nAC   A0A7T8F1M6;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=NmrA-like family domain-containing oxidoreductase FrzB {ECO:0000303|PubMed:33372776};\nDE            EC=1.5.1.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis cluster protein B {ECO:0000303|PubMed:33372776};\nGN   Name=FrzB {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:51.134889+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee1a2be9be3ccf677aecb6332a99ec11ea500e17cc26c192f117732e78966d27",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M6?format=txt&versions=12"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M6?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:51.134889+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee1a2be9be3ccf677aecb6332a99ec11ea500e17cc26c192f117732e78966d27",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M6?format=txt&versions=12"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1M6?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis.\nCC       {ECO:0000269|PubMed:33372776}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:51.134889+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ee1a2be9be3ccf677aecb6332a99ec11ea500e17cc26c192f117732e78966d27",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1M6?format=txt&versions=12"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 101. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
