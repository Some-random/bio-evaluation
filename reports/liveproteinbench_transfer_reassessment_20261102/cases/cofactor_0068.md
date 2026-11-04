# cofactor_0068

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0068.txt)

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
MSTLLDVRVAAIRELTPVIREYSFEALASTLPGFSAGSHVQLHLPNGRRNAYSLLSDPADTRQYRIAVRQQDASRGGSRYLHQHLKVGDRLRLSPPANLFPLHGEAQKHILVAAGIGITPFLAYSQELLRRGADFELHYAYRAGSSDAYVDELRQQLGPRLHEYLSGQRRLDLASLLQGRTLGTHVYACGPQSLLLDLQEQASAQGWSPRRVHWEAFAAAEPGQPFRVELARSGQQLEVAADESLLEALEAAGVEVPNLCRGGVCGQCQTPWLKGDVEHRDHFLSANERTSSLMPCVSRGCGSPILLDL

[Multiple Choices]
A. pantetheine 4'-phosphate
B. [2Fe-2S] cluster
C. heme
D. FMN
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

> The sequence-matched UniProt annotation identifies a &#91;2Fe-2S&#93; cluster and says one binds per subunit, citing both a PROSITE rule and a PubMed source. The same record also annotates FMN, so B is supported but is not the only annotated cofactor.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a conspicuous cysteine-rich region near its C-terminus, a transferable hallmark of iron-sulfur cluster ligation. That makes the &#91;2Fe-2S&#93; option meaningfully distinguishable from pantetheine 4'-phosphate and heme, though the sequence pattern alone does not rule out an additional flavin cofactor.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence feature gives a credible basis for selecting B without needing the exact protein record. However, the question's singular wording obscures that the protein is also annotated with FMN.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The sequence-matched source annotates both a &#91;2Fe-2S&#93; cluster and FMN as cofactors. Thus both B and D are defensible answers to the broad question of which cofactor the protein requires.


### Important caveats

