# GO_molecular_function_0096

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0096.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — UDP-glucose 6-dehydrogenase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | contradicted | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | contradicted | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKDLKVAVVGLGYVGLPLAVEFGKKRTVVGFDINQGRIAELRQGIDSTLEVDAAELKEASELSFTFNLQDLQKCNVFIVTVPTPIDEHKQPDLTPLVKASESIGKVLKKGDIVIYESTVYPGATEEDCVPVLEKFSGLRFNEDFFAGYSPERINPGDKEHRVSSIKKVTSGSTPEIAELVDSLYREIITAGTHKASSIKVAEAAKVIENTQRDLNIALINELAIIFNRMGIDTEAVLKAAGTKWNFMPFRPGLVGGHCIGVDPYYLTHKAQSIGYHPEIILAGRRLNDGMGAYVVSQLVKAMLKRRIHVDGARVLLMGLTFKENCPDLRNTKVVDIVRELAEYNIQVDVFDPWVSAEDAMHEYGITPVGTPSHGAYDGIILAVAHSEFKNMGAENIRKLGKAEHVLYDLKYLLDEDKSDLRL

[Multiple Choices]
A. 4 iron, 4 sulfur cluster binding
B. UDP-glucose 6-dehydrogenase activity
C. DNA-binding transcription factor binding
D. thioredoxin peroxidase activity
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

### Expected-answer support: contradicted

> The sequence-matched record reports experimentally supported UDP-N-acetylglucosamine 6-dehydrogenase activity, converting UDP-GlcNAc to UDP-GlcNAcA. That is not the UDP-glucose 6-dehydrogenase activity named in choice B; the substrates and GO terms differ.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble NAD-dependent nucleotide-sugar dehydrogenase: its length and cofactor-binding/dehydrogenase sequence features fit that enzyme class. Among the choices, B is the only nucleotide-sugar dehydrogenase; iron-sulfur binding, transcription-factor binding, and thioredoxin peroxidase activity are not comparably suggested. This supports B as the closest offered choice, not its exact substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable enzyme-family knowledge meaningfully separates B from the other alternatives. However, it does not establish the precise sugar substrate, and the expected choice names the wrong dehydrogenase activity for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other option is comparably supported by the sequence, although the precise experimentally supported activity is absent from the choices.


### Important caveats

