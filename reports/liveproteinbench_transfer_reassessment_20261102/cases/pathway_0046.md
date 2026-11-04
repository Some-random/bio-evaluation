# pathway_0046

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0046.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDLLQILLAIAGLLAILLLQKQWRTKTSPGAKAGRKLPPEPAGAWPVIGHLHKLGGPNPIYRNLAEWSDKYGPVMTLKLGMQNAVVVSDREAIKECFTTNDKALADRPPSSIGLHLGFNYAAIGAAPYGPYWRDMRKLVLLEVLSSRRLEMLRNVRISEIGTSIKELYSNIIRSSGGSGPAKVVISHWIEQLTLNYILRTIAGRRFSDDSSKDAQYVKGVINDFMYFAGQFVVSDVIPIPLLRWLDPQGHLKGMKRVAKEVDTMCEAWIQEHVQRRMREKPGPGQEQDFIDVLLNNRDVMRKAQEEIDNHVGKERWVDETDLKHLVYLQAIVKEGLRLYPPGPLGAPHRAIEDCQVGGYFIPKGTQLLVNVWKLHRDPRVWSEPEKFMPERFLTRQAEVDVFGHHFELLPFGSGRRACPGITFAVQVMHLTVARLLQGFDMTTPSNLPVDMTEGPGVTMPKAHPVEVLMMPRLPSALYEP

[Multiple Choices]
A. Bacterial outer membrane biogenesis
B. coenzyme A biosynthesis
C. Alkaloid biosynthesis
D. fatty acid beta-oxidation. .
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

> The matched UniProt entry names the protein as vinorine hydroxylase and annotates it to alkaloid and ajmaline biosynthesis, citing evidence coded as experimental. This supports choice C for the supplied sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal segment consistent with a microsomal membrane anchor and a conserved P450 heme-binding motif (FxxGxxxCxG), supporting a cytochrome P450 enzyme. Transferable knowledge that plant P450s commonly catalyze oxidative steps in specialized-metabolite biosynthesis makes alkaloid biosynthesis the strongest offered choice; the other options are associated with substantially different enzyme systems.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and family-level inference meaningfully favor C among these alternatives without requiring recall of this exact protein's annotation. The specific substrate and pathway assignment are not certain from the sequence alone, but the alternatives make the P450-based inference discriminating.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence does not prove an alkaloid pathway assignment by itself, but the offered alternatives do not provide another comparably plausible pathway for a plant-like microsomal P450.


### Important caveats

