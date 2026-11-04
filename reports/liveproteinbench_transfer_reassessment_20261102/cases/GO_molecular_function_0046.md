# GO_molecular_function_0046

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0046.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **B** — pyridoxal phosphate binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATYALSQAHREQMEKSLVDSDPEIAQIMEKEIQRQRESILLIASENVTSRAVFDALGSPMSNKYSEGYPGARYYGGNQHIDAIELTCQARALKAFNLDPEKWGVNVQCLSGSPANLEVYQALMRPHDRLMGLDLPHGGHLSHGYQTPSRKISAVSTYFETFPYRVNTETGIIDYDTLEANAELYRPKCLVAGTSAYCRLIDYGRMRKIADKVGAYLIVDMAHISGLVAAGVIPSPFEYADVVTTTTHKSLRGPRGAMIFFRKGVRSTDPKTGKEIMYDLEGPINFSVFPGHQGGPHNHTITALAVALKQAATPEFRQYQEQVLKNAKALEVEFKALGHKLVSDGTDSHMVLLDLRPKGLDGARVEAVLEQINIACNKNSIPGDKSALTPCGIRIGTPAMTSRGMSEEDFKRVARYIDQVINLCKSIQADLPKEANKLKDFKAKVASGSVPEILALRKEVAEWASTYPLPV

[Multiple Choices]
A. hydrolase activity
B. pyridoxal phosphate binding
C. histone deacetylase activity
D. DNA-binding transcription activator activity, RNA polymerase II-specific
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

> The sequence-matched UniProt record annotates pyridoxal phosphate binding (GO:0030170), with IBA:GO_Central evidence (C8; H6). The record identifies the protein as serine hydroxymethyltransferase and describes its serine–glycine interconversion activity by similarity (C4, C5). This supports B, though the PLP-binding annotation is computationally transferred rather than direct experimental evidence in the supplied excerpts.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 471-aa sequence is consistent with the conserved serine hydroxymethyltransferase family. Knowledge transferable from this enzyme family is that SHMTs are PLP-dependent enzymes, making PLP binding (B) a meaningful choice. Their serine–glycine interconversion is a transferase reaction, not the hydrolase activity in A; C and D describe unrelated activities.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and the conserved cofactor use of SHMTs distinguish B among these choices without needing the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered alternatives, PLP binding is the relevant function for an SHMT-family protein; the other choices do not fit its family or reaction.


### Important caveats

