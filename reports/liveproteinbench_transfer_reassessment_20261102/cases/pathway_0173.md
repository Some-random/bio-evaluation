# pathway_0173

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0173.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Carbohydrate degradation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASGARYAGKVVVVTGAARGIGAGIARAFVDSGAQVVICDKDERGGRALEQELRGAVFIRCDVTREEDVRALLSDTVHRFGRLDCVVNNAGSHPPLQPLEETTAQGFRELLELNLLGTYTLCKLAFPHLRRSRGNIINISTLVGAVGQLQGVPYAATKGAVTALTKALALDESQYGVRVNCISPGNIWTPLWQELAALAPDPRAAIREGAMAQPLGRMGQPAEVGAAAVFLASEASFCTGLELFVTGGAELGSGPENFFRSLGLCVVPEDVPPPTSRPRICSYK

[Multiple Choices]
A. NAD(+) biosynthesis
B. Carbohydrate degradation
C. L-threonine from L-aspartate: step 4/5. .
D. L-threonine from L-aspartate: step 1/5. .
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

> The matched sequence’s UniProt pathway annotation places the protein in carbohydrate degradation, specifically L-fucose degradation. The cited 2024 study identifies it as an L-fucose dehydrogenase and the initial enzyme of that pathway, supporting choice B.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal glycine-rich Rossmann-like motif and the sequence’s dehydrogenase-like features support an NAD-dependent oxidoreductase, and the sequence does not resemble the characteristic enzymes for the listed threonine-biosynthesis steps. But these features do not identify the oxidized substrate or distinguish a sugar-degradation role from other oxidoreductase functions.


**Missing item-specific fact**

> That this particular protein acts as an L-fucose dehydrogenase in L-fucose degradation.


**Reason**

> The pathway assignment depends on the protein’s substrate and biological role, neither of which is established by the broadly shared oxidoreductase features in the input. The exact-protein functional characterization is therefore needed to confidently select carbohydrate degradation over the remaining pathway choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source evidence supports carbohydrate degradation, and the alternatives describe distinct pathways rather than overlapping labels.


### Important caveats

