# GO_molecular_function_0156

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0156.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — ABC-type transporter activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTTLDLTARSDRGRVYWLLADCWNIVRRGLTHYQRQPVNIAWQLGFPILSVLLYGYVFGSAMKVPGGGDYKDFLMPGMFVMTMAFGFINTATLVVYDSTKGVIDRFRSMPMASSAVVAGRGVTDLITACAELAIMMLTAFAMGWRPDGGLGFLGAFGLLLWLRFALIWIGVWLGLLVPNPEAAGGLFAVAFPLTMISSIMVAPQLMPDWLGWVAMWNPISSTAAATRELFGTPVGGDTWVEQHALLMAGVWPVILTLVFLPLAVRRFKKLSR

[Multiple Choices]
A. transcription coregulator activity
B. damaged DNA binding
C. structural constituent of cell wall
D. ABC-type transporter activity
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

> The matched-sequence record identifies this protein as an ABC-transporter permease and reports a role in the DrrA2B2 complex transporting daunorubicin; it also annotates ABC-type transporter activity by InterPro. The functional report supports D, although the GO annotation itself is computational.

Citations as saved: [C1](#evidence-c1), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is strongly hydrophobic and consistent with a multipass membrane permease, unlike the soluble regulatory or DNA-binding functions in A and B or a cell-wall structural protein in C. Transferable knowledge that ABC transporters can have membrane permease subunits separate from their ATP-binding subunits makes D a credible choice even though this sequence lacks an ATP-binding domain.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Sequence architecture and knowledge of ABC transporter subunits meaningfully favor D among these alternatives. The sequence alone may not prove ABC-family membership, but the alternatives do not require distinguishing it from other membrane transporter families.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is the only offered choice consistent with a multipass membrane permease; the other options describe substantially different protein roles.


### Important caveats

- The protein is a permease component, not a complete transporter with its ATP-binding machinery in this sequence; the GO annotation is computational, while the reported transport role is associated with the transporter complex.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multipass membrane permease, unlike the soluble regulatory or DNA-binding functions in A and B or a cell-wall structural protein in C. Transferable knowledge that ABC transporters can have membrane permease subunits separate from their ATP-binding subunits makes D a credible choice even though this sequence lacks an ATP-binding domain.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Sequence architecture and knowledge of ABC transporter subunits meaningfully favor D among these alternatives. The sequence alone may not prove ABC-family membership, but the alternatives do not require distinguishing it from other membrane transporter families."
  },
  "case_id": "GO_molecular_function_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence record identifies this protein as an ABC-transporter permease and reports a role in the DrrA2B2 complex transporting daunorubicin; it also annotates ABC-type transporter activity by InterPro. The functional report supports D, although the GO annotation itself is computational."
  },
  "important_caveats": [
    "The protein is a permease component, not a complete transporter with its ATP-binding machinery in this sequence; the GO annotation is computational, while the reported transport role is associated with the transporter complex."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered choice consistent with a multipass membrane permease; the other options describe substantially different protein roles."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence record identifies this protein as an ABC-transporter permease and reports a role in the DrrA2B2 complex transporting daunorubicin; it also annotates ABC-type transporter activity by InterPro. The functional report supports D, although the GO annotation itself is computational.",
    "evidence_ids": ["C1", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is strongly hydrophobic and consistent with a multipass membrane permease, unlike the soluble regulatory or DNA-binding functions in A and B or a cell-wall structural protein in C. Transferable knowledge that ABC transporters can have membrane permease subunits separate from their ATP-binding subunits makes D a credible choice even though this sequence lacks an ATP-binding domain.",
    "missing_item_specific_fact": "",
    "reason": "Sequence architecture and knowledge of ABC transporter subunits meaningfully favor D among these alternatives. The sequence alone may not prove ABC-family membership, but the alternatives do not require distinguishing it from other membrane transporter families."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is the only offered choice consistent with a multipass membrane permease; the other options describe substantially different protein roles."
  },
  "important_caveats": [
    "The protein is a permease component, not a complete transporter with its ATP-binding machinery in this sequence; the GO annotation is computational, while the reported transport role is associated with the transporter complex."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (P0DXU6) annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB2' with GO:0140359 (ABC-type transporter activity). The functional comment cites experimental evidence (PubMed:39375957) showing it is part of the ABC transporter complex DrrA2B2 involved in daunorubicin efflux. The GO annotation itself is IEA:InterPro (computational), but the broader functional context is supported by experimental data. The sequence matches the benchmark exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [GO4](#evidence-go4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 272-residue sequence is clearly a polytopic integral membrane protein with approximately 6-8 hydrophobic transmembrane segments separated by short hydrophilic loops. This topology immediately rules out A (transcription coregulator activity: soluble nuclear proteins with protein-interaction domains, not polytopic membrane proteins) and B (damaged DNA binding: soluble proteins with DNA-binding motifs such as helix-turn-helix, zinc fingers, or positively charged patches). Between C and D: bacterial cell wall structural constituents (option C) typically possess specific cell-wall-binding domains (LysM, CHAP, SLT) or are large repetitive surface-layer proteins, none of which are present here. ABC transporter permease components are a well-known family of polytopic membrane proteins of ~200-400 residues with 6-12 TM helices that lack Walker A/B nucleotide-binding motifs (those reside in the partner NBD). The size, topology, and absence of any catalytic or DNA-binding domain are classic features of an ABC permease, a pattern extensively learned from homologs across bacterial genomes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the polytopic membrane topology, exclude DNA-binding and transcription-related functions, and use family-level knowledge of ABC permease components (size range, TM helix count, absence of NBD motifs) to select D over C. This is a standard family-recognition inference from transferable knowledge of related proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The polytopic membrane topology unambiguously eliminates A and B. The absence of cell-wall-binding domains and the classic ABC-permease size/topology profile clearly favor D over C. No two options are genuinely defensible.


### Important caveats

- The GO annotation for this entry is IEA:InterPro (computational), not a direct experimental GO annotation, though the functional role is supported by experimental evidence (PubMed:39375957).
- The GO term GO:0140359 definition describes the full ABC transporter (with NBDs and TMDs), but the term's synonyms explicitly include 'ABC-type efflux permease activity,' making it appropriate for the permease component alone.
- The reviewer-only evidence reveals the organism (Streptomyces coeruleorubidus) and protein name, but these were not available to the evaluated model; the reasoning above relies solely on sequence features and family-level transfer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 272-residue sequence is clearly a polytopic integral membrane protein with approximately 6-8 hydrophobic transmembrane segments separated by short hydrophilic loops. This topology immediately rules out A (transcription coregulator activity: soluble nuclear proteins with protein-interaction domains, not polytopic membrane proteins) and B (damaged DNA binding: soluble proteins with DNA-binding motifs such as helix-turn-helix, zinc fingers, or positively charged patches). Between C and D: bacterial cell wall structural constituents (option C) typically possess specific cell-wall-binding domains (LysM, CHAP, SLT) or are large repetitive surface-layer proteins, none of which are present here. ABC transporter permease components are a well-known family of polytopic membrane proteins of ~200-400 residues with 6-12 TM helices that lack Walker A/B nucleotide-binding motifs (those reside in the partner NBD). The size, topology, and absence of any catalytic or DNA-binding domain are classic features of an ABC permease, a pattern extensively learned from homologs across bacterial genomes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the polytopic membrane topology, exclude DNA-binding and transcription-related functions, and use family-level knowledge of ABC permease components (size range, TM helix count, absence of NBD motifs) to select D over C. This is a standard family-recognition inference from transferable knowledge of related proteins."
  },
  "case_id": "GO_molecular_function_0156",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4",
      "GO4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (P0DXU6) annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB2' with GO:0140359 (ABC-type transporter activity). The functional comment cites experimental evidence (PubMed:39375957) showing it is part of the ABC transporter complex DrrA2B2 involved in daunorubicin efflux. The GO annotation itself is IEA:InterPro (computational), but the broader functional context is supported by experimental data. The sequence matches the benchmark exactly."
  },
  "important_caveats": [
    "The GO annotation for this entry is IEA:InterPro (computational), not a direct experimental GO annotation, though the functional role is supported by experimental evidence (PubMed:39375957).",
    "The GO term GO:0140359 definition describes the full ABC transporter (with NBDs and TMDs), but the term's synonyms explicitly include 'ABC-type efflux permease activity,' making it appropriate for the permease component alone.",
    "The reviewer-only evidence reveals the organism (Streptomyces coeruleorubidus) and protein name, but these were not available to the evaluated model; the reasoning above relies solely on sequence features and family-level transfer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The polytopic membrane topology unambiguously eliminates A and B. The absence of cell-wall-binding domains and the classic ABC-permease size/topology profile clearly favor D over C. No two options are genuinely defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0156",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (P0DXU6) annotates this protein as 'Daunorubicin resistance ABC transporter permease protein DrrB2' with GO:0140359 (ABC-type transporter activity). The functional comment cites experimental evidence (PubMed:39375957) showing it is part of the ABC transporter complex DrrA2B2 involved in daunorubicin efflux. The GO annotation itself is IEA:InterPro (computational), but the broader functional context is supported by experimental data. The sequence matches the benchmark exactly.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4", "GO4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 272-residue sequence is clearly a polytopic integral membrane protein with approximately 6-8 hydrophobic transmembrane segments separated by short hydrophilic loops. This topology immediately rules out A (transcription coregulator activity: soluble nuclear proteins with protein-interaction domains, not polytopic membrane proteins) and B (damaged DNA binding: soluble proteins with DNA-binding motifs such as helix-turn-helix, zinc fingers, or positively charged patches). Between C and D: bacterial cell wall structural constituents (option C) typically possess specific cell-wall-binding domains (LysM, CHAP, SLT) or are large repetitive surface-layer proteins, none of which are present here. ABC transporter permease components are a well-known family of polytopic membrane proteins of ~200-400 residues with 6-12 TM helices that lack Walker A/B nucleotide-binding motifs (those reside in the partner NBD). The size, topology, and absence of any catalytic or DNA-binding domain are classic features of an ABC permease, a pattern extensively learned from homologs across bacterial genomes.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the polytopic membrane topology, exclude DNA-binding and transcription-related functions, and use family-level knowledge of ABC permease components (size range, TM helix count, absence of NBD motifs) to select D over C. This is a standard family-recognition inference from transferable knowledge of related proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The polytopic membrane topology unambiguously eliminates A and B. The absence of cell-wall-binding domains and the classic ABC-permease size/topology profile clearly favor D over C. No two options are genuinely defensible."
  },
  "important_caveats": [
    "The GO annotation for this entry is IEA:InterPro (computational), not a direct experimental GO annotation, though the functional role is supported by experimental evidence (PubMed:39375957).",
    "The GO term GO:0140359 definition describes the full ABC transporter (with NBDs and TMDs), but the term's synonyms explicitly include 'ABC-type efflux permease activity,' making it appropriate for the permease component alone.",
    "The reviewer-only evidence reveals the organism (Streptomyces coeruleorubidus) and protein name, but these were not available to the evaluated model; the reasoning above relies solely on sequence features and family-level transfer."
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
  "benchmark_sequence_length": 272,
  "benchmark_sequence_sha256": "59e638eb8cf60b05352d61e55cf16844ce8b914c1394940c66e4190daaf561d9",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 272,
  "current_source_sequence_sha256": "59e638eb8cf60b05352d61e55cf16844ce8b914c1394940c66e4190daaf561d9",
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
  "requested_accession": "P0DXU6",
  "selected_historical_entry_version": 4,
  "selected_historical_record_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "selected_historical_source_sequence_length": 272,
  "selected_historical_source_sequence_sha256": "59e638eb8cf60b05352d61e55cf16844ce8b914c1394940c66e4190daaf561d9",
  "selected_historical_version": {
    "accession": "P0DXU6",
    "database": "Swiss-Prot",
    "entryVersion": 4,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DRRB2_STRC4",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXU6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Actinomycetota\",\"Actinomycetes\",\"Kitasatosporales\",\"Streptomycetaceae\",\"Streptomyces\"],\"scientificName\":\"Streptomyces coeruleorubidus\",\"taxonId\":116188}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Daunorubicin resistance ABC transporter permease protein DrrB2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39375957\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Part of the ABC transporter complex DrrA2B2 involved in daunorubicin efflux (PubMed:39375957). Responsible for the translocation of the substrate across the membrane (Probable). Confers self-resistance to daunorubicin, an antibiotic produced by S.coeruleorubidus (PubMed:39375957)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0140359\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:ABC-type transporter activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/7",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXU6.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Dong J.\",\"Ning J.\",\"Tian Y.\",\"Li H.\",\"Chen H.\",\"Guan W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39375957\"},{\"database\":\"DOI\",\"id\":\"10.1111/1751-7915.70023\"}],\"citationType\":\"journal article\",\"firstPage\":\"e70023\",\"id\":\"39375957\",\"journal\":\"Microb. Biotechnol.\",\"lastPage\":\"e70023\",\"publicationDate\":\"2024\",\"title\":\"The involvement of multiple ABC transporters in daunorubicin efflux in Streptomyces coeruleorubidus.\",\"volume\":\"17\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION IN DAUNORUBICIN EFFLUX\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:29:39.151534+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4e7d0b296d64a4ffb645956bc9763e367bd0533eedf73ba35b4dc16bd7421217",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXU6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H1",
  "excerpt": "ID   DRRB2_STRC4             Reviewed;         272 AA.\nAC   P0DXU6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   28-JAN-2026, entry version 4.\nDE   RecName: Full=Daunorubicin resistance ABC transporter permease protein DrrB2 {ECO:0000305};\nGN   Name=drrB2 {ECO:0000303|PubMed:39375957};\nGN   ORFNames=R5U08_15990 {ECO:0000312|EMBL:WOT35540.1};\nOS   Streptomyces coeruleorubidus.\nOC   Bacteria; Bacillati; Actinomycetota; Actinomycetes; Kitasatosporales;\nOC   Streptomycetaceae; Streptomyces.\nOX   NCBI_TaxID=116188;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION IN DAUNORUBICIN EFFLUX, INDUCTION, AND DISRUPTION PHENOTYPE.\nRX   PubMed=39375957; DOI=10.1111/1751-7915.70023;\nRA   Dong J., Ning J., Tian Y., Li H., Chen H., Guan W.;\nRT   \"The involvement of multiple ABC transporters in daunorubicin efflux in\nRT   Streptomyces coeruleorubidus.\";\nRL   Microb. Biotechnol. 17:e70023-e70023(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Part of the ABC transporter complex DrrA2B2 involved in\nCC       daunorubicin efflux (PubMed:39375957). Responsible for the\nCC       translocation of the substrate across the membrane (Probable). Confers\nCC       self-resistance to daunorubicin, an antibiotic produced by\nCC       S.coeruleorubidus (PubMed:39375957). {ECO:0000269|PubMed:39375957,\nCC       ECO:0000305}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4)

```json
{
  "entry_version": 4,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0140359; F:ABC-type transporter activity; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:40.921406+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-55",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "372a99e71818628749a5230f6a3ea50eb4a3ab3f801909ad5a5e951310594fb7",
  "url": "https://rest.uniprot.org/unisave/P0DXU6?format=txt&versions=4"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0003684\nname: damaged DNA binding\nnamespace: molecular_function\ndef: \"Binding to damaged DNA.\" [GOC:jl]\nsynonym: \"DNA repair enzyme\" RELATED []\nsynonym: \"DNA repair protein\" RELATED []\nis_a: GO:0003677 ! DNA binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003684",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 27876-27884",
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
  "excerpt": "[Term]\nid: GO:0003712\nname: transcription coregulator activity\nnamespace: molecular_function\nalt_id: GO:0001104\nalt_id: GO:0016455\ndef: \"A transcription regulator activity that modulates the transcription of specific gene sets via binding to a DNA-binding transcription factor at a specific genomic locus, either on its own or as part of a complex. Coregulators often act by altering chromatin structure and modifications. For example, one class of transcription coregulators modifies chromatin structure through covalent modification of histones. A second class remodels the conformation of chromatin in an ATP-dependent fashion. A third class modulates interactions of DNA-bound DNA-binding transcription factors with other transcription coregulators.\" [GOC:txnOH-2018, PMID:10213677, PMID:16858867, PMID:24203923, PMID:25957681, Wikipedia:Transcription_coregulator]\ncomment: Usage guidance: Most transcription coregulators do not bind DNA. Those that do usually bind DNA either in a non-specific or non-direct manner. If a protein binds DNA specifically, consider annotating to GO:0003700 DNA binding transcription factor activity.\nsubset: goslim_drosophila\nsynonym: \"nuclear receptor coreceptor activity\" NARROW []\nsynonym: \"RNA polymerase II transcriptional cofactor activity\" RELATED []\nsynonym: \"transcription cofactor activity\" EXACT []\nsynonym: \"transcription coreceptor activity\" EXACT []\nsynonym: \"transcriptional co-regulator\" EXACT []\nxref: Reactome:R-HSA-5340251 \"NR1H4:DCA,CDCA,LCHA binds RXRA and NCOA1,2\"\nis_a: GO:0140110 ! transcription regulator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003712",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 28124-28140",
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
  "excerpt": "[Term]\nid: GO:0005199\nname: structural constituent of cell wall\nnamespace: molecular_function\ndef: \"The action of a molecule that contributes to the structural integrity of a cell wall.\" [GOC:mah]\nis_a: GO:0005198 ! structural molecule activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005199",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 54695-54701",
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 156. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
