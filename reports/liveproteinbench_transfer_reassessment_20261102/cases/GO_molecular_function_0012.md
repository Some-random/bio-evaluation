# GO_molecular_function_0012

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0012.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — ADP-ribosylarginine hydrolase activity

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
A. RNA polymerase II core promoter sequence-specific DNA binding
B. ADP-ribosylarginine hydrolase activity
C. peptidase inhibitor activity
D. zinc ion binding
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence-matched source identifies the protein as an ADP-ribosylarginine hydrolase and reports experimental evidence for its function and catalytic activity. It also carries a direct-assay GO annotation matching choice B.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a long, enzyme-like globular protein with glycine-rich motifs and conserved-looking polar residues, consistent with an ADP-ribose-processing hydrolase/macrodomain-type protein. That family-level pattern makes B more plausible than promoter-specific DNA binding, peptidase inhibition, or zinc binding; the sequence does not show an obvious zinc-binding cluster. This is a probabilistic family inference, not proof of the exact substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable recognition of an ADP-ribose-processing enzyme family, together with the distractors' mismatch to the sequence's enzyme-like character, provides a meaningful basis to distinguish B without relying on the target's recorded annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, B is meaningfully distinguished by the enzyme-like sequence and the plausible ADP-ribose-processing family pattern.


### Important caveats