- The source supports B with PROSITE and PubMed evidence, but the cited primary study was not independently reviewed here.
- The source identifies this subunit as part of a heme-dependent enzyme; that does not by itself establish heme as a cofactor bound by this protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a conspicuous cysteine-rich region near its C-terminus, a transferable hallmark of iron-sulfur cluster ligation. That makes the [2Fe-2S] option meaningfully distinguishable from pantetheine 4'-phosphate and heme, though the sequence pattern alone does not rule out an additional flavin cofactor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence feature gives a credible basis for selecting B without needing the exact protein record. However, the question's singular wording obscures that the protein is also annotated with FMN."
  },
  "case_id": "cofactor_0068",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies a [2Fe-2S] cluster and says one binds per subunit, citing both a PROSITE rule and a PubMed source. The same record also annotates FMN, so B is supported but is not the only annotated cofactor."
  },
  "important_caveats": [
    "The source supports B with PROSITE and PubMed evidence, but the cited primary study was not independently reviewed here.",
    "The source identifies this subunit as part of a heme-dependent enzyme; that does not by itself establish heme as a cofactor bound by this protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The sequence-matched source annotates both a [2Fe-2S] cluster and FMN as cofactors. Thus both B and D are defensible answers to the broad question of which cofactor the protein requires."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies a [2Fe-2S] cluster and says one binds per subunit, citing both a PROSITE rule and a PubMed source. The same record also annotates FMN, so B is supported but is not the only annotated cofactor.",
    "evidence_ids": ["C5", "H4", "C6", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a conspicuous cysteine-rich region near its C-terminus, a transferable hallmark of iron-sulfur cluster ligation. That makes the [2Fe-2S] option meaningfully distinguishable from pantetheine 4'-phosphate and heme, though the sequence pattern alone does not rule out an additional flavin cofactor.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence feature gives a credible basis for selecting B without needing the exact protein record. However, the question's singular wording obscures that the protein is also annotated with FMN."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The sequence-matched source annotates both a [2Fe-2S] cluster and FMN as cofactors. Thus both B and D are defensible answers to the broad question of which cofactor the protein requires."
  },
  "important_caveats": [
    "The source supports B with PROSITE and PubMed evidence, but the cited primary study was not independently reviewed here.",
    "The source identifies this subunit as part of a heme-dependent enzyme; that does not by itself establish heme as a cofactor bound by this protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A4XXY8) explicitly lists &#91;2Fe-2S&#93; cluster as a cofactor with evidence codes ECO:0000255 (PROSITE-ProRule PRU00465, computational) and ECO:0000269 (PubMed:27851736, experimental), stating 'Binds 1 2Fe-2S cluster per subunit.' The author's answer B is directly supported. However, FMN (option D) is also listed as a cofactor with experimental evidence (ECO:0000269, PubMed:27851736), so the answer is supported but not uniquely so.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the sequence contains a cysteine cluster: 'CRGGVCGQCQTPWLKGDVEHRDHFLSANERTSSLMPCVSRGCGSPILLDL.' The pattern of four cysteines (C-X4-C-X2-C-X35-C) is recognizable as a 2Fe-2S cluster-binding motif using transferable knowledge of ferredoxin-type and Rieske-type iron-sulfur proteins. PROSITE ProRule PRU00465 (2Fe-2S ferredoxin-like domain) is a well-known family-level pattern. Additionally, the protein contains a Rossmann-fold-like motif 'AAGIGITPFLAYSQ' (GxGxxP pattern) suggestive of FMN or dinucleotide binding, but this motif is less diagnostically specific (it could indicate FMN, FAD, NADH, or NADPH). The &#91;2Fe-2S&#93; cysteine motif is a more uniquely identifiable and specific sequence signature, making B the more defensible single answer when the question asks for 'the specific cofactor.'


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the 2Fe-2S cluster-binding cysteine motif from the C-terminal sequence using well-established family-level knowledge of iron-sulfur protein motifs (ferredoxin-type, Rieske-type). This is a legitimate transferable inference from other proteins. The FMN Rossmann motif is also present, creating some ambiguity, but the &#91;2Fe-2S&#93; motif is more uniquely diagnostic from sequence alone, providing a credible basis to prefer B over D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> The UniProt entry lists both &#91;2Fe-2S&#93; cluster and FMN as cofactors of this protein, both with experimental evidence from PubMed:27851736. The question asks for 'the specific cofactor' (singular), but the protein requires both. A model identifying the Rossmann-fold FMN-binding motif could reasonably select D. The &#91;2Fe-2S&#93; motif is arguably more uniquely identifiable from sequence, giving B a slight edge, but D remains defensible.


### Important caveats

- The protein is the beta subunit of a 'Heme-dependent oxidative N-demethylase' (HODM). The heme cofactor (option C) belongs to the alpha subunit, not this beta subunit, so C is correctly excluded.
- Both &#91;2Fe-2S&#93; and FMN are experimentally confirmed cofactors (PubMed:27851736). The question's singular phrasing ('the specific cofactor') is imprecise given that two cofactors are annotated.
- The &#91;2Fe-2S&#93; evidence includes both computational (PROSITE-ProRule) and experimental (PubMed) support, while FMN has only experimental support from the same paper.
- The 2Fe-2S cysteine spacing (C-X4-C-X2-C-X35-C) deviates somewhat from the canonical C-X2-C-X3-C-X2-C pattern, but variable spacing is known in some 2Fe-2S proteins, particularly those with split binding sites across domains.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the sequence contains a cysteine cluster: 'CRGGVCGQCQTPWLKGDVEHRDHFLSANERTSSLMPCVSRGCGSPILLDL.' The pattern of four cysteines (C-X4-C-X2-C-X35-C) is recognizable as a 2Fe-2S cluster-binding motif using transferable knowledge of ferredoxin-type and Rieske-type iron-sulfur proteins. PROSITE ProRule PRU00465 (2Fe-2S ferredoxin-like domain) is a well-known family-level pattern. Additionally, the protein contains a Rossmann-fold-like motif 'AAGIGITPFLAYSQ' (GxGxxP pattern) suggestive of FMN or dinucleotide binding, but this motif is less diagnostically specific (it could indicate FMN, FAD, NADH, or NADPH). The [2Fe-2S] cysteine motif is a more uniquely identifiable and specific sequence signature, making B the more defensible single answer when the question asks for 'the specific cofactor.'",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the 2Fe-2S cluster-binding cysteine motif from the C-terminal sequence using well-established family-level knowledge of iron-sulfur protein motifs (ferredoxin-type, Rieske-type). This is a legitimate transferable inference from other proteins. The FMN Rossmann motif is also present, creating some ambiguity, but the [2Fe-2S] motif is more uniquely diagnostic from sequence alone, providing a credible basis to prefer B over D."
  },
  "case_id": "cofactor_0068",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A4XXY8) explicitly lists [2Fe-2S] cluster as a cofactor with evidence codes ECO:0000255 (PROSITE-ProRule PRU00465, computational) and ECO:0000269 (PubMed:27851736, experimental), stating 'Binds 1 2Fe-2S cluster per subunit.' The author's answer B is directly supported. However, FMN (option D) is also listed as a cofactor with experimental evidence (ECO:0000269, PubMed:27851736), so the answer is supported but not uniquely so."
  },
  "important_caveats": [
    "The protein is the beta subunit of a 'Heme-dependent oxidative N-demethylase' (HODM). The heme cofactor (option C) belongs to the alpha subunit, not this beta subunit, so C is correctly excluded.",
    "Both [2Fe-2S] and FMN are experimentally confirmed cofactors (PubMed:27851736). The question's singular phrasing ('the specific cofactor') is imprecise given that two cofactors are annotated.",
    "The [2Fe-2S] evidence includes both computational (PROSITE-ProRule) and experimental (PubMed) support, while FMN has only experimental support from the same paper.",
    "The 2Fe-2S cysteine spacing (C-X4-C-X2-C-X35-C) deviates somewhat from the canonical C-X2-C-X3-C-X2-C pattern, but variable spacing is known in some 2Fe-2S proteins, particularly those with split binding sites across domains."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "The UniProt entry lists both [2Fe-2S] cluster and FMN as cofactors of this protein, both with experimental evidence from PubMed:27851736. The question asks for 'the specific cofactor' (singular), but the protein requires both. A model identifying the Rossmann-fold FMN-binding motif could reasonably select D. The [2Fe-2S] motif is arguably more uniquely identifiable from sequence, giving B a slight edge, but D remains defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0068",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A4XXY8) explicitly lists [2Fe-2S] cluster as a cofactor with evidence codes ECO:0000255 (PROSITE-ProRule PRU00465, computational) and ECO:0000269 (PubMed:27851736, experimental), stating 'Binds 1 2Fe-2S cluster per subunit.' The author's answer B is directly supported. However, FMN (option D) is also listed as a cofactor with experimental evidence (ECO:0000269, PubMed:27851736), so the answer is supported but not uniquely so.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the sequence contains a cysteine cluster: 'CRGGVCGQCQTPWLKGDVEHRDHFLSANERTSSLMPCVSRGCGSPILLDL.' The pattern of four cysteines (C-X4-C-X2-C-X35-C) is recognizable as a 2Fe-2S cluster-binding motif using transferable knowledge of ferredoxin-type and Rieske-type iron-sulfur proteins. PROSITE ProRule PRU00465 (2Fe-2S ferredoxin-like domain) is a well-known family-level pattern. Additionally, the protein contains a Rossmann-fold-like motif 'AAGIGITPFLAYSQ' (GxGxxP pattern) suggestive of FMN or dinucleotide binding, but this motif is less diagnostically specific (it could indicate FMN, FAD, NADH, or NADPH). The [2Fe-2S] cysteine motif is a more uniquely identifiable and specific sequence signature, making B the more defensible single answer when the question asks for 'the specific cofactor.'",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the 2Fe-2S cluster-binding cysteine motif from the C-terminal sequence using well-established family-level knowledge of iron-sulfur protein motifs (ferredoxin-type, Rieske-type). This is a legitimate transferable inference from other proteins. The FMN Rossmann motif is also present, creating some ambiguity, but the [2Fe-2S] motif is more uniquely diagnostic from sequence alone, providing a credible basis to prefer B over D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "The UniProt entry lists both [2Fe-2S] cluster and FMN as cofactors of this protein, both with experimental evidence from PubMed:27851736. The question asks for 'the specific cofactor' (singular), but the protein requires both. A model identifying the Rossmann-fold FMN-binding motif could reasonably select D. The [2Fe-2S] motif is arguably more uniquely identifiable from sequence, giving B a slight edge, but D remains defensible."
  },
  "important_caveats": [
    "The protein is the beta subunit of a 'Heme-dependent oxidative N-demethylase' (HODM). The heme cofactor (option C) belongs to the alpha subunit, not this beta subunit, so C is correctly excluded.",
    "Both [2Fe-2S] and FMN are experimentally confirmed cofactors (PubMed:27851736). The question's singular phrasing ('the specific cofactor') is imprecise given that two cofactors are annotated.",
    "The [2Fe-2S] evidence includes both computational (PROSITE-ProRule) and experimental (PubMed) support, while FMN has only experimental support from the same paper.",
    "The 2Fe-2S cysteine spacing (C-X4-C-X2-C-X35-C) deviates somewhat from the canonical C-X2-C-X3-C-X2-C pattern, but variable spacing is known in some 2Fe-2S proteins, particularly those with split binding sites across domains."
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
  "benchmark_sequence_length": 309,
  "benchmark_sequence_sha256": "bda6ab24214df28092cbdba9684d36de583471faedd3a23726c54f1bcc731122",
  "current_entry_audit": {
    "entryVersion": 115,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-05-29",
    "sequenceVersion": 1
  },
  "current_record_sha256": "14091c473d916fc14eb92a56db9612f8840e33b147125c29052c25bb91a96bf1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 309,
  "current_source_sequence_sha256": "bda6ab24214df28092cbdba9684d36de583471faedd3a23726c54f1bcc731122",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 114,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A4XXY8",
  "selected_historical_entry_version": 114,
  "selected_historical_record_sha256": "76f92cfc1f9ead1f561371a2da8acce3787355263fc28bb8326613f4ec3df955",
  "selected_historical_source_sequence_length": 309,
  "selected_historical_source_sequence_sha256": "bda6ab24214df28092cbdba9684d36de583471faedd3a23726c54f1bcc731122",
  "selected_historical_version": {
    "accession": "A4XXY8",
    "database": "Swiss-Prot",
    "entryVersion": 114,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "HODMB_ECTM1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A4XXY8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:59.775561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14091c473d916fc14eb92a56db9612f8840e33b147125c29052c25bb91a96bf1",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":115,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-05-29\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:59.775561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14091c473d916fc14eb92a56db9612f8840e33b147125c29052c25bb91a96bf1",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Pseudomonas mendocina\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Pseudomonadales\",\"Pseudomonadaceae\",\"Ectopseudomonas\"],\"scientificName\":\"Ectopseudomonas mendocina (strain ymp)\",\"taxonId\":399739}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:59.775561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14091c473d916fc14eb92a56db9612f8840e33b147125c29052c25bb91a96bf1",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"27851736\",\"source\":\"PubMed\"}],\"value\":\"1.6.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27851736\",\"source\":\"PubMed\"}],\"value\":\"Heme-dependent oxidative N-demethylase beta subunit\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"27851736\",\"source\":\"PubMed\"}],\"value\":\"HODM beta subunit\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:59.775561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14091c473d916fc14eb92a56db9612f8840e33b147125c29052c25bb91a96bf1",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:190135\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00465\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27851736\",\"source\":\"PubMed\"}],\"name\":\"[2Fe-2S] cluster\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU00465\",\"source\":\"PROSITE-ProRule\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27851736\",\"source\":\"PubMed\"}],\"value\":\"Binds 1 2Fe-2S cluster per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:59.775561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14091c473d916fc14eb92a56db9612f8840e33b147125c29052c25bb91a96bf1",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"27851736\",\"source\":\"PubMed\"}],\"name\":\"FMN\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:26:59.775561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14091c473d916fc14eb92a56db9612f8840e33b147125c29052c25bb91a96bf1",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A4XXY8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Ortmayer M.\",\"Lafite P.\",\"Menon B.R.\",\"Tralau T.\",\"Fisher K.\",\"Denkhaus L.\",\"Scrutton N.S.\",\"Rigby S.E.\",\"Munro A.W.\",\"Hay S.\",\"Leys D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"27851736\"},{\"database\":\"DOI\",\"id\":\"10.1038/nature20159\"}],\"citationType\":\"journal article\",\"firstPage\":\"593\",\"id\":\"27851736\",\"journal\":\"Nature\",\"lastPage\":\"597\",\"publicationDate\":\"2016\",\"title\":\"An oxidative N-demethylase reveals PAS transition from ubiquitous sensor to enzyme.\",\"volume\":\"539\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"COFACTOR\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:59.775561+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "14091c473d916fc14eb92a56db9612f8840e33b147125c29052c25bb91a96bf1",
  "url": "https://rest.uniprot.org/uniprotkb/A4XXY8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H1",
  "excerpt": "ID   HODMB_ECTM1             Reviewed;         309 AA.\nAC   A4XXY8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   29-MAY-2007, sequence version 1.\nDT   28-JAN-2026, entry version 114.\nDE   RecName: Full=Heme-dependent oxidative N-demethylase beta subunit {ECO:0000303|PubMed:27851736};\nDE            Short=HODM beta subunit {ECO:0000303|PubMed:27851736};\nDE            EC=1.6.2.- {ECO:0000305|PubMed:27851736};\nGN   OrderedLocusNames=Pmen_3454 {ECO:0000312|EMBL:ABP86204.1};\nOS   Ectopseudomonas mendocina (strain ymp) (Pseudomonas mendocina).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Pseudomonadales; Pseudomonadaceae; Ectopseudomonas.\nOX   NCBI_TaxID=399739;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:01.748975+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "76f92cfc1f9ead1f561371a2da8acce3787355263fc28bb8326613f4ec3df955",
  "url": "https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Heme-dependent oxidative N-demethylase beta subunit {ECO:0000303|PubMed:27851736};\nDE            Short=HODM beta subunit {ECO:0000303|PubMed:27851736};\nDE            EC=1.6.2.- {ECO:0000305|PubMed:27851736};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:01.748975+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "76f92cfc1f9ead1f561371a2da8acce3787355263fc28bb8326613f4ec3df955",
  "url": "https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, COFACTOR, AND SUBUNIT.\nRX   PubMed=27851736; DOI=10.1038/nature20159;\nRA   Ortmayer M., Lafite P., Menon B.R., Tralau T., Fisher K., Denkhaus L.,\nRA   Scrutton N.S., Rigby S.E., Munro A.W., Hay S., Leys D.;\nRT   \"An oxidative N-demethylase reveals PAS transition from ubiquitous sensor\nRT   to enzyme.\";\nRL   Nature 539:593-597(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:01.748975+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "76f92cfc1f9ead1f561371a2da8acce3787355263fc28bb8326613f4ec3df955",
  "url": "https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=[2Fe-2S] cluster; Xref=ChEBI:CHEBI:190135;\nCC         Evidence={ECO:0000255|PROSITE-ProRule:PRU00465,\nCC         ECO:0000269|PubMed:27851736};\nCC       Note=Binds 1 2Fe-2S cluster per subunit. {ECO:0000255|PROSITE-\nCC       ProRule:PRU00465, ECO:0000269|PubMed:27851736};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:01.748975+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-44",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "76f92cfc1f9ead1f561371a2da8acce3787355263fc28bb8326613f4ec3df955",
  "url": "https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114)

```json
{
  "entry_version": 114,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FMN; Xref=ChEBI:CHEBI:58210;\nCC         Evidence={ECO:0000269|PubMed:27851736};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:01.748975+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "76f92cfc1f9ead1f561371a2da8acce3787355263fc28bb8326613f4ec3df955",
  "url": "https://rest.uniprot.org/unisave/A4XXY8?format=txt&versions=114"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 68. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
