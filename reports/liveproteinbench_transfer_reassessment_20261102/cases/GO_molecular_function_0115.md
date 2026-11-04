# GO_molecular_function_0115

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0115.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — phosphopantothenoylcysteine decarboxylase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTSSEPASPEIEQQANSAPRRPRILLAASGSVAAIKFGNLCHSFSEWAEVKAVATRASLHFIDRASLPKDVILYTEEDEWSTWNKVGDSVLHIELRSWADILVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTLMWKNPFTEQHIMSIDELGVSLIPPVTKRLACGDYGNGAMAEPSVIYSTVRLFFESRVQQSGNIVQQPV

[Multiple Choices]
A. ATP hydrolysis activity
B. phosphopantothenoylcysteine decarboxylase activity
C. potassium channel regulator activity
D. peroxidase inhibitor activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record reports phosphopantothenoylcysteine decarboxylase activity and the corresponding catalytic reaction, citing experimental evidence (ECO:0000269). The matching GO annotation also assigns the activity with IDA evidence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 214-aa sequence is consistent with the compact soluble HAL3/PPCDC enzyme family, whose conserved family features support phosphopantothenoylcysteine decarboxylase activity. It also lacks an obvious P-loop nucleotide-binding motif expected for many ATP-hydrolyzing proteins, while the sequence offers no clear basis for a potassium-channel-regulatory or peroxidase-inhibitory role. This makes B meaningfully distinguishable among these choices, though sequence-based family recognition is not experimental proof.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable family-level inference can identify the likely enzyme activity from the sequence and distinguish it from the offered alternatives; the exact protein's recorded annotation is not necessary to make that inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the supplied choices, the PPCDC family inference supports B; the alternatives describe activities for which the sequence provides no comparably credible signal.


### Important caveats

