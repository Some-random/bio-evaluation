# EC_number_0113

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0113.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 5.6.1.1

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLDKLSKHKTMFYERVKEIDQILFSQQQAKQTQLDNLSNNNASGGFFSGFMKMFSPLSTPPNSSSNNNSNTQQAISQETRKLCSVNNNRHEPIYNQYTTNSQVIRSFPAVSSIGQSSTNMYNSVNICDGISSSEKRSPTPPRNRSNSNDKILFGHYDALGSLPQNNMGHYQQPPQQSSQQQQQPLVPKQNSVTALRNTTSATSSTTTANNKKPSLDQIPELKGVDRKLLDHILNEVIETKTTNWDDIAGLKDAKQTLLETVILPSIRPDLFNGLRAPCRGILLFGPPGTGKTMIARACASQCNATFFSISAGSLVSKYHGEGEKLVRCLFAAARYLQPSVIFIDEIDSILSARSSEEHEASRRMKTEFMIQMDGVSNMNGKEDRVLVMGATNIPTELDEAILRRFTKRIYIPLPDHAARASLIKQLSHGQNMSLSETDINKICVATEGFSGSDLTALCKETSMVPLREISMDQLISIDARKIRPIVLKDFQSSLVHVRPSTSQDTIKKLEKWNESYGTFAKGI

[Multiple Choices]
A. 5.6.1.1
B. 5.4.99.14
C. 1.2.1.46
D. 4.1.1.129
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

> The exact sequence-matched UniProt record assigns EC 5.6.1.1 to spastin and describes ATP-dependent microtubule severing. The assignment is supported, though its cited evidence is transferred from a related protein rather than direct experimental evidence for this sequence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a C-terminal AAA+ ATPase-like region, including a Walker A nucleotide-binding motif (…GPPGTGKT), alongside a long low-complexity N-terminal region consistent with a regulatory portion of an ATP-driven remodeling protein. Among the options, EC 5.6.1.1 is the ATP-dependent protein-remodeling choice; the other options classify distinct isomerase, oxidoreductase, and lyase activities. This supports A without needing the exact protein annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of AAA+ ATPases and their ATP-dependent remodeling activities, together with the sequence motifs and the offered alternatives, meaningfully distinguishes A. The motif alone would not prove a specific substrate or EC assignment, but the alternatives make the inference credible.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence evidence and the offered EC classes support A; no other option is comparably defensible.


### Important caveats

