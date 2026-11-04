# transmembrane_0048

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/transmembrane_0048.txt)

**Task:** `transmembrane`  
**Expected answer:** **D** — 15..33

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDVAMRVEWLATPRVILGIGAGWVAYALCLDPLRHIPGPRLNAVSMIPYARHLLAGTTVQNSVSLHQQYGEVVRIAPNEVSLICGETAFPDIYGRLFITSQTMGQIRANSAVCRVSDGKDERASKYVQGRRVLAHAFSDKALMGQEPLVQRYVDQLIDRLKEVTSANDEPVDMVKWYNWTTFDVIADLLFGEPFGCLQDLSTHQYVALLFQSLKSLRMIYILAYYPWLRFLGNLIVDKGLIQKRKEYATWVSTQVTKRINTATPRPDFMSHILANNNNRGVKLTRAEIDSNATLMTTAGSETTATLLSGATYLLLTHPRVLRTLQDEIHSEFPTYESITLEAVAKRTPYLNAVISEALRFFPPIPVGFIRRVPKGGETVSGYWIPEGTILSVSHYAAYHSERNFRDPDSWVPERWLGDERYVNDKRAAFQPFSFGPRSCLGRNLAYAEMRLILAKMVWSFEMELDEGLSRDWLQRCRVMRLWQKPELEVRVRPRVVA

[Multiple Choices]
A. 5..25; 40..60; 78..98; 119..139; 187..207; 223..243; 261..281; 302..322; 330..350; 385..405
B. 16..32
C. 15..33; 258..281
D. 15..33
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Transmembrane Region Prediction, which is to predict a region of the protein that spans across a cell membrane. These transmembrane domains are typically hydrophobic alpha-helices that anchor the protein within the lipid bilayer or form channels. Based on the provided amino acid sequence, you must select the option that correctly identifies the start and end positions of a segment that crosses the membrane.. The inputs provided by the user for this task include:

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

> The exact supplied sequence is annotated as a helical transmembrane region at 15..33 in both the historical and current UniProt records. The evidence is computational annotation (ECO:0000255), not direct experimental confirmation.

