# GO_molecular_function_0082

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0082.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — aspartate kinase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSQSPTNVPRSYNSVLDLKLASPTNSASGATGGWIVQKFGGTSVGKFPENIVDNIVKVYSQTNRVAVVCSARSSQTKSEGTTSRLLRSADLAENDKDYQPLLNAIEEDHVTNAERIQSEEIKQELIKDTKQEIEHVRELLHACQIIGEISPRSLDSIMAVGEKLSCLFMTALMKDHGLNAVYINLQDVIPLSYDFQKGFDDSFYQFLSQEIGKRVLQCDKEREGEEDVIPVLTGYFGVVPGGLLNGVGRGYTDLCAALAAVALQADELQIWKEVDGIFTADPRKVPNARLLDSVTPEEAAELTYYGSEVIHPFTMEQVIRAKIPIRIKNVENPTGKGTIIYPDNIGRRGEATPPHPPAAFEQLAMSSLLQRKRSATAITAKQDIVVINIHSNKKTLSHGFLAHVFTTLDKYKLVVDLISTSEVHVSMALSIQSDQESQLKHALVDLRKMGTVDVTKKMTIVSLVGKQMVNFIGIAGNMFKVLADEKINIEMISQGANEINISAVINEKDTIRALKSIHAKLLEGGSAIGDSSAVDTRLEALKLS

[Multiple Choices]
A. aspartate kinase activity
B. dioxygenase activity
C. mannose-6-phosphate isomerase activity
D. O-methyltransferase activity
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

> The matched sequence is annotated as an aspartokinase, with the reaction L-aspartate + ATP → 4-phospho-L-aspartate + ADP. The cited functional evidence is transferred from a related UniProtKB entry (ECO:0000250), rather than direct experimental evidence for this sequence; the historical record nevertheless supports choice A.

