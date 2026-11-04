# GO_molecular_function_0186

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0186.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — DNA-binding transcription factor activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSDLAKTAQRRALRSSGSARPDEDVPAPNRRGNRLPRDERRGQLLVVASDVFVDRGYHAAGMDEIADRAGVSKPVLYQHFSSKLELYLAVLHRHVENLVSGVHQALSTTTDNRQRLHVAVQAFFDFIEHDSQGYRLIFENDFVTEPEVAAQVRVATESCIDAVFALISADSGLDPHRARMIAVGLVGMSVDCARYWLDADKPISKSDAVEGTVQFAWGGLSHVPLTRS

[Multiple Choices]
A. DNA-binding transcription factor activity
B. zinc ion binding
C. nicotinamide-nucleotide adenylyltransferase activity
D. structural constituent of nuclear pore
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

> The sequence matches the annotated protein, whose function is described as a transcriptional activator that binds promoter operators. The GO annotation also assigns DNA-binding transcription factor activity; the functional description cites experimental evidence, while the GO annotation itself is IBA.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 228-aa sequence is compatible with a compact bacterial transcription regulator: its basic N-terminal region is consistent with a DNA-binding region, followed by a larger globular region that could support regulation or ligand sensing. This makes DNA-binding transcription factor activity meaningfully more plausible than the alternatives. There is no evident cysteine-rich zinc-binding motif, no clear basis for an NMN adenylyltransferase enzyme assignment, and a nuclear-pore structural role is implausible for a small protein with this sequence architecture.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family- or architecture-level inference from the sequence and general knowledge of bacterial regulators can distinguish A among these choices without knowing this exact protein's database annotation. The sequence alone does not prove DNA binding, so the inference is probabilistic.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered alternatives, DNA-binding transcription factor activity is the only one meaningfully supported by the sequence-level regulator-like features.


### Important caveats