- The reviewer-only annotation supports the key but does not establish direct experimental measurement of PLP binding for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 471-aa sequence is consistent with the conserved serine hydroxymethyltransferase family. Knowledge transferable from this enzyme family is that SHMTs are PLP-dependent enzymes, making PLP binding (B) a meaningful choice. Their serine–glycine interconversion is a transferase reaction, not the hydrolase activity in A; C and D describe unrelated activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the conserved cofactor use of SHMTs distinguish B among these choices without needing the exact protein's database record."
  },
  "case_id": "GO_molecular_function_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates pyridoxal phosphate binding (GO:0030170), with IBA:GO_Central evidence (C8; H6). The record identifies the protein as serine hydroxymethyltransferase and describes its serine–glycine interconversion activity by similarity (C4, C5). This supports B, though the PLP-binding annotation is computationally transferred rather than direct experimental evidence in the supplied excerpts."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but does not establish direct experimental measurement of PLP binding for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, PLP binding is the relevant function for an SHMT-family protein; the other choices do not fit its family or reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates pyridoxal phosphate binding (GO:0030170), with IBA:GO_Central evidence (C8; H6). The record identifies the protein as serine hydroxymethyltransferase and describes its serine–glycine interconversion activity by similarity (C4, C5). This supports B, though the PLP-binding annotation is computationally transferred rather than direct experimental evidence in the supplied excerpts.",
    "evidence_ids": ["C4", "C5", "C8", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 471-aa sequence is consistent with the conserved serine hydroxymethyltransferase family. Knowledge transferable from this enzyme family is that SHMTs are PLP-dependent enzymes, making PLP binding (B) a meaningful choice. Their serine–glycine interconversion is a transferase reaction, not the hydrolase activity in A; C and D describe unrelated activities.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the conserved cofactor use of SHMTs distinguish B among these choices without needing the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, PLP binding is the relevant function for an SHMT-family protein; the other choices do not fit its family or reaction."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but does not establish direct experimental measurement of PLP binding for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is serine hydroxymethyltransferase (SHMT, EC 2.1.2.1), a well-characterized PLP-dependent enzyme. UniProt annotates GO:0030170 (pyridoxal phosphate binding) for this entry via IBA:GO_Central evidence. Among the four offered options, B is the only one that is an actual molecular function of this protein. The protein is a transferase (not a hydrolase, ruling out A), not a histone deacetylase (ruling out C), and not a transcription activator (ruling out D). While the catalytic activity (glycine hydroxymethyltransferase activity, GO:0004372) could be argued as more 'primary,' it is not among the choices, making B the best available answer.

Citations as saved: [C8](#evidence-c8), [H6](#evidence-h6), [C7](#evidence-c7), [H5](#evidence-h5), [C4](#evidence-c4), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the highly conserved 'TTTTHK' motif (in the region 'VVTTTTHKSLRGPRGAMIFFRKGV') and the overall ~471-residue fold-type I architecture characteristic of the serine hydroxymethyltransferase (SHMT) protein family. All known SHMT enzymes across bacteria, fungi, and eukaryotes are obligately PLP-dependent, with the conserved lysine in the TTTTHK motif forming the Schiff base with pyridoxal 5'-phosphate. This is robust family-level knowledge transferable from well-studied SHMT homologs (e.g., E. coli GlyA, human SHMT1/2). A model recognizing SHMT family features would know: (1) SHMT is a transferase (EC 2.1), not a hydrolase → eliminates A; (2) SHMT has no histone-deacetylase structural or mechanistic relationship → eliminates C; (3) SHMT is a cytosolic metabolic enzyme, not a DNA-binding transcription factor → eliminates D. The only remaining option compatible with SHMT family biology is B (pyridoxal phosphate binding).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the SHMT family via the TTTTHK PLP-binding lysine motif and overall fold-type I architecture, combined with the universally conserved PLP-dependence of all SHMT enzymes, provides a concrete transferable inference that meaningfully eliminates options A, C, and D and selects B. This is family-level knowledge learned from other SHMT proteins, not a lookup of this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the four offered choices, only B (pyridoxal phosphate binding) is compatible with SHMT family biology. The protein is a transferase, not a hydrolase (A); it is not a histone deacetylase (C); it is not a transcription factor (D). No other option is defensible.


### Important caveats

- The 'primary molecular function' of SHMT is arguably its catalytic activity (glycine hydroxymethyltransferase activity, GO:0004372), which is not among the options. PLP binding is a supporting cofactor-binding function. However, among the four choices presented, only B applies.
- The GO:0030170 annotation uses IBA:GO_Central (computational inference by phylogenetic propagation), not direct experimental evidence, though PLP-dependence of SHMT is biochemically well-established across the family.
- The reviewer-only evidence confirms the sequence matches Q4WXF4 (GLYC_ASPFU), but this accession was not provided to the evaluated model; the family inference must come from sequence features alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the highly conserved 'TTTTHK' motif (in the region 'VVTTTTHKSLRGPRGAMIFFRKGV') and the overall ~471-residue fold-type I architecture characteristic of the serine hydroxymethyltransferase (SHMT) protein family. All known SHMT enzymes across bacteria, fungi, and eukaryotes are obligately PLP-dependent, with the conserved lysine in the TTTTHK motif forming the Schiff base with pyridoxal 5'-phosphate. This is robust family-level knowledge transferable from well-studied SHMT homologs (e.g., E. coli GlyA, human SHMT1/2). A model recognizing SHMT family features would know: (1) SHMT is a transferase (EC 2.1), not a hydrolase → eliminates A; (2) SHMT has no histone-deacetylase structural or mechanistic relationship → eliminates C; (3) SHMT is a cytosolic metabolic enzyme, not a DNA-binding transcription factor → eliminates D. The only remaining option compatible with SHMT family biology is B (pyridoxal phosphate binding).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the SHMT family via the TTTTHK PLP-binding lysine motif and overall fold-type I architecture, combined with the universally conserved PLP-dependence of all SHMT enzymes, provides a concrete transferable inference that meaningfully eliminates options A, C, and D and selects B. This is family-level knowledge learned from other SHMT proteins, not a lookup of this specific entry's annotation."
  },
  "case_id": "GO_molecular_function_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C8",
      "H6",
      "C7",
      "H5",
      "C4",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The protein is serine hydroxymethyltransferase (SHMT, EC 2.1.2.1), a well-characterized PLP-dependent enzyme. UniProt annotates GO:0030170 (pyridoxal phosphate binding) for this entry via IBA:GO_Central evidence. Among the four offered options, B is the only one that is an actual molecular function of this protein. The protein is a transferase (not a hydrolase, ruling out A), not a histone deacetylase (ruling out C), and not a transcription activator (ruling out D). While the catalytic activity (glycine hydroxymethyltransferase activity, GO:0004372) could be argued as more 'primary,' it is not among the choices, making B the best available answer."
  },
  "important_caveats": [
    "The 'primary molecular function' of SHMT is arguably its catalytic activity (glycine hydroxymethyltransferase activity, GO:0004372), which is not among the options. PLP binding is a supporting cofactor-binding function. However, among the four choices presented, only B applies.",
    "The GO:0030170 annotation uses IBA:GO_Central (computational inference by phylogenetic propagation), not direct experimental evidence, though PLP-dependence of SHMT is biochemically well-established across the family.",
    "The reviewer-only evidence confirms the sequence matches Q4WXF4 (GLYC_ASPFU), but this accession was not provided to the evaluated model; the family inference must come from sequence features alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only B (pyridoxal phosphate binding) is compatible with SHMT family biology. The protein is a transferase, not a hydrolase (A); it is not a histone deacetylase (C); it is not a transcription factor (D). No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is serine hydroxymethyltransferase (SHMT, EC 2.1.2.1), a well-characterized PLP-dependent enzyme. UniProt annotates GO:0030170 (pyridoxal phosphate binding) for this entry via IBA:GO_Central evidence. Among the four offered options, B is the only one that is an actual molecular function of this protein. The protein is a transferase (not a hydrolase, ruling out A), not a histone deacetylase (ruling out C), and not a transcription activator (ruling out D). While the catalytic activity (glycine hydroxymethyltransferase activity, GO:0004372) could be argued as more 'primary,' it is not among the choices, making B the best available answer.",
    "evidence_ids": ["C8", "H6", "C7", "H5", "C4", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the highly conserved 'TTTTHK' motif (in the region 'VVTTTTHKSLRGPRGAMIFFRKGV') and the overall ~471-residue fold-type I architecture characteristic of the serine hydroxymethyltransferase (SHMT) protein family. All known SHMT enzymes across bacteria, fungi, and eukaryotes are obligately PLP-dependent, with the conserved lysine in the TTTTHK motif forming the Schiff base with pyridoxal 5'-phosphate. This is robust family-level knowledge transferable from well-studied SHMT homologs (e.g., E. coli GlyA, human SHMT1/2). A model recognizing SHMT family features would know: (1) SHMT is a transferase (EC 2.1), not a hydrolase → eliminates A; (2) SHMT has no histone-deacetylase structural or mechanistic relationship → eliminates C; (3) SHMT is a cytosolic metabolic enzyme, not a DNA-binding transcription factor → eliminates D. The only remaining option compatible with SHMT family biology is B (pyridoxal phosphate binding).",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the SHMT family via the TTTTHK PLP-binding lysine motif and overall fold-type I architecture, combined with the universally conserved PLP-dependence of all SHMT enzymes, provides a concrete transferable inference that meaningfully eliminates options A, C, and D and selects B. This is family-level knowledge learned from other SHMT proteins, not a lookup of this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the four offered choices, only B (pyridoxal phosphate binding) is compatible with SHMT family biology. The protein is a transferase, not a hydrolase (A); it is not a histone deacetylase (C); it is not a transcription factor (D). No other option is defensible."
  },
  "important_caveats": [
    "The 'primary molecular function' of SHMT is arguably its catalytic activity (glycine hydroxymethyltransferase activity, GO:0004372), which is not among the options. PLP binding is a supporting cofactor-binding function. However, among the four choices presented, only B applies.",
    "The GO:0030170 annotation uses IBA:GO_Central (computational inference by phylogenetic propagation), not direct experimental evidence, though PLP-dependence of SHMT is biochemically well-established across the family.",
    "The reviewer-only evidence confirms the sequence matches Q4WXF4 (GLYC_ASPFU), but this accession was not provided to the evaluated model; the family inference must come from sequence features alone."
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
  "benchmark_sequence_length": 471,
  "benchmark_sequence_sha256": "f701b7b612f66565fce8586e5acff753094d2b7e38617cd4fba5d0a2faa13b4f",
  "current_entry_audit": {
    "entryVersion": 124,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2005-07-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 471,
  "current_source_sequence_sha256": "f701b7b612f66565fce8586e5acff753094d2b7e38617cd4fba5d0a2faa13b4f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 122,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q4WXF4",
  "selected_historical_entry_version": 122,
  "selected_historical_record_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "selected_historical_source_sequence_length": 471,
  "selected_historical_source_sequence_sha256": "f701b7b612f66565fce8586e5acff753094d2b7e38617cd4fba5d0a2faa13b4f",
  "selected_historical_version": {
    "accession": "Q4WXF4",
    "database": "Swiss-Prot",
    "entryVersion": 122,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GLYC_ASPFU",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q4WXF4\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":124,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2005-07-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Neosartorya fumigata\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Aspergillus\",\"Fumigati\"],\"scientificName\":\"Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 / Af293)\",\"taxonId\":330879}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P34896\",\"source\":\"UniProtKB\"}],\"value\":\"2.1.2.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39825596\",\"source\":\"PubMed\"}],\"value\":\"Serine hydroxymethyltransferase, cytosolic\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P34896\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39825596\",\"source\":\"PubMed\"}],\"value\":\"Catalyzes the interconversion of serine and glycine (By similarity). Essential for viability and required for virulence in a murine model of established pulmonary infection (PubMed:39825596)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.1.2.1\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P34896\",\"source\":\"UniProtKB\"}],\"name\":\"(6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:15481\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15636\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33384\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57305\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57453\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0004372\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:glycine hydroxymethyltransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"ISS:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/19",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0030170\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:pyridoxal phosphate binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/20",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q4WXF4.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Alharthi R.\",\"Sueiro-Olivares M.\",\"Storer I.\",\"Bin Shuraym H.\",\"Scott J.\",\"Al-Shidhani R.\",\"Fortune-Grant R.\",\"Bignell E.\",\"Tabernero L.\",\"Bromley M.\",\"Zhao C.\",\"Amich J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39825596\"},{\"database\":\"DOI\",\"id\":\"10.1080/21505594.2024.2449075\"}],\"citationType\":\"journal article\",\"firstPage\":\"2449075\",\"id\":\"39825596\",\"journal\":\"Virulence\",\"lastPage\":\"2449075\",\"publicationDate\":\"2025\",\"title\":\"The sulfur-related metabolic status of Aspergillus fumigatus during infection reveals cytosolic serine hydroxymethyltransferase as a promising antifungal target.\",\"volume\":\"16\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"SUBCELLULAR LOCATION\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:30:56.546837+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "58c0e8a11da085febbdf3005ab56b79d104ea1a48cbcd1855ec692b54ad939c6",
  "url": "https://rest.uniprot.org/uniprotkb/Q4WXF4.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H1",
  "excerpt": "ID   GLYC_ASPFU              Reviewed;         471 AA.\nAC   Q4WXF4;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUL-2005, sequence version 1.\nDT   28-JAN-2026, entry version 122.\nDE   RecName: Full=Serine hydroxymethyltransferase, cytosolic {ECO:0000303|PubMed:39825596};\nDE            EC=2.1.2.1 {ECO:0000250|UniProtKB:P34896};\nGN   Name=shmB {ECO:0000303|PubMed:39825596}; ORFNames=AFUA_3G09320;\nOS   Aspergillus fumigatus (strain ATCC MYA-4609 / CBS 101355 / FGSC A1100 /\nOS   Af293) (Neosartorya fumigata).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Aspergillus;\nOC   Aspergillus subgen. Fumigati.\nOX   NCBI_TaxID=330879;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.835030+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "url": "https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, SUBCELLULAR LOCATION, INDUCTION, DISRUPTION PHENOTYPE, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=39825596; DOI=10.1080/21505594.2024.2449075;\nRA   Alharthi R., Sueiro-Olivares M., Storer I., Bin Shuraym H., Scott J.,\nRA   Al-Shidhani R., Fortune-Grant R., Bignell E., Tabernero L., Bromley M.,\nRA   Zhao C., Amich J.;\nRT   \"The sulfur-related metabolic status of Aspergillus fumigatus during\nRT   infection reveals cytosolic serine hydroxymethyltransferase as a promising\nRT   antifungal target.\";\nRL   Virulence 16:2449075-2449075(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.835030+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "url": "https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Catalyzes the interconversion of serine and glycine (By\nCC       similarity). Essential for viability and required for virulence in a\nCC       murine model of established pulmonary infection (PubMed:39825596).\nCC       {ECO:0000250|UniProtKB:P34896, ECO:0000269|PubMed:39825596}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.835030+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "url": "https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O =\nCC         (6S)-5,6,7,8-tetrahydrofolate + L-serine; Xref=Rhea:RHEA:15481,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15636, ChEBI:CHEBI:33384,\nCC         ChEBI:CHEBI:57305, ChEBI:CHEBI:57453; EC=2.1.2.1;\nCC         Evidence={ECO:0000250|UniProtKB:P34896};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.835030+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "url": "https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0004372; F:glycine hydroxymethyltransferase activity; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.835030+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 100-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "url": "https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122)

```json
{
  "entry_version": 122,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0030170; F:pyridoxal phosphate binding; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:31:00.835030+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-101",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "86dc299bb08ad4eed40a64d75bf36be229472b86dc3076c4f22bd2ef05466eec",
  "url": "https://rest.uniprot.org/unisave/Q4WXF4?format=txt&versions=122"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0001228\nname: DNA-binding transcription activator activity, RNA polymerase II-specific\nnamespace: molecular_function\nalt_id: GO:0001077\nalt_id: GO:0001205\nalt_id: GO:0001209\nalt_id: GO:0001211\nalt_id: GO:0001212\nalt_id: GO:0001213\ndef: \"A DNA-binding transcription factor activity that activates or increases transcription of specific gene sets transcribed by RNA polymerase II.\" [GOC:aruk, GOC:txnOH-2018, PMID:20737563, PMID:27145859]\ncomment: For usage guidance, see comment in GO:0003700 ; DNA-binding transcription factor activity.\nsynonym: \"copper ion regulated core promoter proximal region sequence-specific DNA binding RNA polymerase II transcription factor activity involved in positive regulation of transcription\" NARROW []\nsynonym: \"distal enhancer DNA-binding transcription activator activity, RNA polymerase II-specific\" NARROW []\nsynonym: \"metal ion regulated core promoter proximal region sequence-specific DNA binding RNA polymerase II transcription factor activity involved in positive regulation of transcription\" NARROW []\nsynonym: \"metal ion regulated sequence-specific DNA binding transcription factor activity involved in positive regulation of transcription\" NARROW []\nsynonym: \"proximal promoter DNA-binding transcription activator activity, RNA polymerase II-specific\" NARROW []\nsynonym: \"RNA polymerase II core promoter proximal region sequence-specific DNA binding transcription factor activity involved in positive regulation of transcription\" NARROW []\nsynonym: \"RNA polymerase II distal enhancer sequence-specific DNA-binding transcription factor activity involved in positive regulation of transcription\" NARROW []\nsynonym: \"RNA polymerase II transcription regulatory region sequence-specific DNA binding transcription factor activity involved in positive regulation of transcription\" EXACT []\nsynonym: \"RNA polymerase II transcriptional activator activity, copper ion regulated proximal promoter sequence-specific DNA binding\" NARROW []\nsynonym: \"RNA polymerase II transcriptional activator activity, metal ion regulated core promoter proximal region sequence-specific binding\" NARROW []\nsynonym: \"RNA polymerase II transcriptional activator activity, metal ion regulated proximal promoter sequence-specific DNA binding\" NARROW []\nsynonym: \"RNA polymerase II transcriptional activator activity, zinc ion regulated core promoter proximal region sequence-specific binding\" NARROW []\nsynonym: \"RNA polymerase II transcriptional activator activity, zinc ion regulated proximal promoter sequence-specific DNA binding\" NARROW []\nsynonym: \"sequence-specific distal enhancer binding RNA polymerase II transcription factor activity involved in positive regulation of transcription\" NARROW []\nsynonym: \"transcriptional activator activity, metal ion regulated sequence-specific DNA binding\" NARROW []\nsynonym: \"transcriptional activator activity, RNA polymerase II core promoter proximal region sequence-specific binding\" NARROW []\nsynonym: \"transcriptional activator activity, RNA polymerase II distal enhancer sequence-specific DNA binding\" NARROW []\nsynonym: \"transcriptional activator activity, RNA polymerase II proximal promoter sequence-specific DNA binding\" NARROW []\nsynonym: \"transcriptional activator activity, RNA polymerase II transcription regulatory region sequence-specific DNA binding\" EXACT []\nsynonym: \"zinc ion regulated core promoter proximal region sequence-specific DNA binding RNA polymerase II transcription factor activity involved in positive regulation of transcription\" NARROW []\nxref: Reactome:R-HSA-8937177 \"AHR:TCDD binds ARNT\"\nxref: Reactome:R-HSA-9856539 \"MLXIPL:MLX binds PKLR gene promoter\"\nxref: Reactome:R-HSA-9856546 \"MLXIPL:MLX binds FASN gene promoter\"\nxref: Reactome:R-HSA-9856548 \"MLXIPL:MLX binds ACACB gene promoter\"\nxref: Reactome:R-HSA-9856549 \"MLXIPL:MLX binds ACLY gene promoter\"\nxref: Reactome:R-HSA-9856550 \"MLXIPL:MLX binds ACACA gene promoter\"\nxref: Reactome:R-HSA-9856604 \"MLXIPL:MLX binds AGPAT1 gene promoter\"\nis_a: GO:0000981 ! DNA-binding transcription factor activity, RNA polymerase II-specific\nis_a: GO:0001216 ! DNA-binding transcription activator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0001228",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 8656-8697",
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
  "excerpt": "[Term]\nid: GO:0004407\nname: histone deacetylase activity\nnamespace: molecular_function\ndef: \"Removal of an acetyl group from a lysine residue in a histone.\" [PMID:24691964, PMID:9893272]\ncomment: Histone deacytylase (HDAC) enzymes are divided into four classes: the Class I Rpd3-like proteins (in human: HDAC1, HDAC2, HDAC3, and HDAC8); the Class II Hda1-like proteins (in human: HDAC4, HDAC5, HDAC6, HDAC7, HDAC9, and HDAC10); the Class III Sir2-like proteins (in human: SIRT1, SIRT2, SIRT3, SIRT4, SIRT5, SIRT6, and SIRT7); and the Class IV protein (HDAC11 in human). Except for Class III enzymes, the mechanism is a metal-dependent hydrolysis of the acetylated substrate. The Class III HDACs use NAD+ as a reactant to deacetylate acetyl lysine residues of protein substrates forming nicotinamide, the deacetylated product, and the metabolite 2'-O-acetyl-ADP-ribose. Therefore, Class III are classified as transferases (EC:2) and others are hydrolases (EC:3).\nsynonym: \"histone deacetylase activity (NAD-independent)\" EXACT []\nxref: Reactome:R-HSA-2545203 \"Deacetylation of cleaved cohesin\"\nxref: Reactome:R-HSA-2545253 \"Deacetylation of cohesin\"\nxref: Reactome:R-HSA-3769447 \"HDAC1:2-containing complex deacetylate histones\"\nxref: Reactome:R-HSA-3777129 \"HDAC3 containing complexes deacetylate histone\"\nxref: Reactome:R-HSA-3782637 \"HDAC8 deacetylates histones\"\nxref: Reactome:R-HSA-3782655 \"HDAC10 deacetylates histone\"\nxref: Reactome:R-HSA-427514 \"eNoSC deacetylates histone H3\"\nxref: Reactome:R-HSA-433672 \"NoRC:HDAC:DNMT deacetylates histone H4 and methylates histone H3\"\nxref: Reactome:R-HSA-6805650 \"MTA2-NuRD complex deacetylates TP53\"\nis_a: GO:0033558 ! protein lysine deacetylase activity\nis_a: GO:0140993 ! histone modifying activity\nproperty_value: skos:broadMatch EC:2.3.1.-\nproperty_value: skos:broadMatch EC:3.5.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004407",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 41440-41460",
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
  "excerpt": "[Term]\nid: GO:0016787\nname: hydrolase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of various bonds, e.g. C-O, C-N, C-C, phosphoric anhydride bonds, etc.\" [ISBN:0198506732]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_prokaryote\nsubset: goslim_yeast\nxref: EC:3.-.-.-\nxref: Reactome:R-HSA-1236938 \"Partial proteolysis of antigen in phagolysosomes\"\nxref: Reactome:R-HSA-2029475 \"Production of AA by iPLA2 upon FCGR activation\"\nxref: Reactome:R-HSA-5694583 \"ABHD4 hydrolyses NAPE\"\nxref: Reactome:R-HSA-5695964 \"ABHD14B hydrolyses PNPB\"\nxref: Reactome:R-HSA-6786190 \"CMBL hydrolyses OM to OLMS\"\nxref: Reactome:R-HSA-6788295 \"HDHD1:Mg2+ dephosphorylates PURIDP\"\nxref: Reactome:R-HSA-8938314 \"ENPPs hydrolyse CoA-SH to PPANT, PAP\"\nxref: Reactome:R-HSA-8952137 \"Phospholipid phosphatase 6 hydrolyses Presqualene diphosphate to presqualene monophosphate\"\nxref: Reactome:R-HSA-9942295 \"QNG1 hydrolyzes queuosine 5'-monophosphate yielding queuine and ribose 5'-monophosphate\"\nis_a: GO:0003824 ! catalytic activity\nproperty_value: skos:exactMatch EC:3.-.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016787",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 130166-130193",
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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 46. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
