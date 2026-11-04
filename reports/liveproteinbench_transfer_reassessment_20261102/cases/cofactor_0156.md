# cofactor_0156

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0156.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — heme

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTNELSNAAGASQQGPAASSFSADTPPRTTAGGDVLVLLLIDVAPAARLWGYGRFVAGTTPALGEPGARFAKQLGTGYEGGFGLRPSATRQGLFVLFEDEAAADAFIGRSELVQTYRRNARELCIVKARPYSARGSWDGQKLRVGSPAPVDGPVAALTRASIRPSQAHRFWPNAGPSQDSLERAAGCRLAVGLGEAPFLRQATFSVWDSVAAMDAYARTGAHQRAIVASRDFFSESMFVRFVPLSIEGVWKGRRYG

[Multiple Choices]
A. Mg(2+)
B. NAD(+)
C. heme
D. pyridoxal 5'-phosphate
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

> The matched-sequence UniProt annotation identifies heme and says one heme binds per subunit. Its evidence is transferred by similarity rather than stated as direct experimental evidence for this sequence, so it supports the key with that qualification.

Citations as saved: [C5](#evidence-c5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model could recognize the sequence as belonging to the CrtA-like carotenoid monooxygenase family and use transferable family knowledge that these enzymes are associated with heme. That provides a meaningful basis for choosing heme over NAD(+), Mg(2+), or PLP, although sequence recognition alone may not establish the cofactor with certainty.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The distinction can be made from family-level sequence recognition and learned cofactor patterns; it need not rely on recalling this exact protein's database entry. The inference is probabilistic, not a direct demonstration of catalytic dependence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied annotation supports heme, and no other listed option is comparably supported.


### Important caveats

- The cited cofactor annotation is based on similarity evidence; the excerpts do not independently establish experimentally that heme is essential for catalysis in this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as belonging to the CrtA-like carotenoid monooxygenase family and use transferable family knowledge that these enzymes are associated with heme. That provides a meaningful basis for choosing heme over NAD(+), Mg(2+), or PLP, although sequence recognition alone may not establish the cofactor with certainty.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The distinction can be made from family-level sequence recognition and learned cofactor patterns; it need not rely on recalling this exact protein's database entry. The inference is probabilistic, not a direct demonstration of catalytic dependence."
  },
  "case_id": "cofactor_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies heme and says one heme binds per subunit. Its evidence is transferred by similarity rather than stated as direct experimental evidence for this sequence, so it supports the key with that qualification."
  },
  "important_caveats": [
    "The cited cofactor annotation is based on similarity evidence; the excerpts do not independently establish experimentally that heme is essential for catalysis in this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied annotation supports heme, and no other listed option is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies heme and says one heme binds per subunit. Its evidence is transferred by similarity rather than stated as direct experimental evidence for this sequence, so it supports the key with that qualification.",
    "evidence_ids": ["C5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model could recognize the sequence as belonging to the CrtA-like carotenoid monooxygenase family and use transferable family knowledge that these enzymes are associated with heme. That provides a meaningful basis for choosing heme over NAD(+), Mg(2+), or PLP, although sequence recognition alone may not establish the cofactor with certainty.",
    "missing_item_specific_fact": "",
    "reason": "The distinction can be made from family-level sequence recognition and learned cofactor patterns; it need not rely on recalling this exact protein's database entry. The inference is probabilistic, not a direct demonstration of catalytic dependence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied annotation supports heme, and no other listed option is comparably supported."
  },
  "important_caveats": [
    "The cited cofactor annotation is based on similarity evidence; the excerpts do not independently establish experimentally that heme is essential for catalysis in this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q83YH3, Spheroidene monooxygenase, EC 1.14.15.9) annotates heme as the cofactor (ChEBI:CHEBI:30413, 'Binds 1 heme per subunit'). The evidence code is ECO:0000250 (inferred by similarity to Q3J189, the Rhodobacter capsulatus CrtA homolog), so the heme assignment for this exact protein is a computational transfer rather than direct experimental proof. However, the EC number 1.14.15.9 is experimentally supported (ECO:0000269, PubMed:19136077), and the EC 1.14.15 subclass corresponds to NAD(P)H-dependent monooxygenases, a class that includes heme-dependent (P450-type) enzymes. The annotation is consistent with the family-level biochemistry.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C7](#evidence-c7), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 256-aa sequence lacks a Rossmann-fold motif (GxGxxG) that would indicate NAD+ as a structural cofactor, lacks the characteristic PLP-binding lysine in a conserved context typical of transaminases/decarboxylases, and lacks the DxD or similar metal-chelating motifs associated with Mg2+-dependent kinases or polymerases. The protein's small size (~256 aa) and overall composition are consistent with a compact oxidoreductase/monooxygenase. Among the four choices, heme is the cofactor classically associated with small oxygenation enzymes (P450-type monooxygenases, peroxidases). By elimination of the other three cofactors whose signature motifs are absent, and by the general principle that oxygenation of organic substrates in small enzymes frequently involves a heme prosthetic group, a knowledgeable model can meaningfully favor C over A, B, and D. This is a probabilistic family-level inference rather than a certainty, but it does distinguish the offered alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model can apply elimination reasoning: the sequence shows no NAD+-binding motif, no PLP-binding context, and no Mg2+-chelating motif. The protein's small size and oxidoreductase character are consistent with a heme-dependent monooxygenase. While the CrtA family is not a universally known heme family, the elimination of the other three choices plus the general association of heme with small oxygenation enzymes provides a meaningful, transferable basis to select C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent distinct cofactor classes (metal ion, nicotinamide coenzyme, porphyrin, vitamin B6 derivative) with well-separated biochemical roles. The sequence lacks motifs for NAD+, PLP, and Mg2+, leaving heme as the most defensible choice. No two options are equally supported by the sequence features.


### Important caveats

- The heme cofactor annotation for this exact protein carries evidence code ECO:0000250 (similarity-based transfer from Q3J189), not direct experimental proof for Q83YH3 itself.
- The protein lacks a canonical P450 heme-binding motif (FxxGxxxCxG), so positive identification of heme from the sequence alone is weak; the argument relies more on elimination of the other three choices.
- The EC 1.14.15 subclass is experimentally supported, but the specific cofactor identity within that subclass (heme vs. flavin) is not guaranteed by the EC number alone.
- The reviewer-only source identification (accession Q83YH3, organism, protein name) was not available to the evaluated model; the reasoning must rely on sequence features and general biochemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 256-aa sequence lacks a Rossmann-fold motif (GxGxxG) that would indicate NAD+ as a structural cofactor, lacks the characteristic PLP-binding lysine in a conserved context typical of transaminases/decarboxylases, and lacks the DxD or similar metal-chelating motifs associated with Mg2+-dependent kinases or polymerases. The protein's small size (~256 aa) and overall composition are consistent with a compact oxidoreductase/monooxygenase. Among the four choices, heme is the cofactor classically associated with small oxygenation enzymes (P450-type monooxygenases, peroxidases). By elimination of the other three cofactors whose signature motifs are absent, and by the general principle that oxygenation of organic substrates in small enzymes frequently involves a heme prosthetic group, a knowledgeable model can meaningfully favor C over A, B, and D. This is a probabilistic family-level inference rather than a certainty, but it does distinguish the offered alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model can apply elimination reasoning: the sequence shows no NAD+-binding motif, no PLP-binding context, and no Mg2+-chelating motif. The protein's small size and oxidoreductase character are consistent with a heme-dependent monooxygenase. While the CrtA family is not a universally known heme family, the elimination of the other three choices plus the general association of heme with small oxygenation enzymes provides a meaningful, transferable basis to select C."
  },
  "case_id": "cofactor_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C7",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q83YH3, Spheroidene monooxygenase, EC 1.14.15.9) annotates heme as the cofactor (ChEBI:CHEBI:30413, 'Binds 1 heme per subunit'). The evidence code is ECO:0000250 (inferred by similarity to Q3J189, the Rhodobacter capsulatus CrtA homolog), so the heme assignment for this exact protein is a computational transfer rather than direct experimental proof. However, the EC number 1.14.15.9 is experimentally supported (ECO:0000269, PubMed:19136077), and the EC 1.14.15 subclass corresponds to NAD(P)H-dependent monooxygenases, a class that includes heme-dependent (P450-type) enzymes. The annotation is consistent with the family-level biochemistry."
  },
  "important_caveats": [
    "The heme cofactor annotation for this exact protein carries evidence code ECO:0000250 (similarity-based transfer from Q3J189), not direct experimental proof for Q83YH3 itself.",
    "The protein lacks a canonical P450 heme-binding motif (FxxGxxxCxG), so positive identification of heme from the sequence alone is weak; the argument relies more on elimination of the other three choices.",
    "The EC 1.14.15 subclass is experimentally supported, but the specific cofactor identity within that subclass (heme vs. flavin) is not guaranteed by the EC number alone.",
    "The reviewer-only source identification (accession Q83YH3, organism, protein name) was not available to the evaluated model; the reasoning must rely on sequence features and general biochemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct cofactor classes (metal ion, nicotinamide coenzyme, porphyrin, vitamin B6 derivative) with well-separated biochemical roles. The sequence lacks motifs for NAD+, PLP, and Mg2+, leaving heme as the most defensible choice. No two options are equally supported by the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q83YH3, Spheroidene monooxygenase, EC 1.14.15.9) annotates heme as the cofactor (ChEBI:CHEBI:30413, 'Binds 1 heme per subunit'). The evidence code is ECO:0000250 (inferred by similarity to Q3J189, the Rhodobacter capsulatus CrtA homolog), so the heme assignment for this exact protein is a computational transfer rather than direct experimental proof. However, the EC number 1.14.15.9 is experimentally supported (ECO:0000269, PubMed:19136077), and the EC 1.14.15 subclass corresponds to NAD(P)H-dependent monooxygenases, a class that includes heme-dependent (P450-type) enzymes. The annotation is consistent with the family-level biochemistry.",
    "evidence_ids": ["C5", "C4", "C7", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 256-aa sequence lacks a Rossmann-fold motif (GxGxxG) that would indicate NAD+ as a structural cofactor, lacks the characteristic PLP-binding lysine in a conserved context typical of transaminases/decarboxylases, and lacks the DxD or similar metal-chelating motifs associated with Mg2+-dependent kinases or polymerases. The protein's small size (~256 aa) and overall composition are consistent with a compact oxidoreductase/monooxygenase. Among the four choices, heme is the cofactor classically associated with small oxygenation enzymes (P450-type monooxygenases, peroxidases). By elimination of the other three cofactors whose signature motifs are absent, and by the general principle that oxygenation of organic substrates in small enzymes frequently involves a heme prosthetic group, a knowledgeable model can meaningfully favor C over A, B, and D. This is a probabilistic family-level inference rather than a certainty, but it does distinguish the offered alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A model can apply elimination reasoning: the sequence shows no NAD+-binding motif, no PLP-binding context, and no Mg2+-chelating motif. The protein's small size and oxidoreductase character are consistent with a heme-dependent monooxygenase. While the CrtA family is not a universally known heme family, the elimination of the other three choices plus the general association of heme with small oxygenation enzymes provides a meaningful, transferable basis to select C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent distinct cofactor classes (metal ion, nicotinamide coenzyme, porphyrin, vitamin B6 derivative) with well-separated biochemical roles. The sequence lacks motifs for NAD+, PLP, and Mg2+, leaving heme as the most defensible choice. No two options are equally supported by the sequence features."
  },
  "important_caveats": [
    "The heme cofactor annotation for this exact protein carries evidence code ECO:0000250 (similarity-based transfer from Q3J189), not direct experimental proof for Q83YH3 itself.",
    "The protein lacks a canonical P450 heme-binding motif (FxxGxxxCxG), so positive identification of heme from the sequence alone is weak; the argument relies more on elimination of the other three choices.",
    "The EC 1.14.15 subclass is experimentally supported, but the specific cofactor identity within that subclass (heme vs. flavin) is not guaranteed by the EC number alone.",
    "The reviewer-only source identification (accession Q83YH3, organism, protein name) was not available to the evaluated model; the reasoning must rely on sequence features and general biochemistry."
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
  "benchmark_sequence_length": 256,
  "benchmark_sequence_sha256": "a65db65812f53b7088d2d99b943e650ad4c0d7b76ec0cdde3b3dcfcb5bf162d5",
  "current_entry_audit": {
    "entryVersion": 42,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2003-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 256,
  "current_source_sequence_sha256": "a65db65812f53b7088d2d99b943e650ad4c0d7b76ec0cdde3b3dcfcb5bf162d5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 41,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q83YH3",
  "selected_historical_entry_version": 41,
  "selected_historical_record_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "selected_historical_source_sequence_length": 256,
  "selected_historical_source_sequence_sha256": "a65db65812f53b7088d2d99b943e650ad4c0d7b76ec0cdde3b3dcfcb5bf162d5",
  "selected_historical_version": {
    "accession": "Q83YH3",
    "database": "Swiss-Prot",
    "entryVersion": 41,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "CRTA_RUBGE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q83YH3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":42,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2003-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rhodocyclus gelatinosus\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Betaproteobacteria\",\"Burkholderiales\",\"Sphaerotilaceae\",\"Rubrivivax\"],\"scientificName\":\"Rubrivivax gelatinosus\",\"synonyms\":[\"Rhodopseudomonas gelatinosa\"],\"taxonId\":28068}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"value\":\"Acyclic carotenoid 2-ketolase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Spheroidene/spirilloxanthin monooxygenase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"19136077\",\"source\":\"PubMed\"}],\"value\":\"1.14.15.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"12664193\",\"source\":\"PubMed\"}],\"value\":\"Spheroidene monooxygenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:30413\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3J189\",\"source\":\"UniProtKB\"}],\"name\":\"heme\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q3J189\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 heme per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/13",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Pinta V.\",\"Ouchane S.\",\"Picaud M.\",\"Takaichi S.\",\"Astier C.\",\"Reiss-Husson F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12664193\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00203-003-0538-3\"}],\"citationType\":\"journal article\",\"firstPage\":\"354\",\"id\":\"12664193\",\"journal\":\"Arch. Microbiol.\",\"lastPage\":\"362\",\"publicationDate\":\"2003\",\"title\":\"Characterization of unusual hydroxy- and ketocarotenoids in Rubrivivax gelatinosus: involvement of enzyme CrtF or CrtA.\",\"volume\":\"179\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"S1\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q83YH3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Gerjets T.\",\"Steiger S.\",\"Sandmann G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"19136077\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbalip.2008.12.006\"}],\"citationType\":\"journal article\",\"firstPage\":\"125\",\"id\":\"19136077\",\"journal\":\"Biochim. Biophys. Acta\",\"lastPage\":\"131\",\"publicationDate\":\"2009\",\"title\":\"Catalytic properties of the expressed acyclic carotenoid 2-ketolases from Rhodobacter capsulatus and Rubrivivax gelatinosus.\",\"volume\":\"1791\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"S1\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:31:53.398958+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "415b0c5c709a9871648380468badca26797ea86b5dcd24f2ca939a756b8bbaf9",
  "url": "https://rest.uniprot.org/uniprotkb/Q83YH3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H1",
  "excerpt": "ID   CRTA_RUBGE              Reviewed;         256 AA.\nAC   Q83YH3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2003, sequence version 1.\nDT   28-JAN-2026, entry version 41.\nDE   RecName: Full=Spheroidene monooxygenase {ECO:0000303|PubMed:12664193};\nDE            EC=1.14.15.9 {ECO:0000269|PubMed:19136077};\nDE   AltName: Full=Acyclic carotenoid 2-ketolase {ECO:0000303|PubMed:19136077};\nDE   AltName: Full=Spheroidene/spirilloxanthin monooxygenase {ECO:0000305};\nGN   Name=crtA {ECO:0000303|PubMed:8999844};\nOS   Rubrivivax gelatinosus (Rhodocyclus gelatinosus) (Rhodopseudomonas\nOS   gelatinosa).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Betaproteobacteria;\nOC   Burkholderiales; Sphaerotilaceae; Rubrivivax.\nOX   NCBI_TaxID=28068;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Spheroidene monooxygenase {ECO:0000303|PubMed:12664193};\nDE            EC=1.14.15.9 {ECO:0000269|PubMed:19136077};\nDE   AltName: Full=Acyclic carotenoid 2-ketolase {ECO:0000303|PubMed:19136077};\nDE   AltName: Full=Spheroidene/spirilloxanthin monooxygenase {ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:AAO93123.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=S1;\nRX   PubMed=8999844; DOI=10.1074/jbc.272.3.1670;\nRA   Ouchane S., Picaud M., Vernotte C., Reiss-Husson F., Astier C.;\nRT   \"Pleiotropic effects of puf interposon mutagenesis on carotenoid\nRT   biosynthesis in Rubrivivax gelatinosus. A new gene organization in purple\nRT   bacteria.\";\nRL   J. Biol. Chem. 272:1670-1676(1997).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H4",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=S1;\nRX   PubMed=12664193; DOI=10.1007/s00203-003-0538-3;\nRA   Pinta V., Ouchane S., Picaud M., Takaichi S., Astier C., Reiss-Husson F.;\nRT   \"Characterization of unusual hydroxy- and ketocarotenoids in Rubrivivax\nRT   gelatinosus: involvement of enzyme CrtF or CrtA.\";\nRL   Arch. Microbiol. 179:354-362(2003).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-32",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H5",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=S1;\nRX   PubMed=19136077; DOI=10.1016/j.bbalip.2008.12.006;\nRA   Gerjets T., Steiger S., Sandmann G.;\nRT   \"Catalytic properties of the expressed acyclic carotenoid 2-ketolases from\nRT   Rhodobacter capsulatus and Rubrivivax gelatinosus.\";\nRL   Biochim. Biophys. Acta 1791:125-131(2009).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H6",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=heme; Xref=ChEBI:CHEBI:30413;\nCC         Evidence={ECO:0000250|UniProtKB:Q3J189};\nCC       Note=Binds 1 heme per subunit. {ECO:0000250|UniProtKB:Q3J189};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:55.957280+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 153-156",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4cb02fc77dffc8afd3037d666dd2cb6ddcd919a72332edbea1fb5b05014e9bc4",
  "url": "https://rest.uniprot.org/unisave/Q83YH3?format=txt&versions=41"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 156. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
