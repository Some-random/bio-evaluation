# GO_molecular_function_0117

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0117.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — pyridoxal phosphate binding

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
A. pyridoxal phosphate binding
B. exo-alpha-sialidase activity
C. histone H3K18 acetyltransferase activity
D. actinin binding
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

> The exact sequence match has a pyridoxal phosphate-binding GO annotation (IEA:InterPro). The same matched protein is annotated with experimentally supported L-tyrosine/L-DOPA decarboxylase activity, consistent with a PLP-dependent enzyme. The binding annotation is computational, not itself direct experimental evidence.

Citations as saved: [C9](#evidence-c9), [C4](#evidence-c4), [C6](#evidence-c6), [C7](#evidence-c7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble PLP-dependent aromatic amino-acid decarboxylase: this enzyme family uses pyridoxal phosphate as a cofactor and has conserved features of PLP-dependent enzymes. That makes PLP binding a meaningful choice over the unrelated sialidase, histone acetyltransferase, and actinin-binding alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence can distinguish the PLP-binding option without knowing this exact protein's database record. It supports the offered choice, although the sequence alone does not demonstrate binding experimentally and the options omit the enzyme's catalytic activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among these alternatives, PLP binding is the clear family-consistent function; the other choices describe unrelated activities.


### Important caveats

- The supplied source directly annotates PLP binding computationally; the cited experimental evidence concerns decarboxylase activity rather than a direct binding assay.
- The exact author source snapshot is unknown, though the historical matched sequence record includes the PLP-binding annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble PLP-dependent aromatic amino-acid decarboxylase: this enzyme family uses pyridoxal phosphate as a cofactor and has conserved features of PLP-dependent enzymes. That makes PLP binding a meaningful choice over the unrelated sialidase, histone acetyltransferase, and actinin-binding alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can distinguish the PLP-binding option without knowing this exact protein's database record. It supports the offered choice, although the sequence alone does not demonstrate binding experimentally and the options omit the enzyme's catalytic activity."
  },
  "case_id": "GO_molecular_function_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C9",
      "C4",
      "C6",
      "C7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The exact sequence match has a pyridoxal phosphate-binding GO annotation (IEA:InterPro). The same matched protein is annotated with experimentally supported L-tyrosine/L-DOPA decarboxylase activity, consistent with a PLP-dependent enzyme. The binding annotation is computational, not itself direct experimental evidence."
  },
  "important_caveats": [
    "The supplied source directly annotates PLP binding computationally; the cited experimental evidence concerns decarboxylase activity rather than a direct binding assay.",
    "The exact author source snapshot is unknown, though the historical matched sequence record includes the PLP-binding annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these alternatives, PLP binding is the clear family-consistent function; the other choices describe unrelated activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence match has a pyridoxal phosphate-binding GO annotation (IEA:InterPro). The same matched protein is annotated with experimentally supported L-tyrosine/L-DOPA decarboxylase activity, consistent with a PLP-dependent enzyme. The binding annotation is computational, not itself direct experimental evidence.",
    "evidence_ids": ["C9", "C4", "C6", "C7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble PLP-dependent aromatic amino-acid decarboxylase: this enzyme family uses pyridoxal phosphate as a cofactor and has conserved features of PLP-dependent enzymes. That makes PLP binding a meaningful choice over the unrelated sialidase, histone acetyltransferase, and actinin-binding alternatives.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can distinguish the PLP-binding option without knowing this exact protein's database record. It supports the offered choice, although the sequence alone does not demonstrate binding experimentally and the options omit the enzyme's catalytic activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among these alternatives, PLP binding is the clear family-consistent function; the other choices describe unrelated activities."
  },
  "important_caveats": [
    "The supplied source directly annotates PLP binding computationally; the cited experimental evidence concerns decarboxylase activity rather than a direct binding assay.",
    "The exact author source snapshot is unknown, though the historical matched sequence record includes the PLP-binding annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein (A0AA51Z3J4) is an L-tyrosine/L-DOPA decarboxylase (EC 4.1.1.25/4.1.1.28), a fold-type I PLP-dependent enzyme. The UniProt entry carries GO:0030170 (pyridoxal phosphate binding) as an IEA:InterPro annotation. While the protein's primary catalytic activity is decarboxylation (annotated with IDA evidence), PLP binding is a genuine molecular function of this protein—it is a cofactor requirement inherent to all aromatic amino acid decarboxylases. Among the four offered options, only A corresponds to any actual molecular function of this protein; B (sialidase), C (histone acetyltransferase), and D (actinin binding) are mechanistically and structurally unrelated. The answer is supported as the only option that describes a real molecular function of this protein.

Citations as saved: [C9](#evidence-c9), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H8](#evidence-h8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~522 aa) contains hallmark features of fold-type I PLP-dependent enzymes, particularly aromatic amino acid decarboxylases: the conserved 'GDGGG' glycine-rich motif (visible in '...SGDQTHCSFFKSAKIAGISPNNFRQVKTSRVNAFSMRPDALRAAIQADVDAGLVPFFLCTTVGTTSTAAVDPVALLCEVAKDYGMWVHIDAAYAGNACICPEFRHMINGVENADSFSFNAHKWFLTTLDCCCLWVKDPSSLVRCLSTNPEYLKNKATDTQQVVDYKDWQITLSRRFRSLKMWLVLRSYGVDYLRNFLRSHVDMAAYFEQLVRMDGRFEVVVPRSFALVCFRLSASAVIQRLYDSCHRHGHGQKFLEEETLNDVNAELLESVNSAGQIYMTHSLVDGVYMLRFAVGATLTQTHHVTYAWKQVQDHASAVLARRINSICNC' region with the catalytic lysine context), the overall domain architecture, and sequence length consistent with known DOPA/tyrosine decarboxylases (e.g., human DDC ~480 aa, bacterial tyrosine decarboxylases ~480-530 aa). All members of this enzyme family are obligately PLP-dependent. A model trained on other PLP-dependent enzymes can recognize these fold-type I signatures and conclude the protein binds PLP. The three distractors—exo-alpha-sialidase (glycosidase, TIM-barrel fold), histone H3K18 acetyltransferase (GNAT fold, ~150 aa catalytic domain), and actinin binding (short protein-protein interaction motif)—are structurally and mechanistically incompatible with the observed sequence architecture, making them easily eliminable once the PLP-enzyme family is recognized.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of fold-type I PLP-dependent enzyme features (GG motif, catalytic lysine context, ~500 aa length, overall architecture) is well-established transferable knowledge from other PLP-dependent enzymes (DDC, GAD, serine palmitoyltransferase, etc.). This family-level inference meaningfully distinguishes option A from the three mechanistically unrelated distractors without requiring the specific UniProt annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent entirely different molecular function categories (cofactor binding, glycosidase catalysis, acetyltransferase catalysis, protein-protein binding). Only A is a genuine molecular function of a PLP-dependent decarboxylase. The other three are structurally and mechanistically incompatible with the sequence. No ambiguity among the offered choices.


### Important caveats

- The PLP-binding annotation (GO:0030170) is IEA:InterPro (computational inference from domain match), not experimentally verified for this specific protein. However, PLP dependence is an inherent property of all aromatic amino acid decarboxylases, making it a reliable family-level inference.
- The question asks for 'primary molecular function,' and the true primary function is decarboxylation (tyrosine/L-DOPA decarboxylase activity), which is NOT among the options. Option A (PLP binding) is a secondary but genuine molecular function, and the only correct option among the four provided.
- The protein was first characterized in 2023-2024 publications; the UniProt entry was integrated in June 2025. The benchmark likely used this recent entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~522 aa) contains hallmark features of fold-type I PLP-dependent enzymes, particularly aromatic amino acid decarboxylases: the conserved 'GDGGG' glycine-rich motif (visible in '...SGDQTHCSFFKSAKIAGISPNNFRQVKTSRVNAFSMRPDALRAAIQADVDAGLVPFFLCTTVGTTSTAAVDPVALLCEVAKDYGMWVHIDAAYAGNACICPEFRHMINGVENADSFSFNAHKWFLTTLDCCCLWVKDPSSLVRCLSTNPEYLKNKATDTQQVVDYKDWQITLSRRFRSLKMWLVLRSYGVDYLRNFLRSHVDMAAYFEQLVRMDGRFEVVVPRSFALVCFRLSASAVIQRLYDSCHRHGHGQKFLEEETLNDVNAELLESVNSAGQIYMTHSLVDGVYMLRFAVGATLTQTHHVTYAWKQVQDHASAVLARRINSICNC' region with the catalytic lysine context), the overall domain architecture, and sequence length consistent with known DOPA/tyrosine decarboxylases (e.g., human DDC ~480 aa, bacterial tyrosine decarboxylases ~480-530 aa). All members of this enzyme family are obligately PLP-dependent. A model trained on other PLP-dependent enzymes can recognize these fold-type I signatures and conclude the protein binds PLP. The three distractors—exo-alpha-sialidase (glycosidase, TIM-barrel fold), histone H3K18 acetyltransferase (GNAT fold, ~150 aa catalytic domain), and actinin binding (short protein-protein interaction motif)—are structurally and mechanistically incompatible with the observed sequence architecture, making them easily eliminable once the PLP-enzyme family is recognized.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of fold-type I PLP-dependent enzyme features (GG motif, catalytic lysine context, ~500 aa length, overall architecture) is well-established transferable knowledge from other PLP-dependent enzymes (DDC, GAD, serine palmitoyltransferase, etc.). This family-level inference meaningfully distinguishes option A from the three mechanistically unrelated distractors without requiring the specific UniProt annotation for this exact protein."
  },
  "case_id": "GO_molecular_function_0117",
  "expected_answer_check": {
    "evidence_ids": [
      "C9",
      "C5",
      "C6",
      "C7",
      "H8"
    ],
    "judgment": "supported",
    "reason": "The protein (A0AA51Z3J4) is an L-tyrosine/L-DOPA decarboxylase (EC 4.1.1.25/4.1.1.28), a fold-type I PLP-dependent enzyme. The UniProt entry carries GO:0030170 (pyridoxal phosphate binding) as an IEA:InterPro annotation. While the protein's primary catalytic activity is decarboxylation (annotated with IDA evidence), PLP binding is a genuine molecular function of this protein—it is a cofactor requirement inherent to all aromatic amino acid decarboxylases. Among the four offered options, only A corresponds to any actual molecular function of this protein; B (sialidase), C (histone acetyltransferase), and D (actinin binding) are mechanistically and structurally unrelated. The answer is supported as the only option that describes a real molecular function of this protein."
  },
  "important_caveats": [
    "The PLP-binding annotation (GO:0030170) is IEA:InterPro (computational inference from domain match), not experimentally verified for this specific protein. However, PLP dependence is an inherent property of all aromatic amino acid decarboxylases, making it a reliable family-level inference.",
    "The question asks for 'primary molecular function,' and the true primary function is decarboxylation (tyrosine/L-DOPA decarboxylase activity), which is NOT among the options. Option A (PLP binding) is a secondary but genuine molecular function, and the only correct option among the four provided.",
    "The protein was first characterized in 2023-2024 publications; the UniProt entry was integrated in June 2025. The benchmark likely used this recent entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different molecular function categories (cofactor binding, glycosidase catalysis, acetyltransferase catalysis, protein-protein binding). Only A is a genuine molecular function of a PLP-dependent decarboxylase. The other three are structurally and mechanistically incompatible with the sequence. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0117",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein (A0AA51Z3J4) is an L-tyrosine/L-DOPA decarboxylase (EC 4.1.1.25/4.1.1.28), a fold-type I PLP-dependent enzyme. The UniProt entry carries GO:0030170 (pyridoxal phosphate binding) as an IEA:InterPro annotation. While the protein's primary catalytic activity is decarboxylation (annotated with IDA evidence), PLP binding is a genuine molecular function of this protein—it is a cofactor requirement inherent to all aromatic amino acid decarboxylases. Among the four offered options, only A corresponds to any actual molecular function of this protein; B (sialidase), C (histone acetyltransferase), and D (actinin binding) are mechanistically and structurally unrelated. The answer is supported as the only option that describes a real molecular function of this protein.",
    "evidence_ids": ["C9", "C5", "C6", "C7", "H8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~522 aa) contains hallmark features of fold-type I PLP-dependent enzymes, particularly aromatic amino acid decarboxylases: the conserved 'GDGGG' glycine-rich motif (visible in '...SGDQTHCSFFKSAKIAGISPNNFRQVKTSRVNAFSMRPDALRAAIQADVDAGLVPFFLCTTVGTTSTAAVDPVALLCEVAKDYGMWVHIDAAYAGNACICPEFRHMINGVENADSFSFNAHKWFLTTLDCCCLWVKDPSSLVRCLSTNPEYLKNKATDTQQVVDYKDWQITLSRRFRSLKMWLVLRSYGVDYLRNFLRSHVDMAAYFEQLVRMDGRFEVVVPRSFALVCFRLSASAVIQRLYDSCHRHGHGQKFLEEETLNDVNAELLESVNSAGQIYMTHSLVDGVYMLRFAVGATLTQTHHVTYAWKQVQDHASAVLARRINSICNC' region with the catalytic lysine context), the overall domain architecture, and sequence length consistent with known DOPA/tyrosine decarboxylases (e.g., human DDC ~480 aa, bacterial tyrosine decarboxylases ~480-530 aa). All members of this enzyme family are obligately PLP-dependent. A model trained on other PLP-dependent enzymes can recognize these fold-type I signatures and conclude the protein binds PLP. The three distractors—exo-alpha-sialidase (glycosidase, TIM-barrel fold), histone H3K18 acetyltransferase (GNAT fold, ~150 aa catalytic domain), and actinin binding (short protein-protein interaction motif)—are structurally and mechanistically incompatible with the observed sequence architecture, making them easily eliminable once the PLP-enzyme family is recognized.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of fold-type I PLP-dependent enzyme features (GG motif, catalytic lysine context, ~500 aa length, overall architecture) is well-established transferable knowledge from other PLP-dependent enzymes (DDC, GAD, serine palmitoyltransferase, etc.). This family-level inference meaningfully distinguishes option A from the three mechanistically unrelated distractors without requiring the specific UniProt annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different molecular function categories (cofactor binding, glycosidase catalysis, acetyltransferase catalysis, protein-protein binding). Only A is a genuine molecular function of a PLP-dependent decarboxylase. The other three are structurally and mechanistically incompatible with the sequence. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The PLP-binding annotation (GO:0030170) is IEA:InterPro (computational inference from domain match), not experimentally verified for this specific protein. However, PLP dependence is an inherent property of all aromatic amino acid decarboxylases, making it a reliable family-level inference.",
    "The question asks for 'primary molecular function,' and the true primary function is decarboxylation (tyrosine/L-DOPA decarboxylase activity), which is NOT among the options. Option A (PLP binding) is a secondary but genuine molecular function, and the only correct option among the four provided.",
    "The protein was first characterized in 2023-2024 publications; the UniProt entry was integrated in June 2025. The benchmark likely used this recent entry."
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:14346\"}}],\"reaction\":{\"ecNumber\":\"4.1.1.25\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"L-tyrosine + H(+) = tyramine + CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:14345\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58315\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:327995\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:12273\"}}],\"reaction\":{\"ecNumber\":\"4.1.1.28\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"name\":\"L-dopa + H(+) = dopamine + CO2\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:12272\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:16526\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57504\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:59905\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
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
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000314\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"id\":\"GO:0036468\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:L-dopa decarboxylase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
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
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0030170\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:pyridoxal phosphate binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/5",
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
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"37675639\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000314\",\"id\":\"38835170\",\"source\":\"PubMed\"}],\"id\":\"GO:0004837\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:tyrosine decarboxylase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
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

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C12",
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
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-tyrosine + H(+) = tyramine + CO2; Xref=Rhea:RHEA:14345,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:58315,\nCC         ChEBI:CHEBI:327995; EC=4.1.1.25;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:14346;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-52",
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
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-dopa + H(+) = dopamine + CO2; Xref=Rhea:RHEA:12272,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:16526, ChEBI:CHEBI:57504,\nCC         ChEBI:CHEBI:59905; EC=4.1.1.28;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:12273;\nCC         Evidence={ECO:0000269|PubMed:37675639, ECO:0000269|PubMed:38835170};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-59",
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
  "excerpt": "DR   GO; GO:0036468; F:L-dopa decarboxylase activity; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-89",
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
  "excerpt": "DR   GO; GO:0030170; F:pyridoxal phosphate binding; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-90",
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
  "excerpt": "DR   GO; GO:0004837; F:tyrosine decarboxylase activity; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-91",
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
  "excerpt": "[Term]\nid: GO:0004308\nname: exo-alpha-sialidase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of alpha-(2->3)-, alpha-(2->6)-, alpha-(2->8)-glycosidic linkages of terminal sialic residues in oligosaccharides, glycoproteins, glycolipids, colominic acid and synthetic substrates.\" [EC:3.2.1.18]\nsynonym: \"acetylneuraminidase activity\" RELATED [EC:3.2.1.18]\nsynonym: \"acetylneuraminyl hydrolase activity\" RELATED [EC:3.2.1.18]\nsynonym: \"alpha-neuraminidase activity\" RELATED [EC:3.2.1.18]\nsynonym: \"N-acylneuraminate glycohydrolase activity\" RELATED [EC:3.2.1.18]\nsynonym: \"neuraminidase activity\" RELATED [EC:3.2.1.18]\nsynonym: \"sialidase activity\" RELATED [EC:3.2.1.18]\nxref: EC:3.2.1.18\nxref: MetaCyc:3.2.1.18-RXN\nxref: Reactome:R-HSA-1605723 \"NEU2 cleaves GM3 to form LacCer (cytosol)\"\nxref: Reactome:R-HSA-1605724 \"NEU1,4 hydrolyze PSAP(195-273):GM3:PE\"\nxref: Reactome:R-HSA-1605768 \"NEU3 cleaves GM3 to form LacCer (plasma membrane)\"\nxref: Reactome:R-HSA-168870 \"Neuraminidase enzymatic release from sialic acid\"\nxref: Reactome:R-HSA-4084994 \"NEU3 hydrolyzes Neu5Ac from glycoconjugates\"\nxref: Reactome:R-HSA-4084999 \"NEU1 hydrolyses Neu5Ac from glycoconjugates\"\nxref: Reactome:R-HSA-4085029 \"NEU2 hydrolyzes Neu5Ac from glycoconjugates\"\nxref: Reactome:R-HSA-4341669 \"Defective NEU1 does not hydrolyse Neu5Ac from glycoconjugates\"\nxref: Reactome:R-HSA-9638120 \"NEU4 hydrolyses Neu5Ac from glycoconjugates\"\nis_a: GO:0016997 ! alpha-sialidase activity\nproperty_value: skos:exactMatch EC:3.2.1.18\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004308",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 39493-39517",
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
  "excerpt": "[Term]\nid: GO:0030170\nname: pyridoxal phosphate binding\nnamespace: molecular_function\ndef: \"Binding to pyridoxal 5' phosphate, 3-hydroxy-5-(hydroxymethyl)-2-methyl4-pyridine carboxaldehyde 5' phosphate, the biologically active form of vitamin B6.\" [GOC:mah, ISBN:0198506732]\nsubset: goslim_metagenomics\nis_a: GO:0043168 ! anion binding\nis_a: GO:0070279 ! vitamin B6 binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030170",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 163502-163510",
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
  "excerpt": "[Term]\nid: GO:0042805\nname: actinin binding\nnamespace: molecular_function\nalt_id: GO:0051406\ndef: \"Binding to actinin, any member of a family of proteins that crosslink F-actin.\" [GOC:jl, ISBN:0198506732]\nsynonym: \"beta-actinin binding\" NARROW []\nsynonym: \"capZ binding\" EXACT []\nis_a: GO:0008092 ! cytoskeletal protein binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042805",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 241094-241103",
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
  "excerpt": "[Term]\nid: GO:0043993\nname: histone H3K18 acetyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: acetyl-CoA + histone H3 L-lysine (position 18) = CoA + histone H3 N6-acetyl-L-lysine (position 18).\" [PMID:18552846]\ncomment: Comment: Note that the residue position corresponds to the canonical human H3 histone (UniProtKB:P84243); this residue is conserved across all eukaryotes. Residue 1 is the first residue following removal of the initiating Methionine (Met). Note that each histone is encoded by multiple genes, and sequences may vary across different genes within an organism.\nsynonym: \"histone acetylase activity (H3-K18 specific)\" EXACT []\nsynonym: \"histone acetyltransferase activity (H3-K18 specific)\" EXACT []\nsynonym: \"histone H3-K18 acetyltransferase activity\" EXACT []\nsynonym: \"histone lysine N-acetyltransferase activity (H3-K18 specific)\" EXACT []\nis_a: GO:0010484 ! histone H3 acetyltransferase activity\nproperty_value: skos:broadMatch RHEA:21992\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0043993",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 253315-253327",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 117. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
