# EC_number_0008

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0008.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 2.3.2.27

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPVILNFSSERVLSESELEALRHVGRVSQSEQLVVRGRTMRLHHISFMDSFSVEPVSGGLLDRLSARGHRLLAENLEIQLNRGHTFLQAFRLYMEQSRATPCTRQNVSSAIQNKINSHAFTVSHQDFSCHEQHLNCPITLCIPETGVFVRNAKNSEICSLYDHNALTELIRRNAPHPLSREPFVPEMIVSKDECHFNLIEQYFCILATQNICTRI

[Multiple Choices]
A. 2.3.2.27
B. 2.3.1.193
C. 4.1.1.129
D. 3.2.1.20
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

> The sequence-matched UniProt record assigns EC 2.3.2.27 and gives the corresponding ubiquitin-transfer reaction, citing experimental evidence (ECO:0000269). The archived record also contains this assignment before the stated cutoff. This supports the key, though the primary study was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal Cys/His-rich region is consistent with the conserved domain found in NleG-family bacterial effector E3 ubiquitin ligases. Family-level knowledge links NleG proteins to E3-mediated ubiquitin transfer, matching EC 2.3.2.27 among the choices; the other options describe different reaction classes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference meaningfully distinguishes the ubiquitin-ligase option without needing the exact protein's database record. The sequence pattern alone is not experimental proof, but the alternatives make the family inference informative.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option A matches the inferred E3 ubiquitin-ligase function.


### Important caveats

