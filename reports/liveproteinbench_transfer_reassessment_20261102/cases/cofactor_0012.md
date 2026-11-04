# cofactor_0012

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0012.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGKSPEEQHPVKAYGWAARDSSGILSPFKFSRRATGDHDVRVKILYAGVCHSDLQSARNEMGCFTYPLVPGFETVGIATEVGSKVTKMKVGDKVAVGIMVGSCGKCDDCVNDRECYCPEVITSYGRIDHDGTPTYGGFSNETVANEKFVFRFPEKLPMAAGAPLLNAGVSVYSPMRFYGLDKPGMHLGVVGLGGLGHLAVKFAKAFGVKVTVISTSSIKKGEAINDLGADAFLVSTDAKQMQAGSGTLDGILDTVPVVHPIEPLLGLLKNHTKLVLVGATMGSFELPILPLGVGRKSVASTVGGSTTEAQEMLDFAAEHNITANVEIIPMDYINTAMERIEKNDVRYRFVIDVGNTLTPPES

[Multiple Choices]
A. pantetheine 4'-phosphate
B. Zn(2+)
C. NAD(+)
D. Fe cation
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The matched sequence has a UniProt Zn(2+) cofactor annotation, including a note of two Zn(2+) ions per subunit. That annotation is transferred from another UniProt protein rather than direct experimental evidence for this exact protein, but it supports the expected choice.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a zinc-dependent dehydrogenase/reductase family: its cysteine- and histidine-containing regions are compatible with the metal-binding features of such enzymes. Transferable family knowledge therefore favors Zn(2+) over pantetheine 4'-phosphate or Fe; the reductive enzyme context also makes NAD(+) a less fitting choice than a metal cofactor.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence provides a meaningful basis for selecting Zn(2+) among these alternatives, without needing the exact protein's database record. This is a probabilistic inference, not a guarantee that the sequence alone establishes metal binding.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although nucleotide cofactors are relevant to many reductases, NAD(+) is not as defensible here as the metal cofactor, and the other choices are less consistent with the sequence and enzyme-family inference.


### Important caveats

