# pathway_0191

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0191.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVSFKSLLLAASAFTAVLGRPFDSFDGPDVNITDADELLVRRQVTANSEGTHNGYFYSWWSDGGGQVTYTMGAGSRYSVTWKDTGNFVGGKGWNPGTGRTINYGGSFSPQGNGYLAVYGWTRNPLIEYYVVESYGTYNPGSGGQLKGTVTTDGGTYNVYVSTRTNQPSIDGTRTFQQYWSVRTSKRVGGAVTMQNHFNAWAQFGMNLGAHYYQIVATEGNGDFVGTEIWGLARGCRR

[Multiple Choices]
A. Antifungal biosynthesis. .
B. iron-sulfur cluster biosynthesis. .
C. terpenoid biosynthesis.
D. Glycan degradation
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

> The exact supplied sequence matches a historical UniProt record that annotates its pathway as glycan degradation, specifically xylan degradation. That pathway annotation is attributed to a PROSITE ProRule, so it is computational rather than direct experimental pathway evidence.

Citations as saved: [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secreted fungal enzyme, and the sequence's length and enzyme-like, aromatic-rich pattern are compatible with a fungal xylanase. Xylanases hydrolyze xylan, a polysaccharide, so glycan degradation is meaningfully favored over the biosynthesis and iron-sulfur-cluster alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable inference from secreted fungal glycoside-hydrolase/xylanase patterns distinguishes the degradation choice without requiring the exact protein's recorded annotation. The sequence-based inference is not by itself definitive, but is credible among these alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, glycan degradation is the clear fit for a likely secreted xylan-hydrolyzing enzyme.


### Important caveats

- The matched historical pathway annotation is computationally assigned; it should not be represented as direct experimental validation of pathway membership.
- The current UniProt sequence differs from the supplied sequence, so the historical sequence-matched evidence is the applicable record.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted fungal enzyme, and the sequence's length and enzyme-like, aromatic-rich pattern are compatible with a fungal xylanase. Xylanases hydrolyze xylan, a polysaccharide, so glycan degradation is meaningfully favored over the biosynthesis and iron-sulfur-cluster alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from secreted fungal glycoside-hydrolase/xylanase patterns distinguishes the degradation choice without requiring the exact protein's recorded annotation. The sequence-based inference is not by itself definitive, but is credible among these alternatives."
  },
  "case_id": "pathway_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence matches a historical UniProt record that annotates its pathway as glycan degradation, specifically xylan degradation. That pathway annotation is attributed to a PROSITE ProRule, so it is computational rather than direct experimental pathway evidence."
  },
  "important_caveats": [
    "The matched historical pathway annotation is computationally assigned; it should not be represented as direct experimental validation of pathway membership.",
    "The current UniProt sequence differs from the supplied sequence, so the historical sequence-matched evidence is the applicable record."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, glycan degradation is the clear fit for a likely secreted xylan-hydrolyzing enzyme."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0191",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence matches a historical UniProt record that annotates its pathway as glycan degradation, specifically xylan degradation. That pathway annotation is attributed to a PROSITE ProRule, so it is computational rather than direct experimental pathway evidence.",
    "evidence_ids": ["H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secreted fungal enzyme, and the sequence's length and enzyme-like, aromatic-rich pattern are compatible with a fungal xylanase. Xylanases hydrolyze xylan, a polysaccharide, so glycan degradation is meaningfully favored over the biosynthesis and iron-sulfur-cluster alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A transferable inference from secreted fungal glycoside-hydrolase/xylanase patterns distinguishes the degradation choice without requiring the exact protein's recorded annotation. The sequence-based inference is not by itself definitive, but is credible among these alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, glycan degradation is the clear fit for a likely secreted xylan-hydrolyzing enzyme."
  },
  "important_caveats": [
    "The matched historical pathway annotation is computationally assigned; it should not be represented as direct experimental validation of pathway membership.",
    "The current UniProt sequence differs from the supplied sequence, so the historical sequence-matched evidence is the applicable record."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this protein (EIX2, G2X0L1) explicitly states the pathway as 'Glycan degradation; xylan degradation' (evidence C5, H3). The protein is annotated as EC 3.2.1.8 (Endo-1,4-beta-xylanase), a glycoside hydrolase that hydrolyzes xylan, a polysaccharide (glycan). The historical sequence (entry version 60, sequence version 1) matches the benchmark sequence exactly (237 AA, SHA256 match confirmed). The evidence code is ECO:0000255|PROSITE-ProRule:PRU01097, indicating computational family-based inference, but this is consistent with the well-characterized GH11 xylanase family. The expected answer D 'Glycan degradation' is directly supported.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays hallmark motifs of glycoside hydrolase family 11 (GH11) xylanases: a signal peptide (MVSFKSLLLAASAFTAVLGRP), followed by the conserved 'TGNFVGGKGWNPGTGRTINYGGSFSPQGNGYLAVYGW' region containing the characteristic catalytic glutamate pair and the beta-jellyroll fold signature. GH11 xylanases are a well-characterized ~180-250 AA family of secreted fungal/bacterial enzymes that hydrolyze xylan (a plant cell wall glycan). The sequence length (~237 AA) and overall architecture match this family. This is transferable knowledge from the extensive literature on GH11 xylanases (e.g., Trichoderma, Aspergillus, Bacillus xylanases). Among the choices: (A) antifungal biosynthesis involves non-ribosomal peptide synthetases or polyketide synthases with entirely different architecture; (B) iron-sulfur cluster biosynthesis involves IscU/NifU-type scaffolds with distinct motifs; (C) terpenoid biosynthesis involves terpene cyclases or prenyltransferases with different folds. Only (D) glycan degradation matches a secreted glycoside hydrolase with GH11 motifs. The EIX (ethylene-inducing xylanase) subfamily is also recognizable from the 'EIX' nomenclature established for Trichoderma viride xylanases, which are GH11 members.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH11 xylanase family is extensively characterized across many organisms. The conserved catalytic motifs (TGNF, the two catalytic Glu residues, the beta-jellyroll topology) are well-known transferable features. A model recognizing these motifs can confidently assign the protein to glycan degradation (xylan hydrolysis) rather than the other three pathways, which involve structurally and mechanistically unrelated enzyme classes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (antifungal biosynthesis, iron-sulfur cluster biosynthesis, terpenoid biosynthesis) involve enzyme classes with completely different architectures, cofactors, and sequence motifs compared to a GH11 glycoside hydrolase. The GH11 signature is distinctive enough to unambiguously point to glycan degradation among these options.


### Important caveats

- The UniProt pathway annotation uses evidence code ECO:0000255 (PROSITE-ProRule), indicating computational family-based inference rather than direct experimental pathway tracing, though the enzymatic activity (EC 3.2.1.8) has experimental support from PubMed:18720841.
- The current UniProt sequence (version 2, 250 AA) differs from the benchmark sequence (237 AA); however, the historical version 1 sequence matches exactly, confirming the annotation applies to the benchmark input.
- The 'ethylene-inducing' aspect of EIX proteins relates to their role in plant-pathogen signaling, but the primary enzymatic function is xylan hydrolysis (glycan degradation), which is what the question asks about.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays hallmark motifs of glycoside hydrolase family 11 (GH11) xylanases: a signal peptide (MVSFKSLLLAASAFTAVLGRP), followed by the conserved 'TGNFVGGKGWNPGTGRTINYGGSFSPQGNGYLAVYGW' region containing the characteristic catalytic glutamate pair and the beta-jellyroll fold signature. GH11 xylanases are a well-characterized ~180-250 AA family of secreted fungal/bacterial enzymes that hydrolyze xylan (a plant cell wall glycan). The sequence length (~237 AA) and overall architecture match this family. This is transferable knowledge from the extensive literature on GH11 xylanases (e.g., Trichoderma, Aspergillus, Bacillus xylanases). Among the choices: (A) antifungal biosynthesis involves non-ribosomal peptide synthetases or polyketide synthases with entirely different architecture; (B) iron-sulfur cluster biosynthesis involves IscU/NifU-type scaffolds with distinct motifs; (C) terpenoid biosynthesis involves terpene cyclases or prenyltransferases with different folds. Only (D) glycan degradation matches a secreted glycoside hydrolase with GH11 motifs. The EIX (ethylene-inducing xylanase) subfamily is also recognizable from the 'EIX' nomenclature established for Trichoderma viride xylanases, which are GH11 members.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH11 xylanase family is extensively characterized across many organisms. The conserved catalytic motifs (TGNF, the two catalytic Glu residues, the beta-jellyroll topology) are well-known transferable features. A model recognizing these motifs can confidently assign the protein to glycan degradation (xylan hydrolysis) rather than the other three pathways, which involve structurally and mechanistically unrelated enzyme classes."
  },
  "case_id": "pathway_0191",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this protein (EIX2, G2X0L1) explicitly states the pathway as 'Glycan degradation; xylan degradation' (evidence C5, H3). The protein is annotated as EC 3.2.1.8 (Endo-1,4-beta-xylanase), a glycoside hydrolase that hydrolyzes xylan, a polysaccharide (glycan). The historical sequence (entry version 60, sequence version 1) matches the benchmark sequence exactly (237 AA, SHA256 match confirmed). The evidence code is ECO:0000255|PROSITE-ProRule:PRU01097, indicating computational family-based inference, but this is consistent with the well-characterized GH11 xylanase family. The expected answer D 'Glycan degradation' is directly supported."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses evidence code ECO:0000255 (PROSITE-ProRule), indicating computational family-based inference rather than direct experimental pathway tracing, though the enzymatic activity (EC 3.2.1.8) has experimental support from PubMed:18720841.",
    "The current UniProt sequence (version 2, 250 AA) differs from the benchmark sequence (237 AA); however, the historical version 1 sequence matches exactly, confirming the annotation applies to the benchmark input.",
    "The 'ethylene-inducing' aspect of EIX proteins relates to their role in plant-pathogen signaling, but the primary enzymatic function is xylan hydrolysis (glycan degradation), which is what the question asks about."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (antifungal biosynthesis, iron-sulfur cluster biosynthesis, terpenoid biosynthesis) involve enzyme classes with completely different architectures, cofactors, and sequence motifs compared to a GH11 glycoside hydrolase. The GH11 signature is distinctive enough to unambiguously point to glycan degradation among these options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0191",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this protein (EIX2, G2X0L1) explicitly states the pathway as 'Glycan degradation; xylan degradation' (evidence C5, H3). The protein is annotated as EC 3.2.1.8 (Endo-1,4-beta-xylanase), a glycoside hydrolase that hydrolyzes xylan, a polysaccharide (glycan). The historical sequence (entry version 60, sequence version 1) matches the benchmark sequence exactly (237 AA, SHA256 match confirmed). The evidence code is ECO:0000255|PROSITE-ProRule:PRU01097, indicating computational family-based inference, but this is consistent with the well-characterized GH11 xylanase family. The expected answer D 'Glycan degradation' is directly supported.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays hallmark motifs of glycoside hydrolase family 11 (GH11) xylanases: a signal peptide (MVSFKSLLLAASAFTAVLGRP), followed by the conserved 'TGNFVGGKGWNPGTGRTINYGGSFSPQGNGYLAVYGW' region containing the characteristic catalytic glutamate pair and the beta-jellyroll fold signature. GH11 xylanases are a well-characterized ~180-250 AA family of secreted fungal/bacterial enzymes that hydrolyze xylan (a plant cell wall glycan). The sequence length (~237 AA) and overall architecture match this family. This is transferable knowledge from the extensive literature on GH11 xylanases (e.g., Trichoderma, Aspergillus, Bacillus xylanases). Among the choices: (A) antifungal biosynthesis involves non-ribosomal peptide synthetases or polyketide synthases with entirely different architecture; (B) iron-sulfur cluster biosynthesis involves IscU/NifU-type scaffolds with distinct motifs; (C) terpenoid biosynthesis involves terpene cyclases or prenyltransferases with different folds. Only (D) glycan degradation matches a secreted glycoside hydrolase with GH11 motifs. The EIX (ethylene-inducing xylanase) subfamily is also recognizable from the 'EIX' nomenclature established for Trichoderma viride xylanases, which are GH11 members.",
    "missing_item_specific_fact": "",
    "reason": "The GH11 xylanase family is extensively characterized across many organisms. The conserved catalytic motifs (TGNF, the two catalytic Glu residues, the beta-jellyroll topology) are well-known transferable features. A model recognizing these motifs can confidently assign the protein to glycan degradation (xylan hydrolysis) rather than the other three pathways, which involve structurally and mechanistically unrelated enzyme classes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (antifungal biosynthesis, iron-sulfur cluster biosynthesis, terpenoid biosynthesis) involve enzyme classes with completely different architectures, cofactors, and sequence motifs compared to a GH11 glycoside hydrolase. The GH11 signature is distinctive enough to unambiguously point to glycan degradation among these options."
  },
  "important_caveats": [
    "The UniProt pathway annotation uses evidence code ECO:0000255 (PROSITE-ProRule), indicating computational family-based inference rather than direct experimental pathway tracing, though the enzymatic activity (EC 3.2.1.8) has experimental support from PubMed:18720841.",
    "The current UniProt sequence (version 2, 250 AA) differs from the benchmark sequence (237 AA); however, the historical version 1 sequence matches exactly, confirming the annotation applies to the benchmark input.",
    "The 'ethylene-inducing' aspect of EIX proteins relates to their role in plant-pathogen signaling, but the primary enzymatic function is xylan hydrolysis (glycan degradation), which is what the question asks about."
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
  "benchmark_sequence_length": 237,
  "benchmark_sequence_sha256": "cfdd4b83b607c771888b0e9deb32dd898625aa384e94930782d11bae4f218452",
  "current_entry_audit": {
    "entryVersion": 62,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2026-06-10",
    "sequenceVersion": 2
  },
  "current_record_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "current_sequence_comparison": "mismatch",
  "current_source_sequence_length": 250,
  "current_source_sequence_sha256": "5530b30cec055de49b753bba02a39d9eca395ae75579bf67e16c02b7b3c232ce",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 60,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G2X0L1",
  "selected_historical_entry_version": 60,
  "selected_historical_record_sha256": "fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a",
  "selected_historical_source_sequence_length": 237,
  "selected_historical_source_sequence_sha256": "cfdd4b83b607c771888b0e9deb32dd898625aa384e94930782d11bae4f218452",
  "selected_historical_version": {
    "accession": "G2X0L1",
    "database": "Swiss-Prot",
    "entryVersion": 60,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX2_VERDV",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- The current UniProt sequence differs from the supplied sequence; applicability of current annotation excerpts is qualified by that mismatch.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G2X0L1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":62,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2026-06-10\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Verticillium wilt\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Glomerellales\",\"Plectosphaerellaceae\",\"Verticillium\"],\"scientificName\":\"Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\",\"taxonId\":498257}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"1,4-beta-D-xylan xylanohydrolase G\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18720841\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase G\"},\"shortNames\":[{\"value\":\"Xylanase G\"}]}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18720841\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"Glycan degradation; xylan degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang G.\",\"Rao B.\",\"Ye J.\",\"Ma L.\",\"Zhang X.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18720841\"}],\"citationType\":\"journal article\",\"firstPage\":\"765\",\"id\":\"18720841\",\"journal\":\"Wei Sheng Wu Xue Bao\",\"lastPage\":\"771\",\"publicationDate\":\"2008\",\"title\":\"Molecular cloning and heterologous expression of a new xylanase gene from Verticillium dahliae.\",\"volume\":\"48\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"SUBCELLULAR LOCATION\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)

```json
{
  "entry_version": 60,
  "evidence_id": "H1",
  "excerpt": "ID   EIX2_VERDV              Reviewed;         237 AA.\nAC   G2X0L1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 60.\nDE   RecName: Full=Ethylene-inducing xylanase 2 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX2 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX2 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX2 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_03790;\nOS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\nOS   (Verticillium wilt).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.\nOX   NCBI_TaxID=498257;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:04.256317+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a",
  "url": "https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)

```json
{
  "entry_version": 60,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:04.256317+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a",
  "url": "https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)

```json
{
  "entry_version": 60,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Glycan degradation; xylan degradation. {ECO:0000255|PROSITE-\nCC       ProRule:PRU01097}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:04.256317+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a",
  "url": "https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 191. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
