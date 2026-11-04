# GO_molecular_function_0026

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0026.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — alpha-1,6-mannosyltransferase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MWSLDPSQKEVLRFAVSCRILTLMLQALFNIIIPDHHADAFSPPRLASSCSVDQLVEGLLGGLSRWDAEHFLFIAEHGYLYEHNFAFFPGFPLALLMGTELLRPLQGLLSQRSCLLVSVALLNFLFSVLAAVTLHDLGCLVLGCPRQAFYAAMLFCLSPANVFLAAGYSEALFAFLTFSAMGQLERGRSWASGLLFALATGVRSNGLVSVGFLLHAQCRGFFSSLVVLNPLKPLFKLMASLCLSVLTVSLPFALFQYYAYTQFCLPGSAHSVPEPLVQLAVDKGYRITGGNEPPWCSWGLPLVYSYIQDVYWNVGFLRYYELRQVPNFLLATPVAVLVVWAAWTYVTTHPWLCLTLGLRRSKDSKKTLEKPHPGFLSPKVFVYLVHAAGLLLFGSLCMHVQVLTRLLCSSTPVVYWFPAHLLQNQEPLLRSVDTVPEKLLEKNSPPGQKAPRNCIMKLLYNWRACSPVTRCILGYFLTYWLLGLLLHCNFLPWT

[Multiple Choices]
A. 4 iron, 4 sulfur cluster binding
B. Hsp90 protein binding
C. NADPH dehydrogenase (quinone) activity
D. alpha-1,6-mannosyltransferase activity
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

> The sequence-matched UniProt records describe alpha-1,6-mannosyltransferase activity and a catalytic reaction transferring mannose to a GPI precursor. The catalytic activity is linked to experimental evidence (ECO:0000269); the separate GO annotation is computationally assigned.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is strongly hydrophobic and consistent with a multipass membrane protein. Together with transferable knowledge of membrane-embedded GPI mannosyltransferases and their homologs, this favors D, a glycosyltransferase activity, over the iron-sulfur-cluster binding, Hsp90-binding, and NADPH-dehydrogenase alternatives. This is a family-level, probabilistic inference rather than proof of the exact substrate or linkage.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and choices support a meaningful family/topology-based distinction without requiring the target's database annotation or experimental measurement.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the only offered choice consistent with the sequence-based membrane-protein and glycosyltransferase inference; the other options describe distinct activities.


### Important caveats

