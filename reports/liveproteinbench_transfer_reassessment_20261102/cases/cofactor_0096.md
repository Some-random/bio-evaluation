# cofactor_0096

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0096.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — Mg(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | uncertain |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGQTLSEPVVEKTSEKGEDDRLIYGVSAMQGWRISMEDAHTAELNLPPPDNDTKTHPDRLSFFGVFDGHGGDKVALFAGENIHNIVFKQESFKSGDYAQGLKDGFLATDRAILNDPKYEEEVSGCTACVTLIAGNKLYVANAGDSRSVLGIKGRAKPLSNDHKPQLETEKNRITAAGGFVDFGRVNGNLALSRAIGDFEFKKSAELSPENQIVTAFPDVEVHELTEEDEFLVIACDGIWDCQSSQAVVEFVRRGIAAKQDLDKICENMMDNCLASNSETGGVGCDNMTMVIIGFLHGKTKEEWYDEIAKRVANGDGPCAPPEYAEFRGPGVHHNYEDSDSGYDVDADSGGKFSLAGSRGRIIFLGDGTEVLTGSDDTEMFDNADEDKDLASQVPKSSGKTDAKEETEAKPAPEAESSKPADGSEKKQDEKTPEESKKD

[Multiple Choices]
A. Mn(2+)
B. Mg(2+)
C. a divalent metal cation
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

> The sequence-matched UniProt annotation lists Mg(2+) as a cofactor, so choice B is supported. However, it also lists Mn(2+) and says the protein binds magnesium or manganese ions; the annotation is based on similarity evidence rather than a direct experiment in this protein.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: uncertain

**Discriminating biological argument**

> The sequence is consistent with a PP2C-family phosphatase, whose transferable family-level cofactor pattern is divalent-metal dependence, commonly involving Mg(2+) or Mn(2+). That supports the metal choices over Fe, but does not meaningfully distinguish Mg(2+) from Mn(2+) here.


**Missing item-specific fact**

> A demonstrated preference or requirement for Mg(2+) rather than Mn(2+) under the relevant catalytic conditions would be needed to choose uniquely between A and B; the supplied evidence does not establish one.


**Reason**

> Family knowledge provides a credible basis for recognizing Mg(2+) and Mn(2+) as plausible cofactors, but not for selecting B over A. This leaves the alternatives unresolved rather than showing that an exact-protein lookup would uniquely answer the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The sequence-matched annotation names both Mg(2+) and Mn(2+) and describes binding magnesium or manganese ions, so the wording does not distinguish A from B. Choice C is a broader category, not a specific cofactor.


### Important caveats

- The cofactor annotation is similarity-based and should not be presented as direct experimental evidence for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a PP2C-family phosphatase, whose transferable family-level cofactor pattern is divalent-metal dependence, commonly involving Mg(2+) or Mn(2+). That supports the metal choices over Fe, but does not meaningfully distinguish Mg(2+) from Mn(2+) here.",
    "judgment": "cannot_determine",
    "missing_item_specific_fact": "A demonstrated preference or requirement for Mg(2+) rather than Mn(2+) under the relevant catalytic conditions would be needed to choose uniquely between A and B; the supplied evidence does not establish one.",
    "reason": "Family knowledge provides a credible basis for recognizing Mg(2+) and Mn(2+) as plausible cofactors, but not for selecting B over A. This leaves the alternatives unresolved rather than showing that an exact-protein lookup would uniquely answer the question."
  },
  "case_id": "cofactor_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists Mg(2+) as a cofactor, so choice B is supported. However, it also lists Mn(2+) and says the protein binds magnesium or manganese ions; the annotation is based on similarity evidence rather than a direct experiment in this protein."
  },
  "important_caveats": [
    "The cofactor annotation is similarity-based and should not be presented as direct experimental evidence for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The sequence-matched annotation names both Mg(2+) and Mn(2+) and describes binding magnesium or manganese ions, so the wording does not distinguish A from B. Choice C is a broader category, not a specific cofactor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation lists Mg(2+) as a cofactor, so choice B is supported. However, it also lists Mn(2+) and says the protein binds magnesium or manganese ions; the annotation is based on similarity evidence rather than a direct experiment in this protein.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "cannot_determine",
    "discriminating_biological_argument": "The sequence is consistent with a PP2C-family phosphatase, whose transferable family-level cofactor pattern is divalent-metal dependence, commonly involving Mg(2+) or Mn(2+). That supports the metal choices over Fe, but does not meaningfully distinguish Mg(2+) from Mn(2+) here.",
    "missing_item_specific_fact": "A demonstrated preference or requirement for Mg(2+) rather than Mn(2+) under the relevant catalytic conditions would be needed to choose uniquely between A and B; the supplied evidence does not establish one.",
    "reason": "Family knowledge provides a credible basis for recognizing Mg(2+) and Mn(2+) as plausible cofactors, but not for selecting B over A. This leaves the alternatives unresolved rather than showing that an exact-protein lookup would uniquely answer the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The sequence-matched annotation names both Mg(2+) and Mn(2+) and describes binding magnesium or manganese ions, so the wording does not distinguish A from B. Choice C is a broader category, not a specific cofactor."
  },
  "important_caveats": [
    "The cofactor annotation is similarity-based and should not be presented as direct experimental evidence for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H4) explicitly lists Mg(2+) as a cofactor for this PP2C homolog, so choice B is directly supported. However, the same annotation also lists Mn(2+) as a cofactor and notes 'Binds 2 magnesium or manganese ions per subunit,' meaning A and C are also annotated cofactors. The evidence codes are ECO:0000250 (similarity-based, from P35813) and ECO:0000255 (PROSITE-ProRule PRU01082), indicating computational/transferred annotation rather than direct experimental determination for this specific protein. B is supported but not uniquely so by the annotation.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmark PP2C-family motifs (e.g., the conserved 'GVSAMQGWRIS' N-terminal region, the 'FDGHGGDK' and 'ACDGIWDCQ' catalytic motifs, and the overall ~438-residue architecture). The PP2C (Protein Phosphatase 2C) family is one of the most well-characterized metal-dependent phosphatase families. Transferable family-level knowledge establishes that PP2C enzymes are canonically Mg(2+)-dependent, using two Mg(2+) ions in the active site for catalysis of serine/threonine dephosphorylation. While some PP2C members can substitute Mn(2+) in vitro, Mg(2+) is the physiologically relevant and most commonly cited cofactor across the family (e.g., PPM1A, PPM1B, PTC1/PP2Cα in mammals). A model recognizing PP2C family features would infer Mg(2+) as the primary cofactor, distinguishing B from D (Fe is not a PP2C cofactor) and generally from A (Mn is a less common alternative). Choice C ('a divalent metal cation') is technically true but overly generic when specific ion choices are offered.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> PP2C family recognition from conserved sequence motifs is a legitimate transferable inference. The canonical Mg(2+) cofactor assignment for PP2C is well-established across many homologs (mammalian PP2Cα, plant ABI1/ABI2, fungal Ptc1). This family-level knowledge meaningfully distinguishes B from D and provides a probabilistic preference for B over A. The annotation's 'magnesium or manganese' note introduces ambiguity with A, but the canonical/primary assignment in the literature and in the PROSITE-ProRule is Mg(2+).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B",
  "C"
]
```

> The UniProt annotation explicitly lists both Mg(2+) and Mn(2+) as cofactors and states 'Binds 2 magnesium or manganese ions per subunit.' This makes A (Mn(2+)) and C (a divalent metal cation) also defensible answers. While B is the canonical primary cofactor for PP2C family members, the annotation does not privilege Mg(2+) over Mn(2+) for this specific entry. Option C is technically correct as a superset. The question stem asks for 'the specific cofactor required,' which could favor B as the most specific and canonical answer, but does not fully exclude A or C.


### Important caveats

- The cofactor annotation is based on similarity (ECO:0000250 from P35813) and PROSITE-ProRule (ECO:0000255), not direct experimental measurement on this Trichoderma PP2C-2 protein.
- The annotation lists both Mg(2+) and Mn(2+) as cofactors with the note 'magnesium or manganese,' creating genuine ambiguity between options A, B, and C.
- The PROSITE-ProRule PRU01082 is a family-level rule for PP2C proteins, not a protein-specific experimental result.
- The question asks for 'the specific cofactor required,' which implicitly favors a single specific ion (B) over a generic category (C) or an alternative ion (A), but the annotation does not strictly enforce this hierarchy.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmark PP2C-family motifs (e.g., the conserved 'GVSAMQGWRIS' N-terminal region, the 'FDGHGGDK' and 'ACDGIWDCQ' catalytic motifs, and the overall ~438-residue architecture). The PP2C (Protein Phosphatase 2C) family is one of the most well-characterized metal-dependent phosphatase families. Transferable family-level knowledge establishes that PP2C enzymes are canonically Mg(2+)-dependent, using two Mg(2+) ions in the active site for catalysis of serine/threonine dephosphorylation. While some PP2C members can substitute Mn(2+) in vitro, Mg(2+) is the physiologically relevant and most commonly cited cofactor across the family (e.g., PPM1A, PPM1B, PTC1/PP2Cα in mammals). A model recognizing PP2C family features would infer Mg(2+) as the primary cofactor, distinguishing B from D (Fe is not a PP2C cofactor) and generally from A (Mn is a less common alternative). Choice C ('a divalent metal cation') is technically true but overly generic when specific ion choices are offered.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "PP2C family recognition from conserved sequence motifs is a legitimate transferable inference. The canonical Mg(2+) cofactor assignment for PP2C is well-established across many homologs (mammalian PP2Cα, plant ABI1/ABI2, fungal Ptc1). This family-level knowledge meaningfully distinguishes B from D and provides a probabilistic preference for B over A. The annotation's 'magnesium or manganese' note introduces ambiguity with A, but the canonical/primary assignment in the literature and in the PROSITE-ProRule is Mg(2+)."
  },
  "case_id": "cofactor_0096",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists Mg(2+) as a cofactor for this PP2C homolog, so choice B is directly supported. However, the same annotation also lists Mn(2+) as a cofactor and notes 'Binds 2 magnesium or manganese ions per subunit,' meaning A and C are also annotated cofactors. The evidence codes are ECO:0000250 (similarity-based, from P35813) and ECO:0000255 (PROSITE-ProRule PRU01082), indicating computational/transferred annotation rather than direct experimental determination for this specific protein. B is supported but not uniquely so by the annotation."
  },
  "important_caveats": [
    "The cofactor annotation is based on similarity (ECO:0000250 from P35813) and PROSITE-ProRule (ECO:0000255), not direct experimental measurement on this Trichoderma PP2C-2 protein.",
    "The annotation lists both Mg(2+) and Mn(2+) as cofactors with the note 'magnesium or manganese,' creating genuine ambiguity between options A, B, and C.",
    "The PROSITE-ProRule PRU01082 is a family-level rule for PP2C proteins, not a protein-specific experimental result.",
    "The question asks for 'the specific cofactor required,' which implicitly favors a single specific ion (B) over a generic category (C) or an alternative ion (A), but the annotation does not strictly enforce this hierarchy."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B",
      "C"
    ],
    "reason": "The UniProt annotation explicitly lists both Mg(2+) and Mn(2+) as cofactors and states 'Binds 2 magnesium or manganese ions per subunit.' This makes A (Mn(2+)) and C (a divalent metal cation) also defensible answers. While B is the canonical primary cofactor for PP2C family members, the annotation does not privilege Mg(2+) over Mn(2+) for this specific entry. Option C is technically correct as a superset. The question stem asks for 'the specific cofactor required,' which could favor B as the most specific and canonical answer, but does not fully exclude A or C."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0096",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H4) explicitly lists Mg(2+) as a cofactor for this PP2C homolog, so choice B is directly supported. However, the same annotation also lists Mn(2+) as a cofactor and notes 'Binds 2 magnesium or manganese ions per subunit,' meaning A and C are also annotated cofactors. The evidence codes are ECO:0000250 (similarity-based, from P35813) and ECO:0000255 (PROSITE-ProRule PRU01082), indicating computational/transferred annotation rather than direct experimental determination for this specific protein. B is supported but not uniquely so by the annotation.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmark PP2C-family motifs (e.g., the conserved 'GVSAMQGWRIS' N-terminal region, the 'FDGHGGDK' and 'ACDGIWDCQ' catalytic motifs, and the overall ~438-residue architecture). The PP2C (Protein Phosphatase 2C) family is one of the most well-characterized metal-dependent phosphatase families. Transferable family-level knowledge establishes that PP2C enzymes are canonically Mg(2+)-dependent, using two Mg(2+) ions in the active site for catalysis of serine/threonine dephosphorylation. While some PP2C members can substitute Mn(2+) in vitro, Mg(2+) is the physiologically relevant and most commonly cited cofactor across the family (e.g., PPM1A, PPM1B, PTC1/PP2Cα in mammals). A model recognizing PP2C family features would infer Mg(2+) as the primary cofactor, distinguishing B from D (Fe is not a PP2C cofactor) and generally from A (Mn is a less common alternative). Choice C ('a divalent metal cation') is technically true but overly generic when specific ion choices are offered.",
    "missing_item_specific_fact": "",
    "reason": "PP2C family recognition from conserved sequence motifs is a legitimate transferable inference. The canonical Mg(2+) cofactor assignment for PP2C is well-established across many homologs (mammalian PP2Cα, plant ABI1/ABI2, fungal Ptc1). This family-level knowledge meaningfully distinguishes B from D and provides a probabilistic preference for B over A. The annotation's 'magnesium or manganese' note introduces ambiguity with A, but the canonical/primary assignment in the literature and in the PROSITE-ProRule is Mg(2+)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B", "C"],
    "reason": "The UniProt annotation explicitly lists both Mg(2+) and Mn(2+) as cofactors and states 'Binds 2 magnesium or manganese ions per subunit.' This makes A (Mn(2+)) and C (a divalent metal cation) also defensible answers. While B is the canonical primary cofactor for PP2C family members, the annotation does not privilege Mg(2+) over Mn(2+) for this specific entry. Option C is technically correct as a superset. The question stem asks for 'the specific cofactor required,' which could favor B as the most specific and canonical answer, but does not fully exclude A or C."
  },
  "important_caveats": [
    "The cofactor annotation is based on similarity (ECO:0000250 from P35813) and PROSITE-ProRule (ECO:0000255), not direct experimental measurement on this Trichoderma PP2C-2 protein.",
    "The annotation lists both Mg(2+) and Mn(2+) as cofactors with the note 'magnesium or manganese,' creating genuine ambiguity between options A, B, and C.",
    "The PROSITE-ProRule PRU01082 is a family-level rule for PP2C proteins, not a protein-specific experimental result.",
    "The question asks for 'the specific cofactor required,' which implicitly favors a single specific ion (B) over a generic category (C) or an alternative ion (A), but the annotation does not strictly enforce this hierarchy."
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
  "benchmark_sequence_length": 438,
  "benchmark_sequence_sha256": "efbbcdee3241f50914fd3bb7a34e775e47c29401edf8b099e3e0786d71712cdc",
  "current_entry_audit": {
    "entryVersion": 62,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-10-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b557aa8f7ad6947823afc5e66f6b07b2436a2f57ca1be08b5981519707c03d1f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 438,
  "current_source_sequence_sha256": "efbbcdee3241f50914fd3bb7a34e775e47c29401edf8b099e3e0786d71712cdc",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 60,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G0RT93",
  "selected_historical_entry_version": 60,
  "selected_historical_record_sha256": "83146ed00f355669ea8dbc58d2920f98c3d145a36f529863e100646c52277769",
  "selected_historical_source_sequence_length": 438,
  "selected_historical_source_sequence_sha256": "efbbcdee3241f50914fd3bb7a34e775e47c29401edf8b099e3e0786d71712cdc",
  "selected_historical_version": {
    "accession": "G0RT93",
    "database": "Swiss-Prot",
    "entryVersion": 60,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PP2C2_HYPJQ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RT93.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G0RT93\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:20.800559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b557aa8f7ad6947823afc5e66f6b07b2436a2f57ca1be08b5981519707c03d1f",
  "url": "https://rest.uniprot.org/uniprotkb/G0RT93.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RT93.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":62,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-10-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:20.800559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b557aa8f7ad6947823afc5e66f6b07b2436a2f57ca1be08b5981519707c03d1f",
  "url": "https://rest.uniprot.org/uniprotkb/G0RT93.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RT93.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Filamentous fungus\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000008984\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Trichoderma\"],\"scientificName\":\"Trichoderma reesei (strain QM6a)\",\"synonyms\":[\"Hypocrea jecorina\"],\"taxonId\":431241}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:20.800559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b557aa8f7ad6947823afc5e66f6b07b2436a2f57ca1be08b5981519707c03d1f",
  "url": "https://rest.uniprot.org/uniprotkb/G0RT93.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RT93.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P39966\",\"source\":\"UniProtKB\"}],\"value\":\"3.1.3.16\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Protein phosphatase 2C homolog 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"PP2C-2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:20.800559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b557aa8f7ad6947823afc5e66f6b07b2436a2f57ca1be08b5981519707c03d1f",
  "url": "https://rest.uniprot.org/uniprotkb/G0RT93.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G0RT93.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35813\",\"source\":\"UniProtKB\"}],\"name\":\"Mg(2+)\"},{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29035\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P35813\",\"source\":\"UniProtKB\"}],\"name\":\"Mn(2+)\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01082\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"Binds 2 magnesium or manganese ions per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:28:20.800559+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b557aa8f7ad6947823afc5e66f6b07b2436a2f57ca1be08b5981519707c03d1f",
  "url": "https://rest.uniprot.org/uniprotkb/G0RT93.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60)

```json
{
  "entry_version": 60,
  "evidence_id": "H1",
  "excerpt": "ID   PP2C2_HYPJQ             Reviewed;         438 AA.\nAC   G0RT93; Q7Z8F2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-OCT-2011, sequence version 1.\nDT   28-JAN-2026, entry version 60.\nDE   RecName: Full=Protein phosphatase 2C homolog 2 {ECO:0000305};\nDE            Short=PP2C-2 {ECO:0000305};\nDE            EC=3.1.3.16 {ECO:0000250|UniProtKB:P39966};\nGN   Name=PTC2 {ECO:0000303|PubMed:15480788};\nGN   ORFNames=TRIREDRAFT_81164 {ECO:0000312|EMBL:EGR45524.1};\nOS   Hypocrea jecorina (strain QM6a) (Trichoderma reesei).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Trichoderma.\nOX   NCBI_TaxID=431241 {ECO:0000312|Proteomes:UP000008984};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:22.841847+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "83146ed00f355669ea8dbc58d2920f98c3d145a36f529863e100646c52277769",
  "url": "https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60)

```json
{
  "entry_version": 60,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Protein phosphatase 2C homolog 2 {ECO:0000305};\nDE            Short=PP2C-2 {ECO:0000305};\nDE            EC=3.1.3.16 {ECO:0000250|UniProtKB:P39966};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:22.841847+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "83146ed00f355669ea8dbc58d2920f98c3d145a36f529863e100646c52277769",
  "url": "https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60)

```json
{
  "entry_version": 60,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAP92916.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], AND FUNCTION.\nRC   STRAIN=QM6a {ECO:0000303|PubMed:15480788};\nRX   PubMed=15480788; DOI=10.1007/s00438-004-1070-0;\nRA   Valkonen M., Penttila M., Saloheimo M.;\nRT   \"The ire1 and ptc2 genes involved in the unfolded protein response pathway\nRT   in the filamentous fungus Trichoderma reesei.\";\nRL   Mol. Genet. Genomics 272:443-451(2004).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:22.841847+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "83146ed00f355669ea8dbc58d2920f98c3d145a36f529863e100646c52277769",
  "url": "https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60)

```json
{
  "entry_version": 60,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000250|UniProtKB:P35813};\nCC       Name=Mn(2+); Xref=ChEBI:CHEBI:29035;\nCC         Evidence={ECO:0000250|UniProtKB:P35813};\nCC       Note=Binds 2 magnesium or manganese ions per subunit.\nCC       {ECO:0000255|PROSITE-ProRule:PRU01082};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:22.841847+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "83146ed00f355669ea8dbc58d2920f98c3d145a36f529863e100646c52277769",
  "url": "https://rest.uniprot.org/unisave/G0RT93?format=txt&versions=60"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 96. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
