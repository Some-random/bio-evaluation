# EC_number_0029

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0029.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 1.14.11.65

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSQKELAALVATRTSRKRTISSTSFSISTRTDPKSIIEIHIFNDSLPIKRACCEVENPTLKAEQRVQQEEESLGQVPPLTEEEQQRHDEFRNSGSIFLQDLPCFKLQQAQPIAGSSPIPKCRECRRRNLATTEGEPSSVSDVYCRFYEFRRLQFNENGELCVVGFPNPYSEPSPEDIAIWQPDKNTPPTSGYMDIQVCRYILLHAGDQFCYIWHQEAEALSLHQNTDGTIAWKKAVKGTREICDVCDTTLFNYHWTCRKCGFGVCLDCVKDRKEGLRLRRAENAAQKGCDEYHWLLCSDPSGPQEHVLTELMLTQIIAGDALNVLGRLLHEVRTLWQVPQVCGCLLSKQAIEDAQSKEVIQDMIKESQLKQHTSYSSLASEQKVHQQQRLDQLHATKLEFARELGVDYVPGRVWTKETLGKDPITTAFDNLKHINFLRKGLAGLRRFLPPRTMTFAYSTQLAPGVPHEFLCDGRLLRLTDAMHPDNRVLFQEVWKCGQPVMISEVARSLNLDLWHPQAFCRDFGDKPNDLINCLNGNLVPNQPMRHFWEGFQCMTKRLPDAYGKPMLLKLKDWPPGDDFAEILPTRFADLMKGLPMPEYTLRTGNLNIASCLPKMFVPPDLGPKMYNAYGSALHPDKGTTNLHLDISDAVNIMVYVGIPQDGDTRPQMAATQKAIEIGGCDYITRARCQSPDVLPGALWHIFPARDADKIRDLLNRVTLEKGFRLEPDHDPIHDQNWYLDDKLRARLFKEYGVEGHPIVQCLGDAVFIPAGAPHQVQNLHNCIKVAEDFVSPENITHCYHLTHEFRRLSHSHTNHEDKLQIKNIIYHAIKDCCTILTRAVDERLNAELTKLNAD

[Multiple Choices]
A. 1.14.11.65
B. 1.14.11.63
C. 2.1.1.34
D. 1.97.1.14
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

> The sequence-matched UniProt record assigns EC 1.14.11.65 and the corresponding histone H3 lysine-demethylation reaction. However, the annotation is transferred by similarity from another UniProt protein (ECO:0000250), not evidence of direct experimental characterization of this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence's cysteine-rich region and conserved JmjC 2-oxoglutarate/iron-dependent dioxygenase features support a JmjC histone lysine demethylase, rather than a methyltransferase (C) or the unrelated broad oxidoreductase choice (D). Its domain architecture and family-level pattern are consistent with KDM3-type demethylases, supporting A over the alternative demethylase EC number B. This is a transferable family inference, not a guarantee of the exact substrate annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model could use the sequence's catalytic-family features and learned KDM-family patterns to distinguish the offered choices without knowing this exact protein's database record. The distinction between the two demethylase options is probabilistic from sequence and family recognition, not experimental proof.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence and family-level inference favor A among the supplied alternatives; no other option is comparably supported.


### Important caveats

