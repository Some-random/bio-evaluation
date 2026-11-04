# GO_cellular_component_0006

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_cellular_component_0006.txt)

**Task:** `GO_cellular_component`  
**Expected answer:** **D** — plasma membrane

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | contradicted | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKSLIGTLGLYCLFILTNNVVSSYGDDLYPLTIMHTNDFHARFEETNVKGNPCKSGEKCIGGLARVLHTIKKIIKEQEKKNIESLYINAGDNFQGTIWYNIGRWNVTSELMNIQPPDVMVLGNHEFDHGIDGLLPFLNNMDKTEIVVANMDARDEPQVAKKIKPFTIIKKKYRNIGVIGVVVEEVPDLANTGKLKFRNESEAILEAARNLKKEDPSVNIIIVVSHVGFDVDKIIAERTGSEVDIIVGGHSHTVLYTGTPPGPEKPEDNYPYVYNHPSGNKVLVVQAVCHAKYVGNLTVFFDKKGKVVTYEGAPIYMDTKVEQDKDVLEAMKPWRKLIDEKTKLVVGRTNVDLPRDICRSEECALGNLYTDSMIYAFGGKENCKSGSTWTTAPIAFVHAGAMRSSLHQGDILYSDALLLSPFTNMVVAYDLPGAQLKAALEFSAAPKNEDEKRRFLQMSGLKVTYNMSRAANNRIVDLKVRTNVCPYDQYENLDEKKTYRVVSPSFLQGGGDGFKMLRDYAKNIQNQKIDLDALVDYLKKFSPLAPKAEGRITIIH

[Multiple Choices]
A. aggresome
B. cytoplasmic vesicle
C. host cell plasma membrane
D. plasma membrane
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

### Expected-answer support: contradicted

> The sequence-matched record reports experimental evidence that the protein is secreted and is in the extracellular region/space (C5, C6, H3, H4). The plasma-membrane annotation is computationally inferred (C7, H5), so the supplied evidence does not support plasma membrane as its primary location and instead conflicts with it.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal hydrophobic segment is consistent with a secretory signal peptide, while the rest of the sequence lacks an evident membrane-spanning segment or C-terminal membrane anchor. Transferable knowledge therefore favors a soluble secreted protein, not a resident plasma-membrane protein; none of the offered choices cleanly represents that destination.


**Missing item-specific fact**

> Reproducing D as the keyed answer requires the target-specific plasma-membrane annotation, which is not supplied in the original input and is computationally inferred in the reviewer evidence.


**Reason**

> Sequence features and general secretory-pathway knowledge do not meaningfully support D over the biological destination suggested by the sequence, which is absent from the choices. Choosing D as the recorded answer depends on knowing this exact protein's annotation, rather than a transferable feature that distinguishes it.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No offered option is clearly supported as the primary location by the sequence-based inference: the sequence favors secretion, while aggresome, cytoplasmic vesicle, and host cell plasma membrane are not established destinations. This is a missing-best-option issue rather than multiple defensible choices.


### Important caveats

