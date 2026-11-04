# active_site_0026

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0026.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 131 (Charge relay system)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKFLCLHGAYGNIPAFRVQLGPMIDALEFDGSASFEFIQGRVSVVPPPGFESYFGPAPHYRFLKDRGEAEASAVEGIRVFPEAETPEDALRALMPRDDMEIGFADARGLALEQLYEALDADPEISGIIGYSEGASAAATLVYDEQERMRSEGYVPRIKAAIFFMGWPALTAENVPALSDEVENLLEVPSLHIVGANDPYKDGALALYNIFDDNMAVFFDSAGGHTIPRHGKLLQELVSAVKDLIADVPEDNSADLLAPAVTGKRLDSAVDIPNLSFLKNEDA

[Multiple Choices]
A. Position 1334 (Proton acceptor; for dehydratase activity)
B. Position 131 (Charge relay)
C. Position 131 (Charge relay system)
D. Position 1045 (Proton acceptor; for dehydratase activity)
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

> The sequence-matched UniProt annotation identifies position 131 as an active-site charge relay system. This is consistent with the sequence’s G-x-S-x-G motif at positions 129–133, with Ser131 as the likely catalytic serine. The annotation is transferred by similarity rather than presented as direct experimental evidence.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the classic G-x-S-x-G motif of many serine hydrolases at positions 129–133; Ser131 is the likely catalytic serine, and serine-hydrolase catalytic residues participate in a charge-relay system. This supports the position and description in choices B and C, while choices A and D give positions outside the 282-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A conserved catalytic motif and transferable serine-hydrolase knowledge provide a meaningful inference about the active-site position without needing the exact protein’s database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Both choices name position 131 and describe a charge relay; “charge relay” and “charge relay system” do not establish a meaningful scientific distinction.


### Important caveats

