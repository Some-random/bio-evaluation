# GO_molecular_function_0130

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0130.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — translation regulator activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MASDQLRFLGSLEGHKGWVTAIATSQENPDMILTASRDKTIIVWQLTRDEDSYGYPKRILTGHNHFVSDVVISSDGQFALSSSWDHTLRLWDLNTGATTRRFVGHTSDVLSVSFSADNRQIVSGSRDKTIKLWNTLGECKYDIKDECHTEWVSCVRFSPNVSNPVIVSCGWDRVVKVWELSKFKLKTNHYGHTGYINTVSVSPDGSLAASGGKDGITMLWDLNEGKHLYSLEAGDIVNALVFSPNRYWLCAATASCVKIFDLESKSIVDELKPAYTDVQDEGRQPECVSIAWSADGQTLFAGFTDNQLRVWTVTS

[Multiple Choices]
A. aspartic-type endopeptidase activity
B. glycosaminoglycan binding
C. phosphoglycolate phosphatase activity
D. translation regulator activity
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

> The sequence matches the UniProt entry annotated with translation regulator activity (C7; H5). The entry describes the protein as a ribosome component and reports regulatory effects on gene expression, though the GO annotation is computational (IEA:InterPro) and the functional description also includes similarity-based evidence (C5; H3).

