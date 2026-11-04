# GO_cellular_component_0037

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0037.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **B** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTSSEPASPEIEQQANSAPRRPRILLAASGSVAAIKFGNLCHSFSEWAEVKAVATRASLHFIDRASLPKDVILYTEEDEWSTWNKVGDSVLHIELRSWADILVIAPLSANTLGKIAGGLCDNLLTCIVRAWDYSKPFFVAPAMNTLMWKNPFTEQHIMSIDELGVSLIPPVTKRLACGDYGNGAMAEPSVIYSTVRLFFESRVQQSGNIVQQPV

[Multiple Choices]
A. replisome
B. plasma membrane
C. host cell plasma membrane
D. RQC complex
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Cellular Component Prediction, which is to predict the primary Cellular Component where a protein is located, according to the Gene Ontology (GO) framework. A protein's location within a cell (e.g., Nucleus, Mitochondria, Cytoplasm) is critical for its function and is often determined by specific targeting signals in its amino acid sequence. Based on the provided sequence, you must identify the most likely compartment where the protein resides.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record reports cell membrane localization with experimental evidence and includes an experimental GO annotation to plasma membrane, supporting choice B. The record also reports cytoplasmic localization, so it does not establish that plasma membrane is the protein’s exclusive or primary location.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [H3](#evidence-h3), [H6](#evidence-h6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> This protein’s experimentally reported plasma-membrane localization, which is not established by the supplied sequence.


**Reason**

> The compact sequence is consistent with a soluble enzyme and has no clear membrane-spanning segment or obvious classical targeting signal. Recognizing an enzyme family may support a general expectation of soluble localization, but does not meaningfully predict the reported plasma-membrane localization or distinguish B from the other offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source supports both cell-membrane and cytoplasmic localization, but cytoplasm is not among the choices; none of the other offered options is supported by the supplied evidence.


### Important caveats

