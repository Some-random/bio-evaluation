# pathway_0051

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0051.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Cofactor biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MMESAVTAHTLRIAMAQFDFPVGAVTQNTDRIIEYIAAARDEFEADIVLFPELAISGYPPEDLLLRPGFLAHCEQALARIAAATRGIVAVVGWPQSAGSVVYNAASVLREGRIEATYRKRELPNYAVFDERRYFDVDPDGDNCVVTVKGVQVGVVICEDLWFAEPLAKTVQAGAELVLVPNASPYERGKHAQRDALLAERTRESGAAIAYLNVVGGQDALVFDGASVVADGDGTVHPAAAAFVDQWLVVDYAAGERSFTPVVWVDDGDESMDALAWRAVVRGLKDYCGKNGFRKVWLGLSGGIDSALVLAMAVDALGGENVTAVRLPSRYTAGLSNDLADEQCRALGVKLETIAIEPAFEGLLAALGPLFADTQPDITEENLQSRSRGVILMALSNKFGGLVLTTGNKSEYAVGYATIYGDMCGGYAPLKDLYKTEVFGLAKWRNTVGGAPVIPPAVISRPPSAELRDNQTDQDSLPPYDVLDGILYRYVDQEQSRDDIVAAGYAADTVEHVLRLVRLNEWKRHQAAPGPKVSRRAFGRERRYPITNGYSGQ

[Multiple Choices]
A. Antifungal biosynthesis. .
B. L-cystathionine from O-succinyl-L-homoserine: step 1/1. .
C. Cofactor biosynthesis
D. Membrane lipid metabolism. .
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

> The sequence-matched record annotates the protein as glutamine-dependent NAD(+) synthetase and places it in NAD(+) biosynthesis, a cofactor biosynthesis pathway. The annotations are attributed to a HAMAP rule, so this is computational support rather than direct experimental evidence in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 552-residue sequence is consistent with the two-domain glutamine-dependent NAD synthetase family: an N-terminal glutamine-hydrolyzing domain coupled to a C-terminal nucleotide-synthetase domain. Family knowledge links this enzyme to NAD biosynthesis, which meaningfully selects cofactor biosynthesis (C) over cystathionine formation, antifungal biosynthesis, or membrane lipid metabolism.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and transferable knowledge of NAD synthetase family architecture and function provide a credible pathway-level inference without needing this exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices distinguish NAD/cofactor biosynthesis from unrelated pathways; the sequence-supported enzyme-family inference favors C.


### Important caveats

