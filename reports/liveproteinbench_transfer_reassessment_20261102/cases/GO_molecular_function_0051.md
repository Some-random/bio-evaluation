# GO_molecular_function_0051

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0051.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — structural molecule activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSSVLKAFERFTIEQELQDRGEEGSIPPETLKSAVKVFVINTPNPTTRYQMLNFCLRIICSQNARASHRVGALITLFSLPSAGMQNHIRLADRSPEAQIERCEIDGFEPGTYRLIPNARANLTANEIAAYALLADDLPPTINNGTPYVHADVEGQPCDEIEQFLDRCYSVLIQAWVMVCKCMTAYDQPAGSADRRFAKYQQQGRLEARYMLQPEAQRLIQTAIRKSLVVRQYLTFELQLARRQGLLSNRYYAMVGDIGKYIENSGLTAFFLTLKYALGTKWSPLSLAAFTGELTKLRSLMMLYRGLGEQARYLALLEAPQIMDFAPGGYPLIFSYAMGVGTVLDVQMRNYTYARPFLNGYYFQIGVETARRQQGTVDNRVADDLGLTPEQRTEVTQLVDRLARGRGAGIPGGPVNPFVPPVQQQQPAAVYEDIPALEESDDDGDEDGGAGFQHGAQAPAVRQGGQNDFRAQPLQDPIQAQLFMPLYPQVSNIPNHQNHQINRIGGMEHQDLLRYNENGDSQQDARGEHGNTFPNNPNQNAQSQVGDWDE

[Multiple Choices]
A. structural molecule activity
B. mechanosensitive monoatomic cation channel activity
C. carboxylesterase activity
D. magnesium ion binding
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

> The sequence-matched UniProt entry describes this protein as forming a helical nucleocapsid and annotates structural molecule activity. The functional description is by similarity, and the GO annotation is computational (IEA:InterPro), so this supports the key without establishing it through direct experimental evidence.

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a substantial ordered protein core followed by a low-complexity, likely flexible C-terminal region, a pattern compatible with viral nucleoproteins. Transferable knowledge of this protein family is that nucleoproteins assemble with genomic RNA into nucleocapsids, contributing structural integrity. That favors structural molecule activity (A) over a mechanosensitive channel, carboxylesterase, or magnesium-ion-binding function. The sequence pattern alone is not definitive, but family-level recognition provides a meaningful distinction.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from sequence architecture and the known role of viral nucleoproteins provides a credible basis to select A among these alternatives; recalling this exact protein's record is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices distinguish a nucleocapsid structural role from unrelated channel and enzyme functions. Magnesium binding is possible for many proteins in a broad sense, but the input provides no specific basis for that molecular-function assignment.


### Important caveats

