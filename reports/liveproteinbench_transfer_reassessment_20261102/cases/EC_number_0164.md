# EC_number_0164

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0164.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 5.1.3.45

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MMSRYEELRKELPAQPKVWLITGVAGFIGSNLLETLLKLDQKVVGLDNFATGHQRNLDEVRSLVSEKQWSNFKFIQGDIRNLDDCNNACAGVDYVLHQAALGSVPRSINDPITSNATNIDGFLNMLIAARDAKVQSFTYAASSSTYGDHPGLPKVEDTIGKPLSPYAVTKYVNELYADVFSRCYGFSTIGLRYFNVFGRRQDPNGAYAAVIPKWTSSMIQGDDVYINGDGETSRDFCYIENTVQANLLAATAGLDARNQVYNIAVGGRTSLNQLFFALRDGLAENGVSYHREPVYRDFREGDVRHSLADISKAAKLLGYAPKYDVSAGVALAMPWYIMFLK

[Multiple Choices]
A. 5.1.3.45
B. 5.1.3.14
C. 5.1.1.25
D. 2.1.2.1
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

> The sequence-matched UniProt record reports the reaction assigned EC 5.1.3.45 with experimental evidence, supporting choice A. The record also reports EC 5.1.3.7 activity, which is not among the choices.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal glycine-rich motif is consistent with an NAD-dependent UDP-sugar epimerase, which helps distinguish the epimerase choices from the unrelated amino-acid racemase and transferase options. But that broad family-level inference does not establish which specific UDP-sugar substrate is epimerized.


**Missing item-specific fact**

> The enzyme's substrate specificity, needed to distinguish EC 5.1.3.45 from the other closely related epimerase choice.


**Reason**

> The sequence provides a credible basis for recognizing a UDP-sugar epimerase, but the offered epimerase alternatives differ in reaction/substrate specificity. No supplied context or clearly discriminating sequence feature establishes that specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered options, the evidence supports A; the separately annotated EC 5.1.3.7 activity is not offered.


### Important caveats

