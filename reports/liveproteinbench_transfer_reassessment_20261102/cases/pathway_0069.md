# pathway_0069

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0069.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Capsule biogenesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVIAVIPARSGSKGIKNKNLVLLNNQPLIYYTIKAALNSKCISKVLVSSDSEEILSYAKSQNVDILKRPIELAQDDTTSDKVLLHALEFYKDYEDVIFLQPTSPLRTNIHIDEAFKIYKNSDANALISVTECDNKILKAFICDNKGDLKGICDDEYPFMPRQKLPKTYMSNGAIYILSIKDFLNKPSFLQSKTKYFLMNKISSLDIDNLEDLKQVENIQKMKGCVVWISGLAGAGKTTISSGLYKKLKEKYNNSVLLDGDELRKIFKHTGYTREERLESAKKISSLCSFLAKNDIIVICATISLFEEIYLLNRNTIENYFEVFVDCPMEELILRDQKGLYSGALKGEIKDVVGVDIKYAKPNAHYIIDNSSKTDLEKKINNLYNEVELFFNKER

[Multiple Choices]
A. 5-methoxycarbonylmethyl-2-thiouridine-tRNA biosynthesis. .
B. spheroidene biosynthesis. .
C. Capsule biogenesis
D. Amino-acid degradation
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

> The sequence-matched historical UniProt record assigns the protein to capsule biogenesis and cites a publication addressing its role in capsular-polysaccharide biosynthesis. This supports choice C; the annotation includes experimental evidence, though the primary paper was not independently reviewed here.

