# GO_biological_process_0184

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0184.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **A** — carboxylic acid metabolic process

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGSLDIKQESSPLMTNPLDSEEFRRQGYMVIDFLAEYYKNIQKFPVRSQVEPGYLRKRLPESAPYEPESIETILKDVHDDIVPGLTHWQSPNYYAYFPSSGSTAGLLGETLAAGFNVVGFNWISSPASTELESIVMDWLAEMLNLPKSFTFSGDGGGVMMGTTCEAILTTITAARDRILDRIGREHINKLVVYGSDQTHCSFFKSAKIAGISPNNFRQVKTSRVNAFSMRPDALRAAIQADVDAGLVPFFLCTTVGTTSTAAVDPVALLCEVAKDYGMWVHIDAAYAGNACICPEFRHMINGVENADSFSFNAHKWFLTTLDCCCLWVKDPSSLVRCLSTNPEYLKNKATDTQQVVDYKDWQITLSRRFRSLKMWLVLRSYGVDYLRNFLRSHVDMAAYFEQLVRMDGRFEVVVPRSFALVCFRLSASAVIQRLYDSCHRHGHGQKFLEEETLNDVNAELLESVNSAGQIYMTHSLVDGVYMLRFAVGATLTQTHHVTYAWKQVQDHASAVLARRINSICNC

[Multiple Choices]
A. carboxylic acid metabolic process
B. response to cytokine
C. bone mineralization
D. coenzyme A biosynthetic process
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The sequence-matched entry reports experimentally supported decarboxylation of L-tyrosine and L-DOPA. These amino-acid substrates contain carboxyl groups, so their decarboxylation is a defensible instance of carboxylic acid metabolism. The annotation also places the protein in amino-acid metabolism. Option A is broad; the more specific reported role is natural-product/alkaloid biosynthesis, which is not offered.