- The reviewer evidence identifies the annotation as inferred by similarity (ECO:0000250), not as an experimentally established activity for this exact protein.
- The supplied evidence matches the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a C-terminal AAA+ ATPase-like region, including a Walker A nucleotide-binding motif (…GPPGTGKT), alongside a long low-complexity N-terminal region consistent with a regulatory portion of an ATP-driven remodeling protein. Among the options, EC 5.6.1.1 is the ATP-dependent protein-remodeling choice; the other options classify distinct isomerase, oxidoreductase, and lyase activities. This supports A without needing the exact protein annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of AAA+ ATPases and their ATP-dependent remodeling activities, together with the sequence motifs and the offered alternatives, meaningfully distinguishes A. The motif alone would not prove a specific substrate or EC assignment, but the alternatives make the inference credible."
  },
  "case_id": "EC_number_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The exact sequence-matched UniProt record assigns EC 5.6.1.1 to spastin and describes ATP-dependent microtubule severing. The assignment is supported, though its cited evidence is transferred from a related protein rather than direct experimental evidence for this sequence."
  },
  "important_caveats": [
    "The reviewer evidence identifies the annotation as inferred by similarity (ECO:0000250), not as an experimentally established activity for this exact protein.",
    "The supplied evidence matches the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence evidence and the offered EC classes support A; no other option is comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence-matched UniProt record assigns EC 5.6.1.1 to spastin and describes ATP-dependent microtubule severing. The assignment is supported, though its cited evidence is transferred from a related protein rather than direct experimental evidence for this sequence.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a C-terminal AAA+ ATPase-like region, including a Walker A nucleotide-binding motif (…GPPGTGKT), alongside a long low-complexity N-terminal region consistent with a regulatory portion of an ATP-driven remodeling protein. Among the options, EC 5.6.1.1 is the ATP-dependent protein-remodeling choice; the other options classify distinct isomerase, oxidoreductase, and lyase activities. This supports A without needing the exact protein annotation.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of AAA+ ATPases and their ATP-dependent remodeling activities, together with the sequence motifs and the offered alternatives, meaningfully distinguishes A. The motif alone would not prove a specific substrate or EC assignment, but the alternatives make the inference credible."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence evidence and the offered EC classes support A; no other option is comparably defensible."
  },
  "important_caveats": [
    "The reviewer evidence identifies the annotation as inferred by similarity (ECO:0000250), not as an experimentally established activity for this exact protein.",
    "The supplied evidence matches the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry D2VS83 (SPAST_NAEGR) annotates this protein as Spastin with EC 5.6.1.1 (microtubule-severing ATPase). The annotation is based on similarity to human spastin Q9UBP0 (evidence code ECO:0000250), not direct experimental measurement on this protein. The sequence contains the canonical AAA+ Walker A motif (GPPGTGKT) and Walker B motif (IDEIDS), consistent with the AAA+ ATPase architecture of spastin. The database annotation supports the expected answer, though it is a computational inference by homology rather than experimental verification on this specific protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Walker A (P-loop) motif 'GPPGTGKT' and a Walker B motif 'IDEIDS', which are hallmark signatures of AAA+ ATPases. This is a highly recognizable, transferable feature learned from many AAA+ family proteins (RecA, ClpX, NSF, proteasome subunits, etc.). Among the four choices: EC 1.2.1.46 (oxidoreductase) and EC 4.1.1.129 (lyase/decarboxylase) are incompatible with an ATP-binding Walker A/B architecture and can be eliminated. EC 5.4.99.14 (an obscure intramolecular transferase) does not correspond to the AAA+ ATPase class. EC 5.6.1.1 (microtubule-severing ATPase) is the only option that matches the AAA+ ATPase signature. The N-terminal region's composition (rich in Q, S, N, T) is also consistent with the disordered N-terminal domain seen in spastin/katanin/fidgetin family members. Thus, recognition of the AAA+ motif pattern from other proteins meaningfully distinguishes option A from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Walker A and Walker B motifs are well-known, transferable sequence features of the AAA+ superfamily. A model with knowledge of protein families can recognize these motifs and associate them with EC 5.6.1.1 (the microtubule-severing ATPase class) while eliminating the oxidoreductase and lyase options. The inference does not require memorizing this specific protein's annotation; it relies on the conserved AAA+ signature shared across hundreds of characterized proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The AAA+ Walker A/B motifs clearly indicate an ATPase, eliminating the oxidoreductase (C) and lyase (D) options. EC 5.4.99.14 (intramolecular transferase) is inconsistent with the ATP-hydrolysis architecture. Only EC 5.6.1.1 matches the AAA+ ATPase signature among the choices.


### Important caveats

- The UniProt annotation for this protein is based on similarity (ECO:0000250) to human spastin Q9UBP0, not on direct experimental characterization of the Naegleria gruberi protein.
- The Walker A motif (GPPGTGKT) is shared by all AAA+ ATPases, not unique to spastin. However, among the four offered choices, only EC 5.6.1.1 corresponds to an AAA+ ATPase, so the motif is sufficient to select the correct option.
- The EC 5.6.1.1 classification itself was a reclassification from the former EC 3.6.4.12; this historical context does not affect the current answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Walker A (P-loop) motif 'GPPGTGKT' and a Walker B motif 'IDEIDS', which are hallmark signatures of AAA+ ATPases. This is a highly recognizable, transferable feature learned from many AAA+ family proteins (RecA, ClpX, NSF, proteasome subunits, etc.). Among the four choices: EC 1.2.1.46 (oxidoreductase) and EC 4.1.1.129 (lyase/decarboxylase) are incompatible with an ATP-binding Walker A/B architecture and can be eliminated. EC 5.4.99.14 (an obscure intramolecular transferase) does not correspond to the AAA+ ATPase class. EC 5.6.1.1 (microtubule-severing ATPase) is the only option that matches the AAA+ ATPase signature. The N-terminal region's composition (rich in Q, S, N, T) is also consistent with the disordered N-terminal domain seen in spastin/katanin/fidgetin family members. Thus, recognition of the AAA+ motif pattern from other proteins meaningfully distinguishes option A from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Walker A and Walker B motifs are well-known, transferable sequence features of the AAA+ superfamily. A model with knowledge of protein families can recognize these motifs and associate them with EC 5.6.1.1 (the microtubule-severing ATPase class) while eliminating the oxidoreductase and lyase options. The inference does not require memorizing this specific protein's annotation; it relies on the conserved AAA+ signature shared across hundreds of characterized proteins."
  },
  "case_id": "EC_number_0113",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry D2VS83 (SPAST_NAEGR) annotates this protein as Spastin with EC 5.6.1.1 (microtubule-severing ATPase). The annotation is based on similarity to human spastin Q9UBP0 (evidence code ECO:0000250), not direct experimental measurement on this protein. The sequence contains the canonical AAA+ Walker A motif (GPPGTGKT) and Walker B motif (IDEIDS), consistent with the AAA+ ATPase architecture of spastin. The database annotation supports the expected answer, though it is a computational inference by homology rather than experimental verification on this specific protein."
  },
  "important_caveats": [
    "The UniProt annotation for this protein is based on similarity (ECO:0000250) to human spastin Q9UBP0, not on direct experimental characterization of the Naegleria gruberi protein.",
    "The Walker A motif (GPPGTGKT) is shared by all AAA+ ATPases, not unique to spastin. However, among the four offered choices, only EC 5.6.1.1 corresponds to an AAA+ ATPase, so the motif is sufficient to select the correct option.",
    "The EC 5.6.1.1 classification itself was a reclassification from the former EC 3.6.4.12; this historical context does not affect the current answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The AAA+ Walker A/B motifs clearly indicate an ATPase, eliminating the oxidoreductase (C) and lyase (D) options. EC 5.4.99.14 (intramolecular transferase) is inconsistent with the ATP-hydrolysis architecture. Only EC 5.6.1.1 matches the AAA+ ATPase signature among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0113",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry D2VS83 (SPAST_NAEGR) annotates this protein as Spastin with EC 5.6.1.1 (microtubule-severing ATPase). The annotation is based on similarity to human spastin Q9UBP0 (evidence code ECO:0000250), not direct experimental measurement on this protein. The sequence contains the canonical AAA+ Walker A motif (GPPGTGKT) and Walker B motif (IDEIDS), consistent with the AAA+ ATPase architecture of spastin. The database annotation supports the expected answer, though it is a computational inference by homology rather than experimental verification on this specific protein.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Walker A (P-loop) motif 'GPPGTGKT' and a Walker B motif 'IDEIDS', which are hallmark signatures of AAA+ ATPases. This is a highly recognizable, transferable feature learned from many AAA+ family proteins (RecA, ClpX, NSF, proteasome subunits, etc.). Among the four choices: EC 1.2.1.46 (oxidoreductase) and EC 4.1.1.129 (lyase/decarboxylase) are incompatible with an ATP-binding Walker A/B architecture and can be eliminated. EC 5.4.99.14 (an obscure intramolecular transferase) does not correspond to the AAA+ ATPase class. EC 5.6.1.1 (microtubule-severing ATPase) is the only option that matches the AAA+ ATPase signature. The N-terminal region's composition (rich in Q, S, N, T) is also consistent with the disordered N-terminal domain seen in spastin/katanin/fidgetin family members. Thus, recognition of the AAA+ motif pattern from other proteins meaningfully distinguishes option A from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The Walker A and Walker B motifs are well-known, transferable sequence features of the AAA+ superfamily. A model with knowledge of protein families can recognize these motifs and associate them with EC 5.6.1.1 (the microtubule-severing ATPase class) while eliminating the oxidoreductase and lyase options. The inference does not require memorizing this specific protein's annotation; it relies on the conserved AAA+ signature shared across hundreds of characterized proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The AAA+ Walker A/B motifs clearly indicate an ATPase, eliminating the oxidoreductase (C) and lyase (D) options. EC 5.4.99.14 (intramolecular transferase) is inconsistent with the ATP-hydrolysis architecture. Only EC 5.6.1.1 matches the AAA+ ATPase signature among the choices."
  },
  "important_caveats": [
    "The UniProt annotation for this protein is based on similarity (ECO:0000250) to human spastin Q9UBP0, not on direct experimental characterization of the Naegleria gruberi protein.",
    "The Walker A motif (GPPGTGKT) is shared by all AAA+ ATPases, not unique to spastin. However, among the four offered choices, only EC 5.6.1.1 corresponds to an AAA+ ATPase, so the motif is sufficient to select the correct option.",
    "The EC 5.6.1.1 classification itself was a reclassification from the former EC 3.6.4.12; this historical context does not affect the current answer."
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
  "benchmark_sequence_length": 523,
  "benchmark_sequence_sha256": "c8fd32de6fd20724529e572780b2db849b6d2ecbbdc0453e4b65581e4566e59f",
  "current_entry_audit": {
    "entryVersion": 59,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 2
  },
  "current_record_sha256": "f2d05a3764bfe542789168be15fff27920e51b65cc7b7371af2071c35d38ae49",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 523,
  "current_source_sequence_sha256": "c8fd32de6fd20724529e572780b2db849b6d2ecbbdc0453e4b65581e4566e59f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 58,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "D2VS83",
  "selected_historical_entry_version": 58,
  "selected_historical_record_sha256": "123dedfbcb996ba2eb5d074dfcba479c91bc1a7b15ef6201c1c7e612fb862587",
  "selected_historical_source_sequence_length": 523,
  "selected_historical_source_sequence_sha256": "c8fd32de6fd20724529e572780b2db849b6d2ecbbdc0453e4b65581e4566e59f",
  "selected_historical_version": {
    "accession": "D2VS83",
    "database": "Swiss-Prot",
    "entryVersion": 58,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "SPAST_NAEGR",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D2VS83.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"D2VS83\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:39.406341+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2d05a3764bfe542789168be15fff27920e51b65cc7b7371af2071c35d38ae49",
  "url": "https://rest.uniprot.org/uniprotkb/D2VS83.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D2VS83.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":59,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:39.406341+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2d05a3764bfe542789168be15fff27920e51b65cc7b7371af2071c35d38ae49",
  "url": "https://rest.uniprot.org/uniprotkb/D2VS83.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D2VS83.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Amoeba\",\"lineage\":[\"Eukaryota\",\"Discoba\",\"Heterolobosea\",\"Tetramitia\",\"Eutetramitea\",\"Acrasida\",\"Naegleriidae\",\"Naegleria\"],\"scientificName\":\"Naegleria gruberi\",\"taxonId\":5762}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:39.406341+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2d05a3764bfe542789168be15fff27920e51b65cc7b7371af2071c35d38ae49",
  "url": "https://rest.uniprot.org/uniprotkb/D2VS83.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D2VS83.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9UBP0\",\"source\":\"UniProtKB\"}],\"value\":\"5.6.1.1\"}],\"fullName\":{\"value\":\"Spastin\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:39.406341+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2d05a3764bfe542789168be15fff27920e51b65cc7b7371af2071c35d38ae49",
  "url": "https://rest.uniprot.org/uniprotkb/D2VS83.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/D2VS83.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"5.6.1.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9UBP0\",\"source\":\"UniProtKB\"}],\"name\":\"n ATP + n H2O + a microtubule = n ADP + n phosphate + (n+1) alpha/beta tubulin heterodimers.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:39.406341+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f2d05a3764bfe542789168be15fff27920e51b65cc7b7371af2071c35d38ae49",
  "url": "https://rest.uniprot.org/uniprotkb/D2VS83.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D2VS83?format=txt&versions=58)

```json
{
  "entry_version": 58,
  "evidence_id": "H1",
  "excerpt": "ID   SPAST_NAEGR             Reviewed;         523 AA.\nAC   D2VS83;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 2.\nDT   28-JAN-2026, entry version 58.\nDE   RecName: Full=Spastin;\nDE            EC=5.6.1.1 {ECO:0000250|UniProtKB:Q9UBP0};\nGN   ORFNames=NAEGRDRAFT_83257;\nOS   Naegleria gruberi (Amoeba).\nOC   Eukaryota; Discoba; Heterolobosea; Tetramitia; Eutetramitia;\nOC   Vahlkampfiidae; Naegleria.\nOX   NCBI_TaxID=5762;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:44.335585+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "123dedfbcb996ba2eb5d074dfcba479c91bc1a7b15ef6201c1c7e612fb862587",
  "url": "https://rest.uniprot.org/unisave/D2VS83?format=txt&versions=58"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D2VS83?format=txt&versions=58)

```json
{
  "entry_version": 58,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Spastin;\nDE            EC=5.6.1.1 {ECO:0000250|UniProtKB:Q9UBP0};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:44.335585+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "123dedfbcb996ba2eb5d074dfcba479c91bc1a7b15ef6201c1c7e612fb862587",
  "url": "https://rest.uniprot.org/unisave/D2VS83?format=txt&versions=58"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/D2VS83?format=txt&versions=58)

```json
{
  "entry_version": 58,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=n ATP + n H2O + a microtubule = n ADP + n phosphate + (n+1)\nCC         alpha/beta tubulin heterodimers.; EC=5.6.1.1;\nCC         Evidence={ECO:0000250|UniProtKB:Q9UBP0};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:44.335585+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "123dedfbcb996ba2eb5d074dfcba479c91bc1a7b15ef6201c1c7e612fb862587",
  "url": "https://rest.uniprot.org/unisave/D2VS83?format=txt&versions=58"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 113. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