Citations as saved: [C5](#evidence-c5), [C7](#evidence-c7), [H3](#evidence-h3), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains repeated WD-like motifs, consistent with a WD40-repeat, beta-propeller interaction scaffold rather than a typical catalytic enzyme. Transferable knowledge of fungal CPC2-like WD-repeat proteins and ribosome-associated regulatory proteins makes translation regulator activity a meaningful fit among these choices; the enzyme activities in A and C are poor fits, and B lacks a clear sequence-based indication.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides a credible family-level and structural inference that favors D over the offered alternatives. This is a probabilistic inference, not proof that WD40 repeats alone specify translation regulation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No alternative offered has comparable support from the sequence and transferable family-level knowledge.


### Important caveats

- The translation-regulator GO annotation is computationally assigned, not a direct experimental measurement of molecular function.
- The supplied source evidence matches the sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains repeated WD-like motifs, consistent with a WD40-repeat, beta-propeller interaction scaffold rather than a typical catalytic enzyme. Transferable knowledge of fungal CPC2-like WD-repeat proteins and ribosome-associated regulatory proteins makes translation regulator activity a meaningful fit among these choices; the enzyme activities in A and C are poor fits, and B lacks a clear sequence-based indication.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a credible family-level and structural inference that favors D over the offered alternatives. This is a probabilistic inference, not proof that WD40 repeats alone specify translation regulation."
  },
  "case_id": "GO_molecular_function_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C7",
      "H3",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated with translation regulator activity (C7; H5). The entry describes the protein as a ribosome component and reports regulatory effects on gene expression, though the GO annotation is computational (IEA:InterPro) and the functional description also includes similarity-based evidence (C5; H3)."
  },
  "important_caveats": [
    "The translation-regulator GO annotation is computationally assigned, not a direct experimental measurement of molecular function.",
    "The supplied source evidence matches the sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative offered has comparable support from the sequence and transferable family-level knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry annotated with translation regulator activity (C7; H5). The entry describes the protein as a ribosome component and reports regulatory effects on gene expression, though the GO annotation is computational (IEA:InterPro) and the functional description also includes similarity-based evidence (C5; H3).",
    "evidence_ids": ["C5", "C7", "H3", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains repeated WD-like motifs, consistent with a WD40-repeat, beta-propeller interaction scaffold rather than a typical catalytic enzyme. Transferable knowledge of fungal CPC2-like WD-repeat proteins and ribosome-associated regulatory proteins makes translation regulator activity a meaningful fit among these choices; the enzyme activities in A and C are poor fits, and B lacks a clear sequence-based indication.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a credible family-level and structural inference that favors D over the offered alternatives. This is a probabilistic inference, not proof that WD40 repeats alone specify translation regulation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No alternative offered has comparable support from the sequence and transferable family-level knowledge."
  },
  "important_caveats": [
    "The translation-regulator GO annotation is computationally assigned, not a direct experimental measurement of molecular function.",
    "The supplied source evidence matches the sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A223GEB2 (CPC2_FLAVE) annotates GO:0045182 (translation regulator activity) via IEA:InterPro. The protein is described as a 'Cross-pathway control WD-repeat protein 2' and a component of the ribosome (by similarity to Q01369). The GO annotation is present in the database, though it is computationally inferred (IEA) rather than experimentally determined. The protein's functional description also notes regulation of gene expression programs. The annotation is supported as a database record, with the caveat that the evidence code is IEA:InterPro.

Citations as saved: [C7](#evidence-c7), [H5](#evidence-h5), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is dominated by WD40 repeats (multiple W-D pairs in a ~40-residue periodic pattern: WQLTRDE, WDLNTG, WNTLGE, WVSCV, WELSKF, WDLNEG, WTVTS). WD40 repeats form β-propeller scaffolds for protein-protein interactions and are not catalytic domains. This eliminates option A (aspartic-type endopeptidase, requiring a catalytic Asp dyad/triad) and option C (phosphoglycolate phosphatase, requiring a specific phosphatase active site). WD40 β-propellers are not carbohydrate-binding modules, eliminating option B (glycosaminoglycan binding, typically associated with C-type lectins, pentraxins, or specific GAG-binding motifs). Among the four choices, only D (translation regulator activity) is compatible with a WD40 scaffold protein. Additionally, the specific 'RDKTI' motif pattern within the repeats is characteristic of WD40 domains found in ribosomal and translation-associated proteins (e.g., yeast Rpb3/Rpb11-like domains, eIF3 subunits), further supporting a ribosome/translation context. By family-level elimination, D is the only viable choice.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The WD40 repeat family is one of the most well-characterized protein families. A knowledgeable model can identify the WD40 β-propeller architecture from the sequence pattern, eliminate catalytic (A, C) and carbohydrate-binding (B) functions as incompatible with this fold, and recognize that among the offered alternatives only D is consistent with a WD40 scaffold protein. The ribosomal-protein-characteristic 'RDKTI' spacing further narrows the inference toward translation regulation rather than other WD40 functions (e.g., vesicle trafficking, chromatin remodeling).


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (A, B, C) are all mechanistically incompatible with a WD40 β-propeller scaffold, leaving only D as a viable choice. No other option is defensible given the dominant WD40 repeat architecture.


### Important caveats

- The GO:0045182 annotation is IEA:InterPro (computationally inferred), not experimentally validated for this specific protein.
- WD40 proteins participate in many cellular processes beyond translation regulation; the specificity to 'translation regulator activity' relies on the offered choices being mutually exclusive with WD40 function and on ribosomal-characteristic motif spacing.
- The protein's PubMed-validated function (PubMed:32273873) describes regulation of fruiting body development and cAMP signaling gene expression, which is transcriptional regulation rather than direct translation regulation at the ribosome. The GO molecular function annotation of 'translation regulator activity' reflects the ribosomal component annotation by similarity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is dominated by WD40 repeats (multiple W-D pairs in a ~40-residue periodic pattern: WQLTRDE, WDLNTG, WNTLGE, WVSCV, WELSKF, WDLNEG, WTVTS). WD40 repeats form β-propeller scaffolds for protein-protein interactions and are not catalytic domains. This eliminates option A (aspartic-type endopeptidase, requiring a catalytic Asp dyad/triad) and option C (phosphoglycolate phosphatase, requiring a specific phosphatase active site). WD40 β-propellers are not carbohydrate-binding modules, eliminating option B (glycosaminoglycan binding, typically associated with C-type lectins, pentraxins, or specific GAG-binding motifs). Among the four choices, only D (translation regulator activity) is compatible with a WD40 scaffold protein. Additionally, the specific 'RDKTI' motif pattern within the repeats is characteristic of WD40 domains found in ribosomal and translation-associated proteins (e.g., yeast Rpb3/Rpb11-like domains, eIF3 subunits), further supporting a ribosome/translation context. By family-level elimination, D is the only viable choice.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The WD40 repeat family is one of the most well-characterized protein families. A knowledgeable model can identify the WD40 β-propeller architecture from the sequence pattern, eliminate catalytic (A, C) and carbohydrate-binding (B) functions as incompatible with this fold, and recognize that among the offered alternatives only D is consistent with a WD40 scaffold protein. The ribosomal-protein-characteristic 'RDKTI' spacing further narrows the inference toward translation regulation rather than other WD40 functions (e.g., vesicle trafficking, chromatin remodeling)."
  },
  "case_id": "GO_molecular_function_0130",
  "expected_answer_check": {
    "evidence_ids": [
      "C7",
      "H5",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A223GEB2 (CPC2_FLAVE) annotates GO:0045182 (translation regulator activity) via IEA:InterPro. The protein is described as a 'Cross-pathway control WD-repeat protein 2' and a component of the ribosome (by similarity to Q01369). The GO annotation is present in the database, though it is computationally inferred (IEA) rather than experimentally determined. The protein's functional description also notes regulation of gene expression programs. The annotation is supported as a database record, with the caveat that the evidence code is IEA:InterPro."
  },
  "important_caveats": [
    "The GO:0045182 annotation is IEA:InterPro (computationally inferred), not experimentally validated for this specific protein.",
    "WD40 proteins participate in many cellular processes beyond translation regulation; the specificity to 'translation regulator activity' relies on the offered choices being mutually exclusive with WD40 function and on ribosomal-characteristic motif spacing.",
    "The protein's PubMed-validated function (PubMed:32273873) describes regulation of fruiting body development and cAMP signaling gene expression, which is transcriptional regulation rather than direct translation regulation at the ribosome. The GO molecular function annotation of 'translation regulator activity' reflects the ribosomal component annotation by similarity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (A, B, C) are all mechanistically incompatible with a WD40 β-propeller scaffold, leaving only D as a viable choice. No other option is defensible given the dominant WD40 repeat architecture."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0130",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A223GEB2 (CPC2_FLAVE) annotates GO:0045182 (translation regulator activity) via IEA:InterPro. The protein is described as a 'Cross-pathway control WD-repeat protein 2' and a component of the ribosome (by similarity to Q01369). The GO annotation is present in the database, though it is computationally inferred (IEA) rather than experimentally determined. The protein's functional description also notes regulation of gene expression programs. The annotation is supported as a database record, with the caveat that the evidence code is IEA:InterPro.",
    "evidence_ids": ["C7", "H5", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is dominated by WD40 repeats (multiple W-D pairs in a ~40-residue periodic pattern: WQLTRDE, WDLNTG, WNTLGE, WVSCV, WELSKF, WDLNEG, WTVTS). WD40 repeats form β-propeller scaffolds for protein-protein interactions and are not catalytic domains. This eliminates option A (aspartic-type endopeptidase, requiring a catalytic Asp dyad/triad) and option C (phosphoglycolate phosphatase, requiring a specific phosphatase active site). WD40 β-propellers are not carbohydrate-binding modules, eliminating option B (glycosaminoglycan binding, typically associated with C-type lectins, pentraxins, or specific GAG-binding motifs). Among the four choices, only D (translation regulator activity) is compatible with a WD40 scaffold protein. Additionally, the specific 'RDKTI' motif pattern within the repeats is characteristic of WD40 domains found in ribosomal and translation-associated proteins (e.g., yeast Rpb3/Rpb11-like domains, eIF3 subunits), further supporting a ribosome/translation context. By family-level elimination, D is the only viable choice.",
    "missing_item_specific_fact": "",
    "reason": "The WD40 repeat family is one of the most well-characterized protein families. A knowledgeable model can identify the WD40 β-propeller architecture from the sequence pattern, eliminate catalytic (A, C) and carbohydrate-binding (B) functions as incompatible with this fold, and recognize that among the offered alternatives only D is consistent with a WD40 scaffold protein. The ribosomal-protein-characteristic 'RDKTI' spacing further narrows the inference toward translation regulation rather than other WD40 functions (e.g., vesicle trafficking, chromatin remodeling)."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (A, B, C) are all mechanistically incompatible with a WD40 β-propeller scaffold, leaving only D as a viable choice. No other option is defensible given the dominant WD40 repeat architecture."
  },
  "important_caveats": [
    "The GO:0045182 annotation is IEA:InterPro (computationally inferred), not experimentally validated for this specific protein.",
    "WD40 proteins participate in many cellular processes beyond translation regulation; the specificity to 'translation regulator activity' relies on the offered choices being mutually exclusive with WD40 function and on ribosomal-characteristic motif spacing.",
    "The protein's PubMed-validated function (PubMed:32273873) describes regulation of fruiting body development and cAMP signaling gene expression, which is transcriptional regulation rather than direct translation regulation at the ribosome. The GO molecular function annotation of 'translation regulator activity' reflects the ribosomal component annotation by similarity."
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
  "benchmark_sequence_length": 315,
  "benchmark_sequence_sha256": "d3baf37b83300da4d76fe26c43b8f9d51ac1b0b73b08def9479ca54c6a46ba37",
  "current_entry_audit": {
    "entryVersion": 19,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-10-25",
    "sequenceVersion": 1
  },
  "current_record_sha256": "bff2f48356558647c2396d801380e7284c70fbbee4d4dfc282d68400dcdb751b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 315,
  "current_source_sequence_sha256": "d3baf37b83300da4d76fe26c43b8f9d51ac1b0b73b08def9479ca54c6a46ba37",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 18,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A223GEB2",
  "selected_historical_entry_version": 18,
  "selected_historical_record_sha256": "08b21d0de3ba4039cd1c346641d0bdb62523c8a44c63067352d57b9a47ef9174",
  "selected_historical_source_sequence_length": 315,
  "selected_historical_source_sequence_sha256": "d3baf37b83300da4d76fe26c43b8f9d51ac1b0b73b08def9479ca54c6a46ba37",
  "selected_historical_version": {
    "accession": "A0A223GEB2",
    "database": "Swiss-Prot",
    "entryVersion": 18,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "CPC2_FLAVE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GEB2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A223GEB2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:42.147209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bff2f48356558647c2396d801380e7284c70fbbee4d4dfc282d68400dcdb751b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GEB2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GEB2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":19,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-10-25\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:42.147209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bff2f48356558647c2396d801380e7284c70fbbee4d4dfc282d68400dcdb751b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GEB2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GEB2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Agaricus velutipes\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Agaricomycetes\",\"Agaricomycetidae\",\"Agaricales\",\"Marasmiineae\",\"Physalacriaceae\",\"Flammulina\"],\"scientificName\":\"Flammulina velutipes\",\"taxonId\":38945}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:42.147209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bff2f48356558647c2396d801380e7284c70fbbee4d4dfc282d68400dcdb751b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GEB2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GEB2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"32273873\",\"source\":\"PubMed\"}],\"value\":\"Cross-pathway control WD-repeat protein 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:42.147209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bff2f48356558647c2396d801380e7284c70fbbee4d4dfc282d68400dcdb751b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GEB2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GEB2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q01369\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"32273873\",\"source\":\"PubMed\"}],\"value\":\"Component of the ribosome, a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell. The small ribosomal subunit (SSU) binds messenger RNAs (mRNAs) and translates the encoded message by selecting cognate aminoacyl-transfer RNA (tRNA) molecules. The large subunit (LSU) contains the ribosomal catalytic site termed the peptidyl transferase center (PTC), which catalyzes the formation of peptide bonds, thereby polymerizing the amino acids delivered by tRNAs into a polypeptide chain. The nascent polypeptides leave the ribosome through a tunnel in the LSU and interact with protein factors that function in enzymatic processing, targeting, and the membrane insertion of nascent chains at the exit of the ribosomal tunnel (By similarity). Plays in important role in the regulation of vegetative growth and fruiting body development (PubMed:32273873). Especially, positively regulates the expression of genes involved in fruiting body development such as FVFD30 and FVFD16, as well as genes encoding for lectins and hydrophobins (PubMed:32273873). Also regulates the expression of genes involved in cAMP signaling pathway (PubMed:32273873)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:24:42.147209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bff2f48356558647c2396d801380e7284c70fbbee4d4dfc282d68400dcdb751b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GEB2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GEB2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0043022\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:ribosome binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/3",
  "retrieved_utc": "2026-11-02T04:24:42.147209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bff2f48356558647c2396d801380e7284c70fbbee4d4dfc282d68400dcdb751b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GEB2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GEB2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0045182\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:translation regulator activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-02T04:24:42.147209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bff2f48356558647c2396d801380e7284c70fbbee4d4dfc282d68400dcdb751b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GEB2.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A223GEB2.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Wu T.\",\"Zhang Z.\",\"Hu C.\",\"Zhang L.\",\"Wei S.\",\"Li S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"32273873\"},{\"database\":\"DOI\",\"id\":\"10.3389/fmicb.2020.00498\"}],\"citationType\":\"journal article\",\"firstPage\":\"498\",\"id\":\"32273873\",\"journal\":\"Front. Microbiol.\",\"lastPage\":\"498\",\"publicationDate\":\"2020\",\"title\":\"A WD40 Protein Encoding Gene Fvcpc2 Positively Regulates Mushroom Development and Yield in Flammulina velutipes.\",\"volume\":\"11\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"DEVELOPMENTAL STAGE\",\"FUNCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:24:42.147209+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "bff2f48356558647c2396d801380e7284c70fbbee4d4dfc282d68400dcdb751b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A223GEB2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GEB2?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H1",
  "excerpt": "ID   CPC2_FLAVE              Reviewed;         315 AA.\nAC   A0A223GEB2;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   25-OCT-2017, sequence version 1.\nDT   28-JAN-2026, entry version 18.\nDE   RecName: Full=Cross-pathway control WD-repeat protein 2 {ECO:0000303|PubMed:32273873};\nGN   Name=cpc2 {ECO:0000303|PubMed:32273873};\nOS   Flammulina velutipes (Agaricus velutipes).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Agaricomycetes;\nOC   Agaricomycetidae; Agaricales; Marasmiineae; Physalacriaceae; Flammulina.\nOX   NCBI_TaxID=38945;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:43.872451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-11",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "08b21d0de3ba4039cd1c346641d0bdb62523c8a44c63067352d57b9a47ef9174",
  "url": "https://rest.uniprot.org/unisave/A0A223GEB2?format=txt&versions=18"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GEB2?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], DEVELOPMENTAL STAGE, FUNCTION, AND\nRP   DISRUPTION PHENOTYPE.\nRX   PubMed=32273873; DOI=10.3389/fmicb.2020.00498;\nRA   Wu T., Zhang Z., Hu C., Zhang L., Wei S., Li S.;\nRT   \"A WD40 Protein Encoding Gene Fvcpc2 Positively Regulates Mushroom\nRT   Development and Yield in Flammulina velutipes.\";\nRL   Front. Microbiol. 11:498-498(2020).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:43.872451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 12-19",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "08b21d0de3ba4039cd1c346641d0bdb62523c8a44c63067352d57b9a47ef9174",
  "url": "https://rest.uniprot.org/unisave/A0A223GEB2?format=txt&versions=18"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GEB2?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Component of the ribosome, a large ribonucleoprotein complex\nCC       responsible for the synthesis of proteins in the cell. The small\nCC       ribosomal subunit (SSU) binds messenger RNAs (mRNAs) and translates the\nCC       encoded message by selecting cognate aminoacyl-transfer RNA (tRNA)\nCC       molecules. The large subunit (LSU) contains the ribosomal catalytic\nCC       site termed the peptidyl transferase center (PTC), which catalyzes the\nCC       formation of peptide bonds, thereby polymerizing the amino acids\nCC       delivered by tRNAs into a polypeptide chain. The nascent polypeptides\nCC       leave the ribosome through a tunnel in the LSU and interact with\nCC       protein factors that function in enzymatic processing, targeting, and\nCC       the membrane insertion of nascent chains at the exit of the ribosomal\nCC       tunnel (By similarity). Plays in important role in the regulation of\nCC       vegetative growth and fruiting body development (PubMed:32273873).\nCC       Especially, positively regulates the expression of genes involved in\nCC       fruiting body development such as FVFD30 and FVFD16, as well as genes\nCC       encoding for lectins and hydrophobins (PubMed:32273873). Also regulates\nCC       the expression of genes involved in cAMP signaling pathway\nCC       (PubMed:32273873). {ECO:0000250|UniProtKB:Q01369,\nCC       ECO:0000269|PubMed:32273873}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:43.872451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 20-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "08b21d0de3ba4039cd1c346641d0bdb62523c8a44c63067352d57b9a47ef9174",
  "url": "https://rest.uniprot.org/unisave/A0A223GEB2?format=txt&versions=18"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GEB2?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0043022; F:ribosome binding; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:43.872451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 60-60",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "08b21d0de3ba4039cd1c346641d0bdb62523c8a44c63067352d57b9a47ef9174",
  "url": "https://rest.uniprot.org/unisave/A0A223GEB2?format=txt&versions=18"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A223GEB2?format=txt&versions=18)

```json
{
  "entry_version": 18,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0045182; F:translation regulator activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:43.872451+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 61-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "08b21d0de3ba4039cd1c346641d0bdb62523c8a44c63067352d57b9a47ef9174",
  "url": "https://rest.uniprot.org/unisave/A0A223GEB2?format=txt&versions=18"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004190\nname: aspartic-type endopeptidase activity\nnamespace: molecular_function\ndef: \"Catalysis of the hydrolysis of internal, alpha-peptide bonds in a polypeptide chain by a mechanism in which a water molecule bound by the side chains of aspartic residues at the active center acts as a nucleophile.\" [ISBN:0198506732]\nsynonym: \"aspartate protease activity\" NARROW [GOC:mah, GOC:vw]\nsynonym: \"aspartic endopeptidase activity\" EXACT []\nsynonym: \"aspartic protease activity\" NARROW []\nsynonym: \"aspartyl protease activity\" NARROW []\nsynonym: \"carboxyl protease activity\" NARROW []\nxref: EC:3.4.23.-\nxref: EC:3.4.23.1\nxref: EC:3.4.23.15\nxref: EC:3.4.23.20\nxref: EC:3.4.23.25\nxref: EC:3.4.23.32\nxref: EC:3.4.23.34\nxref: EC:3.4.23.35\nxref: EC:3.4.23.36\nxref: EC:3.4.23.4\nxref: EC:3.4.23.43\nxref: EC:3.4.23.49\nxref: EC:3.4.23.5\nxref: MetaCyc:3.4.23.1-RXN\nxref: MetaCyc:3.4.23.15-RXN\nxref: MetaCyc:3.4.23.20-RXN\nxref: MetaCyc:3.4.23.25-RXN\nxref: MetaCyc:3.4.23.32-RXN\nxref: MetaCyc:3.4.23.34-RXN\nxref: MetaCyc:3.4.23.35-RXN\nxref: MetaCyc:3.4.23.4-RXN\nxref: MetaCyc:3.4.23.43-RXN\nxref: MetaCyc:3.4.23.5-RXN\nxref: Reactome:R-HSA-157353 \"NEXT1 is cleaved to produce NICD1\"\nxref: Reactome:R-HSA-157640 \"NEXT2 is cleaved to produce NICD2\"\nxref: Reactome:R-HSA-2022403 \"Renin:Prorenin Receptor hydrolyzes Angiotensinogen to AGT(25-34) (Angiotensin-(1-10))\"\nxref: Reactome:R-HSA-2022412 \"Renin hydrolyzes Angiotensinogen to AGT(25-34) (Angiotensin-(1-10))\"\nxref: Reactome:R-HSA-2065357 \"Prorenin:Prorenin Receptor hydrolyzes Angiotensinogen to AGT(25-35) (Angiotensin-(1-10))\"\nxref: Reactome:R-HSA-2220988 \"NEXT1 PEST domain mutants are cleaved to produce NICD1 PEST domain mutants\"\nxref: Reactome:R-HSA-373705 \"Caspase cleavage of DCC\"\nxref: Reactome:R-HSA-9013361 \"NEXT3 is cleaved to produce NICD3\"\nxref: Reactome:R-HSA-9017817 \"Gamma-secretase cleaves YBX1:NOTCH3\"\nxref: Reactome:R-HSA-9604294 \"Gamma-secretase cleaves NOTCH4\"\nis_a: GO:0004175 ! endopeptidase activity\nis_a: GO:0070001 ! aspartic-type peptidase activity\nproperty_value: skos:exactMatch EC:3.4.23.-\nproperty_value: skos:narrowMatch EC:3.4.23.1\nproperty_value: skos:narrowMatch EC:3.4.23.15\nproperty_value: skos:narrowMatch EC:3.4.23.20\nproperty_value: skos:narrowMatch EC:3.4.23.25\nproperty_value: skos:narrowMatch EC:3.4.23.32\nproperty_value: skos:narrowMatch EC:3.4.23.34\nproperty_value: skos:narrowMatch EC:3.4.23.35\nproperty_value: skos:narrowMatch EC:3.4.23.36\nproperty_value: skos:narrowMatch EC:3.4.23.4\nproperty_value: skos:narrowMatch EC:3.4.23.43\nproperty_value: skos:narrowMatch EC:3.4.23.49\nproperty_value: skos:narrowMatch EC:3.4.23.5\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.1-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.15-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.20-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.25-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.32-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.34-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.35-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.4-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.43-RXN\nproperty_value: skos:narrowMatch MetaCyc:3.4.23.5-RXN\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004190",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 37379-37447",
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
  "excerpt": "[Term]\nid: GO:0005539\nname: glycosaminoglycan binding\nnamespace: molecular_function\ndef: \"Binding to a glycan (polysaccharide) containing a substantial proportion of aminomonosaccharide residues.\" [GOC:jl, ISBN:0198506732]\nsubset: goslim_chembl\nis_a: GO:0097367 ! carbohydrate derivative binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005539",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 57150-57157",
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
  "excerpt": "[Term]\nid: GO:0008967\nname: phosphoglycolate phosphatase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: 2-phosphoglycolate + H2O = glycolate + phosphate.\" [EC:3.1.3.18, RHEA:14369]\nsynonym: \"2-phosphoglycolate phosphatase activity\" RELATED [EC:3.1.3.18]\nsynonym: \"2-phosphoglycolate phosphohydrolase activity\" RELATED [EC:3.1.3.18]\nsynonym: \"P-glycolate phosphatase activity\" RELATED [EC:3.1.3.18]\nsynonym: \"phosphoglycolate hydrolase activity\" RELATED [EC:3.1.3.18]\nsynonym: \"phosphoglycollate phosphatase activity\" RELATED [EC:3.1.3.18]\nxref: EC:3.1.3.18\nxref: KEGG_REACTION:R01334\nxref: MetaCyc:GPH-RXN\nxref: RHEA:14369\nis_a: GO:0016791 ! phosphatase activity\nproperty_value: skos:exactMatch EC:3.1.3.18\nproperty_value: skos:exactMatch RHEA:14369\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008967",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 90815-90832",
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
  "excerpt": "[Term]\nid: GO:0045182\nname: translation regulator activity\nnamespace: molecular_function\ndef: \"Any molecular function involved in the regulation of initiation, activation, perpetuation, repression or termination of polypeptide synthesis at the ribosome.\" [GOC:ai]\nsubset: goslim_candida\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_generic\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nis_a: GO:0003674 ! molecular_function\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0045182",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 262674-262689",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 130. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