- The source annotation is based on evidence transferred from a related protein, not direct experimental evidence in the supplied excerpts.
- The duplicate choices prevent a unique selection between B and C.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the classic G-x-S-x-G motif of many serine hydrolases at positions 129–133; Ser131 is the likely catalytic serine, and serine-hydrolase catalytic residues participate in a charge-relay system. This supports the position and description in choices B and C, while choices A and D give positions outside the 282-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A conserved catalytic motif and transferable serine-hydrolase knowledge provide a meaningful inference about the active-site position without needing the exact protein’s database record."
  },
  "case_id": "active_site_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 131 as an active-site charge relay system. This is consistent with the sequence’s G-x-S-x-G motif at positions 129–133, with Ser131 as the likely catalytic serine. The annotation is transferred by similarity rather than presented as direct experimental evidence."
  },
  "important_caveats": [
    "The source annotation is based on evidence transferred from a related protein, not direct experimental evidence in the supplied excerpts.",
    "The duplicate choices prevent a unique selection between B and C."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Both choices name position 131 and describe a charge relay; “charge relay” and “charge relay system” do not establish a meaningful scientific distinction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 131 as an active-site charge relay system. This is consistent with the sequence’s G-x-S-x-G motif at positions 129–133, with Ser131 as the likely catalytic serine. The annotation is transferred by similarity rather than presented as direct experimental evidence.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the classic G-x-S-x-G motif of many serine hydrolases at positions 129–133; Ser131 is the likely catalytic serine, and serine-hydrolase catalytic residues participate in a charge-relay system. This supports the position and description in choices B and C, while choices A and D give positions outside the 282-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "A conserved catalytic motif and transferable serine-hydrolase knowledge provide a meaningful inference about the active-site position without needing the exact protein’s database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Both choices name position 131 and describe a charge relay; “charge relay” and “charge relay system” do not establish a meaningful scientific distinction."
  },
  "important_caveats": [
    "The source annotation is based on evidence transferred from a related protein, not direct experimental evidence in the supplied excerpts.",
    "The duplicate choices prevent a unique selection between B and C."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A385XI13 (Esterase 1, EST1, from Aureobasidium melanogenum) annotates an Active site at position 131 with the description 'Charge relay system' (evidence ECO:0000250, inferred by similarity from P38777, a carboxylesterase). The author's expected answer C ('Position 131 (Charge relay system)') matches this annotation exactly. The evidence is computational (similarity-based transfer), not directly experimental, but the annotation exists and is consistent with the protein's esterase function (EC 3.1.2.-) and the G-Y-S motif at positions 129-131 in the sequence.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The protein is 282 amino acids long, immediately eliminating options A (position 1334) and D (position 1045) as physically impossible. The sequence around position 131 reads ...G(129)-Y(130)-S(131)-E(132)-G(133)..., a G-Y-S motif characteristic of the catalytic serine in α/β-hydrolase-fold serine esterases (the canonical GXSXG motif). The protein is annotated as an esterase (EC 3.1.2.-), consistent with a serine-hydrolase catalytic mechanism. In serine hydrolases, the catalytic triad (Ser-His-Asp/Glu) operates via what Blow and Steitz (1970) termed the 'charge relay system'—the standard, complete biochemical term for this mechanism. Option C uses this canonical full term 'Charge relay system,' while option B uses the truncated 'Charge relay,' which is an incomplete rendering of the standard term. A model familiar with serine-hydrolase mechanism terminology from textbooks and the broader literature would recognize 'charge relay system' as the established, complete descriptor.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Eliminating A and D requires only counting the sequence length. Identifying position 131 as catalytic relies on recognizing the GYS motif and esterase context, both transferable knowledge. Distinguishing C from B rests on knowing that the standard biochemical term for the catalytic triad mechanism is 'charge relay system' (the full term from Blow & Steitz), not merely 'charge relay.' This is general terminology knowledge applicable to all serine hydrolases, not a fact unique to this protein. However, the B-vs-C distinction is extremely fine and primarily a terminology-completeness issue rather than a substantive biological difference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "C"
]
```

> Options B ('Charge relay') and C ('Charge relay system') describe the same biological mechanism. 'Charge relay' is a widely used shorthand for 'charge relay system' in the biochemistry literature, and many sources use them interchangeably. The distinction is essentially the presence or absence of the word 'system,' which is a UniProt controlled-vocabulary convention rather than a substantive biological difference. A knowledgeable model could reasonably consider both B and C as describing the same catalytic mechanism, making the choice between them dependent on exact annotation wording rather than biological reasoning.


### Important caveats

- The active-site annotation carries evidence code ECO:0000250 (inferred by similarity from UniProtKB:P38777, a carboxylesterase), meaning it is a computational transfer, not a direct experimental determination for this specific protein.
- The B-vs-C distinction hinges on the presence of the word 'system' in the annotation term. While 'charge relay system' is the canonical full term in biochemistry, 'charge relay' is common shorthand and both are understood to refer to the same Ser-His-Asp/Glu mechanism.
- The protein is only 282 residues long, making options A (position 1334) and D (position 1045) trivially eliminable, which reduces the effective difficulty of the question to the B-vs-C distinction.
- The UniProt annotation was first released in 2026 (entry version 13, 28-Jan-2026), so the annotation postdates the sequence deposition (2018). The author's source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The protein is 282 amino acids long, immediately eliminating options A (position 1334) and D (position 1045) as physically impossible. The sequence around position 131 reads ...G(129)-Y(130)-S(131)-E(132)-G(133)..., a G-Y-S motif characteristic of the catalytic serine in α/β-hydrolase-fold serine esterases (the canonical GXSXG motif). The protein is annotated as an esterase (EC 3.1.2.-), consistent with a serine-hydrolase catalytic mechanism. In serine hydrolases, the catalytic triad (Ser-His-Asp/Glu) operates via what Blow and Steitz (1970) termed the 'charge relay system'—the standard, complete biochemical term for this mechanism. Option C uses this canonical full term 'Charge relay system,' while option B uses the truncated 'Charge relay,' which is an incomplete rendering of the standard term. A model familiar with serine-hydrolase mechanism terminology from textbooks and the broader literature would recognize 'charge relay system' as the established, complete descriptor.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Eliminating A and D requires only counting the sequence length. Identifying position 131 as catalytic relies on recognizing the GYS motif and esterase context, both transferable knowledge. Distinguishing C from B rests on knowing that the standard biochemical term for the catalytic triad mechanism is 'charge relay system' (the full term from Blow & Steitz), not merely 'charge relay.' This is general terminology knowledge applicable to all serine hydrolases, not a fact unique to this protein. However, the B-vs-C distinction is extremely fine and primarily a terminology-completeness issue rather than a substantive biological difference."
  },
  "case_id": "active_site_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A385XI13 (Esterase 1, EST1, from Aureobasidium melanogenum) annotates an Active site at position 131 with the description 'Charge relay system' (evidence ECO:0000250, inferred by similarity from P38777, a carboxylesterase). The author's expected answer C ('Position 131 (Charge relay system)') matches this annotation exactly. The evidence is computational (similarity-based transfer), not directly experimental, but the annotation exists and is consistent with the protein's esterase function (EC 3.1.2.-) and the G-Y-S motif at positions 129-131 in the sequence."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000250 (inferred by similarity from UniProtKB:P38777, a carboxylesterase), meaning it is a computational transfer, not a direct experimental determination for this specific protein.",
    "The B-vs-C distinction hinges on the presence of the word 'system' in the annotation term. While 'charge relay system' is the canonical full term in biochemistry, 'charge relay' is common shorthand and both are understood to refer to the same Ser-His-Asp/Glu mechanism.",
    "The protein is only 282 residues long, making options A (position 1334) and D (position 1045) trivially eliminable, which reduces the effective difficulty of the question to the B-vs-C distinction.",
    "The UniProt annotation was first released in 2026 (entry version 13, 28-Jan-2026), so the annotation postdates the sequence deposition (2018). The author's source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "C"
    ],
    "reason": "Options B ('Charge relay') and C ('Charge relay system') describe the same biological mechanism. 'Charge relay' is a widely used shorthand for 'charge relay system' in the biochemistry literature, and many sources use them interchangeably. The distinction is essentially the presence or absence of the word 'system,' which is a UniProt controlled-vocabulary convention rather than a substantive biological difference. A knowledgeable model could reasonably consider both B and C as describing the same catalytic mechanism, making the choice between them dependent on exact annotation wording rather than biological reasoning."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A385XI13 (Esterase 1, EST1, from Aureobasidium melanogenum) annotates an Active site at position 131 with the description 'Charge relay system' (evidence ECO:0000250, inferred by similarity from P38777, a carboxylesterase). The author's expected answer C ('Position 131 (Charge relay system)') matches this annotation exactly. The evidence is computational (similarity-based transfer), not directly experimental, but the annotation exists and is consistent with the protein's esterase function (EC 3.1.2.-) and the G-Y-S motif at positions 129-131 in the sequence.",
    "evidence_ids": ["C5", "H3", "C4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The protein is 282 amino acids long, immediately eliminating options A (position 1334) and D (position 1045) as physically impossible. The sequence around position 131 reads ...G(129)-Y(130)-S(131)-E(132)-G(133)..., a G-Y-S motif characteristic of the catalytic serine in α/β-hydrolase-fold serine esterases (the canonical GXSXG motif). The protein is annotated as an esterase (EC 3.1.2.-), consistent with a serine-hydrolase catalytic mechanism. In serine hydrolases, the catalytic triad (Ser-His-Asp/Glu) operates via what Blow and Steitz (1970) termed the 'charge relay system'—the standard, complete biochemical term for this mechanism. Option C uses this canonical full term 'Charge relay system,' while option B uses the truncated 'Charge relay,' which is an incomplete rendering of the standard term. A model familiar with serine-hydrolase mechanism terminology from textbooks and the broader literature would recognize 'charge relay system' as the established, complete descriptor.",
    "missing_item_specific_fact": "",
    "reason": "Eliminating A and D requires only counting the sequence length. Identifying position 131 as catalytic relies on recognizing the GYS motif and esterase context, both transferable knowledge. Distinguishing C from B rests on knowing that the standard biochemical term for the catalytic triad mechanism is 'charge relay system' (the full term from Blow & Steitz), not merely 'charge relay.' This is general terminology knowledge applicable to all serine hydrolases, not a fact unique to this protein. However, the B-vs-C distinction is extremely fine and primarily a terminology-completeness issue rather than a substantive biological difference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "C"],
    "reason": "Options B ('Charge relay') and C ('Charge relay system') describe the same biological mechanism. 'Charge relay' is a widely used shorthand for 'charge relay system' in the biochemistry literature, and many sources use them interchangeably. The distinction is essentially the presence or absence of the word 'system,' which is a UniProt controlled-vocabulary convention rather than a substantive biological difference. A knowledgeable model could reasonably consider both B and C as describing the same catalytic mechanism, making the choice between them dependent on exact annotation wording rather than biological reasoning."
  },
  "important_caveats": [
    "The active-site annotation carries evidence code ECO:0000250 (inferred by similarity from UniProtKB:P38777, a carboxylesterase), meaning it is a computational transfer, not a direct experimental determination for this specific protein.",
    "The B-vs-C distinction hinges on the presence of the word 'system' in the annotation term. While 'charge relay system' is the canonical full term in biochemistry, 'charge relay' is common shorthand and both are understood to refer to the same Ser-His-Asp/Glu mechanism.",
    "The protein is only 282 residues long, making options A (position 1334) and D (position 1045) trivially eliminable, which reduces the effective difficulty of the question to the B-vs-C distinction.",
    "The UniProt annotation was first released in 2026 (entry version 13, 28-Jan-2026), so the annotation postdates the sequence deposition (2018). The author's source snapshot is unknown."
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
  "benchmark_sequence_length": 282,
  "benchmark_sequence_sha256": "6f138603563b5b34481d3d083d9e6174741b3d962eda8324cf8e0e4d8c656576",
  "current_entry_audit": {
    "entryVersion": 14,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2018-12-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0604cd5410cd5850ed1061ec3c5b369f42c7da183cd38472972d9c4ba536b805",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 282,
  "current_source_sequence_sha256": "6f138603563b5b34481d3d083d9e6174741b3d962eda8324cf8e0e4d8c656576",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 13,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A385XI13",
  "selected_historical_entry_version": 13,
  "selected_historical_record_sha256": "2adf58d8fd74514947bfa0569f28f495b9be466e1ab51987b05e8007a9a288ca",
  "selected_historical_source_sequence_length": 282,
  "selected_historical_source_sequence_sha256": "6f138603563b5b34481d3d083d9e6174741b3d962eda8324cf8e0e4d8c656576",
  "selected_historical_version": {
    "accession": "A0A385XI13",
    "database": "Swiss-Prot",
    "entryVersion": 13,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "EST1_AURME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI13.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A385XI13\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:45.462174+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0604cd5410cd5850ed1061ec3c5b369f42c7da183cd38472972d9c4ba536b805",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI13.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI13.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":14,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2018-12-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:45.462174+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0604cd5410cd5850ed1061ec3c5b369f42c7da183cd38472972d9c4ba536b805",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI13.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI13.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Aureobasidium pullulans var. melanogenum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Dothideomycetidae\",\"Dothideales\",\"Saccotheciaceae\",\"Aureobasidium\"],\"scientificName\":\"Aureobasidium melanogenum\",\"taxonId\":46634}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:45.462174+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0604cd5410cd5850ed1061ec3c5b369f42c7da183cd38472972d9c4ba536b805",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI13.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI13.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"Liamocins biosynthesis cluster protein EST1\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"3.1.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"Esterase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32003433\",\"source\":\"PubMed\"}],\"value\":\"EST1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:45.462174+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0604cd5410cd5850ed1061ec3c5b369f42c7da183cd38472972d9c4ba536b805",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI13.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI13.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Charge relay system\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P38777\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":131},\"start\":{\"modifier\":\"EXACT\",\"value\":131}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:45.462174+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0604cd5410cd5850ed1061ec3c5b369f42c7da183cd38472972d9c4ba536b805",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI13.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A385XI13.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Xue S.J.\",\"Liu G.L.\",\"Chi Z.\",\"Gao Z.C.\",\"Hu Z.\",\"Chi Z.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32003433\"},{\"database\":\"DOI\",\"id\":\"10.1042/bcj20190922\"}],\"citationType\":\"journal article\",\"firstPage\":\"887\",\"id\":\"32003433\",\"journal\":\"Biochem. J.\",\"lastPage\":\"903\",\"publicationDate\":\"2020\",\"title\":\"Genetic evidences for the core biosynthesis pathway, regulation, transport and secretion of liamocins in yeast-like fungal cells.\",\"volume\":\"477\"},\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:24:45.462174+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0604cd5410cd5850ed1061ec3c5b369f42c7da183cd38472972d9c4ba536b805",
  "url": "https://rest.uniprot.org/uniprotkb/A0A385XI13.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI13?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H1",
  "excerpt": "ID   EST1_AURME              Reviewed;         282 AA.\nAC   A0A385XI13;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-DEC-2018, sequence version 1.\nDT   28-JAN-2026, entry version 13.\nDE   RecName: Full=Esterase 1 {ECO:0000303|PubMed:32003433};\nDE            Short=EST1 {ECO:0000303|PubMed:32003433};\nDE            EC=3.1.2.- {ECO:0000269|PubMed:32003433};\nDE   AltName: Full=Liamocins biosynthesis cluster protein EST1 {ECO:0000303|PubMed:32003433};\nGN   Name=EST1 {ECO:0000303|PubMed:32003433};\nOS   Aureobasidium melanogenum (Aureobasidium pullulans var. melanogenum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Dothideomycetidae; Dothideales; Saccotheciaceae; Aureobasidium.\nOX   NCBI_TaxID=46634;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:29.350597+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2adf58d8fd74514947bfa0569f28f495b9be466e1ab51987b05e8007a9a288ca",
  "url": "https://rest.uniprot.org/unisave/A0A385XI13?format=txt&versions=13"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI13?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H2",
  "excerpt": "RN   [4]\nRP   FUNCTION, DISRUPTION PHENOTYPE, AND INDUCTION.\nRX   PubMed=32003433; DOI=10.1042/bcj20190922;\nRA   Xue S.J., Liu G.L., Chi Z., Gao Z.C., Hu Z., Chi Z.M.;\nRT   \"Genetic evidences for the core biosynthesis pathway, regulation, transport\nRT   and secretion of liamocins in yeast-like fungal cells.\";\nRL   Biochem. J. 477:887-903(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:29.350597+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 33-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2adf58d8fd74514947bfa0569f28f495b9be466e1ab51987b05e8007a9a288ca",
  "url": "https://rest.uniprot.org/unisave/A0A385XI13?format=txt&versions=13"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A385XI13?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        131\nFT                   /note=\"Charge relay system\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P38777\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:29.350597+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 106-108",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "2adf58d8fd74514947bfa0569f28f495b9be466e1ab51987b05e8007a9a288ca",
  "url": "https://rest.uniprot.org/unisave/A0A385XI13?format=txt&versions=13"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 26. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
