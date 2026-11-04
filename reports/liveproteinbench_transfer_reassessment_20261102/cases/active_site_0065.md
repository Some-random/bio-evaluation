# active_site_0065

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0065.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 143 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MADKETLLKLREDFKMQNKSVFILGASGETGKVLLKEILGQNLFSKVTLIGRRKLTFEEEAYNNVNQEVVDFEKLDEYAPAFQGHDVGFCCLGTTRRKAGADGFVRVDRDYVLKSAELAKAGGCKHFNLLSSRGADKSSSFLYLQVKGEVEAKVEELKFDRLSVFRPGVLLCDRQESRPGEWLARKFFGSLPDSWASGYAVPVVTVVRAMLNNLVSPGSGQMELLENKAILHLGKDSDGPKL

[Multiple Choices]
A. Position 1978 (For beta-ketoacyl synthase 2 activity)
B. Position 436 (Proton acceptor)
C. Position 143 (Proton acceptor)
D. Position 12 (Proton acceptor)
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

> The sequence-matched UniProt annotation identifies position 143 as the proton acceptor. Its evidence code indicates transfer by similarity, not direct experimental validation. Position 143 is Tyr in the supplied sequence, consistent with a catalytic role.

Citations as saved: [H2](#evidence-h2), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence has Tyr143 followed by three residues and Lys147, a recognizable catalytic Tyr-X3-Lys pattern found in NAD(P)-dependent oxidoreductase families. That transferable motif makes position 143 a credible catalytic proton-handling residue; position 12 is Glu and does not match the motif. Positions 436 and 1978 exceed the 242-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and a family-level catalytic motif meaningfully favor C over the valid-length alternative D, without needing to recall this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered positions, the sequence motif and the similarity-based annotation both support position 143; the other positions do not provide an equally credible alternative.


### Important caveats

- The database annotation is similarity-derived rather than direct experimental evidence for this exact protein.
- The annotation also lists position 147 as an active-site residue, but it is not an offered choice.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence has Tyr143 followed by three residues and Lys147, a recognizable catalytic Tyr-X3-Lys pattern found in NAD(P)-dependent oxidoreductase families. That transferable motif makes position 143 a credible catalytic proton-handling residue; position 12 is Glu and does not match the motif. Positions 436 and 1978 exceed the 242-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and a family-level catalytic motif meaningfully favor C over the valid-length alternative D, without needing to recall this exact protein's annotation."
  },
  "case_id": "active_site_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 143 as the proton acceptor. Its evidence code indicates transfer by similarity, not direct experimental validation. Position 143 is Tyr in the supplied sequence, consistent with a catalytic role."
  },
  "important_caveats": [
    "The database annotation is similarity-derived rather than direct experimental evidence for this exact protein.",
    "The annotation also lists position 147 as an active-site residue, but it is not an offered choice."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered positions, the sequence motif and the similarity-based annotation both support position 143; the other positions do not provide an equally credible alternative."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 143 as the proton acceptor. Its evidence code indicates transfer by similarity, not direct experimental validation. Position 143 is Tyr in the supplied sequence, consistent with a catalytic role.",
    "evidence_ids": ["H2", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence has Tyr143 followed by three residues and Lys147, a recognizable catalytic Tyr-X3-Lys pattern found in NAD(P)-dependent oxidoreductase families. That transferable motif makes position 143 a credible catalytic proton-handling residue; position 12 is Glu and does not match the motif. Positions 436 and 1978 exceed the 242-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and a family-level catalytic motif meaningfully favor C over the valid-length alternative D, without needing to recall this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered positions, the sequence motif and the similarity-based annotation both support position 143; the other positions do not provide an equally credible alternative."
  },
  "important_caveats": [
    "The database annotation is similarity-derived rather than direct experimental evidence for this exact protein.",
    "The annotation also lists position 147 as an active-site residue, but it is not an offered choice."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B0BNF8 (Protein HTATIP2, Rattus norvegicus, 242 AA) annotates position 143 as 'Proton acceptor' active site (evidence ECO:0000250, by similarity to Q9BUP3). The provided sequence matches the source entry. Position 143 in the sequence is Tyrosine (Y), consistent with the SDR catalytic tyrosine. The annotation is computational (similarity-based) rather than experimentally derived, but it is the recorded annotation and is consistent with the SDR family mechanism.

Citations as saved: [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 242 amino acids long, immediately eliminating options A (position 1978) and B (position 436) as impossible. The sequence contains 'GASGETGKV' at positions 25-33, a GxGxxG Rossmann fold motif diagnostic of NAD(P)H-binding enzymes, particularly the short-chain dehydrogenase/reductase (SDR) superfamily. The region around positions 140-147 reads 'SSSFLYLQVK', containing the canonical SDR catalytic triad Ser(140)-Tyr(143)-Lys(147). In SDRs, the tyrosine of this triad is the well-established proton acceptor/donor in the catalytic mechanism (transferring a hydride from NAD(P)H to the substrate carbonyl). Position 12 is Glutamic acid (E), which is not a recognized proton acceptor in SDR catalysis. Thus, family-level SDR knowledge (Rossmann fold + S-Y-K triad → Tyr as proton acceptor) meaningfully distinguishes C from D without needing the specific database annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing the SDR family signature (Rossmann fold motif + S-Y-K catalytic triad) can apply the well-known mechanism that the tyrosine in this triad serves as the proton acceptor. Combined with the trivial elimination of A and B (positions beyond the 242-residue protein), this leaves C as the only biochemically coherent answer. This is standard transferable knowledge about the SDR protein family.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B reference positions (1978, 436) that exceed the protein length of 242 residues and are physically impossible. Option D (position 12, Glutamic acid) is not a recognized proton acceptor in the SDR catalytic mechanism. Only option C is viable given both the sequence length constraint and the SDR family mechanism.


### Important caveats

- The UniProt annotation for position 143 is computational (ECO:0000250, by similarity to human Q9BUP3), not experimental. However, the SDR family mechanism independently supports this assignment.
- The protein is annotated as 'Protein HTATIP2' but its sequence and annotations (NADPH binding, SDR catalytic triad) suggest it belongs to the SDR/reductase superfamily, which may reflect an annotation discrepancy or dual function.
- Options A and B are trivially eliminated by protein length, making the effective discrimination between C and D dependent on SDR family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 242 amino acids long, immediately eliminating options A (position 1978) and B (position 436) as impossible. The sequence contains 'GASGETGKV' at positions 25-33, a GxGxxG Rossmann fold motif diagnostic of NAD(P)H-binding enzymes, particularly the short-chain dehydrogenase/reductase (SDR) superfamily. The region around positions 140-147 reads 'SSSFLYLQVK', containing the canonical SDR catalytic triad Ser(140)-Tyr(143)-Lys(147). In SDRs, the tyrosine of this triad is the well-established proton acceptor/donor in the catalytic mechanism (transferring a hydride from NAD(P)H to the substrate carbonyl). Position 12 is Glutamic acid (E), which is not a recognized proton acceptor in SDR catalysis. Thus, family-level SDR knowledge (Rossmann fold + S-Y-K triad → Tyr as proton acceptor) meaningfully distinguishes C from D without needing the specific database annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the SDR family signature (Rossmann fold motif + S-Y-K catalytic triad) can apply the well-known mechanism that the tyrosine in this triad serves as the proton acceptor. Combined with the trivial elimination of A and B (positions beyond the 242-residue protein), this leaves C as the only biochemically coherent answer. This is standard transferable knowledge about the SDR protein family."
  },
  "case_id": "active_site_0065",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B0BNF8 (Protein HTATIP2, Rattus norvegicus, 242 AA) annotates position 143 as 'Proton acceptor' active site (evidence ECO:0000250, by similarity to Q9BUP3). The provided sequence matches the source entry. Position 143 in the sequence is Tyrosine (Y), consistent with the SDR catalytic tyrosine. The annotation is computational (similarity-based) rather than experimentally derived, but it is the recorded annotation and is consistent with the SDR family mechanism."
  },
  "important_caveats": [
    "The UniProt annotation for position 143 is computational (ECO:0000250, by similarity to human Q9BUP3), not experimental. However, the SDR family mechanism independently supports this assignment.",
    "The protein is annotated as 'Protein HTATIP2' but its sequence and annotations (NADPH binding, SDR catalytic triad) suggest it belongs to the SDR/reductase superfamily, which may reflect an annotation discrepancy or dual function.",
    "Options A and B are trivially eliminated by protein length, making the effective discrimination between C and D dependent on SDR family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B reference positions (1978, 436) that exceed the protein length of 242 residues and are physically impossible. Option D (position 12, Glutamic acid) is not a recognized proton acceptor in the SDR catalytic mechanism. Only option C is viable given both the sequence length constraint and the SDR family mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0065",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B0BNF8 (Protein HTATIP2, Rattus norvegicus, 242 AA) annotates position 143 as 'Proton acceptor' active site (evidence ECO:0000250, by similarity to Q9BUP3). The provided sequence matches the source entry. Position 143 in the sequence is Tyrosine (Y), consistent with the SDR catalytic tyrosine. The annotation is computational (similarity-based) rather than experimentally derived, but it is the recorded annotation and is consistent with the SDR family mechanism.",
    "evidence_ids": ["C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 242 amino acids long, immediately eliminating options A (position 1978) and B (position 436) as impossible. The sequence contains 'GASGETGKV' at positions 25-33, a GxGxxG Rossmann fold motif diagnostic of NAD(P)H-binding enzymes, particularly the short-chain dehydrogenase/reductase (SDR) superfamily. The region around positions 140-147 reads 'SSSFLYLQVK', containing the canonical SDR catalytic triad Ser(140)-Tyr(143)-Lys(147). In SDRs, the tyrosine of this triad is the well-established proton acceptor/donor in the catalytic mechanism (transferring a hydride from NAD(P)H to the substrate carbonyl). Position 12 is Glutamic acid (E), which is not a recognized proton acceptor in SDR catalysis. Thus, family-level SDR knowledge (Rossmann fold + S-Y-K triad → Tyr as proton acceptor) meaningfully distinguishes C from D without needing the specific database annotation.",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the SDR family signature (Rossmann fold motif + S-Y-K catalytic triad) can apply the well-known mechanism that the tyrosine in this triad serves as the proton acceptor. Combined with the trivial elimination of A and B (positions beyond the 242-residue protein), this leaves C as the only biochemically coherent answer. This is standard transferable knowledge about the SDR protein family."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B reference positions (1978, 436) that exceed the protein length of 242 residues and are physically impossible. Option D (position 12, Glutamic acid) is not a recognized proton acceptor in the SDR catalytic mechanism. Only option C is viable given both the sequence length constraint and the SDR family mechanism."
  },
  "important_caveats": [
    "The UniProt annotation for position 143 is computational (ECO:0000250, by similarity to human Q9BUP3), not experimental. However, the SDR family mechanism independently supports this assignment.",
    "The protein is annotated as 'Protein HTATIP2' but its sequence and annotations (NADPH binding, SDR catalytic triad) suggest it belongs to the SDR/reductase superfamily, which may reflect an annotation discrepancy or dual function.",
    "Options A and B are trivially eliminated by protein length, making the effective discrimination between C and D dependent on SDR family knowledge."
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
  "benchmark_sequence_length": 242,
  "benchmark_sequence_sha256": "84a71691c15d738414b9418bb4ec9b787bd7004f741e211117cb2d48da890b5f",
  "current_entry_audit": {
    "entryVersion": 119,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2008-02-26",
    "sequenceVersion": 1
  },
  "current_record_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 242,
  "current_source_sequence_sha256": "84a71691c15d738414b9418bb4ec9b787bd7004f741e211117cb2d48da890b5f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 117,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B0BNF8",
  "selected_historical_entry_version": 117,
  "selected_historical_record_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "selected_historical_source_sequence_length": 242,
  "selected_historical_source_sequence_sha256": "84a71691c15d738414b9418bb4ec9b787bd7004f741e211117cb2d48da890b5f",
  "selected_historical_version": {
    "accession": "B0BNF8",
    "database": "Swiss-Prot",
    "entryVersion": 117,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HTAI2_RAT",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B0BNF8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":119,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2008-02-26\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rat\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000002494\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Muridae\",\"Murinae\",\"Rattus\"],\"scientificName\":\"Rattus norvegicus\",\"taxonId\":10116}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Protein HTATIP2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":143},\"start\":{\"modifier\":\"EXACT\",\"value\":143}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":147},\"start\":{\"modifier\":\"EXACT\",\"value\":147}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57783\",\"name\":\"NADPH\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":27},\"start\":{\"modifier\":\"EXACT\",\"value\":27}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57783\",\"name\":\"NADPH\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":28},\"start\":{\"modifier\":\"EXACT\",\"value\":28}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57783\",\"name\":\"NADPH\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":29},\"start\":{\"modifier\":\"EXACT\",\"value\":29}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57783\",\"name\":\"NADPH\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":30},\"start\":{\"modifier\":\"EXACT\",\"value\":30}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57783\",\"name\":\"NADPH\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":52},\"start\":{\"modifier\":\"EXACT\",\"value\":52}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57783\",\"name\":\"NADPH\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":53},\"start\":{\"modifier\":\"EXACT\",\"value\":53}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57783\",\"name\":\"NADPH\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":92},\"start\":{\"modifier\":\"EXACT\",\"value\":92}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/11",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C14",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57783\",\"name\":\"NADPH\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":93},\"start\":{\"modifier\":\"EXACT\",\"value\":93}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/12",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C15

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C15",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57783\",\"name\":\"NADPH\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":143},\"start\":{\"modifier\":\"EXACT\",\"value\":143}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/13",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C16

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C16",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57783\",\"name\":\"NADPH\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":147},\"start\":{\"modifier\":\"EXACT\",\"value\":147}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/14",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C17

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C17",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57783\",\"name\":\"NADPH\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":170},\"start\":{\"modifier\":\"EXACT\",\"value\":170}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/15",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence C18

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B0BNF8.json)