- The sequence-matched source reports both experimental secretion and a computational plasma-membrane annotation; the latter does not establish experimental plasma-membrane residence.
- The author’s exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretory signal peptide, while the rest of the sequence lacks an evident membrane-spanning segment or C-terminal membrane anchor. Transferable knowledge therefore favors a soluble secreted protein, not a resident plasma-membrane protein; none of the offered choices cleanly represents that destination.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Reproducing D as the keyed answer requires the target-specific plasma-membrane annotation, which is not supplied in the original input and is computationally inferred in the reviewer evidence.",
    "reason": "Sequence features and general secretory-pathway knowledge do not meaningfully support D over the biological destination suggested by the sequence, which is absent from the choices. Choosing D as the recorded answer depends on knowing this exact protein's annotation, rather than a transferable feature that distinguishes it."
  },
  "case_id": "GO_cellular_component_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports experimental evidence that the protein is secreted and is in the extracellular region/space (C5, C6, H3, H4). The plasma-membrane annotation is computationally inferred (C7, H5), so the supplied evidence does not support plasma membrane as its primary location and instead conflicts with it."
  },
  "important_caveats": [
    "The sequence-matched source reports both experimental secretion and a computational plasma-membrane annotation; the latter does not establish experimental plasma-membrane residence.",
    "The author’s exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No offered option is clearly supported as the primary location by the sequence-based inference: the sequence favors secretion, while aggresome, cytoplasmic vesicle, and host cell plasma membrane are not established destinations. This is a missing-best-option issue rather than multiple defensible choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_cellular_component_0006",
  "expected_answer_check": {
    "judgment": "contradicted",
    "reason": "The sequence-matched record reports experimental evidence that the protein is secreted and is in the extracellular region/space (C5, C6, H3, H4). The plasma-membrane annotation is computationally inferred (C7, H5), so the supplied evidence does not support plasma membrane as its primary location and instead conflicts with it.",
    "evidence_ids": ["C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal hydrophobic segment is consistent with a secretory signal peptide, while the rest of the sequence lacks an evident membrane-spanning segment or C-terminal membrane anchor. Transferable knowledge therefore favors a soluble secreted protein, not a resident plasma-membrane protein; none of the offered choices cleanly represents that destination.",
    "missing_item_specific_fact": "Reproducing D as the keyed answer requires the target-specific plasma-membrane annotation, which is not supplied in the original input and is computationally inferred in the reviewer evidence.",
    "reason": "Sequence features and general secretory-pathway knowledge do not meaningfully support D over the biological destination suggested by the sequence, which is absent from the choices. Choosing D as the recorded answer depends on knowing this exact protein's annotation, rather than a transferable feature that distinguishes it."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No offered option is clearly supported as the primary location by the sequence-based inference: the sequence favors secretion, while aggresome, cytoplasmic vesicle, and host cell plasma membrane are not established destinations. This is a missing-best-option issue rather than multiple defensible choices."
  },
  "important_caveats": [
    "The sequence-matched source reports both experimental secretion and a computational plasma-membrane annotation; the latter does not establish experimental plasma-membrane residence.",
    "The author’s exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for Q95P65 carries a GO:0005886 (plasma membrane) annotation, albeit with IEA:TreeGrafter evidence (computational inference by homology). The primary experimental annotation (IDA) is 'Secreted' / extracellular region (GO:0005576), which is not among the offered choices. Among the four options provided, 'plasma membrane' is the only one that appears in the UniProt record and is the most appropriate proxy for a secreted protein when 'extracellular region' is unavailable. The support is weak (IEA only), but the key is not contradicted by the evidence.

Citations as saved: [C7](#evidence-c7), [H5](#evidence-h5), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminus of the sequence (MKSLIGTLGLYCLFILTNNVVSSYG) displays a classic hydrophobic signal peptide, indicating entry into the secretory pathway. This immediately eliminates A (aggresome – a cytoplasmic inclusion body) and B (cytoplasmic vesicle – an intracellular compartment; a signal-peptide protein is not primarily retained in cytoplasmic vesicles). Option C ('host cell plasma membrane') is a GO term specifically reserved for pathogen/virus interactions with a host cell membrane (goslim_virus subset); a fly salivary enzyme is not a pathogen product localizing to a 'host cell' membrane. The remaining option D (plasma membrane) is the standard GO cellular-component assignment for a secreted protein when 'extracellular region' is not offered, as the protein must traverse and associate with the plasma membrane during exocytosis. This reasoning relies on general knowledge of signal peptides, the secretory pathway, and the specific semantics of the 'host cell plasma membrane' GO term – all transferable from other proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the signal peptide in the raw sequence, apply general secretion-pathway biology to exclude cytoplasmic compartments (A, B), and use the specific semantics of 'host cell plasma membrane' (pathogen context) to exclude C, arriving at D without needing the recorded answer for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The signal peptide unambiguously places the protein in the secretory pathway, excluding A and B. The 'host cell' qualifier in C restricts it to pathogen–host interactions, excluding it for an endogenous fly enzyme. D is the only remaining viable choice. While 'extracellular region' would be a more precise GO term for a fully secreted protein, it is not offered, making D the best available answer without genuine ambiguity among the four choices.


### Important caveats

- The plasma membrane GO annotation is IEA:TreeGrafter (computational homology inference), not experimental. The experimental (IDA) annotation is 'Secreted'/extracellular region, which is not among the options.
- The protein is a 5'-nucleotidase-related protein (apyrase, EC 3.6.1.5) from tsetse fly saliva, flagged as a Precursor with a signal peptide.
- The reviewer-only evidence confirms sequence match (555 AA, SHA256 identical) between the benchmark input and UniProt Q95P65.
- The GO ontology snapshot used by the benchmark authors is unknown; the supplied ontology is the current version.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminus of the sequence (MKSLIGTLGLYCLFILTNNVVSSYG) displays a classic hydrophobic signal peptide, indicating entry into the secretory pathway. This immediately eliminates A (aggresome – a cytoplasmic inclusion body) and B (cytoplasmic vesicle – an intracellular compartment; a signal-peptide protein is not primarily retained in cytoplasmic vesicles). Option C ('host cell plasma membrane') is a GO term specifically reserved for pathogen/virus interactions with a host cell membrane (goslim_virus subset); a fly salivary enzyme is not a pathogen product localizing to a 'host cell' membrane. The remaining option D (plasma membrane) is the standard GO cellular-component assignment for a secreted protein when 'extracellular region' is not offered, as the protein must traverse and associate with the plasma membrane during exocytosis. This reasoning relies on general knowledge of signal peptides, the secretory pathway, and the specific semantics of the 'host cell plasma membrane' GO term – all transferable from other proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the signal peptide in the raw sequence, apply general secretion-pathway biology to exclude cytoplasmic compartments (A, B), and use the specific semantics of 'host cell plasma membrane' (pathogen context) to exclude C, arriving at D without needing the recorded answer for this exact protein."
  },
  "case_id": "GO_cellular_component_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H5",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for Q95P65 carries a GO:0005886 (plasma membrane) annotation, albeit with IEA:TreeGrafter evidence (computational inference by homology). The primary experimental annotation (IDA) is 'Secreted' / extracellular region (GO:0005576), which is not among the offered choices. Among the four options provided, 'plasma membrane' is the only one that appears in the UniProt record and is the most appropriate proxy for a secreted protein when 'extracellular region' is unavailable. The support is weak (IEA only), but the key is not contradicted by the evidence."
  },
  "important_caveats": [
    "The plasma membrane GO annotation is IEA:TreeGrafter (computational homology inference), not experimental. The experimental (IDA) annotation is 'Secreted'/extracellular region, which is not among the options.",
    "The protein is a 5'-nucleotidase-related protein (apyrase, EC 3.6.1.5) from tsetse fly saliva, flagged as a Precursor with a signal peptide.",
    "The reviewer-only evidence confirms sequence match (555 AA, SHA256 identical) between the benchmark input and UniProt Q95P65.",
    "The GO ontology snapshot used by the benchmark authors is unknown; the supplied ontology is the current version."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide unambiguously places the protein in the secretory pathway, excluding A and B. The 'host cell' qualifier in C restricts it to pathogen–host interactions, excluding it for an endogenous fly enzyme. D is the only remaining viable choice. While 'extracellular region' would be a more precise GO term for a fully secreted protein, it is not offered, making D the best available answer without genuine ambiguity among the four choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_cellular_component_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for Q95P65 carries a GO:0005886 (plasma membrane) annotation, albeit with IEA:TreeGrafter evidence (computational inference by homology). The primary experimental annotation (IDA) is 'Secreted' / extracellular region (GO:0005576), which is not among the offered choices. Among the four options provided, 'plasma membrane' is the only one that appears in the UniProt record and is the most appropriate proxy for a secreted protein when 'extracellular region' is unavailable. The support is weak (IEA only), but the key is not contradicted by the evidence.",
    "evidence_ids": ["C7", "H5", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminus of the sequence (MKSLIGTLGLYCLFILTNNVVSSYG) displays a classic hydrophobic signal peptide, indicating entry into the secretory pathway. This immediately eliminates A (aggresome – a cytoplasmic inclusion body) and B (cytoplasmic vesicle – an intracellular compartment; a signal-peptide protein is not primarily retained in cytoplasmic vesicles). Option C ('host cell plasma membrane') is a GO term specifically reserved for pathogen/virus interactions with a host cell membrane (goslim_virus subset); a fly salivary enzyme is not a pathogen product localizing to a 'host cell' membrane. The remaining option D (plasma membrane) is the standard GO cellular-component assignment for a secreted protein when 'extracellular region' is not offered, as the protein must traverse and associate with the plasma membrane during exocytosis. This reasoning relies on general knowledge of signal peptides, the secretory pathway, and the specific semantics of the 'host cell plasma membrane' GO term – all transferable from other proteins.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the signal peptide in the raw sequence, apply general secretion-pathway biology to exclude cytoplasmic compartments (A, B), and use the specific semantics of 'host cell plasma membrane' (pathogen context) to exclude C, arriving at D without needing the recorded answer for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The signal peptide unambiguously places the protein in the secretory pathway, excluding A and B. The 'host cell' qualifier in C restricts it to pathogen–host interactions, excluding it for an endogenous fly enzyme. D is the only remaining viable choice. While 'extracellular region' would be a more precise GO term for a fully secreted protein, it is not offered, making D the best available answer without genuine ambiguity among the four choices."
  },
  "important_caveats": [
    "The plasma membrane GO annotation is IEA:TreeGrafter (computational homology inference), not experimental. The experimental (IDA) annotation is 'Secreted'/extracellular region, which is not among the options.",
    "The protein is a 5'-nucleotidase-related protein (apyrase, EC 3.6.1.5) from tsetse fly saliva, flagged as a Precursor with a signal peptide.",
    "The reviewer-only evidence confirms sequence match (555 AA, SHA256 identical) between the benchmark input and UniProt Q95P65.",
    "The GO ontology snapshot used by the benchmark authors is unknown; the supplied ontology is the current version."
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
  "benchmark_sequence_length": 555,
  "benchmark_sequence_sha256": "881429cdee022e789feb0de1032bd5397cddc0acbccdc7813dfdf72b98b7d5e1",
  "current_entry_audit": {
    "entryVersion": 84,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2001-12-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 555,
  "current_source_sequence_sha256": "881429cdee022e789feb0de1032bd5397cddc0acbccdc7813dfdf72b98b7d5e1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 83,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q95P65",
  "selected_historical_entry_version": 83,
  "selected_historical_record_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "selected_historical_source_sequence_length": 555,
  "selected_historical_source_sequence_sha256": "881429cdee022e789feb0de1032bd5397cddc0acbccdc7813dfdf72b98b7d5e1",
  "selected_historical_version": {
    "accession": "Q95P65",
    "database": "Swiss-Prot",
    "entryVersion": 83,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "APY_GLOMM",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q95P65\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":84,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2001-12-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Savannah tsetse fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AAK63848.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Hippoboscoidea\",\"Glossinidae\",\"Glossina\"],\"scientificName\":\"Glossina morsitans morsitans\",\"taxonId\":37546}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"value\":\"3.6.1.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"value\":\"5'-nucleotidase-related protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"value\":\"5'Nuc\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"SUBCELLULAR LOCATION\",\"subcellularLocations\":[{\"location\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"id\":\"SL-0243\",\"value\":\"Secreted\"}}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"20351782\",\"source\":\"PubMed\"}],\"id\":\"GO:0005576\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:extracellular region\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005886\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"C:plasma membrane\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q95P65.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Caljon G.\",\"De Ridder K.\",\"De Baetselier P.\",\"Coosemans M.\",\"Van Den Abbeele J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20351782\"},{\"database\":\"DOI\",\"id\":\"10.1371/journal.pone.0009671\"}],\"citationType\":\"journal article\",\"firstPage\":\"e9671\",\"id\":\"20351782\",\"journal\":\"PLoS ONE\",\"lastPage\":\"e9671\",\"publicationDate\":\"2010\",\"title\":\"Identification of a tsetse fly salivary protein with dual inhibitory action on human platelet aggregation.\",\"volume\":\"5\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBCELLULAR LOCATION\",\"TISSUE SPECIFICITY\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:25.918010+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b872d4ca06488362fc74985c252629d952ce7dbc06301bfe01faba9bd8e3702c",
  "url": "https://rest.uniprot.org/uniprotkb/Q95P65.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H1",
  "excerpt": "ID   APY_GLOMM               Reviewed;         555 AA.\nAC   Q95P65; D3TRV7;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-DEC-2001, sequence version 1.\nDT   28-JAN-2026, entry version 83.\nDE   RecName: Full=5'-nucleotidase-related protein {ECO:0000303|PubMed:20351782};\nDE            Short=5'Nuc {ECO:0000303|PubMed:20351782};\nDE            EC=3.6.1.5 {ECO:0000269|PubMed:20351782};\nDE   Flags: Precursor;\nOS   Glossina morsitans morsitans (Savannah tsetse fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Hippoboscoidea;\nOC   Glossinidae; Glossina.\nOX   NCBI_TaxID=37546 {ECO:0000312|EMBL:AAK63848.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:44.138990+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "url": "https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H2",
  "excerpt": "RN   [3] {ECO:0000305}\nRP   FUNCTION, CATALYTIC ACTIVITY, COFACTOR, ACTIVITY REGULATION,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBCELLULAR LOCATION, TISSUE SPECIFICITY,\nRP   AND DISRUPTION PHENOTYPE.\nRX   PubMed=20351782; DOI=10.1371/journal.pone.0009671;\nRA   Caljon G., De Ridder K., De Baetselier P., Coosemans M.,\nRA   Van Den Abbeele J.;\nRT   \"Identification of a tsetse fly salivary protein with dual inhibitory\nRT   action on human platelet aggregation.\";\nRL   PLoS ONE 5:e9671-e9671(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:44.138990+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "url": "https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H3",
  "excerpt": "CC   -!- SUBCELLULAR LOCATION: Secreted {ECO:0000269|PubMed:20351782}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:44.138990+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-77",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "url": "https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005615; C:extracellular space; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:44.138990+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "url": "https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83)

```json
{
  "entry_version": 83,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005886; C:plasma membrane; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:44.138990+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-99",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8f94d1be0e1177c1751f4d603face9ec9ba5dce46bd55845e3dbe4b520719448",
  "url": "https://rest.uniprot.org/unisave/Q95P65?format=txt&versions=83"
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
  "excerpt": "[Term]\nid: GO:0016235\nname: aggresome\nnamespace: cellular_component\ndef: \"An inclusion body formed by dynein-dependent retrograde transport of an aggregated protein on microtubules.\" [PMID:11121744]\nxref: Wikipedia:Aggresome\nis_a: GO:0016234 ! inclusion body\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016235",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 124908-124915",
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

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0031410\nname: cytoplasmic vesicle\nnamespace: cellular_component\nalt_id: GO:0016023\ndef: \"A vesicle found in the cytoplasm of a cell.\" [GOC:ai, GOC:mah, GOC:vesicles]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_yeast\nsynonym: \"cytoplasmic membrane bounded vesicle\" RELATED []\nsynonym: \"cytoplasmic membrane-enclosed vesicle\" RELATED []\nsynonym: \"cytoplasmic, membrane-bounded vesicle\" RELATED []\nxref: NIF_Subcellular:sao180601769\nis_a: GO:0097708 ! intracellular vesicle\nrelationship: part_of GO:0005737 ! cytoplasm\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0031410",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 176239-176257",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_cellular_component.json), zero-based source row 6. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