Citations as saved: [H3](#evidence-h3), [C5](#evidence-c5).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence has a conspicuous hydrophobic N-terminal stretch, consistent with the membrane anchor found in many cytochrome P450 proteins. This supports the region around 15..33 and distinguishes it from choices proposing many membrane spans or an additional distant span, but it does not reliably distinguish the nearly identical 15..33 and 16..32 alternatives.


**Missing item-specific fact**

> A target-specific boundary call or annotation distinguishing 15..33 from 16..32 is needed to identify the keyed choice.


**Reason**

> Transferable sequence and P450-family knowledge supports an N-terminal membrane anchor, but the two leading alternatives overlap almost entirely. Their precise endpoints are not reliably resolved by that general inference.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "B",
  "D"
]
```

> Both options describe essentially the same hydrophobic N-terminal region; the supplied sequence and general membrane-helix knowledge do not establish a biologically decisive difference between their one-residue-shifted boundaries.


### Important caveats

- The source annotation is computational and does not establish experimentally measured membrane boundaries.
- The source sequence matches the supplied sequence; the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a conspicuous hydrophobic N-terminal stretch, consistent with the membrane anchor found in many cytochrome P450 proteins. This supports the region around 15..33 and distinguishes it from choices proposing many membrane spans or an additional distant span, but it does not reliably distinguish the nearly identical 15..33 and 16..32 alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "A target-specific boundary call or annotation distinguishing 15..33 from 16..32 is needed to identify the keyed choice.",
    "reason": "Transferable sequence and P450-family knowledge supports an N-terminal membrane anchor, but the two leading alternatives overlap almost entirely. Their precise endpoints are not reliably resolved by that general inference."
  },
  "case_id": "transmembrane_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The exact supplied sequence is annotated as a helical transmembrane region at 15..33 in both the historical and current UniProt records. The evidence is computational annotation (ECO:0000255), not direct experimental confirmation."
  },
  "important_caveats": [
    "The source annotation is computational and does not establish experimentally measured membrane boundaries.",
    "The source sequence matches the supplied sequence; the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "B",
      "D"
    ],
    "reason": "Both options describe essentially the same hydrophobic N-terminal region; the supplied sequence and general membrane-helix knowledge do not establish a biologically decisive difference between their one-residue-shifted boundaries."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "transmembrane_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact supplied sequence is annotated as a helical transmembrane region at 15..33 in both the historical and current UniProt records. The evidence is computational annotation (ECO:0000255), not direct experimental confirmation.",
    "evidence_ids": ["H3", "C5"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence has a conspicuous hydrophobic N-terminal stretch, consistent with the membrane anchor found in many cytochrome P450 proteins. This supports the region around 15..33 and distinguishes it from choices proposing many membrane spans or an additional distant span, but it does not reliably distinguish the nearly identical 15..33 and 16..32 alternatives.",
    "missing_item_specific_fact": "A target-specific boundary call or annotation distinguishing 15..33 from 16..32 is needed to identify the keyed choice.",
    "reason": "Transferable sequence and P450-family knowledge supports an N-terminal membrane anchor, but the two leading alternatives overlap almost entirely. Their precise endpoints are not reliably resolved by that general inference."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["B", "D"],
    "reason": "Both options describe essentially the same hydrophobic N-terminal region; the supplied sequence and general membrane-helix knowledge do not establish a biologically decisive difference between their one-residue-shifted boundaries."
  },
  "important_caveats": [
    "The source annotation is computational and does not establish experimentally measured membrane boundaries.",
    "The source sequence matches the supplied sequence; the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (C5, H3) records a single Transmembrane feature at positions 15..33 (Helical), matching option D exactly. The evidence code ECO:0000255 indicates a similarity-based (computational) annotation rather than direct experimental determination, but the sequence at positions 15-33 (VILGIGAGWVAYALCLDPL) is a hydrophobic stretch bounded by charged residues (R14 and R34), consistent with a TM alpha-helix. The annotation applies to the supplied sequence (497 AA, SHA-256 matched).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three transferable lines of reasoning distinguish D from the alternatives: (1) Cytochrome P450 family knowledge: microsomal/fungal P450s characteristically possess a single N-terminal transmembrane anchor helix; the sequence contains P450 signature motifs (e.g., FGCLQDL near 191-197, conserved Cys in the heme-binding FxxGxxxCxG region), confirming P450 identity and strongly favoring a single TM segment, which eliminates option A (10 TM regions). (2) Hydrophobicity analysis of the candidate regions: positions 258-281 (RINTATPRPDFMSHILANNNRGV) contain multiple charged and polar residues (R, N, T, D, H, S) and are clearly non-hydrophobic, eliminating option C. (3) Boundary analysis for B vs D: the hydrophobic stretch is flanked by charged Arg residues at positions 14 and 34, making 15-33 the natural boundaries of the TM helix. A 19-residue hydrophobic segment (D) is more consistent with spanning the ~30 Å hydrophobic core of a lipid bilayer (requiring ~19-20 residues at 1.5 Å/residue rise) than the truncated 17-residue segment in B (16..32), which would exclude the hydrophobic V15 and L33 that are clearly part of the continuous hydrophobic stretch.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of P450 family topology knowledge (single N-terminal TM anchor), sequence-level hydrophobicity assessment, and boundary analysis using flanking charged residues provides a concrete, transferable argument that meaningfully distinguishes D from A, C, and B. The B-vs-D distinction is subtle but the flanking-charge boundary and helix-length requirement give a defensible probabilistic preference for D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While B (16..32) and D (15..33) are close, the boundary analysis (charged R residues at 14 and 34 flanking the hydrophobic stretch) and the 19-residue helix length requirement for membrane spanning provide a reasonable preference for D. Options A and C are clearly eliminable by family knowledge and hydrophobicity analysis respectively.


### Important caveats

- The UniProt TM annotation carries evidence code ECO:0000255 (similarity-based), meaning it is a computational prediction transferred from related proteins, not an experimentally verified topology.
- The distinction between B (16..32) and D (15..33) is subtle; a hydrophobicity window predictor could plausibly yield either boundary. The argument for D relies on the flanking charged residues and helix-length reasoning rather than a sharp experimental boundary.
- The protein was annotated as Swiss-Prot entry CAAC_ASPNC (A2QQU9), first released 2025-04-09; the author's source snapshot is unknown but the sequence matches the current and historical records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three transferable lines of reasoning distinguish D from the alternatives: (1) Cytochrome P450 family knowledge: microsomal/fungal P450s characteristically possess a single N-terminal transmembrane anchor helix; the sequence contains P450 signature motifs (e.g., FGCLQDL near 191-197, conserved Cys in the heme-binding FxxGxxxCxG region), confirming P450 identity and strongly favoring a single TM segment, which eliminates option A (10 TM regions). (2) Hydrophobicity analysis of the candidate regions: positions 258-281 (RINTATPRPDFMSHILANNNRGV) contain multiple charged and polar residues (R, N, T, D, H, S) and are clearly non-hydrophobic, eliminating option C. (3) Boundary analysis for B vs D: the hydrophobic stretch is flanked by charged Arg residues at positions 14 and 34, making 15-33 the natural boundaries of the TM helix. A 19-residue hydrophobic segment (D) is more consistent with spanning the ~30 Å hydrophobic core of a lipid bilayer (requiring ~19-20 residues at 1.5 Å/residue rise) than the truncated 17-residue segment in B (16..32), which would exclude the hydrophobic V15 and L33 that are clearly part of the continuous hydrophobic stretch.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of P450 family topology knowledge (single N-terminal TM anchor), sequence-level hydrophobicity assessment, and boundary analysis using flanking charged residues provides a concrete, transferable argument that meaningfully distinguishes D from A, C, and B. The B-vs-D distinction is subtle but the flanking-charge boundary and helix-length requirement give a defensible probabilistic preference for D."
  },
  "case_id": "transmembrane_0048",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) records a single Transmembrane feature at positions 15..33 (Helical), matching option D exactly. The evidence code ECO:0000255 indicates a similarity-based (computational) annotation rather than direct experimental determination, but the sequence at positions 15-33 (VILGIGAGWVAYALCLDPL) is a hydrophobic stretch bounded by charged residues (R14 and R34), consistent with a TM alpha-helix. The annotation applies to the supplied sequence (497 AA, SHA-256 matched)."
  },
  "important_caveats": [
    "The UniProt TM annotation carries evidence code ECO:0000255 (similarity-based), meaning it is a computational prediction transferred from related proteins, not an experimentally verified topology.",
    "The distinction between B (16..32) and D (15..33) is subtle; a hydrophobicity window predictor could plausibly yield either boundary. The argument for D relies on the flanking charged residues and helix-length reasoning rather than a sharp experimental boundary.",
    "The protein was annotated as Swiss-Prot entry CAAC_ASPNC (A2QQU9), first released 2025-04-09; the author's source snapshot is unknown but the sequence matches the current and historical records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B (16..32) and D (15..33) are close, the boundary analysis (charged R residues at 14 and 34 flanking the hydrophobic stretch) and the 19-residue helix length requirement for membrane spanning provide a reasonable preference for D. Options A and C are clearly eliminable by family knowledge and hydrophobicity analysis respectively."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "transmembrane_0048",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (C5, H3) records a single Transmembrane feature at positions 15..33 (Helical), matching option D exactly. The evidence code ECO:0000255 indicates a similarity-based (computational) annotation rather than direct experimental determination, but the sequence at positions 15-33 (VILGIGAGWVAYALCLDPL) is a hydrophobic stretch bounded by charged residues (R14 and R34), consistent with a TM alpha-helix. The annotation applies to the supplied sequence (497 AA, SHA-256 matched).",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three transferable lines of reasoning distinguish D from the alternatives: (1) Cytochrome P450 family knowledge: microsomal/fungal P450s characteristically possess a single N-terminal transmembrane anchor helix; the sequence contains P450 signature motifs (e.g., FGCLQDL near 191-197, conserved Cys in the heme-binding FxxGxxxCxG region), confirming P450 identity and strongly favoring a single TM segment, which eliminates option A (10 TM regions). (2) Hydrophobicity analysis of the candidate regions: positions 258-281 (RINTATPRPDFMSHILANNNRGV) contain multiple charged and polar residues (R, N, T, D, H, S) and are clearly non-hydrophobic, eliminating option C. (3) Boundary analysis for B vs D: the hydrophobic stretch is flanked by charged Arg residues at positions 14 and 34, making 15-33 the natural boundaries of the TM helix. A 19-residue hydrophobic segment (D) is more consistent with spanning the ~30 Å hydrophobic core of a lipid bilayer (requiring ~19-20 residues at 1.5 Å/residue rise) than the truncated 17-residue segment in B (16..32), which would exclude the hydrophobic V15 and L33 that are clearly part of the continuous hydrophobic stretch.",
    "missing_item_specific_fact": "",
    "reason": "The combination of P450 family topology knowledge (single N-terminal TM anchor), sequence-level hydrophobicity assessment, and boundary analysis using flanking charged residues provides a concrete, transferable argument that meaningfully distinguishes D from A, C, and B. The B-vs-D distinction is subtle but the flanking-charge boundary and helix-length requirement give a defensible probabilistic preference for D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While B (16..32) and D (15..33) are close, the boundary analysis (charged R residues at 14 and 34 flanking the hydrophobic stretch) and the 19-residue helix length requirement for membrane spanning provide a reasonable preference for D. Options A and C are clearly eliminable by family knowledge and hydrophobicity analysis respectively."
  },
  "important_caveats": [
    "The UniProt TM annotation carries evidence code ECO:0000255 (similarity-based), meaning it is a computational prediction transferred from related proteins, not an experimentally verified topology.",
    "The distinction between B (16..32) and D (15..33) is subtle; a hydrophobicity window predictor could plausibly yield either boundary. The argument for D relies on the flanking charged residues and helix-length reasoning rather than a sharp experimental boundary.",
    "The protein was annotated as Swiss-Prot entry CAAC_ASPNC (A2QQU9), first released 2025-04-09; the author's source snapshot is unknown but the sequence matches the current and historical records."
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
  "benchmark_sequence_length": 497,
  "benchmark_sequence_sha256": "e271fb0582945d7a03d461266638ea0af4ac9474621fe87ecd6725c3a0f85b69",
  "current_entry_audit": {
    "entryVersion": 88,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-03-06",
    "sequenceVersion": 1
  },
  "current_record_sha256": "da743c57c89b0ab786ac3a1103de54e0cfdcba8a2bc83d6afcffbb82b38db7a1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 497,
  "current_source_sequence_sha256": "e271fb0582945d7a03d461266638ea0af4ac9474621fe87ecd6725c3a0f85b69",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 87,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A2QQU9",
  "selected_historical_entry_version": 87,
  "selected_historical_record_sha256": "7a9ce4cdb7446a207fbe542c309e101b336add0fcb1eacdc0748a053d0baa66d",
  "selected_historical_source_sequence_length": 497,
  "selected_historical_source_sequence_sha256": "e271fb0582945d7a03d461266638ea0af4ac9474621fe87ecd6725c3a0f85b69",
  "selected_historical_version": {
    "accession": "A2QQU9",
    "database": "Swiss-Prot",
    "entryVersion": 87,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "CAAC_ASPNC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A2QQU9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:57.143489+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "da743c57c89b0ab786ac3a1103de54e0cfdcba8a2bc83d6afcffbb82b38db7a1",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":88,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-03-06\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:57.143489+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "da743c57c89b0ab786ac3a1103de54e0cfdcba8a2bc83d6afcffbb82b38db7a1",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Circumdati\"],\"scientificName\":\"Aspergillus niger (strain ATCC MYA-4892 / CBS 513.88 / FGSC A1513)\",\"taxonId\":425011}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:57.143489+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "da743c57c89b0ab786ac3a1103de54e0cfdcba8a2bc83d6afcffbb82b38db7a1",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25044953\",\"source\":\"PubMed\"}],\"value\":\"Carlosic acid biosynthesis cluster protein C\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"25044953\",\"source\":\"PubMed\"}],\"value\":\"1.14.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"25044953\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 monooxygenase caaC\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:57.143489+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "da743c57c89b0ab786ac3a1103de54e0cfdcba8a2bc83d6afcffbb82b38db7a1",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Helical\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":33},\"start\":{\"modifier\":\"EXACT\",\"value\":15}},\"type\":\"Transmembrane\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-01T06:24:57.143489+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "da743c57c89b0ab786ac3a1103de54e0cfdcba8a2bc83d6afcffbb82b38db7a1",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A2QQU9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yang X.L.\",\"Awakawa T.\",\"Wakimoto T.\",\"Abe I.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"25044953\"},{\"database\":\"DOI\",\"id\":\"10.1002/cbic.201402172\"}],\"citationType\":\"journal article\",\"firstPage\":\"1578\",\"id\":\"25044953\",\"journal\":\"ChemBioChem\",\"lastPage\":\"1583\",\"publicationDate\":\"2014\",\"title\":\"Three acyltetronic acid derivatives: noncanonical cryptic polyketides from Aspergillus niger identified by genome mining.\",\"volume\":\"15\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"INDUCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:57.143489+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "da743c57c89b0ab786ac3a1103de54e0cfdcba8a2bc83d6afcffbb82b38db7a1",
  "url": "https://rest.uniprot.org/uniprotkb/A2QQU9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2QQU9?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H1",
  "excerpt": "ID   CAAC_ASPNC              Reviewed;         497 AA.\nAC   A2QQU9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   06-MAR-2007, sequence version 1.\nDT   28-JAN-2026, entry version 87.\nDE   RecName: Full=Cytochrome P450 monooxygenase caaC {ECO:0000303|PubMed:25044953};\nDE            EC=1.14.-.- {ECO:0000305|PubMed:25044953};\nDE   AltName: Full=Carlosic acid biosynthesis cluster protein C {ECO:0000303|PubMed:25044953};\nGN   Name=caaC {ECO:0000303|PubMed:25044953}; ORFNames=An08g03780;\nOS   Aspergillus niger (strain ATCC MYA-4892 / CBS 513.88 / FGSC A1513).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Circumdati.\nOX   NCBI_TaxID=425011;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:45.219435+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7a9ce4cdb7446a207fbe542c309e101b336add0fcb1eacdc0748a053d0baa66d",
  "url": "https://rest.uniprot.org/unisave/A2QQU9?format=txt&versions=87"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2QQU9?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, INDUCTION, AND PATHWAY.\nRX   PubMed=25044953; DOI=10.1002/cbic.201402172;\nRA   Yang X.L., Awakawa T., Wakimoto T., Abe I.;\nRT   \"Three acyltetronic acid derivatives: noncanonical cryptic polyketides from\nRT   Aspergillus niger identified by genome mining.\";\nRL   ChemBioChem 15:1578-1583(2014).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:45.219435+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7a9ce4cdb7446a207fbe542c309e101b336add0fcb1eacdc0748a053d0baa66d",
  "url": "https://rest.uniprot.org/unisave/A2QQU9?format=txt&versions=87"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A2QQU9?format=txt&versions=87)

```json
{
  "entry_version": 87,
  "evidence_id": "H3",
  "excerpt": "FT   TRANSMEM        15..33\nFT                   /note=\"Helical\"\nFT                   /evidence=\"ECO:0000255\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:45.219435+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7a9ce4cdb7446a207fbe542c309e101b336add0fcb1eacdc0748a053d0baa66d",
  "url": "https://rest.uniprot.org/unisave/A2QQU9?format=txt&versions=87"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/transmembrane.json), zero-based source row 48. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