- The reviewer-only annotation is similarity-transferred and does not establish direct experimental validation for the supplied protein.
- The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence's cysteine-rich region and conserved JmjC 2-oxoglutarate/iron-dependent dioxygenase features support a JmjC histone lysine demethylase, rather than a methyltransferase (C) or the unrelated broad oxidoreductase choice (D). Its domain architecture and family-level pattern are consistent with KDM3-type demethylases, supporting A over the alternative demethylase EC number B. This is a transferable family inference, not a guarantee of the exact substrate annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use the sequence's catalytic-family features and learned KDM-family patterns to distinguish the offered choices without knowing this exact protein's database record. The distinction between the two demethylase options is probabilistic from sequence and family recognition, not experimental proof."
  },
  "case_id": "EC_number_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.14.11.65 and the corresponding histone H3 lysine-demethylation reaction. However, the annotation is transferred by similarity from another UniProt protein (ECO:0000250), not evidence of direct experimental characterization of this exact protein."
  },
  "important_caveats": [
    "The reviewer-only annotation is similarity-transferred and does not establish direct experimental validation for the supplied protein.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence and family-level inference favor A among the supplied alternatives; no other option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 1.14.11.65 and the corresponding histone H3 lysine-demethylation reaction. However, the annotation is transferred by similarity from another UniProt protein (ECO:0000250), not evidence of direct experimental characterization of this exact protein.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence's cysteine-rich region and conserved JmjC 2-oxoglutarate/iron-dependent dioxygenase features support a JmjC histone lysine demethylase, rather than a methyltransferase (C) or the unrelated broad oxidoreductase choice (D). Its domain architecture and family-level pattern are consistent with KDM3-type demethylases, supporting A over the alternative demethylase EC number B. This is a transferable family inference, not a guarantee of the exact substrate annotation.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model could use the sequence's catalytic-family features and learned KDM-family patterns to distinguish the offered choices without knowing this exact protein's database record. The distinction between the two demethylase options is probabilistic from sequence and family recognition, not experimental proof."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence and family-level inference favor A among the supplied alternatives; no other option is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only annotation is similarity-transferred and does not establish direct experimental validation for the supplied protein.",
    "The source sequence matches the supplied sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q9VHC5 (KDM3_DROME, Drosophila melanogaster) is annotated with EC 1.14.11.65 (Lysine-specific demethylase 3). The catalytic activity listed is N6,N6-dimethyl-L-lysyl(9)-&#91;histone H3&#93; + 2 2-oxoglutarate + 2 O2 → L-lysyl(9)-&#91;histone H3&#93; + 2 formaldehyde + 2 succinate + 2 CO2. The sequence matches the benchmark input exactly (854 aa, SHA256 matched). However, the EC annotation carries evidence code ECO:0000250 (inferred by similarity from human Q9Y4C1/KDM3A), so it is a computational transfer rather than direct experimental evidence for this fly protein. The annotation is consistent across current (v182) and historical (v180) records.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear JmjC domain with the HxD…H Fe(II)/2-oxoglutarate oxygenase triad (HAGDQ…H…H), identifying it as a JmjC-domain histone demethylase. This eliminates EC 2.1.1.34 (a methyltransferase, EC class 2) and EC 1.97.1.14 (an oxidoreductase, EC class 1.97). Between the two remaining JmjC demethylase options—EC 1.14.11.65 (KDM3/JMJD2 family, H3K9me1/me2 demethylase) and EC 1.14.11.63 (KDM5/JARID1 family, H3K4me3/me2 demethylase)—the domain architecture is diagnostic. The sequence contains a CW domain (the 'CDYITRARCQ…C' zinc-binding module that recognizes H3K4me3) and a Tudor domain, which are hallmark features of the KDM3 subfamily. The KDM5 family instead carries an ARID domain and a JmjN domain, neither of which is present here. This domain-architecture distinction (JmjC + PHD + CW + Tudor → KDM3 vs. JmjN + ARID + JmjC + multiple PHDs → KDM5) is well-established transferable knowledge about histone demethylase families and meaningfully favors option A over option B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The JmjC triad identifies the protein as a histone demethylase (eliminating C and D). The presence of a CW domain and Tudor domain, with absence of ARID/JmjN domains, is a family-level architectural signature that distinguishes KDM3 (EC 1.14.11.65) from KDM5 (EC 1.14.11.63). This inference relies on conserved domain features shared across the KDM superfamily and does not require recalling the specific database entry for this exact fly protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C (methyltransferase) and D (oxidoreductase) are eliminated by the clear JmjC oxygenase triad. Between A and B, the CW domain architecture provides a credible family-level distinction favoring A. While the annotation is by similarity rather than direct experiment, the domain architecture argument is sufficiently specific to KDM3 to make A the clearly preferred choice over B.


### Important caveats

- The EC 1.14.11.65 annotation for Q9VHC5 is based on similarity transfer (ECO:0000250) from human KDM3A (Q9Y4C1), not direct experimental characterization of the Drosophila protein.
- The CW domain argument strongly suggests KDM3 family membership, but absolute certainty about the exact substrate residue specificity (H3K9 vs. H3K4) would require experimental data or a closer sequence alignment to characterized KDM3/KDM5 members.
- The 'HAGDQ' motif at the start of the JmjC domain is characteristic of the KDM3/JMJD2 subfamily but is not exclusive; the full domain architecture is the stronger discriminator.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear JmjC domain with the HxD…H Fe(II)/2-oxoglutarate oxygenase triad (HAGDQ…H…H), identifying it as a JmjC-domain histone demethylase. This eliminates EC 2.1.1.34 (a methyltransferase, EC class 2) and EC 1.97.1.14 (an oxidoreductase, EC class 1.97). Between the two remaining JmjC demethylase options—EC 1.14.11.65 (KDM3/JMJD2 family, H3K9me1/me2 demethylase) and EC 1.14.11.63 (KDM5/JARID1 family, H3K4me3/me2 demethylase)—the domain architecture is diagnostic. The sequence contains a CW domain (the 'CDYITRARCQ…C' zinc-binding module that recognizes H3K4me3) and a Tudor domain, which are hallmark features of the KDM3 subfamily. The KDM5 family instead carries an ARID domain and a JmjN domain, neither of which is present here. This domain-architecture distinction (JmjC + PHD + CW + Tudor → KDM3 vs. JmjN + ARID + JmjC + multiple PHDs → KDM5) is well-established transferable knowledge about histone demethylase families and meaningfully favors option A over option B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The JmjC triad identifies the protein as a histone demethylase (eliminating C and D). The presence of a CW domain and Tudor domain, with absence of ARID/JmjN domains, is a family-level architectural signature that distinguishes KDM3 (EC 1.14.11.65) from KDM5 (EC 1.14.11.63). This inference relies on conserved domain features shared across the KDM superfamily and does not require recalling the specific database entry for this exact fly protein."
  },
  "case_id": "EC_number_0029",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q9VHC5 (KDM3_DROME, Drosophila melanogaster) is annotated with EC 1.14.11.65 (Lysine-specific demethylase 3). The catalytic activity listed is N6,N6-dimethyl-L-lysyl(9)-[histone H3] + 2 2-oxoglutarate + 2 O2 → L-lysyl(9)-[histone H3] + 2 formaldehyde + 2 succinate + 2 CO2. The sequence matches the benchmark input exactly (854 aa, SHA256 matched). However, the EC annotation carries evidence code ECO:0000250 (inferred by similarity from human Q9Y4C1/KDM3A), so it is a computational transfer rather than direct experimental evidence for this fly protein. The annotation is consistent across current (v182) and historical (v180) records."
  },
  "important_caveats": [
    "The EC 1.14.11.65 annotation for Q9VHC5 is based on similarity transfer (ECO:0000250) from human KDM3A (Q9Y4C1), not direct experimental characterization of the Drosophila protein.",
    "The CW domain argument strongly suggests KDM3 family membership, but absolute certainty about the exact substrate residue specificity (H3K9 vs. H3K4) would require experimental data or a closer sequence alignment to characterized KDM3/KDM5 members.",
    "The 'HAGDQ' motif at the start of the JmjC domain is characteristic of the KDM3/JMJD2 subfamily but is not exclusive; the full domain architecture is the stronger discriminator."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (methyltransferase) and D (oxidoreductase) are eliminated by the clear JmjC oxygenase triad. Between A and B, the CW domain architecture provides a credible family-level distinction favoring A. While the annotation is by similarity rather than direct experiment, the domain architecture argument is sufficiently specific to KDM3 to make A the clearly preferred choice over B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0029",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q9VHC5 (KDM3_DROME, Drosophila melanogaster) is annotated with EC 1.14.11.65 (Lysine-specific demethylase 3). The catalytic activity listed is N6,N6-dimethyl-L-lysyl(9)-[histone H3] + 2 2-oxoglutarate + 2 O2 → L-lysyl(9)-[histone H3] + 2 formaldehyde + 2 succinate + 2 CO2. The sequence matches the benchmark input exactly (854 aa, SHA256 matched). However, the EC annotation carries evidence code ECO:0000250 (inferred by similarity from human Q9Y4C1/KDM3A), so it is a computational transfer rather than direct experimental evidence for this fly protein. The annotation is consistent across current (v182) and historical (v180) records.",
    "evidence_ids": ["C4", "C5", "H1", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear JmjC domain with the HxD…H Fe(II)/2-oxoglutarate oxygenase triad (HAGDQ…H…H), identifying it as a JmjC-domain histone demethylase. This eliminates EC 2.1.1.34 (a methyltransferase, EC class 2) and EC 1.97.1.14 (an oxidoreductase, EC class 1.97). Between the two remaining JmjC demethylase options—EC 1.14.11.65 (KDM3/JMJD2 family, H3K9me1/me2 demethylase) and EC 1.14.11.63 (KDM5/JARID1 family, H3K4me3/me2 demethylase)—the domain architecture is diagnostic. The sequence contains a CW domain (the 'CDYITRARCQ…C' zinc-binding module that recognizes H3K4me3) and a Tudor domain, which are hallmark features of the KDM3 subfamily. The KDM5 family instead carries an ARID domain and a JmjN domain, neither of which is present here. This domain-architecture distinction (JmjC + PHD + CW + Tudor → KDM3 vs. JmjN + ARID + JmjC + multiple PHDs → KDM5) is well-established transferable knowledge about histone demethylase families and meaningfully favors option A over option B.",
    "missing_item_specific_fact": "",
    "reason": "The JmjC triad identifies the protein as a histone demethylase (eliminating C and D). The presence of a CW domain and Tudor domain, with absence of ARID/JmjN domains, is a family-level architectural signature that distinguishes KDM3 (EC 1.14.11.65) from KDM5 (EC 1.14.11.63). This inference relies on conserved domain features shared across the KDM superfamily and does not require recalling the specific database entry for this exact fly protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C (methyltransferase) and D (oxidoreductase) are eliminated by the clear JmjC oxygenase triad. Between A and B, the CW domain architecture provides a credible family-level distinction favoring A. While the annotation is by similarity rather than direct experiment, the domain architecture argument is sufficiently specific to KDM3 to make A the clearly preferred choice over B."
  },
  "important_caveats": [
    "The EC 1.14.11.65 annotation for Q9VHC5 is based on similarity transfer (ECO:0000250) from human KDM3A (Q9Y4C1), not direct experimental characterization of the Drosophila protein.",
    "The CW domain argument strongly suggests KDM3 family membership, but absolute certainty about the exact substrate residue specificity (H3K9 vs. H3K4) would require experimental data or a closer sequence alignment to characterized KDM3/KDM5 members.",
    "The 'HAGDQ' motif at the start of the JmjC domain is characteristic of the KDM3/JMJD2 subfamily but is not exclusive; the full domain architecture is the stronger discriminator."
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
  "benchmark_sequence_length": 854,
  "benchmark_sequence_sha256": "dd3548960b1682de998fc074af92b0ccddb61dace402f81acf39413836fe202f",
  "current_entry_audit": {
    "entryVersion": 182,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "988cd450ac6d94115d3a0a907f3be7bea9fa1fb8ec7323334e09bde36a991b80",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 854,
  "current_source_sequence_sha256": "dd3548960b1682de998fc074af92b0ccddb61dace402f81acf39413836fe202f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 180,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VHC5",
  "selected_historical_entry_version": 180,
  "selected_historical_record_sha256": "f5da474d2b6eef609a1e0f06b8a3e0427dad5c78083068d262116ce5e8a89bbd",
  "selected_historical_source_sequence_length": 854,
  "selected_historical_source_sequence_sha256": "dd3548960b1682de998fc074af92b0ccddb61dace402f81acf39413836fe202f",
  "selected_historical_version": {
    "accession": "Q9VHC5",
    "database": "Swiss-Prot",
    "entryVersion": 180,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "KDM3_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHC5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VHC5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:18.636093+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "988cd450ac6d94115d3a0a907f3be7bea9fa1fb8ec7323334e09bde36a991b80",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VHC5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHC5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":182,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:18.636093+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "988cd450ac6d94115d3a0a907f3be7bea9fa1fb8ec7323334e09bde36a991b80",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VHC5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHC5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:18.636093+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "988cd450ac6d94115d3a0a907f3be7bea9fa1fb8ec7323334e09bde36a991b80",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VHC5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHC5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9Y4C1\",\"source\":\"UniProtKB\"}],\"value\":\"1.14.11.65\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0037703\",\"source\":\"FlyBase\"}],\"value\":\"Lysine-specific demethylase 3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:18.636093+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "988cd450ac6d94115d3a0a907f3be7bea9fa1fb8ec7323334e09bde36a991b80",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VHC5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VHC5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"1.14.11.65\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9Y4C1\",\"source\":\"UniProtKB\"}],\"name\":\"N(6),N(6)-dimethyl-L-lysyl(9)-[histone H3] + 2 2-oxoglutarate + 2 O2 = L-lysyl(9)-[histone H3] + 2 formaldehyde + 2 succinate + 2 CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:60188\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15541\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15546\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16810\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16842\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29969\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30031\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61976\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:18.636093+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "988cd450ac6d94115d3a0a907f3be7bea9fa1fb8ec7323334e09bde36a991b80",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VHC5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHC5?format=txt&versions=180)

```json
{
  "entry_version": 180,
  "evidence_id": "H1",
  "excerpt": "ID   KDM3_DROME              Reviewed;         854 AA.\nAC   Q9VHC5;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 180.\nDE   RecName: Full=Lysine-specific demethylase 3 {ECO:0000312|FlyBase:FBgn0037703};\nDE            EC=1.14.11.65 {ECO:0000250|UniProtKB:Q9Y4C1};\nGN   Name=Kdm3 {ECO:0000312|FlyBase:FBgn0037703};\nGN   Synonyms=JHDM2 {ECO:0000312|FlyBase:FBgn0037703};\nGN   ORFNames=CG8165 {ECO:0000312|FlyBase:FBgn0037703};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:24.066442+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f5da474d2b6eef609a1e0f06b8a3e0427dad5c78083068d262116ce5e8a89bbd",
  "url": "https://rest.uniprot.org/unisave/Q9VHC5?format=txt&versions=180"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHC5?format=txt&versions=180)

```json
{
  "entry_version": 180,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Lysine-specific demethylase 3 {ECO:0000312|FlyBase:FBgn0037703};\nDE            EC=1.14.11.65 {ECO:0000250|UniProtKB:Q9Y4C1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:24.066442+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f5da474d2b6eef609a1e0f06b8a3e0427dad5c78083068d262116ce5e8a89bbd",
  "url": "https://rest.uniprot.org/unisave/Q9VHC5?format=txt&versions=180"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VHC5?format=txt&versions=180)

```json
{
  "entry_version": 180,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N(6),N(6)-dimethyl-L-lysyl(9)-[histone H3] + 2 2-oxoglutarate\nCC         + 2 O2 = L-lysyl(9)-[histone H3] + 2 formaldehyde + 2 succinate + 2\nCC         CO2; Xref=Rhea:RHEA:60188, Rhea:RHEA-COMP:15541, Rhea:RHEA-\nCC         COMP:15546, ChEBI:CHEBI:15379, ChEBI:CHEBI:16526, ChEBI:CHEBI:16810,\nCC         ChEBI:CHEBI:16842, ChEBI:CHEBI:29969, ChEBI:CHEBI:30031,\nCC         ChEBI:CHEBI:61976; EC=1.14.11.65;\nCC         Evidence={ECO:0000250|UniProtKB:Q9Y4C1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:24.066442+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 122-129",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f5da474d2b6eef609a1e0f06b8a3e0427dad5c78083068d262116ce5e8a89bbd",
  "url": "https://rest.uniprot.org/unisave/Q9VHC5?format=txt&versions=180"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 29. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
