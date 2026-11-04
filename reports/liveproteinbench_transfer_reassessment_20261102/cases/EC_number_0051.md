# EC_number_0051

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0051.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.1.1.27

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGNEEAFTFALAMATGSFANMVLRAVVELDVFEIMKRAGPGTHLSAAEIAAHLPTKNPDANAMLDRMLRVLAGYEVLSCSNRSLPNGQVERLYGLSPVSQFFTKSEDGASLAPLCLLNQDKVYWESWYHLKDAVLDGGIAFNRAHNLTLYEYAGIDDRFNKVFNDGMSGCSTTIMKKMVENYKGFEGVSTLVDVAGGIGKNLNMIISKYPTIKGINFDLPHVIKDAPRCRGVENIGGDMFISVPQGDAIFIKWICCDWNDEHCLKFLKNCYAALPDHGKVILYEFIFPKASETSYAARVILNIDAVTLATVVGGRIRTEAEFEALAKGAGFEGFKMAYSTSEVDAVMEFLKKK

[Multiple Choices]
A. 2.1.1.395
B. 2.1.1.27
C. 2.3.1.319
D. 5.1.1.24
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

> The sequence-matched UniProt record assigns EC 2.1.1.27 and reports an experimentally evidenced tyramine N-methylation reaction for this protein. This supports the keyed answer, though the record also reports activity on other substrates.

