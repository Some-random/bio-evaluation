# catalytic_activity_0118

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0118.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDGYAVRAEAMEKRYGEKRALDGFDLAVGEGTVHGLLGPNGAGKTTAVRILSTLVRLDGGRATVAGLDVARQPREVRARIGLTGQYAAVDEVLTGRQNLEMFGRLFHLGGRRARLRATELLEQFDLTDAGDRGVGKYSGGMRRRLDLAASMILAPAVLFLDEPTTGLDPRSRGEVWESVRALVAGGTTVLLTTQYLEEADKLASRITVIDQGRAIADDTPDGLKNLVGGDRIEVVVAERAEIPRVVKVVARVADGEPEADETESRVHAPVTDRVTALTEVARTLQDEGVRVEDIGLRRPSLDDVFLRLTGHRTENTEAKEAA

[Multiple Choices]
A. daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)
B. apo-[ACP] + CoA = holo-[ACP] + adenosine 3',5'-bisphosphate + H(+)
C. 2-oxospirilloxanthin + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2'-hydroxy-2-oxospirilloxanthin + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
D. guanosine in U6 snRNA + S-adenosyl-L-methionine = N(2)-methylguanosine in U6 snRNA + S-adenosyl-L-homocysteine + H(+)
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

> The sequence-matched UniProt record assigns this protein the daunorubicin-resistance ATP-binding protein function and explicitly annotates the reaction in choice A. The annotation cites a study on daunorubicin efflux, although the supplied excerpts do not independently establish the experimental details of the catalytic assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a P-loop/Walker A-like ATP-binding motif (GPNGAGKTT) in a roughly 322-residue ATPase-like protein. Transferable knowledge of ABC transporter ATPases supports ATP-driven transport, which matches choice A; the other choices describe ACP modification, carotenoid hydroxylation, or RNA methylation and are not the corresponding ATP-driven transport reaction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and choices support distinguishing the transport reaction from the unrelated enzyme reactions without recalling this exact protein's database entry. The sequence alone does not establish daunorubicin as the transported substrate, so the exact substrate assignment is less directly inferable than the choice-level distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only choice A describes ATP-driven transport; the other choices describe different reaction types.


### Important caveats