- The reviewer-only evidence supports the key but was not available as input to the evaluated model.
- Sequence-based family inference is not by itself an experimental demonstration of ADP-ribosylarginine hydrolase activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a long, enzyme-like globular protein with glycine-rich motifs and conserved-looking polar residues, consistent with an ADP-ribose-processing hydrolase/macrodomain-type protein. That family-level pattern makes B more plausible than promoter-specific DNA binding, peptidase inhibition, or zinc binding; the sequence does not show an obvious zinc-binding cluster. This is a probabilistic family inference, not proof of the exact substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of an ADP-ribose-processing enzyme family, together with the distractors' mismatch to the sequence's enzyme-like character, provides a meaningful basis to distinguish B without relying on the target's recorded annotation."
  },
  "case_id": "GO_molecular_function_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched source identifies the protein as an ADP-ribosylarginine hydrolase and reports experimental evidence for its function and catalytic activity. It also carries a direct-assay GO annotation matching choice B."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key but was not available as input to the evaluated model.",
    "Sequence-based family inference is not by itself an experimental demonstration of ADP-ribosylarginine hydrolase activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, B is meaningfully distinguished by the enzyme-like sequence and the plausible ADP-ribose-processing family pattern."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched source identifies the protein as an ADP-ribosylarginine hydrolase and reports experimental evidence for its function and catalytic activity. It also carries a direct-assay GO annotation matching choice B.",
    "evidence_ids": ["C5", "C6", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a long, enzyme-like globular protein with glycine-rich motifs and conserved-looking polar residues, consistent with an ADP-ribose-processing hydrolase/macrodomain-type protein. That family-level pattern makes B more plausible than promoter-specific DNA binding, peptidase inhibition, or zinc binding; the sequence does not show an obvious zinc-binding cluster. This is a probabilistic family inference, not proof of the exact substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "Transferable recognition of an ADP-ribose-processing enzyme family, together with the distractors' mismatch to the sequence's enzyme-like character, provides a meaningful basis to distinguish B without relying on the target's recorded annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, B is meaningfully distinguished by the enzyme-like sequence and the plausible ADP-ribose-processing family pattern."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key but was not available as input to the evaluated model.",
    "Sequence-based family inference is not by itself an experimental demonstration of ADP-ribosylarginine hydrolase activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q9W4J9 (ADPR2_DROME, Drosophila melanogaster) is annotated with EC 3.2.2.19 and GO:0003875 (ADP-ribosylarginine-&#91;protein&#93; hydrolase activity) with IDA evidence from FlyBase. The function was confirmed experimentally by X-ray crystallography (PDB 8DMU, 2.0 Å) and a 2024 Nature Communications paper (PMID 38503748). The sequence matches exactly (508 AA, SHA256 identical). The GO term's EXACT synonym 'ADP-ribosylarginine hydrolase activity' matches option B verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable macrodomain signatures: the 'ANGYGFDLEQ' motif (residues ~250-260) matches the canonical G-Y-F-D motif of the macrodomain fold, and the 'GIFDHQ' motif (residues ~290-295) represents a close variant. The C-terminal ~200 residues show the characteristic macrodomain architecture (conserved hydrophobic core with patterns like 'VVGIGLGVW', 'FEGRLRALGERLSHIGVVHFSWFHLACVGSLHDGAIIPVDKHPQGGIRIRNSVRNPGDKLTEDMLPVVTYAWDGNALPGNEFWANMLISTGDPAAACSTLISELQNPHINVHYMNGANLHIASVEHGLLHVGDYARRLIV'). Macrodomains are a well-characterized protein family (found in ARH1/ARH3, macroH2A, PARP10/15/16, bacterial virulence factors like MavL) whose defining molecular function is recognition and/or hydrolysis of ADP-ribosyl modifications. Among the four offered choices, only B (ADP-ribosylarginine hydrolase activity) is consistent with a macrodomain-containing enzyme. Choice A (RNA Pol II promoter DNA binding) requires zinc fingers, homeodomains, or TBP-like folds absent here. Choice C (peptidase inhibitor activity) requires serpin/Kunitz/Cystatin-type inhibitory folds not present. Choice D (zinc ion binding) requires clustered Cys/His motifs (CxxC, HxxxH) which are absent. Thus, recognizing the macrodomain fold from family-level knowledge of other macrodomain proteins meaningfully selects B over A, C, and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The macrodomain fold with its GYFD/GIFDH signature is a well-known, transferable structural motif. A knowledgeable model recognizing this family-level feature can eliminate A, C, and D (which require entirely different structural architectures) and select B as the only ADP-ribosyl-related activity among the choices. The inference does not require memorizing this specific protein's annotation; it relies on the established association between the macrodomain fold and ADP-ribosyl hydrolase/reader function learned from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The macrodomain signature clearly distinguishes B from the other three options. No zinc-binding cluster, DNA-binding domain, or peptidase-inhibitor fold is present. While macrodomains can also be readers (non-catalytic ADP-ribose binders), none of the offered alternatives correspond to a reader function, so B is the uniquely defensible choice among the given options.


### Important caveats

- The macrodomain alone indicates ADP-ribosyl recognition/hydrolysis broadly; distinguishing ADP-ribosylarginine from ADP-ribosylglycine or ADP-ribosylserine hydrolase specificity would require finer catalytic residue analysis. However, among the four offered choices, only B falls within the ADP-ribosyl hydrolase family, so this granularity is not needed for the MCQ.
- The GO annotation carries IDA (direct assay) evidence and was confirmed by 2024 X-ray crystallography, making the key well-supported experimentally.
- The sequence's N-terminal ~150 residues do not contain the macrodomain and may represent a regulatory or targeting region; this does not affect the MCQ discrimination.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable macrodomain signatures: the 'ANGYGFDLEQ' motif (residues ~250-260) matches the canonical G-Y-F-D motif of the macrodomain fold, and the 'GIFDHQ' motif (residues ~290-295) represents a close variant. The C-terminal ~200 residues show the characteristic macrodomain architecture (conserved hydrophobic core with patterns like 'VVGIGLGVW', 'FEGRLRALGERLSHIGVVHFSWFHLACVGSLHDGAIIPVDKHPQGGIRIRNSVRNPGDKLTEDMLPVVTYAWDGNALPGNEFWANMLISTGDPAAACSTLISELQNPHINVHYMNGANLHIASVEHGLLHVGDYARRLIV'). Macrodomains are a well-characterized protein family (found in ARH1/ARH3, macroH2A, PARP10/15/16, bacterial virulence factors like MavL) whose defining molecular function is recognition and/or hydrolysis of ADP-ribosyl modifications. Among the four offered choices, only B (ADP-ribosylarginine hydrolase activity) is consistent with a macrodomain-containing enzyme. Choice A (RNA Pol II promoter DNA binding) requires zinc fingers, homeodomains, or TBP-like folds absent here. Choice C (peptidase inhibitor activity) requires serpin/Kunitz/Cystatin-type inhibitory folds not present. Choice D (zinc ion binding) requires clustered Cys/His motifs (CxxC, HxxxH) which are absent. Thus, recognizing the macrodomain fold from family-level knowledge of other macrodomain proteins meaningfully selects B over A, C, and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The macrodomain fold with its GYFD/GIFDH signature is a well-known, transferable structural motif. A knowledgeable model recognizing this family-level feature can eliminate A, C, and D (which require entirely different structural architectures) and select B as the only ADP-ribosyl-related activity among the choices. The inference does not require memorizing this specific protein's annotation; it relies on the established association between the macrodomain fold and ADP-ribosyl hydrolase/reader function learned from other proteins."
  },
  "case_id": "GO_molecular_function_0012",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H1",
      "H3",
      "H4",
      "H5",
      "H6",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q9W4J9 (ADPR2_DROME, Drosophila melanogaster) is annotated with EC 3.2.2.19 and GO:0003875 (ADP-ribosylarginine-[protein] hydrolase activity) with IDA evidence from FlyBase. The function was confirmed experimentally by X-ray crystallography (PDB 8DMU, 2.0 Å) and a 2024 Nature Communications paper (PMID 38503748). The sequence matches exactly (508 AA, SHA256 identical). The GO term's EXACT synonym 'ADP-ribosylarginine hydrolase activity' matches option B verbatim."
  },
  "important_caveats": [
    "The macrodomain alone indicates ADP-ribosyl recognition/hydrolysis broadly; distinguishing ADP-ribosylarginine from ADP-ribosylglycine or ADP-ribosylserine hydrolase specificity would require finer catalytic residue analysis. However, among the four offered choices, only B falls within the ADP-ribosyl hydrolase family, so this granularity is not needed for the MCQ.",
    "The GO annotation carries IDA (direct assay) evidence and was confirmed by 2024 X-ray crystallography, making the key well-supported experimentally.",
    "The sequence's N-terminal ~150 residues do not contain the macrodomain and may represent a regulatory or targeting region; this does not affect the MCQ discrimination."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The macrodomain signature clearly distinguishes B from the other three options. No zinc-binding cluster, DNA-binding domain, or peptidase-inhibitor fold is present. While macrodomains can also be readers (non-catalytic ADP-ribose binders), none of the offered alternatives correspond to a reader function, so B is the uniquely defensible choice among the given options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0012",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q9W4J9 (ADPR2_DROME, Drosophila melanogaster) is annotated with EC 3.2.2.19 and GO:0003875 (ADP-ribosylarginine-[protein] hydrolase activity) with IDA evidence from FlyBase. The function was confirmed experimentally by X-ray crystallography (PDB 8DMU, 2.0 Å) and a 2024 Nature Communications paper (PMID 38503748). The sequence matches exactly (508 AA, SHA256 identical). The GO term's EXACT synonym 'ADP-ribosylarginine hydrolase activity' matches option B verbatim.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "H1", "H3", "H4", "H5", "H6", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable macrodomain signatures: the 'ANGYGFDLEQ' motif (residues ~250-260) matches the canonical G-Y-F-D motif of the macrodomain fold, and the 'GIFDHQ' motif (residues ~290-295) represents a close variant. The C-terminal ~200 residues show the characteristic macrodomain architecture (conserved hydrophobic core with patterns like 'VVGIGLGVW', 'FEGRLRALGERLSHIGVVHFSWFHLACVGSLHDGAIIPVDKHPQGGIRIRNSVRNPGDKLTEDMLPVVTYAWDGNALPGNEFWANMLISTGDPAAACSTLISELQNPHINVHYMNGANLHIASVEHGLLHVGDYARRLIV'). Macrodomains are a well-characterized protein family (found in ARH1/ARH3, macroH2A, PARP10/15/16, bacterial virulence factors like MavL) whose defining molecular function is recognition and/or hydrolysis of ADP-ribosyl modifications. Among the four offered choices, only B (ADP-ribosylarginine hydrolase activity) is consistent with a macrodomain-containing enzyme. Choice A (RNA Pol II promoter DNA binding) requires zinc fingers, homeodomains, or TBP-like folds absent here. Choice C (peptidase inhibitor activity) requires serpin/Kunitz/Cystatin-type inhibitory folds not present. Choice D (zinc ion binding) requires clustered Cys/His motifs (CxxC, HxxxH) which are absent. Thus, recognizing the macrodomain fold from family-level knowledge of other macrodomain proteins meaningfully selects B over A, C, and D.",
    "missing_item_specific_fact": "",
    "reason": "The macrodomain fold with its GYFD/GIFDH signature is a well-known, transferable structural motif. A knowledgeable model recognizing this family-level feature can eliminate A, C, and D (which require entirely different structural architectures) and select B as the only ADP-ribosyl-related activity among the choices. The inference does not require memorizing this specific protein's annotation; it relies on the established association between the macrodomain fold and ADP-ribosyl hydrolase/reader function learned from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The macrodomain signature clearly distinguishes B from the other three options. No zinc-binding cluster, DNA-binding domain, or peptidase-inhibitor fold is present. While macrodomains can also be readers (non-catalytic ADP-ribose binders), none of the offered alternatives correspond to a reader function, so B is the uniquely defensible choice among the given options."
  },
  "important_caveats": [
    "The macrodomain alone indicates ADP-ribosyl recognition/hydrolysis broadly; distinguishing ADP-ribosylarginine from ADP-ribosylglycine or ADP-ribosylserine hydrolase specificity would require finer catalytic residue analysis. However, among the four offered choices, only B falls within the ADP-ribosyl hydrolase family, so this granularity is not needed for the MCQ.",
    "The GO annotation carries IDA (direct assay) evidence and was confirmed by 2024 X-ray crystallography, making the key well-supported experimentally.",
    "The sequence's N-terminal ~150 residues do not contain the macrodomain and may represent a regulatory or targeting region; this does not affect the MCQ discrimination."
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
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

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
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38503748\",\"source\":\"PubMed\"}],\"value\":\"Protein ADP-ribosyl hydrolase that specifically removes mono-ADP-ribosyl modifications from protein arginine residues\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
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

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)

