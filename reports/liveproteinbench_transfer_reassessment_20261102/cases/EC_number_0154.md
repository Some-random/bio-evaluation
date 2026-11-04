# EC_number_0154

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0154.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 1.1.1.440

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEKQVQIPEIELNSGHKMPLVGFGTCVPDPIPPLEELAGIFLEAIKVGYRHFDTASSYGTEEALGRAVAQAIETGLVNGREEFFISSKLWCEDADLDLILPALKKTLGNMGLDYLDLSMIHMPVRVRKGAEMFNYTKEDLLPFDIQGTWKAMEECNKLGLAKSIGVSNYSCEKLTKLLENATVPPAVNQVEMNVVWQQRKLLPFCKEKNIHVTAWSPLLSYGAVWGSNAVMENPILVEIAASKNKTVAQVALRWIYEQGASFIMRTFNKDRMFENVQIFDWELTKEELDKIQKIPQRRGTLGEDFIHPEGPIKSVEDLWDGDL

[Multiple Choices]
A. 1.1.1.195
B. 3.1.1.4
C. 1.1.1.440
D. 3.1.26.3
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

> The sequence-matched UniProt annotation assigns EC 1.1.1.440 and reports the NADP-dependent rhazimol/rhazimal reaction with experimental evidence. This supports the author's key, though the cited study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is consistent with a soluble NAD(P)-dependent oxidoreductase, which makes the 1.1.1 choices more plausible than the hydrolase or nuclease choices. But that broad family-level signal does not identify the enzyme's substrate or distinguish EC 1.1.1.440 from EC 1.1.1.195.


**Missing item-specific fact**

> The enzyme's substrate specificity or experimentally established catalytic reaction is needed to distinguish the two oxidoreductase EC choices.


**Reason**

> Transferable sequence knowledge can support the broad oxidoreductase class, but the key distinction between the two offered oxidoreductase numbers is reaction-specific and is not established by the sequence/context provided.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> The input offers two oxidoreductase EC numbers, and the sequence-level class inference does not resolve which reaction the protein catalyzes. The supplied reviewer-only evidence resolves this in favor of C, but it was not part of the original input.


### Important caveats

