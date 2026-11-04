# EC_number_0096

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0096.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 3.2.1.8

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVSFTTLLAGFVAVTGVLSAPTETVEVVDVEKRQTIGPGTGFNNGYYYSYWNDGHSGVTYTNGAGGSFSVNWANSGNFVGGKGWNPGSSSRVINFSGSYNPNGNSYLSVYGWSKNPLIEYYIVENFGTYNPSTGTTKLGEVTSDGSVYDIYRTQRVNQPSIIGTATFYQYWSVRRNHAPAARSRLRTTSNAWRNLGLTLGTLDYQIIAVEGYFSSGNANINVS

[Multiple Choices]
A. 3.2.1.8
B. 3.2.1.20
C. 1.1.1.1
D. 5.1.1.25
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

> The matched sequence's UniProt entry assigns EC 3.2.1.8 computationally via a PROSITE-ProRule, and separately records the xylan-hydrolysis reaction with experimental evidence (ECO:0000269).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal signal-peptide-like hydrophobic region followed by a small, aromatic-rich carbohydrate-active domain, consistent with a secreted fungal endo-xylanase. Fungal GH11 xylanases are compact proteins of roughly this size and catalyze endohydrolysis of beta-1,4-xylan linkages, matching EC 3.2.1.8 (A). That family-level inference distinguishes A from the offered alpha-glucosidase (B), alcohol dehydrogenase (C), and racemase (D).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable enzyme-family inference from the sequence meaningfully identifies the xylanase option; it does not require knowing this exact protein's database annotation. The inference is probabilistic, not an independent demonstration of catalytic activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, the sequence and likely secreted fungal xylanase family support A; the alternatives represent distinct enzyme activities.


### Important caveats

