# EC_number_0028

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0028.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 3.2.1.20

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPPLGVLLLLVALGHSTQGHRPLPIRKAHKFDWWERGNFYQIYPRSFKDSDGDGIGDLKGITQTIDYLKTIGIDGVWLSPIFKSPMNDFGYDISDFYAIQEEYGTMEDFEELAAKCASIGLKLILDFVPNHSSDEHEHFRLSEEGIEPYKDYYIWHSGVLDANGTRHPPSNWISVFRGSAWQWSDKRQQYYLHQFQKKQPDLNYRNPALVEEMKNVMRFWLNKGIAGFRIDALPYLFESEEVDGHYRDEPLSGQATDDPDNPAYLTHTETKDQPETYDMVHQWRQVVDEYTARDNFTRIILTEAYTAVQNMTRFYGTPAAPGAQIPFNFQLITLLTVNSTGRDFVNAVQSWTRAMPSGAIANWVLGNHDNSRIASRLGVARADLYNIALQTLPGIAVTYYGEEIAMVDQWISWNDTIDPAACNADPATYELYSRDPVRTPFQWSNGTNAGFSNASRTWLPVADGYRELNVAAQLAAPRSHLKTFMQLTAYRKRRLLAEGNFVLRTVGRDLVMYKRSVPGVGYVVVALNFGPEPATLPVASQFPGTGEHWLKVIASSLQAQPQAGTWINTRLYKLAPDSGIVLERLTGRNDLMT

[Multiple Choices]
A. 3.2.1.20
B. 3.2.1.8
C. 3.1.1.80
D. 5.3.3.21
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

> The matched sequence is annotated as a salivary alpha-glucosidase, EC 3.2.1.20, and its catalytic activity is explicitly described as hydrolysis of terminal non-reducing alpha-D-glucose residues. The annotation cites experimental evidence (ECO:0000269), though the underlying paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence has an N-terminal signal-peptide-like region followed by a large glycosidase-like enzyme domain, consistent with a secreted carbohydrate hydrolase. More specifically, its sequence is consistent with the alpha-glucosidase family: transferable family knowledge links that family to hydrolysis of terminal alpha-glucose residues (EC 3.2.1.20). That meaningfully favors A over the beta-xylanase alternative B, the esterase C, and the isomerase D. Sequence-based family recognition supports a prediction, not proof of exact substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A recognizable enzyme-family pattern provides a credible distinction among the offered EC numbers without requiring recall of this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered alternatives represent different reaction types, and the alpha-glucosidase family inference distinguishes A from the other choices.


### Important caveats

