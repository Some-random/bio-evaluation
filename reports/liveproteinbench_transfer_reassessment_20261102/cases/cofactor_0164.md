# cofactor_0164

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0164.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — &#91;2Fe-2S&#93; cluster

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTANPTSIHQRLDRRLSGFSLEQPFYTSPEVYALDLQHIFYKQWLYAVPVCQLAKAGSYTTLRVGAYEVVIVRSRDGEVRAFHNSCRHRGSLICKARQGQVAKLVCPYHQWTYELDGKLIWANDMGPDFDASKYGLKPVNLRNLDGLIYICLSDTPPDFQTFAQLARPYLEVHDLKDAKVAFTSTIIEKGNWKLVWENNRECYHCSSNHPALCRSFPLDPEVAGVQADGGVSKKLQAHFDRCEAAGTPAQFVLAGDGQYRLARMPLQEKALSYTMDGKAAVSRHLGRVAPPDAGTLLMFHYPSTWNHFLPDHSLTFRVMPISPTETEVTTTWLVHKDAVEGVDYDLKRLTEVWIATNDEDREIVETNQQGILSPAYVPGPYSPGQESGVMQFVDWYAASLERALAPRQVAAE

[Multiple Choices]
A. Fe cation
B. [2Fe-2S] cluster
C. Zn(2+)
D. pyridoxal 5'-phosphate
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

> The sequence-matched entry reports one &#91;2Fe-2S&#93; cluster per subunit, with experimental-evidence codes; it also reports one Fe cation per subunit. Thus B is a genuine required cofactor, though not the only one among the choices.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence's Cys/His-rich region is compatible with a Rieske-type iron-sulfur-binding site. Transferable knowledge of Rieske enzymes therefore gives a credible basis for selecting the &#91;2Fe-2S&#93; cluster (B) over options such as Zn(2+) or PLP.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference can meaningfully support B without recalling this protein's exact database record. However, the inference does not make B the unique answer here: iron-dependent Rieske enzymes can also require mononuclear Fe, and A is independently supported for this protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The evidence reports that each subunit binds both a &#91;2Fe-2S&#93; cluster and an Fe cation, so both offered options are required cofactors despite the singular wording.


### Important caveats