```json
{
  "evidence_id": "C18",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9BUP3\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:57783\",\"name\":\"NADPH\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":178},\"start\":{\"modifier\":\"EXACT\",\"value\":178}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/16",
  "retrieved_utc": "2026-11-02T04:27:12.867856+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "5bc2319a85294d9bd0de3c58ce0c0ccfe250318e8fba8d882b03e077196791bb",
  "url": "https://rest.uniprot.org/uniprotkb/B0BNF8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H1",
  "excerpt": "ID   HTAI2_RAT               Reviewed;         242 AA.\nAC   B0BNF8; A0A8I6AEZ6; G3V8Y4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   26-FEB-2008, sequence version 1.\nDT   28-JAN-2026, entry version 117.\nDE   RecName: Full=Protein HTATIP2 {ECO:0000305};\nGN   Name=Htatip2 {ECO:0000312|RGD:1309941};\nOS   Rattus norvegicus (Rat).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea; Muridae;\nOC   Murinae; Rattus.\nOX   NCBI_TaxID=10116 {ECO:0000312|Proteomes:UP000002494};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H2",
  "excerpt": "FT   ACT_SITE        143\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 157-159",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        147\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 160-161",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         27\nFT                   /ligand=\"NADPH\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57783\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 162-165",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         28\nFT                   /ligand=\"NADPH\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57783\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 166-169",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         29\nFT                   /ligand=\"NADPH\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57783\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 170-173",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         30\nFT                   /ligand=\"NADPH\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57783\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 174-177",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         52\nFT                   /ligand=\"NADPH\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57783\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 178-181",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         53\nFT                   /ligand=\"NADPH\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57783\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 182-185",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         92\nFT                   /ligand=\"NADPH\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57783\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 186-189",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         93\nFT                   /ligand=\"NADPH\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57783\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 190-193",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H12

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H12",
  "excerpt": "FT   BINDING         143\nFT                   /ligand=\"NADPH\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57783\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 194-197",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H13

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H13",
  "excerpt": "FT   BINDING         147\nFT                   /ligand=\"NADPH\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57783\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 198-201",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H14

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H14",
  "excerpt": "FT   BINDING         170\nFT                   /ligand=\"NADPH\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57783\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 202-205",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

### Evidence H15

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117)

```json
{
  "entry_version": 117,
  "evidence_id": "H15",
  "excerpt": "FT   BINDING         178\nFT                   /ligand=\"NADPH\"\nFT                   /ligand_id=\"ChEBI:CHEBI:57783\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:Q9BUP3\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:16.468432+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 206-209",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c91b6ccd39bbf56d358216a7ae481826bd770d8f3f708b47271a14d3c7924ec0",
  "url": "https://rest.uniprot.org/unisave/B0BNF8?format=txt&versions=117"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 65. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