- The reviewer-only source evidence supports the key but was not available to the evaluated model.
- The cited experimental evidence is reported in the database annotation; the underlying publication was not independently assessed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal Cys/His-rich region is consistent with the conserved domain found in NleG-family bacterial effector E3 ubiquitin ligases. Family-level knowledge links NleG proteins to E3-mediated ubiquitin transfer, matching EC 2.3.2.27 among the choices; the other options describe different reaction classes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference meaningfully distinguishes the ubiquitin-ligase option without needing the exact protein's database record. The sequence pattern alone is not experimental proof, but the alternatives make the family inference informative."
  },
  "case_id": "EC_number_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.3.2.27 and gives the corresponding ubiquitin-transfer reaction, citing experimental evidence (ECO:0000269). The archived record also contains this assignment before the stated cutoff. This supports the key, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only source evidence supports the key but was not available to the evaluated model.",
    "The cited experimental evidence is reported in the database annotation; the underlying publication was not independently assessed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A matches the inferred E3 ubiquitin-ligase function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.3.2.27 and gives the corresponding ubiquitin-transfer reaction, citing experimental evidence (ECO:0000269). The archived record also contains this assignment before the stated cutoff. This supports the key, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal Cys/His-rich region is consistent with the conserved domain found in NleG-family bacterial effector E3 ubiquitin ligases. Family-level knowledge links NleG proteins to E3-mediated ubiquitin transfer, matching EC 2.3.2.27 among the choices; the other options describe different reaction classes.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference meaningfully distinguishes the ubiquitin-ligase option without needing the exact protein's database record. The sequence pattern alone is not experimental proof, but the alternatives make the family inference informative."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option A matches the inferred E3 ubiquitin-ligase function."
  },
  "important_caveats": [
    "The reviewer-only source evidence supports the key but was not available to the evaluated model.",
    "The cited experimental evidence is reported in the database annotation; the underlying publication was not independently assessed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8XAN6 (NleG8 from E. coli O157:H7) is annotated as EC 2.3.2.27 (E3 ubiquitin-protein ligase NleG) with experimental evidence (ECO:0000269|PubMed:36511702). The catalytic activity is documented as S-ubiquitinyl-&#91;E2 ubiquitin-conjugating enzyme&#93;-L-cysteine + &#91;acceptor protein&#93;-L-lysine → &#91;E2&#93;-L-cysteine + N(6)-ubiquitinyl-&#91;acceptor protein&#93;-L-lysine. The sequence matches exactly (215 aa, SHA256 confirmed).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal ~70 residues contain a characteristic cysteine-rich pattern (multiple Cys residues in defined spacing: ...CIPETG...EICSL...CHFNL...YFCIL...NICTRI) consistent with a U-box domain, a well-characterized E3 ubiquitin ligase domain family found across eukaryotic and bacterial proteins. U-box domains are specifically E3 ubiquitin ligases, which map to EC 2.3.2.27. This is transferable family-level knowledge: recognizing the U-box/RING-like cysteine spacing in a small (~215 aa) bacterial protein and knowing that such domains catalyze ubiquitin transfer from E2 to substrate lysine residues. The other options are mechanistically incompatible: 2.3.1.193 is an acyltransferase, 4.1.1.129 is a carboxy-lyase, and 3.2.1.20 is an alpha-galactosidase—none of which would be suggested by a C-terminal cysteine-rich U-box-like fold. The small protein size and bacterial origin are also consistent with the NleG-type effector family of U-box E3 ligases.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The C-terminal U-box domain cysteine pattern is a recognizable family-level feature. Knowledge that U-box domains are E3 ubiquitin ligases (EC 2.3.2.27) is broadly transferable from the many characterized U-box proteins (e.g., PUB, TRIM, CHIP, and bacterial NleG homologs). This meaningfully distinguishes choice A from the mechanistically unrelated alternatives B, C, and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices span entirely different EC classes (E3 ligase, acyltransferase, lyase, glycosidase). The U-box cysteine pattern uniquely points to E3 ubiquitin ligase activity. No other option is mechanistically plausible given the sequence features.


### Important caveats

- The U-box domain in NleG is somewhat degenerate compared to canonical eukaryotic U-box domains; a model must recognize the bacterial variant pattern.
- Recognition of the specific NleG family would strengthen the inference, but the broader U-box/RING E3 ligase family knowledge is sufficient to distinguish the offered choices.
- The annotation evidence is experimental (PubMed:36511702, PDB:6XNJ), confirming the EC assignment is not merely computational.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal ~70 residues contain a characteristic cysteine-rich pattern (multiple Cys residues in defined spacing: ...CIPETG...EICSL...CHFNL...YFCIL...NICTRI) consistent with a U-box domain, a well-characterized E3 ubiquitin ligase domain family found across eukaryotic and bacterial proteins. U-box domains are specifically E3 ubiquitin ligases, which map to EC 2.3.2.27. This is transferable family-level knowledge: recognizing the U-box/RING-like cysteine spacing in a small (~215 aa) bacterial protein and knowing that such domains catalyze ubiquitin transfer from E2 to substrate lysine residues. The other options are mechanistically incompatible: 2.3.1.193 is an acyltransferase, 4.1.1.129 is a carboxy-lyase, and 3.2.1.20 is an alpha-galactosidase—none of which would be suggested by a C-terminal cysteine-rich U-box-like fold. The small protein size and bacterial origin are also consistent with the NleG-type effector family of U-box E3 ligases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The C-terminal U-box domain cysteine pattern is a recognizable family-level feature. Knowledge that U-box domains are E3 ubiquitin ligases (EC 2.3.2.27) is broadly transferable from the many characterized U-box proteins (e.g., PUB, TRIM, CHIP, and bacterial NleG homologs). This meaningfully distinguishes choice A from the mechanistically unrelated alternatives B, C, and D."
  },
  "case_id": "EC_number_0008",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8XAN6 (NleG8 from E. coli O157:H7) is annotated as EC 2.3.2.27 (E3 ubiquitin-protein ligase NleG) with experimental evidence (ECO:0000269|PubMed:36511702). The catalytic activity is documented as S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine → [E2]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine. The sequence matches exactly (215 aa, SHA256 confirmed)."
  },
  "important_caveats": [
    "The U-box domain in NleG is somewhat degenerate compared to canonical eukaryotic U-box domains; a model must recognize the bacterial variant pattern.",
    "Recognition of the specific NleG family would strengthen the inference, but the broader U-box/RING E3 ligase family knowledge is sufficient to distinguish the offered choices.",
    "The annotation evidence is experimental (PubMed:36511702, PDB:6XNJ), confirming the EC assignment is not merely computational."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span entirely different EC classes (E3 ligase, acyltransferase, lyase, glycosidase). The U-box cysteine pattern uniquely points to E3 ubiquitin ligase activity. No other option is mechanistically plausible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0008",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8XAN6 (NleG8 from E. coli O157:H7) is annotated as EC 2.3.2.27 (E3 ubiquitin-protein ligase NleG) with experimental evidence (ECO:0000269|PubMed:36511702). The catalytic activity is documented as S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine → [E2]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine. The sequence matches exactly (215 aa, SHA256 confirmed).",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal ~70 residues contain a characteristic cysteine-rich pattern (multiple Cys residues in defined spacing: ...CIPETG...EICSL...CHFNL...YFCIL...NICTRI) consistent with a U-box domain, a well-characterized E3 ubiquitin ligase domain family found across eukaryotic and bacterial proteins. U-box domains are specifically E3 ubiquitin ligases, which map to EC 2.3.2.27. This is transferable family-level knowledge: recognizing the U-box/RING-like cysteine spacing in a small (~215 aa) bacterial protein and knowing that such domains catalyze ubiquitin transfer from E2 to substrate lysine residues. The other options are mechanistically incompatible: 2.3.1.193 is an acyltransferase, 4.1.1.129 is a carboxy-lyase, and 3.2.1.20 is an alpha-galactosidase—none of which would be suggested by a C-terminal cysteine-rich U-box-like fold. The small protein size and bacterial origin are also consistent with the NleG-type effector family of U-box E3 ligases.",
    "missing_item_specific_fact": "",
    "reason": "The C-terminal U-box domain cysteine pattern is a recognizable family-level feature. Knowledge that U-box domains are E3 ubiquitin ligases (EC 2.3.2.27) is broadly transferable from the many characterized U-box proteins (e.g., PUB, TRIM, CHIP, and bacterial NleG homologs). This meaningfully distinguishes choice A from the mechanistically unrelated alternatives B, C, and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices span entirely different EC classes (E3 ligase, acyltransferase, lyase, glycosidase). The U-box cysteine pattern uniquely points to E3 ubiquitin ligase activity. No other option is mechanistically plausible given the sequence features."
  },
  "important_caveats": [
    "The U-box domain in NleG is somewhat degenerate compared to canonical eukaryotic U-box domains; a model must recognize the bacterial variant pattern.",
    "Recognition of the specific NleG family would strengthen the inference, but the broader U-box/RING E3 ligase family knowledge is sufficient to distinguish the offered choices.",
    "The annotation evidence is experimental (PubMed:36511702, PDB:6XNJ), confirming the EC assignment is not merely computational."
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
  "benchmark_sequence_length": 215,
  "benchmark_sequence_sha256": "ebd4800979a86f7074a5ae32983d282e50962a3735f30deb653b969a18f418ac",
  "current_entry_audit": {
    "entryVersion": 130,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 215,
  "current_source_sequence_sha256": "ebd4800979a86f7074a5ae32983d282e50962a3735f30deb653b969a18f418ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 129,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8XAN6",
  "selected_historical_entry_version": 129,
  "selected_historical_record_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "selected_historical_source_sequence_length": 215,
  "selected_historical_source_sequence_sha256": "ebd4800979a86f7074a5ae32983d282e50962a3735f30deb653b969a18f418ac",
  "selected_historical_version": {
    "accession": "Q8XAN6",
    "database": "Swiss-Prot",
    "entryVersion": 129,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "NLEG8_ECO57",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8XAN6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":130,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Escherichia\"],\"scientificName\":\"Escherichia coli O157:H7\",\"taxonId\":83334}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36511702\",\"source\":\"PubMed\"}],\"value\":\"2.3.2.27\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"E3 ubiquitin-protein ligase NleG\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.2.27\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36511702\",\"source\":\"PubMed\"}],\"name\":\"S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Popov G.\",\"Fiebig-Comyn A.\",\"Syriste L.\",\"Little D.J.\",\"Skarina T.\",\"Stogios P.J.\",\"Birstonas S.\",\"Coombes B.K.\",\"Savchenko A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36511702\"},{\"database\":\"DOI\",\"id\":\"10.1128/iai.00505-22\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0050522\",\"id\":\"36511702\",\"journal\":\"Infect. Immun.\",\"lastPage\":\"e0050522\",\"publicationDate\":\"2023\",\"title\":\"Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for Different Roles during Citrobacter rodentium Infection in Mice.\",\"volume\":\"91\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6XNJ\",\"source\":\"PDB\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.85 ANGSTROMS) OF 206-215 IN COMPLEX WITH HUMAN GOPC\",\"FUNCTION\",\"SUBUNIT\",\"INTERACTION WITH HOST GOPC\",\"SUBCELLULAR LOCATION\",\"DOMAIN\",\"MOTIF\",\"MUTAGENESIS OF ILE-138 AND 212-CYS--ILE-215\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H1",
  "excerpt": "ID   NLEG8_ECO57             Reviewed;         215 AA.\nAC   Q8XAN6; A0A0H3JIV3; A0A6M0JK84; Q7AEM3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2002, sequence version 1.\nDT   28-JAN-2026, entry version 129.\nDE   RecName: Full=E3 ubiquitin-protein ligase NleG {ECO:0000305};\nDE            EC=2.3.2.27 {ECO:0000269|PubMed:36511702};\nGN   Name=nleG8 {ECO:0000303|PubMed:36511702};\nGN   Synonyms=nleG {ECO:0000312|EMBL:BAB35247.1};\nGN   ORFNames=ECs_1824 {ECO:0000312|EMBL:BAB35247.1};\nOS   Escherichia coli O157:H7.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Escherichia.\nOX   NCBI_TaxID=83334;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:42.292045+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "url": "https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=E3 ubiquitin-protein ligase NleG {ECO:0000305};\nDE            EC=2.3.2.27 {ECO:0000269|PubMed:36511702};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:42.292045+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "url": "https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:6XNJ}\nRP   X-RAY CRYSTALLOGRAPHY (1.85 ANGSTROMS) OF 206-215 IN COMPLEX WITH HUMAN\nRP   GOPC, FUNCTION, SUBUNIT, INTERACTION WITH HOST GOPC, SUBCELLULAR LOCATION,\nRP   DOMAIN, MOTIF, AND MUTAGENESIS OF ILE-138 AND 212-CYS--ILE-215.\nRX   PubMed=36511702; DOI=10.1128/iai.00505-22;\nRA   Popov G., Fiebig-Comyn A., Syriste L., Little D.J., Skarina T.,\nRA   Stogios P.J., Birstonas S., Coombes B.K., Savchenko A.;\nRT   \"Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for\nRT   Different Roles during Citrobacter rodentium Infection in Mice.\";\nRL   Infect. Immun. 91:e0050522-e0050522(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:42.292045+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "url": "https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine +\nCC         [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-\nCC         cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.;\nCC         EC=2.3.2.27; Evidence={ECO:0000269|PubMed:36511702};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:42.292045+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "url": "https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 8. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