<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 228-aa sequence is compatible with a compact bacterial transcription regulator: its basic N-terminal region is consistent with a DNA-binding region, followed by a larger globular region that could support regulation or ligand sensing. This makes DNA-binding transcription factor activity meaningfully more plausible than the alternatives. There is no evident cysteine-rich zinc-binding motif, no clear basis for an NMN adenylyltransferase enzyme assignment, and a nuclear-pore structural role is implausible for a small protein with this sequence architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family- or architecture-level inference from the sequence and general knowledge of bacterial regulators can distinguish A among these choices without knowing this exact protein's database annotation. The sequence alone does not prove DNA binding, so the inference is probabilistic."
  },
  "case_id": "GO_molecular_function_0186",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, whose function is described as a transcriptional activator that binds promoter operators. The GO annotation also assigns DNA-binding transcription factor activity; the functional description cites experimental evidence, while the GO annotation itself is IBA."
  },
  "important_caveats": [],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, DNA-binding transcription factor activity is the only one meaningfully supported by the sequence-level regulator-like features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0186",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, whose function is described as a transcriptional activator that binds promoter operators. The GO annotation also assigns DNA-binding transcription factor activity; the functional description cites experimental evidence, while the GO annotation itself is IBA.",
    "evidence_ids": ["C5", "C6", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 228-aa sequence is compatible with a compact bacterial transcription regulator: its basic N-terminal region is consistent with a DNA-binding region, followed by a larger globular region that could support regulation or ligand sensing. This makes DNA-binding transcription factor activity meaningfully more plausible than the alternatives. There is no evident cysteine-rich zinc-binding motif, no clear basis for an NMN adenylyltransferase enzyme assignment, and a nuclear-pore structural role is implausible for a small protein with this sequence architecture.",
    "missing_item_specific_fact": "",
    "reason": "A family- or architecture-level inference from the sequence and general knowledge of bacterial regulators can distinguish A among these choices without knowing this exact protein's database annotation. The sequence alone does not prove DNA binding, so the inference is probabilistic."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, DNA-binding transcription factor activity is the only one meaningfully supported by the sequence-level regulator-like features."
  },
  "important_caveats": []
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry O05858 (FasR_MYCTU) is annotated as 'HTH-type transcriptional activator FasR' with GO:0003700 (DNA-binding transcription factor activity). The function is supported by experimental evidence (ECO:0000269, PubMed:23721164, PubMed:32710080, PubMed:33193236) showing it specifically binds operator sequences in the fas-acpS promoter. X-ray crystallography (PDB 6O6N/6O6O/6O6P) confirms DNA binding in complex with acyl effector ligands.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H5](#evidence-h5), [H6](#evidence-h6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 228-residue sequence can be assessed against each option using general protein knowledge: (1) Against B (zinc ion binding): No canonical zinc-coordinating motifs are present—there is no C-x2-C-x12-H-x3-H zinc finger pattern, no C4 cluster, and no His-rich arrangement typical of zinc-binding sites. (2) Against C (nicotinamide-nucleotide adenylyltransferase activity): NMNAT enzymes possess conserved catalytic motifs (e.g., HGGH or similar adenylyltransferase signatures) and are typically larger; none are present here. (3) Against D (structural constituent of nuclear pore): Nucleoporins are typically >100 kDa with FG-repeat domains and are eukaryotic-specific; this small, bacterial-characteristic sequence (no signal peptide, no eukaryotic PTM motifs, no FG repeats) is incompatible. (4) For A (DNA-binding transcription factor activity): The protein's size (~228 aa) is typical of bacterial transcriptional regulators (e.g., TetR-family members). The N-terminal region contains a basic, potentially helical segment consistent with an HTH DNA-recognition motif, followed by a hydrophobic ligand-binding domain—architecture characteristic of small bacterial HTH transcription factors. The absence of features defining B, C, and D, combined with positive features (size, potential HTH, bacterial character) consistent with A, provides a credible elimination-based inference.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question is answerable through elimination of clearly incompatible options (B lacks zinc motifs, C lacks catalytic transferase motifs, D is incompatible in size/domain/organism type) and positive recognition of features consistent with a small bacterial HTH transcription factor. This uses general protein-family knowledge and sequence-feature recognition transferable from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B, C, and D are clearly excluded by the absence of their defining structural/sequence features. Option A is the only one consistent with the protein's size, domain architecture, and bacterial character. No other option is defensible.


### Important caveats

- The GO:0003700 annotation uses IBA:GO_Central (inferred by ancestry), but the underlying experimental evidence (DNA-binding assays, crystal structures with DNA) supports the function independently.
- The HTH motif identification from raw sequence without structural data is approximate; however, the elimination logic for B/C/D is robust and the positive features for A are sufficient in the context of four choices.
- The reviewer-only evidence confirms the sequence matches O05858 exactly (SHA256 match), validating applicability of all annotations.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 228-residue sequence can be assessed against each option using general protein knowledge: (1) Against B (zinc ion binding): No canonical zinc-coordinating motifs are present—there is no C-x2-C-x12-H-x3-H zinc finger pattern, no C4 cluster, and no His-rich arrangement typical of zinc-binding sites. (2) Against C (nicotinamide-nucleotide adenylyltransferase activity): NMNAT enzymes possess conserved catalytic motifs (e.g., HGGH or similar adenylyltransferase signatures) and are typically larger; none are present here. (3) Against D (structural constituent of nuclear pore): Nucleoporins are typically >100 kDa with FG-repeat domains and are eukaryotic-specific; this small, bacterial-characteristic sequence (no signal peptide, no eukaryotic PTM motifs, no FG repeats) is incompatible. (4) For A (DNA-binding transcription factor activity): The protein's size (~228 aa) is typical of bacterial transcriptional regulators (e.g., TetR-family members). The N-terminal region contains a basic, potentially helical segment consistent with an HTH DNA-recognition motif, followed by a hydrophobic ligand-binding domain—architecture characteristic of small bacterial HTH transcription factors. The absence of features defining B, C, and D, combined with positive features (size, potential HTH, bacterial character) consistent with A, provides a credible elimination-based inference.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through elimination of clearly incompatible options (B lacks zinc motifs, C lacks catalytic transferase motifs, D is incompatible in size/domain/organism type) and positive recognition of features consistent with a small bacterial HTH transcription factor. This uses general protein-family knowledge and sequence-feature recognition transferable from other proteins."
  },
  "case_id": "GO_molecular_function_0186",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H5",
      "H6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry O05858 (FasR_MYCTU) is annotated as 'HTH-type transcriptional activator FasR' with GO:0003700 (DNA-binding transcription factor activity). The function is supported by experimental evidence (ECO:0000269, PubMed:23721164, PubMed:32710080, PubMed:33193236) showing it specifically binds operator sequences in the fas-acpS promoter. X-ray crystallography (PDB 6O6N/6O6O/6O6P) confirms DNA binding in complex with acyl effector ligands."
  },
  "important_caveats": [
    "The GO:0003700 annotation uses IBA:GO_Central (inferred by ancestry), but the underlying experimental evidence (DNA-binding assays, crystal structures with DNA) supports the function independently.",
    "The HTH motif identification from raw sequence without structural data is approximate; however, the elimination logic for B/C/D is robust and the positive features for A are sufficient in the context of four choices.",
    "The reviewer-only evidence confirms the sequence matches O05858 exactly (SHA256 match), validating applicability of all annotations."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly excluded by the absence of their defining structural/sequence features. Option A is the only one consistent with the protein's size, domain architecture, and bacterial character. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0186",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry O05858 (FasR_MYCTU) is annotated as 'HTH-type transcriptional activator FasR' with GO:0003700 (DNA-binding transcription factor activity). The function is supported by experimental evidence (ECO:0000269, PubMed:23721164, PubMed:32710080, PubMed:33193236) showing it specifically binds operator sequences in the fas-acpS promoter. X-ray crystallography (PDB 6O6N/6O6O/6O6P) confirms DNA binding in complex with acyl effector ligands.",
    "evidence_ids": ["C4", "C5", "C6", "H5", "H6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 228-residue sequence can be assessed against each option using general protein knowledge: (1) Against B (zinc ion binding): No canonical zinc-coordinating motifs are present—there is no C-x2-C-x12-H-x3-H zinc finger pattern, no C4 cluster, and no His-rich arrangement typical of zinc-binding sites. (2) Against C (nicotinamide-nucleotide adenylyltransferase activity): NMNAT enzymes possess conserved catalytic motifs (e.g., HGGH or similar adenylyltransferase signatures) and are typically larger; none are present here. (3) Against D (structural constituent of nuclear pore): Nucleoporins are typically >100 kDa with FG-repeat domains and are eukaryotic-specific; this small, bacterial-characteristic sequence (no signal peptide, no eukaryotic PTM motifs, no FG repeats) is incompatible. (4) For A (DNA-binding transcription factor activity): The protein's size (~228 aa) is typical of bacterial transcriptional regulators (e.g., TetR-family members). The N-terminal region contains a basic, potentially helical segment consistent with an HTH DNA-recognition motif, followed by a hydrophobic ligand-binding domain—architecture characteristic of small bacterial HTH transcription factors. The absence of features defining B, C, and D, combined with positive features (size, potential HTH, bacterial character) consistent with A, provides a credible elimination-based inference.",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through elimination of clearly incompatible options (B lacks zinc motifs, C lacks catalytic transferase motifs, D is incompatible in size/domain/organism type) and positive recognition of features consistent with a small bacterial HTH transcription factor. This uses general protein-family knowledge and sequence-feature recognition transferable from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B, C, and D are clearly excluded by the absence of their defining structural/sequence features. Option A is the only one consistent with the protein's size, domain architecture, and bacterial character. No other option is defensible."
  },
  "important_caveats": [
    "The GO:0003700 annotation uses IBA:GO_Central (inferred by ancestry), but the underlying experimental evidence (DNA-binding assays, crystal structures with DNA) supports the function independently.",
    "The HTH motif identification from raw sequence without structural data is approximate; however, the elimination logic for B/C/D is robust and the positive features for A are sufficient in the context of four choices.",
    "The reviewer-only evidence confirms the sequence matches O05858 exactly (SHA256 match), validating applicability of all annotations."
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
  "benchmark_sequence_length": 228,
  "benchmark_sequence_sha256": "1621eedefff3630c8192cd5b4fcfd4879e875f8fbc8942b921307bce32788e81",
  "current_entry_audit": {
    "entryVersion": 172,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1997-07-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 228,
  "current_source_sequence_sha256": "1621eedefff3630c8192cd5b4fcfd4879e875f8fbc8942b921307bce32788e81",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 170,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O05858",
  "selected_historical_entry_version": 170,
  "selected_historical_record_sha256": "91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d",
  "selected_historical_source_sequence_length": 228,
  "selected_historical_source_sequence_sha256": "1621eedefff3630c8192cd5b4fcfd4879e875f8fbc8942b921307bce32788e81",
  "selected_historical_version": {
    "accession": "O05858",
    "database": "Swiss-Prot",
    "entryVersion": 170,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FASR_MYCTU",
    "sequenceVersion": 1
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O05858\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":172,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1997-07-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Mycobacteriales\",\"Mycobacteriaceae\",\"Mycobacterium\",\"Mycobacterium tuberculosis complex\"],\"scientificName\":\"Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv)\",\"taxonId\":83332}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"23721164\",\"source\":\"PubMed\"}],\"value\":\"Fatty acid synthesis regulator\"}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"HTH-type transcriptional activator FasR\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23721164\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32710080\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33193236\",\"source\":\"PubMed\"}],\"value\":\"Transcriptional activator that plays a central role in sensing mycobacterial long-chain fatty acids and regulating lipid biosynthesis (PubMed:23721164, PubMed:32710080, PubMed:33193236). Activates the expression of the genes encoding the fatty acid synthase (fas) and the 4-phosphopantetheinyl transferase (acpS), whose products are involved in the fatty acid and mycolic acid biosynthesis (PubMed:23721164, PubMed:33193236). Specifically binds to three conserved operator sequences present in the fas-acpS promoter region (PubMed:23721164). Not essential for M.tuberculosis viability, although it is required for the optimal growth in vitro and for virulence in macrophages and in a mouse model of infection (PubMed:33193236)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0003700\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:DNA-binding transcription factor activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/27",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0000976\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:transcription cis-regulatory region binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/28",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Mondino S.\",\"Gago G.\",\"Gramajo H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23721164\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.12282\"}],\"citationType\":\"journal article\",\"firstPage\":\"372\",\"id\":\"23721164\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"387\",\"publicationDate\":\"2013\",\"title\":\"Transcriptional regulation of fatty acid biosynthesis in mycobacteria.\",\"volume\":\"89\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"H37Rv\"}],\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"DNA-BINDING\",\"ACTIVITY REGULATION\",\"SUBUNIT\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Mondino S.\",\"Vazquez C.L.\",\"Cabruja M.\",\"Sala C.\",\"Cazenave-Gassiot A.\",\"Blanco F.C.\",\"Wenk M.R.\",\"Bigi F.\",\"Cole S.T.\",\"Gramajo H.\",\"Gago G.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33193236\"},{\"database\":\"DOI\",\"id\":\"10.3389/fmicb.2020.586285\"}],\"citationType\":\"journal article\",\"firstPage\":\"586285\",\"id\":\"33193236\",\"journal\":\"Front. Microbiol.\",\"lastPage\":\"586285\",\"publicationDate\":\"2020\",\"title\":\"FasR Regulates Fatty Acid Biosynthesis and Is Essential for Virulence of Mycobacterium tuberculosis.\",\"volume\":\"11\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"H37Rv\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O05858.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Lara J.\",\"Diacovich L.\",\"Trajtenberg F.\",\"Larrieux N.\",\"Malchiodi E.L.\",\"Fernandez M.M.\",\"Gago G.\",\"Gramajo H.\",\"Buschiazzo A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32710080\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-020-17504-x\"}],\"citationType\":\"journal article\",\"firstPage\":\"3703\",\"id\":\"32710080\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"3703\",\"publicationDate\":\"2020\",\"title\":\"Mycobacterium tuberculosis FasR senses long fatty acyl-CoA through a tunnel and a hydrophobic transmission spine.\",\"volume\":\"11\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6O6N\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6O6O\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6O6P\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"H37Rv\"}],\"referenceNumber\":5,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.63 ANGSTROMS) IN COMPLEX WITH ACYL EFFECTOR LIGANDS AND DNA\",\"FUNCTION\",\"ACTIVITY REGULATION\",\"SUBUNIT\",\"DOMAIN\",\"MUTAGENESIS OF LEU-98; LEU-106 AND PHE-123\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/4",
  "retrieved_utc": "2026-11-02T04:29:07.365865+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "fdecd845a2166f556987ddc68c2d2d2aba810cb32cc1ba0ae64c5acbb7547fd1",
  "url": "https://rest.uniprot.org/uniprotkb/O05858.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)

```json
{
  "entry_version": 170,
  "evidence_id": "H1",
  "excerpt": "ID   FASR_MYCTU              Reviewed;         228 AA.\nAC   O05858; F2GK79; I6Y2X8; Q7D5X8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUL-1997, sequence version 1.\nDT   28-JAN-2026, entry version 170.\nDE   RecName: Full=HTH-type transcriptional activator FasR {ECO:0000305};\nDE   AltName: Full=Fatty acid synthesis regulator {ECO:0000303|PubMed:23721164};\nGN   Name=fasR {ECO:0000303|PubMed:23721164};\nGN   OrderedLocusNames=Rv3208 {ECO:0000312|EMBL:CCP46023.1};\nOS   Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv).\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Mycobacteriales;\nOC   Mycobacteriaceae; Mycobacterium; Mycobacterium tuberculosis complex.\nOX   NCBI_TaxID=83332;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:12.681576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d",
  "url": "https://rest.uniprot.org/unisave/O05858?format=txt&versions=170"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)

```json
{
  "entry_version": 170,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   FUNCTION, DNA-BINDING, ACTIVITY REGULATION, AND SUBUNIT.\nRC   STRAIN=H37Rv;\nRX   PubMed=23721164; DOI=10.1111/mmi.12282;\nRA   Mondino S., Gago G., Gramajo H.;\nRT   \"Transcriptional regulation of fatty acid biosynthesis in mycobacteria.\";\nRL   Mol. Microbiol. 89:372-387(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:12.681576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d",
  "url": "https://rest.uniprot.org/unisave/O05858?format=txt&versions=170"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)

```json
{
  "entry_version": 170,
  "evidence_id": "H3",
  "excerpt": "RN   [4]\nRP   FUNCTION, AND DISRUPTION PHENOTYPE.\nRC   STRAIN=H37Rv;\nRX   PubMed=33193236; DOI=10.3389/fmicb.2020.586285;\nRA   Mondino S., Vazquez C.L., Cabruja M., Sala C., Cazenave-Gassiot A.,\nRA   Blanco F.C., Wenk M.R., Bigi F., Cole S.T., Gramajo H., Gago G.;\nRT   \"FasR Regulates Fatty Acid Biosynthesis and Is Essential for Virulence of\nRT   Mycobacterium tuberculosis.\";\nRL   Front. Microbiol. 11:586285-586285(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:12.681576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d",
  "url": "https://rest.uniprot.org/unisave/O05858?format=txt&versions=170"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)

```json
{
  "entry_version": 170,
  "evidence_id": "H4",
  "excerpt": "RN   [5] {ECO:0007744|PDB:6O6N, ECO:0007744|PDB:6O6O, ECO:0007744|PDB:6O6P}\nRP   X-RAY CRYSTALLOGRAPHY (1.63 ANGSTROMS) IN COMPLEX WITH ACYL EFFECTOR\nRP   LIGANDS AND DNA, FUNCTION, ACTIVITY REGULATION, SUBUNIT, DOMAIN, AND\nRP   MUTAGENESIS OF LEU-98; LEU-106 AND PHE-123.\nRC   STRAIN=H37Rv;\nRX   PubMed=32710080; DOI=10.1038/s41467-020-17504-x;\nRA   Lara J., Diacovich L., Trajtenberg F., Larrieux N., Malchiodi E.L.,\nRA   Fernandez M.M., Gago G., Gramajo H., Buschiazzo A.;\nRT   \"Mycobacterium tuberculosis FasR senses long fatty acyl-CoA through a\nRT   tunnel and a hydrophobic transmission spine.\";\nRL   Nat. Commun. 11:3703-3703(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:12.681576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-66",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d",
  "url": "https://rest.uniprot.org/unisave/O05858?format=txt&versions=170"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)

```json
{
  "entry_version": 170,
  "evidence_id": "H5",
  "excerpt": "CC   -!- FUNCTION: Transcriptional activator that plays a central role in\nCC       sensing mycobacterial long-chain fatty acids and regulating lipid\nCC       biosynthesis (PubMed:23721164, PubMed:32710080, PubMed:33193236).\nCC       Activates the expression of the genes encoding the fatty acid synthase\nCC       (fas) and the 4-phosphopantetheinyl transferase (acpS), whose products\nCC       are involved in the fatty acid and mycolic acid biosynthesis\nCC       (PubMed:23721164, PubMed:33193236). Specifically binds to three\nCC       conserved operator sequences present in the fas-acpS promoter region\nCC       (PubMed:23721164). Not essential for M.tuberculosis viability, although\nCC       it is required for the optimal growth in vitro and for virulence in\nCC       macrophages and in a mouse model of infection (PubMed:33193236).\nCC       {ECO:0000269|PubMed:23721164, ECO:0000269|PubMed:32710080,\nCC       ECO:0000269|PubMed:33193236}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:12.681576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-79",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d",
  "url": "https://rest.uniprot.org/unisave/O05858?format=txt&versions=170"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)

```json
{
  "entry_version": 170,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0003700; F:DNA-binding transcription factor activity; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:12.681576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 137-137",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d",
  "url": "https://rest.uniprot.org/unisave/O05858?format=txt&versions=170"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O05858?format=txt&versions=170)

```json
{
  "entry_version": 170,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0000976; F:transcription cis-regulatory region binding; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:12.681576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 138-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "91cae8ebaffc3d1817ee5aa4f4cebdc7a53b7c5509e61df55a7e6f08fd13e47d",
  "url": "https://rest.uniprot.org/unisave/O05858?format=txt&versions=170"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000309\nname: nicotinamide-nucleotide adenylyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: beta-nicotinamide D-ribonucleotide + ATP + H+ = diphosphate + NAD+.\" [RHEA:21360]\nsynonym: \"adenosine triphosphate-nicotinamide mononucleotide transadenylase activity\" RELATED [EC:2.7.7.1]\nsynonym: \"ATP:nicotinamide-nucleotide adenylyltransferase activity\" EXACT []\nsynonym: \"ATP:NMN adenylyltransferase activity\" RELATED [EC:2.7.7.1]\nsynonym: \"diphosphopyridine nucleotide pyrophosphorylase activity\" RELATED [EC:2.7.7.1]\nsynonym: \"NAD(+) diphosphorylase activity\" NARROW [EC:2.7.7.1]\nsynonym: \"NAD(+) pyrophosphorylase activity\" NARROW [EC:2.7.7.1]\nsynonym: \"NAD+ diphosphorylase activity\" RELATED [EC:2.7.7.1]\nsynonym: \"NAD+ pyrophosphorylase activity\" RELATED [EC:2.7.7.1]\nsynonym: \"nicotinamide adenine dinucleotide pyrophosphorylase activity\" NARROW [EC:2.7.7.1]\nsynonym: \"nicotinamide mononucleotide adenylyltransferase activity\" NARROW [EC:2.7.7.1]\nsynonym: \"NMN adenylyltransferase activity\" NARROW [EC:2.7.7.1]\nsynonym: \"NMNAT activity\" NARROW [EC:2.7.7.1]\nxref: EC:2.7.7.1\nxref: MetaCyc:2.7.7.1-RXN\nxref: Reactome:R-HSA-8939959 \"NMNAT2 transfers an adenylyl group from ATP to NMN to yield NAD+\"\nxref: RHEA:21360\nis_a: GO:0070566 ! adenylyltransferase activity\nproperty_value: skos:exactMatch EC:2.7.7.1\nproperty_value: skos:exactMatch MetaCyc:2.7.7.1-RXN\nproperty_value: skos:exactMatch RHEA:21360\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000309",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 3347-3372",
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
  "excerpt": "[Term]\nid: GO:0003700\nname: DNA-binding transcription factor activity\nnamespace: molecular_function\nalt_id: GO:0000130\nalt_id: GO:0001071\nalt_id: GO:0001130\nalt_id: GO:0001131\nalt_id: GO:0001151\nalt_id: GO:0001199\nalt_id: GO:0001204\ndef: \"A transcription regulator activity that modulates transcription of gene sets via selective and non-covalent binding to a specific double-stranded genomic DNA sequence (sometimes referred to as a motif) within a cis-regulatory region. Regulatory regions include promoters (proximal and distal) and enhancers. Genes are transcriptional units, and include bacterial operons.\" [GOC:txnOH-2018]\ncomment: Usage guidance: Most DNA-binding transcription factors do not have enzymatic activity. The presence of specific DNA-binding domains known to be present in DNA-binding transcription factors (HOX, GATA etc) should be used to help decide whether a protein is a DNA binding transcription factor or a coregulator. If a protein has an enzymatic activity (for example, ubiquitin ligase, histone acetyl transferase) and no known DNA binding domain, consider annotating to GO:0003712 transcription coregulator activity. Special care should be taken with proteins containing zinc fingers, Myb/SANT and ARID domains, since only a subset of proteins containing these domains directly and selectively bind to regulatory DNA motifs in cis-regulatory regions.\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_yeast\nsynonym: \"bacterial-type DNA binding transcription factor activity\" NARROW []\nsynonym: \"bacterial-type RNA polymerase core promoter proximal region sequence-specific DNA binding transcription factor activity\" NARROW []\nsynonym: \"bacterial-type RNA polymerase transcription enhancer sequence-specific DNA binding transcription factor activity\" NARROW []\nsynonym: \"bacterial-type RNA polymerase transcription factor activity, metal ion regulated sequence-specific DNA binding\" NARROW []\nsynonym: \"bacterial-type RNA polymerase transcription factor activity, sequence-specific DNA binding\" NARROW []\nsynonym: \"DNA binding transcription factor activity\" EXACT []\nsynonym: \"gene-specific transcription factor activity\" EXACT []\nsynonym: \"metal ion regulated sequence-specific DNA binding bacterial-type RNA polymerase transcription factor activity\" NARROW []\nsynonym: \"metal ion regulated sequence-specific DNA binding transcription factor activity\" NARROW []\nsynonym: \"nucleic acid binding transcription factor activity\" BROAD []\nsynonym: \"sequence-specific DNA binding bacterial-type RNA polymerase transcription factor activity\" NARROW []\nsynonym: \"sequence-specific DNA binding transcription factor activity\" EXACT []\nsynonym: \"transcription factor activity\" BROAD []\nsynonym: \"transcription factor activity, bacterial-type RNA polymerase core promoter proximal region sequence-specific binding\" NARROW []\nsynonym: \"transcription factor activity, bacterial-type RNA polymerase proximal promoter sequence-specific DNA binding\" NARROW []\nsynonym: \"transcription factor activity, bacterial-type RNA polymerase transcription enhancer sequence-specific binding\" NARROW []\nsynonym: \"transcription factor activity, metal ion regulated sequence-specific DNA binding\" NARROW []\nxref: Reactome:R-HSA-163666 \"Formation of ChREBP:MLX heterodimer\"\nis_a: GO:0140110 ! transcription regulator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003700",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 28009-28049",
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
  "excerpt": "[Term]\nid: GO:0017056\nname: structural constituent of nuclear pore\nnamespace: molecular_function\nalt_id: GO:0005487\ndef: \"The action of a molecule that contributes to the structural integrity of the nuclear pore complex, a protein-lined channel in the nuclear envelope that allows the transfer of macromolecules.\" [GOC:mah, PMID:25802992]\ncomment: Note that this term is meant to be used for nuclear pore proteins. For importins and exportins, consider 'nuclear import signal receptor activity' or 'nuclear export signal receptor activity', respectively.\nsynonym: \"nuclear pore activity\" RELATED []\nsynonym: \"nucleocytoplasmic transporter activity\" EXACT []\nxref: Reactome:R-HSA-1176059 \"Translocation of Influenza A virus nonstructural protein 1 (NS1A) into the nucleus\"\nxref: Reactome:R-HSA-170796 \"NPC transports GCK1:GCKR from cytosol to nucleoplasm\"\nxref: Reactome:R-HSA-192627 \"Viral mRNA Export\"\nxref: Reactome:R-HSA-192925 \"Export of Spliced Viral mRNA\"\nxref: Reactome:R-HSA-5252041 \"NPC transports Hikeshi:HSP70s:ATP from cytosol to nucleoplasm\"\nxref: Reactome:R-HSA-5661474 \"Defective NPC does not transport GCK1:GKRP from cytosol to nucleoplasm\"\nxref: Reactome:R-HSA-6783483 \"tRNA:XPOT:RAN:GTP translocates from the nucleus to the cytosol\"\nis_a: GO:0005198 ! structural molecule activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0017056",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 132832-132849",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 186. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
