# pathway_0192

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0192.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Capsule biogenesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKEIKIQNIIINEEKAPLVVPEIGINHNGSLELAKIMVDAAFSAGAKIIKHQTHIVEDEMSKAAKKVIPGNAKISIYEIMQKCALDYKDELALKEYTEKLGLVYLSTPFSRAGANRLEDMGVSAFKIGSGECNNYPLIKHIAAFKKPMIVSTGMNSIESIKPTVKILLDNEIPFVLMHTTNLYPTPHNLVRLNAMLELKKEFSCMVGLSDHTTDNLACLGAVALGACVLERHFTDSMDRSGPDIVCSMDTKALKELIMQSEQMAIMRGNNESKKAAKQEQVTIDFAFASVVSIKDIKKGEVLSMDNIWVKRPGLGGISAAEFENILGKKALRDIENDTQLSYEDFA

[Multiple Choices]
A. L-valine biosynthesis
B. Capsule biogenesis
C. ajmaline biosynthesis. .
D. L-threonine from L-aspartate: step 5/5. .
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

> The sequence-matched UniProt records annotate the protein's pathway as capsule biogenesis and capsule polysaccharide biosynthesis, with experimental evidence cited. The annotation supports choice B; the cited study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 346-aa enzyme-like sequence is consistent with the NeuB family of N-acetylneuraminate synthases. Transferable knowledge of this family links it to sialic-acid precursor synthesis, which can feed bacterial capsule polysaccharide biosynthesis. That provides a meaningful basis for choosing capsule biogenesis over valine or threonine biosynthesis; ajmaline biosynthesis is also a poor fit for this enzyme-family inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference can distinguish the offered pathway choices without relying on the exact protein's database record. It is probabilistic: the sequence alone does not establish the organism's particular pathway context or experimentally confirmed role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered options, capsule biogenesis is the defensible choice given the inferred sialic-acid-synthase family.


### Important caveats

