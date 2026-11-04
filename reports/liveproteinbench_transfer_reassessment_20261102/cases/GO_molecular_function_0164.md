# GO_molecular_function_0164

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0164.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — metal ion binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQTVTLSIFRFNEFEKRLWVLGQMTANKLGMHYLPKAKFWKMFGSGTGQGFTPKPNWHVWSILAVWPDEETARREVAESPIYQRWTKMADESYTVLLQPTSAWGKWDGKEPFEPVKPASDVRPIAALTRATVKFWKAERFWAREPAISHMIGRNKDVVFKIGVGEVPFVQQVTFSIWPDARSMEEFARGAGGPHGEAIKAVRAENWFKEELYARFQILGTIGKWEGKDPVGEALTARPSEAPKPAPAPAAAQPAPAAEAPKPAPAPVAEKPALAVEMPKPAEPPKPVVEAPKPASAPVASKPMPQGGKPNFKGKPGKGGRKENA

[Multiple Choices]
A. RNA polymerase II transcription regulatory region sequence-specific DNA binding
B. chromatin binding
C. D-lactate dehydrogenase activity
D. metal ion binding
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

> The historical UniProt entry matching the supplied sequence assigns metal ion binding (GO:0046872) by IEA:UniProtKB-KW. This supports D as a database annotation, but it is computational rather than direct experimental evidence. The entry also describes a spheroidene monooxygenase activity, which is not among the options.