- The reviewer-only annotation is sequence-matched, but the evaluated model did not receive the accession or database record.
- The specific catalytic annotation cites experimental evidence; the sequence-family inference alone is probabilistic.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence has an N-terminal signal-peptide-like region followed by a large glycosidase-like enzyme domain, consistent with a secreted carbohydrate hydrolase. More specifically, its sequence is consistent with the alpha-glucosidase family: transferable family knowledge links that family to hydrolysis of terminal alpha-glucose residues (EC 3.2.1.20). That meaningfully favors A over the beta-xylanase alternative B, the esterase C, and the isomerase D. Sequence-based family recognition supports a prediction, not proof of exact substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A recognizable enzyme-family pattern provides a credible distinction among the offered EC numbers without requiring recall of this exact protein's annotation."
  },
  "case_id": "EC_number_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as a salivary alpha-glucosidase, EC 3.2.1.20, and its catalytic activity is explicitly described as hydrolysis of terminal non-reducing alpha-D-glucose residues. The annotation cites experimental evidence (ECO:0000269), though the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only annotation is sequence-matched, but the evaluated model did not receive the accession or database record.",
    "The specific catalytic annotation cites experimental evidence; the sequence-family inference alone is probabilistic."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives represent different reaction types, and the alpha-glucosidase family inference distinguishes A from the other choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as a salivary alpha-glucosidase, EC 3.2.1.20, and its catalytic activity is explicitly described as hydrolysis of terminal non-reducing alpha-D-glucose residues. The annotation cites experimental evidence (ECO:0000269), though the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence has an N-terminal signal-peptide-like region followed by a large glycosidase-like enzyme domain, consistent with a secreted carbohydrate hydrolase. More specifically, its sequence is consistent with the alpha-glucosidase family: transferable family knowledge links that family to hydrolysis of terminal alpha-glucose residues (EC 3.2.1.20). That meaningfully favors A over the beta-xylanase alternative B, the esterase C, and the isomerase D. Sequence-based family recognition supports a prediction, not proof of exact substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "A recognizable enzyme-family pattern provides a credible distinction among the offered EC numbers without requiring recall of this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered alternatives represent different reaction types, and the alpha-glucosidase family inference distinguishes A from the other choices."
  },
  "important_caveats": [
    "The reviewer-only annotation is sequence-matched, but the evaluated model did not receive the accession or database record.",
    "The specific catalytic annotation cites experimental evidence; the sequence-family inference alone is probabilistic."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q7PYT9 (MALT_ANOGA, Anopheles gambiae) confirms EC 3.2.1.20 (Salivary alpha-glucosidase) with experimental evidence (ECO:0000269, PubMed:38428508). The catalytic activity is 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' The sequence matches the benchmark input (593 aa, SHA256 matched). The annotation is based on a 2024 experimental study comparing mosquito salivary alpha-glucosidases.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple DxxDxD motifs, notably 'DFGYDISDF' and 'ATDDPDNPA', which are hallmark catalytic signatures of Glycoside Hydrolase family 31 (GH31) alpha-glucosidases. The first D in DxxDxD serves as the catalytic nucleophile. The N-terminal signal peptide (MPPLGVLLLLVALGHSTQG) indicates a secreted protein, consistent with a digestive/salivary enzyme. The ~600 aa multi-domain architecture (beta-sandwich + TIM-barrel-like domains) matches GH31. In contrast: (B) 3.2.1.8 endo-1,4-beta-xylanase (GH10/GH11) uses Glu-x-x-x-Glu-x-Asp catalytic residues and a (β/α)8 TIM barrel or β-jelly roll fold, not DxxDxD; (C) 3.1.1.80 pyrethroid hydrolase is an α/β-hydrolase with a G-x-S-x-G motif and Ser-His-Asp triad, absent here; (D) 5.3.3.21 oxidosqualene-lanosterol cyclase is a triterpene cyclase with DxxCTxxxD motifs, a completely different fold and EC class. The DxxDxD pattern is a well-established family-level feature transferable across GH31 members.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The DxxDxD catalytic motif is a widely recognized family-level signature for GH31 alpha-glucosidases, learnable from many homologous proteins. The signal peptide, domain architecture, and absence of esterase or cyclase motifs further eliminate alternatives. A knowledgeable model can distinguish all four options using conserved sequence features and family-level knowledge without needing the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different EC top-level classes (3.2 hydrolases/glycosidases, 3.1 esterases, 5.3 isomerases). Within 3.2.1.x, the DxxDxD motif specifically identifies alpha-glucosidase (GH31) versus xylanase (GH10/GH11). No ambiguity among the offered choices.


### Important caveats

- The UniProt annotation for this entry was added in 2025 based on a 2024 experimental study; the benchmark may have been constructed before this annotation existed, meaning the author's key may have relied on homology transfer rather than direct experimental annotation at construction time.
- The DxxDxD motif is necessary but not fully sufficient to prove alpha-glucosidase specificity over other GH31 members (e.g., alpha-galactosidases also in GH27 use different motifs, but GH31 is predominantly alpha-glucosidase).
- Sequence-based identification of GH31 from this sequence alone is robust given the multiple conserved motifs and domain architecture, but precise substrate linkage specificity (1->4 alpha-D-glucose) is harder to confirm from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple DxxDxD motifs, notably 'DFGYDISDF' and 'ATDDPDNPA', which are hallmark catalytic signatures of Glycoside Hydrolase family 31 (GH31) alpha-glucosidases. The first D in DxxDxD serves as the catalytic nucleophile. The N-terminal signal peptide (MPPLGVLLLLVALGHSTQG) indicates a secreted protein, consistent with a digestive/salivary enzyme. The ~600 aa multi-domain architecture (beta-sandwich + TIM-barrel-like domains) matches GH31. In contrast: (B) 3.2.1.8 endo-1,4-beta-xylanase (GH10/GH11) uses Glu-x-x-x-Glu-x-Asp catalytic residues and a (β/α)8 TIM barrel or β-jelly roll fold, not DxxDxD; (C) 3.1.1.80 pyrethroid hydrolase is an α/β-hydrolase with a G-x-S-x-G motif and Ser-His-Asp triad, absent here; (D) 5.3.3.21 oxidosqualene-lanosterol cyclase is a triterpene cyclase with DxxCTxxxD motifs, a completely different fold and EC class. The DxxDxD pattern is a well-established family-level feature transferable across GH31 members.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The DxxDxD catalytic motif is a widely recognized family-level signature for GH31 alpha-glucosidases, learnable from many homologous proteins. The signal peptide, domain architecture, and absence of esterase or cyclase motifs further eliminate alternatives. A knowledgeable model can distinguish all four options using conserved sequence features and family-level knowledge without needing the specific UniProt annotation for this exact protein."
  },
  "case_id": "EC_number_0028",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q7PYT9 (MALT_ANOGA, Anopheles gambiae) confirms EC 3.2.1.20 (Salivary alpha-glucosidase) with experimental evidence (ECO:0000269, PubMed:38428508). The catalytic activity is 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' The sequence matches the benchmark input (593 aa, SHA256 matched). The annotation is based on a 2024 experimental study comparing mosquito salivary alpha-glucosidases."
  },
  "important_caveats": [
    "The UniProt annotation for this entry was added in 2025 based on a 2024 experimental study; the benchmark may have been constructed before this annotation existed, meaning the author's key may have relied on homology transfer rather than direct experimental annotation at construction time.",
    "The DxxDxD motif is necessary but not fully sufficient to prove alpha-glucosidase specificity over other GH31 members (e.g., alpha-galactosidases also in GH27 use different motifs, but GH31 is predominantly alpha-glucosidase).",
    "Sequence-based identification of GH31 from this sequence alone is robust given the multiple conserved motifs and domain architecture, but precise substrate linkage specificity (1->4 alpha-D-glucose) is harder to confirm from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (3.2 hydrolases/glycosidases, 3.1 esterases, 5.3 isomerases). Within 3.2.1.x, the DxxDxD motif specifically identifies alpha-glucosidase (GH31) versus xylanase (GH10/GH11). No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0028",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q7PYT9 (MALT_ANOGA, Anopheles gambiae) confirms EC 3.2.1.20 (Salivary alpha-glucosidase) with experimental evidence (ECO:0000269, PubMed:38428508). The catalytic activity is 'Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.' The sequence matches the benchmark input (593 aa, SHA256 matched). The annotation is based on a 2024 experimental study comparing mosquito salivary alpha-glucosidases.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple DxxDxD motifs, notably 'DFGYDISDF' and 'ATDDPDNPA', which are hallmark catalytic signatures of Glycoside Hydrolase family 31 (GH31) alpha-glucosidases. The first D in DxxDxD serves as the catalytic nucleophile. The N-terminal signal peptide (MPPLGVLLLLVALGHSTQG) indicates a secreted protein, consistent with a digestive/salivary enzyme. The ~600 aa multi-domain architecture (beta-sandwich + TIM-barrel-like domains) matches GH31. In contrast: (B) 3.2.1.8 endo-1,4-beta-xylanase (GH10/GH11) uses Glu-x-x-x-Glu-x-Asp catalytic residues and a (β/α)8 TIM barrel or β-jelly roll fold, not DxxDxD; (C) 3.1.1.80 pyrethroid hydrolase is an α/β-hydrolase with a G-x-S-x-G motif and Ser-His-Asp triad, absent here; (D) 5.3.3.21 oxidosqualene-lanosterol cyclase is a triterpene cyclase with DxxCTxxxD motifs, a completely different fold and EC class. The DxxDxD pattern is a well-established family-level feature transferable across GH31 members.",
    "missing_item_specific_fact": "",
    "reason": "The DxxDxD catalytic motif is a widely recognized family-level signature for GH31 alpha-glucosidases, learnable from many homologous proteins. The signal peptide, domain architecture, and absence of esterase or cyclase motifs further eliminate alternatives. A knowledgeable model can distinguish all four options using conserved sequence features and family-level knowledge without needing the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different EC top-level classes (3.2 hydrolases/glycosidases, 3.1 esterases, 5.3 isomerases). Within 3.2.1.x, the DxxDxD motif specifically identifies alpha-glucosidase (GH31) versus xylanase (GH10/GH11). No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation for this entry was added in 2025 based on a 2024 experimental study; the benchmark may have been constructed before this annotation existed, meaning the author's key may have relied on homology transfer rather than direct experimental annotation at construction time.",
    "The DxxDxD motif is necessary but not fully sufficient to prove alpha-glucosidase specificity over other GH31 members (e.g., alpha-galactosidases also in GH27 use different motifs, but GH31 is predominantly alpha-glucosidase).",
    "Sequence-based identification of GH31 from this sequence alone is robust given the multiple conserved motifs and domain architecture, but precise substrate linkage specificity (1->4 alpha-D-glucose) is harder to confirm from sequence alone."
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
  "benchmark_sequence_length": 593,
  "benchmark_sequence_sha256": "b5c0d534d7a7b2a76bff2705c7926754dc64b40cdbcc8632b99a9db0d4f8a9b7",
  "current_entry_audit": {
    "entryVersion": 134,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-01-09",
    "sequenceVersion": 3
  },
  "current_record_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 593,
  "current_source_sequence_sha256": "b5c0d534d7a7b2a76bff2705c7926754dc64b40cdbcc8632b99a9db0d4f8a9b7",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 132,
      "exact_sequence_comparison": "matched",
      "sequence_version": 3
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q7PYT9",
  "selected_historical_entry_version": 132,
  "selected_historical_record_sha256": "de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052",
  "selected_historical_source_sequence_length": 593,
  "selected_historical_source_sequence_sha256": "b5c0d534d7a7b2a76bff2705c7926754dc64b40cdbcc8632b99a9db0d4f8a9b7",
  "selected_historical_version": {
    "accession": "Q7PYT9",
    "database": "Swiss-Prot",
    "entryVersion": 132,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MALT_ANOGA",
    "sequenceVersion": 3
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q7PYT9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:10.588074+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "url": "https://rest.uniprot.org/uniprotkb/Q7PYT9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":134,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-01-09\",\"sequenceVersion\":3}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:10.588074+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "url": "https://rest.uniprot.org/uniprotkb/Q7PYT9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"African malaria mosquito\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"EAA00998.3\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Nematocera\",\"Culicoidea\",\"Culicidae\",\"Anophelinae\",\"Anopheles\"],\"scientificName\":\"Anopheles gambiae\",\"taxonId\":7165}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:10.588074+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "url": "https://rest.uniprot.org/uniprotkb/Q7PYT9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.20\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"Salivary alpha-glucosidase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"value\":\"AnGluc\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:10.588074+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "url": "https://rest.uniprot.org/uniprotkb/Q7PYT9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.20\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38428508\",\"source\":\"PubMed\"}],\"name\":\"Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-glucose residues with release of alpha-D-glucose.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:10.588074+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "url": "https://rest.uniprot.org/uniprotkb/Q7PYT9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q7PYT9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Williams A.E.\",\"Gittis A.G.\",\"Botello K.\",\"Cruz P.\",\"Martin-Martin I.\",\"Valenzuela Leon P.C.\",\"Sumner B.\",\"Bonilla B.\",\"Calvo E.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38428508\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.ibmb.2024.104097\"}],\"citationType\":\"journal article\",\"firstPage\":\"104097\",\"id\":\"38428508\",\"journal\":\"Insect Biochem. Mol. Biol.\",\"lastPage\":\"104097\",\"publicationDate\":\"2024\",\"title\":\"Structural and functional comparisons of salivary alpha-glucosidases from the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex quinquefasciatus.\",\"volume\":\"167\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:10.588074+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b95ba5f84a3c800481a01173df1ae62cd4cae90bbd222bbb34ea446d40d2dc8d",
  "url": "https://rest.uniprot.org/uniprotkb/Q7PYT9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H1",
  "excerpt": "ID   MALT_ANOGA              Reviewed;         593 AA.\nAC   Q7PYT9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-JAN-2007, sequence version 3.\nDT   28-JAN-2026, entry version 132.\nDE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};\nDE            Short=AnGluc {ECO:0000303|PubMed:38428508};\nDE            EC=3.2.1.20 {ECO:0000269|PubMed:38428508};\nDE   Flags: Precursor;\nGN   Name=MAL1 {ECO:0000250|UniProtKB:P13080};\nGN   ORFNames=AgaP_AGAP002102 {ECO:0000312|EMBL:EAA00998.3};\nOS   Anopheles gambiae (African malaria mosquito).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Nematocera; Culicoidea; Culicidae;\nOC   Anophelinae; Anopheles.\nOX   NCBI_TaxID=7165 {ECO:0000312|EMBL:EAA00998.3};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:03.279027+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052",
  "url": "https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Salivary alpha-glucosidase {ECO:0000303|PubMed:38428508};\nDE            Short=AnGluc {ECO:0000303|PubMed:38428508};\nDE            EC=3.2.1.20 {ECO:0000269|PubMed:38428508};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:03.279027+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052",
  "url": "https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR\nRP   LOCATION, AND TISSUE SPECIFICITY.\nRX   PubMed=38428508; DOI=10.1016/j.ibmb.2024.104097;\nRA   Williams A.E., Gittis A.G., Botello K., Cruz P., Martin-Martin I.,\nRA   Valenzuela Leon P.C., Sumner B., Bonilla B., Calvo E.;\nRT   \"Structural and functional comparisons of salivary alpha-glucosidases from\nRT   the mosquito vectors Aedes aegypti, Anopheles gambiae, and Culex\nRT   quinquefasciatus.\";\nRL   Insect Biochem. Mol. Biol. 167:104097-104097(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:03.279027+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052",
  "url": "https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132)

```json
{
  "entry_version": 132,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=Hydrolysis of terminal, non-reducing (1->4)-linked alpha-D-\nCC         glucose residues with release of alpha-D-glucose.; EC=3.2.1.20;\nCC         Evidence={ECO:0000269|PubMed:38428508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:42:03.279027+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 3,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "de59e19c2630176f429b35ceca36f772399cba06a5d924df213abc4f4cd0c052",
  "url": "https://rest.uniprot.org/unisave/Q7PYT9?format=txt&versions=132"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 28. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