- The supplied annotation supports the key, but the excerpts are not an independent review of the cited primary study.
- Transferable sequence-level inference supports a transporter ATPase, not the exact daunorubicin specificity by itself.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a P-loop/Walker A-like ATP-binding motif (GPNGAGKTT) in a roughly 322-residue ATPase-like protein. Transferable knowledge of ABC transporter ATPases supports ATP-driven transport, which matches choice A; the other choices describe ACP modification, carotenoid hydroxylation, or RNA methylation and are not the corresponding ATP-driven transport reaction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices support distinguishing the transport reaction from the unrelated enzyme reactions without recalling this exact protein's database entry. The sequence alone does not establish daunorubicin as the transported substrate, so the exact substrate assignment is less directly inferable than the choice-level distinction."
  },
  "case_id": "catalytic_activity_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein the daunorubicin-resistance ATP-binding protein function and explicitly annotates the reaction in choice A. The annotation cites a study on daunorubicin efflux, although the supplied excerpts do not independently establish the experimental details of the catalytic assignment."
  },
  "important_caveats": [
    "The supplied annotation supports the key, but the excerpts are not an independent review of the cited primary study.",
    "Transferable sequence-level inference supports a transporter ATPase, not the exact daunorubicin specificity by itself."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice A describes ATP-driven transport; the other choices describe different reaction types."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns this protein the daunorubicin-resistance ATP-binding protein function and explicitly annotates the reaction in choice A. The annotation cites a study on daunorubicin efflux, although the supplied excerpts do not independently establish the experimental details of the catalytic assignment.",
    "evidence_ids": ["C4", "C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a P-loop/Walker A-like ATP-binding motif (GPNGAGKTT) in a roughly 322-residue ATPase-like protein. Transferable knowledge of ABC transporter ATPases supports ATP-driven transport, which matches choice A; the other choices describe ACP modification, carotenoid hydroxylation, or RNA methylation and are not the corresponding ATP-driven transport reaction.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices support distinguishing the transport reaction from the unrelated enzyme reactions without recalling this exact protein's database entry. The sequence alone does not establish daunorubicin as the transported substrate, so the exact substrate assignment is less directly inferable than the choice-level distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only choice A describes ATP-driven transport; the other choices describe different reaction types."
  },
  "important_caveats": [
    "The supplied annotation supports the key, but the excerpts are not an independent review of the cited primary study.",
    "Transferable sequence-level inference supports a transporter ATPase, not the exact daunorubicin specificity by itself."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXU5 explicitly annotates the catalytic activity as 'daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)' (EC 7.6.2.2), matching Choice A verbatim. The evidence code ECO:0000305 indicates inference by similarity to other proteins, supported by reference to PubMed:39375957 (Dong et al. 2024, Microb. Biotechnol.). The sequence matches (322 AA, identical SHA256). The annotation is a database-confirmed entry, though the evidence code notes it is inferred rather than directly experimentally characterized for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical Walker A motif (P-loop): 'GEGTVHGLLGPNGAGKTT' (residues ~17-32), where 'GPNGAGKTT' is the classic GxxGxGKS/T signature of ABC transporter nucleotide-binding domains (NBDs). Additionally, the 'DEPTT' motif in the downstream region is characteristic of the ABC transporter signature domain. ABC transporters are a large, well-characterized superfamily whose defining biochemical reaction is ATP hydrolysis-driven translocation of substrates across membranes. Among the four options, only Choice A describes an ATP-hydrolysis-driven transport reaction (daunorubicin efflux via ABC transporter). Choice B (ACP synthetase) is a CoA-transfer reaction with no ATP-driven transport. Choice C is a hydroxylase using O2 and ferredoxin electrons. Choice D is a SAM-dependent methyltransferase. The Walker A motif is one of the most universally recognized sequence features in biology, learned from hundreds of ABC transporter structures and sequences. It immediately classifies this protein as an ABC-type ATPase/NBD, which uniquely matches the reaction stoichiometry in Choice A (ATP + H2O → ADP + Pi + H+ coupled to substrate translocation). The other three options involve entirely different cofactors (CoA, O2/ferredoxin, SAM) and reaction classes incompatible with an ABC transporter fold.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Walker A motif (GPNGAGKTT) is a highly conserved, transferable sequence feature recognized across the entire ABC transporter superfamily. Its presence definitively identifies the protein as an ABC-type ATPase. Since only one of the four offered choices describes an ABC transporter reaction (ATP-driven efflux), the motif alone is sufficient to select Choice A without needing to know the specific substrate. The other three options are mechanistically incompatible with an ABC transporter NBD architecture.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Walker A motif unambiguously identifies an ABC transporter. Only Choice A matches ABC transporter biochemistry (ATP hydrolysis driving substrate translocation). The other options involve fundamentally different enzyme classes and cofactors. No ambiguity exists among the offered choices.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the specific daunorubicin substrate selectivity for this exact protein is inferred rather than directly experimentally demonstrated. However, this does not affect the answerability assessment since the Walker A motif identifies the ABC transporter class, and only one option matches that class.
- Distinguishing daunorubicin from other ABC transporter substrates would require additional knowledge, but this is unnecessary because only one option is an ABC transporter reaction.
- The entry was first public in February 2025; the benchmark author's source snapshot is unknown but the sequence matches the current entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical Walker A motif (P-loop): 'GEGTVHGLLGPNGAGKTT' (residues ~17-32), where 'GPNGAGKTT' is the classic GxxGxGKS/T signature of ABC transporter nucleotide-binding domains (NBDs). Additionally, the 'DEPTT' motif in the downstream region is characteristic of the ABC transporter signature domain. ABC transporters are a large, well-characterized superfamily whose defining biochemical reaction is ATP hydrolysis-driven translocation of substrates across membranes. Among the four options, only Choice A describes an ATP-hydrolysis-driven transport reaction (daunorubicin efflux via ABC transporter). Choice B (ACP synthetase) is a CoA-transfer reaction with no ATP-driven transport. Choice C is a hydroxylase using O2 and ferredoxin electrons. Choice D is a SAM-dependent methyltransferase. The Walker A motif is one of the most universally recognized sequence features in biology, learned from hundreds of ABC transporter structures and sequences. It immediately classifies this protein as an ABC-type ATPase/NBD, which uniquely matches the reaction stoichiometry in Choice A (ATP + H2O → ADP + Pi + H+ coupled to substrate translocation). The other three options involve entirely different cofactors (CoA, O2/ferredoxin, SAM) and reaction classes incompatible with an ABC transporter fold.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Walker A motif (GPNGAGKTT) is a highly conserved, transferable sequence feature recognized across the entire ABC transporter superfamily. Its presence definitively identifies the protein as an ABC-type ATPase. Since only one of the four offered choices describes an ABC transporter reaction (ATP-driven efflux), the motif alone is sufficient to select Choice A without needing to know the specific substrate. The other three options are mechanistically incompatible with an ABC transporter NBD architecture."
  },
  "case_id": "catalytic_activity_0118",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU5 explicitly annotates the catalytic activity as 'daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)' (EC 7.6.2.2), matching Choice A verbatim. The evidence code ECO:0000305 indicates inference by similarity to other proteins, supported by reference to PubMed:39375957 (Dong et al. 2024, Microb. Biotechnol.). The sequence matches (322 AA, identical SHA256). The annotation is a database-confirmed entry, though the evidence code notes it is inferred rather than directly experimentally characterized for this exact protein."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the specific daunorubicin substrate selectivity for this exact protein is inferred rather than directly experimentally demonstrated. However, this does not affect the answerability assessment since the Walker A motif identifies the ABC transporter class, and only one option matches that class.",
    "Distinguishing daunorubicin from other ABC transporter substrates would require additional knowledge, but this is unnecessary because only one option is an ABC transporter reaction.",
    "The entry was first public in February 2025; the benchmark author's source snapshot is unknown but the sequence matches the current entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Walker A motif unambiguously identifies an ABC transporter. Only Choice A matches ABC transporter biochemistry (ATP hydrolysis driving substrate translocation). The other options involve fundamentally different enzyme classes and cofactors. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0118",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU5 explicitly annotates the catalytic activity as 'daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)' (EC 7.6.2.2), matching Choice A verbatim. The evidence code ECO:0000305 indicates inference by similarity to other proteins, supported by reference to PubMed:39375957 (Dong et al. 2024, Microb. Biotechnol.). The sequence matches (322 AA, identical SHA256). The annotation is a database-confirmed entry, though the evidence code notes it is inferred rather than directly experimentally characterized for this exact protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical Walker A motif (P-loop): 'GEGTVHGLLGPNGAGKTT' (residues ~17-32), where 'GPNGAGKTT' is the classic GxxGxGKS/T signature of ABC transporter nucleotide-binding domains (NBDs). Additionally, the 'DEPTT' motif in the downstream region is characteristic of the ABC transporter signature domain. ABC transporters are a large, well-characterized superfamily whose defining biochemical reaction is ATP hydrolysis-driven translocation of substrates across membranes. Among the four options, only Choice A describes an ATP-hydrolysis-driven transport reaction (daunorubicin efflux via ABC transporter). Choice B (ACP synthetase) is a CoA-transfer reaction with no ATP-driven transport. Choice C is a hydroxylase using O2 and ferredoxin electrons. Choice D is a SAM-dependent methyltransferase. The Walker A motif is one of the most universally recognized sequence features in biology, learned from hundreds of ABC transporter structures and sequences. It immediately classifies this protein as an ABC-type ATPase/NBD, which uniquely matches the reaction stoichiometry in Choice A (ATP + H2O → ADP + Pi + H+ coupled to substrate translocation). The other three options involve entirely different cofactors (CoA, O2/ferredoxin, SAM) and reaction classes incompatible with an ABC transporter fold.",
    "missing_item_specific_fact": "",
    "reason": "The Walker A motif (GPNGAGKTT) is a highly conserved, transferable sequence feature recognized across the entire ABC transporter superfamily. Its presence definitively identifies the protein as an ABC-type ATPase. Since only one of the four offered choices describes an ABC transporter reaction (ATP-driven efflux), the motif alone is sufficient to select Choice A without needing to know the specific substrate. The other three options are mechanistically incompatible with an ABC transporter NBD architecture."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Walker A motif unambiguously identifies an ABC transporter. Only Choice A matches ABC transporter biochemistry (ATP hydrolysis driving substrate translocation). The other options involve fundamentally different enzyme classes and cofactors. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred by similarity), meaning the specific daunorubicin substrate selectivity for this exact protein is inferred rather than directly experimentally demonstrated. However, this does not affect the answerability assessment since the Walker A motif identifies the ABC transporter class, and only one option matches that class.",
    "Distinguishing daunorubicin from other ABC transporter substrates would require additional knowledge, but this is unnecessary because only one option is an ABC transporter reaction.",
    "The entry was first public in February 2025; the benchmark author's source snapshot is unknown but the sequence matches the current entry."
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
  "benchmark_sequence_length": 322,
  "benchmark_sequence_sha256": "2ca962384eab52f63840ebe294f20a563ed32fb8966a77e2f1c8c7c091f6e9f3",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 322,
  "current_source_sequence_sha256": "2ca962384eab52f63840ebe294f20a563ed32fb8966a77e2f1c8c7c091f6e9f3",
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
  "requested_accession": "P0DXU5",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425",
  "selected_historical_source_sequence_length": 322,
  "selected_historical_source_sequence_sha256": "2ca962384eab52f63840ebe294f20a563ed32fb8966a77e2f1c8c7c091f6e9f3",
  "selected_historical_version": {
    "accession": "P0DXU5",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DRRA2_STRC4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXU5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:36.968817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:36.968817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces coeruleorubidus\",\"taxonId\":116188}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:36.968817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"value\":\"7.6.2.2\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Daunorubicin resistance ATP-binding protein DrrA2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:36.968817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:33148\"}}],\"reaction\":{\"ecNumber\":\"7.6.2.2\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39375957\",\"source\":\"PubMed\"}],\"name\":\"daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP + phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:33147\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64677\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:36.968817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Dong J.\",\"Ning J.\",\"Tian Y.\",\"Li H.\",\"Chen H.\",\"Guan W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39375957\"},{\"database\":\"DOI\",\"id\":\"10.1111/1751-7915.70023\"}],\"citationType\":\"journal article\",\"firstPage\":\"e70023\",\"id\":\"39375957\",\"journal\":\"Microb. Biotechnol.\",\"lastPage\":\"e70023\",\"publicationDate\":\"2024\",\"title\":\"The involvement of multiple ABC transporters in daunorubicin efflux in Streptomyces coeruleorubidus.\",\"volume\":\"17\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION IN DAUNORUBICIN EFFLUX\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:36.968817+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "baac9668267e84b61df008cf051b563a50e82848a7f38c23d90babada2c0b4f1",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   DRRA2_STRC4             Reviewed;         322 AA.\nAC   P0DXU5;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA2 {ECO:0000305};\nDE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};\nGN   Name=drrA2 {ECO:0000303|PubMed:39375957};\nGN   ORFNames=R5U08_15995 {ECO:0000312|EMBL:WOT35541.1};\nOS   Streptomyces coeruleorubidus.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=116188;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:38.836268+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425",
  "url": "https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Daunorubicin resistance ATP-binding protein DrrA2 {ECO:0000305};\nDE            EC=7.6.2.2 {ECO:0000305|PubMed:39375957};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:38.836268+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425",
  "url": "https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39375957; DOI=10.1111/1751-7915.70023;\nRA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;\nRT   \"The involvement of multiple ABC transporters in daunorubicin efflux in\nRT   Streptomyces coeruleorubidus.\";\nRL   Microb. Biotechnol. 17:e70023-e70023(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:38.836268+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425",
  "url": "https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=daunorubicin(in) + ATP + H2O = daunorubicin(out) + ADP +\nCC         phosphate + H(+); Xref=Rhea:RHEA:33147, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:30616, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:64677, ChEBI:CHEBI:456216; EC=7.6.2.2;\nCC         Evidence={ECO:0000305|PubMed:39375957};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33148;\nCC         Evidence={ECO:0000305|PubMed:39375957};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:38.836268+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f00825c338b58f426a5eb95aec87540f7863679985e8548e4b444a06c4394425",
  "url": "https://rest.uniprot.org/unisave/P0DXU5?format=txt&versions=4"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 118. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