- The pathway annotation is computationally evidenced (ECO:0000305), while the cited publication is specifically reported as identifying the enzyme and its catalytic activity.
- The sequence match establishes that the reviewer-only source record applies to the supplied sequence; that record was not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich Rossmann-like motif and the sequence’s dehydrogenase-like features support an NAD-dependent oxidoreductase, and the sequence does not resemble the characteristic enzymes for the listed threonine-biosynthesis steps. But these features do not identify the oxidized substrate or distinguish a sugar-degradation role from other oxidoreductase functions.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "That this particular protein acts as an L-fucose dehydrogenase in L-fucose degradation.",
    "reason": "The pathway assignment depends on the protein’s substrate and biological role, neither of which is established by the broadly shared oxidoreductase features in the input. The exact-protein functional characterization is therefore needed to confidently select carbohydrate degradation over the remaining pathway choice."
  },
  "case_id": "pathway_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The matched sequence’s UniProt pathway annotation places the protein in carbohydrate degradation, specifically L-fucose degradation. The cited 2024 study identifies it as an L-fucose dehydrogenase and the initial enzyme of that pathway, supporting choice B."
  },
  "important_caveats": [
    "The pathway annotation is computationally evidenced (ECO:0000305), while the cited publication is specifically reported as identifying the enzyme and its catalytic activity.",
    "The sequence match establishes that the reviewer-only source record applies to the supplied sequence; that record was not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source evidence supports carbohydrate degradation, and the alternatives describe distinct pathways rather than overlapping labels."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence’s UniProt pathway annotation places the protein in carbohydrate degradation, specifically L-fucose degradation. The cited 2024 study identifies it as an L-fucose dehydrogenase and the initial enzyme of that pathway, supporting choice B.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal glycine-rich Rossmann-like motif and the sequence’s dehydrogenase-like features support an NAD-dependent oxidoreductase, and the sequence does not resemble the characteristic enzymes for the listed threonine-biosynthesis steps. But these features do not identify the oxidized substrate or distinguish a sugar-degradation role from other oxidoreductase functions.",
    "missing_item_specific_fact": "That this particular protein acts as an L-fucose dehydrogenase in L-fucose degradation.",
    "reason": "The pathway assignment depends on the protein’s substrate and biological role, neither of which is established by the broadly shared oxidoreductase features in the input. The exact-protein functional characterization is therefore needed to confidently select carbohydrate degradation over the remaining pathway choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source evidence supports carbohydrate degradation, and the alternatives describe distinct pathways rather than overlapping labels."
  },
  "important_caveats": [
    "The pathway annotation is computationally evidenced (ECO:0000305), while the cited publication is specifically reported as identifying the enzyme and its catalytic activity.",
    "The sequence match establishes that the reviewer-only source record applies to the supplied sequence; that record was not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAT9JA24 annotates this protein as L-fucose dehydrogenase (EC 1.1.1.122) with pathway 'Carbohydrate degradation; L-fucose degradation' (ECO:0000305, curator inference from experimentally verified enzyme activity ECO:0000269, PubMed:38944119). The 2024 JBC paper experimentally demonstrated HSD17B14 as the initial enzyme of L-fucose degradation. The expected answer 'Carbohydrate degradation' matches the UniProt pathway classification for this sugar-degradation enzyme.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'VVVVTGAARGIGAGI' contains a canonical Rossmann-fold GxGxxG nucleotide-binding motif (GIGAGI), identifying this as an NAD(P)-dependent oxidoreductase. This immediately disfavors A (NAD+ biosynthesis enzymes such as NAMPT, QPRT, or NMNAT are not NAD(P)-dependent dehydrogenases; they synthesize NAD+ rather than bind it as a cofactor) and D (aspartate kinase, EC 2.7.2.4, is a kinase with no Rossmann fold). The distinction between B and C(step 4, homoserine dehydrogenase EC 1.1.1.3) relies on family-level features: homoserine dehydrogenase is typically 350–500+ AA and belongs to a distinct family with different Rossmann-fold context; this protein is only 284 AA with a 'TGAARGIGAG' motif and adjacent Cys residues (VICDKDERGG) more characteristic of medium-chain dehydrogenases/SDRs acting on small-molecule substrates like sugars. The size and specific motif architecture are inconsistent with the homoserine dehydrogenase/threonine synthase superfamily, favoring a sugar-metabolizing dehydrogenase (B) over an amino-acid biosynthesis enzyme (C).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann fold identifies the enzyme class (oxidoreductase), eliminating A and D. The protein's small size (284 AA) and specific Rossmann-fold context with adjacent cysteines are inconsistent with homoserine dehydrogenase (typically 350+ AA, different family architecture), providing a defensible family-level inference favoring carbohydrate-degradation dehydrogenase over amino-acid-biosynthesis dehydrogenase. This is probabilistic but grounded in transferable knowledge of dehydrogenase families.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While both B and C(step 4) involve NAD(P)-dependent dehydrogenases, the size (284 vs 350+ AA) and specific sequence-family features provide a meaningful basis to favor B. The distinction is not trivial but is defensible from family-level sequence knowledge.


### Important caveats

- The L-fucose dehydrogenase activity of HSD17B14 was only experimentally characterized in 2024 (PubMed:38944119); prior to this, the protein was annotated as a hydroxysteroid dehydrogenase. The pathway annotation uses ECO:0000305 (curator inference) rather than direct experimental pathway evidence.
- The distinction between B and C(step 4) relies on probabilistic family-level inference (size, motif context) rather than a single definitive sequence feature. A model familiar with homoserine dehydrogenase sequences would find the 284-AA length and SDR-like architecture inconsistent with that enzyme, but this is not an airtight proof.
- The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt A0AAT9JA24 (284 AA, Oryctolagus cuniculus).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'VVVVTGAARGIGAGI' contains a canonical Rossmann-fold GxGxxG nucleotide-binding motif (GIGAGI), identifying this as an NAD(P)-dependent oxidoreductase. This immediately disfavors A (NAD+ biosynthesis enzymes such as NAMPT, QPRT, or NMNAT are not NAD(P)-dependent dehydrogenases; they synthesize NAD+ rather than bind it as a cofactor) and D (aspartate kinase, EC 2.7.2.4, is a kinase with no Rossmann fold). The distinction between B and C(step 4, homoserine dehydrogenase EC 1.1.1.3) relies on family-level features: homoserine dehydrogenase is typically 350–500+ AA and belongs to a distinct family with different Rossmann-fold context; this protein is only 284 AA with a 'TGAARGIGAG' motif and adjacent Cys residues (VICDKDERGG) more characteristic of medium-chain dehydrogenases/SDRs acting on small-molecule substrates like sugars. The size and specific motif architecture are inconsistent with the homoserine dehydrogenase/threonine synthase superfamily, favoring a sugar-metabolizing dehydrogenase (B) over an amino-acid biosynthesis enzyme (C).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold identifies the enzyme class (oxidoreductase), eliminating A and D. The protein's small size (284 AA) and specific Rossmann-fold context with adjacent cysteines are inconsistent with homoserine dehydrogenase (typically 350+ AA, different family architecture), providing a defensible family-level inference favoring carbohydrate-degradation dehydrogenase over amino-acid-biosynthesis dehydrogenase. This is probabilistic but grounded in transferable knowledge of dehydrogenase families."
  },
  "case_id": "pathway_0173",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAT9JA24 annotates this protein as L-fucose dehydrogenase (EC 1.1.1.122) with pathway 'Carbohydrate degradation; L-fucose degradation' (ECO:0000305, curator inference from experimentally verified enzyme activity ECO:0000269, PubMed:38944119). The 2024 JBC paper experimentally demonstrated HSD17B14 as the initial enzyme of L-fucose degradation. The expected answer 'Carbohydrate degradation' matches the UniProt pathway classification for this sugar-degradation enzyme."
  },
  "important_caveats": [
    "The L-fucose dehydrogenase activity of HSD17B14 was only experimentally characterized in 2024 (PubMed:38944119); prior to this, the protein was annotated as a hydroxysteroid dehydrogenase. The pathway annotation uses ECO:0000305 (curator inference) rather than direct experimental pathway evidence.",
    "The distinction between B and C(step 4) relies on probabilistic family-level inference (size, motif context) rather than a single definitive sequence feature. A model familiar with homoserine dehydrogenase sequences would find the 284-AA length and SDR-like architecture inconsistent with that enzyme, but this is not an airtight proof.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt A0AAT9JA24 (284 AA, Oryctolagus cuniculus)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While both B and C(step 4) involve NAD(P)-dependent dehydrogenases, the size (284 vs 350+ AA) and specific sequence-family features provide a meaningful basis to favor B. The distinction is not trivial but is defensible from family-level sequence knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0173",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAT9JA24 annotates this protein as L-fucose dehydrogenase (EC 1.1.1.122) with pathway 'Carbohydrate degradation; L-fucose degradation' (ECO:0000305, curator inference from experimentally verified enzyme activity ECO:0000269, PubMed:38944119). The 2024 JBC paper experimentally demonstrated HSD17B14 as the initial enzyme of L-fucose degradation. The expected answer 'Carbohydrate degradation' matches the UniProt pathway classification for this sugar-degradation enzyme.",
    "evidence_ids": ["C5", "C6", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'VVVVTGAARGIGAGI' contains a canonical Rossmann-fold GxGxxG nucleotide-binding motif (GIGAGI), identifying this as an NAD(P)-dependent oxidoreductase. This immediately disfavors A (NAD+ biosynthesis enzymes such as NAMPT, QPRT, or NMNAT are not NAD(P)-dependent dehydrogenases; they synthesize NAD+ rather than bind it as a cofactor) and D (aspartate kinase, EC 2.7.2.4, is a kinase with no Rossmann fold). The distinction between B and C(step 4, homoserine dehydrogenase EC 1.1.1.3) relies on family-level features: homoserine dehydrogenase is typically 350–500+ AA and belongs to a distinct family with different Rossmann-fold context; this protein is only 284 AA with a 'TGAARGIGAG' motif and adjacent Cys residues (VICDKDERGG) more characteristic of medium-chain dehydrogenases/SDRs acting on small-molecule substrates like sugars. The size and specific motif architecture are inconsistent with the homoserine dehydrogenase/threonine synthase superfamily, favoring a sugar-metabolizing dehydrogenase (B) over an amino-acid biosynthesis enzyme (C).",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold identifies the enzyme class (oxidoreductase), eliminating A and D. The protein's small size (284 AA) and specific Rossmann-fold context with adjacent cysteines are inconsistent with homoserine dehydrogenase (typically 350+ AA, different family architecture), providing a defensible family-level inference favoring carbohydrate-degradation dehydrogenase over amino-acid-biosynthesis dehydrogenase. This is probabilistic but grounded in transferable knowledge of dehydrogenase families."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While both B and C(step 4) involve NAD(P)-dependent dehydrogenases, the size (284 vs 350+ AA) and specific sequence-family features provide a meaningful basis to favor B. The distinction is not trivial but is defensible from family-level sequence knowledge."
  },
  "important_caveats": [
    "The L-fucose dehydrogenase activity of HSD17B14 was only experimentally characterized in 2024 (PubMed:38944119); prior to this, the protein was annotated as a hydroxysteroid dehydrogenase. The pathway annotation uses ECO:0000305 (curator inference) rather than direct experimental pathway evidence.",
    "The distinction between B and C(step 4) relies on probabilistic family-level inference (size, motif context) rather than a single definitive sequence feature. A model familiar with homoserine dehydrogenase sequences would find the 284-AA length and SDR-like architecture inconsistent with that enzyme, but this is not an airtight proof.",
    "The reviewer-only evidence confirms sequence match (SHA-256 identical) between the benchmark sequence and UniProt A0AAT9JA24 (284 AA, Oryctolagus cuniculus)."
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
  "benchmark_sequence_length": 284,
  "benchmark_sequence_sha256": "866d78afb63c4ef17950a8b38eb26f81ee9da683687494456a69d4262af65809",
  "current_entry_audit": {
    "entryVersion": 7,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 2
  },
  "current_record_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 284,
  "current_source_sequence_sha256": "866d78afb63c4ef17950a8b38eb26f81ee9da683687494456a69d4262af65809",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AAT9JA24",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "selected_historical_source_sequence_length": 284,
  "selected_historical_source_sequence_sha256": "866d78afb63c4ef17950a8b38eb26f81ee9da683687494456a69d4262af65809",
  "selected_historical_version": {
    "accession": "A0AAT9JA24",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHB14_RABIT",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAT9JA24\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":7,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rabbit\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Lagomorpha\",\"Leporidae\",\"Oryctolagus\"],\"scientificName\":\"Oryctolagus cuniculus\",\"taxonId\":9986}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Hydroxysteroid 17-beta dehydrogenase 14\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38944119\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.122\"}],\"fullName\":{\"value\":\"L-fucose dehydrogenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Carbohydrate degradation; L-fucose degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Witecka A.\",\"Kazak V.\",\"Kwiatkowski S.\",\"Kiersztan A.\",\"Jagielski A.K.\",\"Kozminski W.\",\"Augustyniak R.\",\"Drozak J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38944119\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107501\"}],\"citationType\":\"journal article\",\"firstPage\":\"107501\",\"id\":\"38944119\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107501\",\"publicationDate\":\"2024\",\"title\":\"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose dehydrogenase, the initial enzyme of the L-fucose degradation pathway.\",\"volume\":\"300\"},\"referenceNumber\":2,\"referencePositions\":[\"IDENTIFICATION\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"MUTAGENESIS OF TYR-154\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:55.009007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b78142c3b7a786522dada45f85209580d47b497829a21a3d6e92a8460fba680a",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAT9JA24.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   DHB14_RABIT             Reviewed;         284 AA.\nAC   A0AAT9JA24; A0A5F9CLT4;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 2.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=L-fucose dehydrogenase;\nDE            EC=1.1.1.122 {ECO:0000269|PubMed:38944119};\nDE   AltName: Full=Hydroxysteroid 17-beta dehydrogenase 14;\nGN   Name=HSD17B14;\nOS   Oryctolagus cuniculus (Rabbit).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Lagomorpha; Leporidae; Oryctolagus.\nOX   NCBI_TaxID=9986;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   IDENTIFICATION, FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND MUTAGENESIS OF TYR-154.\nRX   PubMed=38944119; DOI=10.1016/j.jbc.2024.107501;\nRA   Witecka A., Kazak V., Kwiatkowski S., Kiersztan A., Jagielski A.K.,\nRA   Kozminski W., Augustyniak R., Drozak J.;\nRT   \"Hydroxysteroid 17-beta dehydrogenase 14 (HSD17B14) is an L-fucose\nRT   dehydrogenase, the initial enzyme of the L-fucose degradation pathway.\";\nRL   J. Biol. Chem. 300:107501-107501(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Carbohydrate degradation; L-fucose degradation. {ECO:0000305}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:41.890371+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fa238b1004917cb558400b2d1bdad52c610280cb2a3deaaa45f9f7d300426d5f",
  "url": "https://rest.uniprot.org/unisave/A0AAT9JA24?format=txt&versions=5"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 173. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