- The supplied pathway annotation is computational (HAMAP-rule evidence); the excerpts do not independently establish experimental validation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 552-residue sequence is consistent with the two-domain glutamine-dependent NAD synthetase family: an N-terminal glutamine-hydrolyzing domain coupled to a C-terminal nucleotide-synthetase domain. Family knowledge links this enzyme to NAD biosynthesis, which meaningfully selects cofactor biosynthesis (C) over cystathionine formation, antifungal biosynthesis, or membrane lipid metabolism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge of NAD synthetase family architecture and function provide a credible pathway-level inference without needing this exact protein's database record."
  },
  "case_id": "pathway_0051",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record annotates the protein as glutamine-dependent NAD(+) synthetase and places it in NAD(+) biosynthesis, a cofactor biosynthesis pathway. The annotations are attributed to a HAMAP rule, so this is computational support rather than direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The supplied pathway annotation is computational (HAMAP-rule evidence); the excerpts do not independently establish experimental validation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish NAD/cofactor biosynthesis from unrelated pathways; the sequence-supported enzyme-family inference favors C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0051",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record annotates the protein as glutamine-dependent NAD(+) synthetase and places it in NAD(+) biosynthesis, a cofactor biosynthesis pathway. The annotations are attributed to a HAMAP rule, so this is computational support rather than direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 552-residue sequence is consistent with the two-domain glutamine-dependent NAD synthetase family: an N-terminal glutamine-hydrolyzing domain coupled to a C-terminal nucleotide-synthetase domain. Family knowledge links this enzyme to NAD biosynthesis, which meaningfully selects cofactor biosynthesis (C) over cystathionine formation, antifungal biosynthesis, or membrane lipid metabolism.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and transferable knowledge of NAD synthetase family architecture and function provide a credible pathway-level inference without needing this exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish NAD/cofactor biosynthesis from unrelated pathways; the sequence-supported enzyme-family inference favors C."
  },
  "important_caveats": [
    "The supplied pathway annotation is computational (HAMAP-rule evidence); the excerpts do not independently establish experimental validation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (evidence C5, H3) explicitly assigns the pathway as 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1' under HAMAP-Rule MF_02090 (ECO:0000255, computational/family-based). A 2024 PubMed reference (38429435, C6/H2) provides structural and disruption-phenotype evidence for NAD+ biosynthesis in Xanthomonas campestris pv. campestris. The expected answer 'Cofactor biosynthesis' matches the top-level UniProt pathway category. The annotation is primarily family-based (HAMAP), but corroborated by experimental structural work.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly diagnostic GIDSA motif (residues ~'GIDSALVLAMAVDALGGEN') and the catalytic Cys of a Cys-His-Glu triad in 'GDMCGGY', which are hallmark features of the glutamine amidotransferase (GAT) domain family. This is a well-known, transferable sequence signature learned from many GAT enzymes (e.g., GMP synthase, carbamoyl phosphate synthetase, phosphoribosyl-ATP pyrophosphohydrolase). The overall two-domain architecture (N-terminal synthetase/adenylase domain + C-terminal GAT domain, ~550 aa total) is characteristic of glutamine-dependent synthetases that transfer an amide nitrogen. Among the four options: (B) cystathionine gamma-synthase is a PLP-dependent enzyme with entirely different sequence features and would not contain a GIDSA/GAT motif; (D) membrane lipid metabolism enzymes (e.g., desaturases, acyltransferases) do not typically harbor GAT domains; (A) antifungal biosynthesis is not a standard UniProt pathway category and does not match GAT-domain enzymes. Cofactor biosynthesis (C) is the natural fit: NAD+ is a classic redox cofactor, and the GAT domain is prevalent in cofactor/nucleotide biosynthesis enzymes (GMP synthase, NAD+ synthetase, FAD synthetase). Thus, recognizing the GIDSA/GAT signature and the synthetase+GAT architecture from the raw sequence, combined with the well-established pattern that GAT domains cluster in cofactor biosynthesis, meaningfully distinguishes C from the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GIDSA motif and Cys-His-Glu triad are directly readable from the supplied sequence and are textbook GAT-domain signatures. The association of GAT-containing synthetases with cofactor biosynthesis is a broad, transferable biochemical pattern. The distractors (PLP-dependent cystathionine synthase, membrane lipid enzymes, antifungal biosynthesis) are inconsistent with a GAT-domain architecture, making C the most defensible choice without needing the exact UniProt annotation for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The GAT domain signature and synthetase architecture clearly point to cofactor biosynthesis (C). Option B (cystathionine gamma-synthase) is a PLP enzyme with no GAT domain; D (membrane lipid metabolism) lacks GAT involvement; A (antifungal biosynthesis) is not a standard pathway category and does not match the domain architecture. No two options are genuinely defensible given the sequence features.


### Important caveats

- The primary UniProt pathway annotation is HAMAP-rule-based (ECO:0000255), i.e., a protein-family computational assignment rather than direct enzymatic assay. However, a 2024 structural and disruption-phenotype study (PubMed:38429435) provides experimental corroboration for NAD+ biosynthesis in this organism.
- The option text 'Cofactor biosynthesis' is the broad UniProt top-level pathway category; the full annotation specifies NAD(+) biosynthesis as a sub-pathway. This is consistent and not ambiguous.
- The GIDSA motif is a strong but not absolutely unique GAT signature; however, combined with the full domain architecture and the elimination of clearly incompatible distractors, it provides a robust and transferable basis for selecting C.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly diagnostic GIDSA motif (residues ~'GIDSALVLAMAVDALGGEN') and the catalytic Cys of a Cys-His-Glu triad in 'GDMCGGY', which are hallmark features of the glutamine amidotransferase (GAT) domain family. This is a well-known, transferable sequence signature learned from many GAT enzymes (e.g., GMP synthase, carbamoyl phosphate synthetase, phosphoribosyl-ATP pyrophosphohydrolase). The overall two-domain architecture (N-terminal synthetase/adenylase domain + C-terminal GAT domain, ~550 aa total) is characteristic of glutamine-dependent synthetases that transfer an amide nitrogen. Among the four options: (B) cystathionine gamma-synthase is a PLP-dependent enzyme with entirely different sequence features and would not contain a GIDSA/GAT motif; (D) membrane lipid metabolism enzymes (e.g., desaturases, acyltransferases) do not typically harbor GAT domains; (A) antifungal biosynthesis is not a standard UniProt pathway category and does not match GAT-domain enzymes. Cofactor biosynthesis (C) is the natural fit: NAD+ is a classic redox cofactor, and the GAT domain is prevalent in cofactor/nucleotide biosynthesis enzymes (GMP synthase, NAD+ synthetase, FAD synthetase). Thus, recognizing the GIDSA/GAT signature and the synthetase+GAT architecture from the raw sequence, combined with the well-established pattern that GAT domains cluster in cofactor biosynthesis, meaningfully distinguishes C from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GIDSA motif and Cys-His-Glu triad are directly readable from the supplied sequence and are textbook GAT-domain signatures. The association of GAT-containing synthetases with cofactor biosynthesis is a broad, transferable biochemical pattern. The distractors (PLP-dependent cystathionine synthase, membrane lipid enzymes, antifungal biosynthesis) are inconsistent with a GAT-domain architecture, making C the most defensible choice without needing the exact UniProt annotation for this protein."
  },
  "case_id": "pathway_0051",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) explicitly assigns the pathway as 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1' under HAMAP-Rule MF_02090 (ECO:0000255, computational/family-based). A 2024 PubMed reference (38429435, C6/H2) provides structural and disruption-phenotype evidence for NAD+ biosynthesis in Xanthomonas campestris pv. campestris. The expected answer 'Cofactor biosynthesis' matches the top-level UniProt pathway category. The annotation is primarily family-based (HAMAP), but corroborated by experimental structural work."
  },
  "important_caveats": [
    "The primary UniProt pathway annotation is HAMAP-rule-based (ECO:0000255), i.e., a protein-family computational assignment rather than direct enzymatic assay. However, a 2024 structural and disruption-phenotype study (PubMed:38429435) provides experimental corroboration for NAD+ biosynthesis in this organism.",
    "The option text 'Cofactor biosynthesis' is the broad UniProt top-level pathway category; the full annotation specifies NAD(+) biosynthesis as a sub-pathway. This is consistent and not ambiguous.",
    "The GIDSA motif is a strong but not absolutely unique GAT signature; however, combined with the full domain architecture and the elimination of clearly incompatible distractors, it provides a robust and transferable basis for selecting C."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GAT domain signature and synthetase architecture clearly point to cofactor biosynthesis (C). Option B (cystathionine gamma-synthase) is a PLP enzyme with no GAT domain; D (membrane lipid metabolism) lacks GAT involvement; A (antifungal biosynthesis) is not a standard pathway category and does not match the domain architecture. No two options are genuinely defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0051",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (evidence C5, H3) explicitly assigns the pathway as 'Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1' under HAMAP-Rule MF_02090 (ECO:0000255, computational/family-based). A 2024 PubMed reference (38429435, C6/H2) provides structural and disruption-phenotype evidence for NAD+ biosynthesis in Xanthomonas campestris pv. campestris. The expected answer 'Cofactor biosynthesis' matches the top-level UniProt pathway category. The annotation is primarily family-based (HAMAP), but corroborated by experimental structural work.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly diagnostic GIDSA motif (residues ~'GIDSALVLAMAVDALGGEN') and the catalytic Cys of a Cys-His-Glu triad in 'GDMCGGY', which are hallmark features of the glutamine amidotransferase (GAT) domain family. This is a well-known, transferable sequence signature learned from many GAT enzymes (e.g., GMP synthase, carbamoyl phosphate synthetase, phosphoribosyl-ATP pyrophosphohydrolase). The overall two-domain architecture (N-terminal synthetase/adenylase domain + C-terminal GAT domain, ~550 aa total) is characteristic of glutamine-dependent synthetases that transfer an amide nitrogen. Among the four options: (B) cystathionine gamma-synthase is a PLP-dependent enzyme with entirely different sequence features and would not contain a GIDSA/GAT motif; (D) membrane lipid metabolism enzymes (e.g., desaturases, acyltransferases) do not typically harbor GAT domains; (A) antifungal biosynthesis is not a standard UniProt pathway category and does not match GAT-domain enzymes. Cofactor biosynthesis (C) is the natural fit: NAD+ is a classic redox cofactor, and the GAT domain is prevalent in cofactor/nucleotide biosynthesis enzymes (GMP synthase, NAD+ synthetase, FAD synthetase). Thus, recognizing the GIDSA/GAT signature and the synthetase+GAT architecture from the raw sequence, combined with the well-established pattern that GAT domains cluster in cofactor biosynthesis, meaningfully distinguishes C from the other three options.",
    "missing_item_specific_fact": "",
    "reason": "The GIDSA motif and Cys-His-Glu triad are directly readable from the supplied sequence and are textbook GAT-domain signatures. The association of GAT-containing synthetases with cofactor biosynthesis is a broad, transferable biochemical pattern. The distractors (PLP-dependent cystathionine synthase, membrane lipid enzymes, antifungal biosynthesis) are inconsistent with a GAT-domain architecture, making C the most defensible choice without needing the exact UniProt annotation for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The GAT domain signature and synthetase architecture clearly point to cofactor biosynthesis (C). Option B (cystathionine gamma-synthase) is a PLP enzyme with no GAT domain; D (membrane lipid metabolism) lacks GAT involvement; A (antifungal biosynthesis) is not a standard pathway category and does not match the domain architecture. No two options are genuinely defensible given the sequence features."
  },
  "important_caveats": [
    "The primary UniProt pathway annotation is HAMAP-rule-based (ECO:0000255), i.e., a protein-family computational assignment rather than direct enzymatic assay. However, a 2024 structural and disruption-phenotype study (PubMed:38429435) provides experimental corroboration for NAD+ biosynthesis in this organism.",
    "The option text 'Cofactor biosynthesis' is the broad UniProt top-level pathway category; the full annotation specifies NAD(+) biosynthesis as a sub-pathway. This is consistent and not ambiguous.",
    "The GIDSA motif is a strong but not absolutely unique GAT signature; however, combined with the full domain architecture and the elimination of clearly incompatible distractors, it provides a robust and transferable basis for selecting C."
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
  "benchmark_sequence_length": 552,
  "benchmark_sequence_sha256": "3d11eda2e9e6481a31767f7fc550e14d13db9c3ed7ac21360bb4b2288341703d",
  "current_entry_audit": {
    "entryVersion": 50,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2015-09-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 552,
  "current_source_sequence_sha256": "3d11eda2e9e6481a31767f7fc550e14d13db9c3ed7ac21360bb4b2288341703d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 49,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0H2X6L3",
  "selected_historical_entry_version": 49,
  "selected_historical_record_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "selected_historical_source_sequence_length": 552,
  "selected_historical_source_sequence_sha256": "3d11eda2e9e6481a31767f7fc550e14d13db9c3ed7ac21360bb4b2288341703d",
  "selected_historical_version": {
    "accession": "A0A0H2X6L3",
    "database": "Swiss-Prot",
    "entryVersion": 49,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NADE_XANC8",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0H2X6L3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":50,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2015-09-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Lysobacterales\",\"Lysobacteraceae\",\"Xanthomonas\"],\"scientificName\":\"Xanthomonas campestris pv. campestris (strain 8004)\",\"taxonId\":314565}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"value\":\"NAD(+) synthase [glutamine-hydrolyzing]\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"NAD(+) synthetase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38429435\",\"source\":\"PubMed\"}],\"value\":\"NADS\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"value\":\"6.3.5.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Glutamine-dependent NAD(+) synthetase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"MF_02090\",\"source\":\"HAMAP-Rule\"}],\"value\":\"Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Xu G.\",\"Ma J.\",\"Fang Q.\",\"Peng Q.\",\"Jiao X.\",\"Hu W.\",\"Zhao Q.\",\"Kong Y.\",\"Liu F.\",\"Shi X.\",\"Tang D.J.\",\"Tang J.L.\",\"Ming Z.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38429435\"},{\"database\":\"DOI\",\"id\":\"10.1038/s42003-024-05921-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"255\",\"id\":\"38429435\",\"journal\":\"Commun. Biol.\",\"lastPage\":\"255\",\"publicationDate\":\"2024\",\"title\":\"Structural insights into Xanthomonas campestris pv. campestris NAD+ biosynthesis via the NAM salvage pathway.\",\"volume\":\"7\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"8004\"}],\"referenceNumber\":2,\"referencePositions\":[\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:06.673007+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c621b7373f2a6fa91b908243cb91d5f7c41394ff382a16440790296873fffe79",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0H2X6L3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "entry_version": 49,
  "evidence_id": "H1",
  "excerpt": "ID   NADE_XANC8              Reviewed;         552 AA.\nAC   A0A0H2X6L3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-SEP-2015, sequence version 1.\nDT   28-JAN-2026, entry version 49.\nDE   RecName: Full=Glutamine-dependent NAD(+) synthetase {ECO:0000255|HAMAP-Rule:MF_02090};\nDE            EC=6.3.5.1 {ECO:0000255|HAMAP-Rule:MF_02090};\nDE   AltName: Full=NAD(+) synthase [glutamine-hydrolyzing] {ECO:0000255|HAMAP-Rule:MF_02090};\nDE   AltName: Full=NAD(+) synthetase {ECO:0000303|PubMed:38429435};\nDE            Short=NADS {ECO:0000303|PubMed:38429435};\nGN   Name=nadE {ECO:0000255|HAMAP-Rule:MF_02090};\nGN   OrderedLocusNames=XC_1067 {ECO:0000312|EMBL:AAY48137.1};\nOS   Xanthomonas campestris pv. campestris (strain 8004).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Lysobacterales; Lysobacteraceae; Xanthomonas.\nOX   NCBI_TaxID=314565;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "entry_version": 49,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   DISRUPTION PHENOTYPE.\nRC   STRAIN=8004;\nRX   PubMed=38429435; DOI=10.1038/s42003-024-05921-3;\nRA   Xu G., Ma J., Fang Q., Peng Q., Jiao X., Hu W., Zhao Q., Kong Y., Liu F.,\nRA   Shi X., Tang D.J., Tang J.L., Ming Z.;\nRT   \"Structural insights into Xanthomonas campestris pv. campestris NAD+\nRT   biosynthesis via the NAM salvage pathway.\";\nRL   Commun. Biol. 7:255-255(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49)

```json
{
  "entry_version": 49,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from\nCC       deamido-NAD(+) (L-Gln route): step 1/1. {ECO:0000255|HAMAP-\nCC       Rule:MF_02090}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:10.555808+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fb3a35bb9946c1cd8f5bc8cbdbcf89a05f7652dac19292f276cf608a43a2cb41",
  "url": "https://rest.uniprot.org/unisave/A0A0H2X6L3?format=txt&versions=49"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 51. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