```json
{
  "evidence_id": "C7",
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

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"38503748\",\"source\":\"PubMed\"}],\"id\":\"GO:0003875\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:ADP-ribosylarginine-[protein] hydrolase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:FlyBase\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/27",
  "retrieved_utc": "2026-11-02T04:33:51.239752+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e43f663c4a6ec05c64f399f29a4677086a1bfced688daf5a6847c683d3f7aa9",
  "url": "https://rest.uniprot.org/uniprotkb/Q9W4J9.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9W4J9.json)

```json
{
  "evidence_id": "C9",
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Protein ADP-ribosyl hydrolase that specifically removes mono-\nCC       ADP-ribosyl modifications from protein arginine residues.\nCC       {ECO:0000269|PubMed:38503748}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:55.177738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 86-88",
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

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153)

```json
{
  "entry_version": 153,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0003875; F:ADP-ribosylarginine hydrolase activity; IDA:FlyBase.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:55.177738+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a427837811b39d632570986b671acc0e2a210f55a2733ccdd16e4480a28b86b",
  "url": "https://rest.uniprot.org/unisave/Q9W4J9?format=txt&versions=153"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000979\nname: RNA polymerase II core promoter sequence-specific DNA binding\nnamespace: molecular_function\ndef: \"Binding to a DNA sequence that is part of the core promoter of a RNA polymerase II-transcribed gene.\" [GOC:pg, GOC:txnOH, PMID:12381658]\nis_a: GO:0000977 ! RNA polymerase II transcription regulatory region sequence-specific DNA binding\nis_a: GO:0001046 ! core promoter sequence-specific DNA binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000979",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 7142-7149",
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
  "excerpt": "[Term]\nid: GO:0003875\nname: ADP-ribosylarginine-[protein] hydrolase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reactions: H2O + N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] = ADP-D-ribose + L-arginyl-[protein], and H2O + N(omega)-(ADP-D-ribosyl)-L-arginine = ADP-D-ribose + L-arginine.\" [EC:3.2.2.19]\nsynonym: \"ADP-ribose-L-arginine cleavage enzyme activity\" RELATED [EC:3.2.2.19]\nsynonym: \"ADP-ribose-L-arginine cleaving enzyme activity\" RELATED [EC:3.2.2.19]\nsynonym: \"ADP-ribosylarginine hydrolase activity\" EXACT []\nsynonym: \"ADPribosylarginine hydrolase activity\" EXACT []\nsynonym: \"N(omega)-(ADP-D-ribosyl)-L-arginine ADP-ribosylhydrolase activity\" RELATED [EC:3.2.2.19]\nsynonym: \"nomega-(ADP-D-ribosyl)-L-arginine ADP-ribosylhydrolase activity\" RELATED [EC:3.2.2.19]\nsynonym: \"omega-protein-N-(ADP-D-ribosyl)-L-arginine ADP-ribosylhydrolase activity\" RELATED [EC:3.2.2.19]\nsynonym: \"protein ADP-ribosylarginine hydrolase activity\" RELATED [EC:3.2.2.19]\nsynonym: \"protein-nomega-(ADP-D-ribosyl)-L-arginine ADP-ribosylhydrolase activity\" RELATED [EC:3.2.2.19]\nxref: EC:3.2.2.19\nxref: MetaCyc:3.2.2.24-RXN\nxref: MetaCyc:ADP-RIBOSYLARGININE-HYDROLASE-RXN\nxref: MetaCyc:RXN-8732\nxref: RHEA:14493\nxref: RHEA:14885\nxref: RHEA:20784\nis_a: GO:0016799 ! hydrolase activity, hydrolyzing N-glycosyl compounds\nis_a: GO:0140096 ! catalytic activity, acting on a protein\nproperty_value: skos:exactMatch EC:3.2.2.19\nproperty_value: skos:narrowMatch MetaCyc:3.2.2.24-RXN\nproperty_value: skos:narrowMatch MetaCyc:ADP-RIBOSYLARGININE-HYDROLASE-RXN\nproperty_value: skos:narrowMatch MetaCyc:RXN-8732\nproperty_value: skos:narrowMatch RHEA:14493\nproperty_value: skos:narrowMatch RHEA:14885\nproperty_value: skos:narrowMatch RHEA:20784\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003875",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 30576-30606",
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
  "excerpt": "[Term]\nid: GO:0008270\nname: zinc ion binding\nnamespace: molecular_function\ndef: \"Binding to a zinc ion (Zn).\" [GOC:ai]\nsynonym: \"zinc binding\" EXACT []\nsynonym: \"Zn binding\" EXACT []\nis_a: GO:0046914 ! transition metal ion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008270",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 81431-81439",
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
  "excerpt": "[Term]\nid: GO:0030414\nname: peptidase inhibitor activity\nnamespace: molecular_function\ndef: \"Binds to and stops, prevents or reduces the activity of a peptidase, any enzyme that catalyzes the hydrolysis peptide bonds.\" [GOC:jl]\nsynonym: \"protease inhibitor activity\" NARROW [GOC:mah]\nis_a: GO:0004857 ! enzyme inhibitor activity\nis_a: GO:0061134 ! peptidase regulator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030414",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 165960-165968",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 12. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
