# active_site_0049

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0049.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 18 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSAKMLHVVMYPWFAYGHMIPFLHLSNKLAETGHKVTYILPPKALTRLQNLNLNPTQITFRTITVPRVDGLPAGAENVTDIPDITLHTHLATALDRTRPEFETIVELIKPDVIMYDVAYWVPEVAVKYGAKSVAYSVVSAASVSLSKTVVDRMTPLEKPMTEEERKKKFAQYPHLIQLYGPFGEGITMYDRLTGMLSKCDAIACRTCREIEGKYCQYLSTQYEKKVTLTGPVLPEPEVGATLEAPWSEWLSRFKLGSVLFCAFGSQFYLDKDQFQEIILGLEMTNLPFLMAVQPPKGCATIEEAYPEGFAERVKDRGVVTSQWVQQLVILAHPAVGCFVNHCAFGTMWEALLSEKQLVMIPQLGDQILNTKMLADELKVGVEVERGIGGWVSKENLCKAIKSVMDEDSEIGKDVKQSHEKWRATLSSKDLMSTYIDSFIKDLQALVE

[Multiple Choices]
A. Position 2113 (For beta-ketoacyl synthase 2 activity)
B. Position 18 (Proton acceptor)
C. Position 1160 (Proton donor; for dehydratase activity)
D. Position 83 (Acyl-ester intermediate)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The matched-sequence UniProt annotation identifies position 18 as an active site proton acceptor. Its evidence is transferred from a homolog (ECO:0000250), so this supports the annotation but is not direct experimental validation of this protein.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Position 18 in the supplied sequence is histidine, a chemically plausible proton acceptor and a transferable catalytic role in enzyme families that use histidine as a general base. The sequence is 447 residues long, making the positions in A and C impossible; position 83 is threonine, not a plausible acyl-ester intermediate residue. These features meaningfully favor B among the offered choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and the alternatives provide a credible basis to favor B without knowing the recorded annotation for this exact protein, although the sequence alone does not prove the catalytic role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives are sufficiently distinguishable: A and C cite positions beyond the sequence length, and D assigns an acyl-ester intermediate to threonine at position 83.


### Important caveats

