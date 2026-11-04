# cofactor_0019

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0019.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — Zn(2+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNFSIKATIRAWSAPEHKLACRKQLWRKIVAELERRGKRRHEAGTFLLGIERNGRKEVQSAVYYDDLDPSAYDSGVCILHGDAFAKLWSHCREKGLTVVADVHTHPGAGFQSDSDRTNPMVARQGHIAIILPNFARWPIRQGNLGIYEYCGQHEWLERSPAHAPNFFYTGFWS

[Multiple Choices]
A. Ca(2+)
B. Zn(2+)
C. tungstopterin
D. cob(II)alamin
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

> The sequence-matched UniProt record annotates Zn(2+) as a cofactor, and the archived record available by the stated cutoff carries the same annotation. Its evidence is transferred from another UniProt entry (ECO:0000250), however, so this supports the key as a database annotation rather than demonstrating experimentally that zinc is required for this protein's catalytic activity.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The sequence-matched protein's Zn(2+) cofactor annotation, which is itself transferred from another UniProt entry; alternatively, direct evidence of this protein's metal dependence.


**Reason**

> The sequence has cysteine and histidine residues, but they do not establish a zinc-binding site or an obligatory zinc requirement. A cysteine/histidine catalytic arrangement can occur in proteases without a metal cofactor, and the sequence does not meaningfully resolve Zn(2+) versus Ca(2+). The larger cofactors are less plausible from general enzyme-family patterns, but that does not provide a sound basis for selecting Zn over calcium.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence and choices do not establish multiple particular cofactors; the source annotation supports Zn, though only by transferred evidence.


### Important caveats

- The reviewer-only source record matches the supplied sequence; its identity and annotation were not part of the original model input.
- The cofactor evidence is computationally transferred, not direct experimental evidence that zinc is required for catalytic activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The sequence-matched protein's Zn(2+) cofactor annotation, which is itself transferred from another UniProt entry; alternatively, direct evidence of this protein's metal dependence.",
    "reason": "The sequence has cysteine and histidine residues, but they do not establish a zinc-binding site or an obligatory zinc requirement. A cysteine/histidine catalytic arrangement can occur in proteases without a metal cofactor, and the sequence does not meaningfully resolve Zn(2+) versus Ca(2+). The larger cofactors are less plausible from general enzyme-family patterns, but that does not provide a sound basis for selecting Zn over calcium."
  },
  "case_id": "cofactor_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Zn(2+) as a cofactor, and the archived record available by the stated cutoff carries the same annotation. Its evidence is transferred from another UniProt entry (ECO:0000250), however, so this supports the key as a database annotation rather than demonstrating experimentally that zinc is required for this protein's catalytic activity."
  },
  "important_caveats": [
    "The reviewer-only source record matches the supplied sequence; its identity and annotation were not part of the original model input.",
    "The cofactor evidence is computationally transferred, not direct experimental evidence that zinc is required for catalytic activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence and choices do not establish multiple particular cofactors; the source annotation supports Zn, though only by transferred evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates Zn(2+) as a cofactor, and the archived record available by the stated cutoff carries the same annotation. Its evidence is transferred from another UniProt entry (ECO:0000250), however, so this supports the key as a database annotation rather than demonstrating experimentally that zinc is required for this protein's catalytic activity.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The sequence-matched protein's Zn(2+) cofactor annotation, which is itself transferred from another UniProt entry; alternatively, direct evidence of this protein's metal dependence.",
    "reason": "The sequence has cysteine and histidine residues, but they do not establish a zinc-binding site or an obligatory zinc requirement. A cysteine/histidine catalytic arrangement can occur in proteases without a metal cofactor, and the sequence does not meaningfully resolve Zn(2+) versus Ca(2+). The larger cofactors are less plausible from general enzyme-family patterns, but that does not provide a sound basis for selecting Zn over calcium."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence and choices do not establish multiple particular cofactors; the source annotation supports Zn, though only by transferred evidence."
  },
  "important_caveats": [
    "The reviewer-only source record matches the supplied sequence; its identity and annotation were not part of the original model input.",
    "The cofactor evidence is computationally transferred, not direct experimental evidence that zinc is required for catalytic activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A1I1NU16) explicitly annotates Zn(2+) as the cofactor (evidence IDs C5, H4). The EC number is 3.4.19.- (deubiquitinase), and the evidence code is ECO:0000250 (inferred by similarity to Q8U1Y4, another DUB). While this is a similarity-based transfer rather than direct experimental proof for this exact protein, the annotation is present and consistent with the known biochemistry of DUB-family proteases, which are predominantly Zn(2+)-dependent metalloproteases.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 173-aa sequence contains multiple Cys and His residues clustered in regions (e.g., 'VCILHGDAFAKLWSHCREKG', 'VHTHPGAG', 'YEYCGQHEWLERSPAHAPNFFYTGFWS'), a pattern highly characteristic of zinc-coordination sites in metalloproteases. Transferable knowledge establishes that: (1) tungstopterin is a cofactor exclusively for certain anaerobic oxidoreductases (formate dehydrogenases, aldehyde oxidoreductases) with very different large multi-domain architectures; (2) cob(II)alamin is restricted to specific isomerases, methyltransferases, and radical enzymes, none of which are proteases; (3) Ca(2+) in proteases is typically structural (e.g., subtilisins) and does not coordinate via Cys/His clusters; (4) Zn(2+) is the overwhelmingly dominant catalytic/structural cofactor for cysteine-histidine proteases, including the entire DUB superfamily. The Cys/His clustering plus elimination of clearly mismatched cofactor classes makes Zn(2+) the strongly preferred answer without needing to know this exact protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the Cys/His residue clustering as a transferable sequence feature indicating zinc coordination, combined with general enzyme-cofactor specificity knowledge to eliminate tungstopterin (oxidoreductase-specific), cob(II)alamin (isomerase/radical-enzyme-specific), and Ca(2+) (structural, not Cys/His-coordinated). This constitutes legitimate family-level and mechanistic reasoning from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The Cys/His clustering pattern and the strong class-specificity of the other cofactors (tungstopterin for oxidoreductases, cobalamin for isomerases) leave Zn(2+) as the only biochemically plausible answer among the four choices. Ca(2+) is the only other metal ion but lacks the coordination chemistry suggested by the sequence.


### Important caveats

- The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (similarity to Q8U1Y4), meaning it is a computational transfer rather than direct experimental measurement on this exact protein.
- Identifying the protein specifically as a 'deubiquitinase' from the raw sequence alone is non-trivial; the reasoning relies on Cys/His clustering and elimination rather than a recognizable DUB catalytic motif.
- The protein was characterized in a 2024 Nature paper (Hoer, Wolf, Sorek) as a bacterial DUB-like protein involved in ubiquitin-like protein conjugation to interfere with phage assembly.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 173-aa sequence contains multiple Cys and His residues clustered in regions (e.g., 'VCILHGDAFAKLWSHCREKG', 'VHTHPGAG', 'YEYCGQHEWLERSPAHAPNFFYTGFWS'), a pattern highly characteristic of zinc-coordination sites in metalloproteases. Transferable knowledge establishes that: (1) tungstopterin is a cofactor exclusively for certain anaerobic oxidoreductases (formate dehydrogenases, aldehyde oxidoreductases) with very different large multi-domain architectures; (2) cob(II)alamin is restricted to specific isomerases, methyltransferases, and radical enzymes, none of which are proteases; (3) Ca(2+) in proteases is typically structural (e.g., subtilisins) and does not coordinate via Cys/His clusters; (4) Zn(2+) is the overwhelmingly dominant catalytic/structural cofactor for cysteine-histidine proteases, including the entire DUB superfamily. The Cys/His clustering plus elimination of clearly mismatched cofactor classes makes Zn(2+) the strongly preferred answer without needing to know this exact protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the Cys/His residue clustering as a transferable sequence feature indicating zinc coordination, combined with general enzyme-cofactor specificity knowledge to eliminate tungstopterin (oxidoreductase-specific), cob(II)alamin (isomerase/radical-enzyme-specific), and Ca(2+) (structural, not Cys/His-coordinated). This constitutes legitimate family-level and mechanistic reasoning from other proteins."
  },
  "case_id": "cofactor_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A1I1NU16) explicitly annotates Zn(2+) as the cofactor (evidence IDs C5, H4). The EC number is 3.4.19.- (deubiquitinase), and the evidence code is ECO:0000250 (inferred by similarity to Q8U1Y4, another DUB). While this is a similarity-based transfer rather than direct experimental proof for this exact protein, the annotation is present and consistent with the known biochemistry of DUB-family proteases, which are predominantly Zn(2+)-dependent metalloproteases."
  },
  "important_caveats": [
    "The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (similarity to Q8U1Y4), meaning it is a computational transfer rather than direct experimental measurement on this exact protein.",
    "Identifying the protein specifically as a 'deubiquitinase' from the raw sequence alone is non-trivial; the reasoning relies on Cys/His clustering and elimination rather than a recognizable DUB catalytic motif.",
    "The protein was characterized in a 2024 Nature paper (Hoer, Wolf, Sorek) as a bacterial DUB-like protein involved in ubiquitin-like protein conjugation to interfere with phage assembly."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Cys/His clustering pattern and the strong class-specificity of the other cofactors (tungstopterin for oxidoreductases, cobalamin for isomerases) leave Zn(2+) as the only biochemically plausible answer among the four choices. Ca(2+) is the only other metal ion but lacks the coordination chemistry suggested by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A1I1NU16) explicitly annotates Zn(2+) as the cofactor (evidence IDs C5, H4). The EC number is 3.4.19.- (deubiquitinase), and the evidence code is ECO:0000250 (inferred by similarity to Q8U1Y4, another DUB). While this is a similarity-based transfer rather than direct experimental proof for this exact protein, the annotation is present and consistent with the known biochemistry of DUB-family proteases, which are predominantly Zn(2+)-dependent metalloproteases.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 173-aa sequence contains multiple Cys and His residues clustered in regions (e.g., 'VCILHGDAFAKLWSHCREKG', 'VHTHPGAG', 'YEYCGQHEWLERSPAHAPNFFYTGFWS'), a pattern highly characteristic of zinc-coordination sites in metalloproteases. Transferable knowledge establishes that: (1) tungstopterin is a cofactor exclusively for certain anaerobic oxidoreductases (formate dehydrogenases, aldehyde oxidoreductases) with very different large multi-domain architectures; (2) cob(II)alamin is restricted to specific isomerases, methyltransferases, and radical enzymes, none of which are proteases; (3) Ca(2+) in proteases is typically structural (e.g., subtilisins) and does not coordinate via Cys/His clusters; (4) Zn(2+) is the overwhelmingly dominant catalytic/structural cofactor for cysteine-histidine proteases, including the entire DUB superfamily. The Cys/His clustering plus elimination of clearly mismatched cofactor classes makes Zn(2+) the strongly preferred answer without needing to know this exact protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the Cys/His residue clustering as a transferable sequence feature indicating zinc coordination, combined with general enzyme-cofactor specificity knowledge to eliminate tungstopterin (oxidoreductase-specific), cob(II)alamin (isomerase/radical-enzyme-specific), and Ca(2+) (structural, not Cys/His-coordinated). This constitutes legitimate family-level and mechanistic reasoning from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The Cys/His clustering pattern and the strong class-specificity of the other cofactors (tungstopterin for oxidoreductases, cobalamin for isomerases) leave Zn(2+) as the only biochemically plausible answer among the four choices. Ca(2+) is the only other metal ion but lacks the coordination chemistry suggested by the sequence."
  },
  "important_caveats": [
    "The UniProt Zn(2+) annotation carries evidence code ECO:0000250 (similarity to Q8U1Y4), meaning it is a computational transfer rather than direct experimental measurement on this exact protein.",
    "Identifying the protein specifically as a 'deubiquitinase' from the raw sequence alone is non-trivial; the reasoning relies on Cys/His clustering and elimination rather than a recognizable DUB catalytic motif.",
    "The protein was characterized in a 2024 Nature paper (Hoer, Wolf, Sorek) as a bacterial DUB-like protein involved in ubiquitin-like protein conjugation to interfere with phage assembly."
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
  "benchmark_sequence_length": 173,
  "benchmark_sequence_sha256": "d895b201f6e47e07f5d218ae2fc39becf53cafed9f0ce331c296e06777dbb9bb",
  "current_entry_audit": {
    "entryVersion": 17,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-11-22",
    "sequenceVersion": 1
  },
  "current_record_sha256": "2450dd0158f63f7b3f964bfa3e69c422b1dc5d0a2efaa93e6a1ae658b0822f51",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 173,
  "current_source_sequence_sha256": "d895b201f6e47e07f5d218ae2fc39becf53cafed9f0ce331c296e06777dbb9bb",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 16,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A1I1NU16",
  "selected_historical_entry_version": 16,
  "selected_historical_record_sha256": "96684b22a4f18425cd76c99b60ea43354370a287ba92e5f18d487c26373fdf25",
  "selected_historical_source_sequence_length": 173,
  "selected_historical_source_sequence_sha256": "d895b201f6e47e07f5d218ae2fc39becf53cafed9f0ce331c296e06777dbb9bb",
  "selected_historical_version": {
    "accession": "A0A1I1NU16",
    "database": "Swiss-Prot",
    "entryVersion": 16,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "BILC_COLS4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU16.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1I1NU16\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:36.222044+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2450dd0158f63f7b3f964bfa3e69c422b1dc5d0a2efaa93e6a1ae658b0822f51",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1NU16.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU16.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":17,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-11-22\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:36.222044+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2450dd0158f63f7b3f964bfa3e69c422b1dc5d0a2efaa93e6a1ae658b0822f51",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1NU16.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU16.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Oxalobacteraceae\",\"Collimonas\"],\"scientificName\":\"Collimonas sp. (strain OK412)\",\"taxonId\":1801619}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:36.222044+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2450dd0158f63f7b3f964bfa3e69c422b1dc5d0a2efaa93e6a1ae658b0822f51",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1NU16.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU16.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39020165\",\"source\":\"PubMed\"}],\"value\":\"3.4.19.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39020165\",\"source\":\"PubMed\"}],\"value\":\"Bacterial deubiquitinase-like protein BilC\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39020165\",\"source\":\"PubMed\"}],\"value\":\"DUB\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:36.222044+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2450dd0158f63f7b3f964bfa3e69c422b1dc5d0a2efaa93e6a1ae658b0822f51",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1NU16.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU16.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:29105\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q8U1Y4\",\"source\":\"UniProtKB\"}],\"name\":\"Zn(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:24:36.222044+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2450dd0158f63f7b3f964bfa3e69c422b1dc5d0a2efaa93e6a1ae658b0822f51",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1NU16.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1I1NU16.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Hoer J.\",\"Wolf S.G.\",\"Sorek R.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39020165\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41586-024-07616-5\"}],\"citationType\":\"journal article\",\"firstPage\":\"850\",\"id\":\"39020165\",\"journal\":\"Nature\",\"lastPage\":\"856\",\"publicationDate\":\"2024\",\"title\":\"Bacteria conjugate ubiquitin-like proteins to interfere with phage assembly.\",\"volume\":\"631\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"MUTAGENESIS OF ASP-115\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:36.222044+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "2450dd0158f63f7b3f964bfa3e69c422b1dc5d0a2efaa93e6a1ae658b0822f51",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1I1NU16.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1NU16?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H1",
  "excerpt": "ID   BILC_COLS4              Reviewed;         173 AA.\nAC   A0A1I1NU16;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   22-NOV-2017, sequence version 1.\nDT   28-JAN-2026, entry version 16.\nDE   RecName: Full=Bacterial deubiquitinase-like protein BilC {ECO:0000303|PubMed:39020165};\nDE            Short=DUB {ECO:0000303|PubMed:39020165};\nDE            EC=3.4.19.- {ECO:0000269|PubMed:39020165};\nGN   Name=bilC {ECO:0000303|PubMed:39020165};\nGN   ORFNames=SAMN04515619_11956 {ECO:0000312|EMBL:SFD01151.1};\nOS   Collimonas sp. (strain OK412).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Oxalobacteraceae; Collimonas.\nOX   NCBI_TaxID=1801619;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:38.299172+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "96684b22a4f18425cd76c99b60ea43354370a287ba92e5f18d487c26373fdf25",
  "url": "https://rest.uniprot.org/unisave/A0A1I1NU16?format=txt&versions=16"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1NU16?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Bacterial deubiquitinase-like protein BilC {ECO:0000303|PubMed:39020165};\nDE            Short=DUB {ECO:0000303|PubMed:39020165};\nDE            EC=3.4.19.- {ECO:0000269|PubMed:39020165};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:38.299172+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "96684b22a4f18425cd76c99b60ea43354370a287ba92e5f18d487c26373fdf25",
  "url": "https://rest.uniprot.org/unisave/A0A1I1NU16?format=txt&versions=16"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1NU16?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND MUTAGENESIS OF ASP-115.\nRX   PubMed=39020165; DOI=10.1038/s41586-024-07616-5;\nRA   Hoer J., Wolf S.G., Sorek R.;\nRT   \"Bacteria conjugate ubiquitin-like proteins to interfere with phage\nRT   assembly.\";\nRL   Nature 631:850-856(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:38.299172+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "96684b22a4f18425cd76c99b60ea43354370a287ba92e5f18d487c26373fdf25",
  "url": "https://rest.uniprot.org/unisave/A0A1I1NU16?format=txt&versions=16"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1I1NU16?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Zn(2+); Xref=ChEBI:CHEBI:29105;\nCC         Evidence={ECO:0000250|UniProtKB:Q8U1Y4};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:38.299172+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 52-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "96684b22a4f18425cd76c99b60ea43354370a287ba92e5f18d487c26373fdf25",
  "url": "https://rest.uniprot.org/unisave/A0A1I1NU16?format=txt&versions=16"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 19. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
