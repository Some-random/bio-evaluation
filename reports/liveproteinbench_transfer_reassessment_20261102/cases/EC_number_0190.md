# EC_number_0190

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0190.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 3.2.2.19

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRSFLYMLSQRPKLACLCGKSIIIWPGKRTNLPENAFTQRMLQECGQMAKPDASVDLDNFKAISEQSPAEFGIDSCRVKAQPEDRSDRIREQIASAYPVIHERTLLLFISFLEHKLTFGSEQEKAIYKDMTVVDLVQRLLAKRCVWFFGANDYYRTMQGNIGNEGFEAVGTPAEKEPLTLTSVLSYDEIKLSALLYVSCHSEFINNGSRVNGGEVLQNKDTIEREGVVIGLIGARFERPDVMEYQDIMITKTQNTEANGYGFDLEQISSETVTPASDLRRIWREFYEEPRDFIYADTPYDTTRFEEVSQGIFDHQVMRKRYAISFDTLLLEAQDRAFKAGKPAYIHVVGIGLGVWKAARQQERTFLESFEGRLRALGERLSHIGVVHFSWFHLACVGSLHDGAIIPVDKHPQGGIRIRNSVRNPGDKLTEDMLPVVTYAWDGNALPGNEFWANMLISTGDPAAACSTLISELQNPHINVHYMNGANLHIASVEHGLLHVGDYARRLIV

[Multiple Choices]
A. 3.2.2.19
B. 3.2.2.5
C. 1.11.1.24
D. 2.8.1.7
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

> The sequence-matched UniProt annotation assigns EC 3.2.2.19 and cites a publication with experimental-evidence code ECO:0000269. Its catalytic-activity annotations describe hydrolysis of ADP-ribosylated arginine, supporting the keyed choice. This is database-reported experimental support, not an independent validation here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains glycine-rich motifs and a pattern consistent with an ADP-ribose-binding macrodomain-like enzyme. Transferable knowledge of macrodomain enzymes provides a credible basis for predicting removal of ADP-ribose; among these choices, A is the matching arginine-directed ADP-ribose hydrolase, whereas the others describe unrelated enzyme activities.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and family-level inference meaningfully distinguish A from the offered alternatives without needing the exact protein's database record. The sequence alone may not establish substrate specificity with certainty, so this is a defensible probabilistic inference rather than proof.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe sufficiently distinct activities; no second choice is comparably supported by the sequence-level family inference.


### Important caveats

