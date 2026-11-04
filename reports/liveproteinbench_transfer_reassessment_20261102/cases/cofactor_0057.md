# cofactor_0057

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0057.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — pyridoxal 5&#x27;-phosphate

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
A. tungstopterin
B. pyridoxal 5'-phosphate
C. Fe(2+)
D. pantetheine 4'-phosphate
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The matching sequence's UniProt record identifies it as an L-tyrosine/L-DOPA decarboxylase and annotates pyridoxal 5'-phosphate as its cofactor. The cofactor annotation is transferred by similarity, rather than direct experimental evidence in the excerpt, but it supports the key.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the aromatic amino-acid decarboxylase family. Transferable knowledge of this family is that its decarboxylation chemistry is PLP-dependent, which distinguishes pyridoxal 5'-phosphate from the offered tungsten cofactor, iron ion, and pantetheine phosphate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and the known cofactor requirement of aromatic amino-acid decarboxylases provide a meaningful basis for choosing B without recalling this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed alternatives, PLP is the family-appropriate cofactor.


### Important caveats

- The supplied record's cofactor evidence is annotation by similarity, not direct experimental confirmation in the excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the aromatic amino-acid decarboxylase family. Transferable knowledge of this family is that its decarboxylation chemistry is PLP-dependent, which distinguishes pyridoxal 5'-phosphate from the offered tungsten cofactor, iron ion, and pantetheine phosphate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the known cofactor requirement of aromatic amino-acid decarboxylases provide a meaningful basis for choosing B without recalling this exact protein's database entry."
  },
  "case_id": "cofactor_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The matching sequence's UniProt record identifies it as an L-tyrosine/L-DOPA decarboxylase and annotates pyridoxal 5'-phosphate as its cofactor. The cofactor annotation is transferred by similarity, rather than direct experimental evidence in the excerpt, but it supports the key."
  },
  "important_caveats": [
    "The supplied record's cofactor evidence is annotation by similarity, not direct experimental confirmation in the excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed alternatives, PLP is the family-appropriate cofactor."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matching sequence's UniProt record identifies it as an L-tyrosine/L-DOPA decarboxylase and annotates pyridoxal 5'-phosphate as its cofactor. The cofactor annotation is transferred by similarity, rather than direct experimental evidence in the excerpt, but it supports the key.",
    "evidence_ids": ["C4", "C5", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the aromatic amino-acid decarboxylase family. Transferable knowledge of this family is that its decarboxylation chemistry is PLP-dependent, which distinguishes pyridoxal 5'-phosphate from the offered tungsten cofactor, iron ion, and pantetheine phosphate.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the known cofactor requirement of aromatic amino-acid decarboxylases provide a meaningful basis for choosing B without recalling this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed alternatives, PLP is the family-appropriate cofactor."
  },
  "important_caveats": [
    "The supplied record's cofactor evidence is annotation by similarity, not direct experimental confirmation in the excerpts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0AA51Z3J4) explicitly annotates pyridoxal 5'-phosphate as the cofactor (evidence ECO:0000250, inferred by similarity from P20711, the human DOPA decarboxylase). The protein is annotated as L-tyrosine/L-DOPA decarboxylase 2 (EC 4.1.1.25 and 4.1.1.28), both of which are universally PLP-dependent aromatic amino acid decarboxylases. The EC assignments themselves carry experimental evidence (ECO:0000269 from PubMed 38835170). PLP is the sole known cofactor for all members of this enzyme family.

Citations as saved: [C5](#evidence-c5), [H5](#evidence-h5), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved 'GGGVMM' motif (around residues 155-160), which is a hallmark of the aromatic amino acid decarboxylase (AADC) family within the Group IV PLP-dependent enzyme superfamily. This motif, together with the overall ~522-residue length, the presence of a conserved lysine in the context 'KDPSSLVRCLSTNPEYLKNKATDTQQVVDYKDWQ' (the catalytic lysine that forms the internal aldimine with PLP), and the general domain architecture, are recognizable signatures of AADCs (e.g., human DOPA decarboxylase P20711, histidine decarboxylase, tryptophan decarboxylase). All known aromatic amino acid decarboxylases are obligately PLP-dependent; no member of this family uses tungstopterin, free Fe(2+), or pantetheine 4'-phosphate. A model trained on homologous proteins can recognize the GGGVMM motif and the characteristic fold architecture, infer membership in the AADC family, and conclude PLP. The four distractors belong to entirely unrelated enzyme classes (tungstopterin → anaerobic formate dehydrogenases; Fe(2+) → dioxygenases/oxidoreductases; pantetheine 4'-phosphate → acyltransferases/CoA-dependent enzymes), none of which share this sequence architecture.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GGGVMM motif and overall sequence architecture are transferable family-level features shared across aromatic amino acid decarboxylases. Recognizing these features allows a knowledgeable model to place the protein in a family that is exclusively PLP-dependent, cleanly distinguishing option B from the three structurally and mechanistically unrelated alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four cofactor options (tungstopterin, PLP, Fe2+, pantetheine 4'-phosphate) correspond to entirely distinct enzyme superfamilies with no overlap in sequence features. The GGGVMM motif and AADC-family architecture unambiguously point to PLP and exclude the other three.


### Important caveats

- The cofactor annotation in UniProt carries evidence code ECO:0000250 (inferred by similarity from P20711), not direct experimental determination for this exact protein. However, the EC assignments (4.1.1.25, 4.1.1.28) are experimentally supported (ECO:0000269), and PLP dependence is a defining, universal property of the AADC family.
- The protein is from Lophophora williamsii (peyote cactus), involved in mescaline biosynthesis. This organism context was not provided to the evaluated model but is not needed for the family-level cofactor inference.
- The sequence is 522 aa, consistent with the typical AADC length range (~450–530 aa), further supporting family assignment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved 'GGGVMM' motif (around residues 155-160), which is a hallmark of the aromatic amino acid decarboxylase (AADC) family within the Group IV PLP-dependent enzyme superfamily. This motif, together with the overall ~522-residue length, the presence of a conserved lysine in the context 'KDPSSLVRCLSTNPEYLKNKATDTQQVVDYKDWQ' (the catalytic lysine that forms the internal aldimine with PLP), and the general domain architecture, are recognizable signatures of AADCs (e.g., human DOPA decarboxylase P20711, histidine decarboxylase, tryptophan decarboxylase). All known aromatic amino acid decarboxylases are obligately PLP-dependent; no member of this family uses tungstopterin, free Fe(2+), or pantetheine 4'-phosphate. A model trained on homologous proteins can recognize the GGGVMM motif and the characteristic fold architecture, infer membership in the AADC family, and conclude PLP. The four distractors belong to entirely unrelated enzyme classes (tungstopterin → anaerobic formate dehydrogenases; Fe(2+) → dioxygenases/oxidoreductases; pantetheine 4'-phosphate → acyltransferases/CoA-dependent enzymes), none of which share this sequence architecture.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GGGVMM motif and overall sequence architecture are transferable family-level features shared across aromatic amino acid decarboxylases. Recognizing these features allows a knowledgeable model to place the protein in a family that is exclusively PLP-dependent, cleanly distinguishing option B from the three structurally and mechanistically unrelated alternatives."
  },
  "case_id": "cofactor_0057",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H5",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0AA51Z3J4) explicitly annotates pyridoxal 5'-phosphate as the cofactor (evidence ECO:0000250, inferred by similarity from P20711, the human DOPA decarboxylase). The protein is annotated as L-tyrosine/L-DOPA decarboxylase 2 (EC 4.1.1.25 and 4.1.1.28), both of which are universally PLP-dependent aromatic amino acid decarboxylases. The EC assignments themselves carry experimental evidence (ECO:0000269 from PubMed 38835170). PLP is the sole known cofactor for all members of this enzyme family."
  },
  "important_caveats": [
    "The cofactor annotation in UniProt carries evidence code ECO:0000250 (inferred by similarity from P20711), not direct experimental determination for this exact protein. However, the EC assignments (4.1.1.25, 4.1.1.28) are experimentally supported (ECO:0000269), and PLP dependence is a defining, universal property of the AADC family.",
    "The protein is from Lophophora williamsii (peyote cactus), involved in mescaline biosynthesis. This organism context was not provided to the evaluated model but is not needed for the family-level cofactor inference.",
    "The sequence is 522 aa, consistent with the typical AADC length range (~450–530 aa), further supporting family assignment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four cofactor options (tungstopterin, PLP, Fe2+, pantetheine 4'-phosphate) correspond to entirely distinct enzyme superfamilies with no overlap in sequence features. The GGGVMM motif and AADC-family architecture unambiguously point to PLP and exclude the other three."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0057",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0AA51Z3J4) explicitly annotates pyridoxal 5'-phosphate as the cofactor (evidence ECO:0000250, inferred by similarity from P20711, the human DOPA decarboxylase). The protein is annotated as L-tyrosine/L-DOPA decarboxylase 2 (EC 4.1.1.25 and 4.1.1.28), both of which are universally PLP-dependent aromatic amino acid decarboxylases. The EC assignments themselves carry experimental evidence (ECO:0000269 from PubMed 38835170). PLP is the sole known cofactor for all members of this enzyme family.",
    "evidence_ids": ["C5", "H5", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved 'GGGVMM' motif (around residues 155-160), which is a hallmark of the aromatic amino acid decarboxylase (AADC) family within the Group IV PLP-dependent enzyme superfamily. This motif, together with the overall ~522-residue length, the presence of a conserved lysine in the context 'KDPSSLVRCLSTNPEYLKNKATDTQQVVDYKDWQ' (the catalytic lysine that forms the internal aldimine with PLP), and the general domain architecture, are recognizable signatures of AADCs (e.g., human DOPA decarboxylase P20711, histidine decarboxylase, tryptophan decarboxylase). All known aromatic amino acid decarboxylases are obligately PLP-dependent; no member of this family uses tungstopterin, free Fe(2+), or pantetheine 4'-phosphate. A model trained on homologous proteins can recognize the GGGVMM motif and the characteristic fold architecture, infer membership in the AADC family, and conclude PLP. The four distractors belong to entirely unrelated enzyme classes (tungstopterin → anaerobic formate dehydrogenases; Fe(2+) → dioxygenases/oxidoreductases; pantetheine 4'-phosphate → acyltransferases/CoA-dependent enzymes), none of which share this sequence architecture.",
    "missing_item_specific_fact": "",
    "reason": "The GGGVMM motif and overall sequence architecture are transferable family-level features shared across aromatic amino acid decarboxylases. Recognizing these features allows a knowledgeable model to place the protein in a family that is exclusively PLP-dependent, cleanly distinguishing option B from the three structurally and mechanistically unrelated alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four cofactor options (tungstopterin, PLP, Fe2+, pantetheine 4'-phosphate) correspond to entirely distinct enzyme superfamilies with no overlap in sequence features. The GGGVMM motif and AADC-family architecture unambiguously point to PLP and exclude the other three."
  },
  "important_caveats": [
    "The cofactor annotation in UniProt carries evidence code ECO:0000250 (inferred by similarity from P20711), not direct experimental determination for this exact protein. However, the EC assignments (4.1.1.25, 4.1.1.28) are experimentally supported (ECO:0000269), and PLP dependence is a defining, universal property of the AADC family.",
    "The protein is from Lophophora williamsii (peyote cactus), involved in mescaline biosynthesis. This organism context was not provided to the evaluated model but is not needed for the family-level cofactor inference.",
    "The sequence is 522 aa, consistent with the typical AADC length range (~450–530 aa), further supporting family assignment."
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
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:597326\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P20711\",\"source\":\"UniProtKB\"}],\"name\":\"pyridoxal 5'-phosphate\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
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

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AA51Z3J4.json)

```json
{
  "evidence_id": "C7",
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
  "excerpt": "DE   RecName: Full=L-tyrosine/L-DOPA decarboxylase 2 {ECO:0000303|PubMed:38835170};\nDE            Short=LwTyDC2 {ECO:0000303|PubMed:38835170};\nDE            EC=4.1.1.25 {ECO:0000269|PubMed:38835170};\nDE            EC=4.1.1.28 {ECO:0000269|PubMed:38835170};\nDE   AltName: Full=Aromatic amino acid decarboxylase 1 {ECO:0000303|PubMed:37675639};\nDE            Short=LwTyDC1 {ECO:0000303|PubMed:37675639};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-11",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H4",
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

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9)

```json
{
  "entry_version": 9,
  "evidence_id": "H5",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=pyridoxal 5'-phosphate; Xref=ChEBI:CHEBI:597326;\nCC         Evidence={ECO:0000250|UniProtKB:P20711};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:27.253771+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-62",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "19e4ff04ca3b4f42fdb12b700298efb9fc0014c90ac7a93cbc253e504d45c473",
  "url": "https://rest.uniprot.org/unisave/A0AA51Z3J4?format=txt&versions=9"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 57. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
