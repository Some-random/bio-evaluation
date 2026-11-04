# pathway_0136

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0136.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Glycan degradation

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLKSLVVLLLTSRVIAFPTLDTDQTAALHKPQATPNSQGTHGGFFYYWWSDGQSPAAYTNLDGGSYCLRWESGGNLIGGKGWSPGTDNRTIQISGTFQGVENSYLAVYGWLETPKVEYYIVEYHGVFNPAYDAQILGTVICDGSVYDISRSTRVSSGGTKILPRYWSVRRNKRTGGTVQTGCHFDAWRSTGLSAADHGFQIVATEGYFSSGFAEMTVADTSAEE

[Multiple Choices]
A. molybdopterin biosynthesis. .
B. Glycan degradation
C. LPS O-antigen biosynthesis. .
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

> The sequence-matched historical UniProt entry assigns this protein to glycan degradation, specifically xylan degradation, using a PROSITE-ProRule annotation. This supports B, though the cited support is computational rather than direct experimental evidence.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic segment consistent with secretion and a compact, enzyme-like domain consistent with a fungal xylanase. Transferable knowledge that secreted xylanases hydrolyze xylan, a plant cell-wall glycan, points to glycan degradation (B), rather than the biosynthetic pathways in A, C, or D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence and the known role of xylanases meaningfully distinguishes glycan degradation among the offered choices; recalling this exact protein's annotation is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices distinguish glycan degradation from unrelated biosynthetic pathways, and the xylanase inference supports B.


### Important caveats

