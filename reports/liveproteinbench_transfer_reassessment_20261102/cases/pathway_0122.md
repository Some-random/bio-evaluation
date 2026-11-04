# pathway_0122

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0122.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Purine metabolism

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MCGVLALILANQSSSAANDLHEALYVLQHRGQDAAGIATSTSSGHIHIRKKNGMAADVFQSGARLANLFGSMGIAHLRYPTAGGSANTEAQPFYVNSPYGICFAHNGNLINTVELRRYLDFEIHRHINSDSDSELMLNIFADELSETKKARVNTEDIFNGLSKMYQRCEGAWACTAMLAGFGVIGFRDAYGIRPLVMGSRPSSDGDGLDYMIASESIALDRLGFTNVRDIQPGEAVIVAKGAEPVFCQVAPRKSYTPDLFEYVYFARPDSVIDGISVYQSRQRMGRYLAARLLEVLGPEGIKEIDVVIPVPETSSPAAASVAHALNKPYCAGYIRNPYVFRTFIMPGQATRQKGVRRKLSAVKEEFKNRTILLVDDSIARGTTSREAISMAREAGVKKIIAACCSPEITYPHIYGIDLPSPHEMVAYERDNNDIAQNLGADRIVYQTLEDLQASCAEIARENDFQEPHTFENGVFSGQYVTPVPEGYFALLEKIRGTGRKEALDKSSKRL

[Multiple Choices]
A. Purine metabolism
B. Cofactor biosynthesis
C. CoA from (R)-pantothenate: step 3/5. .
D. peptidoglycan biosynthesis. .
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

> The sequence-matched UniProt annotation identifies the protein as phosphoribosylpyrophosphate amidotransferase and places it in de novo purine/IMP biosynthesis, supporting option A. The pathway annotation cites a publication; the excerpt alone does not establish that the pathway assignment was directly experimentally demonstrated.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a glutamine phosphoribosylpyrophosphate amidotransferase (PurF/ATase) family enzyme. Such enzymes use glutamine and PRPP in the first committed step of de novo purine biosynthesis, which distinguishes purine metabolism (A) from cofactor biosynthesis, CoA synthesis, and peptidoglycan biosynthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the conserved enzyme role provide a meaningful transferable inference from the sequence to the offered pathway choices. This does not require recalling the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The enzyme family’s canonical pathway is represented by option A; none of the other options describes its stated biosynthetic role.


### Important caveats

