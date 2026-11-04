# active_site_0119

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0119.txt)

**Task:** `active_site`  
**Expected answer:** **B** — Position 324 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEELTRSLVNDVEVLNNHFVSTGHPLPSFDRHTPTVVLPNDASPDAHAARERILDNALRLFQLAAGPSAYLLNLQTGYQYASCVRWLCHFQIFHLVPLEGSIAYADLAVLAKAPEPQLISVVRMAMTNGLFLESPPQHLAHSATSALLRNDADFHDWAVTMSDLSFPTAFAMVEAHERWPNSVEGNQTAYNIAVGSELPFFSHLAEQSDRKRQFAGFMRSMARSQGTDVEKLAEGWDWAALGQACVVDVGGSTGHTSVALARKYPDLNFVVEDLPEVVAEGPGYLSYLDDAQDLKSRIGYRAHSFFDPQPVQDADVYMLRMILHNWSFDDCVRILSRLVQTLKPGARIIIVDIVLPDPGVVSASKERLLRVQDLIMQQVFNSMERYLENWMDIFRKVDERLEVKRIVEPPGSLMSLIELSMAA

[Multiple Choices]
A. Position 140 (Charge relay system)
B. Position 324 (Proton acceptor)
C. Position 2711 (For beta-ketoacyl synthase 2 activity)
D. Position 279 (Proton donor/acceptor)
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

> The archived UniProt annotation assigns position 324 as the proton acceptor and matches the supplied sequence. Its evidence is a PROSITE-ProRule annotation, so this supports the keyed answer as a computational annotation, not as direct experimental confirmation.

