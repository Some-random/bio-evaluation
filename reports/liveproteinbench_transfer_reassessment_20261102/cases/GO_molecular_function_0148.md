# GO_molecular_function_0148

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0148.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — ABC-type transporter activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTAYALTDSWTMTRRELARWARQPVQLVVNLVFPVMLLLMFGYLIGGGRGVNGEYRDYLIPGMLALTMAFGLEGTMIAVTRDLDKGVIDRFRSMPMADGAVLVGRSAADMLQSAMALVVLIGVGAALGWRVHGGPVAFLGAVGLLLLFRFAMLWIGIYLALVAGKPEMVQAVQILVWPIGFLSNALALPDTMPGWLGTVVEWNPMSHTATAVRDLFGTPGAESGHVGAALVWPLALLAVFFPLAVRRFGRLSR

[Multiple Choices]
A. ABC-type transporter activity
B. tubulin deacetylase activity
C. structural constituent of vitelline membrane
D. RNA binding
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

> The evidence matches the supplied sequence and supports an ABC-transporter role: the UniProt annotation assigns ABC-type transporter activity computationally, and the function annotation describes this protein as a permease in a daunorubicin-efflux ABC complex. The protein’s specific role in substrate translocation is marked probable, so the evidence supports the broad choice without establishing every mechanistic detail experimentally.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is dominated by hydrophobic stretches consistent with a multi-pass integral membrane protein, making a membrane transport/permease role far more plausible than tubulin deacetylation, RNA binding, or a vitelline-membrane structural role. ABC transport systems commonly use membrane permease subunits alongside separate ATP-hydrolyzing subunits, so the absence of an obvious ATP-binding domain does not rule out choice A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and alternatives support a meaningful, probabilistic choice of A over the offered distractors. The sequence alone does not prove that this is specifically an ABC permease rather than another type of membrane protein, but the choices do not offer another membrane-transport option.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the strongly hydrophobic, multi-pass membrane-protein sequence.


### Important caveats