- The cited pathway annotation is based on a computational PROSITE-ProRule, not direct experimental evidence in the supplied excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic segment consistent with secretion and a compact, enzyme-like domain consistent with a fungal xylanase. Transferable knowledge that secreted xylanases hydrolyze xylan, a plant cell-wall glycan, points to glycan degradation (B), rather than the biosynthetic pathways in A, C, or D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the known role of xylanases meaningfully distinguishes glycan degradation among the offered choices; recalling this exact protein's annotation is not necessary."
  },
  "case_id": "pathway_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry assigns this protein to glycan degradation, specifically xylan degradation, using a PROSITE-ProRule annotation. This supports B, though the cited support is computational rather than direct experimental evidence."
  },
  "important_caveats": [
    "The cited pathway annotation is based on a computational PROSITE-ProRule, not direct experimental evidence in the supplied excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish glycan degradation from unrelated biosynthetic pathways, and the xylanase inference supports B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt entry assigns this protein to glycan degradation, specifically xylan degradation, using a PROSITE-ProRule annotation. This supports B, though the cited support is computational rather than direct experimental evidence.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic segment consistent with secretion and a compact, enzyme-like domain consistent with a fungal xylanase. Transferable knowledge that secreted xylanases hydrolyze xylan, a plant cell-wall glycan, points to glycan degradation (B), rather than the biosynthetic pathways in A, C, or D.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence and the known role of xylanases meaningfully distinguishes glycan degradation among the offered choices; recalling this exact protein's annotation is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish glycan degradation from unrelated biosynthetic pathways, and the xylanase inference supports B."
  },
  "important_caveats": [
    "The cited pathway annotation is based on a computational PROSITE-ProRule, not direct experimental evidence in the supplied excerpts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (G2X4G1, EIX5_VERDV) annotates the pathway as 'Glycan degradation; xylan degradation' with evidence code ECO:0000255|PROSITE-ProRule:PRU01097. The protein is assigned EC 3.2.1.8 (endo-1,4-beta-xylanase), a glycoside hydrolase that hydrolyzes xylan, a polysaccharide/glycan. The pathway classification is based on a PROSITE-ProRule computational annotation of the GH10 xylanase family, which is a well-established protein family. The annotation is consistent with the protein's function as a xylanase (glycan-degrading enzyme).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits multiple hallmarks of GH10 (glycoside hydrolase family 10) xylanases, a well-characterized family: (1) an N-terminal hydrophobic signal peptide (MLKSLVVLLLTSRVIAFP) indicating a secreted enzyme, consistent with extracellular glycan degradation; (2) multiple glycine-rich loop motifs ('GGFFYYWW', 'GGNLIGGKGW', 'GGTKILPRYWSVRR', 'GGTVQTGCHFDAWRSTGL', 'GFAEMTVADTSAEE') characteristic of the (β/α)8 TIM-barrel fold of GH10 xylanases; (3) clusters of aromatic residues (W, Y, F) typical of carbohydrate-binding subsites in glycoside hydrolases; (4) small total size (~224 aa) consistent with a single-domain glycoside hydrolase. These features are transferable knowledge from the extensively studied GH10 xylanase family (e.g., Bacillus, Trichoderma, and fungal xylanases). In contrast: (A) molybdopterin biosynthesis enzymes (MoaA, MoaC, MoaD, MoeA) have entirely different architectures and cofactor-binding motifs; (C) LPS O-antigen biosynthesis involves bacterial glycosyltransferases and polymerases with distinct domain organizations; (D) aspartokinase (step 1 of threonine biosynthesis) is a ~400+ aa enzyme with specific amino-acid kinase domains. None of the alternative choices match the observed sequence features.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model familiar with glycoside hydrolase families—particularly the well-characterized GH10 xylanase family—can recognize the GG-rich loops, aromatic clusters, signal peptide, and small size as diagnostic of a secreted xylanase/glycan-degrading enzyme. This family-level pattern is learned from many other GH10 proteins and meaningfully distinguishes option B from A, C, and D without needing to know the specific database annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence features (GG-rich loops, aromatic clusters, signal peptide, small size) are strongly and specifically indicative of a glycoside hydrolase (glycan degradation). The three distractors (molybdopterin biosynthesis, LPS O-antigen biosynthesis, threonine biosynthesis) involve enzymes with fundamentally different architectures, sizes, and cofactor requirements that are inconsistent with the observed sequence. No alternative option is defensible given the sequence evidence.


### Important caveats

- The pathway annotation in UniProt is based on PROSITE-ProRule (computational/family-based, ECO:0000255), not direct experimental pathway reconstitution. However, the protein is also named 'Ethylene-inducing xylanase' with a PubMed reference (33205907) supporting its function as a xylanase.
- The reviewer-only evidence reveals the organism (Verticillium dahliae, a fungus) and specific name (EIX5), which were not provided to the evaluated model. The reasoning above relies only on sequence features and transferable GH10 family knowledge.
- The PROSITE-ProRule annotation (PRU01097) is a computational family assignment; while well-established for GH10, it is not direct experimental evidence of pathway membership in the strictest sense.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits multiple hallmarks of GH10 (glycoside hydrolase family 10) xylanases, a well-characterized family: (1) an N-terminal hydrophobic signal peptide (MLKSLVVLLLTSRVIAFP) indicating a secreted enzyme, consistent with extracellular glycan degradation; (2) multiple glycine-rich loop motifs ('GGFFYYWW', 'GGNLIGGKGW', 'GGTKILPRYWSVRR', 'GGTVQTGCHFDAWRSTGL', 'GFAEMTVADTSAEE') characteristic of the (β/α)8 TIM-barrel fold of GH10 xylanases; (3) clusters of aromatic residues (W, Y, F) typical of carbohydrate-binding subsites in glycoside hydrolases; (4) small total size (~224 aa) consistent with a single-domain glycoside hydrolase. These features are transferable knowledge from the extensively studied GH10 xylanase family (e.g., Bacillus, Trichoderma, and fungal xylanases). In contrast: (A) molybdopterin biosynthesis enzymes (MoaA, MoaC, MoaD, MoeA) have entirely different architectures and cofactor-binding motifs; (C) LPS O-antigen biosynthesis involves bacterial glycosyltransferases and polymerases with distinct domain organizations; (D) aspartokinase (step 1 of threonine biosynthesis) is a ~400+ aa enzyme with specific amino-acid kinase domains. None of the alternative choices match the observed sequence features.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model familiar with glycoside hydrolase families—particularly the well-characterized GH10 xylanase family—can recognize the GG-rich loops, aromatic clusters, signal peptide, and small size as diagnostic of a secreted xylanase/glycan-degrading enzyme. This family-level pattern is learned from many other GH10 proteins and meaningfully distinguishes option B from A, C, and D without needing to know the specific database annotation for this exact protein."
  },
  "case_id": "pathway_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (G2X4G1, EIX5_VERDV) annotates the pathway as 'Glycan degradation; xylan degradation' with evidence code ECO:0000255|PROSITE-ProRule:PRU01097. The protein is assigned EC 3.2.1.8 (endo-1,4-beta-xylanase), a glycoside hydrolase that hydrolyzes xylan, a polysaccharide/glycan. The pathway classification is based on a PROSITE-ProRule computational annotation of the GH10 xylanase family, which is a well-established protein family. The annotation is consistent with the protein's function as a xylanase (glycan-degrading enzyme)."
  },
  "important_caveats": [
    "The pathway annotation in UniProt is based on PROSITE-ProRule (computational/family-based, ECO:0000255), not direct experimental pathway reconstitution. However, the protein is also named 'Ethylene-inducing xylanase' with a PubMed reference (33205907) supporting its function as a xylanase.",
    "The reviewer-only evidence reveals the organism (Verticillium dahliae, a fungus) and specific name (EIX5), which were not provided to the evaluated model. The reasoning above relies only on sequence features and transferable GH10 family knowledge.",
    "The PROSITE-ProRule annotation (PRU01097) is a computational family assignment; while well-established for GH10, it is not direct experimental evidence of pathway membership in the strictest sense."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features (GG-rich loops, aromatic clusters, signal peptide, small size) are strongly and specifically indicative of a glycoside hydrolase (glycan degradation). The three distractors (molybdopterin biosynthesis, LPS O-antigen biosynthesis, threonine biosynthesis) involve enzymes with fundamentally different architectures, sizes, and cofactor requirements that are inconsistent with the observed sequence. No alternative option is defensible given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (G2X4G1, EIX5_VERDV) annotates the pathway as 'Glycan degradation; xylan degradation' with evidence code ECO:0000255|PROSITE-ProRule:PRU01097. The protein is assigned EC 3.2.1.8 (endo-1,4-beta-xylanase), a glycoside hydrolase that hydrolyzes xylan, a polysaccharide/glycan. The pathway classification is based on a PROSITE-ProRule computational annotation of the GH10 xylanase family, which is a well-established protein family. The annotation is consistent with the protein's function as a xylanase (glycan-degrading enzyme).",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits multiple hallmarks of GH10 (glycoside hydrolase family 10) xylanases, a well-characterized family: (1) an N-terminal hydrophobic signal peptide (MLKSLVVLLLTSRVIAFP) indicating a secreted enzyme, consistent with extracellular glycan degradation; (2) multiple glycine-rich loop motifs ('GGFFYYWW', 'GGNLIGGKGW', 'GGTKILPRYWSVRR', 'GGTVQTGCHFDAWRSTGL', 'GFAEMTVADTSAEE') characteristic of the (β/α)8 TIM-barrel fold of GH10 xylanases; (3) clusters of aromatic residues (W, Y, F) typical of carbohydrate-binding subsites in glycoside hydrolases; (4) small total size (~224 aa) consistent with a single-domain glycoside hydrolase. These features are transferable knowledge from the extensively studied GH10 xylanase family (e.g., Bacillus, Trichoderma, and fungal xylanases). In contrast: (A) molybdopterin biosynthesis enzymes (MoaA, MoaC, MoaD, MoeA) have entirely different architectures and cofactor-binding motifs; (C) LPS O-antigen biosynthesis involves bacterial glycosyltransferases and polymerases with distinct domain organizations; (D) aspartokinase (step 1 of threonine biosynthesis) is a ~400+ aa enzyme with specific amino-acid kinase domains. None of the alternative choices match the observed sequence features.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model familiar with glycoside hydrolase families—particularly the well-characterized GH10 xylanase family—can recognize the GG-rich loops, aromatic clusters, signal peptide, and small size as diagnostic of a secreted xylanase/glycan-degrading enzyme. This family-level pattern is learned from many other GH10 proteins and meaningfully distinguishes option B from A, C, and D without needing to know the specific database annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence features (GG-rich loops, aromatic clusters, signal peptide, small size) are strongly and specifically indicative of a glycoside hydrolase (glycan degradation). The three distractors (molybdopterin biosynthesis, LPS O-antigen biosynthesis, threonine biosynthesis) involve enzymes with fundamentally different architectures, sizes, and cofactor requirements that are inconsistent with the observed sequence. No alternative option is defensible given the sequence evidence."
  },
  "important_caveats": [
    "The pathway annotation in UniProt is based on PROSITE-ProRule (computational/family-based, ECO:0000255), not direct experimental pathway reconstitution. However, the protein is also named 'Ethylene-inducing xylanase' with a PubMed reference (33205907) supporting its function as a xylanase.",
    "The reviewer-only evidence reveals the organism (Verticillium dahliae, a fungus) and specific name (EIX5), which were not provided to the evaluated model. The reasoning above relies only on sequence features and transferable GH10 family knowledge.",
    "The PROSITE-ProRule annotation (PRU01097) is a computational family assignment; while well-established for GH10, it is not direct experimental evidence of pathway membership in the strictest sense."
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
  "benchmark_sequence_length": 224,
  "benchmark_sequence_sha256": "980bd9f921aa409c70d3c3af6ec2027d0fd84980947d8618f64a513744e596ed",
  "current_entry_audit": {
    "entryVersion": 58,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2011-11-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "1d3b854e7294c2d9fc95934e8e57b8df5f1a13a692ac39bb9a57962743c2e6c0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 224,
  "current_source_sequence_sha256": "980bd9f921aa409c70d3c3af6ec2027d0fd84980947d8618f64a513744e596ed",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 57,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G2X4G1",
  "selected_historical_entry_version": 57,
  "selected_historical_record_sha256": "e0c511e580167b3398281d34cf1b42f13481b77974f64acc52440d0b06a7af8b",
  "selected_historical_source_sequence_length": 224,
  "selected_historical_source_sequence_sha256": "980bd9f921aa409c70d3c3af6ec2027d0fd84980947d8618f64a513744e596ed",
  "selected_historical_version": {
    "accession": "G2X4G1",
    "database": "Swiss-Prot",
    "entryVersion": 57,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX5_VERDV",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X4G1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G2X4G1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:06.575092+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1d3b854e7294c2d9fc95934e8e57b8df5f1a13a692ac39bb9a57962743c2e6c0",
  "url": "https://rest.uniprot.org/uniprotkb/G2X4G1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X4G1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":58,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2011-11-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:06.575092+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1d3b854e7294c2d9fc95934e8e57b8df5f1a13a692ac39bb9a57962743c2e6c0",
  "url": "https://rest.uniprot.org/uniprotkb/G2X4G1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X4G1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Verticillium wilt\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Glomerellales\",\"Plectosphaerellaceae\",\"Verticillium\"],\"scientificName\":\"Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\",\"taxonId\":498257}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:06.575092+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1d3b854e7294c2d9fc95934e8e57b8df5f1a13a692ac39bb9a57962743c2e6c0",
  "url": "https://rest.uniprot.org/uniprotkb/G2X4G1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X4G1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX5\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 5\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX5\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:06.575092+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1d3b854e7294c2d9fc95934e8e57b8df5f1a13a692ac39bb9a57962743c2e6c0",
  "url": "https://rest.uniprot.org/uniprotkb/G2X4G1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X4G1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"Glycan degradation; xylan degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:06.575092+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1d3b854e7294c2d9fc95934e8e57b8df5f1a13a692ac39bb9a57962743c2e6c0",
  "url": "https://rest.uniprot.org/uniprotkb/G2X4G1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X4G1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:06.575092+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "1d3b854e7294c2d9fc95934e8e57b8df5f1a13a692ac39bb9a57962743c2e6c0",
  "url": "https://rest.uniprot.org/uniprotkb/G2X4G1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X4G1?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H1",
  "excerpt": "ID   EIX5_VERDV              Reviewed;         224 AA.\nAC   G2X4G1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 57.\nDE   RecName: Full=Ethylene-inducing xylanase 5 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX5 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX5 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX5 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_05043;\nOS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\nOS   (Verticillium wilt).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.\nOX   NCBI_TaxID=498257;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:04.705992+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e0c511e580167b3398281d34cf1b42f13481b77974f64acc52440d0b06a7af8b",
  "url": "https://rest.uniprot.org/unisave/G2X4G1?format=txt&versions=57"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X4G1?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:04.705992+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e0c511e580167b3398281d34cf1b42f13481b77974f64acc52440d0b06a7af8b",
  "url": "https://rest.uniprot.org/unisave/G2X4G1?format=txt&versions=57"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X4G1?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Glycan degradation; xylan degradation. {ECO:0000255|PROSITE-\nCC       ProRule:PRU01097}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:04.705992+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e0c511e580167b3398281d34cf1b42f13481b77974f64acc52440d0b06a7af8b",
  "url": "https://rest.uniprot.org/unisave/G2X4G1?format=txt&versions=57"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 136. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