- The reviewer evidence is sequence-matched, but the author’s exact source snapshot is unknown.
- B is the closest offered answer by enzyme class, yet it is not an exact match to the supported molecular function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble NAD-dependent nucleotide-sugar dehydrogenase: its length and cofactor-binding/dehydrogenase sequence features fit that enzyme class. Among the choices, B is the only nucleotide-sugar dehydrogenase; iron-sulfur binding, transcription-factor binding, and thioredoxin peroxidase activity are not comparably suggested. This supports B as the closest offered choice, not its exact substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable enzyme-family knowledge meaningfully separates B from the other alternatives. However, it does not establish the precise sugar substrate, and the expected choice names the wrong dehydrogenase activity for this protein."
  },
  "case_id": "GO_molecular_function_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C9",
      "GO1"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports experimentally supported UDP-N-acetylglucosamine 6-dehydrogenase activity, converting UDP-GlcNAc to UDP-GlcNAcA. That is not the UDP-glucose 6-dehydrogenase activity named in choice B; the substrates and GO terms differ."
  },
  "important_caveats": [
    "The reviewer evidence is sequence-matched, but the author’s exact source snapshot is unknown.",
    "B is the closest offered answer by enzyme class, yet it is not an exact match to the supported molecular function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other option is comparably supported by the sequence, although the precise experimentally supported activity is absent from the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0096",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports experimentally supported UDP-N-acetylglucosamine 6-dehydrogenase activity, converting UDP-GlcNAc to UDP-GlcNAcA. That is not the UDP-glucose 6-dehydrogenase activity named in choice B; the substrates and GO terms differ.",
    "evidence_ids": ["C4", "C5", "C6", "C9", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble NAD-dependent nucleotide-sugar dehydrogenase: its length and cofactor-binding/dehydrogenase sequence features fit that enzyme class. Among the choices, B is the only nucleotide-sugar dehydrogenase; iron-sulfur binding, transcription-factor binding, and thioredoxin peroxidase activity are not comparably suggested. This supports B as the closest offered choice, not its exact substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "Transferable enzyme-family knowledge meaningfully separates B from the other alternatives. However, it does not establish the precise sugar substrate, and the expected choice names the wrong dehydrogenase activity for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other option is comparably supported by the sequence, although the precise experimentally supported activity is absent from the choices."
  },
  "important_caveats": [
    "The reviewer evidence is sequence-matched, but the author’s exact source snapshot is unknown.",
    "B is the closest offered answer by enzyme class, yet it is not an exact match to the supported molecular function."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: contradicted

> The reviewer evidence (C4, C5, C6, C9, H6, H7, H10) clearly identifies this protein (Q9RHD7, WbpO) as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136, GO:0047004), catalyzing UDP-GlcNAc → UDP-GlcNAcA. The expected answer B (UDP-glucose 6-dehydrogenase activity, GO:0003979, EC 1.1.1.22) describes a different enzyme catalyzing UDP-glucose → UDP-glucuronate. These are distinct EC numbers, distinct GO terms, and distinct substrates. The protein's documented substrate specificity is for N-acetylated sugars (UDP-GlcNAc, and weakly UDP-GalNAc), not plain UDP-glucose. The expected answer is therefore contradicted by the experimental evidence (ECO:0000269/PubMed:18065759).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal sequence 'MKDLKVAVVGLGYVGLPL' contains a canonical Rossmann-fold NAD-binding motif (GxGxxG pattern: G-L-G-Y-V-G-L-P-L), identifying the protein as an NAD-dependent oxidoreductase. This immediately eliminates C (DNA-binding TF binding) and D (thioredoxin peroxidase activity, which requires a peroxiredoxin fold with a catalytic Cys and no Rossmann fold). The absence of CxxCxxC-type cysteine clusters typical of 4Fe-4S coordination eliminates A. The remaining sequence architecture (approximately 420 residues, with conserved motifs like 'GTPSHGAYD' and 'GTPVGTPSHG' reminiscent of the UDP-sugar dehydrogenase superfamily) is consistent with a UDP-sugar 6-dehydrogenase. Among the four choices, only B captures a UDP-sugar dehydrogenase activity. A knowledgeable model recognizing the Rossmann fold and UDP-sugar dehydrogenase family architecture would select B as the only viable option, even if the exact substrate (UDP-GlcNAc vs. UDP-glucose) is a finer distinction not resolvable from sequence alone among these particular choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of Rossmann-fold oxidoreductases, UDP-sugar dehydrogenase family architecture, and elimination of clearly incompatible functions (Fe-S binding, peroxidase, TF binding) provides a concrete pathway to select B. The model does not need to know this exact protein's annotation; recognizing the NAD-binding motif and the general dehydrogenase family is sufficient to eliminate A, C, and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only B is a dehydrogenase acting on a UDP-sugar. Options A, C, and D are mechanistically incompatible with the sequence features (no Fe-S motifs, no DNA-binding domain, no peroxiredoxin fold). Although B is technically the wrong substrate specificity (UDP-glucose vs. UDP-N-acetylglucosamine), it is the only choice that captures the correct enzyme class and cofactor mechanism, so no other option is defensible.


### Important caveats

- The expected answer B (UDP-glucose 6-dehydrogenase, GO:0003979/EC 1.1.1.22) is scientifically incorrect for this protein. The correct annotation is UDP-N-acetylglucosamine 6-dehydrogenase (GO:0047004/EC 1.1.1.136). The author appears to have conflated two related but distinct UDP-sugar 6-dehydrogenase activities.
- Despite the key being technically wrong, B remains the best answer among the four choices because it is the only option describing a NAD-dependent UDP-sugar dehydrogenase. The question is answerable but the key contains a substrate-specificity error.
- The GO term GO:0047004 (UDP-N-acetylglucosamine 6-dehydrogenase activity) was not offered as a choice, which forces the model to select the closest but incorrect option.
- The protein's activity on UDP-GalNAc (low efficiency) is documented but no activity on plain UDP-glucose is reported, confirming the substrate specificity distinction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal sequence 'MKDLKVAVVGLGYVGLPL' contains a canonical Rossmann-fold NAD-binding motif (GxGxxG pattern: G-L-G-Y-V-G-L-P-L), identifying the protein as an NAD-dependent oxidoreductase. This immediately eliminates C (DNA-binding TF binding) and D (thioredoxin peroxidase activity, which requires a peroxiredoxin fold with a catalytic Cys and no Rossmann fold). The absence of CxxCxxC-type cysteine clusters typical of 4Fe-4S coordination eliminates A. The remaining sequence architecture (approximately 420 residues, with conserved motifs like 'GTPSHGAYD' and 'GTPVGTPSHG' reminiscent of the UDP-sugar dehydrogenase superfamily) is consistent with a UDP-sugar 6-dehydrogenase. Among the four choices, only B captures a UDP-sugar dehydrogenase activity. A knowledgeable model recognizing the Rossmann fold and UDP-sugar dehydrogenase family architecture would select B as the only viable option, even if the exact substrate (UDP-GlcNAc vs. UDP-glucose) is a finer distinction not resolvable from sequence alone among these particular choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of Rossmann-fold oxidoreductases, UDP-sugar dehydrogenase family architecture, and elimination of clearly incompatible functions (Fe-S binding, peroxidase, TF binding) provides a concrete pathway to select B. The model does not need to know this exact protein's annotation; recognizing the NAD-binding motif and the general dehydrogenase family is sufficient to eliminate A, C, and D."
  },
  "case_id": "GO_molecular_function_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C9",
      "GO1"
    ],
    "judgment": "contradicted",
    "reason": "The reviewer evidence (C4, C5, C6, C9, H6, H7, H10) clearly identifies this protein (Q9RHD7, WbpO) as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136, GO:0047004), catalyzing UDP-GlcNAc → UDP-GlcNAcA. The expected answer B (UDP-glucose 6-dehydrogenase activity, GO:0003979, EC 1.1.1.22) describes a different enzyme catalyzing UDP-glucose → UDP-glucuronate. These are distinct EC numbers, distinct GO terms, and distinct substrates. The protein's documented substrate specificity is for N-acetylated sugars (UDP-GlcNAc, and weakly UDP-GalNAc), not plain UDP-glucose. The expected answer is therefore contradicted by the experimental evidence (ECO:0000269/PubMed:18065759)."
  },
  "important_caveats": [
    "The expected answer B (UDP-glucose 6-dehydrogenase, GO:0003979/EC 1.1.1.22) is scientifically incorrect for this protein. The correct annotation is UDP-N-acetylglucosamine 6-dehydrogenase (GO:0047004/EC 1.1.1.136). The author appears to have conflated two related but distinct UDP-sugar 6-dehydrogenase activities.",
    "Despite the key being technically wrong, B remains the best answer among the four choices because it is the only option describing a NAD-dependent UDP-sugar dehydrogenase. The question is answerable but the key contains a substrate-specificity error.",
    "The GO term GO:0047004 (UDP-N-acetylglucosamine 6-dehydrogenase activity) was not offered as a choice, which forces the model to select the closest but incorrect option.",
    "The protein's activity on UDP-GalNAc (low efficiency) is documented but no activity on plain UDP-glucose is reported, confirming the substrate specificity distinction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only B is a dehydrogenase acting on a UDP-sugar. Options A, C, and D are mechanistically incompatible with the sequence features (no Fe-S motifs, no DNA-binding domain, no peroxiredoxin fold). Although B is technically the wrong substrate specificity (UDP-glucose vs. UDP-N-acetylglucosamine), it is the only choice that captures the correct enzyme class and cofactor mechanism, so no other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0096",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The reviewer evidence (C4, C5, C6, C9, H6, H7, H10) clearly identifies this protein (Q9RHD7, WbpO) as UDP-N-acetyl-D-glucosamine 6-dehydrogenase (EC 1.1.1.136, GO:0047004), catalyzing UDP-GlcNAc → UDP-GlcNAcA. The expected answer B (UDP-glucose 6-dehydrogenase activity, GO:0003979, EC 1.1.1.22) describes a different enzyme catalyzing UDP-glucose → UDP-glucuronate. These are distinct EC numbers, distinct GO terms, and distinct substrates. The protein's documented substrate specificity is for N-acetylated sugars (UDP-GlcNAc, and weakly UDP-GalNAc), not plain UDP-glucose. The expected answer is therefore contradicted by the experimental evidence (ECO:0000269/PubMed:18065759).",
    "evidence_ids": ["C4", "C5", "C6", "C9", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal sequence 'MKDLKVAVVGLGYVGLPL' contains a canonical Rossmann-fold NAD-binding motif (GxGxxG pattern: G-L-G-Y-V-G-L-P-L), identifying the protein as an NAD-dependent oxidoreductase. This immediately eliminates C (DNA-binding TF binding) and D (thioredoxin peroxidase activity, which requires a peroxiredoxin fold with a catalytic Cys and no Rossmann fold). The absence of CxxCxxC-type cysteine clusters typical of 4Fe-4S coordination eliminates A. The remaining sequence architecture (approximately 420 residues, with conserved motifs like 'GTPSHGAYD' and 'GTPVGTPSHG' reminiscent of the UDP-sugar dehydrogenase superfamily) is consistent with a UDP-sugar 6-dehydrogenase. Among the four choices, only B captures a UDP-sugar dehydrogenase activity. A knowledgeable model recognizing the Rossmann fold and UDP-sugar dehydrogenase family architecture would select B as the only viable option, even if the exact substrate (UDP-GlcNAc vs. UDP-glucose) is a finer distinction not resolvable from sequence alone among these particular choices.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of Rossmann-fold oxidoreductases, UDP-sugar dehydrogenase family architecture, and elimination of clearly incompatible functions (Fe-S binding, peroxidase, TF binding) provides a concrete pathway to select B. The model does not need to know this exact protein's annotation; recognizing the NAD-binding motif and the general dehydrogenase family is sufficient to eliminate A, C, and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only B is a dehydrogenase acting on a UDP-sugar. Options A, C, and D are mechanistically incompatible with the sequence features (no Fe-S motifs, no DNA-binding domain, no peroxiredoxin fold). Although B is technically the wrong substrate specificity (UDP-glucose vs. UDP-N-acetylglucosamine), it is the only choice that captures the correct enzyme class and cofactor mechanism, so no other option is defensible."
  },
  "important_caveats": [
    "The expected answer B (UDP-glucose 6-dehydrogenase, GO:0003979/EC 1.1.1.22) is scientifically incorrect for this protein. The correct annotation is UDP-N-acetylglucosamine 6-dehydrogenase (GO:0047004/EC 1.1.1.136). The author appears to have conflated two related but distinct UDP-sugar 6-dehydrogenase activities.",
    "Despite the key being technically wrong, B remains the best answer among the four choices because it is the only option describing a NAD-dependent UDP-sugar dehydrogenase. The question is answerable but the key contains a substrate-specificity error.",
    "The GO term GO:0047004 (UDP-N-acetylglucosamine 6-dehydrogenase activity) was not offered as a choice, which forces the model to select the closest but incorrect option.",
    "The protein's activity on UDP-GalNAc (low efficiency) is documented but no activity on plain UDP-glucose is reported, confirming the substrate specificity distinction."
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
  "benchmark_sequence_length": 422,
  "benchmark_sequence_sha256": "2ef2c7dd997f713d5338089d92650976216ea47165f21da1002f866a128c2ee4",
  "current_entry_audit": {
    "entryVersion": 113,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 422,
  "current_source_sequence_sha256": "2ef2c7dd997f713d5338089d92650976216ea47165f21da1002f866a128c2ee4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 111,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9RHD7",
  "selected_historical_entry_version": 111,
  "selected_historical_record_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "selected_historical_source_sequence_length": 422,
  "selected_historical_source_sequence_sha256": "2ef2c7dd997f713d5338089d92650976216ea47165f21da1002f866a128c2ee4",
  "selected_historical_version": {
    "accession": "Q9RHD7",
    "database": "Swiss-Prot",
    "entryVersion": 111,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "WBPO_PSEAI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9RHD7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":113,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas aeruginosa\",\"taxonId\":287}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.136\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-D-glucosamine 6-dehydrogenase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-GlcNAc 6-dehydrogenase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10627048\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10931835\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"value\":\"Dehydrogenase required for the biosynthesis of the B-band O antigen of serotype O6 lipopolysaccharide (PubMed:10627048). Is also required for flagellin glycosylation (PubMed:18065759). Catalyzes the conversion of UDP-N-acetylglucosamine (UDP-GlcNAc) to UDP-N-acetylglucosaminuronic acid (UDP-GlcNAcA) (PubMed:18065759). Can also catalyze the conversion of UDP-N-acetyl-galactosamine (UDP-GalNAc) to UDP-N-acetylgalactosaminuronic acid (UDP-GalNAcA), with low efficiency (PubMed:10931835, PubMed:18065759). Can use NAD(+) or NADP(+), with a preference for NAD(+) (PubMed:18065759)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:13326\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.136\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"name\":\"UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:13325\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57705\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:65040\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0051287\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:NAD binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0016628\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"id\":\"GO:0047004\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:UDP-N-acetylglucosamine 6-dehydrogenase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Belanger M.\",\"Burrows L.L.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10627048\"},{\"database\":\"DOI\",\"id\":\"10.1099/00221287-145-12-3505\"}],\"citationType\":\"journal article\",\"firstPage\":\"3505\",\"id\":\"10627048\",\"journal\":\"Microbiology\",\"lastPage\":\"3521\",\"publicationDate\":\"1999\",\"title\":\"Functional analysis of genes responsible for the synthesis of the B-band O antigen of Pseudomonas aeruginosa serotype O6 lipopolysaccharide.\",\"volume\":\"145\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAF23997.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 33354 / Serotype O6\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhao X.\",\"Creuzenet C.\",\"Belanger M.\",\"Egbosimba E.\",\"Li J.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10931835\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m004191200\"}],\"citationType\":\"journal article\",\"firstPage\":\"33252\",\"id\":\"10931835\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"33259\",\"publicationDate\":\"2000\",\"title\":\"WbpO, a UDP-N-acetyl-D-galactosamine dehydrogenase from Pseudomonas aeruginosa serotype O6.\",\"volume\":\"275\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Serotype O6\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9RHD7.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Miller W.L.\",\"Matewish M.J.\",\"McNally D.J.\",\"Ishiyama N.\",\"Anderson E.M.\",\"Brewer D.\",\"Brisson J.R.\",\"Berghuis A.M.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18065759\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m708894200\"}],\"citationType\":\"journal article\",\"firstPage\":\"3507\",\"id\":\"18065759\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"3518\",\"publicationDate\":\"2008\",\"title\":\"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-antigen biosynthesis enzyme WbpO.\",\"volume\":\"283\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"PAK / Serotype O6\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:25:27.130209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9908d3a1c42951cf34f5af4acef817be24931c868b8047c883d1accce98092cd",
  "url": "https://rest.uniprot.org/uniprotkb/Q9RHD7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H1",
  "excerpt": "ID   WBPO_PSEAI              Reviewed;         422 AA.\nAC   Q9RHD7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 111.\nDE   RecName: Full=UDP-N-acetyl-D-glucosamine 6-dehydrogenase {ECO:0000305};\nDE            Short=UDP-GlcNAc 6-dehydrogenase {ECO:0000305};\nDE            EC=1.1.1.136 {ECO:0000269|PubMed:18065759};\nGN   Name=wbpO {ECO:0000303|PubMed:10627048, ECO:0000303|PubMed:12057956};\nGN   ORFNames=CAZ10_03215 {ECO:0000312|EMBL:OTI64803.1};\nOS   Pseudomonas aeruginosa.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=287;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAF23997.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, PATHWAY, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 33354 / Serotype O6;\nRX   PubMed=10627048; DOI=10.1099/00221287-145-12-3505;\nRA   Belanger M., Burrows L.L., Lam J.S.;\nRT   \"Functional analysis of genes responsible for the synthesis of the B-band O\nRT   antigen of Pseudomonas aeruginosa serotype O6 lipopolysaccharide.\";\nRL   Microbiology 145:3505-3521(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:AAM27816.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=Serotype O6;\nRX   PubMed=12057956; DOI=10.1128/jb.184.13.3614-3622.2002;\nRA   Raymond C.K., Sims E.H., Kas A., Spencer D.H., Kutyavin T.V., Ivey R.G.,\nRA   Zhou Y., Kaul R., Clendenning J.B., Olson M.V.;\nRT   \"Genetic variation at the O-antigen biosynthetic locus in Pseudomonas\nRT   aeruginosa.\";\nRL   J. Bacteriol. 184:3614-3622(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H4",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=Serotype O6;\nRX   PubMed=10931835; DOI=10.1074/jbc.m004191200;\nRA   Zhao X., Creuzenet C., Belanger M., Egbosimba E., Li J., Lam J.S.;\nRT   \"WbpO, a UDP-N-acetyl-D-galactosamine dehydrogenase from Pseudomonas\nRT   aeruginosa serotype O6.\";\nRL   J. Biol. Chem. 275:33252-33259(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H5",
  "excerpt": "RN   [5]\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=PAK / Serotype O6;\nRX   PubMed=18065759; DOI=10.1074/jbc.m708894200;\nRA   Miller W.L., Matewish M.J., McNally D.J., Ishiyama N., Anderson E.M.,\nRA   Brewer D., Brisson J.R., Berghuis A.M., Lam J.S.;\nRT   \"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-\nRT   antigen biosynthesis enzyme WbpO.\";\nRL   J. Biol. Chem. 283:3507-3518(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H6",
  "excerpt": "CC   -!- FUNCTION: Dehydrogenase required for the biosynthesis of the B-band O\nCC       antigen of serotype O6 lipopolysaccharide (PubMed:10627048). Is also\nCC       required for flagellin glycosylation (PubMed:18065759). Catalyzes the\nCC       conversion of UDP-N-acetylglucosamine (UDP-GlcNAc) to UDP-N-\nCC       acetylglucosaminuronic acid (UDP-GlcNAcA) (PubMed:18065759). Can also\nCC       catalyze the conversion of UDP-N-acetyl-galactosamine (UDP-GalNAc) to\nCC       UDP-N-acetylgalactosaminuronic acid (UDP-GalNAcA), with low efficiency\nCC       (PubMed:10931835, PubMed:18065759). Can use NAD(+) or NADP(+), with a\nCC       preference for NAD(+) (PubMed:18065759). {ECO:0000269|PubMed:10627048,\nCC       ECO:0000269|PubMed:10931835, ECO:0000269|PubMed:18065759}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-N-acetyl-alpha-D-glucosamine + 2 NAD(+) + H2O = UDP-2-\nCC         acetamido-2-deoxy-alpha-D-glucuronate + 2 NADH + 3 H(+);\nCC         Xref=Rhea:RHEA:13325, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57540, ChEBI:CHEBI:57705, ChEBI:CHEBI:57945,\nCC         ChEBI:CHEBI:65040; EC=1.1.1.136;\nCC         Evidence={ECO:0000269|PubMed:18065759};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13326;\nCC         Evidence={ECO:0000269|PubMed:18065759};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:0051287; F:NAD binding; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 144-144",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0016628; F:oxidoreductase activity, acting on the CH-CH group of donors, NAD or NADP as acceptor; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 145-145",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111)

```json
{
  "entry_version": 111,
  "evidence_id": "H10",
  "excerpt": "DR   GO; GO:0047004; F:UDP-N-acetylglucosamine 6-dehydrogenase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.339116+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 146-146",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f7af1f7da3cb8c76a5dd5a6f0015938a765ca8f2ee11a77d973637afedcc3462",
  "url": "https://rest.uniprot.org/unisave/Q9RHD7?format=txt&versions=111"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0003979\nname: UDP-glucose 6-dehydrogenase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: H2O + 2 NAD+ + UDP-alpha-D-glucose = 3 H+ + 2 NADH + UDP-alpha-D-glucuronate.\" [EC:1.1.1.22, RHEA:23596]\nxref: EC:1.1.1.22\nxref: KEGG_REACTION:R00286\nxref: MetaCyc:UGD-RXN\nxref: Reactome:R-HSA-173597 \"UDP-glucose is oxidised to UDP-glucuronate\"\nxref: RHEA:23596\nis_a: GO:0016616 ! oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor\nproperty_value: skos:exactMatch EC:1.1.1.22\nproperty_value: skos:exactMatch RHEA:23596\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003979",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 32563-32576",
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
  "excerpt": "[Term]\nid: GO:0008379\nname: thioredoxin peroxidase activity\nnamespace: molecular_function\nalt_id: GO:0009031\ndef: \"Catalysis of the reaction: [thioredoxin]-dithiol + H2O2 = [thioredoxin]-disulfide + H2O.\" [RHEA:63528]\nsynonym: \"thiol peroxidase activity\" EXACT []\nsynonym: \"TPx activity\" EXACT []\nsynonym: \"TrxPx activity\" EXACT []\nxref: MetaCyc:RXN0-267\nxref: Reactome:R-HSA-3322995 \"PRDX3,5 catalyze TXN2 reduced + H2O2 => TXN2 oxidized + 2H2O\"\nxref: Reactome:R-HSA-3341343 \"PRDX1,2,5 catalyze TXN reduced + H2O2 => TXN oxidized + 2H2O\"\nxref: Reactome:R-HSA-3697882 \"PRDX5 reduces peroxynitrite to nitrite using TXN\"\nxref: Reactome:R-HSA-3697894 \"PRDX5 reduces peroxynitrite to nitrite using TXN2\"\nxref: RHEA:63528\nis_a: GO:0140824 ! thioredoxin-dependent peroxiredoxin activity\nproperty_value: skos:exactMatch RHEA:63528\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008379",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 82543-82560",
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
  "excerpt": "[Term]\nid: GO:0051539\nname: 4 iron, 4 sulfur cluster binding\nnamespace: molecular_function\ndef: \"Binding to a 4 iron, 4 sulfur (4Fe-4S) cluster; this cluster consists of four iron atoms, with the inorganic sulfur atoms found between the irons and acting as bridging ligands.\" [GOC:ai, PMID:15952888, Wikipedia:Iron-sulfur_cluster]\nsynonym: \"4 Fe 4 S cluster binding\" EXACT []\nsynonym: \"4 iron, 4 sulphur cluster binding\" EXACT []\nsynonym: \"4Fe-4S cluster binding\" EXACT []\nsynonym: \"iron-sulfur cluster 4Fe-4S binding\" EXACT []\nsynonym: \"iron-sulphur cluster 4Fe-4S binding\" EXACT []\nsynonym: \"tetrairon tetrasulfide cluster binding\" EXACT []\nsynonym: \"tetrairon tetrasulphide cluster binding\" EXACT []\nis_a: GO:0051536 ! iron-sulfur cluster binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051539",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 327906-327919",
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
  "excerpt": "[Term]\nid: GO:0140297\nname: DNA-binding transcription factor binding\nnamespace: molecular_function\nalt_id: GO:0001107\nalt_id: GO:0033613\nalt_id: GO:0070491\ndef: \"Binding to a DNA-binding transcription factor, a protein that interacts with a specific DNA sequence (sometimes referred to as a motif) within the regulatory region of a gene to modulate transcription.\" [GOC:txnOH-2018]\nsynonym: \"activating transcription factor binding\" RELATED []\nsynonym: \"repressing transcription factor binding\" RELATED []\nsynonym: \"transcription activator binding\" RELATED []\nis_a: GO:0008134 ! transcription factor binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0140297",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 439110-439122",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 96. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
