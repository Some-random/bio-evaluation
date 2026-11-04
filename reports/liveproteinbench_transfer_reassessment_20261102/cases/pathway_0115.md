# pathway_0115

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0115.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MITFSSLLVTFSAISTSLAIPGSILPKRSPMNFVLQRNESSLVRRATPNYEQDYTTGGDVIYTPSGSSFTVDWSTEDDFVVGLGWTTGSTNPINFSGTFGIGSGTALLSIYGWSENPLVEYYIVEDSASPPSFGTVKGSVTSDGSSYTIWENQRVNEPSIVGTATFNQYISVRSSPRKSGTVTVENHFQAWAALGMNLGTLNYQVLAVEGWGGEGAATQTVS

[Multiple Choices]
A. Cell wall degradation
B. Amino-acid degradation
C. Glycan degradation
D. Carotenoid biosynthesis
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

> The exact-matched UniProt record names the protein as an endo-1,4-beta-xylanase and annotates its pathway as glycan degradation, specifically xylan degradation. The pathway annotation is computational (PROSITE-ProRule); it supports the answer but is not itself experimental proof.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic region consistent with a secretion signal and a compact sequence consistent with a fungal glycoside hydrolase, specifically a xylanase-like enzyme. Transferable knowledge that xylanases hydrolyze xylan, a polysaccharide glycan, supports glycan degradation over amino-acid degradation or carotenoid biosynthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family- and substrate-level inference from the sequence can meaningfully favor C without recalling this protein's database entry. However, xylan is also a plant cell-wall component, so the distinction from A is not clean.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Xylan degradation is glycan degradation, but xylan is also a major plant cell-wall polysaccharide, making cell wall degradation a defensible broad description of the same activity.


### Important caveats