- The experimental support is reported through a database annotation citing a publication; the primary study was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains glycine-rich motifs and a pattern consistent with an ADP-ribose-binding macrodomain-like enzyme. Transferable knowledge of macrodomain enzymes provides a credible basis for predicting removal of ADP-ribose; among these choices, A is the matching arginine-directed ADP-ribose hydrolase, whereas the others describe unrelated enzyme activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level inference meaningfully distinguish A from the offered alternatives without needing the exact protein's database record. The sequence alone may not establish substrate specificity with certainty, so this is a defensible probabilistic inference rather than proof."
  },
  "case_id": "EC_number_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 3.2.2.19 and cites a publication with experimental-evidence code ECO:0000269. Its catalytic-activity annotations describe hydrolysis of ADP-ribosylated arginine, supporting the keyed choice. This is database-reported experimental support, not an independent validation here."
  },
  "important_caveats": [
    "The experimental support is reported through a database annotation citing a publication; the primary study was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe sufficiently distinct activities; no second choice is comparably supported by the sequence-level family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 3.2.2.19 and cites a publication with experimental-evidence code ECO:0000269. Its catalytic-activity annotations describe hydrolysis of ADP-ribosylated arginine, supporting the keyed choice. This is database-reported experimental support, not an independent validation here.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains glycine-rich motifs and a pattern consistent with an ADP-ribose-binding macrodomain-like enzyme. Transferable knowledge of macrodomain enzymes provides a credible basis for predicting removal of ADP-ribose; among these choices, A is the matching arginine-directed ADP-ribose hydrolase, whereas the others describe unrelated enzyme activities.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and family-level inference meaningfully distinguish A from the offered alternatives without needing the exact protein's database record. The sequence alone may not establish substrate specificity with certainty, so this is a defensible probabilistic inference rather than proof."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe sufficiently distinct activities; no second choice is comparably supported by the sequence-level family inference."
  },
  "important_caveats": [
    "The experimental support is reported through a database annotation citing a publication; the primary study was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9W4J9 (ADPR2_DROME, Drosophila melanogaster CG3568) is annotated with EC 3.2.2.19 (ADP-ribosylarginine hydrolase) supported by experimental evidence (ECO:0000269|PubMed:38503748; PDB 8DMU X-ray crystallography at 2.00 Å). Two catalytic activity reactions are documented (Rhea:14885 and Rhea:20784), both assigned EC 3.2.2.19. The sequence in the question matches the UniProt sequence exactly (508 AA, SHA256 match). The annotation is based on a 2024 Nature Communications paper demonstrating arginine-specific ADP-ribosylhydrolase activity via a conserved macrodomain.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options span three different EC top-level classes: 3 (hydrolase), 1 (oxidoreductase), and 2 (transferase). Options C (1.11.1.24, ascorbate peroxidase) and D (2.8.1.7, a sulfurtransferase) can be excluded because the sequence lacks heme-binding motifs (no Cys/His pairs typical of peroxidases, no conserved peroxidase catalytic triad) and lacks rhodanese/sulfurtransferase motifs (no conserved Cys in a rhodanese-like fold). The harder discrimination is A (3.2.2.19, ADP-ribosylarginine hydrolase) vs B (3.2.2.5, NAD(+) glycohydrolase/CD38). Both are glycosylases in EC 3.2.2, but they have completely different structural folds: CD38/NAD+ glycohydrolase is a homodimeric enzyme with a distinctive ADP-ribosyl cyclase domain (~280 residues/monomer), while ADP-ribosylarginine hydrolase activity in this protein is mediated by a macrodomain fold (~100-150 residues), a well-characterized ADP-ribose binding/hydrolyzing module found across many proteins (e.g., macroH2A, ARH3, viral macrodomains). The sequence contains motifs consistent with a macrodomain (conserved G residues in a binding pocket context, e.g., 'GANDYY', 'GNEGFEA', 'GFEAVGTP', along with conserved acidic residues for catalysis), rather than the distinctive CD38 cyclase-fold architecture. Family-level knowledge of macrodomains as ADP-ribose-interacting modules, combined with the absence of CD38-specific structural signatures, provides a credible basis for selecting 3.2.2.19 over 3.2.2.5. Additionally, the protein length (508 AA) is more consistent with a macrodomain-containing hydrolase than with a homodimeric CD38-type enzyme.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can exclude C and D by recognizing the absence of peroxidase and sulfurtransferase motifs. The A-vs-B discrimination relies on family-level knowledge: macrodomain fold (ADP-ribose binding/hydrolysis, associated with EC 3.2.2.19-type activity) vs CD38 fold (NAD+ glycohydrolase, EC 3.2.2.5). The sequence shows macrodomain-like features and lacks CD38-specific architecture. This is a legitimate structural/family-level inference from transferable knowledge of macrodomain proteins, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly different enzyme classes (peroxidase, sulfurtransferase) with no sequence support. Option B (NAD+ glycohydrolase/CD38) has a well-known distinct fold incompatible with the macrodomain-like features in this sequence. While macrodomain recognition from raw sequence is not trivial, the structural/fold-level distinction between macrodomain ADP-ribosylhydrolases and CD38 NAD+ glycohydrolases is a well-established family-level difference. No two options are genuinely indistinguishable given the sequence and standard protein-family knowledge.


### Important caveats

- The EC 3.2.2.19 annotation for this protein was established experimentally in 2024 (PubMed 38503748, PDB 8DMU) and the UniProt entry was first public in February 2025. Before that, this protein's function was uncharacterized. A model trained on data before 2024 would not have a database annotation to recall.
- Macrodomain recognition from raw sequence without HMM/Pfam tools is challenging; the argument relies on the model having internalized macrodomain sequence patterns from training on many macrodomain-containing proteins.
- The distinction between arginine-specific (3.2.2.19) and serine-specific (ARH3, EC 3.2.2.-) ADP-ribosylhydrolase activity within the macrodomain family is subtle. However, since serine-specific hydrolase is not among the options, this does not create ambiguity for the given choices.
- The mammalian ARH1/ARH2 (classical ADP-ribosylarginine hydrolases, ~500 kDa, tandem ARH domains) have a different fold from this Drosophila macrodomain protein, despite sharing the same EC number. The macrodomain-mediated ARH activity is a more recently characterized mechanism.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options span three different EC top-level classes: 3 (hydrolase), 1 (oxidoreductase), and 2 (transferase). Options C (1.11.1.24, ascorbate peroxidase) and D (2.8.1.7, a sulfurtransferase) can be excluded because the sequence lacks heme-binding motifs (no Cys/His pairs typical of peroxidases, no conserved peroxidase catalytic triad) and lacks rhodanese/sulfurtransferase motifs (no conserved Cys in a rhodanese-like fold). The harder discrimination is A (3.2.2.19, ADP-ribosylarginine hydrolase) vs B (3.2.2.5, NAD(+) glycohydrolase/CD38). Both are glycosylases in EC 3.2.2, but they have completely different structural folds: CD38/NAD+ glycohydrolase is a homodimeric enzyme with a distinctive ADP-ribosyl cyclase domain (~280 residues/monomer), while ADP-ribosylarginine hydrolase activity in this protein is mediated by a macrodomain fold (~100-150 residues), a well-characterized ADP-ribose binding/hydrolyzing module found across many proteins (e.g., macroH2A, ARH3, viral macrodomains). The sequence contains motifs consistent with a macrodomain (conserved G residues in a binding pocket context, e.g., 'GANDYY', 'GNEGFEA', 'GFEAVGTP', along with conserved acidic residues for catalysis), rather than the distinctive CD38 cyclase-fold architecture. Family-level knowledge of macrodomains as ADP-ribose-interacting modules, combined with the absence of CD38-specific structural signatures, provides a credible basis for selecting 3.2.2.19 over 3.2.2.5. Additionally, the protein length (508 AA) is more consistent with a macrodomain-containing hydrolase than with a homodimeric CD38-type enzyme.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can exclude C and D by recognizing the absence of peroxidase and sulfurtransferase motifs. The A-vs-B discrimination relies on family-level knowledge: macrodomain fold (ADP-ribose binding/hydrolysis, associated with EC 3.2.2.19-type activity) vs CD38 fold (NAD+ glycohydrolase, EC 3.2.2.5). The sequence shows macrodomain-like features and lacks CD38-specific architecture. This is a legitimate structural/family-level inference from transferable knowledge of macrodomain proteins, not a lookup of this specific protein's annotation."
  },
  "case_id": "EC_number_0190",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9W4J9 (ADPR2_DROME, Drosophila melanogaster CG3568) is annotated with EC 3.2.2.19 (ADP-ribosylarginine hydrolase) supported by experimental evidence (ECO:0000269|PubMed:38503748; PDB 8DMU X-ray crystallography at 2.00 Å). Two catalytic activity reactions are documented (Rhea:14885 and Rhea:20784), both assigned EC 3.2.2.19. The sequence in the question matches the UniProt sequence exactly (508 AA, SHA256 match). The annotation is based on a 2024 Nature Communications paper demonstrating arginine-specific ADP-ribosylhydrolase activity via a conserved macrodomain."
  },
  "important_caveats": [
    "The EC 3.2.2.19 annotation for this protein was established experimentally in 2024 (PubMed 38503748, PDB 8DMU) and the UniProt entry was first public in February 2025. Before that, this protein's function was uncharacterized. A model trained on data before 2024 would not have a database annotation to recall.",
    "Macrodomain recognition from raw sequence without HMM/Pfam tools is challenging; the argument relies on the model having internalized macrodomain sequence patterns from training on many macrodomain-containing proteins.",
    "The distinction between arginine-specific (3.2.2.19) and serine-specific (ARH3, EC 3.2.2.-) ADP-ribosylhydrolase activity within the macrodomain family is subtle. However, since serine-specific hydrolase is not among the options, this does not create ambiguity for the given choices.",
    "The mammalian ARH1/ARH2 (classical ADP-ribosylarginine hydrolases, ~500 kDa, tandem ARH domains) have a different fold from this Drosophila macrodomain protein, despite sharing the same EC number. The macrodomain-mediated ARH activity is a more recently characterized mechanism."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly different enzyme classes (peroxidase, sulfurtransferase) with no sequence support. Option B (NAD+ glycohydrolase/CD38) has a well-known distinct fold incompatible with the macrodomain-like features in this sequence. While macrodomain recognition from raw sequence is not trivial, the structural/fold-level distinction between macrodomain ADP-ribosylhydrolases and CD38 NAD+ glycohydrolases is a well-established family-level difference. No two options are genuinely indistinguishable given the sequence and standard protein-family knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0190",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9W4J9 (ADPR2_DROME, Drosophila melanogaster CG3568) is annotated with EC 3.2.2.19 (ADP-ribosylarginine hydrolase) supported by experimental evidence (ECO:0000269|PubMed:38503748; PDB 8DMU X-ray crystallography at 2.00 Å). Two catalytic activity reactions are documented (Rhea:14885 and Rhea:20784), both assigned EC 3.2.2.19. The sequence in the question matches the UniProt sequence exactly (508 AA, SHA256 match). The annotation is based on a 2024 Nature Communications paper demonstrating arginine-specific ADP-ribosylhydrolase activity via a conserved macrodomain.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four options span three different EC top-level classes: 3 (hydrolase), 1 (oxidoreductase), and 2 (transferase). Options C (1.11.1.24, ascorbate peroxidase) and D (2.8.1.7, a sulfurtransferase) can be excluded because the sequence lacks heme-binding motifs (no Cys/His pairs typical of peroxidases, no conserved peroxidase catalytic triad) and lacks rhodanese/sulfurtransferase motifs (no conserved Cys in a rhodanese-like fold). The harder discrimination is A (3.2.2.19, ADP-ribosylarginine hydrolase) vs B (3.2.2.5, NAD(+) glycohydrolase/CD38). Both are glycosylases in EC 3.2.2, but they have completely different structural folds: CD38/NAD+ glycohydrolase is a homodimeric enzyme with a distinctive ADP-ribosyl cyclase domain (~280 residues/monomer), while ADP-ribosylarginine hydrolase activity in this protein is mediated by a macrodomain fold (~100-150 residues), a well-characterized ADP-ribose binding/hydrolyzing module found across many proteins (e.g., macroH2A, ARH3, viral macrodomains). The sequence contains motifs consistent with a macrodomain (conserved G residues in a binding pocket context, e.g., 'GANDYY', 'GNEGFEA', 'GFEAVGTP', along with conserved acidic residues for catalysis), rather than the distinctive CD38 cyclase-fold architecture. Family-level knowledge of macrodomains as ADP-ribose-interacting modules, combined with the absence of CD38-specific structural signatures, provides a credible basis for selecting 3.2.2.19 over 3.2.2.5. Additionally, the protein length (508 AA) is more consistent with a macrodomain-containing hydrolase than with a homodimeric CD38-type enzyme.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can exclude C and D by recognizing the absence of peroxidase and sulfurtransferase motifs. The A-vs-B discrimination relies on family-level knowledge: macrodomain fold (ADP-ribose binding/hydrolysis, associated with EC 3.2.2.19-type activity) vs CD38 fold (NAD+ glycohydrolase, EC 3.2.2.5). The sequence shows macrodomain-like features and lacks CD38-specific architecture. This is a legitimate structural/family-level inference from transferable knowledge of macrodomain proteins, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly different enzyme classes (peroxidase, sulfurtransferase) with no sequence support. Option B (NAD+ glycohydrolase/CD38) has a well-known distinct fold incompatible with the macrodomain-like features in this sequence. While macrodomain recognition from raw sequence is not trivial, the structural/fold-level distinction between macrodomain ADP-ribosylhydrolases and CD38 NAD+ glycohydrolases is a well-established family-level difference. No two options are genuinely indistinguishable given the sequence and standard protein-family knowledge."
  },
  "important_caveats": [
    "The EC 3.2.2.19 annotation for this protein was established experimentally in 2024 (PubMed 38503748, PDB 8DMU) and the UniProt entry was first public in February 2025. Before that, this protein's function was uncharacterized. A model trained on data before 2024 would not have a database annotation to recall.",
    "Macrodomain recognition from raw sequence without HMM/Pfam tools is challenging; the argument relies on the model having internalized macrodomain sequence patterns from training on many macrodomain-containing proteins.",
    "The distinction between arginine-specific (3.2.2.19) and serine-specific (ARH3, EC 3.2.2.-) ADP-ribosylhydrolase activity within the macrodomain family is subtle. However, since serine-specific hydrolase is not among the options, this does not create ambiguity for the given choices.",
    "The mammalian ARH1/ARH2 (classical ADP-ribosylarginine hydrolases, ~500 kDa, tandem ARH domains) have a different fold from this Drosophila macrodomain protein, despite sharing the same EC number. The macrodomain-mediated ARH activity is a more recently characterized mechanism."
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
  "benchmark_sequence_length": 508,
  "benchmark_sequence_sha256": "e96e1998af231b58f41730af94d3c8781aa5e01347bc51d11e0d87abf78c384f",
  "current_entry_audit": {
    "entryVersion": 155,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-10-01",
    "sequenceVersion": 2
  },
  "current_record_sha256": "9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 508,
  "current_source_sequence_sha256": "e96e1998af231b58f41730af94d3c8781aa5e01347bc51d11e0d87abf78c384f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 153,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9W4J9",
  "selected_historical_entry_version": 153,
  "selected_historical_record_sha256": "9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b",
  "selected_historical_source_sequence_length": 508,
  "selected_historical_source_sequence_sha256": "e96e1998af231b58f41730af94d3c8781aa5e01347bc51d11e0d87abf78c384f",
  "selected_historical_version": {
    "accession": "Q9W4J9",
    "database": "Swiss-Prot",
    "entryVersion": 153,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ADPR2_DROME",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9W4J9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:51.239752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W4J9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":155,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-10-01\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:51.239752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W4J9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:51.239752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W4J9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503748\",\"source\":\"PubMed\"}],\"value\":\"3.2.2.19\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"ADP-ribosylarginine hydrolase CG3568\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:51.239752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W4J9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.2.19\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503748\",\"source\":\"PubMed\"}],\"name\":\"N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-ribose + L-arginyl-[protein]\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:14885\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10532\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15087\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57967\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142554\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:33:51.239752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W4J9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.2.19\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503748\",\"source\":\"PubMed\"}],\"name\":\"N(omega)-(ADP-D-ribosyl)-L-arginine + H2O = ADP-D-ribose + L-arginine\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:20784\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:32682\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57967\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:60267\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:33:51.239752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W4J9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Fu J.\",\"Rack J.G.M.\",\"Li C.\",\"Voorneveld J.\",\"Filippov D.V.\",\"Ahel I.\",\"Luo Z.Q.\",\"Das C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38503748\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-46649-2\"}],\"citationType\":\"journal article\",\"firstPage\":\"2452\",\"id\":\"38503748\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"2452\",\"publicationDate\":\"2024\",\"title\":\"Legionella metaeffector MavL reverses ubiquitin ADP-ribosylation via a conserved arginine-specific macrodomain.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8DMU\",\"source\":\"PDB\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.00 ANGSTROMS) OF 25-508\",\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:33:51.239752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W4J9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H1",
  "excerpt": "ID   ADPR2_DROME             Reviewed;         508 AA.\nAC   Q9W4J9;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-OCT-2002, sequence version 2.\nDT   28-JAN-2026, entry version 153.\nDE   RecName: Full=ADP-ribosylarginine hydrolase CG3568 {ECO:0000305};\nDE            EC=3.2.2.19 {ECO:0000269|PubMed:38503748};\nGN   ORFNames=CG3568 {ECO:0000312|FlyBase:FBgn0029710};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:55.177738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b",
  "url": "https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=ADP-ribosylarginine hydrolase CG3568 {ECO:0000305};\nDE            EC=3.2.2.19 {ECO:0000269|PubMed:38503748};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:55.177738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b",
  "url": "https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0007744|PDB:8DMU}\nRP   X-RAY CRYSTALLOGRAPHY (2.00 ANGSTROMS) OF 25-508, FUNCTION, AND CATALYTIC\nRP   ACTIVITY.\nRX   PubMed=38503748; DOI=10.1038/s41467-024-46649-2;\nRA   Zhang Z., Fu J., Rack J.G.M., Li C., Voorneveld J., Filippov D.V., Ahel I.,\nRA   Luo Z.Q., Das C.;\nRT   \"Legionella metaeffector MavL reverses ubiquitin ADP-ribosylation via a\nRT   conserved arginine-specific macrodomain.\";\nRL   Nat. Commun. 15:2452-2452(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:55.177738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-85",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b",
  "url": "https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] + H2O = ADP-D-\nCC         ribose + L-arginyl-[protein]; Xref=Rhea:RHEA:14885, Rhea:RHEA-\nCC         COMP:10532, Rhea:RHEA-COMP:15087, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:29965, ChEBI:CHEBI:57967, ChEBI:CHEBI:142554;\nCC         EC=3.2.2.19; Evidence={ECO:0000269|PubMed:38503748};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:55.177738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b",
  "url": "https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N(omega)-(ADP-D-ribosyl)-L-arginine + H2O = ADP-D-ribose + L-\nCC         arginine; Xref=Rhea:RHEA:20784, ChEBI:CHEBI:15377, ChEBI:CHEBI:32682,\nCC         ChEBI:CHEBI:57967, ChEBI:CHEBI:60267; EC=3.2.2.19;\nCC         Evidence={ECO:0000269|PubMed:38503748};\nCC   ---------------------------------------------------------------------------\nCC   Copyrighted by the UniProt Consortium, see https://www.uniprot.org/terms\nCC   Distributed under the Creative Commons Attribution (CC BY 4.0) License\nCC   ---------------------------------------------------------------------------\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:55.177738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b",
  "url": "https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 190. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