- Reviewer-only annotation evidence supports the key but was not part of the original model input.
- The cofactor annotations cite experimental evidence, but the supplied excerpts do not independently present the underlying experiments.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's Cys/His-rich region is compatible with a Rieske-type iron-sulfur-binding site. Transferable knowledge of Rieske enzymes therefore gives a credible basis for selecting the [2Fe-2S] cluster (B) over options such as Zn(2+) or PLP.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can meaningfully support B without recalling this protein's exact database record. However, the inference does not make B the unique answer here: iron-dependent Rieske enzymes can also require mononuclear Fe, and A is independently supported for this protein."
  },
  "case_id": "cofactor_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched entry reports one [2Fe-2S] cluster per subunit, with experimental-evidence codes; it also reports one Fe cation per subunit. Thus B is a genuine required cofactor, though not the only one among the choices."
  },
  "important_caveats": [
    "Reviewer-only annotation evidence supports the key but was not part of the original model input.",
    "The cofactor annotations cite experimental evidence, but the supplied excerpts do not independently present the underlying experiments."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The evidence reports that each subunit binds both a [2Fe-2S] cluster and an Fe cation, so both offered options are required cofactors despite the singular wording."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched entry reports one [2Fe-2S] cluster per subunit, with experimental-evidence codes; it also reports one Fe cation per subunit. Thus B is a genuine required cofactor, though not the only one among the choices.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence's Cys/His-rich region is compatible with a Rieske-type iron-sulfur-binding site. Transferable knowledge of Rieske enzymes therefore gives a credible basis for selecting the [2Fe-2S] cluster (B) over options such as Zn(2+) or PLP.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference can meaningfully support B without recalling this protein's exact database record. However, the inference does not make B the unique answer here: iron-dependent Rieske enzymes can also require mononuclear Fe, and A is independently supported for this protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The evidence reports that each subunit binds both a [2Fe-2S] cluster and an Fe cation, so both offered options are required cofactors despite the singular wording."
  },
  "important_caveats": [
    "Reviewer-only annotation evidence supports the key but was not part of the original model input.",
    "The cofactor annotations cite experimental evidence, but the supplied excerpts do not independently present the underlying experiments."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (Q92ZP9, Stachydrine N-demethylase) explicitly lists &#91;2Fe-2S&#93; cluster as a cofactor with experimental evidence (ECO:0000269 from PubMed:22224443 and PubMed:26996959, X-ray crystallography in complex with iron and iron-sulfur 2Fe-2S). The protein is annotated as a 'Rieske-type mononuclear non-heme enzyme,' and the &#91;2Fe-2S&#93; cluster is the defining Rieske cofactor. However, a Fe cation is also listed as a cofactor (1 per subunit), so option A is equally supported by the annotation. The expected answer B is correct but not uniquely correct.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a recognizable Rieske-type iron-sulfur motif. Scanning the sequence reveals the pattern C-Y-H-C-S-S-N-H (around residues ~175-185), which approximates the canonical Rieske motif C-X2-H-X3-C-X2-H. Additional Cys/His pairs (e.g., 'CPYHQWTYEL' earlier, 'HYPSTWNHFLPD' later) reinforce this. The Rieske motif is a well-established, transferable family-level feature: any protein bearing this Cys/His coordination pattern is a Rieske protein, which by definition binds a &#91;2Fe-2S&#93; cluster. This distinguishes option B from C (Zn) and D (PLP), which have entirely different sequence signatures. Between A (Fe cation) and B (&#91;2Fe-2S&#93;), the Rieske motif is the most directly identifiable feature from sequence alone; the mononuclear non-heme Fe site (typically a 2-His-1-carboxylate facial triad) is harder to pinpoint unambiguously from primary sequence. A knowledgeable model would recognize the Rieske motif and associate it with &#91;2Fe-2S&#93; as the defining cofactor of this protein family.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rieske motif (C-X2-H-X3-C-X2-H) is a textbook family-level sequence feature shared across Rieske oxygenases, Rieske iron-sulfur proteins, naphthalene dioxygenases, and many other proteins. Recognizing this motif and linking it to &#91;2Fe-2S&#93; is standard transferable knowledge, not memorization of this specific protein's annotation. PLP (D) and Zn (C) can be eliminated by absence of their respective signature motifs. The main difficulty is distinguishing A from B, but the Rieske motif most directly and specifically points to &#91;2Fe-2S&#93;.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> The protein is annotated as a 'Rieske-type mononuclear non-heme enzyme' and UniProt lists both &#91;2Fe-2S&#93; cluster (1 per subunit) and Fe cation (1 per subunit) as cofactors, both supported by experimental evidence. The question asks for 'the specific cofactor' (singular), but the enzyme genuinely requires both. The Fe cation is the catalytic center for substrate oxidation, while the &#91;2Fe-2S&#93; cluster serves electron transfer. A knowledgeable model could reasonably argue either is 'the' cofactor required for catalytic activity. The Rieske motif makes B the more sequence-identifiable answer, but A is not wrong.


### Important caveats

- Both &#91;2Fe-2S&#93; and mononuclear Fe are experimentally confirmed cofactors for this enzyme; the question's singular phrasing ('the specific cofactor') is somewhat misleading for a two-cofactor enzyme.
- The Rieske motif in the sequence is approximate (C-X-H-X3-C-X2-H vs canonical C-X2-H-X3-C-X2-H), but the Cys/His spacing pattern is consistent with Rieske-type coordination.
- The reviewer-only evidence confirms the sequence matches Q92ZP9 (Stachydrine N-demethylase, Sinorhizobium meliloti 1021), but this identification was not available to the evaluated model.
- The distinction between 'catalytic' cofactor (Fe) and 'electron-transfer' cofactor (&#91;2Fe-2S&#93;) could favor A under a strict reading of 'required for catalytic activity,' but both are essential for the enzyme to function.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a recognizable Rieske-type iron-sulfur motif. Scanning the sequence reveals the pattern C-Y-H-C-S-S-N-H (around residues ~175-185), which approximates the canonical Rieske motif C-X2-H-X3-C-X2-H. Additional Cys/His pairs (e.g., 'CPYHQWTYEL' earlier, 'HYPSTWNHFLPD' later) reinforce this. The Rieske motif is a well-established, transferable family-level feature: any protein bearing this Cys/His coordination pattern is a Rieske protein, which by definition binds a [2Fe-2S] cluster. This distinguishes option B from C (Zn) and D (PLP), which have entirely different sequence signatures. Between A (Fe cation) and B ([2Fe-2S]), the Rieske motif is the most directly identifiable feature from sequence alone; the mononuclear non-heme Fe site (typically a 2-His-1-carboxylate facial triad) is harder to pinpoint unambiguously from primary sequence. A knowledgeable model would recognize the Rieske motif and associate it with [2Fe-2S] as the defining cofactor of this protein family.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rieske motif (C-X2-H-X3-C-X2-H) is a textbook family-level sequence feature shared across Rieske oxygenases, Rieske iron-sulfur proteins, naphthalene dioxygenases, and many other proteins. Recognizing this motif and linking it to [2Fe-2S] is standard transferable knowledge, not memorization of this specific protein's annotation. PLP (D) and Zn (C) can be eliminated by absence of their respective signature motifs. The main difficulty is distinguishing A from B, but the Rieske motif most directly and specifically points to [2Fe-2S]."
  },
  "case_id": "cofactor_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (Q92ZP9, Stachydrine N-demethylase) explicitly lists [2Fe-2S] cluster as a cofactor with experimental evidence (ECO:0000269 from PubMed:22224443 and PubMed:26996959, X-ray crystallography in complex with iron and iron-sulfur 2Fe-2S). The protein is annotated as a 'Rieske-type mononuclear non-heme enzyme,' and the [2Fe-2S] cluster is the defining Rieske cofactor. However, a Fe cation is also listed as a cofactor (1 per subunit), so option A is equally supported by the annotation. The expected answer B is correct but not uniquely correct."
  },
  "important_caveats": [
    "Both [2Fe-2S] and mononuclear Fe are experimentally confirmed cofactors for this enzyme; the question's singular phrasing ('the specific cofactor') is somewhat misleading for a two-cofactor enzyme.",
    "The Rieske motif in the sequence is approximate (C-X-H-X3-C-X2-H vs canonical C-X2-H-X3-C-X2-H), but the Cys/His spacing pattern is consistent with Rieske-type coordination.",
    "The reviewer-only evidence confirms the sequence matches Q92ZP9 (Stachydrine N-demethylase, Sinorhizobium meliloti 1021), but this identification was not available to the evaluated model.",
    "The distinction between 'catalytic' cofactor (Fe) and 'electron-transfer' cofactor ([2Fe-2S]) could favor A under a strict reading of 'required for catalytic activity,' but both are essential for the enzyme to function."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "The protein is annotated as a 'Rieske-type mononuclear non-heme enzyme' and UniProt lists both [2Fe-2S] cluster (1 per subunit) and Fe cation (1 per subunit) as cofactors, both supported by experimental evidence. The question asks for 'the specific cofactor' (singular), but the enzyme genuinely requires both. The Fe cation is the catalytic center for substrate oxidation, while the [2Fe-2S] cluster serves electron transfer. A knowledgeable model could reasonably argue either is 'the' cofactor required for catalytic activity. The Rieske motif makes B the more sequence-identifiable answer, but A is not wrong."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (Q92ZP9, Stachydrine N-demethylase) explicitly lists [2Fe-2S] cluster as a cofactor with experimental evidence (ECO:0000269 from PubMed:22224443 and PubMed:26996959, X-ray crystallography in complex with iron and iron-sulfur 2Fe-2S). The protein is annotated as a 'Rieske-type mononuclear non-heme enzyme,' and the [2Fe-2S] cluster is the defining Rieske cofactor. However, a Fe cation is also listed as a cofactor (1 per subunit), so option A is equally supported by the annotation. The expected answer B is correct but not uniquely correct.",
    "evidence_ids": ["C5", "C6", "H4", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a recognizable Rieske-type iron-sulfur motif. Scanning the sequence reveals the pattern C-Y-H-C-S-S-N-H (around residues ~175-185), which approximates the canonical Rieske motif C-X2-H-X3-C-X2-H. Additional Cys/His pairs (e.g., 'CPYHQWTYEL' earlier, 'HYPSTWNHFLPD' later) reinforce this. The Rieske motif is a well-established, transferable family-level feature: any protein bearing this Cys/His coordination pattern is a Rieske protein, which by definition binds a [2Fe-2S] cluster. This distinguishes option B from C (Zn) and D (PLP), which have entirely different sequence signatures. Between A (Fe cation) and B ([2Fe-2S]), the Rieske motif is the most directly identifiable feature from sequence alone; the mononuclear non-heme Fe site (typically a 2-His-1-carboxylate facial triad) is harder to pinpoint unambiguously from primary sequence. A knowledgeable model would recognize the Rieske motif and associate it with [2Fe-2S] as the defining cofactor of this protein family.",
    "missing_item_specific_fact": "",
    "reason": "The Rieske motif (C-X2-H-X3-C-X2-H) is a textbook family-level sequence feature shared across Rieske oxygenases, Rieske iron-sulfur proteins, naphthalene dioxygenases, and many other proteins. Recognizing this motif and linking it to [2Fe-2S] is standard transferable knowledge, not memorization of this specific protein's annotation. PLP (D) and Zn (C) can be eliminated by absence of their respective signature motifs. The main difficulty is distinguishing A from B, but the Rieske motif most directly and specifically points to [2Fe-2S]."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "The protein is annotated as a 'Rieske-type mononuclear non-heme enzyme' and UniProt lists both [2Fe-2S] cluster (1 per subunit) and Fe cation (1 per subunit) as cofactors, both supported by experimental evidence. The question asks for 'the specific cofactor' (singular), but the enzyme genuinely requires both. The Fe cation is the catalytic center for substrate oxidation, while the [2Fe-2S] cluster serves electron transfer. A knowledgeable model could reasonably argue either is 'the' cofactor required for catalytic activity. The Rieske motif makes B the more sequence-identifiable answer, but A is not wrong."
  },
  "important_caveats": [
    "Both [2Fe-2S] and mononuclear Fe are experimentally confirmed cofactors for this enzyme; the question's singular phrasing ('the specific cofactor') is somewhat misleading for a two-cofactor enzyme.",
    "The Rieske motif in the sequence is approximate (C-X-H-X3-C-X2-H vs canonical C-X2-H-X3-C-X2-H), but the Cys/His spacing pattern is consistent with Rieske-type coordination.",
    "The reviewer-only evidence confirms the sequence matches Q92ZP9 (Stachydrine N-demethylase, Sinorhizobium meliloti 1021), but this identification was not available to the evaluated model.",
    "The distinction between 'catalytic' cofactor (Fe) and 'electron-transfer' cofactor ([2Fe-2S]) could favor A under a strict reading of 'required for catalytic activity,' but both are essential for the enzyme to function."
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
  "benchmark_sequence_length": 412,
  "benchmark_sequence_sha256": "02696bd07c892515185be2809c4d39876ddd67459e5b8f8988a93fdc7960d8ea",
  "current_entry_audit": {
    "entryVersion": 140,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2001-12-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 412,
  "current_source_sequence_sha256": "02696bd07c892515185be2809c4d39876ddd67459e5b8f8988a93fdc7960d8ea",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 138,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q92ZP9",
  "selected_historical_entry_version": 138,
  "selected_historical_record_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "selected_historical_source_sequence_length": 412,
  "selected_historical_source_sequence_sha256": "02696bd07c892515185be2809c4d39876ddd67459e5b8f8988a93fdc7960d8ea",
  "selected_historical_version": {
    "accession": "Q92ZP9",
    "database": "Swiss-Prot",
    "entryVersion": 138,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "STC2_RHIME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q92ZP9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":140,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2001-12-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ensifer meliloti\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Alphaproteobacteria\",\"Hyphomicrobiales\",\"Rhizobiaceae\",\"Sinorhizobium/Ensifer group\",\"Sinorhizobium\"],\"scientificName\":\"Rhizobium meliloti (strain 1021)\",\"synonyms\":[\"Sinorhizobium meliloti\"],\"taxonId\":266834}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22224443\",\"source\":\"PubMed\"}],\"value\":\"Rieske-type mononuclear non-heme enzyme\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22224443\",\"source\":\"PubMed\"}],\"value\":\"1.14.13.247\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Stachydrine N-demethylase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:190135\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22224443\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26996959\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"Ref.5\",\"source\":\"Reference\"}],\"name\":\"[2Fe-2S] cluster\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22224443\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26996959\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"Ref.5\",\"source\":\"Reference\"}],\"value\":\"Binds 1 [2Fe-2S] cluster per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:24875\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22224443\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26996959\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"Ref.5\",\"source\":\"Reference\"}],\"name\":\"Fe cation\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22224443\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26996959\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"Ref.5\",\"source\":\"Reference\"}],\"value\":\"Binds 1 Fe cation per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Daughtry K.D.\",\"Xiao Y.\",\"Stoner-Ma D.\",\"Cho E.\",\"Orville A.M.\",\"Liu P.\",\"Allen K.N.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22224443\"},{\"database\":\"DOI\",\"id\":\"10.1021/ja2111898\"}],\"citationType\":\"journal article\",\"firstPage\":\"2823\",\"id\":\"22224443\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"2834\",\"publicationDate\":\"2012\",\"title\":\"Quaternary ammonium oxidative demethylation: X-ray crystallographic, resonance Raman, and UV-visible spectroscopic analysis of a Rieske-type demethylase.\",\"volume\":\"134\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3VCA\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"3VCP\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"1021\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.59 ANGSTROMS) IN COMPLEX WITH IRON AND IRON-SULFUR (2FE-2S)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"REACTION MECHANISM\",\"COFACTOR\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q92ZP9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Roessler C.G.\",\"Agarwal R.\",\"Allaire M.\",\"Alonso-Mori R.\",\"Andi B.\",\"Bachega J.F.\",\"Bommer M.\",\"Brewster A.S.\",\"Browne M.C.\",\"Chatterjee R.\",\"Cho E.\",\"Cohen A.E.\",\"Cowan M.\",\"Datwani S.\",\"Davidson V.L.\",\"Defever J.\",\"Eaton B.\",\"Ellson R.\",\"Feng Y.\",\"Ghislain L.P.\",\"Glownia J.M.\",\"Han G.\",\"Hattne J.\",\"Hellmich J.\",\"Heroux A.\",\"Ibrahim M.\",\"Kern J.\",\"Kuczewski A.\",\"Lemke H.T.\",\"Liu P.\",\"Majlof L.\",\"McClintock W.M.\",\"Myers S.\",\"Nelsen S.\",\"Olechno J.\",\"Orville A.M.\",\"Sauter N.K.\",\"Soares A.S.\",\"Soltis S.M.\",\"Song H.\",\"Stearns R.G.\",\"Tran R.\",\"Tsai Y.\",\"Uervirojnangkoorn M.\",\"Wilmot C.M.\",\"Yachandra V.\",\"Yano J.\",\"Yukl E.T.\",\"Zhu D.\",\"Zouni A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26996959\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.str.2016.02.007\"}],\"citationType\":\"journal article\",\"firstPage\":\"631\",\"id\":\"26996959\",\"journal\":\"Structure\",\"lastPage\":\"640\",\"publicationDate\":\"2016\",\"title\":\"Acoustic Injectors for Drop-On-Demand Serial Femtosecond Crystallography.\",\"volume\":\"24\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"5HL4\",\"source\":\"PDB\"}],\"referenceNumber\":6,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH IRON AND IRON-SULFUR (2FE-2S)\",\"COFACTOR\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:32:35.950168+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "276bbb28b7f728e4d5308c52858a6cf1f7a55297c8e83d33b96d87fe308e1b31",
  "url": "https://rest.uniprot.org/uniprotkb/Q92ZP9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H1",
  "excerpt": "ID   STC2_RHIME              Reviewed;         412 AA.\nAC   Q92ZP9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-DEC-2001, sequence version 1.\nDT   28-JAN-2026, entry version 138.\nDE   RecName: Full=Stachydrine N-demethylase {ECO:0000305};\nDE            EC=1.14.13.247 {ECO:0000269|PubMed:22224443};\nDE   AltName: Full=Rieske-type mononuclear non-heme enzyme {ECO:0000303|PubMed:22224443};\nGN   Name=stc2 {ECO:0000303|PubMed:10689197};\nGN   OrderedLocusNames=RA0400 {ECO:0000305};\nGN   ORFNames=SMa0751 {ECO:0000312|EMBL:AAK65058.1};\nOS   Rhizobium meliloti (strain 1021) (Ensifer meliloti) (Sinorhizobium\nOS   meliloti).\nOG   Plasmid pSymA (megaplasmid 1).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria;\nOC   Hyphomicrobiales; Rhizobiaceae; Sinorhizobium/Ensifer group; Sinorhizobium.\nOX   NCBI_TaxID=266834;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.981731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "url": "https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Stachydrine N-demethylase {ECO:0000305};\nDE            EC=1.14.13.247 {ECO:0000269|PubMed:22224443};\nDE   AltName: Full=Rieske-type mononuclear non-heme enzyme {ECO:0000303|PubMed:22224443};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.981731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "url": "https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=Sm2011 / Rm2011 / 2011;\nRX   PubMed=10689197; DOI=10.1016/s0378-1119(99)00554-5;\nRA   Burnet M.W., Goldmann A., Message B., Drong R., El Amrani A., Loreau O.,\nRA   Slightom J., Tepfer D.;\nRT   \"The stachydrine catabolism region in Sinorhizobium meliloti encodes a\nRT   multi-enzyme complex similar to the xenobiotic degrading systems in other\nRT   bacteria.\";\nRL   Gene 244:151-161(2000).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.981731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "url": "https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H4",
  "excerpt": "RN   [4] {ECO:0007744|PDB:3VCA, ECO:0007744|PDB:3VCP}\nRP   X-RAY CRYSTALLOGRAPHY (1.59 ANGSTROMS) IN COMPLEX WITH IRON AND IRON-SULFUR\nRP   (2FE-2S), FUNCTION, CATALYTIC ACTIVITY, REACTION MECHANISM, COFACTOR, AND\nRP   SUBUNIT.\nRC   STRAIN=1021;\nRX   PubMed=22224443; DOI=10.1021/ja2111898;\nRA   Daughtry K.D., Xiao Y., Stoner-Ma D., Cho E., Orville A.M., Liu P.,\nRA   Allen K.N.;\nRT   \"Quaternary ammonium oxidative demethylation: X-ray crystallographic,\nRT   resonance Raman, and UV-visible spectroscopic analysis of a Rieske-type\nRT   demethylase.\";\nRL   J. Am. Chem. Soc. 134:2823-2834(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.981731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "url": "https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H5",
  "excerpt": "RN   [6] {ECO:0007744|PDB:5HL4}\nRP   X-RAY CRYSTALLOGRAPHY (2.20 ANGSTROMS) IN COMPLEX WITH IRON AND IRON-SULFUR\nRP   (2FE-2S), AND COFACTOR.\nRX   PubMed=26996959; DOI=10.1016/j.str.2016.02.007;\nRA   Roessler C.G., Agarwal R., Allaire M., Alonso-Mori R., Andi B.,\nRA   Bachega J.F., Bommer M., Brewster A.S., Browne M.C., Chatterjee R., Cho E.,\nRA   Cohen A.E., Cowan M., Datwani S., Davidson V.L., Defever J., Eaton B.,\nRA   Ellson R., Feng Y., Ghislain L.P., Glownia J.M., Han G., Hattne J.,\nRA   Hellmich J., Heroux A., Ibrahim M., Kern J., Kuczewski A., Lemke H.T.,\nRA   Liu P., Majlof L., McClintock W.M., Myers S., Nelsen S., Olechno J.,\nRA   Orville A.M., Sauter N.K., Soares A.S., Soltis S.M., Song H., Stearns R.G.,\nRA   Tran R., Tsai Y., Uervirojnangkoorn M., Wilmot C.M., Yachandra V., Yano J.,\nRA   Yukl E.T., Zhu D., Zouni A.;\nRT   \"Acoustic Injectors for Drop-On-Demand Serial Femtosecond\nRT   Crystallography.\";\nRL   Structure 24:631-640(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.981731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 74-89",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "url": "https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H6",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=[2Fe-2S] cluster; Xref=ChEBI:CHEBI:190135;\nCC         Evidence={ECO:0000269|PubMed:22224443, ECO:0000269|PubMed:26996959,\nCC         ECO:0000269|Ref.5};\nCC       Note=Binds 1 [2Fe-2S] cluster per subunit.\nCC       {ECO:0000269|PubMed:22224443, ECO:0000269|PubMed:26996959,\nCC       ECO:0000269|Ref.5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.981731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-117",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "url": "https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138)

```json
{
  "entry_version": 138,
  "evidence_id": "H7",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Fe cation; Xref=ChEBI:CHEBI:24875;\nCC         Evidence={ECO:0000269|PubMed:22224443, ECO:0000269|PubMed:26996959,\nCC         ECO:0000269|Ref.5};\nCC       Note=Binds 1 Fe cation per subunit. {ECO:0000269|PubMed:22224443,\nCC       ECO:0000269|PubMed:26996959, ECO:0000269|Ref.5};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.981731+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-123",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "654ed34bb065302100be233c1866fa2d88c01f29d8687093e81091b3661f244b",
  "url": "https://rest.uniprot.org/unisave/Q92ZP9?format=txt&versions=138"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 164. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
