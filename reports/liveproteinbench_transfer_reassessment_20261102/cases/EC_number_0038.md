# EC_number_0038

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0038.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 2.4.1.259

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAPPAARARYIANKADNQILSKKPPKRPGLNGNNKTKEATPAGKKKDKDAKKRNQPTSGGQEKGLPNPIMPSVQTAFKTFVSARLCSAIWAYIADCDETFNYWEPLHYIINGHGLQTWEYSPQFGLRSYTYLLLQGVPGYFYQKLFNPSPILIFYMVRCMLGFGCAVMERYMYKSICQEFGIHIGRLWLIFQLFSVGMFVSSTALLPSSFSMYFGCAALAAWWQQNYCFAIFLTAISALLGWPFAALIGIPLVLEMLLRQRDWKTFVQWTLISGATVAIPMIAIDTSYFGKLTFAPLNIVWYNVFTSHGPNIFGTEPLSYYIINGFLNFNIIWLLALQLPIMLVIDYLIVPAKSKSTLNFPHYISLAPLYLWLLVFFAQPHKEERFLFPIYPLISLCGAITVDVYQRIFFRMKSVVFKIKAGVHYLDHSMFIAILVMVTSTLLGLSRVFALYRNYHAPMDLMLELNQFKATPQYDPDVIYNVCIGKDWHRYPGSFFFPAKNFRLRFLKSEFRGMLPAYYDEGQNATKVVQPYFNDLNQENEHMYFDYDRCDFLVDFDEGKYTALEPNYSKRSKDWSVMKSLPFLIPEKSHKVLRAFYVPFLTDNHIQYGDFNLLKRKTKRNGR

[Multiple Choices]
A. 2.4.1.392
B. 4.2.1.70
C. 2.4.1.259
D. 2.3.1.319
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence-matched historical UniProt record assigns EC 2.4.1.259, supporting choice C. This is a transferred annotation based on similarity, not direct experimental evidence in the supplied excerpts. The record also assigns EC 2.4.1.261, which is not among the choices.