- The source reports both membrane and cytoplasmic localization, without ranking them, so the wording “primary” is not resolved by the annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "This protein’s experimentally reported plasma-membrane localization, which is not established by the supplied sequence.",
    "reason": "The compact sequence is consistent with a soluble enzyme and has no clear membrane-spanning segment or obvious classical targeting signal. Recognizing an enzyme family may support a general expectation of soluble localization, but does not meaningfully predict the reported plasma-membrane localization or distinguish B from the other offered choices."
  },
  "case_id": "GO_cellular_component_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "H3",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports cell membrane localization with experimental evidence and includes an experimental GO annotation to plasma membrane, supporting choice B. The record also reports cytoplasmic localization, so it does not establish that plasma membrane is the protein’s exclusive or primary location."
  },
  "important_caveats": [
    "The source reports both membrane and cytoplasmic localization, without ranking them, so the wording “primary” is not resolved by the annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source supports both cell-membrane and cytoplasmic localization, but cytoplasm is not among the choices; none of the other offered options is supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports cell membrane localization with experimental evidence and includes an experimental GO annotation to plasma membrane, supporting choice B. The record also reports cytoplasmic localization, so it does not establish that plasma membrane is the protein’s exclusive or primary location.",
    "evidence_ids": ["C5", "C8", "H3", "H6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "This protein’s experimentally reported plasma-membrane localization, which is not established by the supplied sequence.",
    "reason": "The compact sequence is consistent with a soluble enzyme and has no clear membrane-spanning segment or obvious classical targeting signal. Recognizing an enzyme family may support a general expectation of soluble localization, but does not meaningfully predict the reported plasma-membrane localization or distinguish B from the other offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source supports both cell-membrane and cytoplasmic localization, but cytoplasm is not among the choices; none of the other offered options is supported by the supplied evidence."
  },
  "important_caveats": [
    "The source reports both membrane and cytoplasmic localization, without ranking them, so the wording “primary” is not resolved by the annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A498JQK2) annotates this protein with GO:0005886 (plasma membrane, IDA:UniProtKB, experimental evidence from PubMed:32761275) and also GO:0005737 (cytoplasm, IDA). The subcellular location comment lists 'Cell membrane' (an EXACT synonym for plasma membrane per GO1) and 'Cytoplasm.' The expected answer B (plasma membrane) is directly supported by the experimental annotation. Cytoplasm is also annotated but is not among the offered choices, so B is the best-supported option among those presented.

Citations as saved: [C5](#evidence-c5), [C8](#evidence-c8), [C6](#evidence-c6), [H3](#evidence-h3), [H6](#evidence-h6), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable lines of reasoning distinguish B from the alternatives: (1) Replisome (A) consists of large multi-component enzymatic machines (DNA polymerases, helicases, primases) typically hundreds to thousands of residues with catalytic domains; a 214-aa protein with no recognizable polymerase/helicase/primase motifs is inconsistent. (2) RQC complex (D) comprises specific proteins (Cdc48p, Rkr1p, Tae2p, Rqc1p, Npl4p, Ufd1p) with AAA+ ATPase, E3 ligase, or ribosome-binding domains absent here. (3) 'Host cell plasma membrane' (C, GO:0020002) is a GO term specifically defined for viral proteins localizing to the host membrane (goslim_virus subset); the sequence lacks viral structural motifs (capsid, polymerase, envelope proteins) and resembles a small metabolic enzyme, making C inappropriate. (4) Family-level knowledge: the sequence matches the HAL3/PPCDC family; in Saccharomyces cerevisiae, HAL3 (also 214 aa) is a well-characterized plasma membrane-associated protein involved in salt tolerance, a property transferable to homologs. The combination of elimination (A, D clearly wrong; C requires viral context absent here) and positive family inference (HAL3 membrane association in yeast) supports B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination of A and D relies on well-known structural/functional constraints of replisome and RQC components. The B-vs-C distinction relies on GO term semantics (host cell = viral context) and the absence of viral features. The positive support for membrane localization draws on the well-established yeast HAL3 homolog being a plasma membrane protein, which is legitimate family-level transfer. No target-specific annotation is strictly required to arrive at B among the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, B is clearly the most defensible. A and D are eliminated by size/domain incompatibility. C requires a viral context not suggested by the sequence. Although cytoplasm is also annotated for this protein, it is not offered as a choice, so no ambiguity exists among the presented alternatives.


### Important caveats

- The protein is also experimentally annotated to cytoplasm (GO:0005737, IDA), but cytoplasm is not among the choices, so this does not create ambiguity among the offered options.
- The membrane localization of HAL3 may be peripheral rather than integral; the sequence lacks a canonical long hydrophobic transmembrane helix, so sequence-based TM prediction tools might not independently confirm membrane association without family knowledge.
- The 'host cell plasma membrane' vs 'plasma membrane' distinction depends on recognizing that GO:0020002 is virus-specific; a model unfamiliar with GO term semantics might find C and B less clearly separable.
- The yeast HAL3 homology (same 214-aa length, same family) is a strong transferable cue but requires the model to recognize the family from sequence features rather than from the target's own annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable lines of reasoning distinguish B from the alternatives: (1) Replisome (A) consists of large multi-component enzymatic machines (DNA polymerases, helicases, primases) typically hundreds to thousands of residues with catalytic domains; a 214-aa protein with no recognizable polymerase/helicase/primase motifs is inconsistent. (2) RQC complex (D) comprises specific proteins (Cdc48p, Rkr1p, Tae2p, Rqc1p, Npl4p, Ufd1p) with AAA+ ATPase, E3 ligase, or ribosome-binding domains absent here. (3) 'Host cell plasma membrane' (C, GO:0020002) is a GO term specifically defined for viral proteins localizing to the host membrane (goslim_virus subset); the sequence lacks viral structural motifs (capsid, polymerase, envelope proteins) and resembles a small metabolic enzyme, making C inappropriate. (4) Family-level knowledge: the sequence matches the HAL3/PPCDC family; in Saccharomyces cerevisiae, HAL3 (also 214 aa) is a well-characterized plasma membrane-associated protein involved in salt tolerance, a property transferable to homologs. The combination of elimination (A, D clearly wrong; C requires viral context absent here) and positive family inference (HAL3 membrane association in yeast) supports B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A and D relies on well-known structural/functional constraints of replisome and RQC components. The B-vs-C distinction relies on GO term semantics (host cell = viral context) and the absence of viral features. The positive support for membrane localization draws on the well-established yeast HAL3 homolog being a plasma membrane protein, which is legitimate family-level transfer. No target-specific annotation is strictly required to arrive at B among the offered choices."
  },
  "case_id": "GO_cellular_component_0037",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C8",
      "C6",
      "H3",
      "H6",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A498JQK2) annotates this protein with GO:0005886 (plasma membrane, IDA:UniProtKB, experimental evidence from PubMed:32761275) and also GO:0005737 (cytoplasm, IDA). The subcellular location comment lists 'Cell membrane' (an EXACT synonym for plasma membrane per GO1) and 'Cytoplasm.' The expected answer B (plasma membrane) is directly supported by the experimental annotation. Cytoplasm is also annotated but is not among the offered choices, so B is the best-supported option among those presented."
  },
  "important_caveats": [
    "The protein is also experimentally annotated to cytoplasm (GO:0005737, IDA), but cytoplasm is not among the choices, so this does not create ambiguity among the offered options.",
    "The membrane localization of HAL3 may be peripheral rather than integral; the sequence lacks a canonical long hydrophobic transmembrane helix, so sequence-based TM prediction tools might not independently confirm membrane association without family knowledge.",
    "The 'host cell plasma membrane' vs 'plasma membrane' distinction depends on recognizing that GO:0020002 is virus-specific; a model unfamiliar with GO term semantics might find C and B less clearly separable.",
    "The yeast HAL3 homology (same 214-aa length, same family) is a strong transferable cue but requires the model to recognize the family from sequence features rather than from the target's own annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, B is clearly the most defensible. A and D are eliminated by size/domain incompatibility. C requires a viral context not suggested by the sequence. Although cytoplasm is also annotated for this protein, it is not offered as a choice, so no ambiguity exists among the presented alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0037",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A498JQK2) annotates this protein with GO:0005886 (plasma membrane, IDA:UniProtKB, experimental evidence from PubMed:32761275) and also GO:0005737 (cytoplasm, IDA). The subcellular location comment lists 'Cell membrane' (an EXACT synonym for plasma membrane per GO1) and 'Cytoplasm.' The expected answer B (plasma membrane) is directly supported by the experimental annotation. Cytoplasm is also annotated but is not among the offered choices, so B is the best-supported option among those presented.",
    "evidence_ids": ["C5", "C8", "C6", "H3", "H6", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable lines of reasoning distinguish B from the alternatives: (1) Replisome (A) consists of large multi-component enzymatic machines (DNA polymerases, helicases, primases) typically hundreds to thousands of residues with catalytic domains; a 214-aa protein with no recognizable polymerase/helicase/primase motifs is inconsistent. (2) RQC complex (D) comprises specific proteins (Cdc48p, Rkr1p, Tae2p, Rqc1p, Npl4p, Ufd1p) with AAA+ ATPase, E3 ligase, or ribosome-binding domains absent here. (3) 'Host cell plasma membrane' (C, GO:0020002) is a GO term specifically defined for viral proteins localizing to the host membrane (goslim_virus subset); the sequence lacks viral structural motifs (capsid, polymerase, envelope proteins) and resembles a small metabolic enzyme, making C inappropriate. (4) Family-level knowledge: the sequence matches the HAL3/PPCDC family; in Saccharomyces cerevisiae, HAL3 (also 214 aa) is a well-characterized plasma membrane-associated protein involved in salt tolerance, a property transferable to homologs. The combination of elimination (A, D clearly wrong; C requires viral context absent here) and positive family inference (HAL3 membrane association in yeast) supports B.",
    "missing_item_specific_fact": "",
    "reason": "The elimination of A and D relies on well-known structural/functional constraints of replisome and RQC components. The B-vs-C distinction relies on GO term semantics (host cell = viral context) and the absence of viral features. The positive support for membrane localization draws on the well-established yeast HAL3 homolog being a plasma membrane protein, which is legitimate family-level transfer. No target-specific annotation is strictly required to arrive at B among the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, B is clearly the most defensible. A and D are eliminated by size/domain incompatibility. C requires a viral context not suggested by the sequence. Although cytoplasm is also annotated for this protein, it is not offered as a choice, so no ambiguity exists among the presented alternatives."
  },
  "important_caveats": [
    "The protein is also experimentally annotated to cytoplasm (GO:0005737, IDA), but cytoplasm is not among the choices, so this does not create ambiguity among the offered options.",
    "The membrane localization of HAL3 may be peripheral rather than integral; the sequence lacks a canonical long hydrophobic transmembrane helix, so sequence-based TM prediction tools might not independently confirm membrane association without family knowledge.",
    "The 'host cell plasma membrane' vs 'plasma membrane' distinction depends on recognizing that GO:0020002 is virus-specific; a model unfamiliar with GO term semantics might find C and B less clearly separable.",
    "The yeast HAL3 homology (same 214-aa length, same family) is a strong transferable cue but requires the model to recognize the family from sequence features rather than from the target's own annotation."
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
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"id\":\"SL-0039\",\"value\":\"Cell membrane\"}},{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"id\":\"SL-0086\",\"value\":\"Cytoplasm\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
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
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"id\":\"GO:0005737\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:cytoplasm\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/7",
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
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0071513\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:phosphopantothenoylcysteine decarboxylase complex\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/8",
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
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"32761275\",\"source\":\"PubMed\"}],\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
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
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:32761275}.\nCC       Cytoplasm {ECO:0000269|PubMed:32761275}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-59",
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
  "excerpt": "DR   GO; GO:0005737; C:cytoplasm; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 81-81",
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
  "excerpt": "DR   GO; GO:0071513; C:phosphopantothenoylcysteine decarboxylase complex; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 82-82",
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
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:31.570388+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 83-83",
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
  "excerpt": "[Term]\nid: GO:0005886\nname: plasma membrane\nnamespace: cellular_component\nalt_id: GO:0005887\nalt_id: GO:0005904\ndef: \"The membrane surrounding a cell that separates the cell from its external environment. It consists of a phospholipid bilayer and associated proteins.\" [ISBN:0716731363]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"bacterial inner membrane\" NARROW []\nsynonym: \"cell membrane\" EXACT []\nsynonym: \"cellular membrane\" EXACT [NIF_Subcellular:sao6433132645]\nsynonym: \"cytoplasmic membrane\" EXACT []\nsynonym: \"inner endospore membrane\" NARROW []\nsynonym: \"integral component of plasma membrane\" NARROW []\nsynonym: \"integral to plasma membrane\" NARROW []\nsynonym: \"juxtamembrane\" BROAD []\nsynonym: \"plasma membrane lipid bilayer\" NARROW [GOC:mah]\nsynonym: \"plasmalemma\" EXACT []\nxref: NIF_Subcellular:sao1663586795\nxref: Wikipedia:Cell_membrane\nis_a: GO:0016020 ! membrane\nrelationship: part_of GO:0071944 ! cell periphery\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005886",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 60420-60454",
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
  "excerpt": "[Term]\nid: GO:0020002\nname: host cell plasma membrane\nnamespace: cellular_component\ndef: \"The plasma membrane surrounding a host cell.\" [GOC:mb]\nsubset: goslim_virus\nis_a: GO:0033644 ! host cell membrane\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0020002",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 155120-155127",
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
  "excerpt": "[Term]\nid: GO:0030894\nname: replisome\nnamespace: cellular_component\ndef: \"A multi-component enzymatic machine at the replication fork which mediates DNA replication. Includes DNA primase, one or more DNA polymerases, DNA helicases, and other proteins.\" [GOC:mah, GOC:vw]\nsubset: goslim_pir\nsynonym: \"DNA synthesome complex\" RELATED [CORUM:1001]\nsynonym: \"RC complex\" RELATED [CORUM:309, PMID:12006500]\nsynonym: \"replication-competent complex\" RELATED [CORUM:309, PMID:12006500]\nxref: Wikipedia:Replisome\nis_a: GO:0032993 ! protein-DNA complex\nrelationship: part_of GO:0005657 ! replication fork\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030894",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 171246-171258",
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
  "excerpt": "[Term]\nid: GO:1990112\nname: RQC complex\nnamespace: cellular_component\ndef: \"A multiprotein complex that forms a stable complex with large ribosomal subunits (60S in eukaryotes and 50S in prokaryotes) containing stalled polypeptides and triggers their degradation (ribosomal quality control). In budding yeast, this complex includes Cdc48p, Rkr1p, Tae2p, Rqc1p, Npl4p and Ufd1p proteins.\" [GOC:rb, PMID:23178123, PMID:23232563]\nsynonym: \"ribosome quality control complex\" EXACT [PMID:23178123, PMID:23232563]\nsynonym: \"ribosome-bound quality control complex\" EXACT []\nis_a: GO:0032991 ! protein-containing complex\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:1990112",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 549333-549341",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 37. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