Citations as saved: [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 394-aa sequence is consistent with a soluble nucleotide-dependent enzyme and contains a Walker-A-like GxxxxGKT motif. Transferable knowledge of nucleotide-activation enzymes and their roles in making activated sugar precursors makes capsule-polysaccharide biosynthesis a plausible fit. This distinguishes C from the tRNA-modification and carotenoid-biosynthesis options, while the broad amino-acid-degradation option is a less direct match. The sequence motif alone is not diagnostic, so the inference is probabilistic rather than conclusive.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family- and mechanism-level inference from the sequence can meaningfully favor capsule biogenesis among these alternatives without relying on the target's recorded annotation. Exact identification of the enzyme would strengthen the case, but is not necessary to distinguish the offered choices plausibly.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Capsule biogenesis is the clearest offered pathway for a nucleotide-dependent enzyme plausibly involved in producing capsule sugar precursors; no other listed option is comparably supported by the sequence.


### Important caveats

- The Walker-A-like motif is shared by many nucleotide-binding proteins and does not by itself establish enzyme identity or pathway.
- The pathway annotation is database evidence linked to a publication; the cited primary study was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 394-aa sequence is consistent with a soluble nucleotide-dependent enzyme and contains a Walker-A-like GxxxxGKT motif. Transferable knowledge of nucleotide-activation enzymes and their roles in making activated sugar precursors makes capsule-polysaccharide biosynthesis a plausible fit. This distinguishes C from the tRNA-modification and carotenoid-biosynthesis options, while the broad amino-acid-degradation option is a less direct match. The sequence motif alone is not diagnostic, so the inference is probabilistic rather than conclusive.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family- and mechanism-level inference from the sequence can meaningfully favor capsule biogenesis among these alternatives without relying on the target's recorded annotation. Exact identification of the enzyme would strengthen the case, but is not necessary to distinguish the offered choices plausibly."
  },
  "case_id": "pathway_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns the protein to capsule biogenesis and cites a publication addressing its role in capsular-polysaccharide biosynthesis. This supports choice C; the annotation includes experimental evidence, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The Walker-A-like motif is shared by many nucleotide-binding proteins and does not by itself establish enzyme identity or pathway.",
    "The pathway annotation is database evidence linked to a publication; the cited primary study was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Capsule biogenesis is the clearest offered pathway for a nucleotide-dependent enzyme plausibly involved in producing capsule sugar precursors; no other listed option is comparably supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns the protein to capsule biogenesis and cites a publication addressing its role in capsular-polysaccharide biosynthesis. This supports choice C; the annotation includes experimental evidence, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 394-aa sequence is consistent with a soluble nucleotide-dependent enzyme and contains a Walker-A-like GxxxxGKT motif. Transferable knowledge of nucleotide-activation enzymes and their roles in making activated sugar precursors makes capsule-polysaccharide biosynthesis a plausible fit. This distinguishes C from the tRNA-modification and carotenoid-biosynthesis options, while the broad amino-acid-degradation option is a less direct match. The sequence motif alone is not diagnostic, so the inference is probabilistic rather than conclusive.",
    "missing_item_specific_fact": "",
    "reason": "A family- and mechanism-level inference from the sequence can meaningfully favor capsule biogenesis among these alternatives without relying on the target's recorded annotation. Exact identification of the enzyme would strengthen the case, but is not necessary to distinguish the offered choices plausibly."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Capsule biogenesis is the clearest offered pathway for a nucleotide-dependent enzyme plausibly involved in producing capsule sugar precursors; no other listed option is comparably supported by the sequence."
  },
  "important_caveats": [
    "The Walker-A-like motif is shared by many nucleotide-binding proteins and does not by itself establish enzyme identity or pathway.",
    "The pathway annotation is database evidence linked to a publication; the cited primary study was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (P0DY07) annotates this protein as N-acylneuraminate cytidylyltransferase (CMP-Neu5Ac synthase, EC 2.7.7.43) with the pathway 'Capsule biogenesis; capsule polysaccharide biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024 Biochemistry). The 2024 paper explicitly demonstrates that CMP-Neu5Ac is synthesized for the capsular polysaccharides of Campylobacter jejuni. The expected answer C is well-supported by direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical P-loop/Walker A nucleotide-binding motif 'GAGAGKTT' (around residues 188-195, within 'VWISGLAGAGKTTISSGLYKK'), characteristic of the Rossmann-fold nucleotidyltransferase superfamily. Combined with the ~394-aa size and a putative sugar-binding region ('CATISLF'), the overall architecture is consistent with a CMP-sugar synthase (nucleotidyltransferase). Among the four options: (A) mnm5s2U-tRNA biosynthesis involves thiouridylases (MnmA), GTPases (MnmE), and flavin oxidoreductases (MnmG)—none are nucleotidyltransferases; (B) spheroidene biosynthesis involves membrane-bound carotenoid desaturases, phytoene synthases, and cyclases—no nucleotidyltransferase fold; (D) amino-acid degradation involves transaminases (PLP-dependent), oxidases (FAD-dependent), and deaminases—no nucleotidyltransferase fold. Only option C (capsule biogenesis) involves a nucleotidyltransferase: CMP-Neu5Ac synthase (CMP-Neu5Ac synthetase) is a well-characterized member of the nucleotidyltransferase superfamily that activates sialic acid as CMP-Neu5Ac for incorporation into capsular polysaccharides. This is textbook knowledge about the CMP-sugar synthase family (CMP-Neu5Ac, CMP-KDO, CMP-glucose) and their role in polysaccharide/capsule biosynthesis, transferable across bacterial species.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The nucleotidyltransferase fold (identified by the P-loop motif and overall architecture) is a well-known, transferable structural feature. Knowing that CMP-sugar synthases are nucleotidyltransferases involved in capsule/polysaccharide biosynthesis, while the other three pathways involve entirely different enzyme classes (tRNA-modifying enzymes, carotenoid biosynthesis enzymes, amino-acid catabolic enzymes), provides a concrete and credible inference that meaningfully distinguishes option C from A, B, and D without requiring recall of this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent clearly distinct enzyme classes and pathways. The nucleotidyltransferase fold eliminates A (tRNA modification enzymes), B (carotenoid biosynthesis enzymes), and D (amino-acid degradation enzymes), leaving C as the only pathway involving a nucleotidyltransferase. No ambiguity among the offered choices.


### Important caveats

- The P-loop motif (GAGAGKTT) is common across many nucleotide-binding proteins (kinases, GTPases, helicases, nucleotidyltransferases). The inference relies on the overall protein architecture (size, domain arrangement, sugar-binding region) being consistent with a CMP-sugar synthase rather than a kinase or GTPase.
- The reviewer-only evidence confirms the protein is from Campylobacter jejuni and was characterized experimentally in 2024, but the transferable argument does not depend on knowing the organism or accession.
- The specific sugar substrate (Neu5Ac vs. KDO vs. glucose) cannot be determined from the P-loop alone, but among the four offered pathway options, only capsule biogenesis involves a nucleotidyltransferase, so the distinction is sufficient for this multiple-choice question.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical P-loop/Walker A nucleotide-binding motif 'GAGAGKTT' (around residues 188-195, within 'VWISGLAGAGKTTISSGLYKK'), characteristic of the Rossmann-fold nucleotidyltransferase superfamily. Combined with the ~394-aa size and a putative sugar-binding region ('CATISLF'), the overall architecture is consistent with a CMP-sugar synthase (nucleotidyltransferase). Among the four options: (A) mnm5s2U-tRNA biosynthesis involves thiouridylases (MnmA), GTPases (MnmE), and flavin oxidoreductases (MnmG)—none are nucleotidyltransferases; (B) spheroidene biosynthesis involves membrane-bound carotenoid desaturases, phytoene synthases, and cyclases—no nucleotidyltransferase fold; (D) amino-acid degradation involves transaminases (PLP-dependent), oxidases (FAD-dependent), and deaminases—no nucleotidyltransferase fold. Only option C (capsule biogenesis) involves a nucleotidyltransferase: CMP-Neu5Ac synthase (CMP-Neu5Ac synthetase) is a well-characterized member of the nucleotidyltransferase superfamily that activates sialic acid as CMP-Neu5Ac for incorporation into capsular polysaccharides. This is textbook knowledge about the CMP-sugar synthase family (CMP-Neu5Ac, CMP-KDO, CMP-glucose) and their role in polysaccharide/capsule biosynthesis, transferable across bacterial species.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The nucleotidyltransferase fold (identified by the P-loop motif and overall architecture) is a well-known, transferable structural feature. Knowing that CMP-sugar synthases are nucleotidyltransferases involved in capsule/polysaccharide biosynthesis, while the other three pathways involve entirely different enzyme classes (tRNA-modifying enzymes, carotenoid biosynthesis enzymes, amino-acid catabolic enzymes), provides a concrete and credible inference that meaningfully distinguishes option C from A, B, and D without requiring recall of this specific protein's database entry."
  },
  "case_id": "pathway_0069",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (P0DY07) annotates this protein as N-acylneuraminate cytidylyltransferase (CMP-Neu5Ac synthase, EC 2.7.7.43) with the pathway 'Capsule biogenesis; capsule polysaccharide biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024 Biochemistry). The 2024 paper explicitly demonstrates that CMP-Neu5Ac is synthesized for the capsular polysaccharides of Campylobacter jejuni. The expected answer C is well-supported by direct experimental evidence."
  },
  "important_caveats": [
    "The P-loop motif (GAGAGKTT) is common across many nucleotide-binding proteins (kinases, GTPases, helicases, nucleotidyltransferases). The inference relies on the overall protein architecture (size, domain arrangement, sugar-binding region) being consistent with a CMP-sugar synthase rather than a kinase or GTPase.",
    "The reviewer-only evidence confirms the protein is from Campylobacter jejuni and was characterized experimentally in 2024, but the transferable argument does not depend on knowing the organism or accession.",
    "The specific sugar substrate (Neu5Ac vs. KDO vs. glucose) cannot be determined from the P-loop alone, but among the four offered pathway options, only capsule biogenesis involves a nucleotidyltransferase, so the distinction is sufficient for this multiple-choice question."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct enzyme classes and pathways. The nucleotidyltransferase fold eliminates A (tRNA modification enzymes), B (carotenoid biosynthesis enzymes), and D (amino-acid degradation enzymes), leaving C as the only pathway involving a nucleotidyltransferase. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0069",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (P0DY07) annotates this protein as N-acylneuraminate cytidylyltransferase (CMP-Neu5Ac synthase, EC 2.7.7.43) with the pathway 'Capsule biogenesis; capsule polysaccharide biosynthesis' supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024 Biochemistry). The 2024 paper explicitly demonstrates that CMP-Neu5Ac is synthesized for the capsular polysaccharides of Campylobacter jejuni. The expected answer C is well-supported by direct experimental evidence.",
    "evidence_ids": ["C5", "C6", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical P-loop/Walker A nucleotide-binding motif 'GAGAGKTT' (around residues 188-195, within 'VWISGLAGAGKTTISSGLYKK'), characteristic of the Rossmann-fold nucleotidyltransferase superfamily. Combined with the ~394-aa size and a putative sugar-binding region ('CATISLF'), the overall architecture is consistent with a CMP-sugar synthase (nucleotidyltransferase). Among the four options: (A) mnm5s2U-tRNA biosynthesis involves thiouridylases (MnmA), GTPases (MnmE), and flavin oxidoreductases (MnmG)—none are nucleotidyltransferases; (B) spheroidene biosynthesis involves membrane-bound carotenoid desaturases, phytoene synthases, and cyclases—no nucleotidyltransferase fold; (D) amino-acid degradation involves transaminases (PLP-dependent), oxidases (FAD-dependent), and deaminases—no nucleotidyltransferase fold. Only option C (capsule biogenesis) involves a nucleotidyltransferase: CMP-Neu5Ac synthase (CMP-Neu5Ac synthetase) is a well-characterized member of the nucleotidyltransferase superfamily that activates sialic acid as CMP-Neu5Ac for incorporation into capsular polysaccharides. This is textbook knowledge about the CMP-sugar synthase family (CMP-Neu5Ac, CMP-KDO, CMP-glucose) and their role in polysaccharide/capsule biosynthesis, transferable across bacterial species.",
    "missing_item_specific_fact": "",
    "reason": "The nucleotidyltransferase fold (identified by the P-loop motif and overall architecture) is a well-known, transferable structural feature. Knowing that CMP-sugar synthases are nucleotidyltransferases involved in capsule/polysaccharide biosynthesis, while the other three pathways involve entirely different enzyme classes (tRNA-modifying enzymes, carotenoid biosynthesis enzymes, amino-acid catabolic enzymes), provides a concrete and credible inference that meaningfully distinguishes option C from A, B, and D without requiring recall of this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent clearly distinct enzyme classes and pathways. The nucleotidyltransferase fold eliminates A (tRNA modification enzymes), B (carotenoid biosynthesis enzymes), and D (amino-acid degradation enzymes), leaving C as the only pathway involving a nucleotidyltransferase. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The P-loop motif (GAGAGKTT) is common across many nucleotide-binding proteins (kinases, GTPases, helicases, nucleotidyltransferases). The inference relies on the overall protein architecture (size, domain arrangement, sugar-binding region) being consistent with a CMP-sugar synthase rather than a kinase or GTPase.",
    "The reviewer-only evidence confirms the protein is from Campylobacter jejuni and was characterized experimentally in 2024, but the transferable argument does not depend on knowing the organism or accession.",
    "The specific sugar substrate (Neu5Ac vs. KDO vs. glucose) cannot be determined from the P-loop alone, but among the four offered pathway options, only capsule biogenesis involves a nucleotidyltransferase, so the distinction is sufficient for this multiple-choice question."
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
  "benchmark_sequence_length": 394,
  "benchmark_sequence_sha256": "af09f26a5420425be58eeedbd38a5518b9f01e8f548d776db14ae23b9668a66c",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 394,
  "current_source_sequence_sha256": "af09f26a5420425be58eeedbd38a5518b9f01e8f548d776db14ae23b9668a66c",
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
  "requested_accession": "P0DY07",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305",
  "selected_historical_source_sequence_length": 394,
  "selected_historical_source_sequence_sha256": "af09f26a5420425be58eeedbd38a5518b9f01e8f548d776db14ae23b9668a66c",
  "selected_historical_version": {
    "accession": "P0DY07",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NEUAC_CAMJ8",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DY07\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:17.113205+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY07.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:17.113205+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY07.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Campylobacterota\",\"Epsilonproteobacteria\",\"Campylobacterales\",\"Campylobacteraceae\",\"Campylobacter\"],\"scientificName\":\"Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC 11828)\",\"taxonId\":407148}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:17.113205+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY07.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"CMP-N-acetylneuraminate synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"CMP-Neu5Ac synthase\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"2.7.7.43\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"N-acylneuraminate cytidylyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:17.113205+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY07.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"Capsule biogenesis; capsule polysaccharide biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-01T06:25:17.113205+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY07.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ghosh M.K.\",\"Raushel F.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38382015\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.3c00664\"}],\"citationType\":\"journal article\",\"firstPage\":\"688\",\"id\":\"38382015\",\"journal\":\"Biochemistry\",\"lastPage\":\"698\",\"publicationDate\":\"2024\",\"title\":\"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"81116 / NCTC 11828\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:17.113205+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY07.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   NEUAC_CAMJ8             Reviewed;         394 AA.\nAC   P0DY07;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=N-acylneuraminate cytidylyltransferase {ECO:0000305};\nDE            EC=2.7.7.43 {ECO:0000269|PubMed:38382015};\nDE   AltName: Full=CMP-N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};\nDE            Short=CMP-Neu5Ac synthase {ECO:0000303|PubMed:38382015};\nGN   Name=HS6.5 {ECO:0000303|PubMed:38382015};\nGN   OrderedLocusNames=C8J_1333 {ECO:0000312|EMBL:ABV52931.1};\nOS   Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC\nOS   11828).\nOC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;\nOC   Campylobacterales; Campylobacteraceae; Campylobacter.\nOX   NCBI_TaxID=407148;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.379520+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305",
  "url": "https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRC   STRAIN=81116 / NCTC 11828;\nRX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;\nRA   Ghosh M.K., Raushel F.M.;\nRT   \"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-\nRT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter\nRT   jejuni.\";\nRL   Biochemistry 63:688-698(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.379520+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305",
  "url": "https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Capsule biogenesis; capsule polysaccharide biosynthesis.\nCC       {ECO:0000269|PubMed:38382015}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.379520+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305",
  "url": "https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 69. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