- The source pathway annotation is computational, and the cited functional literature excerpt does not independently establish the target protein's catalytic activity.
- The sequence-based family inference is probabilistic; the supplied input does not directly name the enzyme or its substrate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic region consistent with a secretion signal and a compact sequence consistent with a fungal glycoside hydrolase, specifically a xylanase-like enzyme. Transferable knowledge that xylanases hydrolyze xylan, a polysaccharide glycan, supports glycan degradation over amino-acid degradation or carotenoid biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family- and substrate-level inference from the sequence can meaningfully favor C without recalling this protein's database entry. However, xylan is also a plant cell-wall component, so the distinction from A is not clean."
  },
  "case_id": "pathway_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact-matched UniProt record names the protein as an endo-1,4-beta-xylanase and annotates its pathway as glycan degradation, specifically xylan degradation. The pathway annotation is computational (PROSITE-ProRule); it supports the answer but is not itself experimental proof."
  },
  "important_caveats": [
    "The source pathway annotation is computational, and the cited functional literature excerpt does not independently establish the target protein's catalytic activity.",
    "The sequence-based family inference is probabilistic; the supplied input does not directly name the enzyme or its substrate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Xylan degradation is glycan degradation, but xylan is also a major plant cell-wall polysaccharide, making cell wall degradation a defensible broad description of the same activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact-matched UniProt record names the protein as an endo-1,4-beta-xylanase and annotates its pathway as glycan degradation, specifically xylan degradation. The pathway annotation is computational (PROSITE-ProRule); it supports the answer but is not itself experimental proof.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic region consistent with a secretion signal and a compact sequence consistent with a fungal glycoside hydrolase, specifically a xylanase-like enzyme. Transferable knowledge that xylanases hydrolyze xylan, a polysaccharide glycan, supports glycan degradation over amino-acid degradation or carotenoid biosynthesis.",
    "missing_item_specific_fact": "",
    "reason": "Family- and substrate-level inference from the sequence can meaningfully favor C without recalling this protein's database entry. However, xylan is also a plant cell-wall component, so the distinction from A is not clean."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Xylan degradation is glycan degradation, but xylan is also a major plant cell-wall polysaccharide, making cell wall degradation a defensible broad description of the same activity."
  },
  "important_caveats": [
    "The source pathway annotation is computational, and the cited functional literature excerpt does not independently establish the target protein's catalytic activity.",
    "The sequence-based family inference is probabilistic; the supplied input does not directly name the enzyme or its substrate."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A384K474) annotates this protein as Ethylene-inducing xylanase 2 (EIX2), EC 3.2.1.8 (Endo-1,4-beta-xylanase), with the pathway explicitly listed as 'Glycan degradation; xylan degradation.' Xylan is a glycan (xylose polymer), so 'Glycan degradation' is the correct pathway category. The annotation evidence code is ECO:0000255 (PROSITE-ProRule), indicating computational inference from protein-family motifs rather than direct experimental validation, but the pathway assignment is consistent with the enzyme classification.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear N-terminal signal peptide (MITFSSLLVTFSAISTSLAIPG), indicating a secreted protein. The mature protein (~200 aa) contains motifs characteristic of glycoside hydrolases, notably the 'GW...GW' bracketing pattern (GWTTGSTNPINFSGTFGIGSGTALLSIYGW) and the 'GWGGEG' C-terminal motif, which are hallmarks of GH10/GH11 xylanase families. A knowledgeable model familiar with GH families can recognize these motifs as indicative of glycan (polysaccharide) hydrolysis. This rules out B (amino-acid degradation: no protease/peptidase catalytic motifs such as Ser-His-Asp or Cys-His-Asn) and D (carotenoid biosynthesis: no phytoene synthase, desaturase, or cyclase motifs; carotenoid enzymes are typically membrane-associated and much larger). Between A (Cell wall degradation) and C (Glycan degradation): in formal pathway taxonomy (UniProt/KEGG), xylan degradation is classified under 'Glycan degradation,' not 'Cell wall degradation.' 'Cell wall degradation' is a functional/ecological description, not a standard pathway name. The question asks for the 'primary metabolic or signaling pathway,' which points to the formal pathway classification. Thus, recognizing GH motifs → glycan degradation as the formal pathway distinguishes C from A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence-level features (signal peptide, GH-family motifs, size) combined with knowledge of glycoside hydrolase families and pathway taxonomy provide a credible, transferable inference chain that meaningfully distinguishes C from the other options. The GW…GW motif pattern is shared across many GH10/GH11 xylanases from diverse organisms, making this a family-level inference rather than a lookup of this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Xylan is both a glycan and a major component of plant cell walls. A biologist might reasonably describe xylanase activity as 'cell wall degradation' in a functional/ecological sense. However, in formal pathway databases (UniProt, KEGG), xylan degradation is categorized under 'Glycan degradation,' and 'Cell wall degradation' is not a standard pathway name. The question's phrasing ('primary metabolic or signaling pathway') favors the formal pathway taxonomy, making C the more precise answer, but A is not entirely unreasonable as a broader functional description.


### Important caveats