- The supporting annotation is experimental evidence for a reaction of the sequence-matched protein; the record also lists another experimentally supported catalytic activity.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich motif is consistent with an NAD-dependent UDP-sugar epimerase, which helps distinguish the epimerase choices from the unrelated amino-acid racemase and transferase options. But that broad family-level inference does not establish which specific UDP-sugar substrate is epimerized.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's substrate specificity, needed to distinguish EC 5.1.3.45 from the other closely related epimerase choice.",
    "reason": "The sequence provides a credible basis for recognizing a UDP-sugar epimerase, but the offered epimerase alternatives differ in reaction/substrate specificity. No supplied context or clearly discriminating sequence feature establishes that specificity."
  },
  "case_id": "EC_number_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports the reaction assigned EC 5.1.3.45 with experimental evidence, supporting choice A. The record also reports EC 5.1.3.7 activity, which is not among the choices."
  },
  "important_caveats": [
    "The supporting annotation is experimental evidence for a reaction of the sequence-matched protein; the record also lists another experimentally supported catalytic activity.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, the evidence supports A; the separately annotated EC 5.1.3.7 activity is not offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports the reaction assigned EC 5.1.3.45 with experimental evidence, supporting choice A. The record also reports EC 5.1.3.7 activity, which is not among the choices.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal glycine-rich motif is consistent with an NAD-dependent UDP-sugar epimerase, which helps distinguish the epimerase choices from the unrelated amino-acid racemase and transferase options. But that broad family-level inference does not establish which specific UDP-sugar substrate is epimerized.",
    "missing_item_specific_fact": "The enzyme's substrate specificity, needed to distinguish EC 5.1.3.45 from the other closely related epimerase choice.",
    "reason": "The sequence provides a credible basis for recognizing a UDP-sugar epimerase, but the offered epimerase alternatives differ in reaction/substrate specificity. No supplied context or clearly discriminating sequence feature establishes that specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered options, the evidence supports A; the separately annotated EC 5.1.3.7 activity is not offered."
  },
  "important_caveats": [
    "The supporting annotation is experimental evidence for a reaction of the sequence-matched protein; the record also lists another experimentally supported catalytic activity.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q8KN66, WbpP from Pseudomonas aeruginosa) lists EC 5.1.3.45 (UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase) as the recommended name with experimental evidence (ECO:0000269|PubMed:18065759). The catalytic activity reaction UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate is annotated with EC 5.1.3.45. Note that the enzyme also has EC 5.1.3.7 (UDP-GlcNAc 4-epimerase) as an alternative activity, but 5.1.3.45 is the primary/recommended annotation and 5.1.3.7 is not among the offered choices.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H9](#evidence-h9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical Rossmann-fold motif 'GVAGFIGSN' (positions ~22-30), which is the hallmark NAD+-binding motif of the UDP-hexose 4-epimerase superfamily (GalE, WbpP, etc.). Additionally, the 'GDD' motif (~position 230, 'GDDVYINGDGETSRDF') is a conserved catalytic feature of 4-epimerases that use NAD+-mediated oxidation-reduction at C4. The overall length (~341 aa) and domain architecture are consistent with the UDP-sugar 4-epimerase family. These features definitively eliminate C (5.1.1.25, amino acid epimerase — completely different fold and mechanism) and D (2.1.2.1, glycine hydroxymethyltransferase — a transferase with no Rossmann fold). Between A (5.1.3.45) and B (5.1.3.14): the Rossmann fold + GDD motif indicate a 4-epimerase mechanism (NAD+-dependent C4 oxidation-reduction). EC 5.1.3.14, if it represents a 2-epimerase or mechanistically distinct epimerase, would not be expected to possess these 4-epimerase hallmarks. A knowledgeable model recognizing the UDP-hexose 4-epimerase family architecture can reasonably infer a 4-epimerase EC number, making 5.1.3.45 (a 4-epimerase) the best-supported choice among the offered alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann fold, GDD motif, and overall family architecture provide transferable structural/mechanistic knowledge that identifies this as a UDP-sugar 4-epimerase, eliminating the non-epimerase and amino-acid-epimerase choices. The 4-epimerase mechanism features (NAD+ binding, GDD catalytic motif) are inconsistent with a 2-epimerase mechanism, providing a credible basis to prefer 5.1.3.45 (4-epimerase) over 5.1.3.14. While distinguishing 5.1.3.45 from other 4-epimerase EC numbers (e.g., 5.1.3.7, 5.1.3.1) would require substrate-specificity knowledge, those alternatives are not offered, making the family-level inference sufficient for this MC question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Rossmann fold and GDD motif clearly indicate a 4-epimerase mechanism, eliminating C and D. Between A and B, the 4-epimerase mechanism features favor A. No two options are equally defensible given the sequence evidence.


### Important caveats

- The enzyme WbpP is a 'promiscuous' 4-epimerase with dual activity (EC 5.1.3.45 and EC 5.1.3.7). The distinction between these two EC numbers depends on physiological substrate context, which is not directly readable from sequence alone. However, EC 5.1.3.7 is not among the offered choices, so this does not create ambiguity for this MC question.
- The exact identity of EC 5.1.3.14 (option B) could not be fully confirmed from general knowledge alone; if it were another 4-epimerase acting on a different UDP-sugar, the distinction from 5.1.3.45 would require substrate-specificity knowledge. However, the 4-epimerase mechanism features still favor A over a mechanistically distinct alternative.
- The UniProt annotation for EC 5.1.3.45 was assigned based on experimental evidence from PubMed:18065759 (2008), while EC 5.1.3.7 was the original annotation (2000-2005). The 'recommended' vs 'alternative' naming reflects evolving understanding of the physiological substrate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical Rossmann-fold motif 'GVAGFIGSN' (positions ~22-30), which is the hallmark NAD+-binding motif of the UDP-hexose 4-epimerase superfamily (GalE, WbpP, etc.). Additionally, the 'GDD' motif (~position 230, 'GDDVYINGDGETSRDF') is a conserved catalytic feature of 4-epimerases that use NAD+-mediated oxidation-reduction at C4. The overall length (~341 aa) and domain architecture are consistent with the UDP-sugar 4-epimerase family. These features definitively eliminate C (5.1.1.25, amino acid epimerase — completely different fold and mechanism) and D (2.1.2.1, glycine hydroxymethyltransferase — a transferase with no Rossmann fold). Between A (5.1.3.45) and B (5.1.3.14): the Rossmann fold + GDD motif indicate a 4-epimerase mechanism (NAD+-dependent C4 oxidation-reduction). EC 5.1.3.14, if it represents a 2-epimerase or mechanistically distinct epimerase, would not be expected to possess these 4-epimerase hallmarks. A knowledgeable model recognizing the UDP-hexose 4-epimerase family architecture can reasonably infer a 4-epimerase EC number, making 5.1.3.45 (a 4-epimerase) the best-supported choice among the offered alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold, GDD motif, and overall family architecture provide transferable structural/mechanistic knowledge that identifies this as a UDP-sugar 4-epimerase, eliminating the non-epimerase and amino-acid-epimerase choices. The 4-epimerase mechanism features (NAD+ binding, GDD catalytic motif) are inconsistent with a 2-epimerase mechanism, providing a credible basis to prefer 5.1.3.45 (4-epimerase) over 5.1.3.14. While distinguishing 5.1.3.45 from other 4-epimerase EC numbers (e.g., 5.1.3.7, 5.1.3.1) would require substrate-specificity knowledge, those alternatives are not offered, making the family-level inference sufficient for this MC question."
  },
  "case_id": "EC_number_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H9"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q8KN66, WbpP from Pseudomonas aeruginosa) lists EC 5.1.3.45 (UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase) as the recommended name with experimental evidence (ECO:0000269|PubMed:18065759). The catalytic activity reaction UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate is annotated with EC 5.1.3.45. Note that the enzyme also has EC 5.1.3.7 (UDP-GlcNAc 4-epimerase) as an alternative activity, but 5.1.3.45 is the primary/recommended annotation and 5.1.3.7 is not among the offered choices."
  },
  "important_caveats": [
    "The enzyme WbpP is a 'promiscuous' 4-epimerase with dual activity (EC 5.1.3.45 and EC 5.1.3.7). The distinction between these two EC numbers depends on physiological substrate context, which is not directly readable from sequence alone. However, EC 5.1.3.7 is not among the offered choices, so this does not create ambiguity for this MC question.",
    "The exact identity of EC 5.1.3.14 (option B) could not be fully confirmed from general knowledge alone; if it were another 4-epimerase acting on a different UDP-sugar, the distinction from 5.1.3.45 would require substrate-specificity knowledge. However, the 4-epimerase mechanism features still favor A over a mechanistically distinct alternative.",
    "The UniProt annotation for EC 5.1.3.45 was assigned based on experimental evidence from PubMed:18065759 (2008), while EC 5.1.3.7 was the original annotation (2000-2005). The 'recommended' vs 'alternative' naming reflects evolving understanding of the physiological substrate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann fold and GDD motif clearly indicate a 4-epimerase mechanism, eliminating C and D. Between A and B, the 4-epimerase mechanism features favor A. No two options are equally defensible given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q8KN66, WbpP from Pseudomonas aeruginosa) lists EC 5.1.3.45 (UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase) as the recommended name with experimental evidence (ECO:0000269|PubMed:18065759). The catalytic activity reaction UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate is annotated with EC 5.1.3.45. Note that the enzyme also has EC 5.1.3.7 (UDP-GlcNAc 4-epimerase) as an alternative activity, but 5.1.3.45 is the primary/recommended annotation and 5.1.3.7 is not among the offered choices.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical Rossmann-fold motif 'GVAGFIGSN' (positions ~22-30), which is the hallmark NAD+-binding motif of the UDP-hexose 4-epimerase superfamily (GalE, WbpP, etc.). Additionally, the 'GDD' motif (~position 230, 'GDDVYINGDGETSRDF') is a conserved catalytic feature of 4-epimerases that use NAD+-mediated oxidation-reduction at C4. The overall length (~341 aa) and domain architecture are consistent with the UDP-sugar 4-epimerase family. These features definitively eliminate C (5.1.1.25, amino acid epimerase — completely different fold and mechanism) and D (2.1.2.1, glycine hydroxymethyltransferase — a transferase with no Rossmann fold). Between A (5.1.3.45) and B (5.1.3.14): the Rossmann fold + GDD motif indicate a 4-epimerase mechanism (NAD+-dependent C4 oxidation-reduction). EC 5.1.3.14, if it represents a 2-epimerase or mechanistically distinct epimerase, would not be expected to possess these 4-epimerase hallmarks. A knowledgeable model recognizing the UDP-hexose 4-epimerase family architecture can reasonably infer a 4-epimerase EC number, making 5.1.3.45 (a 4-epimerase) the best-supported choice among the offered alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann fold, GDD motif, and overall family architecture provide transferable structural/mechanistic knowledge that identifies this as a UDP-sugar 4-epimerase, eliminating the non-epimerase and amino-acid-epimerase choices. The 4-epimerase mechanism features (NAD+ binding, GDD catalytic motif) are inconsistent with a 2-epimerase mechanism, providing a credible basis to prefer 5.1.3.45 (4-epimerase) over 5.1.3.14. While distinguishing 5.1.3.45 from other 4-epimerase EC numbers (e.g., 5.1.3.7, 5.1.3.1) would require substrate-specificity knowledge, those alternatives are not offered, making the family-level inference sufficient for this MC question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Rossmann fold and GDD motif clearly indicate a 4-epimerase mechanism, eliminating C and D. Between A and B, the 4-epimerase mechanism features favor A. No two options are equally defensible given the sequence evidence."
  },
  "important_caveats": [
    "The enzyme WbpP is a 'promiscuous' 4-epimerase with dual activity (EC 5.1.3.45 and EC 5.1.3.7). The distinction between these two EC numbers depends on physiological substrate context, which is not directly readable from sequence alone. However, EC 5.1.3.7 is not among the offered choices, so this does not create ambiguity for this MC question.",
    "The exact identity of EC 5.1.3.14 (option B) could not be fully confirmed from general knowledge alone; if it were another 4-epimerase acting on a different UDP-sugar, the distinction from 5.1.3.45 would require substrate-specificity knowledge. However, the 4-epimerase mechanism features still favor A over a mechanistically distinct alternative.",
    "The UniProt annotation for EC 5.1.3.45 was assigned based on experimental evidence from PubMed:18065759 (2008), while EC 5.1.3.7 was the original annotation (2000-2005). The 'recommended' vs 'alternative' naming reflects evolving understanding of the physiological substrate."
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
  "benchmark_sequence_length": 341,
  "benchmark_sequence_sha256": "89a20333193e2023e3eb938fc67c5a1fcdbb1a54c07d86617c4a4c0b17109406",
  "current_entry_audit": {
    "entryVersion": 89,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-10-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 341,
  "current_source_sequence_sha256": "89a20333193e2023e3eb938fc67c5a1fcdbb1a54c07d86617c4a4c0b17109406",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 87,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8KN66",
  "selected_historical_entry_version": 87,
  "selected_historical_record_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "selected_historical_source_sequence_length": 341,
  "selected_historical_source_sequence_sha256": "89a20333193e2023e3eb938fc67c5a1fcdbb1a54c07d86617c4a4c0b17109406",
  "selected_historical_version": {
    "accession": "Q8KN66",
    "database": "Swiss-Prot",
    "entryVersion": 87,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "WBPP_PSEAI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8KN66\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":89,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-10-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Pseudomonas\"],\"scientificName\":\"Pseudomonas aeruginosa\",\"taxonId\":287}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10747995\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15016816\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15752069\",\"source\":\"PubMed\"}],\"value\":\"5.1.3.7\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"15752069\",\"source\":\"PubMed\"}],\"value\":\"UDP-N-acetylglucosamine C4 epimerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"10747995\",\"source\":\"PubMed\"}],\"value\":\"UDP-GlcNAc C4 epimerase\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"value\":\"5.1.3.45\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"UDP-GlcNAcA 4-epimerase\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:81512\"}}],\"reaction\":{\"ecNumber\":\"5.1.3.45\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18065759\",\"source\":\"PubMed\"}],\"name\":\"UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-2-deoxy-alpha-D-galacturonate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:81511\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:65040\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:231899\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"5.1.3.7\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"10747995\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15016816\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"15752069\",\"source\":\"PubMed\"}],\"name\":\"UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-galactosamine\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:20517\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57705\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:67138\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Creuzenet C.\",\"Belanger M.\",\"Wakarchuk W.W.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"10747995\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m001171200\"}],\"citationType\":\"journal article\",\"firstPage\":\"19060\",\"id\":\"10747995\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"19067\",\"publicationDate\":\"2000\",\"title\":\"Expression, purification, and biochemical characterization of WbpP, a new UDP-GlcNAc C4 epimerase from Pseudomonas aeruginosa serotype O6.\",\"volume\":\"275\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Serotype O6\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Demendi M.\",\"Ishiyama N.\",\"Lam J.S.\",\"Berghuis A.M.\",\"Creuzenet C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15752069\"},{\"database\":\"DOI\",\"id\":\"10.1042/bj20050263\"}],\"citationType\":\"journal article\",\"firstPage\":\"173\",\"id\":\"15752069\",\"journal\":\"Biochem. J.\",\"lastPage\":\"180\",\"publicationDate\":\"2005\",\"title\":\"Towards a better understanding of the substrate specificity of the UDP-N-acetylglucosamine C4 epimerase WbpP.\",\"volume\":\"389\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Serotype O6\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"MUTAGENESIS OF GLY-102; SER-143; SER-144; GLN-201 AND ALA-209\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Miller W.L.\",\"Matewish M.J.\",\"McNally D.J.\",\"Ishiyama N.\",\"Anderson E.M.\",\"Brewer D.\",\"Brisson J.R.\",\"Berghuis A.M.\",\"Lam J.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18065759\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m708894200\"}],\"citationType\":\"journal article\",\"firstPage\":\"3507\",\"id\":\"18065759\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"3518\",\"publicationDate\":\"2008\",\"title\":\"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-antigen biosynthesis enzyme WbpO.\",\"volume\":\"283\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"PAK / Serotype O6\"}],\"referenceNumber\":5,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8KN66.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Ishiyama N.\",\"Creuzenet C.\",\"Lam J.S.\",\"Berghuis A.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"15016816\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m401642200\"}],\"citationType\":\"journal article\",\"firstPage\":\"22635\",\"id\":\"15016816\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"22642\",\"publicationDate\":\"2004\",\"title\":\"Crystal structure of WbpP, a genuine UDP-N-acetylglucosamine 4-epimerase from Pseudomonas aeruginosa: substrate specificity in UDP-hexose 4-epimerases.\",\"volume\":\"279\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"1SB8\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"1SB9\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"Serotype O6\"}],\"referenceNumber\":6,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.10 ANGSTROMS) IN COMPLEXES WITH NAD(+); UDP-N-ACETYL-ALPHA-D-GALACTOSAMINE AND UDP-GLUCOSE\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBUNIT\",\"MUTAGENESIS OF ALA-209 AND SER-306\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-01T06:25:25.367428+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f67b2500389a81025c9be1998ba5bdf0c0e6d0d7f2971007bc6e11f741355b05",
  "url": "https://rest.uniprot.org/uniprotkb/Q8KN66.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H1",
  "excerpt": "ID   WBPP_PSEAI              Reviewed;         341 AA.\nAC   Q8KN66; Q9RHD6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2002, sequence version 1.\nDT   28-JAN-2026, entry version 87.\nDE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase {ECO:0000305};\nDE            Short=UDP-GlcNAcA 4-epimerase {ECO:0000305};\nDE            EC=5.1.3.45 {ECO:0000269|PubMed:18065759};\nDE   AltName: Full=UDP-N-acetylglucosamine C4 epimerase {ECO:0000303|PubMed:15752069};\nDE            Short=UDP-GlcNAc C4 epimerase {ECO:0000303|PubMed:10747995};\nDE            EC=5.1.3.7 {ECO:0000269|PubMed:10747995, ECO:0000269|PubMed:15016816, ECO:0000269|PubMed:15752069};\nGN   Name=wbpP {ECO:0000303|PubMed:10627048, ECO:0000303|PubMed:12057956};\nOS   Pseudomonas aeruginosa.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Pseudomonas.\nOX   NCBI_TaxID=287;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=UDP-N-acetyl-alpha-D-glucosaminouronate 4-epimerase {ECO:0000305};\nDE            Short=UDP-GlcNAcA 4-epimerase {ECO:0000305};\nDE            EC=5.1.3.45 {ECO:0000269|PubMed:18065759};\nDE   AltName: Full=UDP-N-acetylglucosamine C4 epimerase {ECO:0000303|PubMed:15752069};\nDE            Short=UDP-GlcNAc C4 epimerase {ECO:0000303|PubMed:10747995};\nDE            EC=5.1.3.7 {ECO:0000269|PubMed:10747995, ECO:0000269|PubMed:15016816, ECO:0000269|PubMed:15752069};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAF23998.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, PATHWAY, AND DISRUPTION\nRP   PHENOTYPE.\nRC   STRAIN=ATCC 33354 / Serotype O6;\nRX   PubMed=10627048; DOI=10.1099/00221287-145-12-3505;\nRA   Belanger M., Burrows L.L., Lam J.S.;\nRT   \"Functional analysis of genes responsible for the synthesis of the B-band O\nRT   antigen of Pseudomonas aeruginosa serotype O6 lipopolysaccharide.\";\nRL   Microbiology 145:3505-3521(1999).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H4",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:AAM27817.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=Serotype O6;\nRX   PubMed=12057956; DOI=10.1128/jb.184.13.3614-3622.2002;\nRA   Raymond C.K., Sims E.H., Kas A., Spencer D.H., Kutyavin T.V., Ivey R.G.,\nRA   Zhou Y., Kaul R., Clendenning J.B., Olson M.V.;\nRT   \"Genetic variation at the O-antigen biosynthetic locus in Pseudomonas\nRT   aeruginosa.\";\nRL   J. Bacteriol. 184:3614-3622(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H5",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, BIOPHYSICOCHEMICAL PROPERTIES, AND\nRP   SUBUNIT.\nRC   STRAIN=Serotype O6;\nRX   PubMed=10747995; DOI=10.1074/jbc.m001171200;\nRA   Creuzenet C., Belanger M., Wakarchuk W.W., Lam J.S.;\nRT   \"Expression, purification, and biochemical characterization of WbpP, a new\nRT   UDP-GlcNAc C4 epimerase from Pseudomonas aeruginosa serotype O6.\";\nRL   J. Biol. Chem. 275:19060-19067(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H6",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND MUTAGENESIS OF GLY-102; SER-143; SER-144;\nRP   GLN-201 AND ALA-209.\nRC   STRAIN=Serotype O6;\nRX   PubMed=15752069; DOI=10.1042/bj20050263;\nRA   Demendi M., Ishiyama N., Lam J.S., Berghuis A.M., Creuzenet C.;\nRT   \"Towards a better understanding of the substrate specificity of the UDP-N-\nRT   acetylglucosamine C4 epimerase WbpP.\";\nRL   Biochem. J. 389:173-180(2005).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-52",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H7",
  "excerpt": "RN   [5]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=PAK / Serotype O6;\nRX   PubMed=18065759; DOI=10.1074/jbc.m708894200;\nRA   Miller W.L., Matewish M.J., McNally D.J., Ishiyama N., Anderson E.M.,\nRA   Brewer D., Brisson J.R., Berghuis A.M., Lam J.S.;\nRT   \"Flagellin glycosylation in Pseudomonas aeruginosa PAK requires the O-\nRT   antigen biosynthesis enzyme WbpO.\";\nRL   J. Biol. Chem. 283:3507-3518(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H8",
  "excerpt": "RN   [6] {ECO:0007744|PDB:1SB8, ECO:0007744|PDB:1SB9}\nRP   X-RAY CRYSTALLOGRAPHY (2.10 ANGSTROMS) IN COMPLEXES WITH NAD(+);\nRP   UDP-N-ACETYL-ALPHA-D-GALACTOSAMINE AND UDP-GLUCOSE, FUNCTION, CATALYTIC\nRP   ACTIVITY, COFACTOR, SUBUNIT, AND MUTAGENESIS OF ALA-209 AND SER-306.\nRC   STRAIN=Serotype O6;\nRX   PubMed=15016816; DOI=10.1074/jbc.m401642200;\nRA   Ishiyama N., Creuzenet C., Lam J.S., Berghuis A.M.;\nRT   \"Crystal structure of WbpP, a genuine UDP-N-acetylglucosamine 4-epimerase\nRT   from Pseudomonas aeruginosa: substrate specificity in UDP-hexose 4-\nRT   epimerases.\";\nRL   J. Biol. Chem. 279:22635-22642(2004).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H9",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-2-acetamido-2-deoxy-alpha-D-glucuronate = UDP-2-acetamido-\nCC         2-deoxy-alpha-D-galacturonate; Xref=Rhea:RHEA:81511,\nCC         ChEBI:CHEBI:65040, ChEBI:CHEBI:231899; EC=5.1.3.45;\nCC         Evidence={ECO:0000269|PubMed:18065759};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:81512;\nCC         Evidence={ECO:0000269|PubMed:18065759};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H10",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=UDP-N-acetyl-alpha-D-glucosamine = UDP-N-acetyl-alpha-D-\nCC         galactosamine; Xref=Rhea:RHEA:20517, ChEBI:CHEBI:57705,\nCC         ChEBI:CHEBI:67138; EC=5.1.3.7; Evidence={ECO:0000269|PubMed:10747995,\nCC         ECO:0000269|PubMed:15016816, ECO:0000269|PubMed:15752069};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.451179+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-96",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d549ed0cf621d2667a5b18f1c61cab90f3244af9d4301b29345d83da21267e72",
  "url": "https://rest.uniprot.org/unisave/Q8KN66?format=txt&versions=87"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 164. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