- The functional source description is qualified as by similarity, and the GO structural-molecule annotation is computational rather than direct experimental evidence.
- RNA binding is also annotated for this protein, but it is not among the offered choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a substantial ordered protein core followed by a low-complexity, likely flexible C-terminal region, a pattern compatible with viral nucleoproteins. Transferable knowledge of this protein family is that nucleoproteins assemble with genomic RNA into nucleocapsids, contributing structural integrity. That favors structural molecule activity (A) over a mechanosensitive channel, carboxylesterase, or magnesium-ion-binding function. The sequence pattern alone is not definitive, but family-level recognition provides a meaningful distinction.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence architecture and the known role of viral nucleoproteins provides a credible basis to select A among these alternatives; recalling this exact protein's record is not necessary."
  },
  "case_id": "GO_molecular_function_0051",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry describes this protein as forming a helical nucleocapsid and annotates structural molecule activity. The functional description is by similarity, and the GO annotation is computational (IEA:InterPro), so this supports the key without establishing it through direct experimental evidence."
  },
  "important_caveats": [
    "The functional source description is qualified as by similarity, and the GO structural-molecule annotation is computational rather than direct experimental evidence.",
    "RNA binding is also annotated for this protein, but it is not among the offered choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish a nucleocapsid structural role from unrelated channel and enzyme functions. Magnesium binding is possible for many proteins in a broad sense, but the input provides no specific basis for that molecular-function assignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0051",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry describes this protein as forming a helical nucleocapsid and annotates structural molecule activity. The functional description is by similarity, and the GO annotation is computational (IEA:InterPro), so this supports the key without establishing it through direct experimental evidence.",
    "evidence_ids": ["C5", "C7", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a substantial ordered protein core followed by a low-complexity, likely flexible C-terminal region, a pattern compatible with viral nucleoproteins. Transferable knowledge of this protein family is that nucleoproteins assemble with genomic RNA into nucleocapsids, contributing structural integrity. That favors structural molecule activity (A) over a mechanosensitive channel, carboxylesterase, or magnesium-ion-binding function. The sequence pattern alone is not definitive, but family-level recognition provides a meaningful distinction.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from sequence architecture and the known role of viral nucleoproteins provides a credible basis to select A among these alternatives; recalling this exact protein's record is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish a nucleocapsid structural role from unrelated channel and enzyme functions. Magnesium binding is possible for many proteins in a broad sense, but the input provides no specific basis for that molecular-function assignment."
  },
  "important_caveats": [
    "The functional source description is qualified as by similarity, and the GO structural-molecule annotation is computational rather than direct experimental evidence.",
    "RNA binding is also annotated for this protein, but it is not among the offered choices."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (Q5SC49, Mumps virus nucleoprotein) annotates GO:0005198 (structural molecule activity) with evidence code IEA:InterPro. The functional comment describes the protein forming the helical nucleocapsid with 12.71 N subunits per turn, protecting the genome from nucleases — a structural role. The annotation is computational (IEA:InterPro) rather than experimentally validated, but it is consistent with the well-established role of paramyxovirus nucleoproteins as structural scaffold components of the nucleocapsid. The protein also carries GO:0003723 (RNA binding), but among the four offered choices, structural molecule activity is the best-supported primary molecular function annotation.

Citations as saved: [C7](#evidence-c7), [C5](#evidence-c5), [H4](#evidence-h4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can apply several transferable inferences: (1) The sequence is ~549 aa with no identifiable transmembrane helices or channel-forming topology, which eliminates B (mechanosensitive monoatomic cation channel activity requires multiple TM domains as seen in PIEZO, MscL/MscS families). (2) There is no GxSxG serine hydrolase nucleophile motif, no α/β-hydrolase fold architecture, and no carboxylesterase catalytic triad, eliminating C. (3) The sequence length, overall composition, and domain architecture are consistent with paramyxovirus nucleoproteins (N proteins of measles, Newcastle disease, parainfluenza, and other rubulavirines are well-known helical nucleocapsid-forming structural proteins). This family-level knowledge — that paramyxovirus N proteins encapsidate the genome into a helical ribonucleoprotein complex — is a well-established, transferable pattern across many other paramyxovirus N proteins. (4) While Mg binding (D) is a generic annotation possible for many proteins, the PRIMARY molecular function of a nucleoprotein is to form the structural scaffold of the nucleocapsid, not to bind magnesium. Thus, among the four choices, A is distinguished by family-level inference from other paramyxovirus N proteins.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The answer can be reached through family-level inference: recognizing paramyxovirus N-protein family features (size, lack of TM domains, lack of catalytic motifs) and applying the well-known structural role of these proteins across the family (measles N, NDV N, PIV N, etc.) to select structural molecule activity over the other three options. The distractors B and C are eliminated by clear absence of channel and esterase features; D is eliminated because Mg binding is not the primary function of a nucleocapsid protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only A (structural molecule activity) is consistent with a viral nucleoprotein. B requires TM domains absent here, C requires hydrolase motifs absent here, and D (Mg binding) is not the primary function of a nucleocapsid-forming protein. RNA binding (also annotated) is not offered as a competing option.


### Important caveats

- The GO:0005198 annotation carries evidence code IEA:InterPro, meaning it is computationally inferred rather than experimentally validated.
- The protein also carries GO:0003723 (RNA binding) as an annotation, which is arguably also a primary molecular function; however, RNA binding is not among the offered choices.
- Family recognition of paramyxovirus N proteins relies on the model having learned patterns from other paramyxovirus nucleoproteins (measles, NDV, parainfluenza, etc.), which is permitted transferable knowledge.
- The reviewer-only evidence confirms the protein is Mumps virus N protein, but this identification was not available to the evaluated model; the model must infer the family from sequence features.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can apply several transferable inferences: (1) The sequence is ~549 aa with no identifiable transmembrane helices or channel-forming topology, which eliminates B (mechanosensitive monoatomic cation channel activity requires multiple TM domains as seen in PIEZO, MscL/MscS families). (2) There is no GxSxG serine hydrolase nucleophile motif, no α/β-hydrolase fold architecture, and no carboxylesterase catalytic triad, eliminating C. (3) The sequence length, overall composition, and domain architecture are consistent with paramyxovirus nucleoproteins (N proteins of measles, Newcastle disease, parainfluenza, and other rubulavirines are well-known helical nucleocapsid-forming structural proteins). This family-level knowledge — that paramyxovirus N proteins encapsidate the genome into a helical ribonucleoprotein complex — is a well-established, transferable pattern across many other paramyxovirus N proteins. (4) While Mg binding (D) is a generic annotation possible for many proteins, the PRIMARY molecular function of a nucleoprotein is to form the structural scaffold of the nucleocapsid, not to bind magnesium. Thus, among the four choices, A is distinguished by family-level inference from other paramyxovirus N proteins.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The answer can be reached through family-level inference: recognizing paramyxovirus N-protein family features (size, lack of TM domains, lack of catalytic motifs) and applying the well-known structural role of these proteins across the family (measles N, NDV N, PIV N, etc.) to select structural molecule activity over the other three options. The distractors B and C are eliminated by clear absence of channel and esterase features; D is eliminated because Mg binding is not the primary function of a nucleocapsid protein."
  },
  "case_id": "GO_molecular_function_0051",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "C5",
      "H4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (Q5SC49, Mumps virus nucleoprotein) annotates GO:0005198 (structural molecule activity) with evidence code IEA:InterPro. The functional comment describes the protein forming the helical nucleocapsid with 12.71 N subunits per turn, protecting the genome from nucleases — a structural role. The annotation is computational (IEA:InterPro) rather than experimentally validated, but it is consistent with the well-established role of paramyxovirus nucleoproteins as structural scaffold components of the nucleocapsid. The protein also carries GO:0003723 (RNA binding), but among the four offered choices, structural molecule activity is the best-supported primary molecular function annotation."
  },
  "important_caveats": [
    "The GO:0005198 annotation carries evidence code IEA:InterPro, meaning it is computationally inferred rather than experimentally validated.",
    "The protein also carries GO:0003723 (RNA binding) as an annotation, which is arguably also a primary molecular function; however, RNA binding is not among the offered choices.",
    "Family recognition of paramyxovirus N proteins relies on the model having learned patterns from other paramyxovirus nucleoproteins (measles, NDV, parainfluenza, etc.), which is permitted transferable knowledge.",
    "The reviewer-only evidence confirms the protein is Mumps virus N protein, but this identification was not available to the evaluated model; the model must infer the family from sequence features."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only A (structural molecule activity) is consistent with a viral nucleoprotein. B requires TM domains absent here, C requires hydrolase motifs absent here, and D (Mg binding) is not the primary function of a nucleocapsid-forming protein. RNA binding (also annotated) is not offered as a competing option."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0051",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (Q5SC49, Mumps virus nucleoprotein) annotates GO:0005198 (structural molecule activity) with evidence code IEA:InterPro. The functional comment describes the protein forming the helical nucleocapsid with 12.71 N subunits per turn, protecting the genome from nucleases — a structural role. The annotation is computational (IEA:InterPro) rather than experimentally validated, but it is consistent with the well-established role of paramyxovirus nucleoproteins as structural scaffold components of the nucleocapsid. The protein also carries GO:0003723 (RNA binding), but among the four offered choices, structural molecule activity is the best-supported primary molecular function annotation.",
    "evidence_ids": ["C7", "C5", "H4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can apply several transferable inferences: (1) The sequence is ~549 aa with no identifiable transmembrane helices or channel-forming topology, which eliminates B (mechanosensitive monoatomic cation channel activity requires multiple TM domains as seen in PIEZO, MscL/MscS families). (2) There is no GxSxG serine hydrolase nucleophile motif, no α/β-hydrolase fold architecture, and no carboxylesterase catalytic triad, eliminating C. (3) The sequence length, overall composition, and domain architecture are consistent with paramyxovirus nucleoproteins (N proteins of measles, Newcastle disease, parainfluenza, and other rubulavirines are well-known helical nucleocapsid-forming structural proteins). This family-level knowledge — that paramyxovirus N proteins encapsidate the genome into a helical ribonucleoprotein complex — is a well-established, transferable pattern across many other paramyxovirus N proteins. (4) While Mg binding (D) is a generic annotation possible for many proteins, the PRIMARY molecular function of a nucleoprotein is to form the structural scaffold of the nucleocapsid, not to bind magnesium. Thus, among the four choices, A is distinguished by family-level inference from other paramyxovirus N proteins.",
    "missing_item_specific_fact": "",
    "reason": "The answer can be reached through family-level inference: recognizing paramyxovirus N-protein family features (size, lack of TM domains, lack of catalytic motifs) and applying the well-known structural role of these proteins across the family (measles N, NDV N, PIV N, etc.) to select structural molecule activity over the other three options. The distractors B and C are eliminated by clear absence of channel and esterase features; D is eliminated because Mg binding is not the primary function of a nucleocapsid protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only A (structural molecule activity) is consistent with a viral nucleoprotein. B requires TM domains absent here, C requires hydrolase motifs absent here, and D (Mg binding) is not the primary function of a nucleocapsid-forming protein. RNA binding (also annotated) is not offered as a competing option."
  },
  "important_caveats": [
    "The GO:0005198 annotation carries evidence code IEA:InterPro, meaning it is computationally inferred rather than experimentally validated.",
    "The protein also carries GO:0003723 (RNA binding) as an annotation, which is arguably also a primary molecular function; however, RNA binding is not among the offered choices.",
    "Family recognition of paramyxovirus N proteins relies on the model having learned patterns from other paramyxovirus nucleoproteins (measles, NDV, parainfluenza, etc.), which is permitted transferable knowledge.",
    "The reviewer-only evidence confirms the protein is Mumps virus N protein, but this identification was not available to the evaluated model; the model must infer the family from sequence features."
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
  "benchmark_sequence_length": 549,
  "benchmark_sequence_sha256": "6f53282ef1585614d07505fa9d0dbac53f0388a2394a6b989ff7aa8402940230",
  "current_entry_audit": {
    "entryVersion": 55,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2004-12-21",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b097b38bc60c8032d19262ea1477b4c7623e9e3d70806bae288336783d0f831f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 549,
  "current_source_sequence_sha256": "6f53282ef1585614d07505fa9d0dbac53f0388a2394a6b989ff7aa8402940230",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 53,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q5SC49",
  "selected_historical_entry_version": 53,
  "selected_historical_record_sha256": "cfa7655583d5a9d5b6f1722be1a1d1e12bae4f465ed7b2ad2f5c2c9bca7b2a30",
  "selected_historical_source_sequence_length": 549,
  "selected_historical_source_sequence_sha256": "6f53282ef1585614d07505fa9d0dbac53f0388a2394a6b989ff7aa8402940230",
  "selected_historical_version": {
    "accession": "Q5SC49",
    "database": "Swiss-Prot",
    "entryVersion": 53,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NCAP_MUMPZ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC49.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q5SC49\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:31:26.623016+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b097b38bc60c8032d19262ea1477b4c7623e9e3d70806bae288336783d0f831f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC49.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC49.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":55,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2004-12-21\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:31:26.623016+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b097b38bc60c8032d19262ea1477b4c7623e9e3d70806bae288336783d0f831f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC49.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC49.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"MuV\",\"lineage\":[\"Viruses\",\"Riboviria\",\"Orthornavirae\",\"Negarnaviricota\",\"Haploviricotina\",\"Monjiviricetes\",\"Mononegavirales\",\"Paramyxoviridae\",\"Rubulavirinae\",\"Orthorubulavirus\",\"Orthorubulavirus parotitidis\",\"Mumps orthorubulavirus\"],\"scientificName\":\"Mumps virus genotype N (strain L-Zagreb vaccine)\",\"taxonId\":301186}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:31:26.623016+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b097b38bc60c8032d19262ea1477b4c7623e9e3d70806bae288336783d0f831f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC49.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC49.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"Nucleocapsid protein\"},\"shortNames\":[{\"value\":\"NP\"},{\"value\":\"Protein N\"}]}],\"recommendedName\":{\"fullName\":{\"value\":\"Nucleoprotein\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:31:26.623016+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b097b38bc60c8032d19262ea1477b4c7623e9e3d70806bae288336783d0f831f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC49.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC49.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"D5LWW7\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P06159\",\"source\":\"UniProtKB\"}],\"value\":\"Forms the helical nucleocapsid (NC) with 12.71 N subunits per helical turn and a rise of 5.3 Angstrom per N subunit, protecting the genome from nucleases (By similarity). The encapsidated genomic RNA serves as template for transcription and replication; encapsidation by N is coupled to RNA synthesis (By similarity). Forms the encapsidation complex with the phosphoprotein protein P (By similarity). Before encapsidation, the newly synthesized free N protein, so-called N0, is chaperoned by P (By similarity)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:31:26.623016+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b097b38bc60c8032d19262ea1477b4c7623e9e3d70806bae288336783d0f831f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC49.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC49.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0003723\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:RNA binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-KW\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/8",
  "retrieved_utc": "2026-11-02T04:31:26.623016+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b097b38bc60c8032d19262ea1477b4c7623e9e3d70806bae288336783d0f831f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC49.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q5SC49.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005198\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:structural molecule activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "retrieved_utc": "2026-11-02T04:31:26.623016+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b097b38bc60c8032d19262ea1477b4c7623e9e3d70806bae288336783d0f831f",
  "url": "https://rest.uniprot.org/uniprotkb/Q5SC49.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC49?format=txt&versions=53)

```json
{
  "entry_version": 53,
  "evidence_id": "H1",
  "excerpt": "ID   NCAP_MUMPZ              Reviewed;         549 AA.\nAC   Q5SC49;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   21-DEC-2004, sequence version 1.\nDT   28-JAN-2026, entry version 53.\nDE   RecName: Full=Nucleoprotein;\nDE   AltName: Full=Nucleocapsid protein;\nDE            Short=NP;\nDE            Short=Protein N;\nGN   Name=N; Synonyms=NP;\nOS   Mumps virus genotype N (strain L-Zagreb vaccine) (MuV).\nOC   Viruses; Riboviria; Orthornavirae; Negarnaviricota; Haploviricotina;\nOC   Monjiviricetes; Mononegavirales; Paramyxoviridae; Rubulavirinae;\nOC   Orthorubulavirus; Orthorubulavirus parotitidis; Mumps orthorubulavirus.\nOX   NCBI_TaxID=301186;\nOH   NCBI_TaxID=9606; Homo sapiens (Human).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:28.432764+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cfa7655583d5a9d5b6f1722be1a1d1e12bae4f465ed7b2ad2f5c2c9bca7b2a30",
  "url": "https://rest.uniprot.org/unisave/Q5SC49?format=txt&versions=53"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC49?format=txt&versions=53)

```json
{
  "entry_version": 53,
  "evidence_id": "H2",
  "excerpt": "CC   -!- FUNCTION: Forms the helical nucleocapsid (NC) with 12.71 N subunits per\nCC       helical turn and a rise of 5.3 Angstrom per N subunit, protecting the\nCC       genome from nucleases (By similarity). The encapsidated genomic RNA\nCC       serves as template for transcription and replication; encapsidation by\nCC       N is coupled to RNA synthesis (By similarity). Forms the encapsidation\nCC       complex with the phosphoprotein protein P (By similarity). Before\nCC       encapsidation, the newly synthesized free N protein, so-called N0, is\nCC       chaperoned by P (By similarity). {ECO:0000250|UniProtKB:D5LWW7,\nCC       ECO:0000250|UniProtKB:P06159}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:28.432764+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cfa7655583d5a9d5b6f1722be1a1d1e12bae4f465ed7b2ad2f5c2c9bca7b2a30",
  "url": "https://rest.uniprot.org/unisave/Q5SC49?format=txt&versions=53"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC49?format=txt&versions=53)

```json
{
  "entry_version": 53,
  "evidence_id": "H3",
  "excerpt": "DR   GO; GO:0003723; F:RNA binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:28.432764+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 90-90",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cfa7655583d5a9d5b6f1722be1a1d1e12bae4f465ed7b2ad2f5c2c9bca7b2a30",
  "url": "https://rest.uniprot.org/unisave/Q5SC49?format=txt&versions=53"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q5SC49?format=txt&versions=53)

```json
{
  "entry_version": 53,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0005198; F:structural molecule activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:28.432764+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 91-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "cfa7655583d5a9d5b6f1722be1a1d1e12bae4f465ed7b2ad2f5c2c9bca7b2a30",
  "url": "https://rest.uniprot.org/unisave/Q5SC49?format=txt&versions=53"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000287\nname: magnesium ion binding\nnamespace: molecular_function\ndef: \"Binding to a magnesium (Mg) ion.\" [GOC:ai]\nsynonym: \"magnesium binding\" EXACT []\nsynonym: \"Mg binding\" EXACT []\nis_a: GO:0046872 ! metal ion binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000287",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 3126-3134",
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
  "excerpt": "[Term]\nid: GO:0005198\nname: structural molecule activity\nnamespace: molecular_function\ndef: \"The action of a molecule that contributes to the structural integrity of a complex.\" [GOC:mah, GOC:vw]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nis_a: GO:0003674 ! molecular_function\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005198",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 54676-54694",
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
  "excerpt": "[Term]\nid: GO:0106435\nname: carboxylesterase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: a carboxylic ester + H2O = a carboxylate + an alcohol + H+.\" [RHEA:21164]\ncomment: Note: This covers a broad range of specificity; also hydrolyzes vitamin A esters.\nsynonym: \"ali-esterase activity\" RELATED [EC:3.1.1.1]\nsynonym: \"alpha-carboxylesterase activity\" NARROW []\nsynonym: \"B-esterase activity\" NARROW [EC:3.1.1.1]\nsynonym: \"cocaine esterase\" NARROW [EC:3.1.1.1]\nsynonym: \"nonspecific carboxylesterase activity\" RELATED []\nsynonym: \"procaine esterase\" NARROW [] {comment=\"EC:3.1.1.1\"}\nsynonym: \"serine esterase activity\" NARROW []\nsynonym: \"triacetin esterase\" NARROW []\nsynonym: \"vitamin A esterase\" NARROW []\nxref: EC:3.1.1.1\nxref: MetaCyc:CARBOXYLESTERASE-RXN\nxref: Reactome:R-HSA-9619024 \"CES1 trimer hydrolyses ACEI pro-drugs to ACEIs\"\nxref: Reactome:R-HSA-9727567 \"CES1 hydrolyses sacubitril to sacubitrilat\"\nxref: Reactome:R-HSA-9749647 \"CES2 hydrolyzes ASA-\"\nxref: RHEA:21164\nxref: RHEA:31779\nxref: RHEA:38555\nxref: RHEA:47348\nxref: RHEA:47352\nxref: RHEA:47356\nxref: RHEA:47360\nxref: RHEA:47364\nxref: RHEA:47388\nxref: RHEA:47392\nxref: RHEA:50136\nxref: RHEA:50144\nxref: RHEA:50148\nxref: RHEA:59388\nxref: RHEA:63052\nis_a: GO:0052689 ! carboxylic ester hydrolase activity\nproperty_value: skos:exactMatch EC:3.1.1.1\nproperty_value: skos:exactMatch RHEA:21164\nproperty_value: skos:narrowMatch RHEA:31779\nproperty_value: skos:narrowMatch RHEA:38555\nproperty_value: skos:narrowMatch RHEA:47348\nproperty_value: skos:narrowMatch RHEA:47352\nproperty_value: skos:narrowMatch RHEA:47356\nproperty_value: skos:narrowMatch RHEA:47360\nproperty_value: skos:narrowMatch RHEA:47364\nproperty_value: skos:narrowMatch RHEA:47388\nproperty_value: skos:narrowMatch RHEA:47392\nproperty_value: skos:narrowMatch RHEA:50136\nproperty_value: skos:narrowMatch RHEA:50144\nproperty_value: skos:narrowMatch RHEA:50148\nproperty_value: skos:narrowMatch RHEA:59388\nproperty_value: skos:narrowMatch RHEA:63052\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0106435",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 430643-430695",
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
  "excerpt": "[Term]\nid: GO:0140135\nname: mechanosensitive monoatomic cation channel activity\nnamespace: molecular_function\ndef: \"Enables the transmembrane transfer of a monoatomic cation by a channel that opens in response to a mechanical stress.\" [GOC:ha, PMID:22343900]\nsynonym: \"mechanically-gated cation channel activity\" EXACT []\nsynonym: \"mechanosensitive cation channel activity\" BROAD []\nxref: Reactome:R-HSA-9659380 \"Mechanoelectrical transduction (MET) channel transports cations from the extracellular region into the cytosol of stereocilia of inner hair cell\"\nxref: Reactome:R-HSA-9663363 \"Mechanoelectrical transduction (MET) channel transports cations into the cytosol of stereocilia of cochlear outer hair cell\"\nxref: Reactome:R-HSA-9855089 \"PIEZO1 trimer passively transports cations across the plasma membrane according to their electrochemical gradients\"\nis_a: GO:0005261 ! monoatomic cation channel activity\nis_a: GO:0008381 ! mechanosensitive monoatomic ion channel activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0140135",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 437568-437580",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 51. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
