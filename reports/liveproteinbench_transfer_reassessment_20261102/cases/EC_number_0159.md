# EC_number_0159

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0159.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 4.2.1.121

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSTSNGSTENIQKPLRKIPDITGTPILTAIKDRLDFFYNQGQYEYFQSRVKKNNSTILRMNMIPGPFASNPKIVALCDAASFPTLFDPSKVSKVNSLTGNYMPALSFTGGYRVCAYLDPSEPTHTKIKQVFFNAQAAKKDTFIPTFVSTFNSMFDKMDAEVESKKKAEFTKFNEAAVFEFVGLALVGPKPAREVFDSAKKSVFFQFHPFITAGLPALVEELAFHMFPFPSFVAKSSYKILYEYFSTGGSWILDNAEEIGLSREEAIHHLIFTWAINAYLGIRTCLMRLFKWIVASGPDLQEKLAREVRSVVRSEEGKITFAGIEKMELVKSVAYESFRFDPPVQVQYGTAKSDLIIESHDGKYQVKKGEMLCGFQPMATRDPKVFDRADEFVPDRFMGDGKKLVKHVLWANGYGTDAPKADDKICAGKDLGVLVGRLLIAVMFLRYDKIGGVVGKTMEEVDVIVNELTKVAV

[Multiple Choices]
A. 4.2.1.18
B. 1.1.1.138
C. 4.2.1.121
D. 5.4.99.14
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

> The sequence-matched UniProt record reports EC 4.2.1.121 for experimentally supported colneleate-forming reactions. The key is therefore supported, although the record also assigns this protein another EC number.