- The protein-family assignment from sequence is an inference; the reviewer-only experimental annotation provides stronger support for the recorded activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal signal-peptide-like hydrophobic region followed by a small, aromatic-rich carbohydrate-active domain, consistent with a secreted fungal endo-xylanase. Fungal GH11 xylanases are compact proteins of roughly this size and catalyze endohydrolysis of beta-1,4-xylan linkages, matching EC 3.2.1.8 (A). That family-level inference distinguishes A from the offered alpha-glucosidase (B), alcohol dehydrogenase (C), and racemase (D).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable enzyme-family inference from the sequence meaningfully identifies the xylanase option; it does not require knowing this exact protein's database annotation. The inference is probabilistic, not an independent demonstration of catalytic activity."
  },
  "case_id": "EC_number_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence's UniProt entry assigns EC 3.2.1.8 computationally via a PROSITE-ProRule, and separately records the xylan-hydrolysis reaction with experimental evidence (ECO:0000269)."
  },
  "important_caveats": [
    "The protein-family assignment from sequence is an inference; the reviewer-only experimental annotation provides stronger support for the recorded activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the sequence and likely secreted fungal xylanase family support A; the alternatives represent distinct enzyme activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence's UniProt entry assigns EC 3.2.1.8 computationally via a PROSITE-ProRule, and separately records the xylan-hydrolysis reaction with experimental evidence (ECO:0000269).",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal signal-peptide-like hydrophobic region followed by a small, aromatic-rich carbohydrate-active domain, consistent with a secreted fungal endo-xylanase. Fungal GH11 xylanases are compact proteins of roughly this size and catalyze endohydrolysis of beta-1,4-xylan linkages, matching EC 3.2.1.8 (A). That family-level inference distinguishes A from the offered alpha-glucosidase (B), alcohol dehydrogenase (C), and racemase (D).",
    "missing_item_specific_fact": "",
    "reason": "A transferable enzyme-family inference from the sequence meaningfully identifies the xylanase option; it does not require knowing this exact protein's database annotation. The inference is probabilistic, not an independent demonstration of catalytic activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, the sequence and likely secreted fungal xylanase family support A; the alternatives represent distinct enzyme activities."
  },
  "important_caveats": [
    "The protein-family assignment from sequence is an inference; the reviewer-only experimental annotation provides stronger support for the recorded activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q9UVF9 (sequence SHA256 match confirmed) is annotated EC 3.2.1.8 with both computational evidence (PROSITE-ProRule PRU01097, ECO:0000255) and experimental evidence (PubMed 16668223, ECO:0000269) confirming 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' Multiple independent PubMed references (10517825, 16666504, 16668223) support the xylanase activity. The EC assignment is well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is only 223 AA with an N-terminal signal peptide (MVSFTTLLAGFVAVTGVLSAPT), indicating a small secreted enzyme (~190 AA mature). This size and secretion pattern immediately eliminate C (alcohol dehydrogenase EC 1.1.1.1, typically 350-400+ AA with Rossmann fold and NAD-binding GxGxxG motif absent here) and D (glutamate racemase EC 5.1.1.25, ~350 AA TIM-barrel fold with catalytic Cys, absent here). It also eliminates B (alpha-glucuronidase EC 3.2.1.20, belonging to GH67/GH115 families, typically 500+ AA). The remaining choice A (endo-1,4-beta-xylanase EC 3.2.1.8, GH11 family) matches: GH11 xylanases are characteristically small (~180-220 AA mature), secreted, and aromatic-rich. The sequence shows abundant Tyr/Trp/Phe residues characteristic of the GH11 active-site cleft, and potential catalytic Glu residues (e.g., in 'KLGEVTSD' and 'IIAVEGY' segments) consistent with the two-Glu mechanism of GH11. A knowledgeable model recognizing GH11 family features (small size, secretion, aromatic cleft, catalytic Glu pair) can confidently select A over B, C, D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The small size (~223 AA with signal peptide), secreted nature, aromatic-rich character, and absence of motifs required by the other three enzyme classes (NAD-binding for ADH, TIM-barrel/Cys for racemase, large size for alpha-glucuronidase) allow a knowledgeable model to eliminate B, C, D using general protein-family knowledge and select A (GH11 xylanase) based on well-established family-level characteristics shared across many GH11 xylanases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent very different enzyme classes with distinct size, structural, and cofactor requirements. The small secreted protein with aromatic-rich character uniquely fits GH11 xylanase among the four choices.


### Important caveats

- The EC 3.2.1.8 assignment in UniProt is initially from PROSITE-ProRule (computational family match), but is corroborated by experimental activity data (PubMed 16668223).
- The protein is also known as 'ethylene-inducing xylanase' (EIX), which has elicitor activity beyond its catalytic xylanase function; the EC number refers specifically to the catalytic reaction.
- The PROSITE-ProRule PRU01097 is the GH11 xylanase profile; recognizing this family from sequence is a legitimate transferable-knowledge inference.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is only 223 AA with an N-terminal signal peptide (MVSFTTLLAGFVAVTGVLSAPT), indicating a small secreted enzyme (~190 AA mature). This size and secretion pattern immediately eliminate C (alcohol dehydrogenase EC 1.1.1.1, typically 350-400+ AA with Rossmann fold and NAD-binding GxGxxG motif absent here) and D (glutamate racemase EC 5.1.1.25, ~350 AA TIM-barrel fold with catalytic Cys, absent here). It also eliminates B (alpha-glucuronidase EC 3.2.1.20, belonging to GH67/GH115 families, typically 500+ AA). The remaining choice A (endo-1,4-beta-xylanase EC 3.2.1.8, GH11 family) matches: GH11 xylanases are characteristically small (~180-220 AA mature), secreted, and aromatic-rich. The sequence shows abundant Tyr/Trp/Phe residues characteristic of the GH11 active-site cleft, and potential catalytic Glu residues (e.g., in 'KLGEVTSD' and 'IIAVEGY' segments) consistent with the two-Glu mechanism of GH11. A knowledgeable model recognizing GH11 family features (small size, secretion, aromatic cleft, catalytic Glu pair) can confidently select A over B, C, D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The small size (~223 AA with signal peptide), secreted nature, aromatic-rich character, and absence of motifs required by the other three enzyme classes (NAD-binding for ADH, TIM-barrel/Cys for racemase, large size for alpha-glucuronidase) allow a knowledgeable model to eliminate B, C, D using general protein-family knowledge and select A (GH11 xylanase) based on well-established family-level characteristics shared across many GH11 xylanases."
  },
  "case_id": "EC_number_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "UniProt Q9UVF9 (sequence SHA256 match confirmed) is annotated EC 3.2.1.8 with both computational evidence (PROSITE-ProRule PRU01097, ECO:0000255) and experimental evidence (PubMed 16668223, ECO:0000269) confirming 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' Multiple independent PubMed references (10517825, 16666504, 16668223) support the xylanase activity. The EC assignment is well-supported."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment in UniProt is initially from PROSITE-ProRule (computational family match), but is corroborated by experimental activity data (PubMed 16668223).",
    "The protein is also known as 'ethylene-inducing xylanase' (EIX), which has elicitor activity beyond its catalytic xylanase function; the EC number refers specifically to the catalytic reaction.",
    "The PROSITE-ProRule PRU01097 is the GH11 xylanase profile; recognizing this family from sequence is a legitimate transferable-knowledge inference."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different enzyme classes with distinct size, structural, and cofactor requirements. The small secreted protein with aromatic-rich character uniquely fits GH11 xylanase among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q9UVF9 (sequence SHA256 match confirmed) is annotated EC 3.2.1.8 with both computational evidence (PROSITE-ProRule PRU01097, ECO:0000255) and experimental evidence (PubMed 16668223, ECO:0000269) confirming 'Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.' Multiple independent PubMed references (10517825, 16666504, 16668223) support the xylanase activity. The EC assignment is well-supported.",
    "evidence_ids": ["C4", "C5", "C8", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is only 223 AA with an N-terminal signal peptide (MVSFTTLLAGFVAVTGVLSAPT), indicating a small secreted enzyme (~190 AA mature). This size and secretion pattern immediately eliminate C (alcohol dehydrogenase EC 1.1.1.1, typically 350-400+ AA with Rossmann fold and NAD-binding GxGxxG motif absent here) and D (glutamate racemase EC 5.1.1.25, ~350 AA TIM-barrel fold with catalytic Cys, absent here). It also eliminates B (alpha-glucuronidase EC 3.2.1.20, belonging to GH67/GH115 families, typically 500+ AA). The remaining choice A (endo-1,4-beta-xylanase EC 3.2.1.8, GH11 family) matches: GH11 xylanases are characteristically small (~180-220 AA mature), secreted, and aromatic-rich. The sequence shows abundant Tyr/Trp/Phe residues characteristic of the GH11 active-site cleft, and potential catalytic Glu residues (e.g., in 'KLGEVTSD' and 'IIAVEGY' segments) consistent with the two-Glu mechanism of GH11. A knowledgeable model recognizing GH11 family features (small size, secretion, aromatic cleft, catalytic Glu pair) can confidently select A over B, C, D.",
    "missing_item_specific_fact": "",
    "reason": "The small size (~223 AA with signal peptide), secreted nature, aromatic-rich character, and absence of motifs required by the other three enzyme classes (NAD-binding for ADH, TIM-barrel/Cys for racemase, large size for alpha-glucuronidase) allow a knowledgeable model to eliminate B, C, D using general protein-family knowledge and select A (GH11 xylanase) based on well-established family-level characteristics shared across many GH11 xylanases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent very different enzyme classes with distinct size, structural, and cofactor requirements. The small secreted protein with aromatic-rich character uniquely fits GH11 xylanase among the four choices."
  },
  "important_caveats": [
    "The EC 3.2.1.8 assignment in UniProt is initially from PROSITE-ProRule (computational family match), but is corroborated by experimental activity data (PubMed 16668223).",
    "The protein is also known as 'ethylene-inducing xylanase' (EIX), which has elicitor activity beyond its catalytic xylanase function; the EC number refers specifically to the catalytic reaction.",
    "The PROSITE-ProRule PRU01097 is the GH11 xylanase profile; recognizing this family from sequence is a legitimate transferable-knowledge inference."
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
  "benchmark_sequence_length": 223,
  "benchmark_sequence_sha256": "9a39c4a2d30a03899daeb58151b43bb9f0d0029c8a5c524c3980d9d77838ae9d",
  "current_entry_audit": {
    "entryVersion": 93,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 223,
  "current_source_sequence_sha256": "9a39c4a2d30a03899daeb58151b43bb9f0d0029c8a5c524c3980d9d77838ae9d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 91,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9UVF9",
  "selected_historical_entry_version": 91,
  "selected_historical_record_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "selected_historical_source_sequence_length": 223,
  "selected_historical_source_sequence_sha256": "9a39c4a2d30a03899daeb58151b43bb9f0d0029c8a5c524c3980d9d77838ae9d",
  "selected_historical_version": {
    "accession": "Q9UVF9",
    "database": "Swiss-Prot",
    "entryVersion": 91,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX_HYPRU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9UVF9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":93,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Trichoderma viride\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Trichoderma\"],\"scientificName\":\"Hypocrea rufa\",\"taxonId\":5547}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10517825\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16666504\",\"source\":\"PubMed\"}],\"value\":\"Ethylene biosynthesis-inducing factor\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"16666504\",\"source\":\"PubMed\"}],\"value\":\"EIF\"}]}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10517825\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10517825\",\"source\":\"PubMed\"}],\"value\":\"EIX\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.8\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"16668223\",\"source\":\"PubMed\"}],\"name\":\"Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Furman-Matarasso N.\",\"Cohen E.\",\"Du Q.\",\"Chejanovsky N.\",\"Hanania U.\",\"Avni A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10517825\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.121.2.345\"}],\"citationType\":\"journal article\",\"firstPage\":\"345\",\"id\":\"10517825\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"351\",\"publicationDate\":\"1999\",\"title\":\"A point mutation in the ethylene-inducing xylanase elicitor inhibits the beta-1-4-endoxylanase activity but not the elicitation activity.\",\"volume\":\"121\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"MUTAGENESIS OF GLU-86 AND GLU-177\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Fuchs Y.\",\"Saxena A.\",\"Gamble H.R.\",\"Anderson J.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16666504\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.89.1.138\"}],\"citationType\":\"journal article\",\"firstPage\":\"138\",\"id\":\"16666504\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"143\",\"publicationDate\":\"1989\",\"title\":\"Ethylene biosynthesis-inducing protein from cellulysin is an endoxylanase.\",\"volume\":\"89\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9UVF9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Dean J.F.\",\"Gross K.C.\",\"Anderson J.D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"16668223\"},{\"database\":\"DOI\",\"id\":\"10.1104/pp.96.2.571\"}],\"citationType\":\"journal article\",\"firstPage\":\"571\",\"id\":\"16668223\",\"journal\":\"Plant Physiol.\",\"lastPage\":\"576\",\"publicationDate\":\"1991\",\"title\":\"Ethylene Biosynthesis-Inducing Xylanase: III. Product Characterization.\",\"volume\":\"96\"},\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:25:29.394840+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc363fccbec97698792de8a94b84ee7388d03ddc4aa6d6a0260fbc7434c2a35c",
  "url": "https://rest.uniprot.org/uniprotkb/Q9UVF9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "entry_version": 91,
  "evidence_id": "H1",
  "excerpt": "ID   EIX_HYPRU               Reviewed;         223 AA.\nAC   Q9UVF9;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 91.\nDE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:10517825};\nDE            Short=EIX {ECO:0000303|PubMed:10517825};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:10517825};\nDE   AltName: Full=Ethylene biosynthesis-inducing factor {ECO:0000303|PubMed:16666504};\nDE            Short=EIF {ECO:0000303|PubMed:16666504};\nDE   Flags: Precursor;\nGN   Name=EIX {ECO:0000303|PubMed:10517825};\nOS   Hypocrea rufa (Trichoderma viride).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Trichoderma.\nOX   NCBI_TaxID=5547;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "entry_version": 91,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Ethylene-inducing xylanase {ECO:0000303|PubMed:10517825};\nDE            Short=EIX {ECO:0000303|PubMed:10517825};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX {ECO:0000303|PubMed:10517825};\nDE   AltName: Full=Ethylene biosynthesis-inducing factor {ECO:0000303|PubMed:16666504};\nDE            Short=EIF {ECO:0000303|PubMed:16666504};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "entry_version": 91,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, SUBCELLULAR LOCATION, AND MUTAGENESIS\nRP   OF GLU-86 AND GLU-177.\nRX   PubMed=10517825; DOI=10.1104/pp.121.2.345;\nRA   Furman-Matarasso N., Cohen E., Du Q., Chejanovsky N., Hanania U., Avni A.;\nRT   \"A point mutation in the ethylene-inducing xylanase elicitor inhibits the\nRT   beta-1-4-endoxylanase activity but not the elicitation activity.\";\nRL   Plant Physiol. 121:345-351(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "entry_version": 91,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=16666504; DOI=10.1104/pp.89.1.138;\nRA   Fuchs Y., Saxena A., Gamble H.R., Anderson J.D.;\nRT   \"Ethylene biosynthesis-inducing protein from cellulysin is an\nRT   endoxylanase.\";\nRL   Plant Physiol. 89:138-143(1989).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "entry_version": 91,
  "evidence_id": "H5",
  "excerpt": "RN   [5]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=16668223; DOI=10.1104/pp.96.2.571;\nRA   Dean J.F., Gross K.C., Anderson J.D.;\nRT   \"Ethylene Biosynthesis-Inducing Xylanase: III. Product Characterization.\";\nRL   Plant Physiol. 96:571-576(1991).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91)

```json
{
  "entry_version": 91,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Endohydrolysis of (1->4)-beta-D-xylosidic linkages in xylans.;\nCC         EC=3.2.1.8; Evidence={ECO:0000269|PubMed:16668223};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:50.576003+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 156-158",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "58405d88f8ea2ef78dd2cc137a7fa2fd8d879e249b7706495d0b0eeb486f7eac",
  "url": "https://rest.uniprot.org/unisave/Q9UVF9?format=txt&versions=91"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 96. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