- The sequence's hydrophobicity alone does not establish alpha-1,6 linkage specificity; that finer functional claim is supported by reviewer-only experimental annotation.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multipass membrane protein. Together with transferable knowledge of membrane-embedded GPI mannosyltransferases and their homologs, this favors D, a glycosyltransferase activity, over the iron-sulfur-cluster binding, Hsp90-binding, and NADPH-dehydrogenase alternatives. This is a family-level, probabilistic inference rather than proof of the exact substrate or linkage.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices support a meaningful family/topology-based distinction without requiring the target's database annotation or experimental measurement."
  },
  "case_id": "GO_molecular_function_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records describe alpha-1,6-mannosyltransferase activity and a catalytic reaction transferring mannose to a GPI precursor. The catalytic activity is linked to experimental evidence (ECO:0000269); the separate GO annotation is computationally assigned."
  },
  "important_caveats": [
    "The sequence's hydrophobicity alone does not establish alpha-1,6 linkage specificity; that finer functional claim is supported by reviewer-only experimental annotation."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered choice consistent with the sequence-based membrane-protein and glycosyltransferase inference; the other options describe distinct activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt records describe alpha-1,6-mannosyltransferase activity and a catalytic reaction transferring mannose to a GPI precursor. The catalytic activity is linked to experimental evidence (ECO:0000269); the separate GO annotation is computationally assigned.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multipass membrane protein. Together with transferable knowledge of membrane-embedded GPI mannosyltransferases and their homologs, this favors D, a glycosyltransferase activity, over the iron-sulfur-cluster binding, Hsp90-binding, and NADPH-dehydrogenase alternatives. This is a family-level, probabilistic inference rather than proof of the exact substrate or linkage.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices support a meaningful family/topology-based distinction without requiring the target's database annotation or experimental measurement."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered choice consistent with the sequence-based membrane-protein and glycosyltransferase inference; the other options describe distinct activities."
  },
  "important_caveats": [
    "The sequence's hydrophobicity alone does not establish alpha-1,6 linkage specificity; that finer functional claim is supported by reviewer-only experimental annotation."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A8C2M425) explicitly annotates the protein as 'GPI alpha-1,6-mannosyltransferase 2' (EC 2.4.1.-) with experimental evidence (PubMed:23694781) for its function as an alpha-1,6-mannosyltransferase catalyzing transfer of mannose via an alpha-1,6 bond in GPI-anchor biosynthesis. GO:0000009 (alpha-1,6-mannosyltransferase activity) is annotated, and the more specific GO:0120563 (dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity) is is_a GO:0000009. The expected answer D matches the annotated molecular function.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C8](#evidence-c8), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H6](#evidence-h6), [H7](#evidence-h7), [GO1](#evidence-go1), [GO5](#evidence-go5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 494-aa sequence is dominated by long hydrophobic stretches forming approximately 8-10 transmembrane helices, characteristic of a multi-pass ER membrane protein. Among the four options, only alpha-1,6-mannosyltransferase activity (D) is consistent with a multi-pass membrane glycosyltransferase: GPI mannosyltransferases (PIGV, PIGB, PIGW family) are well-known multi-pass membrane proteins embedded in the ER membrane. In contrast: (A) 4Fe-4S cluster binding proteins are typically soluble and contain specific Cys-rich motifs (e.g., CxxCxxCxxC arrangements) absent here; (B) Hsp90 protein binding involves TPR domains or specific peptide motifs not present in this sequence; (C) NADPH dehydrogenase (quinone) activity requires a Rossmann fold (GxGxxG motif) and is typically soluble. The multi-pass membrane topology alone strongly discriminates D from A, B, and C, which are incompatible with the observed sequence architecture. Additionally, the PIGV/GPI-MT-II family is well-characterized across organisms (human Q9NUD9 is the reference), and its multi-pass membrane architecture is a transferable family-level feature.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use the clearly multi-pass transmembrane architecture of the sequence to eliminate the three soluble-protein options (A, B, C) and select the membrane-embedded glycosyltransferase option (D). This relies on general principles: glycosyltransferases in the GPI pathway are membrane proteins, while iron-sulfur cluster binders, Hsp90 interactors, and NADPH dehydrogenases are typically soluble. Family-level knowledge of GPI mannosyltransferases as multi-pass membrane proteins is transferable across organisms.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different protein classes with distinct structural requirements. The multi-pass membrane topology of the sequence uniquely matches a glycosyltransferase among the given choices. No other option is compatible with the observed sequence architecture.


### Important caveats

- The GO annotation for GO:0000009 on this entry is IEA:Ensembl (computational), while the experimental evidence (ECO:0000269, PubMed:23694781) supports the specific GPI mannosyltransferase II activity (GO:0120563), which is_a GO:0000009.
- The sequence is from Cricetulus griseus (Chinese hamster), a homolog of human PIGV (Q9NUD9). The reviewer-only evidence confirms this identity, but the model only sees the sequence.
- The option D uses the general term 'alpha-1,6-mannosyltransferase activity' (GO:0000009) rather than the more specific GPI-specific term (GO:0120563), which is a valid parent term.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 494-aa sequence is dominated by long hydrophobic stretches forming approximately 8-10 transmembrane helices, characteristic of a multi-pass ER membrane protein. Among the four options, only alpha-1,6-mannosyltransferase activity (D) is consistent with a multi-pass membrane glycosyltransferase: GPI mannosyltransferases (PIGV, PIGB, PIGW family) are well-known multi-pass membrane proteins embedded in the ER membrane. In contrast: (A) 4Fe-4S cluster binding proteins are typically soluble and contain specific Cys-rich motifs (e.g., CxxCxxCxxC arrangements) absent here; (B) Hsp90 protein binding involves TPR domains or specific peptide motifs not present in this sequence; (C) NADPH dehydrogenase (quinone) activity requires a Rossmann fold (GxGxxG motif) and is typically soluble. The multi-pass membrane topology alone strongly discriminates D from A, B, and C, which are incompatible with the observed sequence architecture. Additionally, the PIGV/GPI-MT-II family is well-characterized across organisms (human Q9NUD9 is the reference), and its multi-pass membrane architecture is a transferable family-level feature.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the clearly multi-pass transmembrane architecture of the sequence to eliminate the three soluble-protein options (A, B, C) and select the membrane-embedded glycosyltransferase option (D). This relies on general principles: glycosyltransferases in the GPI pathway are membrane proteins, while iron-sulfur cluster binders, Hsp90 interactors, and NADPH dehydrogenases are typically soluble. Family-level knowledge of GPI mannosyltransferases as multi-pass membrane proteins is transferable across organisms."
  },
  "case_id": "GO_molecular_function_0026",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C8",
      "H1",
      "H3",
      "H4",
      "H6",
      "H7",
      "GO1",
      "GO5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A8C2M425) explicitly annotates the protein as 'GPI alpha-1,6-mannosyltransferase 2' (EC 2.4.1.-) with experimental evidence (PubMed:23694781) for its function as an alpha-1,6-mannosyltransferase catalyzing transfer of mannose via an alpha-1,6 bond in GPI-anchor biosynthesis. GO:0000009 (alpha-1,6-mannosyltransferase activity) is annotated, and the more specific GO:0120563 (dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity) is is_a GO:0000009. The expected answer D matches the annotated molecular function."
  },
  "important_caveats": [
    "The GO annotation for GO:0000009 on this entry is IEA:Ensembl (computational), while the experimental evidence (ECO:0000269, PubMed:23694781) supports the specific GPI mannosyltransferase II activity (GO:0120563), which is_a GO:0000009.",
    "The sequence is from Cricetulus griseus (Chinese hamster), a homolog of human PIGV (Q9NUD9). The reviewer-only evidence confirms this identity, but the model only sees the sequence.",
    "The option D uses the general term 'alpha-1,6-mannosyltransferase activity' (GO:0000009) rather than the more specific GPI-specific term (GO:0120563), which is a valid parent term."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different protein classes with distinct structural requirements. The multi-pass membrane topology of the sequence uniquely matches a glycosyltransferase among the given choices. No other option is compatible with the observed sequence architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0026",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A8C2M425) explicitly annotates the protein as 'GPI alpha-1,6-mannosyltransferase 2' (EC 2.4.1.-) with experimental evidence (PubMed:23694781) for its function as an alpha-1,6-mannosyltransferase catalyzing transfer of mannose via an alpha-1,6 bond in GPI-anchor biosynthesis. GO:0000009 (alpha-1,6-mannosyltransferase activity) is annotated, and the more specific GO:0120563 (dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity) is is_a GO:0000009. The expected answer D matches the annotated molecular function.",
    "evidence_ids": ["C4", "C5", "C6", "C8", "H1", "H3", "H4", "H6", "H7", "GO1", "GO5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 494-aa sequence is dominated by long hydrophobic stretches forming approximately 8-10 transmembrane helices, characteristic of a multi-pass ER membrane protein. Among the four options, only alpha-1,6-mannosyltransferase activity (D) is consistent with a multi-pass membrane glycosyltransferase: GPI mannosyltransferases (PIGV, PIGB, PIGW family) are well-known multi-pass membrane proteins embedded in the ER membrane. In contrast: (A) 4Fe-4S cluster binding proteins are typically soluble and contain specific Cys-rich motifs (e.g., CxxCxxCxxC arrangements) absent here; (B) Hsp90 protein binding involves TPR domains or specific peptide motifs not present in this sequence; (C) NADPH dehydrogenase (quinone) activity requires a Rossmann fold (GxGxxG motif) and is typically soluble. The multi-pass membrane topology alone strongly discriminates D from A, B, and C, which are incompatible with the observed sequence architecture. Additionally, the PIGV/GPI-MT-II family is well-characterized across organisms (human Q9NUD9 is the reference), and its multi-pass membrane architecture is a transferable family-level feature.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use the clearly multi-pass transmembrane architecture of the sequence to eliminate the three soluble-protein options (A, B, C) and select the membrane-embedded glycosyltransferase option (D). This relies on general principles: glycosyltransferases in the GPI pathway are membrane proteins, while iron-sulfur cluster binders, Hsp90 interactors, and NADPH dehydrogenases are typically soluble. Family-level knowledge of GPI mannosyltransferases as multi-pass membrane proteins is transferable across organisms."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different protein classes with distinct structural requirements. The multi-pass membrane topology of the sequence uniquely matches a glycosyltransferase among the given choices. No other option is compatible with the observed sequence architecture."
  },
  "important_caveats": [
    "The GO annotation for GO:0000009 on this entry is IEA:Ensembl (computational), while the experimental evidence (ECO:0000269, PubMed:23694781) supports the specific GPI mannosyltransferase II activity (GO:0120563), which is_a GO:0000009.",
    "The sequence is from Cricetulus griseus (Chinese hamster), a homolog of human PIGV (Q9NUD9). The reviewer-only evidence confirms this identity, but the model only sees the sequence.",
    "The option D uses the general term 'alpha-1,6-mannosyltransferase activity' (GO:0000009) rather than the more specific GPI-specific term (GO:0120563), which is a valid parent term."
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
  "benchmark_sequence_length": 494,
  "benchmark_sequence_sha256": "9d3f46ba22c4115b7a8c603ef5a943e2972a8c829daba3e4cf44f5137f9c98a1",
  "current_entry_audit": {
    "entryVersion": 21,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2022-01-19",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 494,
  "current_source_sequence_sha256": "9d3f46ba22c4115b7a8c603ef5a943e2972a8c829daba3e4cf44f5137f9c98a1",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 19,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A8C2M425",
  "selected_historical_entry_version": 19,
  "selected_historical_record_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "selected_historical_source_sequence_length": 494,
  "selected_historical_source_sequence_sha256": "9d3f46ba22c4115b7a8c603ef5a943e2972a8c829daba3e4cf44f5137f9c98a1",
  "selected_historical_version": {
    "accession": "A0A8C2M425",
    "database": "Swiss-Prot",
    "entryVersion": 19,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "PIGV_CRIGR",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A8C2M425\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":21,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2022-01-19\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Chinese hamster\",\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Chordata\",\"Craniata\",\"Vertebrata\",\"Euteleostomi\",\"Mammalia\",\"Eutheria\",\"Euarchontoglires\",\"Glires\",\"Rodentia\",\"Myomorpha\",\"Muroidea\",\"Cricetidae\",\"Cricetinae\",\"Cricetulus\"],\"scientificName\":\"Cricetulus griseus\",\"synonyms\":[\"Cricetulus barabensis griseus\"],\"taxonId\":10029}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"GPI mannosyltransferase II\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"GPI-MT-II\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"Phosphatidylinositol-glycan biosynthesis class V protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"PIG-V\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q9NUD9\",\"source\":\"UniProtKB\"}],\"value\":\"GPI alpha-1,6-mannosyltransferase 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23694781\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"value\":\"Alpha-1,6-mannosyltransferase that catalyzes the transfer of the second mannose, via an alpha-1,6 bond, from a dolichol-phosphate-mannose (Dol-P-Man) to a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H2) intermediate to generate a 2-acyl-6-[alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H3) and participates in the seventh step of the glycosylphosphatidylinositol-anchor biosynthesis (PubMed:23694781). May also transfer the second mannose on a 2-acyl-6-[2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol (also termed H5), but less effectively (Probable)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:60489\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"name\":\"a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = a 2-acyl-6-[alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:60488\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19498\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19501\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57683\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58211\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:143818\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:144028\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:60993\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"23694781\",\"source\":\"PubMed\"}],\"name\":\"a 2-acyl-6-[2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = a 2-acyl-6-[alpha-D-mannosyl-(1->6)-2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:60992\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19498\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:19501\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57683\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58211\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:144036\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:144054\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0120563\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:Ensembl\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/20",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A8C2M425.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Hirata T.\",\"Fujita M.\",\"Kanzawa N.\",\"Murakami Y.\",\"Maeda Y.\",\"Kinoshita T.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"23694781\"},{\"database\":\"DOI\",\"id\":\"10.1093/jb/mvt045\"}],\"citationType\":\"journal article\",\"firstPage\":\"257\",\"id\":\"23694781\",\"journal\":\"J. Biochem.\",\"lastPage\":\"264\",\"publicationDate\":\"2013\",\"title\":\"Glycosylphosphatidylinositol mannosyltransferase II is the rate-limiting enzyme in glycosylphosphatidylinositol biosynthesis under limited dolichol-phosphate mannose availability.\",\"volume\":\"154\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:57.236271+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4ac1d4befce2ad1aed32c8b789b20db35cf03975e9e81d35460677c7af7b77aa",
  "url": "https://rest.uniprot.org/uniprotkb/A0A8C2M425.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H1",
  "excerpt": "ID   PIGV_CRIGR              Reviewed;         494 AA.\nAC   A0A8C2M425;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   19-JAN-2022, sequence version 1.\nDT   28-JAN-2026, entry version 19.\nDE   RecName: Full=GPI alpha-1,6-mannosyltransferase 2 {ECO:0000250|UniProtKB:Q9NUD9};\nDE            EC=2.4.1.- {ECO:0000269|PubMed:23694781};\nDE   AltName: Full=GPI mannosyltransferase II;\nDE            Short=GPI-MT-II {ECO:0000250|UniProtKB:Q9NUD9};\nDE   AltName: Full=Phosphatidylinositol-glycan biosynthesis class V protein {ECO:0000250|UniProtKB:Q9NUD9};\nDE            Short=PIG-V {ECO:0000250|UniProtKB:Q9NUD9};\nGN   Name=PIGV {ECO:0000303|PubMed:23694781};\nOS   Cricetulus griseus (Chinese hamster) (Cricetulus barabensis griseus).\nOC   Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi; Mammalia;\nOC   Eutheria; Euarchontoglires; Glires; Rodentia; Myomorpha; Muroidea;\nOC   Cricetidae; Cricetinae; Cricetulus.\nOX   NCBI_TaxID=10029;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRX   PubMed=23694781; DOI=10.1093/jb/mvt045;\nRA   Hirata T., Fujita M., Kanzawa N., Murakami Y., Maeda Y., Kinoshita T.;\nRT   \"Glycosylphosphatidylinositol mannosyltransferase II is the rate-limiting\nRT   enzyme in glycosylphosphatidylinositol biosynthesis under limited dolichol-\nRT   phosphate mannose availability.\";\nRL   J. Biochem. 154:257-264(2013).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Alpha-1,6-mannosyltransferase that catalyzes the transfer of\nCC       the second mannose, via an alpha-1,6 bond, from a dolichol-phosphate-\nCC       mannose (Dol-P-Man) to a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-\nCC       glucosaminyl)-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol\nCC       (also termed H2) intermediate to generate a 2-acyl-6-[alpha-D-mannosyl-\nCC       (1->6)-alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-\nCC       sn-glycero-3-phospho)-1D-myo-inositol (also termed H3) and participates\nCC       in the seventh step of the glycosylphosphatidylinositol-anchor\nCC       biosynthesis (PubMed:23694781). May also transfer the second mannose on\nCC       a 2-acyl-6-[2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-alpha-D-\nCC       glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol\nCC       (also termed H5), but less effectively (Probable).\nCC       {ECO:0000269|PubMed:23694781, ECO:0000305|PubMed:23694781}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 2-acyl-6-(alpha-D-mannosyl-(1->4)-alpha-D-glucosaminyl)-1-\nCC         (1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol + a di-\nCC         trans,poly-cis-dolichyl beta-D-mannosyl phosphate = a 2-acyl-6-\nCC         [alpha-D-mannosyl-(1->6)-alpha-D-mannosyl-(1->4)-alpha-D-\nCC         glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-inositol\nCC         + a di-trans,poly-cis-dolichyl phosphate + H(+);\nCC         Xref=Rhea:RHEA:60488, Rhea:RHEA-COMP:19498, Rhea:RHEA-COMP:19501,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:57683, ChEBI:CHEBI:58211,\nCC         ChEBI:CHEBI:143818, ChEBI:CHEBI:144028;\nCC         Evidence={ECO:0000269|PubMed:23694781};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:60489;\nCC         Evidence={ECO:0000269|PubMed:23694781};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 49-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 2-acyl-6-[2-phosphoethanolamine-alpha-D-mannosyl-(1->4)-\nCC         alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-phospho)-1D-myo-\nCC         inositol + a di-trans,poly-cis-dolichyl beta-D-mannosyl phosphate = a\nCC         2-acyl-6-[alpha-D-mannosyl-(1->6)-2-phosphoethanolamine-alpha-D-\nCC         mannosyl-(1->4)-alpha-D-glucosaminyl]-1-(1-radyl,2-acyl-sn-glycero-3-\nCC         phospho)-1D-myo-inositol + a di-trans,poly-cis-dolichyl phosphate +\nCC         H(+); Xref=Rhea:RHEA:60992, Rhea:RHEA-COMP:19498, Rhea:RHEA-\nCC         COMP:19501, ChEBI:CHEBI:15378, ChEBI:CHEBI:57683, ChEBI:CHEBI:58211,\nCC         ChEBI:CHEBI:144036, ChEBI:CHEBI:144054;\nCC         Evidence={ECO:0000305|PubMed:23694781};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:60993;\nCC         Evidence={ECO:0000305|PubMed:23694781};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-74",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0000009; F:alpha-1,6-mannosyltransferase activity; IEA:Ensembl.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-107",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19)

```json
{
  "entry_version": 19,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0004376; F:GPI mannosyltransferase activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:00.136470+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 108-108",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3a921910821c09b2eb30c40b3d3667f24af1b35f453619bbd6c349c529666aef",
  "url": "https://rest.uniprot.org/unisave/A0A8C2M425?format=txt&versions=19"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000009\nname: alpha-1,6-mannosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a mannose residue to an oligosaccharide, forming an alpha-(1->6) linkage.\" [GOC:mcc, PMID:2644248]\nsynonym: \"1,6-alpha-mannosyltransferase activity\" EXACT []\nxref: Reactome:R-HSA-449718 \"Addition of a third mannose to the N-glycan precursor by ALG2\"\nis_a: GO:0000030 ! mannosyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000009",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 117-125",
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
  "excerpt": "[Term]\nid: GO:0008753\nname: NADPH dehydrogenase (quinone) activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: NADPH + H+ + a quinone = NADP+ + a quinol.\" [RHEA:46164]\nsynonym: \"NADPH oxidase\" BROAD [EC:1.6.5.10]\nsynonym: \"NADPH:(quinone-acceptor) oxidoreductase\" RELATED [EC:1.6.5.10]\nsynonym: \"reduced nicotinamide adenine dinucleotide phosphate (quinone) dehydrogenase\" RELATED [EC:1.6.5.10]\nxref: EC:1.6.5.10\nxref: KEGG_REACTION:R07359\nxref: MetaCyc:RXN0-271\nxref: MetaCyc:RXN0-7385\nxref: RHEA:46164\nxref: RHEA:61980\nxref: RHEA:63492\nxref: RHEA:83239\nxref: RHEA:83247\nis_a: GO:0003955 ! NAD(P)H dehydrogenase (quinone) activity\nis_a: GO:0003959 ! NADPH dehydrogenase activity\nproperty_value: skos:exactMatch EC:1.6.5.10\nproperty_value: skos:exactMatch KEGG_REACTION:R07359\nproperty_value: skos:exactMatch MetaCyc:RXN0-7385\nproperty_value: skos:exactMatch RHEA:46164\nproperty_value: skos:narrowMatch MetaCyc:RXN0-271\nproperty_value: skos:narrowMatch RHEA:61980\nproperty_value: skos:narrowMatch RHEA:63492\nproperty_value: skos:narrowMatch RHEA:83239\nproperty_value: skos:narrowMatch RHEA:83247\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008753",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 87356-87384",
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
  "excerpt": "[Term]\nid: GO:0051539\nname: 4 iron, 4 sulfur cluster binding\nnamespace: molecular_function\ndef: \"Binding to a 4 iron, 4 sulfur (4Fe-4S) cluster; this cluster consists of four iron atoms, with the inorganic sulfur atoms found between the irons and acting as bridging ligands.\" [GOC:ai, PMID:15952888, Wikipedia:Iron-sulfur_cluster]\nsynonym: \"4 Fe 4 S cluster binding\" EXACT []\nsynonym: \"4 iron, 4 sulphur cluster binding\" EXACT []\nsynonym: \"4Fe-4S cluster binding\" EXACT []\nsynonym: \"iron-sulfur cluster 4Fe-4S binding\" EXACT []\nsynonym: \"iron-sulphur cluster 4Fe-4S binding\" EXACT []\nsynonym: \"tetrairon tetrasulfide cluster binding\" EXACT []\nsynonym: \"tetrairon tetrasulphide cluster binding\" EXACT []\nis_a: GO:0051536 ! iron-sulfur cluster binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051539",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 327906-327919",
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
  "excerpt": "[Term]\nid: GO:0051879\nname: Hsp90 protein binding\nnamespace: molecular_function\ndef: \"Binding to Hsp90 proteins, any of a group of heat shock proteins around 90kDa in size.\" [GOC:ai]\nsynonym: \"Hsp90 binding\" EXACT []\nsynonym: \"Hsp90 class protein binding\" EXACT []\nis_a: GO:0031072 ! heat shock protein binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051879",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 331451-331459",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO5

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO5",
  "excerpt": "[Term]\nid: GO:0120563\nname: dol-P-Man:Man(1)GlcN-acyl-PI alpha-1,6-mannosyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of an alpha-D-mannosyl residue from dolichol-P-mannose to Man(1)-GlcN-acyl-PI, forming an alpha-(1->6)-D-mannosyl-D-mannose linkage. This transfers the second mannose to the GPI precursor.\" [PMID:15623507]\nsynonym: \"glycosylphosphatidylinositol-mannosyltransferase II activity\" EXACT []\nsynonym: \"GPI-MT-II activity\" EXACT []\nis_a: GO:0000009 ! alpha-1,6-mannosyltransferase activity\nis_a: GO:0004376 ! GPI mannosyltransferase activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0120563",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 436201-436210",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 26. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
