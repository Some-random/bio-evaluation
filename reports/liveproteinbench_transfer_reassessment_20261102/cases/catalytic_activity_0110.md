# catalytic_activity_0110

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0110.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MADTAITVDGAEKRYGDKKALDGLDLRVARGTVHGVLGPNGAGKTTLVRVLSTLLRPDAGRIEVSGHDVVREAYAVRLRIGLLGQHAALDEELGGRQNLELFGRLHHLGARRARARADELLERFDLADTGRKTVRQYSGGMRRRLDLAASLITEPEVLFLDEPTTGLDPRGRAEVWDSVRSLVGGGTTVLLTTQYLEEADQLADRISVVDAGRVIAEGTADELKAETGGDRIDVVLREAGQLGAAVALLPLTGVTVDTDRRLLSAPVTDRMEALSGVVRALQEAGIEAEDVALRRPTLDEVFLHLTGDDRRVKEAA

[Multiple Choices]
A. pyrrolizixenacetamide + H2O = 3-amino-5,6,7,7a-tetrahydro-1H-pyrrolizin-1-one + acetate + H(+)
B. cyclo(N(8)-(alpha,alpha-dimethylallyl)-L-Trp-6a-(alpha,alpha-dimethylallyl)-L-Trp) + AH2 + O2 = okaramine C + A + H2O
C. daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)
D. cytidine(34) in elongator tRNA(Met) + acetyl-CoA + ATP + H2O = N(4)-acetylcytidine(34) in elongator tRNA(Met) + ADP + phosphate + CoA + H(+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The sequence-matched historical UniProt record annotates the daunorubicin/ATP transport reaction as EC 7.6.2.2 and links it to a study of daunorubicin efflux. This supports choice C as a curated functional annotation, though the excerpt alone does not establish that the exact reaction was independently demonstrated in a purified-enzyme assay.

Citations as saved: [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a Walker-A-like P-loop motif (GPNGAGKT) in a compact ATPase-sized protein, consistent with an ATP-driven transporter component. That makes the ATP-coupled transport reaction in C a meaningful fit. D also uses ATP, but requires a tRNA acetylation enzyme; the sequence gives no comparably strong indication of that RNA-modifying function, and the compact transporter-like ATPase pattern favors C. The motif does not by itself reveal daunorubicin specificity, so this is a probabilistic family/function inference rather than proof of the substrate.


**Missing item-specific fact**

> Exact daunorubicin substrate specificity is not established by the sequence motif alone, but is not necessary for a meaningful distinction among these choices.


**Reason**

> A transferable P-loop ATPase/transport inference distinguishes C from the chemically unrelated reactions and makes it more plausible than the other ATP-using option D. The choice does not require recalling this protein's exact database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative is comparably supported by the sequence-level ATPase and transporter inference; uncertainty about the exact transported substrate does not make another offered reaction equally defensible.


### Important caveats

- The reviewer-only annotation and sequence match support the key but were not inputs to the evaluated model.
- The cited evidence is a curated annotation linked to a study of efflux; the supplied excerpts do not independently detail the biochemical assay.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a Walker-A-like P-loop motif (GPNGAGKT) in a compact ATPase-sized protein, consistent with an ATP-driven transporter component. That makes the ATP-coupled transport reaction in C a meaningful fit. D also uses ATP, but requires a tRNA acetylation enzyme; the sequence gives no comparably strong indication of that RNA-modifying function, and the compact transporter-like ATPase pattern favors C. The motif does not by itself reveal daunorubicin specificity, so this is a probabilistic family/function inference rather than proof of the substrate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Exact daunorubicin substrate specificity is not established by the sequence motif alone, but is not necessary for a meaningful distinction among these choices.",
    "reason": "A transferable P-loop ATPase/transport inference distinguishes C from the chemically unrelated reactions and makes it more plausible than the other ATP-using option D. The choice does not require recalling this protein's exact database record."
  },
  "case_id": "catalytic_activity_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates the daunorubicin/ATP transport reaction as EC 7.6.2.2 and links it to a study of daunorubicin efflux. This supports choice C as a curated functional annotation, though the excerpt alone does not establish that the exact reaction was independently demonstrated in a purified-enzyme assay."
  },
  "important_caveats": [
    "The reviewer-only annotation and sequence match support the key but were not inputs to the evaluated model.",
    "The cited evidence is a curated annotation linked to a study of efflux; the supplied excerpts do not independently detail the biochemical assay."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the sequence-level ATPase and transporter inference; uncertainty about the exact transported substrate does not make another offered reaction equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched historical UniProt record annotates the daunorubicin/ATP transport reaction as EC 7.6.2.2 and links it to a study of daunorubicin efflux. This supports choice C as a curated functional annotation, though the excerpt alone does not establish that the exact reaction was independently demonstrated in a purified-enzyme assay.",
    "evidence_ids": ["H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a Walker-A-like P-loop motif (GPNGAGKT) in a compact ATPase-sized protein, consistent with an ATP-driven transporter component. That makes the ATP-coupled transport reaction in C a meaningful fit. D also uses ATP, but requires a tRNA acetylation enzyme; the sequence gives no comparably strong indication of that RNA-modifying function, and the compact transporter-like ATPase pattern favors C. The motif does not by itself reveal daunorubicin specificity, so this is a probabilistic family/function inference rather than proof of the substrate.",
    "missing_item_specific_fact": "Exact daunorubicin substrate specificity is not established by the sequence motif alone, but is not necessary for a meaningful distinction among these choices.",
    "reason": "A transferable P-loop ATPase/transport inference distinguishes C from the chemically unrelated reactions and makes it more plausible than the other ATP-using option D. The choice does not require recalling this protein's exact database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative is comparably supported by the sequence-level ATPase and transporter inference; uncertainty about the exact transported substrate does not make another offered reaction equally defensible."
  },
  "important_caveats": [
    "The reviewer-only annotation and sequence match support the key but were not inputs to the evaluated model.",
    "The cited evidence is a curated annotation linked to a study of efflux; the supplied excerpts do not independently detail the biochemical assay."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry P0DXU7 (DrrA3, Streptomyces coeruleorubidus, 316 AA, sequence matched) annotates the protein as EC 7.6.2.2 with catalytic activity 'daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)', exactly matching choice C. Evidence code ECO:0000305 (inferred from sequence/structural similarity) with supporting PubMed:39375957 on ABC transporter involvement in daunorubicin efflux. The annotation is computational inference supported by experimental functional data on related transporters, which is a standard and acceptable basis for EC assignment.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical Walker A (P-loop) motif 'GNGAGKTTL' (residues ~38-46), a textbook diagnostic feature of P-loop NTPases, and specifically of ABC transporter nucleotide-binding domains (NBDs). The Walker B 'DE' motif is present in 'LDEPTTGLDPRG'. The overall domain length (~316 AA) and architecture are consistent with a single NBD. Among the four choices, only C describes an ATP-dependent translocation reaction catalyzed by an ABC transporter. Choice A is a hydrolase (no ATP, no Walker A). Choice B is a monooxygenase/P450 (uses O2, no Walker A). Choice D is a GNAT-fold acetyltransferase coupled to ATP hydrolysis, but GNAT enzymes lack Walker A motifs. Recognizing the Walker A motif and ABC-transporter domain architecture from general protein-family knowledge is sufficient to eliminate A, B, and D and select C. The specific substrate (daunorubicin) is not predictable from sequence, but the reaction class (ATP-dependent efflux by an ABC transporter) is uniquely identified by the motif and is the only option matching that class.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Walker A motif is one of the most universally recognized sequence features in biochemistry, taught in any structural biology or enzymology course. A model trained on general protein knowledge can identify this as an ABC transporter NBD and match it to the only ABC-transporter reaction among the choices. No target-specific database lookup is needed to distinguish the four alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent fundamentally different enzyme classes (hydrolase, monooxygenase, ABC transporter, acetyltransferase). The Walker A motif unambiguously identifies the protein as a P-loop NTPase, and the domain architecture points to an ABC transporter. Only C fits. No other option is defensible given the sequence features.


### Important caveats

- The specific substrate daunorubicin is not predictable from sequence alone; however, the question only requires identifying the reaction class, and the choices are structured to make that sufficient.
- The UniProt annotation uses ECO:0000305 (sequence-similarity inference), not direct experimental kinetics on this exact protein, but the PubMed reference (39375957) provides experimental functional evidence for daunorubicin efflux by this transporter family in S. coeruleorubidus.
- The entry was first published in February 2025; the benchmark's construction date relative to this is unknown, but the sequence match is exact.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical Walker A (P-loop) motif 'GNGAGKTTL' (residues ~38-46), a textbook diagnostic feature of P-loop NTPases, and specifically of ABC transporter nucleotide-binding domains (NBDs). The Walker B 'DE' motif is present in 'LDEPTTGLDPRG'. The overall domain length (~316 AA) and architecture are consistent with a single NBD. Among the four choices, only C describes an ATP-dependent translocation reaction catalyzed by an ABC transporter. Choice A is a hydrolase (no ATP, no Walker A). Choice B is a monooxygenase/P450 (uses O2, no Walker A). Choice D is a GNAT-fold acetyltransferase coupled to ATP hydrolysis, but GNAT enzymes lack Walker A motifs. Recognizing the Walker A motif and ABC-transporter domain architecture from general protein-family knowledge is sufficient to eliminate A, B, and D and select C. The specific substrate (daunorubicin) is not predictable from sequence, but the reaction class (ATP-dependent efflux by an ABC transporter) is uniquely identified by the motif and is the only option matching that class.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Walker A motif is one of the most universally recognized sequence features in biochemistry, taught in any structural biology or enzymology course. A model trained on general protein knowledge can identify this as an ABC transporter NBD and match it to the only ABC-transporter reaction among the choices. No target-specific database lookup is needed to distinguish the four alternatives."
  },
  "case_id": "catalytic_activity_0110",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry P0DXU7 (DrrA3, Streptomyces coeruleorubidus, 316 AA, sequence matched) annotates the protein as EC 7.6.2.2 with catalytic activity 'daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)', exactly matching choice C. Evidence code ECO:0000305 (inferred from sequence/structural similarity) with supporting PubMed:39375957 on ABC transporter involvement in daunorubicin efflux. The annotation is computational inference supported by experimental functional data on related transporters, which is a standard and acceptable basis for EC assignment."
  },
  "important_caveats": [
    "The specific substrate daunorubicin is not predictable from sequence alone; however, the question only requires identifying the reaction class, and the choices are structured to make that sufficient.",
    "The UniProt annotation uses ECO:0000305 (sequence-similarity inference), not direct experimental kinetics on this exact protein, but the PubMed reference (39375957) provides experimental functional evidence for daunorubicin efflux by this transporter family in S. coeruleorubidus.",
    "The entry was first published in February 2025; the benchmark's construction date relative to this is unknown, but the sequence match is exact."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes (hydrolase, monooxygenase, ABC transporter, acetyltransferase). The Walker A motif unambiguously identifies the protein as a P-loop NTPase, and the domain architecture points to an ABC transporter. Only C fits. No other option is defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0110",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry P0DXU7 (DrrA3, Streptomyces coeruleorubidus, 316 AA, sequence matched) annotates the protein as EC 7.6.2.2 with catalytic activity 'daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)', exactly matching choice C. Evidence code ECO:0000305 (inferred from sequence/structural similarity) with supporting PubMed:39375957 on ABC transporter involvement in daunorubicin efflux. The annotation is computational inference supported by experimental functional data on related transporters, which is a standard and acceptable basis for EC assignment.",
    "evidence_ids": ["C1", "C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical Walker A (P-loop) motif 'GNGAGKTTL' (residues ~38-46), a textbook diagnostic feature of P-loop NTPases, and specifically of ABC transporter nucleotide-binding domains (NBDs). The Walker B 'DE' motif is present in 'LDEPTTGLDPRG'. The overall domain length (~316 AA) and architecture are consistent with a single NBD. Among the four choices, only C describes an ATP-dependent translocation reaction catalyzed by an ABC transporter. Choice A is a hydrolase (no ATP, no Walker A). Choice B is a monooxygenase/P450 (uses O2, no Walker A). Choice D is a GNAT-fold acetyltransferase coupled to ATP hydrolysis, but GNAT enzymes lack Walker A motifs. Recognizing the Walker A motif and ABC-transporter domain architecture from general protein-family knowledge is sufficient to eliminate A, B, and D and select C. The specific substrate (daunorubicin) is not predictable from sequence, but the reaction class (ATP-dependent efflux by an ABC transporter) is uniquely identified by the motif and is the only option matching that class.",
    "missing_item_specific_fact": "",
    "reason": "The Walker A motif is one of the most universally recognized sequence features in biochemistry, taught in any structural biology or enzymology course. A model trained on general protein knowledge can identify this as an ABC transporter NBD and match it to the only ABC-transporter reaction among the choices. No target-specific database lookup is needed to distinguish the four alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent fundamentally different enzyme classes (hydrolase, monooxygenase, ABC transporter, acetyltransferase). The Walker A motif unambiguously identifies the protein as a P-loop NTPase, and the domain architecture points to an ABC transporter. Only C fits. No other option is defensible given the sequence features."
  },
  "important_caveats": [
    "The specific substrate daunorubicin is not predictable from sequence alone; however, the question only requires identifying the reaction class, and the choices are structured to make that sufficient.",
    "The UniProt annotation uses ECO:0000305 (sequence-similarity inference), not direct experimental kinetics on this exact protein, but the PubMed reference (39375957) provides experimental functional evidence for daunorubicin efflux by this transporter family in S. coeruleorubidus.",
    "The entry was first published in February 2025; the benchmark's construction date relative to this is unknown, but the sequence match is exact."
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
  "benchmark_sequence_length": 316,
  "benchmark_sequence_sha256": "bfff69d1d7d031108e1c50bbb606696118d87057cab6e04b802323f2c0487534",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 316,
  "current_source_sequence_sha256": "bfff69d1d7d031108e1c50bbb606696118d87057cab6e04b802323f2c0487534",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXU7",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9",
  "selected_historical_source_sequence_length": 316,
  "selected_historical_source_sequence_sha256": "bfff69d1d7d031108e1c50bbb606696118d87057cab6e04b802323f2c0487534",
  "selected_historical_version": {
    "accession": "P0DXU7",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DRRA3_STRC4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXU7\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:39.757107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU7.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:39.757107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU7.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces coeruleorubidus\",\"taxonId\":116188}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:39.757107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU7.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"value\":\"7.6.2.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Daunorubicin resistance ATP-binding protein DrrA3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:39.757107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU7.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:33148\"}}],\"reaction\":{\"ecNumber\":\"7.6.2.2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"name\":\"daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:33147\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64677\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:39.757107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU7.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU7.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Dong J.\",\"Ning J.\",\"Tian Y.\",\"Li H.\",\"Chen H.\",\"Guan W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39375957\"},{\"database\":\"DOI\",\"id\":\"10.1111/1751-7915.70023\"}],\"citationType\":\"journal article\",\"firstPage\":\"e70023\",\"id\":\"39375957\",\"journal\":\"Microb. Biotechnol.\",\"lastPage\":\"e70023\",\"publicationDate\":\"2024\",\"title\":\"The involvement of multiple ABC transporters in daunorubicin efflux in Streptomyces coeruleorubidus.\",\"volume\":\"17\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION IN DAUNORUBICIN EFFLUX\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:39.757107+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e4ecbe95569eb6174ea1ce5042f5eb78567e393cf608a2fde3f152bb86370540",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU7.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   DRRA3_STRC4             Reviewed;         316 AA.\nAC   P0DXU7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA3 {ECO:0000305};\nDE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};\nGN   Name=drrA3 {ECO:0000303|PubMed:39375957};\nGN   ORFNames=R5U08_20725 {ECO:0000312|EMBL:WOT36399.1};\nOS   Streptomyces coeruleorubidus.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=116188;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:44.049376+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9",
  "url": "https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA3 {ECO:0000305};\nDE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:44.049376+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9",
  "url": "https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39375957; DOI=10.1111/1751-7915.70023;\nRA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;\nRT   \"The involvement of multiple ABC transporters in daunorubicin efflux in\nRT   Streptomyces coeruleorubidus.\";\nRL   Microb. Biotechnol. 17:e70023-e70023(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:44.049376+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9",
  "url": "https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP +\nCC         phosphate + H(+); Xref=Rhea:RHEA:33147, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:30616, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:64677, ChEBI:CHEBI:456216; EC=7.6.2.2;\nCC         Evidence={ECO:0000305|PubMed:39375957};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33148;\nCC         Evidence={ECO:0000305|PubMed:39375957};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:44.049376+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "42d20297633a41a19682385e9a7ca80ef7478fe940d29e171258f49592f4cbc9",
  "url": "https://rest.uniprot.org/unisave/P0DXU7?format=txt&versions=4"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 110. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