- The reviewer-only record supports the key but was not part of the original model input.
- The family-level sequence inference is probabilistic and does not independently establish experimentally measured activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 214-aa sequence is consistent with the compact soluble HAL3/PPCDC enzyme family, whose conserved family features support phosphopantothenoylcysteine decarboxylase activity. It also lacks an obvious P-loop nucleotide-binding motif expected for many ATP-hydrolyzing proteins, while the sequence offers no clear basis for a potassium-channel-regulatory or peroxidase-inhibitory role. This makes B meaningfully distinguishable among these choices, though sequence-based family recognition is not experimental proof.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable family-level inference can identify the likely enzyme activity from the sequence and distinguish it from the offered alternatives; the exact protein's recorded annotation is not necessary to make that inference."
  },
  "case_id": "GO_molecular_function_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports phosphopantothenoylcysteine decarboxylase activity and the corresponding catalytic reaction, citing experimental evidence (ECO:0000269). The matching GO annotation also assigns the activity with IDA evidence."
  },
  "important_caveats": [
    "The reviewer-only record supports the key but was not part of the original model input.",
    "The family-level sequence inference is probabilistic and does not independently establish experimentally measured activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the supplied choices, the PPCDC family inference supports B; the alternatives describe activities for which the sequence provides no comparably credible signal."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports phosphopantothenoylcysteine decarboxylase activity and the corresponding catalytic reaction, citing experimental evidence (ECO:0000269). The matching GO annotation also assigns the activity with IDA evidence.",
    "evidence_ids": ["C5", "C6", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 214-aa sequence is consistent with the compact soluble HAL3/PPCDC enzyme family, whose conserved family features support phosphopantothenoylcysteine decarboxylase activity. It also lacks an obvious P-loop nucleotide-binding motif expected for many ATP-hydrolyzing proteins, while the sequence offers no clear basis for a potassium-channel-regulatory or peroxidase-inhibitory role. This makes B meaningfully distinguishable among these choices, though sequence-based family recognition is not experimental proof.",
    "missing_item_specific_fact": "",
    "reason": "A transferable family-level inference can identify the likely enzyme activity from the sequence and distinguish it from the offered alternatives; the exact protein's recorded annotation is not necessary to make that inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the supplied choices, the PPCDC family inference supports B; the alternatives describe activities for which the sequence provides no comparably credible signal."
  },
  "important_caveats": [
    "The reviewer-only record supports the key but was not part of the original model input.",
    "The family-level sequence inference is probabilistic and does not independently establish experimentally measured activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A498JQK2 is annotated with GO:0004633 (phosphopantothenoylcysteine decarboxylase activity) with IDA evidence code (Inferred by Direct Assay) from PubMed:32761275, an experimental study confirming the catalytic reaction N-&#91;(R)-4-phosphopantothenoyl&#93;-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2 (EC 4.1.1.36, RHEA:16793). The sequence matches the benchmark exactly (SHA256 confirmed). The expected answer B is directly supported by experimental biochemical evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is ~214 aa, small and compact. It lacks Walker A (GxxxxGK&#91;S/T&#93;) and Walker B motifs required for ATP hydrolysis (eliminates A). It lacks ion-channel regulatory domains or transmembrane segments associated with potassium channel regulators (eliminates C). It lacks peroxidase-binding interfaces characteristic of peroxidase inhibitors (eliminates D). The sequence contains motifs characteristic of the PPCDC/vanillate-decarboxylase superfamily: the 'GDSVLH' segment in the FMN-binding region and the conserved 'LACGDYGNGA' motif, both hallmarks of the PPCDC family (Pfam PF02198) well-studied in yeast (DEC1) and human orthologs. The small size, FMN-binding-like architecture, and these conserved motifs are transferable family-level features recognized across PPCDC homologs. Among the four options, only B (a carboxy-lyase/decarboxylase) is consistent with a small FMN-dependent enzyme bearing these motifs, while the other three require entirely different structural and mechanistic features absent from the sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition of PPCDC sequence signatures (FMN-binding motifs, conserved 'GDSVLH...LACGDYGNGA' pattern, small size) combined with elimination of the three distractors (no ATPase motifs, no channel-regulatory domains, no peroxidase-inhibitor interface) provides a concrete, transferable inference from general protein-family knowledge learned from other PPCDC/vanillate-decarboxylase homologs. This does not require recalling the specific UniProt record for this exact apple protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors require structural/mechanistic features (P-loop for ATPase, channel-binding domains for K+ regulator, peroxidase interface for inhibitor) that are clearly absent from the sequence. Only B is consistent with the observed small FMN-decarboxylase architecture and PPCDC-family motifs. No ambiguity among the offered choices.


### Important caveats

- The GO:0010181 (FMN binding) annotation is IEA:TreeGrafter (computational transfer), not experimental, but it is consistent with the known FMN-dependence of PPCDC family members.
- The PPCDC family is related to vanillate/4-hydroxybenzoate decarboxylases; precise sub-family assignment from sequence alone has some uncertainty, but among the four offered choices only a decarboxylase (B) is mechanistically compatible.
- The experimental evidence (PubMed:32761275) was published in 2020; the UniProt entry was first public in 2025. The benchmark sequence and annotation are consistent across the historical snapshot checked.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is ~214 aa, small and compact. It lacks Walker A (GxxxxGK[S/T]) and Walker B motifs required for ATP hydrolysis (eliminates A). It lacks ion-channel regulatory domains or transmembrane segments associated with potassium channel regulators (eliminates C). It lacks peroxidase-binding interfaces characteristic of peroxidase inhibitors (eliminates D). The sequence contains motifs characteristic of the PPCDC/vanillate-decarboxylase superfamily: the 'GDSVLH' segment in the FMN-binding region and the conserved 'LACGDYGNGA' motif, both hallmarks of the PPCDC family (Pfam PF02198) well-studied in yeast (DEC1) and human orthologs. The small size, FMN-binding-like architecture, and these conserved motifs are transferable family-level features recognized across PPCDC homologs. Among the four options, only B (a carboxy-lyase/decarboxylase) is consistent with a small FMN-dependent enzyme bearing these motifs, while the other three require entirely different structural and mechanistic features absent from the sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition of PPCDC sequence signatures (FMN-binding motifs, conserved 'GDSVLH...LACGDYGNGA' pattern, small size) combined with elimination of the three distractors (no ATPase motifs, no channel-regulatory domains, no peroxidase-inhibitor interface) provides a concrete, transferable inference from general protein-family knowledge learned from other PPCDC/vanillate-decarboxylase homologs. This does not require recalling the specific UniProt record for this exact apple protein."
  },
  "case_id": "GO_molecular_function_0115",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H3",
      "H4",
      "H6",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A498JQK2 is annotated with GO:0004633 (phosphopantothenoylcysteine decarboxylase activity) with IDA evidence code (Inferred by Direct Assay) from PubMed:32761275, an experimental study confirming the catalytic reaction N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2 (EC 4.1.1.36, RHEA:16793). The sequence matches the benchmark exactly (SHA256 confirmed). The expected answer B is directly supported by experimental biochemical evidence."
  },
  "important_caveats": [
    "The GO:0010181 (FMN binding) annotation is IEA:TreeGrafter (computational transfer), not experimental, but it is consistent with the known FMN-dependence of PPCDC family members.",
    "The PPCDC family is related to vanillate/4-hydroxybenzoate decarboxylases; precise sub-family assignment from sequence alone has some uncertainty, but among the four offered choices only a decarboxylase (B) is mechanistically compatible.",
    "The experimental evidence (PubMed:32761275) was published in 2020; the UniProt entry was first public in 2025. The benchmark sequence and annotation are consistent across the historical snapshot checked."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors require structural/mechanistic features (P-loop for ATPase, channel-binding domains for K+ regulator, peroxidase interface for inhibitor) that are clearly absent from the sequence. Only B is consistent with the observed small FMN-decarboxylase architecture and PPCDC-family motifs. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0115",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A498JQK2 is annotated with GO:0004633 (phosphopantothenoylcysteine decarboxylase activity) with IDA evidence code (Inferred by Direct Assay) from PubMed:32761275, an experimental study confirming the catalytic reaction N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2 (EC 4.1.1.36, RHEA:16793). The sequence matches the benchmark exactly (SHA256 confirmed). The expected answer B is directly supported by experimental biochemical evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H3", "H4", "H6", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is ~214 aa, small and compact. It lacks Walker A (GxxxxGK[S/T]) and Walker B motifs required for ATP hydrolysis (eliminates A). It lacks ion-channel regulatory domains or transmembrane segments associated with potassium channel regulators (eliminates C). It lacks peroxidase-binding interfaces characteristic of peroxidase inhibitors (eliminates D). The sequence contains motifs characteristic of the PPCDC/vanillate-decarboxylase superfamily: the 'GDSVLH' segment in the FMN-binding region and the conserved 'LACGDYGNGA' motif, both hallmarks of the PPCDC family (Pfam PF02198) well-studied in yeast (DEC1) and human orthologs. The small size, FMN-binding-like architecture, and these conserved motifs are transferable family-level features recognized across PPCDC homologs. Among the four options, only B (a carboxy-lyase/decarboxylase) is consistent with a small FMN-dependent enzyme bearing these motifs, while the other three require entirely different structural and mechanistic features absent from the sequence.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition of PPCDC sequence signatures (FMN-binding motifs, conserved 'GDSVLH...LACGDYGNGA' pattern, small size) combined with elimination of the three distractors (no ATPase motifs, no channel-regulatory domains, no peroxidase-inhibitor interface) provides a concrete, transferable inference from general protein-family knowledge learned from other PPCDC/vanillate-decarboxylase homologs. This does not require recalling the specific UniProt record for this exact apple protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors require structural/mechanistic features (P-loop for ATPase, channel-binding domains for K+ regulator, peroxidase interface for inhibitor) that are clearly absent from the sequence. Only B is consistent with the observed small FMN-decarboxylase architecture and PPCDC-family motifs. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The GO:0010181 (FMN binding) annotation is IEA:TreeGrafter (computational transfer), not experimental, but it is consistent with the known FMN-dependence of PPCDC family members.",
    "The PPCDC family is related to vanillate/4-hydroxybenzoate decarboxylases; precise sub-family assignment from sequence alone has some uncertainty, but among the four offered choices only a decarboxylase (B) is mechanistically compatible.",
    "The experimental evidence (PubMed:32761275) was published in 2020; the UniProt entry was first public in 2025. The benchmark sequence and annotation are consistent across the historical snapshot checked."
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
  "benchmark_sequence_length": 214,
  "benchmark_sequence_sha256": "911d51c767ea28d1df72f610e8076aa0e869282e6e5b17fa85fd72483eb8d447",
  "current_entry_audit": {
    "entryVersion": 20,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 214,
  "current_source_sequence_sha256": "911d51c767ea28d1df72f610e8076aa0e869282e6e5b17fa85fd72483eb8d447",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A498JQK2",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "selected_historical_source_sequence_length": 214,
  "selected_historical_source_sequence_sha256": "911d51c767ea28d1df72f610e8076aa0e869282e6e5b17fa85fd72483eb8d447",
  "selected_historical_version": {
    "accession": "A0A498JQK2",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "HAL3_MALDO",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A498JQK2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":20,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Apple\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"rosids\",\"fabids\",\"Rosales\",\"Rosaceae\",\"Amygdaloideae\",\"Maleae\",\"Malus\"],\"scientificName\":\"Malus domestica\",\"synonyms\":[\"Pyrus malus\"],\"taxonId\":3750}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"value\":\"Halotolerance protein 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"value\":\"MdHAL3\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"value\":\"4.1.1.36\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Phosphopantothenoylcysteine decarboxylase HAL3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"value\":\"PPCDC\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"value\":\"Involved in plant growth, and promotes salt and osmotic tolerance, probably via coenzyme A (CoA) accumulation and endogenous proline accumulation (PubMed:32761275). Catalyzes the decarboxylation of 4'-phosphopantothenoylcysteine to 4'-phosphopantetheine, a key step in coenzyme A biosynthesis (PubMed:32761275). Required for roots development (PubMed:32761275)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:16794\"}}],\"reaction\":{\"ecNumber\":\"4.1.1.36\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"name\":\"N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:16793\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59458\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:61723\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0010181\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:FMN binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"id\":\"GO:0004633\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:phosphopantothenoylcysteine decarboxylase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A498JQK2.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang S.\",\"Zhang F.\",\"Wang Y.\",\"Xue H.\",\"Jiang Q.\",\"Shi J.\",\"Dai H.\",\"Zhang Z.\",\"Li L.\",\"He P.\",\"Li Y.\",\"Ma Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32761275\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00299-020-02576-2\"}],\"citationType\":\"journal article\",\"firstPage\":\"1479\",\"id\":\"32761275\",\"journal\":\"Plant Cell Rep.\",\"lastPage\":\"1491\",\"publicationDate\":\"2020\",\"title\":\"MdHAL3, a 4'-phosphopantothenoylcysteine decarboxylase, is involved in the salt tolerance of autotetraploid apple.\",\"volume\":\"39\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. GL-3\"},{\"type\":\"STRAIN\",\"value\":\"cv. Hanfu\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"INDUCTION BY SALT STRESS\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:46.295142+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2c9613d7efc5e321099105e7df8e04bdd2092654fa07c37207bdc79f66b8d3b2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A498JQK2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   HAL3_MALDO              Reviewed;         214 AA.\nAC   A0A498JQK2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=Phosphopantothenoylcysteine decarboxylase HAL3 {ECO:0000305};\nDE            Short=PPCDC {ECO:0000303|PubMed:32761275};\nDE            EC=4.1.1.36 {ECO:0000269|PubMed:32761275};\nDE   AltName: Full=Halotolerance protein 3 {ECO:0000303|PubMed:32761275};\nDE            Short=MdHAL3 {ECO:0000303|PubMed:32761275};\nGN   Name=HAL3 {ECO:0000303|PubMed:32761275};\nGN   ORFNames=DVH24_008624 {ECO:0000312|EMBL:RXH96124.1};\nOS   Malus domestica (Apple) (Pyrus malus).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   rosids; fabids; Rosales; Rosaceae; Amygdaloideae; Maleae; Malus.\nOX   NCBI_TaxID=3750;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, DISRUPTION PHENOTYPE, CATALYTIC ACTIVITY, TISSUE SPECIFICITY,\nRP   INDUCTION BY SALT STRESS, AND SUBCELLULAR LOCATION.\nRC   STRAIN=cv. GL-3, and cv. Hanfu;\nRX   PubMed=32761275; DOI=10.1007/s00299-020-02576-2;\nRA   Yang S., Zhang F., Wang Y., Xue H., Jiang Q., Shi J., Dai H., Zhang Z.,\nRA   Li L., He P., Li Y., Ma Y.;\nRT   \"MdHAL3, a 4'-phosphopantothenoylcysteine decarboxylase, is involved in the\nRT   salt tolerance of autotetraploid apple.\";\nRL   Plant Cell Rep. 39:1479-1491(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Involved in plant growth, and promotes salt and osmotic\nCC       tolerance, probably via coenzyme A (CoA) accumulation and endogenous\nCC       proline accumulation (PubMed:32761275). Catalyzes the decarboxylation\nCC       of 4'-phosphopantothenoylcysteine to 4'-phosphopantetheine, a key step\nCC       in coenzyme A biosynthesis (PubMed:32761275). Required for roots\nCC       development (PubMed:32761275). {ECO:0000269|PubMed:32761275}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-43",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-\nCC         phosphopantetheine + CO2; Xref=Rhea:RHEA:16793, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:16526, ChEBI:CHEBI:59458, ChEBI:CHEBI:61723; EC=4.1.1.36;\nCC         Evidence={ECO:0000269|PubMed:32761275};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:16794;\nCC         Evidence={ECO:0000269|PubMed:32761275};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0010181; F:FMN binding; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 84-84",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0004633; F:phosphopantothenoylcysteine decarboxylase activity; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 85-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0d82d450cb21391ae574aa004d536baec6b477d61421e803b284844ec1434bbd",
  "url": "https://rest.uniprot.org/unisave/A0A498JQK2?format=txt&versions=19"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004633\nname: phosphopantothenoylcysteine decarboxylase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: N-[(R)-4-phosphonatopantothenoyl]-L-cysteinate + H+ = CO2 + pantetheine 4'-phosphate.\" [EC:4.1.1.36, RHEA:16793]\nsynonym: \"4-phosphopantothenoyl-L-cysteine decarboxylase activity\" RELATED [EC:4.1.1.36]\nsynonym: \"4-phosphopantotheoylcysteine decarboxylase activity\" RELATED [EC:4.1.1.36]\nsynonym: \"N-((R)-4'-phosphopantothenoyl)-L-cysteine carboxy-lyase activity\" RELATED [EC:4.1.1.36]\nsynonym: \"N-[(R)-4'-phosphopantothenoyl]-L-cysteine carboxy-lyase (pantotheine-4'-phosphate-forming)\" RELATED [EC:4.1.1.36]\nsynonym: \"N-[(R)-4'-phosphopantothenoyl]-L-cysteine carboxy-lyase activity\" RELATED [EC:4.1.1.36]\nsynonym: \"PPC-decarboxylase activity\" RELATED [EC:4.1.1.36]\nxref: EC:4.1.1.36\nxref: KEGG_REACTION:R03269\nxref: MetaCyc:P-PANTOCYSDECARB-RXN\nxref: Reactome:R-HSA-196840 \"3xPPCDC:3FMN decarboxylates PPC\"\nxref: RHEA:16793\nis_a: GO:0016831 ! carboxy-lyase activity\nproperty_value: skos:exactMatch EC:4.1.1.36\nproperty_value: skos:exactMatch RHEA:16793\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004633",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 45927-45946",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0015459\nname: potassium channel regulator activity\nnamespace: molecular_function\ndef: \"Binds to and modulates the activity of a potassium channel.\" [GOC:dos, GOC:mah]\nsynonym: \"potassium channel gating activity\" EXACT []\nis_a: GO:0099106 ! ion channel regulator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0015459",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 117999-118006",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0016887\nname: ATP hydrolysis activity\nnamespace: molecular_function\nalt_id: GO:0004002\nalt_id: GO:0042623\ndef: \"Catalysis of the reaction: ATP + H2O = ADP + H+ phosphate. ATP hydrolysis is used in some reactions as an energy source, for example to catalyze a reaction or drive transport against a concentration gradient.\" [RHEA:13065]\ncomment: Note that this term is meant to specifically represent the ATPase activity of proteins using ATP as a source of energy to drive a reaction. If possible, gene products should also be annotated to a child of 'ATP-dependent activity ; GO:0140657', to capture their overall function.\nsynonym: \"adenosine 5'-triphosphatase activity\" EXACT []\nsynonym: \"adenosine triphosphatase activity\" EXACT []\nsynonym: \"adenosinetriphosphatase activity\" EXACT []\nsynonym: \"ATP hydrolase activity\" EXACT []\nsynonym: \"ATP monophosphatase activity\" RELATED []\nsynonym: \"ATP phosphohydrolase activity\" EXACT []\nxref: Reactome:R-HSA-159101 \"NXF1:NXT1 (TAP:p15) binds capped mRNA:CBC:EJC:TREX (minus DDX39B)\"\nxref: Reactome:R-HSA-3371422 \"ATP hydrolysis by HSP70\"\nxref: Reactome:R-HSA-416985 \"Trafficking of GluR2-containing AMPA receptors to synapse\"\nxref: Reactome:R-HSA-5618093 \"ATP hydrolysis by HSP90\"\nxref: Reactome:R-HSA-5654989 \"SPRTN:VCP-mediated release of POLH from monoUb:K164-PCNA\"\nxref: Reactome:R-HSA-5694425 \"NSF ATPase activity dissociates cis-SNARE\"\nxref: Reactome:R-HSA-6809015 \"NSF ATPase activity dissociates cis-SNARE at cis-Golgi\"\nxref: Reactome:R-HSA-6811422 \"NSF ATPase activity dissociates cis-SNARE at the ER\"\nxref: Reactome:R-HSA-6814670 \"ATP hydrolysis by RHOBTB3 promotes PLIN3 dissociation\"\nxref: Reactome:R-HSA-6814678 \"ATP hydrolysis by NSF disassembles the cis-SNARE at the TGN\"\nxref: Reactome:R-HSA-6814683 \"NSF-dependent ATP hydrolysis disassembles the cis-SNARE at the TGN\"\nxref: Reactome:R-HSA-8847638 \"ATP hydrolysis by NSF disassembles the cis-SNARE at the Golgi membrane\"\nxref: Reactome:R-HSA-8868658 \"HSPA8-mediated ATP hydrolysis promotes vesicle uncoating\"\nxref: Reactome:R-HSA-8939203 \"HSP90-dependent ATP hydrolysis promotes release of ESR:ESTG from chaperone complex\"\nxref: Reactome:R-HSA-9038161 \"Progesterone stimulation promotes PGR:P4 binding to ESR1:ESTG\"\nxref: Reactome:R-HSA-917693 \"ESCRT Disassembly\"\nxref: Reactome:R-HSA-9609860 \"Tail-anchored protein:SGTA:BAG6:GET4:UBL4A:ASNA1:ATP dissociates and ASNA1 hydrolyzes ATP yielding Tail-anchored protein:ASNA1:ADP\"\nxref: Reactome:R-HSA-9668415 \"VPS4 mediates disassembly of ESCRTIII subunits to promote sealing of holes in the nuclear envelope\"\nxref: Reactome:R-HSA-9706399 \"RHOBTB3 hydrolyzes ATP\"\nxref: Reactome:R-HSA-9749350 \"ATP-dependent release of CDT1 from the OCCM complex\"\nxref: Reactome:R-HSA-9948300 \"RQT complex:K63polyUb-80S ribosome dissociates yielding K63polyUb-40S subunit and 60S subunit:peptidyl-tRNA with nascent peptide\"\nxref: Reactome:R-HSA-9949632 \"VCP hexamer extracts K48 polyubiquitinated alanine-tailed nascent peptide from VCP hexamer:UFD1:NPLOC4:LTN1:NEMF:TCF25:60S ribosome subunit:K48polyUb-nascent peptide\"\nxref: Reactome:R-HSA-9955731 \"ABCE1:PELO:80S Ribosome:non-stop mRNA:peptidyl-tRNA with elongating peptide dissociates yielding ABCE1:40S ribosomal subunit, PELO, and 60S ribosomal subunit:peptidyl-tRNA with nascent peptide\"\nxref: RHEA:13065\nis_a: GO:0017111 ! ribonucleoside triphosphate phosphatase activity\nrelationship: part_of GO:0140657 ! ATP-dependent activity\nproperty_value: skos:exactMatch RHEA:13065\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016887",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 131251-131292",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0036479\nname: peroxidase inhibitor activity\nnamespace: molecular_function\ndef: \"Binds to and stops, prevents or reduces the activity of peroxidase.\" [GOC:bf, GOC:PARL]\ncomment: GO:0036479 is reserved for cases when the inhibitor directly interacts with the peroxidase. When inhibition of peroxidase activity is achieved without enzyme binding, or when the mechanism of regulation is unknown, instead annotate to 'negative regulation of peroxidase activity ; GO:2000469'.\nis_a: GO:0004857 ! enzyme inhibitor activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0036479",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 228099-228106",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 115. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