Citations as saved: [C4](#evidence-c4), [C7](#evidence-c7).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a SAM-dependent methyltransferase, which meaningfully favors the methyltransferase choices over the acyltransferase and racemase choices. But both A and B are methyltransferases, and general methyltransferase-family features do not establish this protein's specific N-methylation activity or the exact EC assignment.


**Missing item-specific fact**

> Whether this exact protein catalyzes the reaction classified as EC 2.1.1.27, rather than the reaction represented by the other methyltransferase option.


**Reason**

> Transferable sequence and family knowledge can narrow the choices to methyltransferases, but distinguishing the two methyltransferase EC numbers requires substrate-specific functional information not given in the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports B; no other offered option is established as a defensible exact EC assignment.


### Important caveats

- The sequence match supports applying the cited record to this protein, but the record's annotations are reviewer-only evidence and were not available in the original input.
- The protein is reported to act on multiple substrates; support for EC 2.1.1.27 does not imply exclusive activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a SAM-dependent methyltransferase, which meaningfully favors the methyltransferase choices over the acyltransferase and racemase choices. But both A and B are methyltransferases, and general methyltransferase-family features do not establish this protein's specific N-methylation activity or the exact EC assignment.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this exact protein catalyzes the reaction classified as EC 2.1.1.27, rather than the reaction represented by the other methyltransferase option.",
    "reason": "Transferable sequence and family knowledge can narrow the choices to methyltransferases, but distinguishing the two methyltransferase EC numbers requires substrate-specific functional information not given in the original input."
  },
  "case_id": "EC_number_0051",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C7"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.1.1.27 and reports an experimentally evidenced tyramine N-methylation reaction for this protein. This supports the keyed answer, though the record also reports activity on other substrates."
  },
  "important_caveats": [
    "The sequence match supports applying the cited record to this protein, but the record's annotations are reviewer-only evidence and were not available in the original input.",
    "The protein is reported to act on multiple substrates; support for EC 2.1.1.27 does not imply exclusive activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; no other offered option is established as a defensible exact EC assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0051",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.1.1.27 and reports an experimentally evidenced tyramine N-methylation reaction for this protein. This supports the keyed answer, though the record also reports activity on other substrates.",
    "evidence_ids": ["C4", "C7"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a SAM-dependent methyltransferase, which meaningfully favors the methyltransferase choices over the acyltransferase and racemase choices. But both A and B are methyltransferases, and general methyltransferase-family features do not establish this protein's specific N-methylation activity or the exact EC assignment.",
    "missing_item_specific_fact": "Whether this exact protein catalyzes the reaction classified as EC 2.1.1.27, rather than the reaction represented by the other methyltransferase option.",
    "reason": "Transferable sequence and family knowledge can narrow the choices to methyltransferases, but distinguishing the two methyltransferase EC numbers requires substrate-specific functional information not given in the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports B; no other offered option is established as a defensible exact EC assignment."
  },
  "important_caveats": [
    "The sequence match supports applying the cited record to this protein, but the record's annotations are reviewer-only evidence and were not available in the original input.",
    "The protein is reported to act on multiple substrates; support for EC 2.1.1.27 does not imply exclusive activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AA51VIL5 (NMT2_LOPWI) explicitly annotates EC 2.1.1.27 with both PROSITE-ProRule (ECO:0000255) and experimental evidence (ECO:0000269, PubMed:37675639). The catalytic activity 'tyramine + SAM → N-methyltyramine + SAH + H+' is directly tagged with EC=2.1.1.27. The sequence matches (353 AA, SHA256 confirmed). The experimental paper (Watkins et al. 2023, Plant J.) demonstrated N-methyltransferase activity on phenethylamine substrates.

Citations as saved: [C4](#evidence-c4), [C7](#evidence-c7), [H2](#evidence-h2), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains the VAGGxG SAM-binding motif and overall fold characteristic of Class I SAM-dependent methyltransferases, which reasonably eliminates D (5.1.1.24, an isomerase) and likely C (2.3.1.319, an acyltransferase). However, both remaining options A (2.1.1.395) and B (2.1.1.27) are N-methyltransferases (EC 2.1.1.x). Distinguishing between two specific N-methyltransferase EC numbers requires knowledge of the exact substrate specificity (phenylethanolamine/phenethylamine N-methylation for 2.1.1.27 vs. whatever 2.1.1.395 catalyzes). The plant OMT/NMT family fold and SAM-binding motif are shared across hundreds of methyltransferases and do not encode the specific substrate position or identity that determines which EC 2.1.1.xxx number applies. The PROSITE-ProRule PRU01020 annotation is for the generic SAM-dependent methyltransferase motif and does not itself distinguish 2.1.1.27 from 2.1.1.395.


**Missing item-specific fact**

> The specific EC number assignment for this exact enzyme's substrate specificity (N-methylation of phenethylamines like tyramine/mescaline → EC 2.1.1.27) versus whatever reaction EC 2.1.1.395 describes. This is a database annotation fact about this particular protein that cannot be derived from general plant OMT/NMT family knowledge, as both EC numbers fall within the same N-methyltransferase subclass and share the same structural fold.


**Reason**

> While sequence motifs (VAGGxG, SAM-binding fold) confidently identify this as a methyltransferase and eliminate the isomerase and acyltransferase options, the critical discrimination between the two N-methyltransferase EC numbers (A: 2.1.1.395 vs B: 2.1.1.27) requires knowing the specific substrate/reaction assignment for this exact protein. Transferable knowledge of plant OMT/NMT families identifies the broad class but cannot resolve which specific EC 2.1.1.xxx number applies without the experimental substrate-specificity data from PubMed:37675639 or the database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While A and B are both N-methyltransferases, the UniProt annotation with experimental evidence clearly supports B (2.1.1.27). The distinction between A and B, though difficult from sequence alone, has a definitive experimental answer. No other option is defensible given the SAM-binding motif evidence.


### Important caveats

- EC 2.1.1.27 is traditionally 'phenylethanolamine N-methyltransferase' (PNMT) in animal biochemistry (converting norepinephrine to epinephrine). Its assignment to a plant N-methyltransferase acting on tyramine/mescaline is based on the PROSITE-ProRule computational annotation plus experimental demonstration of N-methyltransferase activity on phenethylamine substrates.
- The entry was first released in 2025 (Swiss-Prot), meaning this EC assignment is relatively new and the PROSITE-ProRule annotation (PRU01020) is a generic SAM-methyltransferase motif, not a specific discriminator for EC 2.1.1.27.
- EC 2.1.1.395 is a very recently assigned, highly specific EC number whose exact definition was not independently verified by the reviewer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the VAGGxG SAM-binding motif and overall fold characteristic of Class I SAM-dependent methyltransferases, which reasonably eliminates D (5.1.1.24, an isomerase) and likely C (2.3.1.319, an acyltransferase). However, both remaining options A (2.1.1.395) and B (2.1.1.27) are N-methyltransferases (EC 2.1.1.x). Distinguishing between two specific N-methyltransferase EC numbers requires knowledge of the exact substrate specificity (phenylethanolamine/phenethylamine N-methylation for 2.1.1.27 vs. whatever 2.1.1.395 catalyzes). The plant OMT/NMT family fold and SAM-binding motif are shared across hundreds of methyltransferases and do not encode the specific substrate position or identity that determines which EC 2.1.1.xxx number applies. The PROSITE-ProRule PRU01020 annotation is for the generic SAM-dependent methyltransferase motif and does not itself distinguish 2.1.1.27 from 2.1.1.395.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific EC number assignment for this exact enzyme's substrate specificity (N-methylation of phenethylamines like tyramine/mescaline → EC 2.1.1.27) versus whatever reaction EC 2.1.1.395 describes. This is a database annotation fact about this particular protein that cannot be derived from general plant OMT/NMT family knowledge, as both EC numbers fall within the same N-methyltransferase subclass and share the same structural fold.",
    "reason": "While sequence motifs (VAGGxG, SAM-binding fold) confidently identify this as a methyltransferase and eliminate the isomerase and acyltransferase options, the critical discrimination between the two N-methyltransferase EC numbers (A: 2.1.1.395 vs B: 2.1.1.27) requires knowing the specific substrate/reaction assignment for this exact protein. Transferable knowledge of plant OMT/NMT families identifies the broad class but cannot resolve which specific EC 2.1.1.xxx number applies without the experimental substrate-specificity data from PubMed:37675639 or the database annotation."
  },
  "case_id": "EC_number_0051",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C7",
      "H2",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AA51VIL5 (NMT2_LOPWI) explicitly annotates EC 2.1.1.27 with both PROSITE-ProRule (ECO:0000255) and experimental evidence (ECO:0000269, PubMed:37675639). The catalytic activity 'tyramine + SAM → N-methyltyramine + SAH + H+' is directly tagged with EC=2.1.1.27. The sequence matches (353 AA, SHA256 confirmed). The experimental paper (Watkins et al. 2023, Plant J.) demonstrated N-methyltransferase activity on phenethylamine substrates."
  },
  "important_caveats": [
    "EC 2.1.1.27 is traditionally 'phenylethanolamine N-methyltransferase' (PNMT) in animal biochemistry (converting norepinephrine to epinephrine). Its assignment to a plant N-methyltransferase acting on tyramine/mescaline is based on the PROSITE-ProRule computational annotation plus experimental demonstration of N-methyltransferase activity on phenethylamine substrates.",
    "The entry was first released in 2025 (Swiss-Prot), meaning this EC assignment is relatively new and the PROSITE-ProRule annotation (PRU01020) is a generic SAM-methyltransferase motif, not a specific discriminator for EC 2.1.1.27.",
    "EC 2.1.1.395 is a very recently assigned, highly specific EC number whose exact definition was not independently verified by the reviewer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A and B are both N-methyltransferases, the UniProt annotation with experimental evidence clearly supports B (2.1.1.27). The distinction between A and B, though difficult from sequence alone, has a definitive experimental answer. No other option is defensible given the SAM-binding motif evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0051",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AA51VIL5 (NMT2_LOPWI) explicitly annotates EC 2.1.1.27 with both PROSITE-ProRule (ECO:0000255) and experimental evidence (ECO:0000269, PubMed:37675639). The catalytic activity 'tyramine + SAM → N-methyltyramine + SAH + H+' is directly tagged with EC=2.1.1.27. The sequence matches (353 AA, SHA256 confirmed). The experimental paper (Watkins et al. 2023, Plant J.) demonstrated N-methyltransferase activity on phenethylamine substrates.",
    "evidence_ids": ["C4", "C7", "H2", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains the VAGGxG SAM-binding motif and overall fold characteristic of Class I SAM-dependent methyltransferases, which reasonably eliminates D (5.1.1.24, an isomerase) and likely C (2.3.1.319, an acyltransferase). However, both remaining options A (2.1.1.395) and B (2.1.1.27) are N-methyltransferases (EC 2.1.1.x). Distinguishing between two specific N-methyltransferase EC numbers requires knowledge of the exact substrate specificity (phenylethanolamine/phenethylamine N-methylation for 2.1.1.27 vs. whatever 2.1.1.395 catalyzes). The plant OMT/NMT family fold and SAM-binding motif are shared across hundreds of methyltransferases and do not encode the specific substrate position or identity that determines which EC 2.1.1.xxx number applies. The PROSITE-ProRule PRU01020 annotation is for the generic SAM-dependent methyltransferase motif and does not itself distinguish 2.1.1.27 from 2.1.1.395.",
    "missing_item_specific_fact": "The specific EC number assignment for this exact enzyme's substrate specificity (N-methylation of phenethylamines like tyramine/mescaline → EC 2.1.1.27) versus whatever reaction EC 2.1.1.395 describes. This is a database annotation fact about this particular protein that cannot be derived from general plant OMT/NMT family knowledge, as both EC numbers fall within the same N-methyltransferase subclass and share the same structural fold.",
    "reason": "While sequence motifs (VAGGxG, SAM-binding fold) confidently identify this as a methyltransferase and eliminate the isomerase and acyltransferase options, the critical discrimination between the two N-methyltransferase EC numbers (A: 2.1.1.395 vs B: 2.1.1.27) requires knowing the specific substrate/reaction assignment for this exact protein. Transferable knowledge of plant OMT/NMT families identifies the broad class but cannot resolve which specific EC 2.1.1.xxx number applies without the experimental substrate-specificity data from PubMed:37675639 or the database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While A and B are both N-methyltransferases, the UniProt annotation with experimental evidence clearly supports B (2.1.1.27). The distinction between A and B, though difficult from sequence alone, has a definitive experimental answer. No other option is defensible given the SAM-binding motif evidence."
  },
  "important_caveats": [
    "EC 2.1.1.27 is traditionally 'phenylethanolamine N-methyltransferase' (PNMT) in animal biochemistry (converting norepinephrine to epinephrine). Its assignment to a plant N-methyltransferase acting on tyramine/mescaline is based on the PROSITE-ProRule computational annotation plus experimental demonstration of N-methyltransferase activity on phenethylamine substrates.",
    "The entry was first released in 2025 (Swiss-Prot), meaning this EC assignment is relatively new and the PROSITE-ProRule annotation (PRU01020) is a generic SAM-methyltransferase motif, not a specific discriminator for EC 2.1.1.27.",
    "EC 2.1.1.395 is a very recently assigned, highly specific EC number whose exact definition was not independently verified by the reviewer."
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
  "benchmark_sequence_length": 353,
  "benchmark_sequence_sha256": "8005b9fd67d4f514f3757ccdbcf93619b77c547d65cf8692453380c6d4694638",
  "current_entry_audit": {
    "entryVersion": 12,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2024-01-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "963ca8f6d2aaca7f8a6e322ef5ff232476097d3fd58ca4bf3478362516330c70",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 353,
  "current_source_sequence_sha256": "8005b9fd67d4f514f3757ccdbcf93619b77c547d65cf8692453380c6d4694638",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 10,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AA51VIL5",
  "selected_historical_entry_version": 10,
  "selected_historical_record_sha256": "69c40863ae76ff5400002524808d001fc829f5326ea095f02e4c5b528c954b0f",
  "selected_historical_source_sequence_length": 353,
  "selected_historical_source_sequence_sha256": "8005b9fd67d4f514f3757ccdbcf93619b77c547d65cf8692453380c6d4694638",
  "selected_historical_version": {
    "accession": "A0AA51VIL5",
    "database": "Swiss-Prot",
    "entryVersion": 10,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NMT2_LOPWI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AA51VIL5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:19.727496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "963ca8f6d2aaca7f8a6e322ef5ff232476097d3fd58ca4bf3478362516330c70",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":12,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2024-01-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:19.727496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "963ca8f6d2aaca7f8a6e322ef5ff232476097d3fd58ca4bf3478362516330c70",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Peyote\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Cactineae\",\"Cactaceae\",\"Cactoideae\",\"Cacteae\",\"Lophophora\"],\"scientificName\":\"Lophophora williamsii\",\"synonyms\":[\"Echinocactus williamsii\"],\"taxonId\":130138}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:19.727496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "963ca8f6d2aaca7f8a6e322ef5ff232476097d3fd58ca4bf3478362516330c70",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"LwOMT3\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.27\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"N-methyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"LwNMT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:19.727496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "963ca8f6d2aaca7f8a6e322ef5ff232476097d3fd58ca4bf3478362516330c70",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81004\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"name\":\"3-methoxytyramine + S-adenosyl-L-methionine = N-methyl-3-methoxytyramine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81003\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:192089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231773\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:19.727496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "963ca8f6d2aaca7f8a6e322ef5ff232476097d3fd58ca4bf3478362516330c70",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81036\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"name\":\"mescaline + S-adenosyl-L-methionine = N-methylmescaline + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81035\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231762\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231781\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:26:19.727496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "963ca8f6d2aaca7f8a6e322ef5ff232476097d3fd58ca4bf3478362516330c70",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:14866\"}}],\"reaction\":{\"ecNumber\":\"2.1.1.27\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"name\":\"tyramine + S-adenosyl-L-methionine = N-methyltyramine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:14865\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58155\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:327995\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:26:19.727496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "963ca8f6d2aaca7f8a6e322ef5ff232476097d3fd58ca4bf3478362516330c70",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81028\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"name\":\"4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81027\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231768\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231777\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:26:19.727496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "963ca8f6d2aaca7f8a6e322ef5ff232476097d3fd58ca4bf3478362516330c70",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81020\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"name\":\"3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57856\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231769\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231779\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:26:19.727496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "963ca8f6d2aaca7f8a6e322ef5ff232476097d3fd58ca4bf3478362516330c70",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Watkins J.L.\",\"Li Q.\",\"Yeaman S.\",\"Facchini P.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37675639\"},{\"database\":\"DOI\",\"id\":\"10.1111/tpj.16447\"}],\"citationType\":\"journal article\",\"firstPage\":\"635\",\"id\":\"37675639\",\"journal\":\"Plant J.\",\"lastPage\":\"649\",\"publicationDate\":\"2023\",\"title\":\"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora williamsii).\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WMX25281.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Jourdaniana\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"TISSUE SPECIFICITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:19.727496+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "963ca8f6d2aaca7f8a6e322ef5ff232476097d3fd58ca4bf3478362516330c70",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51VIL5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H1",
  "excerpt": "ID   NMT2_LOPWI              Reviewed;         353 AA.\nAC   A0AA51VIL5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JAN-2024, sequence version 1.\nDT   28-JAN-2026, entry version 10.\nDE   RecName: Full=N-methyltransferase {ECO:0000303|PubMed:37675639};\nDE            Short=LwNMT {ECO:0000303|PubMed:37675639};\nDE            EC=2.1.1.27 {ECO:0000255|PROSITE-ProRule:PRU01020, ECO:0000269|PubMed:37675639};\nDE   AltName: Full=O-methyltransferase 3 {ECO:0000303|PubMed:37675639};\nDE            Short=LwOMT3 {ECO:0000303|PubMed:37675639};\nGN   Name=NMT {ECO:0000303|PubMed:37675639};\nGN   Synonyms=OMT3 {ECO:0000303|PubMed:37675639};\nOS   Lophophora williamsii (Peyote) (Echinocactus williamsii).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Cactineae; Cactaceae; Cactoideae; Cacteae; Lophophora.\nOX   NCBI_TaxID=130138;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:22.219060+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "69c40863ae76ff5400002524808d001fc829f5326ea095f02e4c5b528c954b0f",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=N-methyltransferase {ECO:0000303|PubMed:37675639};\nDE            Short=LwNMT {ECO:0000303|PubMed:37675639};\nDE            EC=2.1.1.27 {ECO:0000255|PROSITE-ProRule:PRU01020, ECO:0000269|PubMed:37675639};\nDE   AltName: Full=O-methyltransferase 3 {ECO:0000303|PubMed:37675639};\nDE            Short=LwOMT3 {ECO:0000303|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:22.219060+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "69c40863ae76ff5400002524808d001fc829f5326ea095f02e4c5b528c954b0f",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WMX25281.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, TISSUE SPECIFICITY, AND PATHWAY.\nRC   STRAIN=cv. Jourdaniana;\nRX   PubMed=37675639; DOI=10.1111/tpj.16447;\nRA   Watkins J.L., Li Q., Yeaman S., Facchini P.J.;\nRT   \"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora\nRT   williamsii).\";\nRL   Plant J. 116:635-649(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:22.219060+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "69c40863ae76ff5400002524808d001fc829f5326ea095f02e4c5b528c954b0f",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3-methoxytyramine + S-adenosyl-L-methionine = N-methyl-3-\nCC         methoxytyramine + S-adenosyl-L-homocysteine + H(+);\nCC         Xref=Rhea:RHEA:81003, ChEBI:CHEBI:15378, ChEBI:CHEBI:57856,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:192089, ChEBI:CHEBI:231773;\nCC         Evidence={ECO:0000269|PubMed:37675639};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81004;\nCC         Evidence={ECO:0000269|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:22.219060+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "69c40863ae76ff5400002524808d001fc829f5326ea095f02e4c5b528c954b0f",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=mescaline + S-adenosyl-L-methionine = N-methylmescaline + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81035,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231762, ChEBI:CHEBI:231781;\nCC         Evidence={ECO:0000269|PubMed:37675639};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81036;\nCC         Evidence={ECO:0000269|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:22.219060+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "69c40863ae76ff5400002524808d001fc829f5326ea095f02e4c5b528c954b0f",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=tyramine + S-adenosyl-L-methionine = N-methyltyramine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:14865,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:58155,\nCC         ChEBI:CHEBI:59789, ChEBI:CHEBI:327995; EC=2.1.1.27;\nCC         Evidence={ECO:0000269|PubMed:37675639};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:14866;\nCC         Evidence={ECO:0000269|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:22.219060+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "69c40863ae76ff5400002524808d001fc829f5326ea095f02e4c5b528c954b0f",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81027,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231768, ChEBI:CHEBI:231777;\nCC         Evidence={ECO:0000269|PubMed:37675639};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81028;\nCC         Evidence={ECO:0000269|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:22.219060+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "69c40863ae76ff5400002524808d001fc829f5326ea095f02e4c5b528c954b0f",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3-hydroxy-4,5-dimethoxyphenethylamine + S-adenosyl-L-\nCC         methionine = N-methyl-3-hydroxy-4,5-dimethoxyphenethylamine + S-\nCC         adenosyl-L-homocysteine + H(+); Xref=Rhea:RHEA:81019,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57856, ChEBI:CHEBI:59789,\nCC         ChEBI:CHEBI:231769, ChEBI:CHEBI:231779;\nCC         Evidence={ECO:0000269|PubMed:37675639};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81020;\nCC         Evidence={ECO:0000269|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:22.219060+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-75",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "69c40863ae76ff5400002524808d001fc829f5326ea095f02e4c5b528c954b0f",
  "url": "https://rest.uniprot.org/unisave/A0AA51VIL5?format=txt&versions=10"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 51. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