Citations as saved: [H9](#evidence-h9), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> Whether this exact protein is annotated or experimentally shown to bind a metal ion; the sequence and choices alone do not establish that property.


**Reason**

> The sequence may indicate a bacterial enzyme, making the eukaryotic transcription and chromatin choices poor fits, but that does not distinguish metal-ion binding from the offered dehydrogenase activity. Monooxygenase-like function, even if inferred from related proteins, does not by itself establish that this protein binds a metal. Selecting D therefore depends on an item-specific annotation or measurement not supplied in the question.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No second offered choice is comparably supported. The mismatch is that the documented spheroidene monooxygenase activity is not offered, while D is a broader database-annotated function.


### Important caveats

- The sequence match supports applying the historical UniProt annotation to this sequence, but the IEA code does not establish experimental confirmation.
- Reviewer-only source evidence was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this exact protein is annotated or experimentally shown to bind a metal ion; the sequence and choices alone do not establish that property.",
    "reason": "The sequence may indicate a bacterial enzyme, making the eukaryotic transcription and chromatin choices poor fits, but that does not distinguish metal-ion binding from the offered dehydrogenase activity. Monooxygenase-like function, even if inferred from related proteins, does not by itself establish that this protein binds a metal. Selecting D therefore depends on an item-specific annotation or measurement not supplied in the question."
  },
  "case_id": "GO_molecular_function_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "H9",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The historical UniProt entry matching the supplied sequence assigns metal ion binding (GO:0046872) by IEA:UniProtKB-KW. This supports D as a database annotation, but it is computational rather than direct experimental evidence. The entry also describes a spheroidene monooxygenase activity, which is not among the options."
  },
  "important_caveats": [
    "The sequence match supports applying the historical UniProt annotation to this sequence, but the IEA code does not establish experimental confirmation.",
    "Reviewer-only source evidence was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second offered choice is comparably supported. The mismatch is that the documented spheroidene monooxygenase activity is not offered, while D is a broader database-annotated function."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The historical UniProt entry matching the supplied sequence assigns metal ion binding (GO:0046872) by IEA:UniProtKB-KW. This supports D as a database annotation, but it is computational rather than direct experimental evidence. The entry also describes a spheroidene monooxygenase activity, which is not among the options.",
    "evidence_ids": ["H9", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "Whether this exact protein is annotated or experimentally shown to bind a metal ion; the sequence and choices alone do not establish that property.",
    "reason": "The sequence may indicate a bacterial enzyme, making the eukaryotic transcription and chromatin choices poor fits, but that does not distinguish metal-ion binding from the offered dehydrogenase activity. Monooxygenase-like function, even if inferred from related proteins, does not by itself establish that this protein binds a metal. Selecting D therefore depends on an item-specific annotation or measurement not supplied in the question."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second offered choice is comparably supported. The mismatch is that the documented spheroidene monooxygenase activity is not offered, while D is a broader database-annotated function."
  },
  "important_caveats": [
    "The sequence match supports applying the historical UniProt annotation to this sequence, but the IEA code does not establish experimental confirmation.",
    "Reviewer-only source evidence was not available to the evaluated model."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry for this protein (Q3J189, spheroidene monooxygenase, EC 1.14.15.9) carries the GO annotation GO:0046872 'metal ion binding' (evidence_id H9, IEA:UniProtKB-KW). The protein's catalytic reactions all involve &#91;2Fe-2S&#93;-&#91;ferredoxin&#93; as electron donors and the EC class 1.14.15.9 designates a non-heme iron-dependent monooxygenase, confirming metal (iron) cofactor binding. While the primary molecular function is more specifically 'spheroidene monooxygenase activity' (GO:0043823), the broader 'metal ion binding' annotation is present in the record and is consistent with the enzyme's requirement for iron cofactors. Among the four offered choices, D is the only annotation that applies to this bacterial enzyme.

Citations as saved: [H9](#evidence-h9), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [H8](#evidence-h8), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can eliminate three options through general biological reasoning without knowing this specific protein's annotation. (1) Options A (RNA polymerase II transcription regulatory region sequence-specific DNA binding) and B (chromatin binding) are eukaryotic-specific molecular functions: RNA Pol II is exclusive to eukaryotes, and chromatin (histone-DNA complexes) exists only in eukaryotic nuclei. The sequence shows no eukaryotic hallmarks—no nuclear localization signals, no zinc-finger/homeodomain/HTH DNA-binding motifs, no histone-binding domains—and its amino acid composition (high proportion of hydrophobic residues in the N-terminal ~100 aa, bacterial-like codon usage patterns, absence of eukaryotic-specific post-translational modification signals) is consistent with a bacterial membrane-associated enzyme. This eliminates A and B. (2) Option C (D-lactate dehydrogenase activity) requires a Rossmann-fold NAD(P)-binding domain with the characteristic GxGxxG motif and specific catalytic residues of 2-hydroxy-acid dehydrogenases (EC 1.1.99.6). The sequence lacks any recognizable Rossmann fold or dehydrogenase catalytic architecture. (3) Option D (metal ion binding) is a broad but valid molecular function for bacterial enzymes requiring metal cofactors. The sequence contains multiple His, Cys, Asp, and Glu residues distributed through the catalytic domain region that are consistent with metal coordination. Many bacterial monooxygenases and oxidoreductases require iron or other metal cofactors. By elimination of the three clearly inapplicable options, D is the only viable choice. This reasoning relies on general knowledge of eukaryotic vs. bacterial biology, enzyme fold recognition, and the ubiquity of metal cofactors in bacterial oxidoreductases—none of which requires knowing this specific protein's database entry.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The elimination logic is robust: A and B are eukaryotic-specific functions inapplicable to a bacterial protein identifiable by sequence composition; C requires a specific dehydrogenase fold absent from the sequence; D is the only remaining option and is broadly consistent with a bacterial enzyme that likely requires metal cofactors. This is a legitimate transferable-knowledge inference from general biology and does not require memorizing this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A and B are eukaryotic-specific functions that cannot apply to a bacterial protein. Option C describes a specific enzyme class (D-lactate dehydrogenase) whose structural and catalytic hallmarks are absent. Option D is the only annotation among the four that is compatible with a bacterial enzyme, making the choice unambiguous despite its generality.


### Important caveats

- The 'metal ion binding' annotation in UniProt is an IEA (Inferred by Electronic Annotation) keyword-based assignment, not a curated experimental annotation. The protein's primary molecular function is more specifically 'spheroidene monooxygenase activity' (GO:0043823), which is not offered as a choice.
- The question asks for the 'primary molecular function,' but 'metal ion binding' is a very generic secondary annotation. The answer is correct only because the more specific function is not among the options and the other three are clearly inapplicable.
- The bacterial origin of the protein is inferred from sequence composition and absence of eukaryotic features; the organism name is not given in the original input. However, the absence of eukaryotic-specific motifs and the overall sequence architecture strongly support a prokaryotic origin.
- The sequence does contain features consistent with a membrane-associated carotenoid biosynthesis enzyme (hydrophobic N-terminal region), but recognizing this specific family is not necessary to answer the question by elimination.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can eliminate three options through general biological reasoning without knowing this specific protein's annotation. (1) Options A (RNA polymerase II transcription regulatory region sequence-specific DNA binding) and B (chromatin binding) are eukaryotic-specific molecular functions: RNA Pol II is exclusive to eukaryotes, and chromatin (histone-DNA complexes) exists only in eukaryotic nuclei. The sequence shows no eukaryotic hallmarks—no nuclear localization signals, no zinc-finger/homeodomain/HTH DNA-binding motifs, no histone-binding domains—and its amino acid composition (high proportion of hydrophobic residues in the N-terminal ~100 aa, bacterial-like codon usage patterns, absence of eukaryotic-specific post-translational modification signals) is consistent with a bacterial membrane-associated enzyme. This eliminates A and B. (2) Option C (D-lactate dehydrogenase activity) requires a Rossmann-fold NAD(P)-binding domain with the characteristic GxGxxG motif and specific catalytic residues of 2-hydroxy-acid dehydrogenases (EC 1.1.99.6). The sequence lacks any recognizable Rossmann fold or dehydrogenase catalytic architecture. (3) Option D (metal ion binding) is a broad but valid molecular function for bacterial enzymes requiring metal cofactors. The sequence contains multiple His, Cys, Asp, and Glu residues distributed through the catalytic domain region that are consistent with metal coordination. Many bacterial monooxygenases and oxidoreductases require iron or other metal cofactors. By elimination of the three clearly inapplicable options, D is the only viable choice. This reasoning relies on general knowledge of eukaryotic vs. bacterial biology, enzyme fold recognition, and the ubiquity of metal cofactors in bacterial oxidoreductases—none of which requires knowing this specific protein's database entry.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The elimination logic is robust: A and B are eukaryotic-specific functions inapplicable to a bacterial protein identifiable by sequence composition; C requires a specific dehydrogenase fold absent from the sequence; D is the only remaining option and is broadly consistent with a bacterial enzyme that likely requires metal cofactors. This is a legitimate transferable-knowledge inference from general biology and does not require memorizing this protein's specific annotation."
  },
  "case_id": "GO_molecular_function_0164",
  "expected_answer_check": {
    "evidence_ids": [
      "H9",
      "H5",
      "H6",
      "H7",
      "H8",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (Q3J189, spheroidene monooxygenase, EC 1.14.15.9) carries the GO annotation GO:0046872 'metal ion binding' (evidence_id H9, IEA:UniProtKB-KW). The protein's catalytic reactions all involve [2Fe-2S]-[ferredoxin] as electron donors and the EC class 1.14.15.9 designates a non-heme iron-dependent monooxygenase, confirming metal (iron) cofactor binding. While the primary molecular function is more specifically 'spheroidene monooxygenase activity' (GO:0043823), the broader 'metal ion binding' annotation is present in the record and is consistent with the enzyme's requirement for iron cofactors. Among the four offered choices, D is the only annotation that applies to this bacterial enzyme."
  },
  "important_caveats": [
    "The 'metal ion binding' annotation in UniProt is an IEA (Inferred by Electronic Annotation) keyword-based assignment, not a curated experimental annotation. The protein's primary molecular function is more specifically 'spheroidene monooxygenase activity' (GO:0043823), which is not offered as a choice.",
    "The question asks for the 'primary molecular function,' but 'metal ion binding' is a very generic secondary annotation. The answer is correct only because the more specific function is not among the options and the other three are clearly inapplicable.",
    "The bacterial origin of the protein is inferred from sequence composition and absence of eukaryotic features; the organism name is not given in the original input. However, the absence of eukaryotic-specific motifs and the overall sequence architecture strongly support a prokaryotic origin.",
    "The sequence does contain features consistent with a membrane-associated carotenoid biosynthesis enzyme (hydrophobic N-terminal region), but recognizing this specific family is not necessary to answer the question by elimination."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are eukaryotic-specific functions that cannot apply to a bacterial protein. Option C describes a specific enzyme class (D-lactate dehydrogenase) whose structural and catalytic hallmarks are absent. Option D is the only annotation among the four that is compatible with a bacterial enzyme, making the choice unambiguous despite its generality."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0164",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry for this protein (Q3J189, spheroidene monooxygenase, EC 1.14.15.9) carries the GO annotation GO:0046872 'metal ion binding' (evidence_id H9, IEA:UniProtKB-KW). The protein's catalytic reactions all involve [2Fe-2S]-[ferredoxin] as electron donors and the EC class 1.14.15.9 designates a non-heme iron-dependent monooxygenase, confirming metal (iron) cofactor binding. While the primary molecular function is more specifically 'spheroidene monooxygenase activity' (GO:0043823), the broader 'metal ion binding' annotation is present in the record and is consistent with the enzyme's requirement for iron cofactors. Among the four offered choices, D is the only annotation that applies to this bacterial enzyme.",
    "evidence_ids": ["H9", "H5", "H6", "H7", "H8", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can eliminate three options through general biological reasoning without knowing this specific protein's annotation. (1) Options A (RNA polymerase II transcription regulatory region sequence-specific DNA binding) and B (chromatin binding) are eukaryotic-specific molecular functions: RNA Pol II is exclusive to eukaryotes, and chromatin (histone-DNA complexes) exists only in eukaryotic nuclei. The sequence shows no eukaryotic hallmarks—no nuclear localization signals, no zinc-finger/homeodomain/HTH DNA-binding motifs, no histone-binding domains—and its amino acid composition (high proportion of hydrophobic residues in the N-terminal ~100 aa, bacterial-like codon usage patterns, absence of eukaryotic-specific post-translational modification signals) is consistent with a bacterial membrane-associated enzyme. This eliminates A and B. (2) Option C (D-lactate dehydrogenase activity) requires a Rossmann-fold NAD(P)-binding domain with the characteristic GxGxxG motif and specific catalytic residues of 2-hydroxy-acid dehydrogenases (EC 1.1.99.6). The sequence lacks any recognizable Rossmann fold or dehydrogenase catalytic architecture. (3) Option D (metal ion binding) is a broad but valid molecular function for bacterial enzymes requiring metal cofactors. The sequence contains multiple His, Cys, Asp, and Glu residues distributed through the catalytic domain region that are consistent with metal coordination. Many bacterial monooxygenases and oxidoreductases require iron or other metal cofactors. By elimination of the three clearly inapplicable options, D is the only viable choice. This reasoning relies on general knowledge of eukaryotic vs. bacterial biology, enzyme fold recognition, and the ubiquity of metal cofactors in bacterial oxidoreductases—none of which requires knowing this specific protein's database entry.",
    "missing_item_specific_fact": "",
    "reason": "The elimination logic is robust: A and B are eukaryotic-specific functions inapplicable to a bacterial protein identifiable by sequence composition; C requires a specific dehydrogenase fold absent from the sequence; D is the only remaining option and is broadly consistent with a bacterial enzyme that likely requires metal cofactors. This is a legitimate transferable-knowledge inference from general biology and does not require memorizing this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A and B are eukaryotic-specific functions that cannot apply to a bacterial protein. Option C describes a specific enzyme class (D-lactate dehydrogenase) whose structural and catalytic hallmarks are absent. Option D is the only annotation among the four that is compatible with a bacterial enzyme, making the choice unambiguous despite its generality."
  },
  "important_caveats": [
    "The 'metal ion binding' annotation in UniProt is an IEA (Inferred by Electronic Annotation) keyword-based assignment, not a curated experimental annotation. The protein's primary molecular function is more specifically 'spheroidene monooxygenase activity' (GO:0043823), which is not offered as a choice.",
    "The question asks for the 'primary molecular function,' but 'metal ion binding' is a very generic secondary annotation. The answer is correct only because the more specific function is not among the options and the other three are clearly inapplicable.",
    "The bacterial origin of the protein is inferred from sequence composition and absence of eukaryotic features; the organism name is not given in the original input. However, the absence of eukaryotic-specific motifs and the overall sequence architecture strongly support a prokaryotic origin.",
    "The sequence does contain features consistent with a membrane-associated carotenoid biosynthesis enzyme (hydrophobic N-terminal region), but recognizing this specific family is not necessary to answer the question by elimination."
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
  "benchmark_sequence_length": 324,
  "benchmark_sequence_sha256": "729a48d70d6bbe461cee74d78aec69eadd0836a65bfc944cb3241dac87281b34",
  "current_entry_audit": {
    "entryVersion": 76,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-11-08",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 324,
  "current_source_sequence_sha256": "729a48d70d6bbe461cee74d78aec69eadd0836a65bfc944cb3241dac87281b34",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 74,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q3J189",
  "selected_historical_entry_version": 74,
  "selected_historical_record_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "selected_historical_source_sequence_length": 324,
  "selected_historical_source_sequence_sha256": "729a48d70d6bbe461cee74d78aec69eadd0836a65bfc944cb3241dac87281b34",
  "selected_historical_version": {
    "accession": "Q3J189",
    "database": "Swiss-Prot",
    "entryVersion": 74,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CRTA_CERS4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q3J189\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":76,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-11-08\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Rhodobacter sphaeroides\",\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Alphaproteobacteria\",\"Rhodobacterales\",\"Paracoccaceae\",\"Cereibacter\"],\"scientificName\":\"Cereibacter sphaeroides (strain ATCC 17023 / DSM 158 / JCM 6121 / CCUG 31486 / LMG 2827 / NBRC 12203 / NCIMB 8253 / ATH 2.4.1.)\",\"taxonId\":272943}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17055\",\"source\":\"UniProtKB\"}],\"value\":\"1.14.15.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"20851979\",\"source\":\"PubMed\"}],\"value\":\"Spheroidene monooxygenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17055\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"20851979\",\"source\":\"PubMed\"}],\"value\":\"Involved in the biosynthesis of the carotenoid spheroidene (By similarity). Catalyzes the introduction of one keto group at the C-2 position of spheroidene (By similarity). In vitro, can use nonnative substrates and produce oxocarotenoids with a hydroxy and/or a keto group, derived from neurosporene, lycopene, 3,4-didehydrolycopene or 3,4,3',4'-tetradehydrolycopene (PubMed:20851979)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17055\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:33028\"}}],\"reaction\":{\"ecNumber\":\"1.14.15.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17055\",\"source\":\"UniProtKB\"}],\"name\":\"spheroidene + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = spheroiden-2-one + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:33027\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10000\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10001\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33737\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33738\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35330\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:62480\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17055\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:49329\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17055\",\"source\":\"UniProtKB\"}],\"name\":\"spheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2-hydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:49328\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10000\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10001\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33737\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33738\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35330\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91221\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17055\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:49333\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17055\",\"source\":\"UniProtKB\"}],\"name\":\"2-hydroxyspheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:49332\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10000\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10001\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33737\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33738\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91221\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91223\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17055\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:49337\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17055\",\"source\":\"UniProtKB\"}],\"name\":\"2,2-dihydroxyspheroidene = spheroiden-2-one + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:49336\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:62480\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:91223\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0043823\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:spheroidene monooxygenase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/15",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q3J189.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Lee P.C.\",\"Holtzapple E.\",\"Schmidt-Dannert C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"20851979\"},{\"database\":\"DOI\",\"id\":\"10.1128/aem.01606-10\"}],\"citationType\":\"journal article\",\"firstPage\":\"7328\",\"id\":\"20851979\",\"journal\":\"Appl. Environ. Microbiol.\",\"lastPage\":\"7331\",\"publicationDate\":\"2010\",\"title\":\"Novel activity of Rhodobacter sphaeroides spheroidene monooxygenase CrtA expressed in Escherichia coli.\",\"volume\":\"76\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"COFACTOR\",\"SUBSTRATE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:30:46.651114+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bb9e4370b135cf6bb041c348a58e23b19fdc2893ec68a930956c87901797cae8",
  "url": "https://rest.uniprot.org/uniprotkb/Q3J189.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H1",
  "excerpt": "ID   CRTA_CERS4              Reviewed;         324 AA.\nAC   Q3J189; Q54790;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   08-NOV-2005, sequence version 1.\nDT   28-JAN-2026, entry version 74.\nDE   RecName: Full=Spheroidene monooxygenase {ECO:0000303|PubMed:20851979};\nDE            EC=1.14.15.9 {ECO:0000250|UniProtKB:P17055};\nGN   Name=crtA {ECO:0000303|PubMed:7721699};\nGN   OrderedLocusNames=RHOS4_18770 {ECO:0000305};\nGN   ORFNames=RSP_0272 {ECO:0000312|EMBL:ABA79445.1};\nOS   Cereibacter sphaeroides (strain ATCC 17023 / DSM 158 / JCM 6121 / CCUG\nOS   31486 / LMG 2827 / NBRC 12203 / NCIMB 8253 / ATH 2.4.1.) (Rhodobacter\nOS   sphaeroides).\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Alphaproteobacteria;\nOC   Rhodobacterales; Paracoccaceae; Cereibacter.\nOX   NCBI_TaxID=272943;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:CAB38738.1}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA].\nRC   STRAIN=ATCC 17023 / DSM 158 / JCM 6121 / CCUG 31486 / LMG 2827 / NBRC 12203\nRC   / NCIMB 8253 / ATH 2.4.1.;\nRX   PubMed=7721699; DOI=10.1128/jb.177.8.2064-2073.1995;\nRA   Lang H.P., Cogdell R.J., Takaichi S., Hunter C.N.;\nRT   \"Complete DNA sequence, specific Tn5 insertion map, and gene assignment of\nRT   the carotenoid biosynthesis pathway of Rhodobacter sphaeroides.\";\nRL   J. Bacteriol. 177:2064-2073(1995).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-25",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H3",
  "excerpt": "RN   [3]\nRP   FUNCTION, COFACTOR, SUBSTRATE SPECIFICITY, AND BIOTECHNOLOGY.\nRX   PubMed=20851979; DOI=10.1128/aem.01606-10;\nRA   Lee P.C., Holtzapple E., Schmidt-Dannert C.;\nRT   \"Novel activity of Rhodobacter sphaeroides spheroidene monooxygenase CrtA\nRT   expressed in Escherichia coli.\";\nRL   Appl. Environ. Microbiol. 76:7328-7331(2010).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Involved in the biosynthesis of the carotenoid spheroidene\nCC       (By similarity). Catalyzes the introduction of one keto group at the C-\nCC       2 position of spheroidene (By similarity). In vitro, can use nonnative\nCC       substrates and produce oxocarotenoids with a hydroxy and/or a keto\nCC       group, derived from neurosporene, lycopene, 3,4-didehydrolycopene or\nCC       3,4,3',4'-tetradehydrolycopene (PubMed:20851979).\nCC       {ECO:0000250|UniProtKB:P17055, ECO:0000269|PubMed:20851979}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=spheroidene + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+)\nCC         = spheroiden-2-one + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O;\nCC         Xref=Rhea:RHEA:33027, Rhea:RHEA-COMP:10000, Rhea:RHEA-COMP:10001,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:33737, ChEBI:CHEBI:33738, ChEBI:CHEBI:35330,\nCC         ChEBI:CHEBI:62480; EC=1.14.15.9;\nCC         Evidence={ECO:0000250|UniProtKB:P17055};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:33028;\nCC         Evidence={ECO:0000250|UniProtKB:P17055};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=spheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) =\nCC         2-hydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O;\nCC         Xref=Rhea:RHEA:49328, Rhea:RHEA-COMP:10000, Rhea:RHEA-COMP:10001,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:33737, ChEBI:CHEBI:33738, ChEBI:CHEBI:35330,\nCC         ChEBI:CHEBI:91221; Evidence={ECO:0000250|UniProtKB:P17055};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49329;\nCC         Evidence={ECO:0000250|UniProtKB:P17055};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H7",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2-hydroxyspheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 +\nCC         2 H(+) = 2,2-dihydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin]\nCC         + H2O; Xref=Rhea:RHEA:49332, Rhea:RHEA-COMP:10000, Rhea:RHEA-\nCC         COMP:10001, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:15379,\nCC         ChEBI:CHEBI:33737, ChEBI:CHEBI:33738, ChEBI:CHEBI:91221,\nCC         ChEBI:CHEBI:91223; Evidence={ECO:0000250|UniProtKB:P17055};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49333;\nCC         Evidence={ECO:0000250|UniProtKB:P17055};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-76",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H8",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2,2-dihydroxyspheroidene = spheroiden-2-one + H2O;\nCC         Xref=Rhea:RHEA:49336, ChEBI:CHEBI:15377, ChEBI:CHEBI:62480,\nCC         ChEBI:CHEBI:91223; Evidence={ECO:0000250|UniProtKB:P17055};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:49337;\nCC         Evidence={ECO:0000250|UniProtKB:P17055};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 77-82",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H9",
  "excerpt": "DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 110-110",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74)

```json
{
  "entry_version": 74,
  "evidence_id": "H10",
  "excerpt": "DR   GO; GO:0043823; F:spheroidene monooxygenase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:50.636898+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f2d04e35df9019d909d7088f5a01d53d2e955051a5e45ba5642a2108e2735aa3",
  "url": "https://rest.uniprot.org/unisave/Q3J189?format=txt&versions=74"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000977\nname: RNA polymerase II transcription regulatory region sequence-specific DNA binding\nnamespace: molecular_function\nalt_id: GO:0001012\ndef: \"Binding to a specific sequence of DNA that is part of a regulatory region that controls the transcription of a gene or cistron by RNA polymerase II.\" [GOC:txnOH]\ncomment: To minimize ambiguity in the use of the word \"promoter\" in GO, we have chosen the phrase \"transcription regulatory region\" to refer to all of the regulatory regions. Regulatory regions in the DNA which control initiation may include the \"core promoter\" where the basal transcription machinery binds, the \"core promoter proximal region\" where regulatory factors other than the basal machinery bind. There are also additional regulatory regions, in both the DNA and the RNA transcript, which regulate elongation or termination of transcription.\nsynonym: \"RNA polymerase II regulatory region DNA binding\" RELATED []\nis_a: GO:0000976 ! transcription cis-regulatory region binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000977",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 7116-7125",
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
  "excerpt": "[Term]\nid: GO:0003682\nname: chromatin binding\nnamespace: molecular_function\ndef: \"Binding to chromatin, the network of fibers of DNA, protein, and sometimes RNA, that make up the chromosomes of the eukaryotic nucleus during interphase.\" [GOC:jl, ISBN:0198506732, PMID:20404130]\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_yeast\nsynonym: \"lamin/chromatin binding\" NARROW []\nsynonym: \"microtubule/chromatin interaction\" NARROW []\nsynonym: \"nuclear membrane vesicle binding to chromatin\" NARROW []\nis_a: GO:0005488 ! binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003682",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 27850-27864",
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
  "excerpt": "[Term]\nid: GO:0046872\nname: metal ion binding\nnamespace: molecular_function\ndef: \"Binding to a metal ion.\" [GOC:ai]\nsubset: goslim_agr\nsubset: goslim_drosophila\nsubset: goslim_flybase_ribbon\nsubset: goslim_metagenomics\nsynonym: \"heavy metal binding\" NARROW []\nsynonym: \"metal binding\" EXACT []\nis_a: GO:0043169 ! cation binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046872",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 281280-281292",
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
  "excerpt": "[Term]\nid: GO:0047809\nname: D-lactate dehydrogenase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: (R)-lactate + A = AH(2) + pyruvate.\" [RHEA:15089]\nsynonym: \"(R)-2-hydroxy-acid:(acceptor) 2-oxidoreductase activity\" RELATED [EC:1.1.99.6]\nsynonym: \"(R)-lactate dehydrogenase activity\" EXACT []\nsynonym: \"2-hydroxy acid dehydrogenase activity\" RELATED [EC:1.1.99.6]\nsynonym: \"D-2-hydroxy-acid dehydrogenase activity\" BROAD []\nxref: EC:1.1.99.6\nxref: KEGG_REACTION:R00297\nxref: MetaCyc:D-2-HYDROXY-ACID-DEHYDROGENASE-RXN\nxref: RHEA:15089\nxref: RHEA:62968\nis_a: GO:0004457 ! lactate dehydrogenase activity\nis_a: GO:0033719 ! (2R)-oxo-acid reductase activity\nproperty_value: skos:exactMatch EC:1.1.99.6\nproperty_value: skos:exactMatch RHEA:15089\nproperty_value: skos:narrowMatch RHEA:62968\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0047809",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 296518-296537",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 164. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