- The reviewer-only source evidence includes experimental-evidence annotations, but the underlying paper was not independently assessed.
- The archived sequence-matched annotation supports the answer; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 346-aa enzyme-like sequence is consistent with the NeuB family of N-acetylneuraminate synthases. Transferable knowledge of this family links it to sialic-acid precursor synthesis, which can feed bacterial capsule polysaccharide biosynthesis. That provides a meaningful basis for choosing capsule biogenesis over valine or threonine biosynthesis; ajmaline biosynthesis is also a poor fit for this enzyme-family inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can distinguish the offered pathway choices without relying on the exact protein's database record. It is probabilistic: the sequence alone does not establish the organism's particular pathway context or experimentally confirmed role."
  },
  "case_id": "pathway_0192",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate the protein's pathway as capsule biogenesis and capsule polysaccharide biosynthesis, with experimental evidence cited. The annotation supports choice B; the cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only source evidence includes experimental-evidence annotations, but the underlying paper was not independently assessed.",
    "The archived sequence-matched annotation supports the answer; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, capsule biogenesis is the defensible choice given the inferred sialic-acid-synthase family."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0192",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records annotate the protein's pathway as capsule biogenesis and capsule polysaccharide biosynthesis, with experimental evidence cited. The annotation supports choice B; the cited study was not independently reviewed here.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 346-aa enzyme-like sequence is consistent with the NeuB family of N-acetylneuraminate synthases. Transferable knowledge of this family links it to sialic-acid precursor synthesis, which can feed bacterial capsule polysaccharide biosynthesis. That provides a meaningful basis for choosing capsule biogenesis over valine or threonine biosynthesis; ajmaline biosynthesis is also a poor fit for this enzyme-family inference.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can distinguish the offered pathway choices without relying on the exact protein's database record. It is probabilistic: the sequence alone does not establish the organism's particular pathway context or experimentally confirmed role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, capsule biogenesis is the defensible choice given the inferred sialic-acid-synthase family."
  },
  "important_caveats": [
    "The reviewer-only source evidence includes experimental-evidence annotations, but the underlying paper was not independently assessed.",
    "The archived sequence-matched annotation supports the answer; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DY06 (N-acetylneuraminate synthase, EC 2.5.1.56, Neu5Ac synthase) from Campylobacter jejuni explicitly annotates the pathway as 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The protein catalyzes condensation of N-acetyl-D-mannosamine with PEP to form N-acetylneuraminic acid (Neu5Ac), a sialic acid incorporated into the capsule polysaccharide of C. jejuni. The expected answer B (Capsule biogenesis) is directly and experimentally supported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable features of the sialic acid synthase (NeuB/Neu5Ac synthase) family: a 'GMN' motif (~residues 130-132) characteristic of PEP binding in sialic acid synthases; a cluster of histidines in 'MHTTNLYPTPHN' consistent with catalytic residues; a 'GLSDHTTDNL' motif in the catalytic domain; and a C-terminal architecture with P-loop-like regions ('RGNNESKKAAKQEQVTIDFAFASVVSIKDIKKGEVLSMDNIWVKRPGLGG') consistent with the TIM-barrel fold of sialic acid synthases. Transferable knowledge from well-studied NeuB homologs (E. coli, C. jejuni) identifies this enzyme family. Sialic acids (Neu5Ac) are well-known components of bacterial capsules, and in Campylobacter the sialic acid biosynthetic pathway is dedicated to capsule polysaccharide production. Among the four options: (C) ajmaline biosynthesis is a plant indole-alkaloid pathway incompatible with a bacterial protein; (D) threonine synthase is a PLP-dependent enzyme with a completely different fold and motifs; (A) L-valine biosynthesis involves branched-chain amino acid enzymes (AHAS, dihydroxy-acid dehydratase, KARI, aminotransferase) with unrelated architecture. Recognizing the sialic acid synthase family thus meaningfully distinguishes option B from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize sialic acid synthase family motifs (GMN PEP-binding motif, catalytic His cluster, TIM-barrel architecture) from the sequence, connect them to sialic acid biosynthesis, and then to capsule biogenesis as the pathway where sialic acids serve as capsule polysaccharide components. The other three options are eliminable by fold/family mismatch (A, D) or organismal context (C, plant-specific). This is a legitimate family-level inference using transferable knowledge of well-characterized sialic acid synthase homologs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated by biological context: ajmaline is plant-specific (eliminates C for a bacterial protein), threonine synthase and valine biosynthesis enzymes have entirely different folds and motifs (eliminates A and D). Sialic acid synthase family recognition uniquely points to capsule biogenesis (B). No ambiguity among the offered choices.


### Important caveats

- The UniProt annotation was added in 2025 based on a 2024 experimental paper (PubMed:38382015). The benchmark author's source snapshot is unknown; if constructed before June 2025, the pathway annotation may not have existed in the source database at construction time, though the sequence and family assignment would still be recognizable.
- Recognition of sialic acid synthase family motifs from a Campylobacter sequence (which may diverge somewhat from the best-studied E. coli NeuB) requires moderate expertise but is within the scope of transferable family-level knowledge.
- The pathway label 'Capsule biogenesis' is a broad UniProt category; the specific sub-pathway is 'capsule polysaccharide biosynthesis' involving sialic acid incorporation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable features of the sialic acid synthase (NeuB/Neu5Ac synthase) family: a 'GMN' motif (~residues 130-132) characteristic of PEP binding in sialic acid synthases; a cluster of histidines in 'MHTTNLYPTPHN' consistent with catalytic residues; a 'GLSDHTTDNL' motif in the catalytic domain; and a C-terminal architecture with P-loop-like regions ('RGNNESKKAAKQEQVTIDFAFASVVSIKDIKKGEVLSMDNIWVKRPGLGG') consistent with the TIM-barrel fold of sialic acid synthases. Transferable knowledge from well-studied NeuB homologs (E. coli, C. jejuni) identifies this enzyme family. Sialic acids (Neu5Ac) are well-known components of bacterial capsules, and in Campylobacter the sialic acid biosynthetic pathway is dedicated to capsule polysaccharide production. Among the four options: (C) ajmaline biosynthesis is a plant indole-alkaloid pathway incompatible with a bacterial protein; (D) threonine synthase is a PLP-dependent enzyme with a completely different fold and motifs; (A) L-valine biosynthesis involves branched-chain amino acid enzymes (AHAS, dihydroxy-acid dehydratase, KARI, aminotransferase) with unrelated architecture. Recognizing the sialic acid synthase family thus meaningfully distinguishes option B from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize sialic acid synthase family motifs (GMN PEP-binding motif, catalytic His cluster, TIM-barrel architecture) from the sequence, connect them to sialic acid biosynthesis, and then to capsule biogenesis as the pathway where sialic acids serve as capsule polysaccharide components. The other three options are eliminable by fold/family mismatch (A, D) or organismal context (C, plant-specific). This is a legitimate family-level inference using transferable knowledge of well-characterized sialic acid synthase homologs."
  },
  "case_id": "pathway_0192",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DY06 (N-acetylneuraminate synthase, EC 2.5.1.56, Neu5Ac synthase) from Campylobacter jejuni explicitly annotates the pathway as 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The protein catalyzes condensation of N-acetyl-D-mannosamine with PEP to form N-acetylneuraminic acid (Neu5Ac), a sialic acid incorporated into the capsule polysaccharide of C. jejuni. The expected answer B (Capsule biogenesis) is directly and experimentally supported."
  },
  "important_caveats": [
    "The UniProt annotation was added in 2025 based on a 2024 experimental paper (PubMed:38382015). The benchmark author's source snapshot is unknown; if constructed before June 2025, the pathway annotation may not have existed in the source database at construction time, though the sequence and family assignment would still be recognizable.",
    "Recognition of sialic acid synthase family motifs from a Campylobacter sequence (which may diverge somewhat from the best-studied E. coli NeuB) requires moderate expertise but is within the scope of transferable family-level knowledge.",
    "The pathway label 'Capsule biogenesis' is a broad UniProt category; the specific sub-pathway is 'capsule polysaccharide biosynthesis' involving sialic acid incorporation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by biological context: ajmaline is plant-specific (eliminates C for a bacterial protein), threonine synthase and valine biosynthesis enzymes have entirely different folds and motifs (eliminates A and D). Sialic acid synthase family recognition uniquely points to capsule biogenesis (B). No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0192",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DY06 (N-acetylneuraminate synthase, EC 2.5.1.56, Neu5Ac synthase) from Campylobacter jejuni explicitly annotates the pathway as 'Capsule biogenesis; capsule polysaccharide biosynthesis' with experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The protein catalyzes condensation of N-acetyl-D-mannosamine with PEP to form N-acetylneuraminic acid (Neu5Ac), a sialic acid incorporated into the capsule polysaccharide of C. jejuni. The expected answer B (Capsule biogenesis) is directly and experimentally supported.",
    "evidence_ids": ["C5", "C6", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable features of the sialic acid synthase (NeuB/Neu5Ac synthase) family: a 'GMN' motif (~residues 130-132) characteristic of PEP binding in sialic acid synthases; a cluster of histidines in 'MHTTNLYPTPHN' consistent with catalytic residues; a 'GLSDHTTDNL' motif in the catalytic domain; and a C-terminal architecture with P-loop-like regions ('RGNNESKKAAKQEQVTIDFAFASVVSIKDIKKGEVLSMDNIWVKRPGLGG') consistent with the TIM-barrel fold of sialic acid synthases. Transferable knowledge from well-studied NeuB homologs (E. coli, C. jejuni) identifies this enzyme family. Sialic acids (Neu5Ac) are well-known components of bacterial capsules, and in Campylobacter the sialic acid biosynthetic pathway is dedicated to capsule polysaccharide production. Among the four options: (C) ajmaline biosynthesis is a plant indole-alkaloid pathway incompatible with a bacterial protein; (D) threonine synthase is a PLP-dependent enzyme with a completely different fold and motifs; (A) L-valine biosynthesis involves branched-chain amino acid enzymes (AHAS, dihydroxy-acid dehydratase, KARI, aminotransferase) with unrelated architecture. Recognizing the sialic acid synthase family thus meaningfully distinguishes option B from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize sialic acid synthase family motifs (GMN PEP-binding motif, catalytic His cluster, TIM-barrel architecture) from the sequence, connect them to sialic acid biosynthesis, and then to capsule biogenesis as the pathway where sialic acids serve as capsule polysaccharide components. The other three options are eliminable by fold/family mismatch (A, D) or organismal context (C, plant-specific). This is a legitimate family-level inference using transferable knowledge of well-characterized sialic acid synthase homologs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by biological context: ajmaline is plant-specific (eliminates C for a bacterial protein), threonine synthase and valine biosynthesis enzymes have entirely different folds and motifs (eliminates A and D). Sialic acid synthase family recognition uniquely points to capsule biogenesis (B). No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation was added in 2025 based on a 2024 experimental paper (PubMed:38382015). The benchmark author's source snapshot is unknown; if constructed before June 2025, the pathway annotation may not have existed in the source database at construction time, though the sequence and family assignment would still be recognizable.",
    "Recognition of sialic acid synthase family motifs from a Campylobacter sequence (which may diverge somewhat from the best-studied E. coli NeuB) requires moderate expertise but is within the scope of transferable family-level knowledge.",
    "The pathway label 'Capsule biogenesis' is a broad UniProt category; the specific sub-pathway is 'capsule polysaccharide biosynthesis' involving sialic acid incorporation."
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
  "benchmark_sequence_length": 346,
  "benchmark_sequence_sha256": "8542949467c46c0d10eb516705d760b1c4148a32078df1045ffb85da51143601",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 346,
  "current_source_sequence_sha256": "8542949467c46c0d10eb516705d760b1c4148a32078df1045ffb85da51143601",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DY06",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0",
  "selected_historical_source_sequence_length": 346,
  "selected_historical_source_sequence_sha256": "8542949467c46c0d10eb516705d760b1c4148a32078df1045ffb85da51143601",
  "selected_historical_version": {
    "accession": "P0DY06",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NEUAS_CAMJ8",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DY06\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:03.200320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY06.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:03.200320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY06.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Campylobacterota\",\"Epsilonproteobacteria\",\"Campylobacterales\",\"Campylobacteraceae\",\"Campylobacter\"],\"scientificName\":\"Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC 11828)\",\"taxonId\":407148}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:03.200320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY06.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"2.5.1.56\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"N-acetylneuraminate synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"Neu5Ac synthase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:03.200320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY06.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"Capsule biogenesis; capsule polysaccharide biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:30:03.200320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY06.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY06.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ghosh M.K.\",\"Raushel F.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38382015\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.3c00664\"}],\"citationType\":\"journal article\",\"firstPage\":\"688\",\"id\":\"38382015\",\"journal\":\"Biochemistry\",\"lastPage\":\"698\",\"publicationDate\":\"2024\",\"title\":\"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"81116 / NCTC 11828\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:03.200320+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "360a6e23ffa22a96d2f530ce41b08596efad1a8a83e5e9a083cacacc7581d59a",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY06.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   NEUAS_CAMJ8             Reviewed;         346 AA.\nAC   P0DY06;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};\nDE            Short=Neu5Ac synthase {ECO:0000303|PubMed:38382015};\nDE            EC=2.5.1.56 {ECO:0000269|PubMed:38382015};\nGN   Name=HS6.11 {ECO:0000303|PubMed:38382015};\nGN   OrderedLocusNames=C8J_1339 {ECO:0000312|EMBL:ABV52937.1};\nOS   Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC\nOS   11828).\nOC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;\nOC   Campylobacterales; Campylobacteraceae; Campylobacter.\nOX   NCBI_TaxID=407148;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:07.414593+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0",
  "url": "https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRC   STRAIN=81116 / NCTC 11828;\nRX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;\nRA   Ghosh M.K., Raushel F.M.;\nRT   \"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-\nRT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter\nRT   jejuni.\";\nRL   Biochemistry 63:688-698(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:07.414593+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0",
  "url": "https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Capsule biogenesis; capsule polysaccharide biosynthesis.\nCC       {ECO:0000269|PubMed:38382015}.\nCC   ---------------------------------------------------------------------------\nCC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms\nCC   Distributed under the Creative Commons Attribution (CC BY 4.0) License\nCC   ---------------------------------------------------------------------------\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:07.414593+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7e4ab42f0bda2ecc304cdd042f2bc5a8d831d80e65982976501788f9a05ab6b0",
  "url": "https://rest.uniprot.org/unisave/P0DY06?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 192. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