Citations as saved: [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, highly hydrophobic sequence is consistent with a multipass membrane enzyme involved in lipid-linked oligosaccharide processing. Recognition of the conserved Alg9-like mannosyltransferase family from sequence similarity provides a transferable basis for favoring an alpha-1,2-mannosyltransferase option such as C over the lyase and acyltransferase choices, and distinguishes it from an unrelated transferase option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence can meaningfully distinguish choice C among the offered alternatives without relying on the exact protein's database record. The sequence's membrane topology alone would not establish the detailed reaction, so the inference depends on recognizing conserved family similarity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only C among the listed choices is supported by the sequence-matched annotation. The protein is additionally assigned EC 2.4.1.261, but that number is not offered.


### Important caveats

- The cited EC assignments are transferred by similarity rather than shown here as direct experimental findings for this protein.
- The question asks for a complete EC number in the singular, while the record assigns two EC numbers; only one is included in the choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, highly hydrophobic sequence is consistent with a multipass membrane enzyme involved in lipid-linked oligosaccharide processing. Recognition of the conserved Alg9-like mannosyltransferase family from sequence similarity provides a transferable basis for favoring an alpha-1,2-mannosyltransferase option such as C over the lyase and acyltransferase choices, and distinguishes it from an unrelated transferase option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can meaningfully distinguish choice C among the offered alternatives without relying on the exact protein's database record. The sequence's membrane topology alone would not establish the detailed reaction, so the inference depends on recognizing conserved family similarity."
  },
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns EC 2.4.1.259, supporting choice C. This is a transferred annotation based on similarity, not direct experimental evidence in the supplied excerpts. The record also assigns EC 2.4.1.261, which is not among the choices."
  },
  "important_caveats": [
    "The cited EC assignments are transferred by similarity rather than shown here as direct experimental findings for this protein.",
    "The question asks for a complete EC number in the singular, while the record assigns two EC numbers; only one is included in the choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the listed choices is supported by the sequence-matched annotation. The protein is additionally assigned EC 2.4.1.261, but that number is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record assigns EC 2.4.1.259, supporting choice C. This is a transferred annotation based on similarity, not direct experimental evidence in the supplied excerpts. The record also assigns EC 2.4.1.261, which is not among the choices.",
    "evidence_ids": ["H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, highly hydrophobic sequence is consistent with a multipass membrane enzyme involved in lipid-linked oligosaccharide processing. Recognition of the conserved Alg9-like mannosyltransferase family from sequence similarity provides a transferable basis for favoring an alpha-1,2-mannosyltransferase option such as C over the lyase and acyltransferase choices, and distinguishes it from an unrelated transferase option.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can meaningfully distinguish choice C among the offered alternatives without relying on the exact protein's database record. The sequence's membrane topology alone would not establish the detailed reaction, so the inference depends on recognizing conserved family similarity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only C among the listed choices is supported by the sequence-matched annotation. The protein is additionally assigned EC 2.4.1.261, but that number is not offered."
  },
  "important_caveats": [
    "The cited EC assignments are transferred by similarity rather than shown here as direct experimental findings for this protein.",
    "The question asks for a complete EC number in the singular, while the record assigns two EC numbers; only one is included in the choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9VBV8 (ALG9_DROME) lists EC=2.4.1.259 as the primary EC number for Alpha-1,2-mannosyltransferase Alg9, with the catalytic activity describing the transfer of an alpha-1,2-linked mannose from dolichyl-P-Man to the Man6GlcNAc2-PP-dolichol acceptor (Rhea:RHEA:29531). The evidence code is ECO:0000250 (inferred by similarity to human Alg9 Q9H6U8), which is computational transfer rather than direct experimental measurement, but the annotation is consistent and the EC number is the standard assignment for Alg9. The entry also carries EC=2.4.1.261 as a secondary activity, but that EC is not among the offered choices, so it does not contradict choice C.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 623-aa sequence contains approximately 10+ hydrophobic segments consistent with a multi-pass transmembrane ER-resident glycosyltransferase, the hallmark architecture of Alg9 (alpha-1,2-mannosyltransferase) in the N-glycan biosynthesis pathway. Alg9 is one of the most well-characterized enzymes in the dolichol-linked oligosaccharide assembly pathway across yeast, human, Drosophila, and other model organisms. A knowledgeable model can recognize the multi-TM topology, overall length (~600 aa), and conserved sequence motifs as characteristic of the Alg9 family. Knowing that Alg9 catalyzes the alpha-1,2-mannosyltransferase step (EC 2.4.1.259) is standard N-glycan biosynthesis pathway knowledge, analogous to knowing hexokinase is EC 2.7.1.1. Distractors B (EC 4.2.1.70, a lyase/hydratase) and D (EC 2.3.1.319, an acyltransferase) belong to entirely different EC classes and are incompatible with a multi-pass membrane glycosyltransferase architecture. Between A (EC 2.4.1.392, a different glycosyltransferase) and C (EC 2.4.1.259, Alg9), family-level recognition of the Alg9 signature narrows the answer to C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multi-pass TM architecture and overall sequence features are consistent with the well-known Alg9 family in N-glycan biosynthesis. Recognizing this family from sequence topology and knowing its canonical EC number (2.4.1.259) is transferable knowledge from studying N-glycan assembly in multiple organisms. The EC-class-level distractors (B, D) are eliminable by basic structural reasoning, and the within-class distinction (A vs C) follows from family identification.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The UniProt entry also lists EC 2.4.1.261 as a secondary activity, but this EC number is not among the offered choices, so it does not create ambiguity. Among the four options, B and D are in wrong EC classes for a multi-pass membrane glycosyltransferase. A (2.4.1.392) is a different glycosyltransferase that does not match the Alg9 family signature. C (2.4.1.259) is the primary and most specific EC assignment for Alg9.


### Important caveats

- The UniProt EC annotation for this Drosophila Alg9 is based on similarity (ECO:0000250) to human Alg9 (Q9H6U8), not on direct experimental characterization of the fly protein.
- The entry also carries EC 2.4.1.261 as a secondary activity; if that EC had been offered as an alternative, the question would be genuinely ambiguous.
- Distinguishing EC 2.4.1.259 from EC 2.4.1.392 at the sequence level requires family-level recognition of Alg9; a model without strong N-glycan biosynthesis knowledge might struggle with this specific pair of glycosyltransferase EC numbers.
- The sequence itself does not contain an explicit signal peptide annotation visible in the raw sequence, though the N-terminal region is consistent with ER targeting.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 623-aa sequence contains approximately 10+ hydrophobic segments consistent with a multi-pass transmembrane ER-resident glycosyltransferase, the hallmark architecture of Alg9 (alpha-1,2-mannosyltransferase) in the N-glycan biosynthesis pathway. Alg9 is one of the most well-characterized enzymes in the dolichol-linked oligosaccharide assembly pathway across yeast, human, Drosophila, and other model organisms. A knowledgeable model can recognize the multi-TM topology, overall length (~600 aa), and conserved sequence motifs as characteristic of the Alg9 family. Knowing that Alg9 catalyzes the alpha-1,2-mannosyltransferase step (EC 2.4.1.259) is standard N-glycan biosynthesis pathway knowledge, analogous to knowing hexokinase is EC 2.7.1.1. Distractors B (EC 4.2.1.70, a lyase/hydratase) and D (EC 2.3.1.319, an acyltransferase) belong to entirely different EC classes and are incompatible with a multi-pass membrane glycosyltransferase architecture. Between A (EC 2.4.1.392, a different glycosyltransferase) and C (EC 2.4.1.259, Alg9), family-level recognition of the Alg9 signature narrows the answer to C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass TM architecture and overall sequence features are consistent with the well-known Alg9 family in N-glycan biosynthesis. Recognizing this family from sequence topology and knowing its canonical EC number (2.4.1.259) is transferable knowledge from studying N-glycan assembly in multiple organisms. The EC-class-level distractors (B, D) are eliminable by basic structural reasoning, and the within-class distinction (A vs C) follows from family identification."
  },
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9VBV8 (ALG9_DROME) lists EC=2.4.1.259 as the primary EC number for Alpha-1,2-mannosyltransferase Alg9, with the catalytic activity describing the transfer of an alpha-1,2-linked mannose from dolichyl-P-Man to the Man6GlcNAc2-PP-dolichol acceptor (Rhea:RHEA:29531). The evidence code is ECO:0000250 (inferred by similarity to human Alg9 Q9H6U8), which is computational transfer rather than direct experimental measurement, but the annotation is consistent and the EC number is the standard assignment for Alg9. The entry also carries EC=2.4.1.261 as a secondary activity, but that EC is not among the offered choices, so it does not contradict choice C."
  },
  "important_caveats": [
    "The UniProt EC annotation for this Drosophila Alg9 is based on similarity (ECO:0000250) to human Alg9 (Q9H6U8), not on direct experimental characterization of the fly protein.",
    "The entry also carries EC 2.4.1.261 as a secondary activity; if that EC had been offered as an alternative, the question would be genuinely ambiguous.",
    "Distinguishing EC 2.4.1.259 from EC 2.4.1.392 at the sequence level requires family-level recognition of Alg9; a model without strong N-glycan biosynthesis knowledge might struggle with this specific pair of glycosyltransferase EC numbers.",
    "The sequence itself does not contain an explicit signal peptide annotation visible in the raw sequence, though the N-terminal region is consistent with ER targeting."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry also lists EC 2.4.1.261 as a secondary activity, but this EC number is not among the offered choices, so it does not create ambiguity. Among the four options, B and D are in wrong EC classes for a multi-pass membrane glycosyltransferase. A (2.4.1.392) is a different glycosyltransferase that does not match the Alg9 family signature. C (2.4.1.259) is the primary and most specific EC assignment for Alg9."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0038",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9VBV8 (ALG9_DROME) lists EC=2.4.1.259 as the primary EC number for Alpha-1,2-mannosyltransferase Alg9, with the catalytic activity describing the transfer of an alpha-1,2-linked mannose from dolichyl-P-Man to the Man6GlcNAc2-PP-dolichol acceptor (Rhea:RHEA:29531). The evidence code is ECO:0000250 (inferred by similarity to human Alg9 Q9H6U8), which is computational transfer rather than direct experimental measurement, but the annotation is consistent and the EC number is the standard assignment for Alg9. The entry also carries EC=2.4.1.261 as a secondary activity, but that EC is not among the offered choices, so it does not contradict choice C.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 623-aa sequence contains approximately 10+ hydrophobic segments consistent with a multi-pass transmembrane ER-resident glycosyltransferase, the hallmark architecture of Alg9 (alpha-1,2-mannosyltransferase) in the N-glycan biosynthesis pathway. Alg9 is one of the most well-characterized enzymes in the dolichol-linked oligosaccharide assembly pathway across yeast, human, Drosophila, and other model organisms. A knowledgeable model can recognize the multi-TM topology, overall length (~600 aa), and conserved sequence motifs as characteristic of the Alg9 family. Knowing that Alg9 catalyzes the alpha-1,2-mannosyltransferase step (EC 2.4.1.259) is standard N-glycan biosynthesis pathway knowledge, analogous to knowing hexokinase is EC 2.7.1.1. Distractors B (EC 4.2.1.70, a lyase/hydratase) and D (EC 2.3.1.319, an acyltransferase) belong to entirely different EC classes and are incompatible with a multi-pass membrane glycosyltransferase architecture. Between A (EC 2.4.1.392, a different glycosyltransferase) and C (EC 2.4.1.259, Alg9), family-level recognition of the Alg9 signature narrows the answer to C.",
    "missing_item_specific_fact": "",
    "reason": "The multi-pass TM architecture and overall sequence features are consistent with the well-known Alg9 family in N-glycan biosynthesis. Recognizing this family from sequence topology and knowing its canonical EC number (2.4.1.259) is transferable knowledge from studying N-glycan assembly in multiple organisms. The EC-class-level distractors (B, D) are eliminable by basic structural reasoning, and the within-class distinction (A vs C) follows from family identification."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The UniProt entry also lists EC 2.4.1.261 as a secondary activity, but this EC number is not among the offered choices, so it does not create ambiguity. Among the four options, B and D are in wrong EC classes for a multi-pass membrane glycosyltransferase. A (2.4.1.392) is a different glycosyltransferase that does not match the Alg9 family signature. C (2.4.1.259) is the primary and most specific EC assignment for Alg9."
  },
  "important_caveats": [
    "The UniProt EC annotation for this Drosophila Alg9 is based on similarity (ECO:0000250) to human Alg9 (Q9H6U8), not on direct experimental characterization of the fly protein.",
    "The entry also carries EC 2.4.1.261 as a secondary activity; if that EC had been offered as an alternative, the question would be genuinely ambiguous.",
    "Distinguishing EC 2.4.1.259 from EC 2.4.1.392 at the sequence level requires family-level recognition of Alg9; a model without strong N-glycan biosynthesis knowledge might struggle with this specific pair of glycosyltransferase EC numbers.",
    "The sequence itself does not contain an explicit signal peptide annotation visible in the raw sequence, though the N-terminal region is consistent with ER targeting."
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
  "benchmark_sequence_length": 623,
  "benchmark_sequence_sha256": "f408e9420c1052e4e0d32438a8e2c7e6058387a35e5959dc8c2bf30c8f4f8cb5",
  "current_entry_audit": {
    "entryVersion": 176,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 623,
  "current_source_sequence_sha256": "f408e9420c1052e4e0d32438a8e2c7e6058387a35e5959dc8c2bf30c8f4f8cb5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 174,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VBV8",
  "selected_historical_entry_version": 174,
  "selected_historical_record_sha256": "32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8",
  "selected_historical_source_sequence_length": 623,
  "selected_historical_source_sequence_sha256": "f408e9420c1052e4e0d32438a8e2c7e6058387a35e5959dc8c2bf30c8f4f8cb5",
  "selected_historical_version": {
    "accession": "Q9VBV8",
    "database": "Swiss-Prot",
    "entryVersion": 174,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ALG9_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VBV8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:29.193985+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VBV8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":176,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:29.193985+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VBV8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:29.193985+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VBV8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Dolichyl-P-Man:Man6GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Dolichyl-P-Man:Man8GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9H6U8\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.1.259\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9H6U8\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.1.261\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0039293\",\"source\":\"FlyBase\"}],\"value\":\"Alpha-1,2-mannosyltransferase Alg9\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:29.193985+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VBV8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.4.1.259\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9H6U8\",\"source\":\"UniProtKB\"}],\"name\":\"an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:29531\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19498\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19501\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19517\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19518\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57683\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58211\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132516\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132517\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:29.193985+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VBV8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VBV8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.4.1.261\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9H6U8\",\"source\":\"UniProtKB\"}],\"name\":\"an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:29539\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19498\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19501\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19519\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19520\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57683\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58211\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132519\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:132520\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:29.193985+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "24b898b648022de52a5691dcf6976ea8900e27682aaaa66849096b4d46e10d5f",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VBV8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)

```json
{
  "entry_version": 174,
  "evidence_id": "H1",
  "excerpt": "ID   ALG9_DROME              Reviewed;         623 AA.\nAC   Q9VBV8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 174.\nDE   RecName: Full=Alpha-1,2-mannosyltransferase Alg9 {ECO:0000312|FlyBase:FBgn0039293};\nDE            EC=2.4.1.259 {ECO:0000250|UniProtKB:Q9H6U8};\nDE            EC=2.4.1.261 {ECO:0000250|UniProtKB:Q9H6U8};\nDE   AltName: Full=Dolichyl-P-Man:Man6GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};\nDE   AltName: Full=Dolichyl-P-Man:Man8GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};\nGN   Name=Alg9 {ECO:0000312|FlyBase:FBgn0039293};\nGN   ORFNames=CG11851 {ECO:0000312|FlyBase:FBgn0039293};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.427257+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8",
  "url": "https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)

```json
{
  "entry_version": 174,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Alpha-1,2-mannosyltransferase Alg9 {ECO:0000312|FlyBase:FBgn0039293};\nDE            EC=2.4.1.259 {ECO:0000250|UniProtKB:Q9H6U8};\nDE            EC=2.4.1.261 {ECO:0000250|UniProtKB:Q9H6U8};\nDE   AltName: Full=Dolichyl-P-Man:Man6GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};\nDE   AltName: Full=Dolichyl-P-Man:Man8GlcNAc2-PP-dolichol alpha-1,2-mannosyltransferase {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.427257+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8",
  "url": "https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)

```json
{
  "entry_version": 174,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-\nCC         [alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-\nCC         GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a\nCC         di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = an alpha-D-\nCC         Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-\nCC         alpha-D-Man-(1->3)-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-beta-D-\nCC         GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-dolichol + a\nCC         di-trans,poly-cis-dolichyl phosphate + H(+); Xref=Rhea:RHEA:29531,\nCC         Rhea:RHEA-COMP:19498, Rhea:RHEA-COMP:19501, Rhea:RHEA-COMP:19517,\nCC         Rhea:RHEA-COMP:19518, ChEBI:CHEBI:15378, ChEBI:CHEBI:57683,\nCC         ChEBI:CHEBI:58211, ChEBI:CHEBI:132516, ChEBI:CHEBI:132517;\nCC         EC=2.4.1.259; Evidence={ECO:0000250|UniProtKB:Q9H6U8};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.427257+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-116",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8",
  "url": "https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174)

```json
{
  "entry_version": 174,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-\nCC         [alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-Man-(1->6)]-alpha-D-\nCC         Man-(1->6)]-beta-D-Man-(1->4)-beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-\nCC         diphospho-di-trans,poly-cis-dolichol + a di-trans,poly-cis-dolichyl\nCC         beta-D-mannosyl phosphate = an alpha-D-Man-(1->2)-alpha-D-Man-(1->2)-\nCC         alpha-D-Man-(1->3)-[alpha-D-Man-(1->2)-alpha-D-Man-(1->3)-[alpha-D-\nCC         Man-(1->2)-alpha-D-Man-(1->6)]-alpha-D-Man-(1->6)]-beta-D-Man-(1->4)-\nCC         beta-D-GlcNAc-(1->4)-alpha-D-GlcNAc-diphospho-di-trans,poly-cis-\nCC         dolichol + a di-trans,poly-cis-dolichyl phosphate + H(+);\nCC         Xref=Rhea:RHEA:29539, Rhea:RHEA-COMP:19498, Rhea:RHEA-COMP:19501,\nCC         Rhea:RHEA-COMP:19519, Rhea:RHEA-COMP:19520, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:57683, ChEBI:CHEBI:58211, ChEBI:CHEBI:132519,\nCC         ChEBI:CHEBI:132520; EC=2.4.1.261;\nCC         Evidence={ECO:0000250|UniProtKB:Q9H6U8};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:51.427257+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 117-131",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "32d28578b9cd594cb2408d344ac0c5be7d01172b1298053b690508892af4f5f8",
  "url": "https://rest.uniprot.org/unisave/Q9VBV8?format=txt&versions=174"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 38. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