- The supplied annotation's Zn(2+) assignment is based on transfer from another protein, not direct experimental evidence for this exact sequence.
- The reviewer-only source record matches the sequence, but its identity and annotations were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a zinc-dependent dehydrogenase/reductase family: its cysteine- and histidine-containing regions are compatible with the metal-binding features of such enzymes. Transferable family knowledge therefore favors Zn(2+) over pantetheine 4'-phosphate or Fe; the reductive enzyme context also makes NAD(+) a less fitting choice than a metal cofactor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence provides a meaningful basis for selecting Zn(2+) among these alternatives, without needing the exact protein's database record. This is a probabilistic inference, not a guarantee that the sequence alone establishes metal binding."
  },
  "case_id": "cofactor_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt Zn(2+) cofactor annotation, including a note of two Zn(2+) ions per subunit. That annotation is transferred from another UniProt protein rather than direct experimental evidence for this exact protein, but it supports the expected choice."
  },
  "important_caveats": [
    "The supplied annotation's Zn(2+) assignment is based on transfer from another protein, not direct experimental evidence for this exact sequence.",
    "The reviewer-only source record matches the sequence, but its identity and annotations were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although nucleotide cofactors are relevant to many reductases, NAD(+) is not as defensible here as the metal cofactor, and the other choices are less consistent with the sequence and enzyme-family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence has a UniProt Zn(2+) cofactor annotation, including a note of two Zn(2+) ions per subunit. That annotation is transferred from another UniProt protein rather than direct experimental evidence for this exact protein, but it supports the expected choice.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a zinc-dependent dehydrogenase/reductase family: its cysteine- and histidine-containing regions are compatible with the metal-binding features of such enzymes. Transferable family knowledge therefore favors Zn(2+) over pantetheine 4'-phosphate or Fe; the reductive enzyme context also makes NAD(+) a less fitting choice than a metal cofactor.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence provides a meaningful basis for selecting Zn(2+) among these alternatives, without needing the exact protein's database record. This is a probabilistic inference, not a guarantee that the sequence alone establishes metal binding."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although nucleotide cofactors are relevant to many reductases, NAD(+) is not as defensible here as the metal cofactor, and the other choices are less consistent with the sequence and enzyme-family inference."
  },
  "important_caveats": [
    "The supplied annotation's Zn(2+) assignment is based on transfer from another protein, not direct experimental evidence for this exact sequence.",
    "The reviewer-only source record matches the sequence, but its identity and annotations were not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H4) explicitly lists Zn(2+) as the cofactor, binding 2 Zn(2+) ions per subunit. The evidence code is ECO:0000250 (inferred by similarity to P06525, a Populus cinnamyl alcohol dehydrogenase), so this is a transferred annotation rather than direct experimental proof for this specific protein. However, the protein is independently confirmed as a CAD-like reductase (paper title, PubMed 26715562), and CAD enzymes in the MDR superfamily are well-established Zn-dependent enzymes. The sequence contains a characteristic cysteine cluster (SCGKCDDCVNDRECYCPE) consistent with zinc coordination in MDR enzymes, and Rossmann-fold motifs (GATMGS, GVGRKS) confirming MDR family membership. The annotation is thus well-supported by family-level biochemistry even though the specific evidence code is computational transfer.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence displays hallmark features of the medium-chain dehydrogenase/reductase (MDR) superfamily: a Rossmann-fold NAD(P)-binding motif (GATMGS…GVGRKS) and a conspicuous cysteine cluster (SCGKCDDCVNDRECYCPE) in the central region. MDR enzymes, including alcohol dehydrogenases and cinnamyl alcohol dehydrogenases (CAD), are classic Zn(2+)-dependent enzymes where a catalytic zinc ion coordinates the substrate. The cysteine cluster is a concrete, observable sequence feature pointing to zinc coordination. Pantetheine 4'-phosphate (A) is associated with acyl carrier proteins/fatty-acid synthase, entirely unrelated to this fold. Fe cation (D) is associated with cytochromes and iron-sulfur proteins, not MDR enzymes. NAD+ (C) is a co-substrate (consumed and regenerated) in MDR dehydrogenases, not a tightly-bound catalytic cofactor; standard biochemical nomenclature reserves 'cofactor' for the metal ion. Thus, family-level MDR/ADH/CAD knowledge plus the visible cysteine cluster meaningfully distinguishes Zn(2+) from all three distractors.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the MDR/ADH-like fold from the Rossmann motif and cysteine cluster, recall that this enzyme family is Zn-dependent, and apply the standard cofactor-vs-co-substrate distinction to exclude NAD+. This is legitimate transferable family knowledge, not target-specific memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While NAD+ is involved in the catalytic mechanism of MDR enzymes, it is a co-substrate (consumed per turnover), not a cofactor in the strict biochemical sense. The question asks for the 'cofactor,' and the standard distinction cleanly selects Zn(2+). Pantetheine 4'-phosphate and Fe are clearly irrelevant to this fold. No genuine ambiguity remains among the offered choices.


### Important caveats

- The Zn(2+) cofactor annotation carries evidence code ECO:0000250 (similarity-based transfer from Populus CAD P06525), not direct experimental measurement on this specific protein.
- The protein's EC classification is 1.3.1.73 (recommended, by similarity) with an alternative EC 1.5.1.- (by direct assay, PubMed 26715562), indicating some uncertainty in the exact reaction classification, though this does not affect the Zn-dependence.
- The sequence is 363 aa and matches the UniProt entry A0A0U4BHM2 exactly; the reviewer-only accession and organism identity were not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence displays hallmark features of the medium-chain dehydrogenase/reductase (MDR) superfamily: a Rossmann-fold NAD(P)-binding motif (GATMGS…GVGRKS) and a conspicuous cysteine cluster (SCGKCDDCVNDRECYCPE) in the central region. MDR enzymes, including alcohol dehydrogenases and cinnamyl alcohol dehydrogenases (CAD), are classic Zn(2+)-dependent enzymes where a catalytic zinc ion coordinates the substrate. The cysteine cluster is a concrete, observable sequence feature pointing to zinc coordination. Pantetheine 4'-phosphate (A) is associated with acyl carrier proteins/fatty-acid synthase, entirely unrelated to this fold. Fe cation (D) is associated with cytochromes and iron-sulfur proteins, not MDR enzymes. NAD+ (C) is a co-substrate (consumed and regenerated) in MDR dehydrogenases, not a tightly-bound catalytic cofactor; standard biochemical nomenclature reserves 'cofactor' for the metal ion. Thus, family-level MDR/ADH/CAD knowledge plus the visible cysteine cluster meaningfully distinguishes Zn(2+) from all three distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the MDR/ADH-like fold from the Rossmann motif and cysteine cluster, recall that this enzyme family is Zn-dependent, and apply the standard cofactor-vs-co-substrate distinction to exclude NAD+. This is legitimate transferable family knowledge, not target-specific memorization."
  },
  "case_id": "cofactor_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists Zn(2+) as the cofactor, binding 2 Zn(2+) ions per subunit. The evidence code is ECO:0000250 (inferred by similarity to P06525, a Populus cinnamyl alcohol dehydrogenase), so this is a transferred annotation rather than direct experimental proof for this specific protein. However, the protein is independently confirmed as a CAD-like reductase (paper title, PubMed 26715562), and CAD enzymes in the MDR superfamily are well-established Zn-dependent enzymes. The sequence contains a characteristic cysteine cluster (SCGKCDDCVNDRECYCPE) consistent with zinc coordination in MDR enzymes, and Rossmann-fold motifs (GATMGS, GVGRKS) confirming MDR family membership. The annotation is thus well-supported by family-level biochemistry even though the specific evidence code is computational transfer."
  },
  "important_caveats": [
    "The Zn(2+) cofactor annotation carries evidence code ECO:0000250 (similarity-based transfer from Populus CAD P06525), not direct experimental measurement on this specific protein.",
    "The protein's EC classification is 1.3.1.73 (recommended, by similarity) with an alternative EC 1.5.1.- (by direct assay, PubMed 26715562), indicating some uncertainty in the exact reaction classification, though this does not affect the Zn-dependence.",
    "The sequence is 363 aa and matches the UniProt entry A0A0U4BHM2 exactly; the reviewer-only accession and organism identity were not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While NAD+ is involved in the catalytic mechanism of MDR enzymes, it is a co-substrate (consumed per turnover), not a cofactor in the strict biochemical sense. The question asks for the 'cofactor,' and the standard distinction cleanly selects Zn(2+). Pantetheine 4'-phosphate and Fe are clearly irrelevant to this fold. No genuine ambiguity remains among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists Zn(2+) as the cofactor, binding 2 Zn(2+) ions per subunit. The evidence code is ECO:0000250 (inferred by similarity to P06525, a Populus cinnamyl alcohol dehydrogenase), so this is a transferred annotation rather than direct experimental proof for this specific protein. However, the protein is independently confirmed as a CAD-like reductase (paper title, PubMed 26715562), and CAD enzymes in the MDR superfamily are well-established Zn-dependent enzymes. The sequence contains a characteristic cysteine cluster (SCGKCDDCVNDRECYCPE) consistent with zinc coordination in MDR enzymes, and Rossmann-fold motifs (GATMGS, GVGRKS) confirming MDR family membership. The annotation is thus well-supported by family-level biochemistry even though the specific evidence code is computational transfer.",
    "evidence_ids": ["C5", "H4", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence displays hallmark features of the medium-chain dehydrogenase/reductase (MDR) superfamily: a Rossmann-fold NAD(P)-binding motif (GATMGS…GVGRKS) and a conspicuous cysteine cluster (SCGKCDDCVNDRECYCPE) in the central region. MDR enzymes, including alcohol dehydrogenases and cinnamyl alcohol dehydrogenases (CAD), are classic Zn(2+)-dependent enzymes where a catalytic zinc ion coordinates the substrate. The cysteine cluster is a concrete, observable sequence feature pointing to zinc coordination. Pantetheine 4'-phosphate (A) is associated with acyl carrier proteins/fatty-acid synthase, entirely unrelated to this fold. Fe cation (D) is associated with cytochromes and iron-sulfur proteins, not MDR enzymes. NAD+ (C) is a co-substrate (consumed and regenerated) in MDR dehydrogenases, not a tightly-bound catalytic cofactor; standard biochemical nomenclature reserves 'cofactor' for the metal ion. Thus, family-level MDR/ADH/CAD knowledge plus the visible cysteine cluster meaningfully distinguishes Zn(2+) from all three distractors.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the MDR/ADH-like fold from the Rossmann motif and cysteine cluster, recall that this enzyme family is Zn-dependent, and apply the standard cofactor-vs-co-substrate distinction to exclude NAD+. This is legitimate transferable family knowledge, not target-specific memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While NAD+ is involved in the catalytic mechanism of MDR enzymes, it is a co-substrate (consumed per turnover), not a cofactor in the strict biochemical sense. The question asks for the 'cofactor,' and the standard distinction cleanly selects Zn(2+). Pantetheine 4'-phosphate and Fe are clearly irrelevant to this fold. No genuine ambiguity remains among the offered choices."
  },
  "important_caveats": [
    "The Zn(2+) cofactor annotation carries evidence code ECO:0000250 (similarity-based transfer from Populus CAD P06525), not direct experimental measurement on this specific protein.",
    "The protein's EC classification is 1.3.1.73 (recommended, by similarity) with an alternative EC 1.5.1.- (by direct assay, PubMed 26715562), indicating some uncertainty in the exact reaction classification, though this does not affect the Zn-dependence.",
    "The sequence is 363 aa and matches the UniProt entry A0A0U4BHM2 exactly; the reviewer-only accession and organism identity were not available to the evaluated model."
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
  "benchmark_sequence_length": 363,
  "benchmark_sequence_sha256": "351c34d2095e544533593a3430ee8d4f870ed8068eab99c7a6c309e20ddfb657",
  "current_entry_audit": {
    "entryVersion": 32,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-03-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 363,
  "current_source_sequence_sha256": "351c34d2095e544533593a3430ee8d4f870ed8068eab99c7a6c309e20ddfb657",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 30,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0U4BHM2",
  "selected_historical_entry_version": 30,
  "selected_historical_record_sha256": "f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634",
  "selected_historical_source_sequence_length": 363,
  "selected_historical_source_sequence_sha256": "351c34d2095e544533593a3430ee8d4f870ed8068eab99c7a6c309e20ddfb657",
  "selected_historical_version": {
    "accession": "A0A0U4BHM2",
    "database": "Swiss-Prot",
    "entryVersion": 30,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHVOR_RAUTE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0U4BHM2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:23.340033+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":32,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-03-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:23.340033+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Be still tree\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia tetraphylla\",\"taxonId\":545371}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:23.340033+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Protein RR2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RtRR2\"}]},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Vomilenine reductase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RtVR2\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0U3S9Q3\",\"source\":\"UniProtKB\"}],\"value\":\"1.3.1.73\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"1,2-Dihydrovomilenine reductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RtDHVR\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:23.340033+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P06525\",\"source\":\"UniProtKB\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P06525\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 2 Zn(2+) ions per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:24:23.340033+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Geissler M.\",\"Burghard M.\",\"Volk J.\",\"Staniek A.\",\"Warzecha H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26715562\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00425-015-2446-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"813\",\"id\":\"26715562\",\"journal\":\"Planta\",\"lastPage\":\"824\",\"publicationDate\":\"2016\",\"title\":\"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\",\"volume\":\"243\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ALW82982.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"PROTEIN SEQUENCE OF 14-26 AND 149-156\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:24:23.340033+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c26b85d02403fbdfc042529d2261359bc369b05deb9442cd6e55153bd5141c6f",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U4BHM2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H1",
  "excerpt": "ID   DHVOR_RAUTE             Reviewed;         363 AA.\nAC   A0A0U4BHM2;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-MAR-2016, sequence version 1.\nDT   28-JAN-2026, entry version 30.\nDE   RecName: Full=1,2-Dihydrovomilenine reductase {ECO:0000303|PubMed:26715562};\nDE            Short=RtDHVR {ECO:0000303|PubMed:26715562};\nDE            EC=1.3.1.73 {ECO:0000250|UniProtKB:A0A0U3S9Q3};\nDE   AltName: Full=Protein RR2 {ECO:0000303|PubMed:26715562};\nDE            Short=RtRR2 {ECO:0000303|PubMed:26715562};\nDE   AltName: Full=Vomilenine reductase 2 {ECO:0000303|PubMed:26715562};\nDE            Short=RtVR2 {ECO:0000303|PubMed:26715562};\nDE            EC=1.5.1.- {ECO:0000269|PubMed:26715562};\nGN   Name=DHVR {ECO:0000303|PubMed:26715562};\nGN   Synonyms=RR2 {ECO:0000303|PubMed:26715562},\nGN   VR2 {ECO:0000303|PubMed:26715562};\nOS   Rauvolfia tetraphylla (Be still tree).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=545371;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:25.840272+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634",
  "url": "https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=1,2-Dihydrovomilenine reductase {ECO:0000303|PubMed:26715562};\nDE            Short=RtDHVR {ECO:0000303|PubMed:26715562};\nDE            EC=1.3.1.73 {ECO:0000250|UniProtKB:A0A0U3S9Q3};\nDE   AltName: Full=Protein RR2 {ECO:0000303|PubMed:26715562};\nDE            Short=RtRR2 {ECO:0000303|PubMed:26715562};\nDE   AltName: Full=Vomilenine reductase 2 {ECO:0000303|PubMed:26715562};\nDE            Short=RtVR2 {ECO:0000303|PubMed:26715562};\nDE            EC=1.5.1.- {ECO:0000269|PubMed:26715562};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:25.840272+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634",
  "url": "https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ALW82982.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], PROTEIN SEQUENCE OF 14-26 AND 149-156,\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=26715562; DOI=10.1007/s00425-015-2446-6;\nRA   Geissler M., Burghard M., Volk J., Staniek A., Warzecha H.;\nRT   \"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to\nRT   the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\";\nRL   Planta 243:813-824(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:25.840272+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634",
  "url": "https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000250|UniProtKB:P06525};\nCC       Note=Binds 2 Zn(2+) ions per subunit. {ECO:0000250|UniProtKB:P06525};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:25.840272+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 54-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f1ca3ed3dfca81ae192adab6c5b2e6c70586c275e9a49b6b2913846785e88634",
  "url": "https://rest.uniprot.org/unisave/A0A0U4BHM2?format=txt&versions=30"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 12. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
