# EC_number_0138

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0138.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 3.2.1.8

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
A. 3.2.1.18
B. 3.2.1.20
C. 3.4.21.62
D. 3.2.1.8
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

> The sequence-matched UniProt record assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans. The EC assignment is supported by a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal hydrophobic signal-peptide-like region followed by a compact domain of roughly 200 residues, consistent with a secreted fungal GH11 endo-beta-1,4-xylanase. Family-level sequence and fold patterns can meaningfully distinguish that activity (option D) from the other listed glycosidase activities and the protease option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The choice is supported by transferable recognition of a secreted fungal xylanase family and its characteristic domain scale and sequence patterns; it does not require knowing this exact protein's database record. This is a family-level inference, not experimental confirmation of the exact substrate specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered EC numbers, 3.2.1.8 is the specific endo-beta-1,4-xylanase classification indicated by the sequence-family inference.


### Important caveats

- The reviewer-only source annotation is sequence-matched, but its EC evidence is computational (PROSITE-ProRule); the excerpts do not establish direct experimental measurement of catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region followed by a compact domain of roughly 200 residues, consistent with a secreted fungal GH11 endo-beta-1,4-xylanase. Family-level sequence and fold patterns can meaningfully distinguish that activity (option D) from the other listed glycosidase activities and the protease option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The choice is supported by transferable recognition of a secreted fungal xylanase family and its characteristic domain scale and sequence patterns; it does not require knowing this exact protein's database record. This is a family-level inference, not experimental confirmation of the exact substrate specificity."
  },
  "case_id": "EC_number_0138",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans. The EC assignment is supported by a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer-only source annotation is sequence-matched, but its EC evidence is computational (PROSITE-ProRule); the excerpts do not establish direct experimental measurement of catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered EC numbers, 3.2.1.8 is the specific endo-beta-1,4-xylanase classification indicated by the sequence-family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0138",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 3.2.1.8 and describes endohydrolysis of beta-D-xylosidic linkages in xylans. The EC assignment is supported by a PROSITE-ProRule computational annotation, not direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal hydrophobic signal-peptide-like region followed by a compact domain of roughly 200 residues, consistent with a secreted fungal GH11 endo-beta-1,4-xylanase. Family-level sequence and fold patterns can meaningfully distinguish that activity (option D) from the other listed glycosidase activities and the protease option.",
    "missing_item_specific_fact": "",
    "reason": "The choice is supported by transferable recognition of a secreted fungal xylanase family and its characteristic domain scale and sequence patterns; it does not require knowing this exact protein's database record. This is a family-level inference, not experimental confirmation of the exact substrate specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered EC numbers, 3.2.1.8 is the specific endo-beta-1,4-xylanase classification indicated by the sequence-family inference."
  },
  "important_caveats": [
    "The reviewer-only source annotation is sequence-matched, but its EC evidence is computational (PROSITE-ProRule); the excerpts do not establish direct experimental measurement of catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry G2X4G1 (EIX5_VERDV) annotates EC 3.2.1.8 (endo-1,4-β-xylanase) with evidence code ECO:0000255 (PROSITE-ProRule:PRU01097), a computational protein-family rule match. The catalytic activity comment states 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The sequence matches the benchmark input exactly (224 aa, same SHA256). The annotation is database-supported but rests on computational inference from a PROSITE glycosyl hydrolase family 11 rule rather than direct experimental enzymatic assay. The PubMed reference (33205907) concerns perception of EIX-like proteins by plant receptors, not xylanase activity measurement.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable sequence-level features meaningfully distinguish the four choices. (1) The N-terminal hydrophobic stretch MLKSLVVLLLTSRVIAFP is a classic signal peptide, indicating a secreted protein—consistent with fungal plant-cell-wall-degrading enzymes but atypical for intracellular serine proteases like caspase-1 (option C). (2) The mature protein is only ~190 aa after signal-peptide cleavage. Among the offered EC numbers, GH11 endo-1,4-β-xylanases (3.2.1.8, option D) are the smallest glycoside hydrolases (~190-250 aa mature), whereas α-galactosidases (3.2.1.18, option A; GH27/36/50 families) are typically 400-700 aa and α-glucuronidases (3.2.1.20, option B; GH67/115) are typically >500 aa. This size constraint strongly disfavors A and B. (3) The sequence contains clusters of aromatic residues (GTHGGFFYYWW, YWSVRR, SYCLRWESGG) characteristic of the carbohydrate-binding groove of β-jelly-roll GH11 xylanases. (4) No catalytic triad (His-Asp-Ser) or GDSGG motif typical of serine proteases is present, ruling out option C. Together, these features—small secreted protein with aromatic-rich binding surface and no protease catalytic architecture—provide a concrete, transferable inference favoring D over A, B, and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of mature-protein size (~190 aa), presence of a signal peptide, aromatic-residue clustering typical of GH11 substrate-binding grooves, and absence of any protease catalytic triad allows a knowledgeable model to eliminate C (wrong fold entirely), and to disfavour A and B (wrong size class for their respective GH families), leaving D as the most consistent choice. This is a legitimate family-level and size-based inference learned from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The size constraint alone (mature ~190 aa) provides a strong quantitative discriminator against α-galactosidases and α-glucuronidases, and the absence of any protease catalytic motif clearly excludes option C. The remaining option D is well-supported by the aromatic-residue pattern and secreted nature.


### Important caveats

- The UniProt EC annotation relies on ECO:0000255 (PROSITE-ProRule PRU01097), a computational protein-family rule match, not direct experimental xylanase assay. The protein was named 'Ethylene-inducing xylanase' based on ethylene-inducing activity in plants; direct xylanase activity measurement for this specific protein is not confirmed in the cited references.
- The PubMed reference (33205907) addresses plant perception of EIX-like proteins, not enzymatic characterization of xylanase activity.
- Distinguishing GH11 from other small GH families purely by sequence is feasible here largely because the alternative choices (α-galactosidase, α-glucuronidase, caspase) belong to very different size and fold classes, making the discrimination more robust than a fine-grained intra-GH comparison would be.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable sequence-level features meaningfully distinguish the four choices. (1) The N-terminal hydrophobic stretch MLKSLVVLLLTSRVIAFP is a classic signal peptide, indicating a secreted protein—consistent with fungal plant-cell-wall-degrading enzymes but atypical for intracellular serine proteases like caspase-1 (option C). (2) The mature protein is only ~190 aa after signal-peptide cleavage. Among the offered EC numbers, GH11 endo-1,4-β-xylanases (3.2.1.8, option D) are the smallest glycoside hydrolases (~190-250 aa mature), whereas α-galactosidases (3.2.1.18, option A; GH27/36/50 families) are typically 400-700 aa and α-glucuronidases (3.2.1.20, option B; GH67/115) are typically >500 aa. This size constraint strongly disfavors A and B. (3) The sequence contains clusters of aromatic residues (GTHGGFFYYWW, YWSVRR, SYCLRWESGG) characteristic of the carbohydrate-binding groove of β-jelly-roll GH11 xylanases. (4) No catalytic triad (His-Asp-Ser) or GDSGG motif typical of serine proteases is present, ruling out option C. Together, these features—small secreted protein with aromatic-rich binding surface and no protease catalytic architecture—provide a concrete, transferable inference favoring D over A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of mature-protein size (~190 aa), presence of a signal peptide, aromatic-residue clustering typical of GH11 substrate-binding grooves, and absence of any protease catalytic triad allows a knowledgeable model to eliminate C (wrong fold entirely), and to disfavour A and B (wrong size class for their respective GH families), leaving D as the most consistent choice. This is a legitimate family-level and size-based inference learned from other proteins."
  },
  "case_id": "EC_number_0138",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry G2X4G1 (EIX5_VERDV) annotates EC 3.2.1.8 (endo-1,4-β-xylanase) with evidence code ECO:0000255 (PROSITE-ProRule:PRU01097), a computational protein-family rule match. The catalytic activity comment states 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The sequence matches the benchmark input exactly (224 aa, same SHA256). The annotation is database-supported but rests on computational inference from a PROSITE glycosyl hydrolase family 11 rule rather than direct experimental enzymatic assay. The PubMed reference (33205907) concerns perception of EIX-like proteins by plant receptors, not xylanase activity measurement."
  },
  "important_caveats": [
    "The UniProt EC annotation relies on ECO:0000255 (PROSITE-ProRule PRU01097), a computational protein-family rule match, not direct experimental xylanase assay. The protein was named 'Ethylene-inducing xylanase' based on ethylene-inducing activity in plants; direct xylanase activity measurement for this specific protein is not confirmed in the cited references.",
    "The PubMed reference (33205907) addresses plant perception of EIX-like proteins, not enzymatic characterization of xylanase activity.",
    "Distinguishing GH11 from other small GH families purely by sequence is feasible here largely because the alternative choices (α-galactosidase, α-glucuronidase, caspase) belong to very different size and fold classes, making the discrimination more robust than a fine-grained intra-GH comparison would be."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size constraint alone (mature ~190 aa) provides a strong quantitative discriminator against α-galactosidases and α-glucuronidases, and the absence of any protease catalytic motif clearly excludes option C. The remaining option D is well-supported by the aromatic-residue pattern and secreted nature."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0138",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry G2X4G1 (EIX5_VERDV) annotates EC 3.2.1.8 (endo-1,4-β-xylanase) with evidence code ECO:0000255 (PROSITE-ProRule:PRU01097), a computational protein-family rule match. The catalytic activity comment states 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' The sequence matches the benchmark input exactly (224 aa, same SHA256). The annotation is database-supported but rests on computational inference from a PROSITE glycosyl hydrolase family 11 rule rather than direct experimental enzymatic assay. The PubMed reference (33205907) concerns perception of EIX-like proteins by plant receptors, not xylanase activity measurement.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable sequence-level features meaningfully distinguish the four choices. (1) The N-terminal hydrophobic stretch MLKSLVVLLLTSRVIAFP is a classic signal peptide, indicating a secreted protein—consistent with fungal plant-cell-wall-degrading enzymes but atypical for intracellular serine proteases like caspase-1 (option C). (2) The mature protein is only ~190 aa after signal-peptide cleavage. Among the offered EC numbers, GH11 endo-1,4-β-xylanases (3.2.1.8, option D) are the smallest glycoside hydrolases (~190-250 aa mature), whereas α-galactosidases (3.2.1.18, option A; GH27/36/50 families) are typically 400-700 aa and α-glucuronidases (3.2.1.20, option B; GH67/115) are typically >500 aa. This size constraint strongly disfavors A and B. (3) The sequence contains clusters of aromatic residues (GTHGGFFYYWW, YWSVRR, SYCLRWESGG) characteristic of the carbohydrate-binding groove of β-jelly-roll GH11 xylanases. (4) No catalytic triad (His-Asp-Ser) or GDSGG motif typical of serine proteases is present, ruling out option C. Together, these features—small secreted protein with aromatic-rich binding surface and no protease catalytic architecture—provide a concrete, transferable inference favoring D over A, B, and C.",
    "missing_item_specific_fact": "",
    "reason": "The combination of mature-protein size (~190 aa), presence of a signal peptide, aromatic-residue clustering typical of GH11 substrate-binding grooves, and absence of any protease catalytic triad allows a knowledgeable model to eliminate C (wrong fold entirely), and to disfavour A and B (wrong size class for their respective GH families), leaving D as the most consistent choice. This is a legitimate family-level and size-based inference learned from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The size constraint alone (mature ~190 aa) provides a strong quantitative discriminator against α-galactosidases and α-glucuronidases, and the absence of any protease catalytic motif clearly excludes option C. The remaining option D is well-supported by the aromatic-residue pattern and secreted nature."
  },
  "important_caveats": [
    "The UniProt EC annotation relies on ECO:0000255 (PROSITE-ProRule PRU01097), a computational protein-family rule match, not direct experimental xylanase assay. The protein was named 'Ethylene-inducing xylanase' based on ethylene-inducing activity in plants; direct xylanase activity measurement for this specific protein is not confirmed in the cited references.",
    "The PubMed reference (33205907) addresses plant perception of EIX-like proteins, not enzymatic characterization of xylanase activity.",
    "Distinguishing GH11 from other small GH families purely by sequence is feasible here largely because the alternative choices (α-galactosidase, α-glucuronidase, caspase) belong to very different size and fold classes, making the discrimination more robust than a fine-grained intra-GH comparison would be."
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
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
  "excerpt": "DE   RecName: Full=Ethylene-inducing xylanase 5 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX5 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX5 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:04.705992+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X4G1?format=txt&versions=57)

```json
{
  "entry_version": 57,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000255|PROSITE-ProRule:PRU01097};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:04.705992+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e0c511e580167b3398281d34cf1b42f13481b77974f64acc52440d0b06a7af8b",
  "url": "https://rest.uniprot.org/unisave/G2X4G1?format=txt&versions=57"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 138. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