Citations as saved: [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the conserved aspartokinase family: a soluble enzyme with an N-terminal region compatible with nucleotide-dependent catalysis and additional regulatory-domain-like regions, a characteristic architecture of many aspartokinases. Family-level sequence and domain-pattern recognition can favor aspartate kinase over the alternatives, which represent distinct isomerase, dioxygenase, and methyltransferase enzyme families.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model need not know this exact protein's database annotation to make a meaningful family-level inference from the sequence and choices. That inference is not experimental proof and may depend on recognizing conserved family patterns.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices describe distinct molecular activities, and the sequence/family inference meaningfully favors aspartate kinase.


### Important caveats

- The supplied annotation's catalytic and functional evidence is transferred by similarity, not evidence of direct biochemical testing of this exact protein.
- The historical record is sequence-matched, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the conserved aspartokinase family: a soluble enzyme with an N-terminal region compatible with nucleotide-dependent catalysis and additional regulatory-domain-like regions, a characteristic architecture of many aspartokinases. Family-level sequence and domain-pattern recognition can favor aspartate kinase over the alternatives, which represent distinct isomerase, dioxygenase, and methyltransferase enzyme families.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model need not know this exact protein's database annotation to make a meaningful family-level inference from the sequence and choices. That inference is not experimental proof and may depend on recognizing conserved family patterns."
  },
  "case_id": "GO_molecular_function_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as an aspartokinase, with the reaction L-aspartate + ATP → 4-phospho-L-aspartate + ADP. The cited functional evidence is transferred from a related UniProtKB entry (ECO:0000250), rather than direct experimental evidence for this sequence; the historical record nevertheless supports choice A."
  },
  "important_caveats": [
    "The supplied annotation's catalytic and functional evidence is transferred by similarity, not evidence of direct biochemical testing of this exact protein.",
    "The historical record is sequence-matched, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe distinct molecular activities, and the sequence/family inference meaningfully favors aspartate kinase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as an aspartokinase, with the reaction L-aspartate + ATP → 4-phospho-L-aspartate + ADP. The cited functional evidence is transferred from a related UniProtKB entry (ECO:0000250), rather than direct experimental evidence for this sequence; the historical record nevertheless supports choice A.",
    "evidence_ids": ["H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the conserved aspartokinase family: a soluble enzyme with an N-terminal region compatible with nucleotide-dependent catalysis and additional regulatory-domain-like regions, a characteristic architecture of many aspartokinases. Family-level sequence and domain-pattern recognition can favor aspartate kinase over the alternatives, which represent distinct isomerase, dioxygenase, and methyltransferase enzyme families.",
    "missing_item_specific_fact": "",
    "reason": "A model need not know this exact protein's database annotation to make a meaningful family-level inference from the sequence and choices. That inference is not experimental proof and may depend on recognizing conserved family patterns."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe distinct molecular activities, and the sequence/family inference meaningfully favors aspartate kinase."
  },
  "important_caveats": [
    "The supplied annotation's catalytic and functional evidence is transferred by similarity, not evidence of direct biochemical testing of this exact protein.",
    "The historical record is sequence-matched, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A1D8PMB8 (AK_CANAL) annotates this protein as Aspartokinase (EC 2.7.2.4) with GO:0004072 (aspartate kinase activity). The sequence in the question matches the UniProt sequence exactly (544 aa, SHA256 match). The annotation is based on sequence similarity (ECO:0000250 to P10869) and IBA (inferred by biological ancestor), which is a computational/transferred annotation rather than direct experimental evidence, but it is a well-established family-level assignment for this protein. The catalytic reaction (L-aspartate + ATP = 4-phospho-L-aspartate + ADP) and function description are consistent with the expected answer.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable motifs of the amino acid kinase superfamily (Pfam PF00696): a glycine-rich ATP-binding region ('GFGVVPGGLLNGVGRGYTDLCAALAAVALQ') and the conserved 'KGT' motif in 'VENPTGKGTIIYPDNIGRRGE', which is a hallmark of the amino acid kinase catalytic domain shared across family members studied in E. coli (LysC), S. typhimurium, and other organisms. The N-terminal region is consistent with an ACT (aspartate kinase, chorismate mutase, TyrA) regulatory domain, which is specifically characteristic of aspartate kinase among amino acid kinases. Among the four offered choices, only option A (aspartate kinase) belongs to the amino acid kinase/phosphotransferase class. The other three options belong to entirely different enzyme classes with incompatible structural and sequence signatures: dioxygenases (option B) require Fe(II)/2-OG or heme cofactor motifs (2-His-1-carboxylate facial triad) absent here; mannose-6-phosphate isomerase (option C) is a TIM-barrel isomerase with a completely different fold and sequence; O-methyltransferases (option D) require SAM-binding Rossmann-like motifs (e.g., 'VLDVGVGSG') absent from this sequence. Thus, family-level recognition of the amino acid kinase fold and ACT domain, combined with elimination of structurally incompatible alternatives, meaningfully distinguishes option A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model trained on protein families can recognize the amino acid kinase superfamily motifs (KGT, glycine-rich loops) and the ACT regulatory domain from the raw sequence. These are transferable features learned from other amino acid kinases (LysC, ArgB, GlnB, etc.). Among the four choices, only aspartate kinase is a phosphotransferase/amino acid kinase; the other three are structurally and mechanistically incompatible with the observed motifs. No target-specific database lookup is required to make this family-level distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span four distinct enzyme classes (kinase, dioxygenase, isomerase, methyltransferase) with fundamentally different catalytic mechanisms and structural folds. The sequence features unambiguously point to the amino acid kinase class, and only one option (A) belongs to that class. No other option is defensible given the sequence evidence.


### Important caveats

- The UniProt annotation for this entry is based on sequence similarity (ECO:0000250) and inferred by biological ancestor (IBA), not on direct experimental characterization of this specific Candida albicans protein.
- The amino acid kinase superfamily includes multiple members (aspartate kinase, glutamate 5-kinase, N-acetylglutamate kinase, etc.); the specific assignment to 'aspartate kinase' rather than another amino acid kinase relies on the ACT domain and broader family context, but among the four offered choices only one is an amino acid kinase, so this sub-distinction does not affect the answer.
- The sequence is from Candida albicans (a fungal organism), and the annotation was transferred from P10869 (likely a better-characterized homolog). The reviewer-only evidence confirms sequence match but does not constitute experimental validation for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable motifs of the amino acid kinase superfamily (Pfam PF00696): a glycine-rich ATP-binding region ('GFGVVPGGLLNGVGRGYTDLCAALAAVALQ') and the conserved 'KGT' motif in 'VENPTGKGTIIYPDNIGRRGE', which is a hallmark of the amino acid kinase catalytic domain shared across family members studied in E. coli (LysC), S. typhimurium, and other organisms. The N-terminal region is consistent with an ACT (aspartate kinase, chorismate mutase, TyrA) regulatory domain, which is specifically characteristic of aspartate kinase among amino acid kinases. Among the four offered choices, only option A (aspartate kinase) belongs to the amino acid kinase/phosphotransferase class. The other three options belong to entirely different enzyme classes with incompatible structural and sequence signatures: dioxygenases (option B) require Fe(II)/2-OG or heme cofactor motifs (2-His-1-carboxylate facial triad) absent here; mannose-6-phosphate isomerase (option C) is a TIM-barrel isomerase with a completely different fold and sequence; O-methyltransferases (option D) require SAM-binding Rossmann-like motifs (e.g., 'VLDVGVGSG') absent from this sequence. Thus, family-level recognition of the amino acid kinase fold and ACT domain, combined with elimination of structurally incompatible alternatives, meaningfully distinguishes option A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model trained on protein families can recognize the amino acid kinase superfamily motifs (KGT, glycine-rich loops) and the ACT regulatory domain from the raw sequence. These are transferable features learned from other amino acid kinases (LysC, ArgB, GlnB, etc.). Among the four choices, only aspartate kinase is a phosphotransferase/amino acid kinase; the other three are structurally and mechanistically incompatible with the observed motifs. No target-specific database lookup is required to make this family-level distinction."
  },
  "case_id": "GO_molecular_function_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A1D8PMB8 (AK_CANAL) annotates this protein as Aspartokinase (EC 2.7.2.4) with GO:0004072 (aspartate kinase activity). The sequence in the question matches the UniProt sequence exactly (544 aa, SHA256 match). The annotation is based on sequence similarity (ECO:0000250 to P10869) and IBA (inferred by biological ancestor), which is a computational/transferred annotation rather than direct experimental evidence, but it is a well-established family-level assignment for this protein. The catalytic reaction (L-aspartate + ATP = 4-phospho-L-aspartate + ADP) and function description are consistent with the expected answer."
  },
  "important_caveats": [
    "The UniProt annotation for this entry is based on sequence similarity (ECO:0000250) and inferred by biological ancestor (IBA), not on direct experimental characterization of this specific Candida albicans protein.",
    "The amino acid kinase superfamily includes multiple members (aspartate kinase, glutamate 5-kinase, N-acetylglutamate kinase, etc.); the specific assignment to 'aspartate kinase' rather than another amino acid kinase relies on the ACT domain and broader family context, but among the four offered choices only one is an amino acid kinase, so this sub-distinction does not affect the answer.",
    "The sequence is from Candida albicans (a fungal organism), and the annotation was transferred from P10869 (likely a better-characterized homolog). The reviewer-only evidence confirms sequence match but does not constitute experimental validation for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct enzyme classes (kinase, dioxygenase, isomerase, methyltransferase) with fundamentally different catalytic mechanisms and structural folds. The sequence features unambiguously point to the amino acid kinase class, and only one option (A) belongs to that class. No other option is defensible given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A1D8PMB8 (AK_CANAL) annotates this protein as Aspartokinase (EC 2.7.2.4) with GO:0004072 (aspartate kinase activity). The sequence in the question matches the UniProt sequence exactly (544 aa, SHA256 match). The annotation is based on sequence similarity (ECO:0000250 to P10869) and IBA (inferred by biological ancestor), which is a computational/transferred annotation rather than direct experimental evidence, but it is a well-established family-level assignment for this protein. The catalytic reaction (L-aspartate + ATP = 4-phospho-L-aspartate + ADP) and function description are consistent with the expected answer.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H3", "H4", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable motifs of the amino acid kinase superfamily (Pfam PF00696): a glycine-rich ATP-binding region ('GFGVVPGGLLNGVGRGYTDLCAALAAVALQ') and the conserved 'KGT' motif in 'VENPTGKGTIIYPDNIGRRGE', which is a hallmark of the amino acid kinase catalytic domain shared across family members studied in E. coli (LysC), S. typhimurium, and other organisms. The N-terminal region is consistent with an ACT (aspartate kinase, chorismate mutase, TyrA) regulatory domain, which is specifically characteristic of aspartate kinase among amino acid kinases. Among the four offered choices, only option A (aspartate kinase) belongs to the amino acid kinase/phosphotransferase class. The other three options belong to entirely different enzyme classes with incompatible structural and sequence signatures: dioxygenases (option B) require Fe(II)/2-OG or heme cofactor motifs (2-His-1-carboxylate facial triad) absent here; mannose-6-phosphate isomerase (option C) is a TIM-barrel isomerase with a completely different fold and sequence; O-methyltransferases (option D) require SAM-binding Rossmann-like motifs (e.g., 'VLDVGVGSG') absent from this sequence. Thus, family-level recognition of the amino acid kinase fold and ACT domain, combined with elimination of structurally incompatible alternatives, meaningfully distinguishes option A.",
    "missing_item_specific_fact": "",
    "reason": "A model trained on protein families can recognize the amino acid kinase superfamily motifs (KGT, glycine-rich loops) and the ACT regulatory domain from the raw sequence. These are transferable features learned from other amino acid kinases (LysC, ArgB, GlnB, etc.). Among the four choices, only aspartate kinase is a phosphotransferase/amino acid kinase; the other three are structurally and mechanistically incompatible with the observed motifs. No target-specific database lookup is required to make this family-level distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct enzyme classes (kinase, dioxygenase, isomerase, methyltransferase) with fundamentally different catalytic mechanisms and structural folds. The sequence features unambiguously point to the amino acid kinase class, and only one option (A) belongs to that class. No other option is defensible given the sequence evidence."
  },
  "important_caveats": [
    "The UniProt annotation for this entry is based on sequence similarity (ECO:0000250) and inferred by biological ancestor (IBA), not on direct experimental characterization of this specific Candida albicans protein.",
    "The amino acid kinase superfamily includes multiple members (aspartate kinase, glutamate 5-kinase, N-acetylglutamate kinase, etc.); the specific assignment to 'aspartate kinase' rather than another amino acid kinase relies on the ACT domain and broader family context, but among the four offered choices only one is an amino acid kinase, so this sub-distinction does not affect the answer.",
    "The sequence is from Candida albicans (a fungal organism), and the annotation was transferred from P10869 (likely a better-characterized homolog). The reviewer-only evidence confirms sequence match but does not constitute experimental validation for this exact protein."
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
  "benchmark_sequence_length": 544,
  "benchmark_sequence_sha256": "a70e31c973f256dd8bc7aaccfa7ecf4ba1619ab22a51f5845f097e63766efe67",
  "current_entry_audit": {
    "entryVersion": 41,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-01-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 544,
  "current_source_sequence_sha256": "a70e31c973f256dd8bc7aaccfa7ecf4ba1619ab22a51f5845f097e63766efe67",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 39,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A1D8PMB8",
  "selected_historical_entry_version": 39,
  "selected_historical_record_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "selected_historical_source_sequence_length": 544,
  "selected_historical_source_sequence_sha256": "a70e31c973f256dd8bc7aaccfa7ecf4ba1619ab22a51f5845f097e63766efe67",
  "selected_historical_version": {
    "accession": "A0A1D8PMB8",
    "database": "Swiss-Prot",
    "entryVersion": 39,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AK_CANAL",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1D8PMB8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":41,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-01-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Debaryomycetaceae\",\"Candida/Lodderomyces clade\",\"Candida\"],\"scientificName\":\"Candida albicans (strain SC5314 / ATCC MYA-2876)\",\"taxonId\":237561}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.2.4\"}],\"fullName\":{\"value\":\"Aspartokinase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"value\":\"Phosphorylates aspartate, the first step in the biosynthesis of amino acids that derive from aspartate (the aspartate family of amino acids), including methioinine and threonine, the latter of which is a precursor to isoleucine\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:23777\"}}],\"reaction\":{\"ecNumber\":\"2.7.2.4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"name\":\"L-aspartate + ATP = 4-phospho-L-aspartate + ADP\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:23776\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29991\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57535\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004072\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:aspartate kinase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/19",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H1",
  "excerpt": "ID   AK_CANAL                Reviewed;         544 AA.\nAC   A0A1D8PMB8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JAN-2017, sequence version 1.\nDT   18-JUN-2025, entry version 39.\nDE   RecName: Full=Aspartokinase;\nDE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};\nGN   Name=HOM3 {ECO:0000312|CGD:CAL0000181037};\nGN   OrderedLocusNames=CAALFM_C405540WA {ECO:0000312|EMBL:AOW29286.1},\nGN   orf19.8820 {ECO:0000312|CGD:CAL0000181037};\nOS   Candida albicans (strain SC5314 / ATCC MYA-2876) (Yeast).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Debaryomycetaceae; Candida/Lodderomyces clade; Candida.\nOX   NCBI_TaxID=237561 {ECO:0000312|Proteomes:UP000000559};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H2",
  "excerpt": "CC   -!- FUNCTION: Phosphorylates aspartate, the first step in the biosynthesis\nCC       of amino acids that derive from aspartate (the aspartate family of\nCC       amino acids), including methioinine and threonine, the latter of which\nCC       is a precursor to isoleucine. {ECO:0000250|UniProtKB:P10869}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-aspartate + ATP = 4-phospho-L-aspartate + ADP;\nCC         Xref=Rhea:RHEA:23776, ChEBI:CHEBI:29991, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:57535, ChEBI:CHEBI:456216; EC=2.7.2.4;\nCC         Evidence={ECO:0000250|UniProtKB:P10869};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23777;\nCC         Evidence={ECO:0000250|UniProtKB:P10869};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0004072; F:aspartate kinase activity; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-104",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005524; F:ATP binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 105-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004072\nname: aspartate kinase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: L-aspartate + ATP = 4-phospho-L-aspartate + ADP + H+.\" [EC:2.7.2.4, RHEA:23776]\nsynonym: \"aspartic kinase activity\" RELATED [EC:2.7.2.4]\nsynonym: \"aspartokinase activity\" RELATED [EC:2.7.2.4]\nsynonym: \"ATP:L-aspartate 4-phosphotransferase activity\" RELATED [EC:2.7.2.4]\nsynonym: \"beta-aspartokinase activity\" RELATED [EC:2.7.2.4]\nxref: EC:2.7.2.4\nxref: KEGG_REACTION:R00480\nxref: MetaCyc:ASPARTATEKIN-RXN\nxref: RHEA:23776\nis_a: GO:0016774 ! phosphotransferase activity, carboxyl group as acceptor\nis_a: GO:0019202 ! amino acid kinase activity\nproperty_value: skos:exactMatch EC:2.7.2.4\nproperty_value: skos:exactMatch RHEA:23776\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004072",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 34816-34833",
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
  "excerpt": "[Term]\nid: GO:0004476\nname: mannose-6-phosphate isomerase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: D-mannose 6-phosphate = D-fructose 6-phosphate.\" [RHEA:12356]\nsynonym: \"D-mannose-6-phosphate aldose-ketose-isomerase activity\" RELATED [EC:5.3.1.8]\nsynonym: \"D-mannose-6-phosphate ketol-isomerase activity\" RELATED [EC:5.3.1.8]\nsynonym: \"mannose phosphate isomerase activity\" RELATED [EC:5.3.1.8]\nsynonym: \"phosphohexoisomerase activity\" BROAD [EC:5.3.1.8]\nsynonym: \"phosphohexomutase activity\" BROAD [EC:5.3.1.8]\nsynonym: \"phosphomannoisomerase activity\" RELATED [EC:5.3.1.8]\nsynonym: \"phosphomannose isomerase activity\" RELATED [EC:5.3.1.8]\nxref: EC:5.3.1.8\nxref: MetaCyc:MANNPISOM-RXN\nxref: Reactome:R-HSA-3781832 \"Defective MPI does not  isomerize Fru6P to Man6P\"\nxref: Reactome:R-HSA-532549 \"MPI isomerises Fru6P to Man6P\"\nxref: RHEA:12356\nis_a: GO:0016861 ! intramolecular oxidoreductase activity, interconverting aldoses and ketoses\nproperty_value: skos:exactMatch EC:5.3.1.8\nproperty_value: skos:exactMatch RHEA:12356\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004476",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 42843-42863",
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
  "excerpt": "[Term]\nid: GO:0008171\nname: O-methyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a methyl group to the oxygen atom of an acceptor molecule.\" [GOC:ai]\nxref: Reactome:R-HSA-5578717 \"BCDIN3D dimethylates 5' phosphate of pre-miR-145\"\nxref: Reactome:R-HSA-5629203 \"HENMT1 methylates 2' hydroxyl at 3' end of piRNA in 4xMeR-PIWIL1:piRNA:TDRD6:TDRKH\"\nxref: Reactome:R-HSA-5629218 \"HENMT1 methylates 2' hydroxyl at 3' end of piRNA in 6xMeR-PIWIL2:piRNA:TDRD1:TDRD12:DDX4:ASZ:MOV10L1\"\nxref: Reactome:R-HSA-5629237 \"HENMT1 methylates 2' hydroxyl at 3' end of piRNA in MeR-PIWIL4:piRNA:TDRD9:MAEL:TDRKH\"\nxref: Reactome:R-HSA-6790907 \"Box C/D snoRNP methylates ribonucleotides in pre-rRNA yielding 2'-O-methylribonucleotides\"\nis_a: GO:0008168 ! methyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008171",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 80302-80313",
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
  "excerpt": "[Term]\nid: GO:0051213\nname: dioxygenase activity\nnamespace: molecular_function\ndef: \"Catalysis of the incorporation of both atoms of molecular oxygen (O2) into the substrate.\" [PMID:1444267]\nsubset: goslim_pir\nxref: Reactome:R-HSA-112120 \"Oxidative demethylation of 3-meC damaged DNA by ALKBH2\"\nxref: Reactome:R-HSA-112121 \"Oxidative dealkylation of 1-etA damaged DNA By ALKBH2\"\nxref: Reactome:R-HSA-112124 \"Oxidative demethylation of 3-meC damaged DNA By ALKBH3\"\nxref: Reactome:R-HSA-112125 \"Oxidative dealkylation of 1-EtA damaged DNA by ABH3\"\nis_a: GO:0016491 ! oxidoreductase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051213",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 324234-324245",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 82. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