- The sequence-matched database pathway annotation is cited to a publication, but the supplied excerpts do not independently establish the experimental basis for every detail of that annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a glutamine phosphoribosylpyrophosphate amidotransferase (PurF/ATase) family enzyme. Such enzymes use glutamine and PRPP in the first committed step of de novo purine biosynthesis, which distinguishes purine metabolism (A) from cofactor biosynthesis, CoA synthesis, and peptidoglycan biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the conserved enzyme role provide a meaningful transferable inference from the sequence to the offered pathway choices. This does not require recalling the exact protein's database record."
  },
  "case_id": "pathway_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as phosphoribosylpyrophosphate amidotransferase and places it in de novo purine/IMP biosynthesis, supporting option A. The pathway annotation cites a publication; the excerpt alone does not establish that the pathway assignment was directly experimentally demonstrated."
  },
  "important_caveats": [
    "The sequence-matched database pathway annotation is cited to a publication, but the supplied excerpts do not independently establish the experimental basis for every detail of that annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme family’s canonical pathway is represented by option A; none of the other options describes its stated biosynthetic role."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as phosphoribosylpyrophosphate amidotransferase and places it in de novo purine/IMP biosynthesis, supporting option A. The pathway annotation cites a publication; the excerpt alone does not establish that the pathway assignment was directly experimentally demonstrated.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a glutamine phosphoribosylpyrophosphate amidotransferase (PurF/ATase) family enzyme. Such enzymes use glutamine and PRPP in the first committed step of de novo purine biosynthesis, which distinguishes purine metabolism (A) from cofactor biosynthesis, CoA synthesis, and peptidoglycan biosynthesis.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the conserved enzyme role provide a meaningful transferable inference from the sequence to the offered pathway choices. This does not require recalling the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The enzyme family’s canonical pathway is represented by option A; none of the other options describes its stated biosynthetic role."
  },
  "important_caveats": [
    "The sequence-matched database pathway annotation is cited to a publication, but the supplied excerpts do not independently establish the experimental basis for every detail of that annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7T8J1U7) explicitly annotates the pathway as 'Purine metabolism; IMP biosynthesis via de novo pathway; N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2' (evidence C5, H3). The enzyme is a glutamine phosphoribosylpyrophosphate amidotransferase (EC 2.4.2.14), which catalyzes the first committed step in de novo purine biosynthesis. The expected answer 'Purine metabolism' is directly supported by the database annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is ~510 amino acids and contains a glutamine amidotransferase (GAT) class I domain (identifiable by the Cys-His-Asp catalytic triad region and characteristic motifs around residues ~380-430, e.g., 'CCSPEITYPHIYGIDLPSPHEM...') combined with a PRPP-binding domain architecture. This specific GAT + PRPP-binding two-domain architecture at ~500-550 aa is the hallmark of the PRPP amidotransferase (PurF) family, which catalyzes the first committed step of de novo purine biosynthesis (PRPP → 5-phosphoribosylamine). This is well-established textbook knowledge transferable from canonical PurF enzymes in E. coli, yeast, and other organisms. Option C (CoA biosynthesis step 3/5) involves small enzymes like phosphopantothenoylcysteine synthetase (~200-300 aa) with entirely different domains. Option D (peptidoglycan biosynthesis) involves transglycosylases/transpeptidases with completely different architectures and is bacterial-specific. Option B (cofactor biosynthesis) is overly broad, but the specific PRPP+GAT combination is not characteristic of common cofactor pathways (folate, NAD, CoA) and instead uniquely identifies purine biosynthesis. A knowledgeable model recognizing the GAT+PRPP architecture would select purine metabolism over the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GAT + PRPP-binding two-domain architecture at ~510 aa is a well-characterized family-level signature (PRPP amidotransferase family) that a model can recognize from homologs and textbook knowledge of purine biosynthesis. This meaningfully distinguishes option A from the other three choices without requiring knowledge of this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-separated by domain architecture and pathway logic. CoA biosynthesis (C) and peptidoglycan biosynthesis (D) require entirely different enzyme families. Cofactor biosynthesis (B) is too broad and does not match the specific PRPP+GAT signature. Purine metabolism (A) is the clear best fit for a GAT+PRPP-binding enzyme of this size.


### Important caveats

- This protein (FrzK, EC 2.4.2.14) is part of the FR901483 immunosuppressant biosynthetic cluster in Cladobotryum sp., not the canonical PurF (EC 6.3.4.18). However, it catalyzes the same chemical reaction (PRPP + glutamine → 5-phosphoribosylamine) and is annotated in the purine metabolism pathway.
- The GAT domain is shared across many amidotransferases (CPS, FGAM synthase, etc.), so recognition of GAT alone is insufficient; the combination with a PRPP-binding domain at this molecular weight is what specifically points to purine biosynthesis.
- The model cannot know from the sequence alone that the organism is a fungus (which would exclude peptidoglycan biosynthesis), but the domain architecture argument independently rules out option D.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is ~510 amino acids and contains a glutamine amidotransferase (GAT) class I domain (identifiable by the Cys-His-Asp catalytic triad region and characteristic motifs around residues ~380-430, e.g., 'CCSPEITYPHIYGIDLPSPHEM...') combined with a PRPP-binding domain architecture. This specific GAT + PRPP-binding two-domain architecture at ~500-550 aa is the hallmark of the PRPP amidotransferase (PurF) family, which catalyzes the first committed step of de novo purine biosynthesis (PRPP → 5-phosphoribosylamine). This is well-established textbook knowledge transferable from canonical PurF enzymes in E. coli, yeast, and other organisms. Option C (CoA biosynthesis step 3/5) involves small enzymes like phosphopantothenoylcysteine synthetase (~200-300 aa) with entirely different domains. Option D (peptidoglycan biosynthesis) involves transglycosylases/transpeptidases with completely different architectures and is bacterial-specific. Option B (cofactor biosynthesis) is overly broad, but the specific PRPP+GAT combination is not characteristic of common cofactor pathways (folate, NAD, CoA) and instead uniquely identifies purine biosynthesis. A knowledgeable model recognizing the GAT+PRPP architecture would select purine metabolism over the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GAT + PRPP-binding two-domain architecture at ~510 aa is a well-characterized family-level signature (PRPP amidotransferase family) that a model can recognize from homologs and textbook knowledge of purine biosynthesis. This meaningfully distinguishes option A from the other three choices without requiring knowledge of this exact protein's annotation."
  },
  "case_id": "pathway_0122",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8J1U7) explicitly annotates the pathway as 'Purine metabolism; IMP biosynthesis via de novo pathway; N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2' (evidence C5, H3). The enzyme is a glutamine phosphoribosylpyrophosphate amidotransferase (EC 2.4.2.14), which catalyzes the first committed step in de novo purine biosynthesis. The expected answer 'Purine metabolism' is directly supported by the database annotation."
  },
  "important_caveats": [
    "This protein (FrzK, EC 2.4.2.14) is part of the FR901483 immunosuppressant biosynthetic cluster in Cladobotryum sp., not the canonical PurF (EC 6.3.4.18). However, it catalyzes the same chemical reaction (PRPP + glutamine → 5-phosphoribosylamine) and is annotated in the purine metabolism pathway.",
    "The GAT domain is shared across many amidotransferases (CPS, FGAM synthase, etc.), so recognition of GAT alone is insufficient; the combination with a PRPP-binding domain at this molecular weight is what specifically points to purine biosynthesis.",
    "The model cannot know from the sequence alone that the organism is a fungus (which would exclude peptidoglycan biosynthesis), but the domain architecture argument independently rules out option D."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by domain architecture and pathway logic. CoA biosynthesis (C) and peptidoglycan biosynthesis (D) require entirely different enzyme families. Cofactor biosynthesis (B) is too broad and does not match the specific PRPP+GAT signature. Purine metabolism (A) is the clear best fit for a GAT+PRPP-binding enzyme of this size."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0122",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8J1U7) explicitly annotates the pathway as 'Purine metabolism; IMP biosynthesis via de novo pathway; N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2' (evidence C5, H3). The enzyme is a glutamine phosphoribosylpyrophosphate amidotransferase (EC 2.4.2.14), which catalyzes the first committed step in de novo purine biosynthesis. The expected answer 'Purine metabolism' is directly supported by the database annotation.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is ~510 amino acids and contains a glutamine amidotransferase (GAT) class I domain (identifiable by the Cys-His-Asp catalytic triad region and characteristic motifs around residues ~380-430, e.g., 'CCSPEITYPHIYGIDLPSPHEM...') combined with a PRPP-binding domain architecture. This specific GAT + PRPP-binding two-domain architecture at ~500-550 aa is the hallmark of the PRPP amidotransferase (PurF) family, which catalyzes the first committed step of de novo purine biosynthesis (PRPP → 5-phosphoribosylamine). This is well-established textbook knowledge transferable from canonical PurF enzymes in E. coli, yeast, and other organisms. Option C (CoA biosynthesis step 3/5) involves small enzymes like phosphopantothenoylcysteine synthetase (~200-300 aa) with entirely different domains. Option D (peptidoglycan biosynthesis) involves transglycosylases/transpeptidases with completely different architectures and is bacterial-specific. Option B (cofactor biosynthesis) is overly broad, but the specific PRPP+GAT combination is not characteristic of common cofactor pathways (folate, NAD, CoA) and instead uniquely identifies purine biosynthesis. A knowledgeable model recognizing the GAT+PRPP architecture would select purine metabolism over the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The GAT + PRPP-binding two-domain architecture at ~510 aa is a well-characterized family-level signature (PRPP amidotransferase family) that a model can recognize from homologs and textbook knowledge of purine biosynthesis. This meaningfully distinguishes option A from the other three choices without requiring knowledge of this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-separated by domain architecture and pathway logic. CoA biosynthesis (C) and peptidoglycan biosynthesis (D) require entirely different enzyme families. Cofactor biosynthesis (B) is too broad and does not match the specific PRPP+GAT signature. Purine metabolism (A) is the clear best fit for a GAT+PRPP-binding enzyme of this size."
  },
  "important_caveats": [
    "This protein (FrzK, EC 2.4.2.14) is part of the FR901483 immunosuppressant biosynthetic cluster in Cladobotryum sp., not the canonical PurF (EC 6.3.4.18). However, it catalyzes the same chemical reaction (PRPP + glutamine → 5-phosphoribosylamine) and is annotated in the purine metabolism pathway.",
    "The GAT domain is shared across many amidotransferases (CPS, FGAM synthase, etc.), so recognition of GAT alone is insufficient; the combination with a PRPP-binding domain at this molecular weight is what specifically points to purine biosynthesis.",
    "The model cannot know from the sequence alone that the organism is a fungus (which would exclude peptidoglycan biosynthesis), but the domain architecture argument independently rules out option D."
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
  "benchmark_sequence_length": 510,
  "benchmark_sequence_sha256": "44dc44e51fdf196ccecccc1dbeec4ed51df88981f809d29be8495d6c59ba2224",
  "current_entry_audit": {
    "entryVersion": 18,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 510,
  "current_source_sequence_sha256": "44dc44e51fdf196ccecccc1dbeec4ed51df88981f809d29be8495d6c59ba2224",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 16,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A7T8J1U7",
  "selected_historical_entry_version": 16,
  "selected_historical_record_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "selected_historical_source_sequence_length": 510,
  "selected_historical_source_sequence_sha256": "44dc44e51fdf196ccecccc1dbeec4ed51df88981f809d29be8495d6c59ba2224",
  "selected_historical_version": {
    "accession": "A0A7T8J1U7",
    "database": "Swiss-Prot",
    "entryVersion": 16,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZK_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8J1U7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":18,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis clusters protein K\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Glutamine phosphoribosylpyrophosphate amidotransferase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"2.4.2.14\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Phosphoribosylpyrophosphate amidotransferase FrzK\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"ATase FrzK\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Purine metabolism; IMP biosynthesis via de novo pathway; N(1)-(5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-diphosphate: step 1/2\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:51.826168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "56665e1cd9e3380e3faeac05a356479129623641a0ef275c9308eeccf948063d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8J1U7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H1",
  "excerpt": "ID   FRZK_CLASX              Reviewed;         510 AA.\nAC   A0A7T8J1U7;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 16.\nDE   RecName: Full=Phosphoribosylpyrophosphate amidotransferase FrzK {ECO:0000303|PubMed:33372776};\nDE            Short=ATase FrzK {ECO:0000303|PubMed:33372776};\nDE            EC=2.4.2.14 {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis clusters protein K {ECO:0000303|PubMed:33372776};\nDE   AltName: Full=Glutamine phosphoribosylpyrophosphate amidotransferase {ECO:0000303|PubMed:33372776};\nGN   Name=FrzK {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], AND FUNCTION.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Purine metabolism; IMP biosynthesis via de novo pathway; N(1)-\nCC       (5-phospho-D-ribosyl)glycinamide from 5-phospho-alpha-D-ribose 1-\nCC       diphosphate: step 1/2. {ECO:0000305|PubMed:33372776}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:55.036238+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "578ee5dbb88bc40f60a644a1dc0fae09acdb5d05f79fe55109621fabea2329a5",
  "url": "https://rest.uniprot.org/unisave/A0A7T8J1U7?format=txt&versions=16"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 122. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