- The pathway annotation is supported by cited experimental evidence in the matched database entry; it is not a direct measurement included in the question.
- P450 family membership alone does not uniquely identify substrate or pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal segment consistent with a microsomal membrane anchor and a conserved P450 heme-binding motif (FxxGxxxCxG), supporting a cytochrome P450 enzyme. Transferable knowledge that plant P450s commonly catalyze oxidative steps in specialized-metabolite biosynthesis makes alkaloid biosynthesis the strongest offered choice; the other options are associated with substantially different enzyme systems.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level inference meaningfully favor C among these alternatives without requiring recall of this exact protein's annotation. The specific substrate and pathway assignment are not certain from the sequence alone, but the alternatives make the P450-based inference discriminating."
  },
  "case_id": "pathway_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt entry names the protein as vinorine hydroxylase and annotates it to alkaloid and ajmaline biosynthesis, citing evidence coded as experimental. This supports choice C for the supplied sequence."
  },
  "important_caveats": [
    "The pathway annotation is supported by cited experimental evidence in the matched database entry; it is not a direct measurement included in the question.",
    "P450 family membership alone does not uniquely identify substrate or pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not prove an alkaloid pathway assignment by itself, but the offered alternatives do not provide another comparably plausible pathway for a plant-like microsomal P450."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt entry names the protein as vinorine hydroxylase and annotates it to alkaloid and ajmaline biosynthesis, citing evidence coded as experimental. This supports choice C for the supplied sequence.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal segment consistent with a microsomal membrane anchor and a conserved P450 heme-binding motif (FxxGxxxCxG), supporting a cytochrome P450 enzyme. Transferable knowledge that plant P450s commonly catalyze oxidative steps in specialized-metabolite biosynthesis makes alkaloid biosynthesis the strongest offered choice; the other options are associated with substantially different enzyme systems.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level inference meaningfully favor C among these alternatives without requiring recall of this exact protein's annotation. The specific substrate and pathway assignment are not certain from the sequence alone, but the alternatives make the P450-based inference discriminating."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence does not prove an alkaloid pathway assignment by itself, but the offered alternatives do not provide another comparably plausible pathway for a plant-like microsomal P450."
  },
  "important_caveats": [
    "The pathway annotation is supported by cited experimental evidence in the matched database entry; it is not a direct measurement included in the question.",
    "P450 family membership alone does not uniquely identify substrate or pathway."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this exact sequence (A0A218NGS0, Vinorine hydroxylase / CYP5437 / CYP82S18 from Rauvolfia serpentina) explicitly annotates the pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence codes (ECO:0000269, PubMed:28654178 and PubMed:38212296). The expected answer C (Alkaloid biosynthesis) is directly and experimentally supported.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical cytochrome P450 heme-binding motif (FGSGRRACPG, matching the FxxGxxxCxG signature) near the C-terminus, and an N-terminal ER-targeting signal peptide (MDLLQILLAIAGLLAILLLQKQWRTKTSPGAKAGRKLPPEPAGAWPVI…), yielding a ~480-aa plant-type CYP450. Transferable knowledge from other plant proteins establishes that plant microsomal CYP450s are overwhelmingly involved in secondary metabolite biosynthesis (alkaloids, terpenoids, phenylpropanoids), not in primary lipid or cofactor pathways. In particular, the CYP82 and CYP5437 subfamilies, recognized across multiple plant species (Catharanthus, Rauvolfia, Nicotiana), are well-characterized alkaloid-biosynthesis P450s. Among the four offered choices: (A) bacterial outer membrane biogenesis is excluded by the eukaryotic signal peptide and CYP450 domain; (B) coenzyme A biosynthesis involves small acyl-CoA synthetases and phosphopantetheinyl transferases, not CYP450s; (D) fatty acid beta-oxidation occurs in peroxisomes/mitochondria via acyl-CoA dehydrogenases and thiolases, not via ER-anchored CYP450s. The combination of CYP450 domain recognition, plant-type ER targeting, and the well-known family-level association of plant CYP82/CYP5437-type P450s with alkaloid biosynthesis meaningfully distinguishes option C from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the CYP450 heme-binding motif from the sequence, recognize the plant-type ER signal peptide, and apply the well-established pattern that plant microsomal CYP450s (especially CYP82/CYP5437-family members across multiple species) function in alkaloid biosynthesis. This family-level transfer from other plant CYP450s is sufficient to select C over the clearly incompatible alternatives without needing the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span fundamentally different biological contexts (bacterial membrane, cofactor synthesis, alkaloid biosynthesis, fatty acid oxidation). The CYP450 domain and plant ER targeting make options A, B, and D strongly incompatible, leaving C as the only plausible pathway for a plant microsomal P450 involved in secondary metabolism.


### Important caveats

- The reviewer-only evidence confirms the protein is Vinorine hydroxylase (CYP5437/CYP82S18) from Rauvolfia serpentina, experimentally characterized in ajmaline biosynthesis, but this specific identity was not available to the evaluated model.
- The CYP82/CYP5437 family association with alkaloid biosynthesis is well-supported across multiple plant species and constitutes legitimate transferable knowledge, not target-specific memorization.
- The sequence match to the UniProt entry is exact (SHA-256 confirmed), and the annotation is backed by two experimental publications.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (FGSGRRACPG, matching the FxxGxxxCxG signature) near the C-terminus, and an N-terminal ER-targeting signal peptide (MDLLQILLAIAGLLAILLLQKQWRTKTSPGAKAGRKLPPEPAGAWPVI…), yielding a ~480-aa plant-type CYP450. Transferable knowledge from other plant proteins establishes that plant microsomal CYP450s are overwhelmingly involved in secondary metabolite biosynthesis (alkaloids, terpenoids, phenylpropanoids), not in primary lipid or cofactor pathways. In particular, the CYP82 and CYP5437 subfamilies, recognized across multiple plant species (Catharanthus, Rauvolfia, Nicotiana), are well-characterized alkaloid-biosynthesis P450s. Among the four offered choices: (A) bacterial outer membrane biogenesis is excluded by the eukaryotic signal peptide and CYP450 domain; (B) coenzyme A biosynthesis involves small acyl-CoA synthetases and phosphopantetheinyl transferases, not CYP450s; (D) fatty acid beta-oxidation occurs in peroxisomes/mitochondria via acyl-CoA dehydrogenases and thiolases, not via ER-anchored CYP450s. The combination of CYP450 domain recognition, plant-type ER targeting, and the well-known family-level association of plant CYP82/CYP5437-type P450s with alkaloid biosynthesis meaningfully distinguishes option C from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the CYP450 heme-binding motif from the sequence, recognize the plant-type ER signal peptide, and apply the well-established pattern that plant microsomal CYP450s (especially CYP82/CYP5437-family members across multiple species) function in alkaloid biosynthesis. This family-level transfer from other plant CYP450s is sufficient to select C over the clearly incompatible alternatives without needing the specific UniProt annotation for this exact protein."
  },
  "case_id": "pathway_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this exact sequence (A0A218NGS0, Vinorine hydroxylase / CYP5437 / CYP82S18 from Rauvolfia serpentina) explicitly annotates the pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence codes (ECO:0000269, PubMed:28654178 and PubMed:38212296). The expected answer C (Alkaloid biosynthesis) is directly and experimentally supported."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the protein is Vinorine hydroxylase (CYP5437/CYP82S18) from Rauvolfia serpentina, experimentally characterized in ajmaline biosynthesis, but this specific identity was not available to the evaluated model.",
    "The CYP82/CYP5437 family association with alkaloid biosynthesis is well-supported across multiple plant species and constitutes legitimate transferable knowledge, not target-specific memorization.",
    "The sequence match to the UniProt entry is exact (SHA-256 confirmed), and the annotation is backed by two experimental publications."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different biological contexts (bacterial membrane, cofactor synthesis, alkaloid biosynthesis, fatty acid oxidation). The CYP450 domain and plant ER targeting make options A, B, and D strongly incompatible, leaving C as the only plausible pathway for a plant microsomal P450 involved in secondary metabolism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this exact sequence (A0A218NGS0, Vinorine hydroxylase / CYP5437 / CYP82S18 from Rauvolfia serpentina) explicitly annotates the pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence codes (ECO:0000269, PubMed:28654178 and PubMed:38212296). The expected answer C (Alkaloid biosynthesis) is directly and experimentally supported.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical cytochrome P450 heme-binding motif (FGSGRRACPG, matching the FxxGxxxCxG signature) near the C-terminus, and an N-terminal ER-targeting signal peptide (MDLLQILLAIAGLLAILLLQKQWRTKTSPGAKAGRKLPPEPAGAWPVI…), yielding a ~480-aa plant-type CYP450. Transferable knowledge from other plant proteins establishes that plant microsomal CYP450s are overwhelmingly involved in secondary metabolite biosynthesis (alkaloids, terpenoids, phenylpropanoids), not in primary lipid or cofactor pathways. In particular, the CYP82 and CYP5437 subfamilies, recognized across multiple plant species (Catharanthus, Rauvolfia, Nicotiana), are well-characterized alkaloid-biosynthesis P450s. Among the four offered choices: (A) bacterial outer membrane biogenesis is excluded by the eukaryotic signal peptide and CYP450 domain; (B) coenzyme A biosynthesis involves small acyl-CoA synthetases and phosphopantetheinyl transferases, not CYP450s; (D) fatty acid beta-oxidation occurs in peroxisomes/mitochondria via acyl-CoA dehydrogenases and thiolases, not via ER-anchored CYP450s. The combination of CYP450 domain recognition, plant-type ER targeting, and the well-known family-level association of plant CYP82/CYP5437-type P450s with alkaloid biosynthesis meaningfully distinguishes option C from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the CYP450 heme-binding motif from the sequence, recognize the plant-type ER signal peptide, and apply the well-established pattern that plant microsomal CYP450s (especially CYP82/CYP5437-family members across multiple species) function in alkaloid biosynthesis. This family-level transfer from other plant CYP450s is sufficient to select C over the clearly incompatible alternatives without needing the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span fundamentally different biological contexts (bacterial membrane, cofactor synthesis, alkaloid biosynthesis, fatty acid oxidation). The CYP450 domain and plant ER targeting make options A, B, and D strongly incompatible, leaving C as the only plausible pathway for a plant microsomal P450 involved in secondary metabolism."
  },
  "important_caveats": [
    "The reviewer-only evidence confirms the protein is Vinorine hydroxylase (CYP5437/CYP82S18) from Rauvolfia serpentina, experimentally characterized in ajmaline biosynthesis, but this specific identity was not available to the evaluated model.",
    "The CYP82/CYP5437 family association with alkaloid biosynthesis is well-supported across multiple plant species and constitutes legitimate transferable knowledge, not target-specific memorization.",
    "The sequence match to the UniProt entry is exact (SHA-256 confirmed), and the annotation is backed by two experimental publications."
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
  "benchmark_sequence_length": 480,
  "benchmark_sequence_sha256": "df32080a6e9de3721d39ca92db4a6f289633e69df676d9b2fd35529c70abf20c",
  "current_entry_audit": {
    "entryVersion": 27,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2017-09-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 480,
  "current_source_sequence_sha256": "df32080a6e9de3721d39ca92db4a6f289633e69df676d9b2fd35529c70abf20c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 26,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A218NGS0",
  "selected_historical_entry_version": 26,
  "selected_historical_record_sha256": "48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f",
  "selected_historical_source_sequence_length": 480,
  "selected_historical_source_sequence_sha256": "df32080a6e9de3721d39ca92db4a6f289633e69df676d9b2fd35529c70abf20c",
  "selected_historical_version": {
    "accession": "A0A218NGS0",
    "database": "Swiss-Prot",
    "entryVersion": 26,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "VINHY_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A218NGS0\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:42.234878+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40",
  "url": "https://rest.uniprot.org/uniprotkb/A0A218NGS0.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":27,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2017-09-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:42.234878+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40",
  "url": "https://rest.uniprot.org/uniprotkb/A0A218NGS0.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:42.234878+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40",
  "url": "https://rest.uniprot.org/uniprotkb/A0A218NGS0.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ASG81458.1\",\"source\":\"EMBL\"}],\"value\":\"Cytochrome P450 5437\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ASG81458.1\",\"source\":\"EMBL\"}],\"value\":\"RsCYP5437\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28654178\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 82S18\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28654178\",\"source\":\"PubMed\"}],\"value\":\"Perakine synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28654178\",\"source\":\"PubMed\"}],\"value\":\"Vomilenine isomerase\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28654178\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.104\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"28654178\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Vinorine hydroxylase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsVH\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:42.234878+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40",
  "url": "https://rest.uniprot.org/uniprotkb/A0A218NGS0.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"28654178\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis; ajmaline biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-01T06:24:42.234878+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40",
  "url": "https://rest.uniprot.org/uniprotkb/A0A218NGS0.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Dang T.T.\",\"Franke J.\",\"Tatsis E.\",\"O'Connor S.E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"28654178\"},{\"database\":\"DOI\",\"id\":\"10.1002/anie.201705010\"}],\"citationType\":\"journal article\",\"firstPage\":\"9440\",\"id\":\"28654178\",\"journal\":\"Angew. Chem. Int. Ed.\",\"lastPage\":\"9444\",\"publicationDate\":\"2017\",\"title\":\"Dual catalytic activity of a cytochrome P450 controls bifurcation at a metabolic branch point of alkaloid biosynthesis in Rauwolfia serpentina.\",\"volume\":\"56\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ASG81458.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:42.234878+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40",
  "url": "https://rest.uniprot.org/uniprotkb/A0A218NGS0.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A218NGS0.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:42.234878+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3344314f4da5addc19db5cda9ea0987bc724f5d222433aee0a5e8af38bc94b40",
  "url": "https://rest.uniprot.org/uniprotkb/A0A218NGS0.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H1",
  "excerpt": "ID   VINHY_RAUSE             Reviewed;         480 AA.\nAC   A0A218NGS0;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-SEP-2017, sequence version 1.\nDT   28-JAN-2026, entry version 26.\nDE   RecName: Full=Vinorine hydroxylase {ECO:0000303|PubMed:28654178, ECO:0000303|PubMed:38212296};\nDE            Short=RsVH {ECO:0000303|PubMed:38212296};\nDE            EC=1.14.14.104 {ECO:0000269|PubMed:28654178, ECO:0000269|PubMed:38212296};\nDE   AltName: Full=Cytochrome P450 5437 {ECO:0000312|EMBL:ASG81458.1};\nDE            Short=RsCYP5437 {ECO:0000312|EMBL:ASG81458.1};\nDE   AltName: Full=Cytochrome P450 82S18 {ECO:0000303|PubMed:28654178};\nDE   AltName: Full=Perakine synthase {ECO:0000303|PubMed:28654178};\nDE            Short=Vomilenine isomerase {ECO:0000303|PubMed:28654178};\nGN   Name=VH {ECO:0000303|PubMed:28654178, ECO:0000303|PubMed:38212296};\nGN   Synonyms=CYP5437 {ECO:0000312|EMBL:ASG81458.1},\nGN   CYP82S18 {ECO:0000303|PubMed:28654178};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.367833+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f",
  "url": "https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ASG81458.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, AND TISSUE SPECIFICITY.\nRX   PubMed=28654178; DOI=10.1002/anie.201705010;\nRA   Dang T.T., Franke J., Tatsis E., O'Connor S.E.;\nRT   \"Dual catalytic activity of a cytochrome P450 controls bifurcation at a\nRT   metabolic branch point of alkaloid biosynthesis in Rauwolfia serpentina.\";\nRL   Angew. Chem. Int. Ed. 56:9440-9444(2017).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.367833+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f",
  "url": "https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.367833+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f",
  "url": "https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26)

```json
{
  "entry_version": 26,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.\nCC       {ECO:0000269|PubMed:28654178, ECO:0000269|PubMed:38212296}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:24.367833+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-79",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "48cff725e5a58f4e22b3c3036b7c75532fc0df2b16678a21392e3db27ec7ea5f",
  "url": "https://rest.uniprot.org/unisave/A0A218NGS0?format=txt&versions=26"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 46. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