- ABC-type transporter activity here is attributed to a permease component of a transporter complex; the protein need not itself contain the ATP-hydrolyzing nucleotide-binding domain.
- The database GO assignment is computational (IEA:InterPro); the specific substrate-translocation role is described as probable.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is dominated by hydrophobic stretches consistent with a multi-pass integral membrane protein, making a membrane transport/permease role far more plausible than tubulin deacetylation, RNA binding, or a vitelline-membrane structural role. ABC transport systems commonly use membrane permease subunits alongside separate ATP-hydrolyzing subunits, so the absence of an obvious ATP-binding domain does not rule out choice A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and alternatives support a meaningful, probabilistic choice of A over the offered distractors. The sequence alone does not prove that this is specifically an ABC permease rather than another type of membrane protein, but the choices do not offer another membrane-transport option."
  },
  "case_id": "GO_molecular_function_0148",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The evidence matches the supplied sequence and supports an ABC-transporter role: the UniProt annotation assigns ABC-type transporter activity computationally, and the function annotation describes this protein as a permease in a daunorubicin-efflux ABC complex. The protein’s specific role in substrate translocation is marked probable, so the evidence supports the broad choice without establishing every mechanistic detail experimentally."
  },
  "important_caveats": [
    "ABC-type transporter activity here is attributed to a permease component of a transporter complex; the protein need not itself contain the ATP-hydrolyzing nucleotide-binding domain.",
    "The database GO assignment is computational (IEA:InterPro); the specific substrate-translocation role is described as probable."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the strongly hydrophobic, multi-pass membrane-protein sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The evidence matches the supplied sequence and supports an ABC-transporter role: the UniProt annotation assigns ABC-type transporter activity computationally, and the function annotation describes this protein as a permease in a daunorubicin-efflux ABC complex. The protein’s specific role in substrate translocation is marked probable, so the evidence supports the broad choice without establishing every mechanistic detail experimentally.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is dominated by hydrophobic stretches consistent with a multi-pass integral membrane protein, making a membrane transport/permease role far more plausible than tubulin deacetylation, RNA binding, or a vitelline-membrane structural role. ABC transport systems commonly use membrane permease subunits alongside separate ATP-hydrolyzing subunits, so the absence of an obvious ATP-binding domain does not rule out choice A.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and alternatives support a meaningful, probabilistic choice of A over the offered distractors. The sequence alone does not prove that this is specifically an ABC permease rather than another type of membrane protein, but the choices do not offer another membrane-transport option."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the strongly hydrophobic, multi-pass membrane-protein sequence."
  },
  "important_caveats": [
    "ABC-type transporter activity here is attributed to a permease component of a transporter complex; the protein need not itself contain the ATP-hydrolyzing nucleotide-binding domain.",
    "The database GO assignment is computational (IEA:InterPro); the specific substrate-translocation role is described as probable."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXU8 annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB3' with GO:0140359 (ABC-type transporter activity). The functional annotation is supported by experimental evidence (PubMed:39375957, ECO:0000269) showing it is part of the ABC transporter complex DrrA3B3 involved in daunorubicin efflux. The GO term assignment itself is IEA:InterPro, but the underlying function is experimentally validated. The protein is described as responsible for translocation of substrate across the membrane.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 253-aa sequence is overwhelmingly hydrophobic with approximately 6 transmembrane helices, characteristic of a membrane permease. Transferable knowledge about protein families allows elimination of all distractors: (1) Tubulin deacetylase (B) requires catalytic HD motif, Zn-coordinating residues, and is a soluble cytoplasmic enzyme — none of these features are present. (2) Structural constituent of vitelline membrane (C) is an extremely specific eukaryotic (Drosophila egg) function; a bacterial hydrophobic membrane protein cannot fulfill this role. (3) RNA binding (D) requires nucleic-acid-binding domains (RRM, KH, zinc fingers, or basic patches) — the sequence lacks any such motifs and is dominated by hydrophobic TM segments. The only remaining option, ABC-type transporter activity (A), is consistent with a multi-TM membrane protein. The 'GG' motifs (e.g., GGGRGVNGEY, GGAALGWRVHGG) and the alternating hydrophilic/hydrophobic topology are well-known features of ABC permease components (6-TM permease subunits). A knowledgeable model can recognize this as a membrane transporter and, among the four choices, only A describes a membrane transport function.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence's extreme hydrophobicity and multi-TM topology immediately identify it as a membrane protein, eliminating the soluble enzyme (B), the eukaryotic structural protein (C), and the nucleic-acid-binding protein (D). The 6-TM permease architecture with GG motifs is a well-known family signature shared across many ABC permease homologs. Among the four offered choices, only A describes a membrane transport activity, making this distinguishable through general protein-family knowledge without needing to look up this specific entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors are clearly incompatible with a hydrophobic bacterial membrane protein: tubulin deacetylase is a soluble enzyme requiring specific catalytic residues; vitelline membrane structural protein is exclusively eukaryotic; RNA binding requires nucleic-acid-binding domains. Only option A (membrane transporter activity) is consistent with the observed multi-TM topology.


### Important caveats

- The GO annotation for ABC-type transporter activity is IEA:InterPro (computational), but the underlying biological function is experimentally supported by PubMed:39375957.
- Distinguishing ABC permease from other 6-TM membrane transporters (MFS, SMR) would require more specific sequence knowledge, but among the four offered choices only A is a membrane transporter function, so this distinction is unnecessary for answering the question.
- The protein was first publicly released in February 2025; the benchmark author's source snapshot is unknown but the sequence matches the historical entry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 253-aa sequence is overwhelmingly hydrophobic with approximately 6 transmembrane helices, characteristic of a membrane permease. Transferable knowledge about protein families allows elimination of all distractors: (1) Tubulin deacetylase (B) requires catalytic HD motif, Zn-coordinating residues, and is a soluble cytoplasmic enzyme — none of these features are present. (2) Structural constituent of vitelline membrane (C) is an extremely specific eukaryotic (Drosophila egg) function; a bacterial hydrophobic membrane protein cannot fulfill this role. (3) RNA binding (D) requires nucleic-acid-binding domains (RRM, KH, zinc fingers, or basic patches) — the sequence lacks any such motifs and is dominated by hydrophobic TM segments. The only remaining option, ABC-type transporter activity (A), is consistent with a multi-TM membrane protein. The 'GG' motifs (e.g., GGGRGVNGEY, GGAALGWRVHGG) and the alternating hydrophilic/hydrophobic topology are well-known features of ABC permease components (6-TM permease subunits). A knowledgeable model can recognize this as a membrane transporter and, among the four choices, only A describes a membrane transport function.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence's extreme hydrophobicity and multi-TM topology immediately identify it as a membrane protein, eliminating the soluble enzyme (B), the eukaryotic structural protein (C), and the nucleic-acid-binding protein (D). The 6-TM permease architecture with GG motifs is a well-known family signature shared across many ABC permease homologs. Among the four offered choices, only A describes a membrane transport activity, making this distinguishable through general protein-family knowledge without needing to look up this specific entry."
  },
  "case_id": "GO_molecular_function_0148",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU8 annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB3' with GO:0140359 (ABC-type transporter activity). The functional annotation is supported by experimental evidence (PubMed:39375957, ECO:0000269) showing it is part of the ABC transporter complex DrrA3B3 involved in daunorubicin efflux. The GO term assignment itself is IEA:InterPro, but the underlying function is experimentally validated. The protein is described as responsible for translocation of substrate across the membrane."
  },
  "important_caveats": [
    "The GO annotation for ABC-type transporter activity is IEA:InterPro (computational), but the underlying biological function is experimentally supported by PubMed:39375957.",
    "Distinguishing ABC permease from other 6-TM membrane transporters (MFS, SMR) would require more specific sequence knowledge, but among the four offered choices only A is a membrane transporter function, so this distinction is unnecessary for answering the question.",
    "The protein was first publicly released in February 2025; the benchmark author's source snapshot is unknown but the sequence matches the historical entry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are clearly incompatible with a hydrophobic bacterial membrane protein: tubulin deacetylase is a soluble enzyme requiring specific catalytic residues; vitelline membrane structural protein is exclusively eukaryotic; RNA binding requires nucleic-acid-binding domains. Only option A (membrane transporter activity) is consistent with the observed multi-TM topology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0148",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXU8 annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB3' with GO:0140359 (ABC-type transporter activity). The functional annotation is supported by experimental evidence (PubMed:39375957, ECO:0000269) showing it is part of the ABC transporter complex DrrA3B3 involved in daunorubicin efflux. The GO term assignment itself is IEA:InterPro, but the underlying function is experimentally validated. The protein is described as responsible for translocation of substrate across the membrane.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 253-aa sequence is overwhelmingly hydrophobic with approximately 6 transmembrane helices, characteristic of a membrane permease. Transferable knowledge about protein families allows elimination of all distractors: (1) Tubulin deacetylase (B) requires catalytic HD motif, Zn-coordinating residues, and is a soluble cytoplasmic enzyme — none of these features are present. (2) Structural constituent of vitelline membrane (C) is an extremely specific eukaryotic (Drosophila egg) function; a bacterial hydrophobic membrane protein cannot fulfill this role. (3) RNA binding (D) requires nucleic-acid-binding domains (RRM, KH, zinc fingers, or basic patches) — the sequence lacks any such motifs and is dominated by hydrophobic TM segments. The only remaining option, ABC-type transporter activity (A), is consistent with a multi-TM membrane protein. The 'GG' motifs (e.g., GGGRGVNGEY, GGAALGWRVHGG) and the alternating hydrophilic/hydrophobic topology are well-known features of ABC permease components (6-TM permease subunits). A knowledgeable model can recognize this as a membrane transporter and, among the four choices, only A describes a membrane transport function.",
    "missing_item_specific_fact": "",
    "reason": "The sequence's extreme hydrophobicity and multi-TM topology immediately identify it as a membrane protein, eliminating the soluble enzyme (B), the eukaryotic structural protein (C), and the nucleic-acid-binding protein (D). The 6-TM permease architecture with GG motifs is a well-known family signature shared across many ABC permease homologs. Among the four offered choices, only A describes a membrane transport activity, making this distinguishable through general protein-family knowledge without needing to look up this specific entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are clearly incompatible with a hydrophobic bacterial membrane protein: tubulin deacetylase is a soluble enzyme requiring specific catalytic residues; vitelline membrane structural protein is exclusively eukaryotic; RNA binding requires nucleic-acid-binding domains. Only option A (membrane transporter activity) is consistent with the observed multi-TM topology."
  },
  "important_caveats": [
    "The GO annotation for ABC-type transporter activity is IEA:InterPro (computational), but the underlying biological function is experimentally supported by PubMed:39375957.",
    "Distinguishing ABC permease from other 6-TM membrane transporters (MFS, SMR) would require more specific sequence knowledge, but among the four offered choices only A is a membrane transporter function, so this distinction is unnecessary for answering the question.",
    "The protein was first publicly released in February 2025; the benchmark author's source snapshot is unknown but the sequence matches the historical entry."
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
  "benchmark_sequence_length": 253,
  "benchmark_sequence_sha256": "9c61ef0503b981c7cb08fb2fc1c1b21bbe37d8e61f0715291f563a59b5c16662",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 253,
  "current_source_sequence_sha256": "9c61ef0503b981c7cb08fb2fc1c1b21bbe37d8e61f0715291f563a59b5c16662",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 4,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXU8",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e",
  "selected_historical_source_sequence_length": 253,
  "selected_historical_source_sequence_sha256": "9c61ef0503b981c7cb08fb2fc1c1b21bbe37d8e61f0715291f563a59b5c16662",
  "selected_historical_version": {
    "accession": "P0DXU8",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DRRB3_STRC4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXU8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:15.602104+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:15.602104+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces coeruleorubidus\",\"taxonId\":116188}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:15.602104+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Daunorubicin resistance ABC transporter permease protein DrrB3\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:15.602104+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39375957\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Part of the ABC transporter complex DrrA3B3 involved in daunorubicin efflux (PubMed:39375957). Responsible for the translocation of the substrate across the membrane (Probable). Confers self-resistance to daunorubicin, an antibiotic produced by S.coeruleorubidus (PubMed:39375957). The efficiency of DrrA3B3 to export daunorubicin is probably lower than that of DrrA1B1 or DrrA2B2 (PubMed:39375957)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:15.602104+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0140359\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:ABC-type transporter activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/7",
  "retrieved_utc": "2026-11-01T06:25:15.602104+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Dong J.\",\"Ning J.\",\"Tian Y.\",\"Li H.\",\"Chen H.\",\"Guan W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39375957\"},{\"database\":\"DOI\",\"id\":\"10.1111/1751-7915.70023\"}],\"citationType\":\"journal article\",\"firstPage\":\"e70023\",\"id\":\"39375957\",\"journal\":\"Microb. Biotechnol.\",\"lastPage\":\"e70023\",\"publicationDate\":\"2024\",\"title\":\"The involvement of multiple ABC transporters in daunorubicin efflux in Streptomyces coeruleorubidus.\",\"volume\":\"17\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION IN DAUNORUBICIN EFFLUX\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:15.602104+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "c44dd25653843feda280457e5b2e85251c777e88151bb6df35b17c700c0142ca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   DRRB3_STRC4             Reviewed;         253 AA.\nAC   P0DXU8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Daunorubicin resistance ABC transporter permease protein DrrB3 {ECO:0000305};\nGN   Name=drrB3 {ECO:0000303|PubMed:39375957};\nGN   ORFNames=R5U08_20730 {ECO:0000312|EMBL:WOT36400.1};\nOS   Streptomyces coeruleorubidus.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=116188;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:21.104799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e",
  "url": "https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39375957; DOI=10.1111/1751-7915.70023;\nRA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;\nRT   \"The involvement of multiple ABC transporters in daunorubicin efflux in\nRT   Streptomyces coeruleorubidus.\";\nRL   Microb. Biotechnol. 17:e70023-e70023(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:21.104799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e",
  "url": "https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Part of the ABC transporter complex DrrA3B3 involved in\nCC       daunorubicin efflux (PubMed:39375957). Responsible for the\nCC       translocation of the substrate across the membrane (Probable). Confers\nCC       self-resistance to daunorubicin, an antibiotic produced by\nCC       S.coeruleorubidus (PubMed:39375957). The efficiency of DrrA3B3 to\nCC       export daunorubicin is probably lower than that of DrrA1B1 or DrrA2B2\nCC       (PubMed:39375957). {ECO:0000269|PubMed:39375957, ECO:0000305}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:21.104799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e",
  "url": "https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0140359; F:ABC-type transporter activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:21.104799+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 56-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "eacc14042885f4a9bee71583e3725efd2169f7b227d732287e6adf264663178e",
  "url": "https://rest.uniprot.org/unisave/P0DXU8?format=txt&versions=4"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0003723\nname: RNA binding\nnamespace: molecular_function\nalt_id: GO:0000498\nalt_id: GO:0044822\ndef: \"Binding to an RNA molecule or a portion thereof.\" [GOC:jl, GOC:mah]\nsubset: goslim_agr\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_mouse\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote\nsubset: goslim_prokaryote_ribbon\nsubset: goslim_yeast\nsynonym: \"base pairing with RNA\" NARROW []\nsynonym: \"poly(A) RNA binding\" RELATED []\nsynonym: \"poly(A)-RNA binding\" RELATED []\nsynonym: \"poly-A RNA binding\" RELATED []\nxref: Reactome:R-HSA-203922 \"Exportin-5 recognizes 3' overhang of pre-miRNA\"\nis_a: GO:0003676 ! nucleic acid binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003723",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 28242-28268",
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
  "excerpt": "[Term]\nid: GO:0008316\nname: structural constituent of vitelline membrane\nnamespace: molecular_function\ndef: \"The action of a molecule that contributes to the structural integrity of the vitelline membrane of an egg. An example of this is found in Drosophila melanogaster.\" [GOC:mah, GOC:sensu]\nis_a: GO:0005198 ! structural molecule activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008316",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 81960-81966",
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
  "excerpt": "[Term]\nid: GO:0042903\nname: tubulin deacetylase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: N-acetyl(alpha-tubulin) + H2O = alpha-tubulin + acetate.\" [PMID:12024216, PMID:12486003]\nxref: Reactome:R-HSA-5618331 \"HDAC6 deacetylates microtubules\"\nis_a: GO:0016811 ! hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds, in linear amides\nis_a: GO:0033558 ! protein lysine deacetylase activity\nproperty_value: skos:broadMatch EC:3.5.1.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0042903",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 242076-242085",
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
  "excerpt": "[Term]\nid: GO:0140359\nname: ABC-type transporter activity\nnamespace: molecular_function\ndef: \"Primary active transporter characterized by two nucleotide-binding domains and two transmembrane domains. Uses the energy generated from ATP hydrolysis to drive the transport of a substance across a membrane.\" [PMID:26517899]\nsynonym: \"ABC transporter\" EXACT []\nsynonym: \"ABC-type efflux permease activity\" EXACT []\nsynonym: \"ABC-type efflux porter activity\" EXACT []\nsynonym: \"ABC-type transmembrane transporter activity\" EXACT []\nsynonym: \"ABC-type uptake permease activity\" EXACT []\nsynonym: \"ATP binding cassette transporter\" EXACT []\nsynonym: \"ATP-binding cassette (ABC) transporter activity\" EXACT []\nsynonym: \"ATP-binding cassette transporter\" EXACT []\nxref: Reactome:R-HSA-266070 \"LTC4 is exported from the cytosol by ABCC1\"\nxref: Reactome:R-HSA-429157 \"ABCC4 accumulation of dense granule contents\"\nxref: Reactome:R-HSA-5362459 \"VCP-catalyzed ATP hydrolysis promotes the translocation of Hh-C into the cytosol\"\nxref: Reactome:R-HSA-5387389 \"Hh processing variants are translocated to the cytosol in a VCP-dependent manner\"\nxref: Reactome:R-HSA-9661405 \"ABCC1 transports BIL from cytosol to extracellular region (blood)\"\nxref: Reactome:R-HSA-9750656 \"ABCC2, ABCC3 transport salicylate metabolites from cytosol to extracellular region of hepatic cells\"\nxref: TC:3.A.1\nxref: Wikipedia:ATP-binding_cassette_transporter\nis_a: GO:0042626 ! ATPase-coupled transmembrane transporter activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0140359",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 439730-439752",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 148. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