Citations as saved: [C4](#evidence-c4), [C7](#evidence-c7), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 472-aa sequence is consistent with a plant CYP74-type oxylipin enzyme. Transferable family knowledge makes a lipid-hydroperoxide lyase/synthase EC option more plausible than the offered alcohol dehydrogenase or isomerase, and distinguishes it from the unrelated fumarate hydratase option. Among these choices, C is the CYP74-associated alternative. This supports a probabilistic choice, not a sequence-only proof of its precise substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition meaningfully distinguishes C from the actual alternatives; exact knowledge of this protein's recorded EC annotation is not necessary for that choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source reports an additional EC activity, 4.2.1.183, but it is not among the offered options. No other offered choice is comparably supported.


### Important caveats

- The protein is annotated with both EC 4.2.1.121 and EC 4.2.1.183, so the singular wording does not capture all reported activities.
- The source record matches the supplied sequence and cites experimental evidence, but the exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 472-aa sequence is consistent with a plant CYP74-type oxylipin enzyme. Transferable family knowledge makes a lipid-hydroperoxide lyase/synthase EC option more plausible than the offered alcohol dehydrogenase or isomerase, and distinguishes it from the unrelated fumarate hydratase option. Among these choices, C is the CYP74-associated alternative. This supports a probabilistic choice, not a sequence-only proof of its precise substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition meaningfully distinguishes C from the actual alternatives; exact knowledge of this protein's recorded EC annotation is not necessary for that choice."
  },
  "case_id": "EC_number_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C7",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports EC 4.2.1.121 for experimentally supported colneleate-forming reactions. The key is therefore supported, although the record also assigns this protein another EC number."
  },
  "important_caveats": [
    "The protein is annotated with both EC 4.2.1.121 and EC 4.2.1.183, so the singular wording does not capture all reported activities.",
    "The source record matches the supplied sequence and cites experimental evidence, but the exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source reports an additional EC activity, 4.2.1.183, but it is not among the offered options. No other offered choice is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports EC 4.2.1.121 for experimentally supported colneleate-forming reactions. The key is therefore supported, although the record also assigns this protein another EC number.",
    "evidence_ids": ["C4", "C7", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 472-aa sequence is consistent with a plant CYP74-type oxylipin enzyme. Transferable family knowledge makes a lipid-hydroperoxide lyase/synthase EC option more plausible than the offered alcohol dehydrogenase or isomerase, and distinguishes it from the unrelated fumarate hydratase option. Among these choices, C is the CYP74-associated alternative. This supports a probabilistic choice, not a sequence-only proof of its precise substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition meaningfully distinguishes C from the actual alternatives; exact knowledge of this protein's recorded EC annotation is not necessary for that choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source reports an additional EC activity, 4.2.1.183, but it is not among the offered options. No other offered choice is comparably supported."
  },
  "important_caveats": [
    "The protein is annotated with both EC 4.2.1.121 and EC 4.2.1.183, so the singular wording does not capture all reported activities.",
    "The source record matches the supplied sequence and cites experimental evidence, but the exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q2WE96 (CP74_ALLSA, Divinyl ether synthase CYP74 from Allium sativum) is annotated with EC 4.2.1.121 (Colneleate synthase) under experimental evidence (ECO:0000269, PubMed:18326559). The catalytic activity comments explicitly list EC 4.2.1.121 for the reaction converting (9S)-hydroperoxy-(10E,12Z)-octadecadienoate to colneleate + H2O. The sequence matches the benchmark input exactly (472 AA, sha256 match confirmed). EC 4.2.1.121 is one of two experimentally verified EC numbers for this enzyme (the other being 4.2.1.183, not among the choices).

Citations as saved: [C4](#evidence-c4), [C7](#evidence-c7), [C8](#evidence-c8), [H2](#evidence-h2), [H9](#evidence-h9), [H10](#evidence-h10).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~472 AA) displays cytochrome P450 architecture recognizable from conserved motifs: a hydrophobic I-helix region, the heme-ligating Cys-containing FGPR-like motif near the C-terminus, and the overall length/fold consistent with plant CYP74 enzymes. CYP74 family members are hydroperoxide-metabolizing enzymes classified in EC class 4.2.1.x (hydro-lyases). This family-level knowledge immediately eliminates B (EC 1.1.1.138, an oxidoreductase/alcohol dehydrogenase requiring a Rossmann fold and Zn-binding motif absent here) and D (EC 5.4.99.14, an isomerase). Between A (4.2.1.18) and C (4.2.1.121): EC 4.2.1.18 is a deprecated, generic 'hydro-lyase' classification not assigned to any CYP74 enzyme in current databases. CYP74 enzymes carry specific EC numbers (4.2.1.92 for AOS, 4.2.1.77 for HPL, 4.2.1.121 for divinyl ether synthase/colneleate synthase, 4.2.1.183 for etheroleic acid synthase). Since only 4.2.1.121 among the choices is a recognized CYP74 EC number, family-level inference distinguishes C from A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the P450/CYP74 fold from sequence motifs and knowledge that CYP74 enzymes are hydroperoxide-metabolizing lyases (EC 4.2.1.x class) with specific EC numbers eliminates B and D. Knowledge that EC 4.2.1.18 is a generic/deprecated number not used for CYP74 enzymes eliminates A. Only 4.2.1.121 (a specific CYP74/divinyl ether synthase EC number) remains among the offered choices. This inference relies on family-level P450 biology and EC nomenclature conventions, not on memorizing this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the protein has dual EC activity (4.2.1.121 and 4.2.1.183), only 4.2.1.121 is offered among the choices. The other three options (4.2.1.18, 1.1.1.138, 5.4.99.14) are clearly eliminable by family-level reasoning. No ambiguity among the offered alternatives.


### Important caveats

- The protein also has experimentally verified EC 4.2.1.183 activity (etheroleic acid synthase), but this EC number is not among the choices, so it does not create ambiguity.
- Distinguishing the specific CYP74 subfamily member (DES vs AOS vs HPL) from sequence alone is non-trivial, but since only one CYP74 EC number (4.2.1.121) is offered, sub-family discrimination is not required to answer correctly.
- The EC 4.2.1.121 annotation is supported by a single experimental reference (PubMed:18326559), while EC 4.2.1.183 has four supporting references. The choice of 4.2.1.121 as the 'expected' answer reflects the recommended/primary annotation in UniProt rather than the most extensively characterized activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~472 AA) displays cytochrome P450 architecture recognizable from conserved motifs: a hydrophobic I-helix region, the heme-ligating Cys-containing FGPR-like motif near the C-terminus, and the overall length/fold consistent with plant CYP74 enzymes. CYP74 family members are hydroperoxide-metabolizing enzymes classified in EC class 4.2.1.x (hydro-lyases). This family-level knowledge immediately eliminates B (EC 1.1.1.138, an oxidoreductase/alcohol dehydrogenase requiring a Rossmann fold and Zn-binding motif absent here) and D (EC 5.4.99.14, an isomerase). Between A (4.2.1.18) and C (4.2.1.121): EC 4.2.1.18 is a deprecated, generic 'hydro-lyase' classification not assigned to any CYP74 enzyme in current databases. CYP74 enzymes carry specific EC numbers (4.2.1.92 for AOS, 4.2.1.77 for HPL, 4.2.1.121 for divinyl ether synthase/colneleate synthase, 4.2.1.183 for etheroleic acid synthase). Since only 4.2.1.121 among the choices is a recognized CYP74 EC number, family-level inference distinguishes C from A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the P450/CYP74 fold from sequence motifs and knowledge that CYP74 enzymes are hydroperoxide-metabolizing lyases (EC 4.2.1.x class) with specific EC numbers eliminates B and D. Knowledge that EC 4.2.1.18 is a generic/deprecated number not used for CYP74 enzymes eliminates A. Only 4.2.1.121 (a specific CYP74/divinyl ether synthase EC number) remains among the offered choices. This inference relies on family-level P450 biology and EC nomenclature conventions, not on memorizing this specific protein's annotation."
  },
  "case_id": "EC_number_0159",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C7",
      "C8",
      "H2",
      "H9",
      "H10"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q2WE96 (CP74_ALLSA, Divinyl ether synthase CYP74 from Allium sativum) is annotated with EC 4.2.1.121 (Colneleate synthase) under experimental evidence (ECO:0000269, PubMed:18326559). The catalytic activity comments explicitly list EC 4.2.1.121 for the reaction converting (9S)-hydroperoxy-(10E,12Z)-octadecadienoate to colneleate + H2O. The sequence matches the benchmark input exactly (472 AA, sha256 match confirmed). EC 4.2.1.121 is one of two experimentally verified EC numbers for this enzyme (the other being 4.2.1.183, not among the choices)."
  },
  "important_caveats": [
    "The protein also has experimentally verified EC 4.2.1.183 activity (etheroleic acid synthase), but this EC number is not among the choices, so it does not create ambiguity.",
    "Distinguishing the specific CYP74 subfamily member (DES vs AOS vs HPL) from sequence alone is non-trivial, but since only one CYP74 EC number (4.2.1.121) is offered, sub-family discrimination is not required to answer correctly.",
    "The EC 4.2.1.121 annotation is supported by a single experimental reference (PubMed:18326559), while EC 4.2.1.183 has four supporting references. The choice of 4.2.1.121 as the 'expected' answer reflects the recommended/primary annotation in UniProt rather than the most extensively characterized activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein has dual EC activity (4.2.1.121 and 4.2.1.183), only 4.2.1.121 is offered among the choices. The other three options (4.2.1.18, 1.1.1.138, 5.4.99.14) are clearly eliminable by family-level reasoning. No ambiguity among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0159",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q2WE96 (CP74_ALLSA, Divinyl ether synthase CYP74 from Allium sativum) is annotated with EC 4.2.1.121 (Colneleate synthase) under experimental evidence (ECO:0000269, PubMed:18326559). The catalytic activity comments explicitly list EC 4.2.1.121 for the reaction converting (9S)-hydroperoxy-(10E,12Z)-octadecadienoate to colneleate + H2O. The sequence matches the benchmark input exactly (472 AA, sha256 match confirmed). EC 4.2.1.121 is one of two experimentally verified EC numbers for this enzyme (the other being 4.2.1.183, not among the choices).",
    "evidence_ids": ["C4", "C7", "C8", "H2", "H9", "H10"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~472 AA) displays cytochrome P450 architecture recognizable from conserved motifs: a hydrophobic I-helix region, the heme-ligating Cys-containing FGPR-like motif near the C-terminus, and the overall length/fold consistent with plant CYP74 enzymes. CYP74 family members are hydroperoxide-metabolizing enzymes classified in EC class 4.2.1.x (hydro-lyases). This family-level knowledge immediately eliminates B (EC 1.1.1.138, an oxidoreductase/alcohol dehydrogenase requiring a Rossmann fold and Zn-binding motif absent here) and D (EC 5.4.99.14, an isomerase). Between A (4.2.1.18) and C (4.2.1.121): EC 4.2.1.18 is a deprecated, generic 'hydro-lyase' classification not assigned to any CYP74 enzyme in current databases. CYP74 enzymes carry specific EC numbers (4.2.1.92 for AOS, 4.2.1.77 for HPL, 4.2.1.121 for divinyl ether synthase/colneleate synthase, 4.2.1.183 for etheroleic acid synthase). Since only 4.2.1.121 among the choices is a recognized CYP74 EC number, family-level inference distinguishes C from A.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the P450/CYP74 fold from sequence motifs and knowledge that CYP74 enzymes are hydroperoxide-metabolizing lyases (EC 4.2.1.x class) with specific EC numbers eliminates B and D. Knowledge that EC 4.2.1.18 is a generic/deprecated number not used for CYP74 enzymes eliminates A. Only 4.2.1.121 (a specific CYP74/divinyl ether synthase EC number) remains among the offered choices. This inference relies on family-level P450 biology and EC nomenclature conventions, not on memorizing this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the protein has dual EC activity (4.2.1.121 and 4.2.1.183), only 4.2.1.121 is offered among the choices. The other three options (4.2.1.18, 1.1.1.138, 5.4.99.14) are clearly eliminable by family-level reasoning. No ambiguity among the offered alternatives."
  },
  "important_caveats": [
    "The protein also has experimentally verified EC 4.2.1.183 activity (etheroleic acid synthase), but this EC number is not among the choices, so it does not create ambiguity.",
    "Distinguishing the specific CYP74 subfamily member (DES vs AOS vs HPL) from sequence alone is non-trivial, but since only one CYP74 EC number (4.2.1.121) is offered, sub-family discrimination is not required to answer correctly.",
    "The EC 4.2.1.121 annotation is supported by a single experimental reference (PubMed:18326559), while EC 4.2.1.183 has four supporting references. The choice of 4.2.1.121 as the 'expected' answer reflects the recommended/primary annotation in UniProt rather than the most extensively characterized activity."
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
  "benchmark_sequence_length": 472,
  "benchmark_sequence_sha256": "cc94de63a12f978e7f97483dcbf56ff963db7489be85ed11fc3191fd4619fd2a",
  "current_entry_audit": {
    "entryVersion": 77,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-01-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 472,
  "current_source_sequence_sha256": "cc94de63a12f978e7f97483dcbf56ff963db7489be85ed11fc3191fd4619fd2a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 75,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q2WE96",
  "selected_historical_entry_version": 75,
  "selected_historical_record_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "selected_historical_source_sequence_length": 472,
  "selected_historical_source_sequence_sha256": "cc94de63a12f978e7f97483dcbf56ff963db7489be85ed11fc3191fd4619fd2a",
  "selected_historical_version": {
    "accession": "Q2WE96",
    "database": "Swiss-Prot",
    "entryVersion": 75,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CP74_ALLSA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q2WE96\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":77,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-01-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Garlic\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"Liliopsida\",\"Asparagales\",\"Amaryllidaceae\",\"Allioideae\",\"Allieae\",\"Allium\"],\"scientificName\":\"Allium sativum\",\"taxonId\":4682}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.121\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"value\":\"Colneleate synthase\"}},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18326559\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"7672118\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"8690066\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9128734\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.183\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"value\":\"Etheroleic acid synthase CYP74\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"value\":\"Divinyl ether synthase CYP74\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"value\":\"AsDES\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79276\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.183\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18326559\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"7672118\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"8690066\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9128734\",\"source\":\"PubMed\"}],\"name\":\"(13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79275\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57466\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:229759\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79272\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.183\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18326559\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"7672118\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"8690066\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"9128734\",\"source\":\"PubMed\"}],\"name\":\"(13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79271\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58757\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:229758\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:28175\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.121\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"name\":\"(9S)-hydroperoxy-(10E,12Z)-octadecadienoate = colneleate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:28174\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:60955\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:60957\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:28179\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.121\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18326559\",\"source\":\"PubMed\"}],\"name\":\"(9S)-hydroperoxy-(10E,12Z,15Z)-octadecatrienoate = colnelenate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:28178\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:60960\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:60962\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Stumpe M.\",\"Carsjens J.G.\",\"Goebel C.\",\"Feussner I.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18326559\"},{\"database\":\"DOI\",\"id\":\"10.1093/jxb/ern010\"}],\"citationType\":\"journal article\",\"firstPage\":\"907\",\"id\":\"18326559\",\"journal\":\"J. Exp. Bot.\",\"lastPage\":\"915\",\"publicationDate\":\"2008\",\"title\":\"Divinyl ether synthesis in garlic bulbs.\",\"volume\":\"59\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Grechkin A.N.\",\"Fazliev F.N.\",\"Mukhtarova L.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"7672118\"},{\"database\":\"DOI\",\"id\":\"10.1016/0014-5793(95)00895-g\"}],\"citationType\":\"journal article\",\"firstPage\":\"159\",\"id\":\"7672118\",\"journal\":\"FEBS Lett.\",\"lastPage\":\"162\",\"publicationDate\":\"1995\",\"title\":\"The lipoxygenase pathway in garlic (Allium sativum L.) bulbs: detection of the novel divinyl ether oxylipins.\",\"volume\":\"371\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Grechkin A.N.\",\"Hamberg M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"8690066\"},{\"database\":\"DOI\",\"id\":\"10.1016/0014-5793(96)00536-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"112\",\"id\":\"8690066\",\"journal\":\"FEBS Lett.\",\"lastPage\":\"114\",\"publicationDate\":\"1996\",\"title\":\"Divinyl ether synthase from garlic (Allium sativum L.) bulbs: sub-cellular localization and substrate regio-and stereospecificity.\",\"volume\":\"388\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2WE96.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Grechkin A.N.\",\"Ilyasov A.V.\",\"Hamberg M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"9128734\"},{\"database\":\"DOI\",\"id\":\"10.1111/j.1432-1033.1997.00137.x\"}],\"citationType\":\"journal article\",\"firstPage\":\"137\",\"id\":\"9128734\",\"journal\":\"Eur. J. Biochem.\",\"lastPage\":\"142\",\"publicationDate\":\"1997\",\"title\":\"On the mechanism of biosynthesis of divinyl ether oxylipins by enzyme from garlic bulbs.\",\"volume\":\"245\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:30:45.939008+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fc101e59b646632c56412a88dd991512655f84d6ab0a59b5df563fac508adb41",
  "url": "https://rest.uniprot.org/uniprotkb/Q2WE96.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H1",
  "excerpt": "ID   CP74_ALLSA              Reviewed;         472 AA.\nAC   Q2WE96;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-JAN-2006, sequence version 1.\nDT   28-JAN-2026, entry version 75.\nDE   RecName: Full=Divinyl ether synthase CYP74 {ECO:0000303|PubMed:18326559};\nDE            Short=AsDES {ECO:0000303|PubMed:18326559};\nDE   AltName: Full=Colneleate synthase {ECO:0000303|PubMed:18326559};\nDE            EC=4.2.1.121 {ECO:0000269|PubMed:18326559};\nDE   AltName: Full=Etheroleic acid synthase CYP74 {ECO:0000305|PubMed:18326559};\nDE            EC=4.2.1.183 {ECO:0000269|PubMed:18326559, ECO:0000269|PubMed:7672118, ECO:0000269|PubMed:8690066, ECO:0000269|PubMed:9128734};\nGN   Name=CYP74 {ECO:0000303|PubMed:18326559};\nGN   Synonyms=DES {ECO:0000303|PubMed:18326559};\nOS   Allium sativum (Garlic).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; Liliopsida; Asparagales; Amaryllidaceae;\nOC   Allioideae; Allieae; Allium.\nOX   NCBI_TaxID=4682;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Divinyl ether synthase CYP74 {ECO:0000303|PubMed:18326559};\nDE            Short=AsDES {ECO:0000303|PubMed:18326559};\nDE   AltName: Full=Colneleate synthase {ECO:0000303|PubMed:18326559};\nDE            EC=4.2.1.121 {ECO:0000269|PubMed:18326559};\nDE   AltName: Full=Etheroleic acid synthase CYP74 {ECO:0000305|PubMed:18326559};\nDE            EC=4.2.1.183 {ECO:0000269|PubMed:18326559, ECO:0000269|PubMed:7672118, ECO:0000269|PubMed:8690066, ECO:0000269|PubMed:9128734};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, TISSUE SPECIFICITY, AND INDUCTION.\nRX   PubMed=18326559; DOI=10.1093/jxb/ern010;\nRA   Stumpe M., Carsjens J.G., Goebel C., Feussner I.;\nRT   \"Divinyl ether synthesis in garlic bulbs.\";\nRL   J. Exp. Bot. 59:907-915(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=7672118; DOI=10.1016/0014-5793(95)00895-g;\nRA   Grechkin A.N., Fazliev F.N., Mukhtarova L.S.;\nRT   \"The lipoxygenase pathway in garlic (Allium sativum L.) bulbs: detection of\nRT   the novel divinyl ether oxylipins.\";\nRL   FEBS Lett. 371:159-162(1995).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H5",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=8690066; DOI=10.1016/0014-5793(96)00536-4;\nRA   Grechkin A.N., Hamberg M.;\nRT   \"Divinyl ether synthase from garlic (Allium sativum L.) bulbs: sub-cellular\nRT   localization and substrate regio-and stereospecificity.\";\nRL   FEBS Lett. 388:112-114(1996).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H6",
  "excerpt": "RN   [4]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=9128734; DOI=10.1111/j.1432-1033.1997.00137.x;\nRA   Grechkin A.N., Ilyasov A.V., Hamberg M.;\nRT   \"On the mechanism of biosynthesis of divinyl ether oxylipins by enzyme from\nRT   garlic bulbs.\";\nRL   Eur. J. Biochem. 245:137-142(1997).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(13S)-hydroperoxy-(9Z,11E)-octadecadienoate = etheroleate +\nCC         H2O; Xref=Rhea:RHEA:79275, ChEBI:CHEBI:15377, ChEBI:CHEBI:57466,\nCC         ChEBI:CHEBI:229759; EC=4.2.1.183;\nCC         Evidence={ECO:0000269|PubMed:18326559, ECO:0000269|PubMed:7672118,\nCC         ECO:0000269|PubMed:8690066, ECO:0000269|PubMed:9128734};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79276;\nCC         Evidence={ECO:0000269|PubMed:18326559};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate =\nCC         etherolenate + H2O; Xref=Rhea:RHEA:79271, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:58757, ChEBI:CHEBI:229758; EC=4.2.1.183;\nCC         Evidence={ECO:0000269|PubMed:18326559, ECO:0000269|PubMed:7672118,\nCC         ECO:0000269|PubMed:8690066, ECO:0000269|PubMed:9128734};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79272;\nCC         Evidence={ECO:0000269|PubMed:18326559};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 66-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H9",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(9S)-hydroperoxy-(10E,12Z)-octadecadienoate = colneleate +\nCC         H2O; Xref=Rhea:RHEA:28174, ChEBI:CHEBI:15377, ChEBI:CHEBI:60955,\nCC         ChEBI:CHEBI:60957; EC=4.2.1.121;\nCC         Evidence={ECO:0000269|PubMed:18326559};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:28175;\nCC         Evidence={ECO:0000269|PubMed:18326559};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-80",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75)

```json
{
  "entry_version": 75,
  "evidence_id": "H10",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(9S)-hydroperoxy-(10E,12Z,15Z)-octadecatrienoate = colnelenate\nCC         + H2O; Xref=Rhea:RHEA:28178, ChEBI:CHEBI:15377, ChEBI:CHEBI:60960,\nCC         ChEBI:CHEBI:60962; EC=4.2.1.121;\nCC         Evidence={ECO:0000269|PubMed:18326559};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:28179;\nCC         Evidence={ECO:0000269|PubMed:18326559};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.045519+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-87",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "529eee09b919f3b5788669e694368548dd1426b011a34543db2180899628437e",
  "url": "https://rest.uniprot.org/unisave/Q2WE96?format=txt&versions=75"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 159. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