- The supporting source annotation is based on transfer from a homolog rather than direct experimental evidence for this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Position 18 in the supplied sequence is histidine, a chemically plausible proton acceptor and a transferable catalytic role in enzyme families that use histidine as a general base. The sequence is 447 residues long, making the positions in A and C impossible; position 83 is threonine, not a plausible acyl-ester intermediate residue. These features meaningfully favor B among the offered choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and the alternatives provide a credible basis to favor B without knowing the recorded annotation for this exact protein, although the sequence alone does not prove the catalytic role."
  },
  "case_id": "active_site_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies position 18 as an active site proton acceptor. Its evidence is transferred from a homolog (ECO:0000250), so this supports the annotation but is not direct experimental validation of this protein."
  },
  "important_caveats": [
    "The supporting source annotation is based on transfer from a homolog rather than direct experimental evidence for this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are sufficiently distinguishable: A and C cite positions beyond the sequence length, and D assigns an acyl-ester intermediate to threonine at position 83."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies position 18 as an active site proton acceptor. Its evidence is transferred from a homolog (ECO:0000250), so this supports the annotation but is not direct experimental validation of this protein.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Position 18 in the supplied sequence is histidine, a chemically plausible proton acceptor and a transferable catalytic role in enzyme families that use histidine as a general base. The sequence is 447 residues long, making the positions in A and C impossible; position 83 is threonine, not a plausible acyl-ester intermediate residue. These features meaningfully favor B among the offered choices.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and the alternatives provide a credible basis to favor B without knowing the recorded annotation for this exact protein, although the sequence alone does not prove the catalytic role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives are sufficiently distinguishable: A and C cite positions beyond the sequence length, and D assigns an acyl-ester intermediate to threonine at position 83."
  },
  "important_caveats": [
    "The supporting source annotation is based on transfer from a homolog rather than direct experimental evidence for this sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this sequence (A0AAW1IQ05, UDP-glucosyl transferase 79T1 from Saponaria officinalis) annotates position 18 as 'Proton acceptor' active site (ECO:0000250, transferred from A0A0A1HA03). The sequence at position 18 is indeed Histidine (H), consistent with a catalytic base role in glycosyltransferases. The annotation is by similarity rather than direct experimentation, but it is the recorded annotation supporting the key.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 447 residues long, so positions 2113 (A) and 1160 (C) are physically impossible and can be eliminated immediately by a simple length check. Position 83 in this sequence is Aspartic acid (D), which cannot form a covalent acyl-ester intermediate—acyl-ester intermediates require a nucleophilic residue such as Ser, Cys, or Thr; Asp's carboxylate is not nucleophilic enough for this role, eliminating D. Position 18 is Histidine, a well-established catalytic proton acceptor/base in many enzyme families including glycosyltransferases, making B the only chemically and structurally viable option. This elimination chain relies on general protein-chemistry knowledge (nucleophile requirements for acyl-esters, His as a general base) and a trivial sequence-length check, not on memorizing this protein's specific annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate A and C by noting the sequence is only 447 aa, eliminate D because Asp cannot form an acyl-ester intermediate (requires Ser/Cys/Thr), and confirm B because His at position 18 is a chemically sensible proton acceptor. The reasoning uses general biochemistry and a length check, not target-specific memorization.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and C reference positions far exceeding the 447-residue sequence length and are trivially impossible. Option D assigns an acyl-ester intermediate to Asp at position 83, which is chemically implausible. Only B survives elimination and is chemically consistent.


### Important caveats

- The UniProt active-site annotation at position 18 is by similarity (ECO:0000250 from A0A0A1HA03), not by direct experimental determination on this protein.
- The question's distractors A and C (positions 2113 and 1160) are obviously impossible for a 447-residue protein, making the question somewhat easier than a well-calibrated active-site prediction task.
- The PSPG motif typical of plant UGTs is usually in the C-terminal region; the His at position 18 in the N-terminal region is annotated as the proton acceptor by similarity transfer, which is a valid but indirect annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 447 residues long, so positions 2113 (A) and 1160 (C) are physically impossible and can be eliminated immediately by a simple length check. Position 83 in this sequence is Aspartic acid (D), which cannot form a covalent acyl-ester intermediate—acyl-ester intermediates require a nucleophilic residue such as Ser, Cys, or Thr; Asp's carboxylate is not nucleophilic enough for this role, eliminating D. Position 18 is Histidine, a well-established catalytic proton acceptor/base in many enzyme families including glycosyltransferases, making B the only chemically and structurally viable option. This elimination chain relies on general protein-chemistry knowledge (nucleophile requirements for acyl-esters, His as a general base) and a trivial sequence-length check, not on memorizing this protein's specific annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A and C by noting the sequence is only 447 aa, eliminate D because Asp cannot form an acyl-ester intermediate (requires Ser/Cys/Thr), and confirm B because His at position 18 is a chemically sensible proton acceptor. The reasoning uses general biochemistry and a length check, not target-specific memorization."
  },
  "case_id": "active_site_0049",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0AAW1IQ05, UDP-glucosyl transferase 79T1 from Saponaria officinalis) annotates position 18 as 'Proton acceptor' active site (ECO:0000250, transferred from A0A0A1HA03). The sequence at position 18 is indeed Histidine (H), consistent with a catalytic base role in glycosyltransferases. The annotation is by similarity rather than direct experimentation, but it is the recorded annotation supporting the key."
  },
  "important_caveats": [
    "The UniProt active-site annotation at position 18 is by similarity (ECO:0000250 from A0A0A1HA03), not by direct experimental determination on this protein.",
    "The question's distractors A and C (positions 2113 and 1160) are obviously impossible for a 447-residue protein, making the question somewhat easier than a well-calibrated active-site prediction task.",
    "The PSPG motif typical of plant UGTs is usually in the C-terminal region; the His at position 18 in the N-terminal region is annotated as the proton acceptor by similarity transfer, which is a valid but indirect annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C reference positions far exceeding the 447-residue sequence length and are trivially impossible. Option D assigns an acyl-ester intermediate to Asp at position 83, which is chemically implausible. Only B survives elimination and is chemically consistent."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0049",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this sequence (A0AAW1IQ05, UDP-glucosyl transferase 79T1 from Saponaria officinalis) annotates position 18 as 'Proton acceptor' active site (ECO:0000250, transferred from A0A0A1HA03). The sequence at position 18 is indeed Histidine (H), consistent with a catalytic base role in glycosyltransferases. The annotation is by similarity rather than direct experimentation, but it is the recorded annotation supporting the key.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 447 residues long, so positions 2113 (A) and 1160 (C) are physically impossible and can be eliminated immediately by a simple length check. Position 83 in this sequence is Aspartic acid (D), which cannot form a covalent acyl-ester intermediate—acyl-ester intermediates require a nucleophilic residue such as Ser, Cys, or Thr; Asp's carboxylate is not nucleophilic enough for this role, eliminating D. Position 18 is Histidine, a well-established catalytic proton acceptor/base in many enzyme families including glycosyltransferases, making B the only chemically and structurally viable option. This elimination chain relies on general protein-chemistry knowledge (nucleophile requirements for acyl-esters, His as a general base) and a trivial sequence-length check, not on memorizing this protein's specific annotation.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate A and C by noting the sequence is only 447 aa, eliminate D because Asp cannot form an acyl-ester intermediate (requires Ser/Cys/Thr), and confirm B because His at position 18 is a chemically sensible proton acceptor. The reasoning uses general biochemistry and a length check, not target-specific memorization."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and C reference positions far exceeding the 447-residue sequence length and are trivially impossible. Option D assigns an acyl-ester intermediate to Asp at position 83, which is chemically implausible. Only B survives elimination and is chemically consistent."
  },
  "important_caveats": [
    "The UniProt active-site annotation at position 18 is by similarity (ECO:0000250 from A0A0A1HA03), not by direct experimental determination on this protein.",
    "The question's distractors A and C (positions 2113 and 1160) are obviously impossible for a 447-residue protein, making the question somewhat easier than a well-calibrated active-site prediction task.",
    "The PSPG motif typical of plant UGTs is usually in the C-terminal region; the His at position 18 in the N-terminal region is annotated as the proton acceptor by similarity transfer, which is a valid but indirect annotation."
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
  "benchmark_sequence_length": 447,
  "benchmark_sequence_sha256": "e9b96404a73576a246ff706f3c603021ade305df43404179546f9de33900d75a",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 447,
  "current_source_sequence_sha256": "e9b96404a73576a246ff706f3c603021ade305df43404179546f9de33900d75a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AAW1IQ05",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19",
  "selected_historical_source_sequence_length": 447,
  "selected_historical_source_sequence_sha256": "e9b96404a73576a246ff706f3c603021ade305df43404179546f9de33900d75a",
  "selected_historical_version": {
    "accession": "A0AAW1IQ05",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GT791_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1IQ05\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:32.727746+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:32.727746+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:32.727746+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"UDP-glucosyl transferase 79T1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoUGT79T1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:32.727746+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0A1HA03\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":18},\"start\":{\"modifier\":\"EXACT\",\"value\":18}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:26:32.727746+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Charge relay\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0A1HA03\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":116},\"start\":{\"modifier\":\"EXACT\",\"value\":116}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:26:32.727746+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":265},\"start\":{\"modifier\":\"EXACT\",\"value\":265}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:26:32.727746+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":323},\"start\":{\"modifier\":\"EXACT\",\"value\":323}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:26:32.727746+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":324},\"start\":{\"modifier\":\"EXACT\",\"value\":324}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:26:32.727746+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":341},\"start\":{\"modifier\":\"EXACT\",\"value\":341}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:26:32.727746+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":346},\"start\":{\"modifier\":\"EXACT\",\"value\":346}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:26:32.727746+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9M156\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58223\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58223\",\"name\":\"UDP\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":349},\"start\":{\"modifier\":\"EXACT\",\"value\":349}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:26:32.727746+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48161.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:32.727746+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7e5d7c440c8ae8ea47ede3a891a67d676cc01d94e61e8c72c81c697c11a8b2f7",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1IQ05.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   GT791_SAPOF             Reviewed;         447 AA.\nAC   A0AAW1IQ05;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=UDP-glucosyl transferase 79T1 {ECO:0000303|PubMed:39043959};\nDE            Short=SoUGT79T1 {ECO:0000303|PubMed:39043959};\nDE            EC=2.4.1.- {ECO:0000269|PubMed:39043959};\nGN   Name=UGT79T1 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11049136m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_09G214900 {ECO:0000312|EMBL:KAK9691727.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:34.746032+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19",
  "url": "https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48161.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:34.746032+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19",
  "url": "https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        18\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A0A1HA03\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:34.746032+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19",
  "url": "https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        116\nFT                   /note=\"Charge relay\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:A0A0A1HA03\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:34.746032+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 96-98",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19",
  "url": "https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         265\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:34.746032+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-102",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19",
  "url": "https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         323\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:34.746032+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 103-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19",
  "url": "https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         324\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:34.746032+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19",
  "url": "https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         341\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:34.746032+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-114",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19",
  "url": "https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         346\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:34.746032+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 115-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19",
  "url": "https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         349\nFT                   /ligand=\"UDP\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58223\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9M156\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:34.746032+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-122",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8338735a50e6923c5727896b3bd6b996442aed5ac91c3323eb6a645c456fff19",
  "url": "https://rest.uniprot.org/unisave/A0AAW1IQ05?format=txt&versions=5"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 49. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