- The UniProt pathway annotation is based on PROSITE-ProRule (ECO:0000255), a computational inference from protein-family motifs, not direct experimental measurement of pathway flux.
- The protein is also described as 'ethylene-inducing' (EIX), suggesting a signaling role in plant-pathogen interactions, but the enzymatic (xylanase) activity maps to glycan degradation.
- The distinction between 'Cell wall degradation' (A) and 'Glycan degradation' (C) depends on whether the question expects formal pathway taxonomy or functional description; the formal pathway name favors C.
- The reviewer-only evidence (accession, organism, entry name) was not available to the evaluated model; the reasoning above relies only on sequence features and general biological knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (MITFSSLLVTFSAISTSLAIPG), indicating a secreted protein. The mature protein (~200 aa) contains motifs characteristic of glycoside hydrolases, notably the 'GW...GW' bracketing pattern (GWTTGSTNPINFSGTFGIGSGTALLSIYGW) and the 'GWGGEG' C-terminal motif, which are hallmarks of GH10/GH11 xylanase families. A knowledgeable model familiar with GH families can recognize these motifs as indicative of glycan (polysaccharide) hydrolysis. This rules out B (amino-acid degradation: no protease/peptidase catalytic motifs such as Ser-His-Asp or Cys-His-Asn) and D (carotenoid biosynthesis: no phytoene synthase, desaturase, or cyclase motifs; carotenoid enzymes are typically membrane-associated and much larger). Between A (Cell wall degradation) and C (Glycan degradation): in formal pathway taxonomy (UniProt/KEGG), xylan degradation is classified under 'Glycan degradation,' not 'Cell wall degradation.' 'Cell wall degradation' is a functional/ecological description, not a standard pathway name. The question asks for the 'primary metabolic or signaling pathway,' which points to the formal pathway classification. Thus, recognizing GH motifs → glycan degradation as the formal pathway distinguishes C from A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence-level features (signal peptide, GH-family motifs, size) combined with knowledge of glycoside hydrolase families and pathway taxonomy provide a credible, transferable inference chain that meaningfully distinguishes C from the other options. The GW…GW motif pattern is shared across many GH10/GH11 xylanases from diverse organisms, making this a family-level inference rather than a lookup of this specific protein's record."
  },
  "case_id": "pathway_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A384K474) annotates this protein as Ethylene-inducing xylanase 2 (EIX2), EC 3.2.1.8 (Endo-1,4-beta-xylanase), with the pathway explicitly listed as 'Glycan degradation; xylan degradation.' Xylan is a glycan (xylose polymer), so 'Glycan degradation' is the correct pathway category. The annotation evidence code is ECO:0000255 (PROSITE-ProRule), indicating computational inference from protein-family motifs rather than direct experimental validation, but the pathway assignment is consistent with the enzyme classification."
  },
  "important_caveats": [
    "The UniProt pathway annotation is based on PROSITE-ProRule (ECO:0000255), a computational inference from protein-family motifs, not direct experimental measurement of pathway flux.",
    "The protein is also described as 'ethylene-inducing' (EIX), suggesting a signaling role in plant-pathogen interactions, but the enzymatic (xylanase) activity maps to glycan degradation.",
    "The distinction between 'Cell wall degradation' (A) and 'Glycan degradation' (C) depends on whether the question expects formal pathway taxonomy or functional description; the formal pathway name favors C.",
    "The reviewer-only evidence (accession, organism, entry name) was not available to the evaluated model; the reasoning above relies only on sequence features and general biological knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Xylan is both a glycan and a major component of plant cell walls. A biologist might reasonably describe xylanase activity as 'cell wall degradation' in a functional/ecological sense. However, in formal pathway databases (UniProt, KEGG), xylan degradation is categorized under 'Glycan degradation,' and 'Cell wall degradation' is not a standard pathway name. The question's phrasing ('primary metabolic or signaling pathway') favors the formal pathway taxonomy, making C the more precise answer, but A is not entirely unreasonable as a broader functional description."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A384K474) annotates this protein as Ethylene-inducing xylanase 2 (EIX2), EC 3.2.1.8 (Endo-1,4-beta-xylanase), with the pathway explicitly listed as 'Glycan degradation; xylan degradation.' Xylan is a glycan (xylose polymer), so 'Glycan degradation' is the correct pathway category. The annotation evidence code is ECO:0000255 (PROSITE-ProRule), indicating computational inference from protein-family motifs rather than direct experimental validation, but the pathway assignment is consistent with the enzyme classification.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear N-terminal signal peptide (MITFSSLLVTFSAISTSLAIPG), indicating a secreted protein. The mature protein (~200 aa) contains motifs characteristic of glycoside hydrolases, notably the 'GW...GW' bracketing pattern (GWTTGSTNPINFSGTFGIGSGTALLSIYGW) and the 'GWGGEG' C-terminal motif, which are hallmarks of GH10/GH11 xylanase families. A knowledgeable model familiar with GH families can recognize these motifs as indicative of glycan (polysaccharide) hydrolysis. This rules out B (amino-acid degradation: no protease/peptidase catalytic motifs such as Ser-His-Asp or Cys-His-Asn) and D (carotenoid biosynthesis: no phytoene synthase, desaturase, or cyclase motifs; carotenoid enzymes are typically membrane-associated and much larger). Between A (Cell wall degradation) and C (Glycan degradation): in formal pathway taxonomy (UniProt/KEGG), xylan degradation is classified under 'Glycan degradation,' not 'Cell wall degradation.' 'Cell wall degradation' is a functional/ecological description, not a standard pathway name. The question asks for the 'primary metabolic or signaling pathway,' which points to the formal pathway classification. Thus, recognizing GH motifs → glycan degradation as the formal pathway distinguishes C from A.",
    "missing_item_specific_fact": "",
    "reason": "The sequence-level features (signal peptide, GH-family motifs, size) combined with knowledge of glycoside hydrolase families and pathway taxonomy provide a credible, transferable inference chain that meaningfully distinguishes C from the other options. The GW…GW motif pattern is shared across many GH10/GH11 xylanases from diverse organisms, making this a family-level inference rather than a lookup of this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Xylan is both a glycan and a major component of plant cell walls. A biologist might reasonably describe xylanase activity as 'cell wall degradation' in a functional/ecological sense. However, in formal pathway databases (UniProt, KEGG), xylan degradation is categorized under 'Glycan degradation,' and 'Cell wall degradation' is not a standard pathway name. The question's phrasing ('primary metabolic or signaling pathway') favors the formal pathway taxonomy, making C the more precise answer, but A is not entirely unreasonable as a broader functional description."
  },
  "important_caveats": [
    "The UniProt pathway annotation is based on PROSITE-ProRule (ECO:0000255), a computational inference from protein-family motifs, not direct experimental measurement of pathway flux.",
    "The protein is also described as 'ethylene-inducing' (EIX), suggesting a signaling role in plant-pathogen interactions, but the enzymatic (xylanase) activity maps to glycan degradation.",
    "The distinction between 'Cell wall degradation' (A) and 'Glycan degradation' (C) depends on whether the question expects formal pathway taxonomy or functional description; the formal pathway name favors C.",
    "The reviewer-only evidence (accession, organism, entry name) was not available to the evaluated model; the reasoning above relies only on sequence features and general biological knowledge."
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
  "benchmark_sequence_length": 222,
  "benchmark_sequence_sha256": "2265146ae5d59cb592dd036988cd6b2763b6251bd85f07a031b262ea02925786",
  "current_entry_audit": {
    "entryVersion": 27,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-11-07",
    "sequenceVersion": 1
  },
  "current_record_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 222,
  "current_source_sequence_sha256": "2265146ae5d59cb592dd036988cd6b2763b6251bd85f07a031b262ea02925786",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 25,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A384K474",
  "selected_historical_entry_version": 25,
  "selected_historical_record_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "selected_historical_source_sequence_length": 222,
  "selected_historical_source_sequence_sha256": "2265146ae5d59cb592dd036988cd6b2763b6251bd85f07a031b262ea02925786",
  "selected_historical_version": {
    "accession": "A0A384K474",
    "database": "Swiss-Prot",
    "entryVersion": 25,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX2_BOTFB",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A384K474\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":27,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-11-07\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Noble rot fungus\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Leotiomycetes\",\"Helotiales\",\"Sclerotiniaceae\",\"Botrytis\"],\"scientificName\":\"Botrytis cinerea (strain B05.10)\",\"synonyms\":[\"Botryotinia fuckeliana\"],\"taxonId\":332648}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX2\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX21\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"Glycan degradation; xylan degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A384K474.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:59.392996+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "55204b82bbe53c219df38fd17bb07b90d74cea40d24431f98ad10936f0fb3921",
  "url": "https://rest.uniprot.org/uniprotkb/A0A384K474.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H1",
  "excerpt": "ID   EIX2_BOTFB              Reviewed;         222 AA.\nAC   A0A384K474;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   07-NOV-2018, sequence version 1.\nDT   28-JAN-2026, entry version 25.\nDE   RecName: Full=Ethylene-inducing xylanase 2 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX21 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX2 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX2 {ECO:0000303|PubMed:33205907}; ORFNames=BCIN_15g01600;\nOS   Botryotinia fuckeliana (strain B05.10) (Noble rot fungus) (Botrytis\nOS   cinerea).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Leotiomycetes;\nOC   Helotiales; Sclerotiniaceae; Botrytis.\nOX   NCBI_TaxID=332648;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.435228+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "url": "https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.435228+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-59",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "url": "https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25)

```json
{
  "entry_version": 25,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Glycan degradation; xylan degradation. {ECO:0000255|PROSITE-\nCC       ProRule:PRU01097}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:01.435228+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 70-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f401e20e06f466f7611bd91f76c327c904201b29c424133348114ef2358dffba",
  "url": "https://rest.uniprot.org/unisave/A0A384K474?format=txt&versions=25"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 115. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