- The supporting database evidence is reviewer-only; it cannot be used as an input to the answerability judgment.
- The supplied annotation reports experimental evidence, but the cited primary paper was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble NAD(P)-dependent oxidoreductase, which makes the 1.1.1 choices more plausible than the hydrolase or nuclease choices. But that broad family-level signal does not identify the enzyme's substrate or distinguish EC 1.1.1.440 from EC 1.1.1.195.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's substrate specificity or experimentally established catalytic reaction is needed to distinguish the two oxidoreductase EC choices.",
    "reason": "Transferable sequence knowledge can support the broad oxidoreductase class, but the key distinction between the two offered oxidoreductase numbers is reaction-specific and is not established by the sequence/context provided."
  },
  "case_id": "EC_number_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 1.1.1.440 and reports the NADP-dependent rhazimol/rhazimal reaction with experimental evidence. This supports the author's key, though the cited study was not independently reviewed here."
  },
  "important_caveats": [
    "The supporting database evidence is reviewer-only; it cannot be used as an input to the answerability judgment.",
    "The supplied annotation reports experimental evidence, but the cited primary paper was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "The input offers two oxidoreductase EC numbers, and the sequence-level class inference does not resolve which reaction the protein catalyzes. The supplied reviewer-only evidence resolves this in favor of C, but it was not part of the original input."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0154",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 1.1.1.440 and reports the NADP-dependent rhazimol/rhazimal reaction with experimental evidence. This supports the author's key, though the cited study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is consistent with a soluble NAD(P)-dependent oxidoreductase, which makes the 1.1.1 choices more plausible than the hydrolase or nuclease choices. But that broad family-level signal does not identify the enzyme's substrate or distinguish EC 1.1.1.440 from EC 1.1.1.195.",
    "missing_item_specific_fact": "The enzyme's substrate specificity or experimentally established catalytic reaction is needed to distinguish the two oxidoreductase EC choices.",
    "reason": "Transferable sequence knowledge can support the broad oxidoreductase class, but the key distinction between the two offered oxidoreductase numbers is reaction-specific and is not established by the sequence/context provided."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "The input offers two oxidoreductase EC numbers, and the sequence-level class inference does not resolve which reaction the protein catalyzes. The supplied reviewer-only evidence resolves this in favor of C, but it was not part of the original input."
  },
  "important_caveats": [
    "The supporting database evidence is reviewer-only; it cannot be used as an input to the answerability judgment.",
    "The supplied annotation reports experimental evidence, but the cited primary paper was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A9E7S518) annotates this protein as Rhazimal reductase 1 (AsRHR1) with EC 1.1.1.440, supported by experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022, Chem. Sci. 13:12389-12395). The catalytic activity is rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+). The sequence matches the benchmark sequence exactly. This is experimentally validated, not merely computational inference.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains a Rossmann-fold NAD(P)-binding motif ('GFGTC' near the N-terminus and 'GAVWGS' around position 200), consistent with an NAD(P)-dependent oxidoreductase (EC 1.x.x.x). This reasonably eliminates the hydrolase options B (3.1.1.4, phospholipase A2) and D (3.1.26.3, ribonuclease). However, both remaining options A (1.1.1.195) and C (1.1.1.440) are EC 1.1.1.x oxidoreductases acting on the CH-OH group with NAD+/NADP+ as acceptor. Distinguishing the 4th digit (substrate specificity) between these two requires knowing the exact enzymatic activity or the specific enzyme identity. EC 1.1.1.440 (rhazimal reductase) was only characterized experimentally in 2022, and no obvious sequence motif uniquely identifies this as rhazimal reductase versus another EC 1.1.1.x dehydrogenase. The overall sequence architecture (323 aa, Rossmann fold) is shared across hundreds of EC 1.1.1.x enzymes.


**Missing item-specific fact**

> The specific substrate identity (rhazimal/rhazimol) and the experimental demonstration that this particular sequence catalyzes the rhazimol-to-rhazimal interconversion, which is the defining feature of EC 1.1.1.440 versus EC 1.1.1.195. Without knowing the exact enzyme identity or its characterized substrate, the sequence alone does not distinguish between these two EC 1.1.1.x numbers.


**Reason**

> While the Rossmann-fold motif provides a credible inference to narrow from four options to two oxidoreductase options (eliminating the hydrolases), the final distinction between EC 1.1.1.195 and EC 1.1.1.440 requires knowledge of the specific substrate or enzyme identity. Both are NAD(P)-dependent dehydrogenases/reductases with no obvious sequence-level discriminator. EC 1.1.1.440 is a recently characterized enzyme (2022), limiting the availability of family-level transferable knowledge that could uniquely identify it from sequence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> Both A (1.1.1.195) and C (1.1.1.440) are EC 1.1.1.x oxidoreductases, and the sequence features (Rossmann fold, length, plant origin) are consistent with either. Without specific substrate knowledge or exact enzyme identity, a model cannot definitively choose between them based on sequence alone. The hydrolase options B and D are clearly eliminated by the NAD(P)-binding Rossmann motif.


### Important caveats

- EC 1.1.1.440 was experimentally characterized in 2022 (PubMed:36349266), making it a relatively new annotation with limited representation in training corpora.
- The Rossmann-fold GxGxxG motif ('GFGTC') is a strong but non-exclusive indicator of NAD(P)-dependent oxidoreductases; it eliminates EC 3.x.x.x hydrolases but does not resolve the 4th digit among EC 1.1.1.x enzymes.
- The protein's role in monoterpene indole alkaloid (MIA) biosynthesis in Apocynaceae is a contextual clue but does not uniquely map to a single EC 1.1.1.x number from sequence features alone.
- The UniProt annotation is experimentally supported (ECO:0000269), confirming the expected answer, but this experimental fact is not derivable from sequence inspection alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold NAD(P)-binding motif ('GFGTC' near the N-terminus and 'GAVWGS' around position 200), consistent with an NAD(P)-dependent oxidoreductase (EC 1.x.x.x). This reasonably eliminates the hydrolase options B (3.1.1.4, phospholipase A2) and D (3.1.26.3, ribonuclease). However, both remaining options A (1.1.1.195) and C (1.1.1.440) are EC 1.1.1.x oxidoreductases acting on the CH-OH group with NAD+/NADP+ as acceptor. Distinguishing the 4th digit (substrate specificity) between these two requires knowing the exact enzymatic activity or the specific enzyme identity. EC 1.1.1.440 (rhazimal reductase) was only characterized experimentally in 2022, and no obvious sequence motif uniquely identifies this as rhazimal reductase versus another EC 1.1.1.x dehydrogenase. The overall sequence architecture (323 aa, Rossmann fold) is shared across hundreds of EC 1.1.1.x enzymes.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate identity (rhazimal/rhazimol) and the experimental demonstration that this particular sequence catalyzes the rhazimol-to-rhazimal interconversion, which is the defining feature of EC 1.1.1.440 versus EC 1.1.1.195. Without knowing the exact enzyme identity or its characterized substrate, the sequence alone does not distinguish between these two EC 1.1.1.x numbers.",
    "reason": "While the Rossmann-fold motif provides a credible inference to narrow from four options to two oxidoreductase options (eliminating the hydrolases), the final distinction between EC 1.1.1.195 and EC 1.1.1.440 requires knowledge of the specific substrate or enzyme identity. Both are NAD(P)-dependent dehydrogenases/reductases with no obvious sequence-level discriminator. EC 1.1.1.440 is a recently characterized enzyme (2022), limiting the availability of family-level transferable knowledge that could uniquely identify it from sequence."
  },
  "case_id": "EC_number_0154",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9E7S518) annotates this protein as Rhazimal reductase 1 (AsRHR1) with EC 1.1.1.440, supported by experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022, Chem. Sci. 13:12389-12395). The catalytic activity is rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+). The sequence matches the benchmark sequence exactly. This is experimentally validated, not merely computational inference."
  },
  "important_caveats": [
    "EC 1.1.1.440 was experimentally characterized in 2022 (PubMed:36349266), making it a relatively new annotation with limited representation in training corpora.",
    "The Rossmann-fold GxGxxG motif ('GFGTC') is a strong but non-exclusive indicator of NAD(P)-dependent oxidoreductases; it eliminates EC 3.x.x.x hydrolases but does not resolve the 4th digit among EC 1.1.1.x enzymes.",
    "The protein's role in monoterpene indole alkaloid (MIA) biosynthesis in Apocynaceae is a contextual clue but does not uniquely map to a single EC 1.1.1.x number from sequence features alone.",
    "The UniProt annotation is experimentally supported (ECO:0000269), confirming the expected answer, but this experimental fact is not derivable from sequence inspection alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "Both A (1.1.1.195) and C (1.1.1.440) are EC 1.1.1.x oxidoreductases, and the sequence features (Rossmann fold, length, plant origin) are consistent with either. Without specific substrate knowledge or exact enzyme identity, a model cannot definitively choose between them based on sequence alone. The hydrolase options B and D are clearly eliminated by the NAD(P)-binding Rossmann motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0154",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A9E7S518) annotates this protein as Rhazimal reductase 1 (AsRHR1) with EC 1.1.1.440, supported by experimental evidence (ECO:0000269, PubMed:36349266, Wang et al. 2022, Chem. Sci. 13:12389-12395). The catalytic activity is rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+). The sequence matches the benchmark sequence exactly. This is experimentally validated, not merely computational inference.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains a Rossmann-fold NAD(P)-binding motif ('GFGTC' near the N-terminus and 'GAVWGS' around position 200), consistent with an NAD(P)-dependent oxidoreductase (EC 1.x.x.x). This reasonably eliminates the hydrolase options B (3.1.1.4, phospholipase A2) and D (3.1.26.3, ribonuclease). However, both remaining options A (1.1.1.195) and C (1.1.1.440) are EC 1.1.1.x oxidoreductases acting on the CH-OH group with NAD+/NADP+ as acceptor. Distinguishing the 4th digit (substrate specificity) between these two requires knowing the exact enzymatic activity or the specific enzyme identity. EC 1.1.1.440 (rhazimal reductase) was only characterized experimentally in 2022, and no obvious sequence motif uniquely identifies this as rhazimal reductase versus another EC 1.1.1.x dehydrogenase. The overall sequence architecture (323 aa, Rossmann fold) is shared across hundreds of EC 1.1.1.x enzymes.",
    "missing_item_specific_fact": "The specific substrate identity (rhazimal/rhazimol) and the experimental demonstration that this particular sequence catalyzes the rhazimol-to-rhazimal interconversion, which is the defining feature of EC 1.1.1.440 versus EC 1.1.1.195. Without knowing the exact enzyme identity or its characterized substrate, the sequence alone does not distinguish between these two EC 1.1.1.x numbers.",
    "reason": "While the Rossmann-fold motif provides a credible inference to narrow from four options to two oxidoreductase options (eliminating the hydrolases), the final distinction between EC 1.1.1.195 and EC 1.1.1.440 requires knowledge of the specific substrate or enzyme identity. Both are NAD(P)-dependent dehydrogenases/reductases with no obvious sequence-level discriminator. EC 1.1.1.440 is a recently characterized enzyme (2022), limiting the availability of family-level transferable knowledge that could uniquely identify it from sequence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "Both A (1.1.1.195) and C (1.1.1.440) are EC 1.1.1.x oxidoreductases, and the sequence features (Rossmann fold, length, plant origin) are consistent with either. Without specific substrate knowledge or exact enzyme identity, a model cannot definitively choose between them based on sequence alone. The hydrolase options B and D are clearly eliminated by the NAD(P)-binding Rossmann motif."
  },
  "important_caveats": [
    "EC 1.1.1.440 was experimentally characterized in 2022 (PubMed:36349266), making it a relatively new annotation with limited representation in training corpora.",
    "The Rossmann-fold GxGxxG motif ('GFGTC') is a strong but non-exclusive indicator of NAD(P)-dependent oxidoreductases; it eliminates EC 3.x.x.x hydrolases but does not resolve the 4th digit among EC 1.1.1.x enzymes.",
    "The protein's role in monoterpene indole alkaloid (MIA) biosynthesis in Apocynaceae is a contextual clue but does not uniquely map to a single EC 1.1.1.x number from sequence features alone.",
    "The UniProt annotation is experimentally supported (ECO:0000269), confirming the expected answer, but this experimental fact is not derivable from sequence inspection alone."
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
  "benchmark_sequence_length": 323,
  "benchmark_sequence_sha256": "016d2556a5540f503b5f5d1c251aaf15f9f522ff3142edec17aaac977d884675",
  "current_entry_audit": {
    "entryVersion": 13,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 323,
  "current_source_sequence_sha256": "016d2556a5540f503b5f5d1c251aaf15f9f522ff3142edec17aaac977d884675",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 12,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9E7S518",
  "selected_historical_entry_version": 12,
  "selected_historical_record_sha256": "9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320",
  "selected_historical_source_sequence_length": 323,
  "selected_historical_source_sequence_sha256": "016d2556a5540f503b5f5d1c251aaf15f9f522ff3142edec17aaac977d884675",
  "selected_historical_version": {
    "accession": "A0A9E7S518",
    "database": "Swiss-Prot",
    "entryVersion": 12,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "RHR1_ALSSC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9E7S518\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":13,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.440\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Rhazimal reductase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsRHR1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79617\"}}],\"reaction\":{\"ecNumber\":\"1.1.1.440\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"name\":\"rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79615\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230473\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230474\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7S518.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65385.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:12.223906+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "48100f49c79084f47d85a13a08484c59c6d716f4326ce301e0bac7ab49997534",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7S518.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H1",
  "excerpt": "ID   RHR1_ALSSC              Reviewed;         323 AA.\nAC   A0A9E7S518;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 12.\nDE   RecName: Full=Rhazimal reductase 1 {ECO:0000303|PubMed:36349266};\nDE            Short=AsRHR1 {ECO:0000303|PubMed:36349266};\nDE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};\nGN   Name=RHR1 {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.092631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Rhazimal reductase 1 {ECO:0000303|PubMed:36349266};\nDE            Short=AsRHR1 {ECO:0000303|PubMed:36349266};\nDE            EC=1.1.1.440 {ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.092631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65385.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.092631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12)

```json
{
  "entry_version": 12,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=rhazimol + NADP(+) = rhazimal + NADPH + 2 H(+);\nCC         Xref=Rhea:RHEA:79615, ChEBI:CHEBI:15378, ChEBI:CHEBI:57783,\nCC         ChEBI:CHEBI:58349, ChEBI:CHEBI:230473, ChEBI:CHEBI:230474;\nCC         EC=1.1.1.440; Evidence={ECO:0000269|PubMed:36349266};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:79617;\nCC         Evidence={ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.092631+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9e7eab76338f130e203ce1b1b78446aa08ea74e562c2d55ca9d31f37f8958320",
  "url": "https://rest.uniprot.org/unisave/A0A9E7S518?format=txt&versions=12"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 154. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