Citations as saved: [C5](#evidence-c5), [C9](#evidence-c9).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble PLP-dependent aromatic amino-acid decarboxylase. Transferable knowledge of this enzyme family connects it to decarboxylation of amino-acid carboxyl groups, supporting the broad metabolic option A. That distinguishes it from cytokine response, bone mineralization, and coenzyme A biosynthesis without requiring knowledge of this exact protein's record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level functional inference from the sequence provides a meaningful basis for choosing A among these alternatives. It does not establish the protein's most specific biological role, but that finer pathway is not among the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> A is the only offered choice supported by the decarboxylase activity; the other choices describe unrelated biological processes.


### Important caveats

- The protein's more specific reported role is alkaloid and phenylethylamine biosynthesis, which is absent from the options.
- The match to carboxylic acid metabolism is broad and follows from substrate decarboxylation; it is not the most specific description of the protein's biological role.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble PLP-dependent aromatic amino-acid decarboxylase. Transferable knowledge of this enzyme family connects it to decarboxylation of amino-acid carboxyl groups, supporting the broad metabolic option A. That distinguishes it from cytokine response, bone mineralization, and coenzyme A biosynthesis without requiring knowledge of this exact protein's record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level functional inference from the sequence provides a meaningful basis for choosing A among these alternatives. It does not establish the protein's most specific biological role, but that finer pathway is not among the choices."
  },
  "case_id": "GO_biological_process_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched entry reports experimentally supported decarboxylation of L-tyrosine and L-DOPA. These amino-acid substrates contain carboxyl groups, so their decarboxylation is a defensible instance of carboxylic acid metabolism. The annotation also places the protein in amino-acid metabolism. Option A is broad; the more specific reported role is natural-product/alkaloid biosynthesis, which is not offered."
  },
  "important_caveats": [
    "The protein's more specific reported role is alkaloid and phenylethylamine biosynthesis, which is absent from the options.",
    "The match to carboxylic acid metabolism is broad and follows from substrate decarboxylation; it is not the most specific description of the protein's biological role."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the only offered choice supported by the decarboxylase activity; the other choices describe unrelated biological processes."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched entry reports experimentally supported decarboxylation of L-tyrosine and L-DOPA. These amino-acid substrates contain carboxyl groups, so their decarboxylation is a defensible instance of carboxylic acid metabolism. The annotation also places the protein in amino-acid metabolism. Option A is broad; the more specific reported role is natural-product/alkaloid biosynthesis, which is not offered.",
    "evidence_ids": ["C5", "C9"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble PLP-dependent aromatic amino-acid decarboxylase. Transferable knowledge of this enzyme family connects it to decarboxylation of amino-acid carboxyl groups, supporting the broad metabolic option A. That distinguishes it from cytokine response, bone mineralization, and coenzyme A biosynthesis without requiring knowledge of this exact protein's record.",
    "missing_item_specific_fact": "",
    "reason": "A family-level functional inference from the sequence provides a meaningful basis for choosing A among these alternatives. It does not establish the protein's most specific biological role, but that finer pathway is not among the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "A is the only offered choice supported by the decarboxylase activity; the other choices describe unrelated biological processes."
  },
  "important_caveats": [
    "The protein's more specific reported role is alkaloid and phenylethylamine biosynthesis, which is absent from the options.",
    "The match to carboxylic acid metabolism is broad and follows from substrate decarboxylation; it is not the most specific description of the protein's biological role."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is an aromatic amino acid decarboxylase (EC 4.1.1.25/4.1.1.28) that catalyzes decarboxylation of L-tyrosine and L-DOPA. Amino acids contain carboxyl (-COOH) groups and are therefore carboxylic acids. Decarboxylation of amino acids constitutes a reaction 'involving carboxylic acids,' which matches the definition of GO:0019752 (carboxylic acid metabolic process). The UniProt entry annotates GO:0006520 (amino acid metabolic process, IEA:InterPro), which is a child of GO:0019752 in the GO hierarchy. Although GO:0019752 carries the 'gocheck_do_not_annotate' flag (indicating it is too broad for direct annotation), the protein does participate in carboxylic acid metabolism as an ancestor-level process. Among the four offered choices, A is the only scientifically defensible one; B (cytokine response), C (bone mineralization), and D (CoA biosynthesis) are clearly unrelated to a PLP-dependent amino acid decarboxylase.

Citations as saved: [C5](#evidence-c5), [C9](#evidence-c9), [H4](#evidence-h4), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains hallmarks of the PLP-dependent aromatic amino acid decarboxylase family (e.g., conserved motifs surrounding the PLP-binding lysine, the ~520-residue length typical of plant aromatic amino acid decarboxylases like AADC/DDC). Recognizing this family, a knowledgeable model knows these enzymes catalyze removal of the α-carboxyl group from amino acids. Amino acids are, by definition, carboxylic acids (they bear a -COOH group). Therefore, amino acid decarboxylation is a subset of carboxylic acid metabolic process. This directly supports option A. The other three options are excluded by family-level reasoning: (B) response to cytokine requires receptor/signaling architecture (e.g., JAK-STAT, TNF receptor), not a metabolic enzyme; (C) bone mineralization is a vertebrate-specific hydroxyapatite deposition process with no enzymatic decarboxylase component; (D) coenzyme A biosynthetic process involves a specific linear pathway (pantothenate kinase → phosphopantothenoylcysteine synthetase → CoA synthetase) with no PLP-dependent decarboxylase step. Thus, family recognition plus the definitional fact that amino acids are carboxylic acids meaningfully distinguishes A from B, C, and D without needing the target's specific database annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model recognizing the PLP-dependent aromatic amino acid decarboxylase family from sequence features can apply the general biochemical fact that amino acids are carboxylic acids and that decarboxylation is a carboxylic-acid-involving reaction. This transfers from well-known enzymology of related proteins (e.g., mammalian AADC, bacterial histidine decarboxylase) and the GO ontology structure where amino acid metabolic process is a child of carboxylic acid metabolic process. The three distractors are excluded by straightforward family-level and pathway-level reasoning.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although GO:0019752 is a very broad ancestor term (flagged gocheck_do_not_annotate) and the protein's more specific annotations (alkaloid biosynthetic process, tyramine biosynthetic process, phenylethylamine biosynthetic process) are not offered, among the four provided choices only A is even remotely applicable. B, C, and D are clearly incompatible with a PLP-dependent amino acid decarboxylase. No ambiguity exists among the offered alternatives.


### Important caveats

- GO:0019752 carries the 'gocheck_do_not_annotate' flag, indicating it is an overly broad grouping term not intended for direct protein annotation. The protein's experimentally determined annotations are more specific (alkaloid biosynthesis, tyramine biosynthesis, phenylethylamine biosynthesis), but those are not offered as choices.
- The protein is from Lophophora williamsii (peyote cactus), a plant. The organism identity is not given in the original input but is inferable from sequence features; regardless, options B (cytokine response) and C (bone mineralization) are vertebrate/animal-specific processes and are excluded for a plant enzyme.
- The sequence matches UniProt A0AA51Z3J4 (LwTyDC2) exactly. The annotation is based on experimental evidence (PubMed:37675639, PubMed:38835170).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains hallmarks of the PLP-dependent aromatic amino acid decarboxylase family (e.g., conserved motifs surrounding the PLP-binding lysine, the ~520-residue length typical of plant aromatic amino acid decarboxylases like AADC/DDC). Recognizing this family, a knowledgeable model knows these enzymes catalyze removal of the α-carboxyl group from amino acids. Amino acids are, by definition, carboxylic acids (they bear a -COOH group). Therefore, amino acid decarboxylation is a subset of carboxylic acid metabolic process. This directly supports option A. The other three options are excluded by family-level reasoning: (B) response to cytokine requires receptor/signaling architecture (e.g., JAK-STAT, TNF receptor), not a metabolic enzyme; (C) bone mineralization is a vertebrate-specific hydroxyapatite deposition process with no enzymatic decarboxylase component; (D) coenzyme A biosynthetic process involves a specific linear pathway (pantothenate kinase → phosphopantothenoylcysteine synthetase → CoA synthetase) with no PLP-dependent decarboxylase step. Thus, family recognition plus the definitional fact that amino acids are carboxylic acids meaningfully distinguishes A from B, C, and D without needing the target's specific database annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the PLP-dependent aromatic amino acid decarboxylase family from sequence features can apply the general biochemical fact that amino acids are carboxylic acids and that decarboxylation is a carboxylic-acid-involving reaction. This transfers from well-known enzymology of related proteins (e.g., mammalian AADC, bacterial histidine decarboxylase) and the GO ontology structure where amino acid metabolic process is a child of carboxylic acid metabolic process. The three distractors are excluded by straightforward family-level and pathway-level reasoning."
  },
  "case_id": "GO_biological_process_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C9",
      "H4",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The protein is an aromatic amino acid decarboxylase (EC 4.1.1.25/4.1.1.28) that catalyzes decarboxylation of L-tyrosine and L-DOPA. Amino acids contain carboxyl (-COOH) groups and are therefore carboxylic acids. Decarboxylation of amino acids constitutes a reaction 'involving carboxylic acids,' which matches the definition of GO:0019752 (carboxylic acid metabolic process). The UniProt entry annotates GO:0006520 (amino acid metabolic process, IEA:InterPro), which is a child of GO:0019752 in the GO hierarchy. Although GO:0019752 carries the 'gocheck_do_not_annotate' flag (indicating it is too broad for direct annotation), the protein does participate in carboxylic acid metabolism as an ancestor-level process. Among the four offered choices, A is the only scientifically defensible one; B (cytokine response), C (bone mineralization), and D (CoA biosynthesis) are clearly unrelated to a PLP-dependent amino acid decarboxylase."
  },
  "important_caveats": [
    "GO:0019752 carries the 'gocheck_do_not_annotate' flag, indicating it is an overly broad grouping term not intended for direct protein annotation. The protein's experimentally determined annotations are more specific (alkaloid biosynthesis, tyramine biosynthesis, phenylethylamine biosynthesis), but those are not offered as choices.",
    "The protein is from Lophophora williamsii (peyote cactus), a plant. The organism identity is not given in the original input but is inferable from sequence features; regardless, options B (cytokine response) and C (bone mineralization) are vertebrate/animal-specific processes and are excluded for a plant enzyme.",
    "The sequence matches UniProt A0AA51Z3J4 (LwTyDC2) exactly. The annotation is based on experimental evidence (PubMed:37675639, PubMed:38835170)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although GO:0019752 is a very broad ancestor term (flagged gocheck_do_not_annotate) and the protein's more specific annotations (alkaloid biosynthetic process, tyramine biosynthetic process, phenylethylamine biosynthetic process) are not offered, among the four provided choices only A is even remotely applicable. B, C, and D are clearly incompatible with a PLP-dependent amino acid decarboxylase. No ambiguity exists among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is an aromatic amino acid decarboxylase (EC 4.1.1.25/4.1.1.28) that catalyzes decarboxylation of L-tyrosine and L-DOPA. Amino acids contain carboxyl (-COOH) groups and are therefore carboxylic acids. Decarboxylation of amino acids constitutes a reaction 'involving carboxylic acids,' which matches the definition of GO:0019752 (carboxylic acid metabolic process). The UniProt entry annotates GO:0006520 (amino acid metabolic process, IEA:InterPro), which is a child of GO:0019752 in the GO hierarchy. Although GO:0019752 carries the 'gocheck_do_not_annotate' flag (indicating it is too broad for direct annotation), the protein does participate in carboxylic acid metabolism as an ancestor-level process. Among the four offered choices, A is the only scientifically defensible one; B (cytokine response), C (bone mineralization), and D (CoA biosynthesis) are clearly unrelated to a PLP-dependent amino acid decarboxylase.",
    "evidence_ids": ["C5", "C9", "H4", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains hallmarks of the PLP-dependent aromatic amino acid decarboxylase family (e.g., conserved motifs surrounding the PLP-binding lysine, the ~520-residue length typical of plant aromatic amino acid decarboxylases like AADC/DDC). Recognizing this family, a knowledgeable model knows these enzymes catalyze removal of the α-carboxyl group from amino acids. Amino acids are, by definition, carboxylic acids (they bear a -COOH group). Therefore, amino acid decarboxylation is a subset of carboxylic acid metabolic process. This directly supports option A. The other three options are excluded by family-level reasoning: (B) response to cytokine requires receptor/signaling architecture (e.g., JAK-STAT, TNF receptor), not a metabolic enzyme; (C) bone mineralization is a vertebrate-specific hydroxyapatite deposition process with no enzymatic decarboxylase component; (D) coenzyme A biosynthetic process involves a specific linear pathway (pantothenate kinase → phosphopantothenoylcysteine synthetase → CoA synthetase) with no PLP-dependent decarboxylase step. Thus, family recognition plus the definitional fact that amino acids are carboxylic acids meaningfully distinguishes A from B, C, and D without needing the target's specific database annotation.",
    "missing_item_specific_fact": "",
    "reason": "A model recognizing the PLP-dependent aromatic amino acid decarboxylase family from sequence features can apply the general biochemical fact that amino acids are carboxylic acids and that decarboxylation is a carboxylic-acid-involving reaction. This transfers from well-known enzymology of related proteins (e.g., mammalian AADC, bacterial histidine decarboxylase) and the GO ontology structure where amino acid metabolic process is a child of carboxylic acid metabolic process. The three distractors are excluded by straightforward family-level and pathway-level reasoning."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although GO:0019752 is a very broad ancestor term (flagged gocheck_do_not_annotate) and the protein's more specific annotations (alkaloid biosynthetic process, tyramine biosynthetic process, phenylethylamine biosynthetic process) are not offered, among the four provided choices only A is even remotely applicable. B, C, and D are clearly incompatible with a PLP-dependent amino acid decarboxylase. No ambiguity exists among the offered alternatives."
  },
  "important_caveats": [
    "GO:0019752 carries the 'gocheck_do_not_annotate' flag, indicating it is an overly broad grouping term not intended for direct protein annotation. The protein's experimentally determined annotations are more specific (alkaloid biosynthesis, tyramine biosynthesis, phenylethylamine biosynthesis), but those are not offered as choices.",
    "The protein is from Lophophora williamsii (peyote cactus), a plant. The organism identity is not given in the original input but is inferable from sequence features; regardless, options B (cytokine response) and C (bone mineralization) are vertebrate/animal-specific processes and are excluded for a plant enzyme.",
    "The sequence matches UniProt A0AA51Z3J4 (LwTyDC2) exactly. The annotation is based on experimental evidence (PubMed:37675639, PubMed:38835170)."
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
  "benchmark_sequence_length": 522,
  "benchmark_sequence_sha256": "39ec61a6d8642a0a7790dd9cb740bee54c5dd090de950c5c89bb7477e43c264e",
  "current_entry_audit": {
    "entryVersion": 11,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 2
  },
  "current_record_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 522,
  "current_source_sequence_sha256": "39ec61a6d8642a0a7790dd9cb740bee54c5dd090de950c5c89bb7477e43c264e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 9,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AA51Z3J4",
  "selected_historical_entry_version": 9,
  "selected_historical_record_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "selected_historical_source_sequence_length": 522,
  "selected_historical_source_sequence_sha256": "39ec61a6d8642a0a7790dd9cb740bee54c5dd090de950c5c89bb7477e43c264e",
  "selected_historical_version": {
    "accession": "A0AA51Z3J4",
    "database": "Swiss-Prot",
    "entryVersion": 9,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "TYDC2_LOPWI",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AA51Z3J4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":11,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Peyote\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Cactineae\",\"Cactaceae\",\"Cactoideae\",\"Cacteae\",\"Lophophora\"],\"scientificName\":\"Lophophora williamsii\",\"synonyms\":[\"Echinocactus williamsii\"],\"taxonId\":130138}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"Aromatic amino acid decarboxylase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"37675639\",\"source\":\"PubMed\"}],\"value\":\"LwTyDC1\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"4.1.1.25\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"4.1.1.28\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"L-tyrosine/L-DOPA decarboxylase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"LwTyDC2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"Aromatic amino acid decarboxylase participating in the biosynthesis of natural products derived from phenylethylamine, including mescaline, a natural hallucinogen potentially used in psychotherapeutic treatments (PubMed:37675639, PubMed:38835170). Catalyzes the decarboxylation of L-tyrosine and L-DOPA (PubMed:37675639, PubMed:38835170)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"Aromatic compound metabolism\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000314\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"id\":\"GO:0009821\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:alkaloid biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/7",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0006520\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:amino acid metabolic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/8",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000314\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"id\":\"GO:0042444\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:phenylethylamine biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000314\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"id\":\"GO:1901695\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:tyramine biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"citation\":{\"authors\":[\"Watkins J.L.\",\"Li Q.\",\"Yeaman S.\",\"Facchini P.J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"37675639\"},{\"database\":\"DOI\",\"id\":\"10.1111/tpj.16447\"}],\"citationType\":\"journal article\",\"firstPage\":\"635\",\"id\":\"37675639\",\"journal\":\"Plant J.\",\"lastPage\":\"649\",\"publicationDate\":\"2023\",\"title\":\"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora williamsii).\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WMX25288.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Jourdaniana\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"citation\":{\"authors\":[\"Berman P.\",\"de Haro L.A.\",\"Cavaco A.-R.\",\"Panda S.\",\"Dong Y.\",\"Kuzmich N.\",\"Lichtenstein G.\",\"Peleg Y.\",\"Harat H.\",\"Jozwiak A.\",\"Cai J.\",\"Heinig U.\",\"Meir S.\",\"Rogachev I.\",\"Aharoni A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38835170\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.molp.2024.05.012\"}],\"citationType\":\"journal article\",\"firstPage\":\"1129\",\"id\":\"38835170\",\"journal\":\"Mol. Plant\",\"lastPage\":\"1150\",\"publicationDate\":\"2024\",\"title\":\"The biosynthetic pathway of the hallucinogen mescaline and its heterologous reconstruction.\",\"volume\":\"17\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"cv. Rehovot 7\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOTECHNOLOGY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"TISSUE SPECIFICITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:26:23.611761+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "df87091c482642dd500c923c44da23a6238f45d97936af1dca1ddc0f7e28eba5",
  "url": "https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H1",
  "excerpt": "ID   TYDC2_LOPWI             Reviewed;         522 AA.\nAC   A0AA51Z3J4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 2.\nDT   28-JAN-2026, entry version 9.\nDE   RecName: Full=L-tyrosine/L-DOPA decarboxylase 2 {ECO:0000303|PubMed:38835170};\nDE            Short=LwTyDC2 {ECO:0000303|PubMed:38835170};\nDE            EC=4.1.1.25 {ECO:0000269|PubMed:38835170};\nDE            EC=4.1.1.28 {ECO:0000269|PubMed:38835170};\nDE   AltName: Full=Aromatic amino acid decarboxylase 1 {ECO:0000303|PubMed:37675639};\nDE            Short=LwTyDC1 {ECO:0000303|PubMed:37675639};\nGN   Name=TyDC2 {ECO:0000303|PubMed:38835170};\nGN   Synonyms=TyDC1 {ECO:0000303|PubMed:37675639};\nOS   Lophophora williamsii (Peyote) (Echinocactus williamsii).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Cactineae; Cactaceae; Cactoideae; Cacteae; Lophophora.\nOX   NCBI_TaxID=130138;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-18",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WMX25288.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND\nRP   TISSUE SPECIFICITY.\nRC   STRAIN=cv. Jourdaniana;\nRX   PubMed=37675639; DOI=10.1111/tpj.16447;\nRA   Watkins J.L., Li Q., Yeaman S., Facchini P.J.;\nRT   \"Elucidation of the mescaline biosynthetic pathway in peyote (Lophophora\nRT   williamsii).\";\nRL   Plant J. 116:635-649(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY,\nRP   BIOTECHNOLOGY, BIOPHYSICOCHEMICAL PROPERTIES, AND TISSUE SPECIFICITY.\nRC   STRAIN=cv. Rehovot 7;\nRX   PubMed=38835170; DOI=10.1016/j.molp.2024.05.012;\nRA   Berman P., de Haro L.A., Cavaco A.-R., Panda S., Dong Y., Kuzmich N.,\nRA   Lichtenstein G., Peleg Y., Harat H., Jozwiak A., Cai J., Heinig U.,\nRA   Meir S., Rogachev I., Aharoni A.;\nRT   \"The biosynthetic pathway of the hallucinogen mescaline and its\nRT   heterologous reconstruction.\";\nRL   Mol. Plant 17:1129-1150(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Aromatic amino acid decarboxylase participating in the\nCC       biosynthesis of natural products derived from phenylethylamine,\nCC       including mescaline, a natural hallucinogen potentially used in\nCC       psychotherapeutic treatments (PubMed:37675639, PubMed:38835170).\nCC       Catalyzes the decarboxylation of L-tyrosine and L-DOPA\nCC       (PubMed:37675639, PubMed:38835170). {ECO:0000269|PubMed:37675639,\nCC       ECO:0000269|PubMed:38835170}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 39-45",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H5",
  "excerpt": "CC   -!- PATHWAY: Aromatic compound metabolism. {ECO:0000269|PubMed:37675639,\nCC       ECO:0000269|PubMed:38835170}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-70",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H6",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis. {ECO:0000269|PubMed:37675639,\nCC       ECO:0000269|PubMed:38835170}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-72",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0009821; P:alkaloid biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 92-92",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H8",
  "excerpt": "DR   GO; GO:1903184; P:L-dopa metabolic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 93-93",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0042444; P:phenylethylamine biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 94-94",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H10",
  "excerpt": "DR   GO; GO:1901695; P:tyramine biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 95-95",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0015937\nname: coenzyme A biosynthetic process\nnamespace: biological_process\nalt_id: GO:0006764\ndef: \"The chemical reactions and pathways resulting in the formation of coenzyme A, 3'-phosphoadenosine-(5')diphospho(4')pantatheine, an acyl carrier in many acylation and acyl-transfer reactions in which the intermediate is a thiol ester.\" [ISBN:0198547684]\nsynonym: \"CoA biosynthesis\" EXACT []\nsynonym: \"coenzyme A anabolism\" EXACT []\nsynonym: \"coenzyme A biosynthesis\" EXACT []\nsynonym: \"coenzyme A formation\" EXACT []\nsynonym: \"coenzyme A synthesis\" EXACT []\nxref: MetaCyc:COA-PWY\nxref: MetaCyc:COA-PWY-1\nxref: MetaCyc:PANTOSYN-PWY\nxref: MetaCyc:PWY-4221\nxref: MetaCyc:PWY-7851\nxref: MetaCyc:PWY-8342\nxref: MetaCyc:PWY8J2-29\nxref: Reactome:R-HSA-196783 \"Coenzyme A biosynthesis\"\nis_a: GO:0015936 ! coenzyme A metabolic process\nis_a: GO:0044272 ! sulfur compound biosynthetic process\nis_a: GO:0072522 ! purine-containing compound biosynthetic process\nis_a: GO:1901293 ! nucleoside phosphate biosynthetic process\nproperty_value: skos:narrowMatch MetaCyc:COA-PWY\nproperty_value: skos:narrowMatch MetaCyc:COA-PWY-1\nproperty_value: skos:narrowMatch MetaCyc:PANTOSYN-PWY\nproperty_value: skos:narrowMatch MetaCyc:PWY-4221\nproperty_value: skos:narrowMatch MetaCyc:PWY-7851\nproperty_value: skos:narrowMatch MetaCyc:PWY-8342\nproperty_value: skos:narrowMatch MetaCyc:PWY8J2-29\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0015937",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 121836-121866",
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
  "excerpt": "[Term]\nid: GO:0019752\nname: carboxylic acid metabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways involving carboxylic acids, any organic acid containing one or more carboxyl (COOH) groups or anions (COO-).\" [ISBN:0198506732]\nsubset: gocheck_do_not_annotate\nsynonym: \"carboxylic acid metabolism\" EXACT []\nxref: Reactome:R-HSA-389661 \"Glyoxylate metabolism and glycine degradation\"\nis_a: GO:0043436 ! oxoacid metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019752",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 152755-152764",
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
  "excerpt": "[Term]\nid: GO:0030282\nname: bone mineralization\nnamespace: biological_process\ndef: \"The deposition of hydroxyapatite, a form of calcium phosphate with the formula Ca10(PO4)6(OH)2, in bone tissue.\" [GOC:mah, PMID:22936354]\nsynonym: \"bone calcification\" NARROW []\nis_a: GO:0031214 ! biomineral tissue development\nis_a: GO:0160108 ! animal gross anatomical part developmental process\nrelationship: part_of GO:0001503 ! ossification\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030282",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 164753-164762",
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
  "excerpt": "[Term]\nid: GO:0034097\nname: response to cytokine\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell or an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a cytokine stimulus.\" [GOC:sl]\nsynonym: \"response to cytokine stimulus\" EXACT [GOC:dos]\nxref: Reactome:R-HSA-9645135 \"STAT5 Activation\"\nis_a: GO:1901652 ! response to peptide\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0034097",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 205545-205553",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 184. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