Citations as saved: [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a glycine-rich region consistent with SAM-dependent methyltransferases, and position 324 is a histidine. Transferable knowledge of this enzyme class makes a catalytic proton-accepting histidine a credible inference for an O-methylation reaction, distinguishing B from the other offered positions and roles. The 2711 alternative is also incompatible with the 423-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence and mechanism inference provides a meaningful basis for choosing B without needing the exact protein's database entry, although it does not independently prove the residue's role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the sequence and methyltransferase-family inference.


### Important caveats

- The cited active-site evidence is computational (PROSITE-ProRule); no direct experimental validation of position 324 is provided.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a glycine-rich region consistent with SAM-dependent methyltransferases, and position 324 is a histidine. Transferable knowledge of this enzyme class makes a catalytic proton-accepting histidine a credible inference for an O-methylation reaction, distinguishing B from the other offered positions and roles. The 2711 alternative is also incompatible with the 423-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence and mechanism inference provides a meaningful basis for choosing B without needing the exact protein's database entry, although it does not independently prove the residue's role."
  },
  "case_id": "active_site_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "H3"
    ],
    "judgment": "supported",
    "reason": "The archived UniProt annotation assigns position 324 as the proton acceptor and matches the supplied sequence. Its evidence is a PROSITE-ProRule annotation, so this supports the keyed answer as a computational annotation, not as direct experimental confirmation."
  },
  "important_caveats": [
    "The cited active-site evidence is computational (PROSITE-ProRule); no direct experimental validation of position 324 is provided."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence and methyltransferase-family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The archived UniProt annotation assigns position 324 as the proton acceptor and matches the supplied sequence. Its evidence is a PROSITE-ProRule annotation, so this supports the keyed answer as a computational annotation, not as direct experimental confirmation.",
    "evidence_ids": ["H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a glycine-rich region consistent with SAM-dependent methyltransferases, and position 324 is a histidine. Transferable knowledge of this enzyme class makes a catalytic proton-accepting histidine a credible inference for an O-methylation reaction, distinguishing B from the other offered positions and roles. The 2711 alternative is also incompatible with the 423-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence and mechanism inference provides a meaningful basis for choosing B without needing the exact protein's database entry, although it does not independently prove the residue's role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence and methyltransferase-family inference."
  },
  "important_caveats": [
    "The cited active-site evidence is computational (PROSITE-ProRule); no direct experimental validation of position 324 is provided."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry Q2TXQ9 annotates position 324 as 'Proton acceptor' (Active site) with evidence code ECO:0000255 (PROSITE-ProRule:PRU01020). The sequence is 423 AA and position 324 corresponds to Histidine (H), which is chemically consistent with a proton acceptor role in an O-methyltransferase (EC 2.1.1.-). The annotation is computational (PROSITE pattern-based) rather than experimentally determined, but it is a recognized and curated annotation method that directly supports the key.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several layers of transferable reasoning distinguish B from the alternatives. (1) Choice C (position 2711) is eliminated immediately: the protein is 423 residues, so position 2711 is impossible. (2) Choice A invokes 'charge relay system,' terminology specific to the His-Asp-Ser triad of serine proteases, not methyltransferases; additionally, counting to position 140 yields Alanine, which has no ionizable side chain and cannot participate in any charge relay. (3) The critical B-vs-D distinction relies on identifying the amino acid at each position by counting the sequence: position 324 is Histidine (in the context RMIL-H-NWSFDD), while position 279 is Alanine (in the context VVEDLPEV-V-A-EG). Histidine's imidazole (pKa ≈ 6–7) is the classic proton acceptor in methyltransferase catalysis, whereas alanine has no ionizable group and cannot donate or accept a proton. (4) Structural anchoring: the VGGST motif at ~positions 250–254 is the canonical SAM-binding motif in methyltransferases; position 279 lies within this binding region (only ~6 residues from the annotated SAM-contact at 273), making it a binding-site residue rather than the catalytic proton acceptor. Position 324, ~50 residues downstream, occupies a distinct structural element consistent with the catalytic center. A knowledgeable model can use the SAM-motif anchor to verify its residue count and apply the well-established principle that the catalytic proton acceptor in SAM-dependent methyltransferases is a basic residue (His, Asp, Glu, or Tyr), not an alanine.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The answer is reachable through sequence analysis (counting to identify residue types), recognition of the SAM-binding VGGST motif as a structural landmark, elimination of impossible/irrelevant choices (C exceeds protein length; A uses wrong enzyme-class terminology and a non-ionizable residue), and the well-known biochemical principle that His is a proton acceptor while Ala is not. No target-specific database lookup is strictly necessary; the reasoning path uses transferable knowledge of methyltransferase mechanism, SAM-binding motifs, and amino-acid chemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A, C, and D are each independently eliminable: C by arithmetic (position exceeds 423 AA), A by enzyme-class mismatch and non-ionizable residue, D by the non-ionizable nature of Alanine at position 279. Only B (Histidine at 324 as proton acceptor) survives all checks.


### Important caveats

- The UniProt annotation at position 324 carries evidence code ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule PRU01020), meaning it is a curated computational pattern assignment rather than direct experimental measurement (e.g., crystallography or mutagenesis). The PROSITE rule is well-validated across the methyltransferase superfamily but is not protein-specific experimental proof.
- Correctly counting to residue 324 in a 423-residue sequence is mechanically possible but error-prone for language models; the SAM-binding motif at ~250–254 provides a useful anchor to verify counting accuracy.
- The reviewer-only evidence (accession Q2TXQ9, organism Aspergillus oryzae, protein name aoiF) was not available to the evaluated model; the reasoning path described above relies solely on the raw sequence and general biochemical knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several layers of transferable reasoning distinguish B from the alternatives. (1) Choice C (position 2711) is eliminated immediately: the protein is 423 residues, so position 2711 is impossible. (2) Choice A invokes 'charge relay system,' terminology specific to the His-Asp-Ser triad of serine proteases, not methyltransferases; additionally, counting to position 140 yields Alanine, which has no ionizable side chain and cannot participate in any charge relay. (3) The critical B-vs-D distinction relies on identifying the amino acid at each position by counting the sequence: position 324 is Histidine (in the context RMIL-H-NWSFDD), while position 279 is Alanine (in the context VVEDLPEV-V-A-EG). Histidine's imidazole (pKa ≈ 6–7) is the classic proton acceptor in methyltransferase catalysis, whereas alanine has no ionizable group and cannot donate or accept a proton. (4) Structural anchoring: the VGGST motif at ~positions 250–254 is the canonical SAM-binding motif in methyltransferases; position 279 lies within this binding region (only ~6 residues from the annotated SAM-contact at 273), making it a binding-site residue rather than the catalytic proton acceptor. Position 324, ~50 residues downstream, occupies a distinct structural element consistent with the catalytic center. A knowledgeable model can use the SAM-motif anchor to verify its residue count and apply the well-established principle that the catalytic proton acceptor in SAM-dependent methyltransferases is a basic residue (His, Asp, Glu, or Tyr), not an alanine.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The answer is reachable through sequence analysis (counting to identify residue types), recognition of the SAM-binding VGGST motif as a structural landmark, elimination of impossible/irrelevant choices (C exceeds protein length; A uses wrong enzyme-class terminology and a non-ionizable residue), and the well-known biochemical principle that His is a proton acceptor while Ala is not. No target-specific database lookup is strictly necessary; the reasoning path uses transferable knowledge of methyltransferase mechanism, SAM-binding motifs, and amino-acid chemistry."
  },
  "case_id": "active_site_0119",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "UniProt entry Q2TXQ9 annotates position 324 as 'Proton acceptor' (Active site) with evidence code ECO:0000255 (PROSITE-ProRule:PRU01020). The sequence is 423 AA and position 324 corresponds to Histidine (H), which is chemically consistent with a proton acceptor role in an O-methyltransferase (EC 2.1.1.-). The annotation is computational (PROSITE pattern-based) rather than experimentally determined, but it is a recognized and curated annotation method that directly supports the key."
  },
  "important_caveats": [
    "The UniProt annotation at position 324 carries evidence code ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule PRU01020), meaning it is a curated computational pattern assignment rather than direct experimental measurement (e.g., crystallography or mutagenesis). The PROSITE rule is well-validated across the methyltransferase superfamily but is not protein-specific experimental proof.",
    "Correctly counting to residue 324 in a 423-residue sequence is mechanically possible but error-prone for language models; the SAM-binding motif at ~250–254 provides a useful anchor to verify counting accuracy.",
    "The reviewer-only evidence (accession Q2TXQ9, organism Aspergillus oryzae, protein name aoiF) was not available to the evaluated model; the reasoning path described above relies solely on the raw sequence and general biochemical knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D are each independently eliminable: C by arithmetic (position exceeds 423 AA), A by enzyme-class mismatch and non-ionizable residue, D by the non-ionizable nature of Alanine at position 279. Only B (Histidine at 324 as proton acceptor) survives all checks."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0119",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry Q2TXQ9 annotates position 324 as 'Proton acceptor' (Active site) with evidence code ECO:0000255 (PROSITE-ProRule:PRU01020). The sequence is 423 AA and position 324 corresponds to Histidine (H), which is chemically consistent with a proton acceptor role in an O-methyltransferase (EC 2.1.1.-). The annotation is computational (PROSITE pattern-based) rather than experimentally determined, but it is a recognized and curated annotation method that directly supports the key.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several layers of transferable reasoning distinguish B from the alternatives. (1) Choice C (position 2711) is eliminated immediately: the protein is 423 residues, so position 2711 is impossible. (2) Choice A invokes 'charge relay system,' terminology specific to the His-Asp-Ser triad of serine proteases, not methyltransferases; additionally, counting to position 140 yields Alanine, which has no ionizable side chain and cannot participate in any charge relay. (3) The critical B-vs-D distinction relies on identifying the amino acid at each position by counting the sequence: position 324 is Histidine (in the context RMIL-H-NWSFDD), while position 279 is Alanine (in the context VVEDLPEV-V-A-EG). Histidine's imidazole (pKa ≈ 6–7) is the classic proton acceptor in methyltransferase catalysis, whereas alanine has no ionizable group and cannot donate or accept a proton. (4) Structural anchoring: the VGGST motif at ~positions 250–254 is the canonical SAM-binding motif in methyltransferases; position 279 lies within this binding region (only ~6 residues from the annotated SAM-contact at 273), making it a binding-site residue rather than the catalytic proton acceptor. Position 324, ~50 residues downstream, occupies a distinct structural element consistent with the catalytic center. A knowledgeable model can use the SAM-motif anchor to verify its residue count and apply the well-established principle that the catalytic proton acceptor in SAM-dependent methyltransferases is a basic residue (His, Asp, Glu, or Tyr), not an alanine.",
    "missing_item_specific_fact": "",
    "reason": "The answer is reachable through sequence analysis (counting to identify residue types), recognition of the SAM-binding VGGST motif as a structural landmark, elimination of impossible/irrelevant choices (C exceeds protein length; A uses wrong enzyme-class terminology and a non-ionizable residue), and the well-known biochemical principle that His is a proton acceptor while Ala is not. No target-specific database lookup is strictly necessary; the reasoning path uses transferable knowledge of methyltransferase mechanism, SAM-binding motifs, and amino-acid chemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A, C, and D are each independently eliminable: C by arithmetic (position exceeds 423 AA), A by enzyme-class mismatch and non-ionizable residue, D by the non-ionizable nature of Alanine at position 279. Only B (Histidine at 324 as proton acceptor) survives all checks."
  },
  "important_caveats": [
    "The UniProt annotation at position 324 carries evidence code ECO:0000255 (inferred from electronic annotation via PROSITE-ProRule PRU01020), meaning it is a curated computational pattern assignment rather than direct experimental measurement (e.g., crystallography or mutagenesis). The PROSITE rule is well-validated across the methyltransferase superfamily but is not protein-specific experimental proof.",
    "Correctly counting to residue 324 in a 423-residue sequence is mechanically possible but error-prone for language models; the SAM-binding motif at ~250–254 provides a useful anchor to verify counting accuracy.",
    "The reviewer-only evidence (accession Q2TXQ9, organism Aspergillus oryzae, protein name aoiF) was not available to the evaluated model; the reasoning path described above relies solely on the raw sequence and general biochemical knowledge."
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
  "benchmark_sequence_length": 423,
  "benchmark_sequence_sha256": "8b6d21fddedc7696cc2ab881cff4b654d21de66a9bb8b63e92634a12ce5f80d5",
  "current_entry_audit": {
    "entryVersion": 90,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2006-01-24",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 423,
  "current_source_sequence_sha256": "8b6d21fddedc7696cc2ab881cff4b654d21de66a9bb8b63e92634a12ce5f80d5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 88,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q2TXQ9",
  "selected_historical_entry_version": 88,
  "selected_historical_record_sha256": "6055a18729991928afae224429f327f87774a963491122cf581c595e953a0777",
  "selected_historical_source_sequence_length": 423,
  "selected_historical_source_sequence_sha256": "8b6d21fddedc7696cc2ab881cff4b654d21de66a9bb8b63e92634a12ce5f80d5",
  "selected_historical_version": {
    "accession": "Q2TXQ9",
    "database": "Swiss-Prot",
    "entryVersion": 88,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AOIF_ASPOR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q2TXQ9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:20.757390+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":90,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2006-01-24\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:20.757390+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yellow koji mold\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus oryzae (strain ATCC 42149 / RIB 40)\",\"taxonId\":510516}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:20.757390+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"22447538\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"22447538\",\"source\":\"PubMed\"}],\"value\":\"O-methyltransferase aoiF\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:20.757390+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":324},\"start\":{\"modifier\":\"EXACT\",\"value\":324}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:25:20.757390+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":273},\"start\":{\"modifier\":\"EXACT\",\"value\":273}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-01T06:25:20.757390+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q2TXQ9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Nakazawa T.\",\"Ishiuchi K.\",\"Praseuth A.\",\"Noguchi H.\",\"Hotta K.\",\"Watanabe K.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"22447538\"},{\"database\":\"DOI\",\"id\":\"10.1002/cbic.201200107\"}],\"citationType\":\"journal article\",\"firstPage\":\"855\",\"id\":\"22447538\",\"journal\":\"ChemBioChem\",\"lastPage\":\"861\",\"publicationDate\":\"2012\",\"title\":\"Overexpressing transcriptional regulator in Aspergillus oryzae activates a silent biosynthetic pathway to produce a novel polyketide.\",\"volume\":\"13\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"INDUCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:20.757390+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c23cf1f9e5ec46c96012eb2633b790ef53c7ca605ab3d2f53d10ae070d83cca9",
  "url": "https://rest.uniprot.org/uniprotkb/Q2TXQ9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H1",
  "excerpt": "ID   AOIF_ASPOR              Reviewed;         423 AA.\nAC   Q2TXQ9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   24-JAN-2006, sequence version 1.\nDT   28-JAN-2026, entry version 88.\nDE   RecName: Full=O-methyltransferase aoiF {ECO:0000303|PubMed:22447538};\nDE            EC=2.1.1.- {ECO:0000269|PubMed:22447538};\nGN   Name=aoiF {ECO:0000303|PubMed:22447538}; ORFNames=AO090010000047;\nOS   Aspergillus oryzae (strain ATCC 42149 / RIB 40) (Yellow koji mold).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=510516;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:32.769835+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6055a18729991928afae224429f327f87774a963491122cf581c595e953a0777",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND INDUCTION.\nRX   PubMed=22447538; DOI=10.1002/cbic.201200107;\nRA   Nakazawa T., Ishiuchi K., Praseuth A., Noguchi H., Hotta K., Watanabe K.;\nRT   \"Overexpressing transcriptional regulator in Aspergillus oryzae activates a\nRT   silent biosynthetic pathway to produce a novel polyketide.\";\nRL   ChemBioChem 13:855-861(2012).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:32.769835+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6055a18729991928afae224429f327f87774a963491122cf581c595e953a0777",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        324\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:32.769835+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6055a18729991928afae224429f327f87774a963491122cf581c595e953a0777",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88)

```json
{
  "entry_version": 88,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         273\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:32.769835+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 102-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6055a18729991928afae224429f327f87774a963491122cf581c595e953a0777",
  "url": "https://rest.uniprot.org/unisave/Q2TXQ9?format=txt&versions=88"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 119. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
