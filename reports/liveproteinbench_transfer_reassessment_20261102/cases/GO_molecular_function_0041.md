# GO_molecular_function_0041

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0041.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **A** — acyltransferase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEPSKMEVKIISSETIKPSSPTPSHLRKYTLSLLDQKYTPIVVPAILFYERPQGVAPLDMDRLRTCLSQTLTAFYPLAGRAESRDVIICNDEGIPFVEAHVDCELSSVVKSLSSLGSDLRSFYPPRDGLLEGGIQFAIQMNVFSCGGFAFAWYCTHNVTDGTSTANFFRYWTALYAQRSEYAVQDLMDFNSVVTAFPPVPPRVPQEEKPVTTELKPEKQEGQEKEEKKKSSFNFSFQSHIVARSFLIKSKAVAELKAKSVSEEVPYPSRFEAVSAFLWKSIVSSSTTEGKTMINMPVNLRPRVDPPLPLDSVGNIFENALVQSEKKAELHEFVARIRGSISKMKDFATEYQGEKREEAKDAHWKRFIKAVIECKGKDAYVISPWYKSSGFTDIDFGFGTPIRVVPMDDVVNHNQRNTIMLMEFVDSDGDGFEAWMFLEEECIKFLESNPEFLAFASPNF

[Multiple Choices]
A. acyltransferase activity
B. ADP-ribosylarginine hydrolase activity
C. ubiquitin protein ligase activity
D. catalytic activity
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

> The supplied source records match the sequence and report an acyltransferase function and acyl-transfer reaction, with experimental evidence attributed to a publication. This supports choice A; catalytic activity (D) is a broader description.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble plant BAHD-like acyltransferase: its enzyme-sized architecture and conserved-region pattern, including a DFGFG-like segment, support that family-level inference. BAHD-family proteins transfer acyl groups, making A meaningfully more specific than generic catalytic activity (D), and unlike the unrelated hydrolase and ubiquitin-ligase functions in B and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable family recognition and sequence-pattern knowledge provide a credible basis for choosing acyltransferase activity without recalling this exact protein's annotation. The inference is not proof of its particular substrate or reaction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D is broadly true of an enzyme, but A is the more informative and specific description of its molecular function, as the question requests.


### Important caveats

- The family-level inference supports the offered broad activity, not the precise substrate or physiological reaction.
- The exact author source snapshot is unknown; the reviewer evidence includes sequence-matched archived and current records.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble plant BAHD-like acyltransferase: its enzyme-sized architecture and conserved-region pattern, including a DFGFG-like segment, support that family-level inference. BAHD-family proteins transfer acyl groups, making A meaningfully more specific than generic catalytic activity (D), and unlike the unrelated hydrolase and ubiquitin-ligase functions in B and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable family recognition and sequence-pattern knowledge provide a credible basis for choosing acyltransferase activity without recalling this exact protein's annotation. The inference is not proof of its particular substrate or reaction."
  },
  "case_id": "GO_molecular_function_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied source records match the sequence and report an acyltransferase function and acyl-transfer reaction, with experimental evidence attributed to a publication. This supports choice A; catalytic activity (D) is a broader description."
  },
  "important_caveats": [
    "The family-level inference supports the offered broad activity, not the precise substrate or physiological reaction.",
    "The exact author source snapshot is unknown; the reviewer evidence includes sequence-matched archived and current records."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is broadly true of an enzyme, but A is the more informative and specific description of its molecular function, as the question requests."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied source records match the sequence and report an acyltransferase function and acyl-transfer reaction, with experimental evidence attributed to a publication. This supports choice A; catalytic activity (D) is a broader description.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble plant BAHD-like acyltransferase: its enzyme-sized architecture and conserved-region pattern, including a DFGFG-like segment, support that family-level inference. BAHD-family proteins transfer acyl groups, making A meaningfully more specific than generic catalytic activity (D), and unlike the unrelated hydrolase and ubiquitin-ligase functions in B and C.",
    "missing_item_specific_fact": "",
    "reason": "Transferable family recognition and sequence-pattern knowledge provide a credible basis for choosing acyltransferase activity without recalling this exact protein's annotation. The inference is not proof of its particular substrate or reaction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D is broadly true of an enzyme, but A is the more informative and specific description of its molecular function, as the question requests."
  },
  "important_caveats": [
    "The family-level inference supports the offered broad activity, not the precise substrate or physiological reaction.",
    "The exact author source snapshot is unknown; the reviewer evidence includes sequence-matched archived and current records."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1LG41 (BAHD1_SAPOF) is experimentally characterized (ECO:0000269, PubMed:39043959) as a BAHD acyltransferase (EC 2.3.1.-) with GO:0016746 acyltransferase activity annotated by IDA. The catalytic activity involves transfer of an acetyl moiety from acetyl-CoA to a saponin acceptor, confirming acyltransferase function. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region contains a DFG/DPFG-like motif ('TDIDFGFG') and an NxxD-like motif ('NHNQRNTIMLMEFVDSDGD'), embedded in a domain architecture characteristic of the BAHD acyltransferase superfamily: a long, variable N-terminal region followed by a compact catalytic domain in the final ~200 residues. BAHD acyltransferases are one of the largest and best-characterized plant enzyme families (hundreds of members, EC 2.3.1.-), and the DPFG/NxxD motif pair plus the overall ~450-aa plant-protein architecture are widely recognized transferable features. BAHD members are exclusively acyltransferases, which distinguishes A from B (ADP-ribosylarginine hydrolase, EC 3.2.2.19, a glycosyl hydrolase with entirely different fold) and C (ubiquitin protein ligase, requiring RING/U-box/HECT domains absent here). Between A and D, 'catalytic activity' (GO:0003824) is the root ancestor of all enzyme MF terms; GO annotation convention and the question's 'best describes' phrasing favor the most specific applicable term, which is acyltransferase activity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The BAHD acyltransferase family is extensively characterized across plant species, and its diagnostic motifs (DPFG/DFG, NxxD, HxxDG) and domain architecture are standard knowledge in plant biochemistry. Recognizing these features from the sequence and knowing that BAHD = acyltransferase (EC 2.3.1.-) constitutes legitimate transferable inference from other proteins. The elimination of B and C relies on the absence of hydrolase or E3-ligase domain signatures, and the preference for A over D follows from the GO specificity principle.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While 'catalytic activity' (D) is a true ancestor term in the GO MF hierarchy, it is the most generic enzyme term and is never the 'best' annotation when a specific subclass is identifiable. The question asks for the option that 'best describes' the primary molecular function, which unambiguously favors the specific term (acyltransferase) over the generic parent (catalytic activity). B and C are mechanistically incompatible with the observed sequence features.


### Important caveats

- The HxxDG motif is somewhat degenerate in this sequence (appearing as AHVDCEL/AHWKR rather than a canonical HxxDG), but the DPFG-like and NxxD motifs plus overall architecture are sufficient for family assignment.
- The specific substrate (saponin acceptor) and exact EC number (2.3.1.-, not fully specified) are not inferable from sequence alone, but the question only asks for the broad GO MF category (acyltransferase vs. other classes).
- The UniProt annotation is based on experimental evidence (PubMed:39043959, Nat. Chem. Biol. 2025), lending strong support to the key.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region contains a DFG/DPFG-like motif ('TDIDFGFG') and an NxxD-like motif ('NHNQRNTIMLMEFVDSDGD'), embedded in a domain architecture characteristic of the BAHD acyltransferase superfamily: a long, variable N-terminal region followed by a compact catalytic domain in the final ~200 residues. BAHD acyltransferases are one of the largest and best-characterized plant enzyme families (hundreds of members, EC 2.3.1.-), and the DPFG/NxxD motif pair plus the overall ~450-aa plant-protein architecture are widely recognized transferable features. BAHD members are exclusively acyltransferases, which distinguishes A from B (ADP-ribosylarginine hydrolase, EC 3.2.2.19, a glycosyl hydrolase with entirely different fold) and C (ubiquitin protein ligase, requiring RING/U-box/HECT domains absent here). Between A and D, 'catalytic activity' (GO:0003824) is the root ancestor of all enzyme MF terms; GO annotation convention and the question's 'best describes' phrasing favor the most specific applicable term, which is acyltransferase activity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The BAHD acyltransferase family is extensively characterized across plant species, and its diagnostic motifs (DPFG/DFG, NxxD, HxxDG) and domain architecture are standard knowledge in plant biochemistry. Recognizing these features from the sequence and knowing that BAHD = acyltransferase (EC 2.3.1.-) constitutes legitimate transferable inference from other proteins. The elimination of B and C relies on the absence of hydrolase or E3-ligase domain signatures, and the preference for A over D follows from the GO specificity principle."
  },
  "case_id": "GO_molecular_function_0041",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1LG41 (BAHD1_SAPOF) is experimentally characterized (ECO:0000269, PubMed:39043959) as a BAHD acyltransferase (EC 2.3.1.-) with GO:0016746 acyltransferase activity annotated by IDA. The catalytic activity involves transfer of an acetyl moiety from acetyl-CoA to a saponin acceptor, confirming acyltransferase function. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The HxxDG motif is somewhat degenerate in this sequence (appearing as AHVDCEL/AHWKR rather than a canonical HxxDG), but the DPFG-like and NxxD motifs plus overall architecture are sufficient for family assignment.",
    "The specific substrate (saponin acceptor) and exact EC number (2.3.1.-, not fully specified) are not inferable from sequence alone, but the question only asks for the broad GO MF category (acyltransferase vs. other classes).",
    "The UniProt annotation is based on experimental evidence (PubMed:39043959, Nat. Chem. Biol. 2025), lending strong support to the key."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While 'catalytic activity' (D) is a true ancestor term in the GO MF hierarchy, it is the most generic enzyme term and is never the 'best' annotation when a specific subclass is identifiable. The question asks for the option that 'best describes' the primary molecular function, which unambiguously favors the specific term (acyltransferase) over the generic parent (catalytic activity). B and C are mechanistically incompatible with the observed sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0041",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1LG41 (BAHD1_SAPOF) is experimentally characterized (ECO:0000269, PubMed:39043959) as a BAHD acyltransferase (EC 2.3.1.-) with GO:0016746 acyltransferase activity annotated by IDA. The catalytic activity involves transfer of an acetyl moiety from acetyl-CoA to a saponin acceptor, confirming acyltransferase function. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region contains a DFG/DPFG-like motif ('TDIDFGFG') and an NxxD-like motif ('NHNQRNTIMLMEFVDSDGD'), embedded in a domain architecture characteristic of the BAHD acyltransferase superfamily: a long, variable N-terminal region followed by a compact catalytic domain in the final ~200 residues. BAHD acyltransferases are one of the largest and best-characterized plant enzyme families (hundreds of members, EC 2.3.1.-), and the DPFG/NxxD motif pair plus the overall ~450-aa plant-protein architecture are widely recognized transferable features. BAHD members are exclusively acyltransferases, which distinguishes A from B (ADP-ribosylarginine hydrolase, EC 3.2.2.19, a glycosyl hydrolase with entirely different fold) and C (ubiquitin protein ligase, requiring RING/U-box/HECT domains absent here). Between A and D, 'catalytic activity' (GO:0003824) is the root ancestor of all enzyme MF terms; GO annotation convention and the question's 'best describes' phrasing favor the most specific applicable term, which is acyltransferase activity.",
    "missing_item_specific_fact": "",
    "reason": "The BAHD acyltransferase family is extensively characterized across plant species, and its diagnostic motifs (DPFG/DFG, NxxD, HxxDG) and domain architecture are standard knowledge in plant biochemistry. Recognizing these features from the sequence and knowing that BAHD = acyltransferase (EC 2.3.1.-) constitutes legitimate transferable inference from other proteins. The elimination of B and C relies on the absence of hydrolase or E3-ligase domain signatures, and the preference for A over D follows from the GO specificity principle."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While 'catalytic activity' (D) is a true ancestor term in the GO MF hierarchy, it is the most generic enzyme term and is never the 'best' annotation when a specific subclass is identifiable. The question asks for the option that 'best describes' the primary molecular function, which unambiguously favors the specific term (acyltransferase) over the generic parent (catalytic activity). B and C are mechanistically incompatible with the observed sequence features."
  },
  "important_caveats": [
    "The HxxDG motif is somewhat degenerate in this sequence (appearing as AHVDCEL/AHWKR rather than a canonical HxxDG), but the DPFG-like and NxxD motifs plus overall architecture are sufficient for family assignment.",
    "The specific substrate (saponin acceptor) and exact EC number (2.3.1.-, not fully specified) are not inferable from sequence alone, but the question only asks for the broad GO MF category (acyltransferase vs. other classes).",
    "The UniProt annotation is based on experimental evidence (PubMed:39043959, Nat. Chem. Biol. 2025), lending strong support to the key."
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
  "benchmark_sequence_length": 459,
  "benchmark_sequence_sha256": "26ed0fa20fc132fc6d2a47c811d0cd8d71f191da088736328b12b747d0946563",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 459,
  "current_source_sequence_sha256": "26ed0fa20fc132fc6d2a47c811d0cd8d71f191da088736328b12b747d0946563",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AAW1LG41",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3",
  "selected_historical_source_sequence_length": 459,
  "selected_historical_source_sequence_sha256": "26ed0fa20fc132fc6d2a47c811d0cd8d71f191da088736328b12b747d0946563",
  "selected_historical_version": {
    "accession": "A0AAW1LG41",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BAHD1_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1LG41\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"BAHD acyltransferase 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoBAHD1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). An acyltransferase that catalyzes the transfer of an acyl moiety to QA-triF(Q)RXX to produce saponarioside B (PubMed:39043959)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:85068\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"name\":\"3-O-{beta-D-Xyl-(1->3)-[beta-D-Gal-(1->2)]-beta-D-GlcA}-quillaic acid {beta-D-Xyl-(1->3)-beta-D-Xyl-(1->4)-alpha-L-Rha-(1->2)-[beta-D-Qui-(1->4)]-beta-D-Fuc} ester + acetyl-CoA = saponarioside B + CoA\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:85067\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:234162\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:234165\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"id\":\"GO:0016746\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:acyltransferase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/6",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48159.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:39.588231+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4b43524e63ed1da72c02309ad27ffc883b243d7c3e81fac6494633cb2601b4f3",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1LG41.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   BAHD1_SAPOF             Reviewed;         459 AA.\nAC   A0AAW1LG41;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=BAHD acyltransferase 1 {ECO:0000303|PubMed:39043959};\nDE            Short=SoBAHD1 {ECO:0000303|PubMed:39043959};\nDE            EC=2.3.1.- {ECO:0000269|PubMed:39043959};\nGN   Name=BAHD1 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11017477m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_04G021000 {ECO:0000312|EMBL:KAK9732775.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:42.902980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3",
  "url": "https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48159.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:42.902980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3",
  "url": "https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.\nCC       saponarioside A and saponarioside B) biosynthetic pathway, leading to\nCC       the production of natural products with detergent properties used as\nCC       traditional sources of soap (PubMed:39043959). An acyltransferase that\nCC       catalyzes the transfer of an acyl moiety to QA-triF(Q)RXX to produce\nCC       saponarioside B (PubMed:39043959). {ECO:0000269|PubMed:39043959}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:42.902980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3",
  "url": "https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=3-O-{beta-D-Xyl-(1->3)-[beta-D-Gal-(1->2)]-beta-D-GlcA}-\nCC         quillaic acid {beta-D-Xyl-(1->3)-beta-D-Xyl-(1->4)-alpha-L-Rha-\nCC         (1->2)-[beta-D-Qui-(1->4)]-beta-D-Fuc} ester + acetyl-CoA =\nCC         saponarioside B + CoA; Xref=Rhea:RHEA:85067, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:57288, ChEBI:CHEBI:234162, ChEBI:CHEBI:234165;\nCC         Evidence={ECO:0000269|PubMed:39043959};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:85068;\nCC         Evidence={ECO:0000269|PubMed:39043959};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:42.902980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3",
  "url": "https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0016746; F:acyltransferase activity; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:42.902980+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 71-71",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1763f34a6b1ea1393727d13c5c9259bfcd95f16e9b472412e8dd15cf063ba7d3",
  "url": "https://rest.uniprot.org/unisave/A0AAW1LG41?format=txt&versions=5"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0003824\nname: catalytic activity\nnamespace: molecular_function\ndef: \"Catalysis of a biochemical reaction at physiological temperatures. In biologically catalyzed reactions, the reactants are known as substrates, and the catalysts are naturally occurring macromolecular substances known as enzymes. Enzymes possess specific binding sites for substrates, and are usually composed wholly or largely of protein, but RNA that has catalytic activity (ribozyme) is often also regarded as enzymatic.\" [GOC:vw, ISBN:0198506732]\nsubset: goslim_agr\nsubset: goslim_chembl\nsubset: goslim_euk_cellular_processes_ribbon\nsubset: goslim_flybase_ribbon\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_plant_ribbon\nsubset: goslim_prokaryote_ribbon\nsynonym: \"enzyme activity\" EXACT [GOC:dph, GOC:tb]\nxref: Wikipedia:Enzyme\nis_a: GO:0003674 ! molecular_function\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003824",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 29250-29268",
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
  "excerpt": "[Term]\nid: GO:0003875\nname: ADP-ribosylarginine-[protein] hydrolase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reactions: H2O + N(omega)-(ADP-D-ribosyl)-L-arginyl-[protein] = ADP-D-ribose + L-arginyl-[protein], and H2O + N(omega)-(ADP-D-ribosyl)-L-arginine = ADP-D-ribose + L-arginine.\" [EC:3.2.2.19]\nsynonym: \"ADP-ribose-L-arginine cleavage enzyme activity\" RELATED [EC:3.2.2.19]\nsynonym: \"ADP-ribose-L-arginine cleaving enzyme activity\" RELATED [EC:3.2.2.19]\nsynonym: \"ADP-ribosylarginine hydrolase activity\" EXACT []\nsynonym: \"ADPribosylarginine hydrolase activity\" EXACT []\nsynonym: \"N(omega)-(ADP-D-ribosyl)-L-arginine ADP-ribosylhydrolase activity\" RELATED [EC:3.2.2.19]\nsynonym: \"nomega-(ADP-D-ribosyl)-L-arginine ADP-ribosylhydrolase activity\" RELATED [EC:3.2.2.19]\nsynonym: \"omega-protein-N-(ADP-D-ribosyl)-L-arginine ADP-ribosylhydrolase activity\" RELATED [EC:3.2.2.19]\nsynonym: \"protein ADP-ribosylarginine hydrolase activity\" RELATED [EC:3.2.2.19]\nsynonym: \"protein-nomega-(ADP-D-ribosyl)-L-arginine ADP-ribosylhydrolase activity\" RELATED [EC:3.2.2.19]\nxref: EC:3.2.2.19\nxref: MetaCyc:3.2.2.24-RXN\nxref: MetaCyc:ADP-RIBOSYLARGININE-HYDROLASE-RXN\nxref: MetaCyc:RXN-8732\nxref: RHEA:14493\nxref: RHEA:14885\nxref: RHEA:20784\nis_a: GO:0016799 ! hydrolase activity, hydrolyzing N-glycosyl compounds\nis_a: GO:0140096 ! catalytic activity, acting on a protein\nproperty_value: skos:exactMatch EC:3.2.2.19\nproperty_value: skos:narrowMatch MetaCyc:3.2.2.24-RXN\nproperty_value: skos:narrowMatch MetaCyc:ADP-RIBOSYLARGININE-HYDROLASE-RXN\nproperty_value: skos:narrowMatch MetaCyc:RXN-8732\nproperty_value: skos:narrowMatch RHEA:14493\nproperty_value: skos:narrowMatch RHEA:14885\nproperty_value: skos:narrowMatch RHEA:20784\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0003875",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 30576-30606",
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
  "excerpt": "[Term]\nid: GO:0016740\nname: transferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a group, e.g. a methyl group, glycosyl group, acyl group, phosphorus-containing, or other groups, from one compound (generally regarded as the donor) to another compound (generally regarded as the acceptor). Transferase is the systematic name for any enzyme of EC class 2.\" [EC:2.-.-.-]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_prokaryote\nsubset: goslim_yeast\nxref: EC:2.-.-.-\nxref: Reactome:R-HSA-1483089 \"PE is converted to PS by PTDSS2\"\nxref: Reactome:R-HSA-1483186 \"PC is converted to PS by PTDSS1\"\nxref: Reactome:R-HSA-5333607 \"GSSeH combines with bGalNAc derivative to form GSSebGalNac\"\nxref: Reactome:R-HSA-5668414 \"TRAF2 ubiquitinates cIAP1,2 in cIAP1,2:TRAF1:TRAF2:TRAF3:NIK\"\nxref: Reactome:R-HSA-8868783 \"TSR3 transfers aminocarboxypropyl group from S-adenosylmethionine to N(1)-methylpseudouridine-1248 of 18SE rRNA yielding N(1)-methyl-N(3)-aminocarboxypropylpseudouridine-1248\"\nis_a: GO:0003824 ! catalytic activity\nproperty_value: skos:exactMatch EC:2.-.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016740",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 129652-129675",
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
  "excerpt": "[Term]\nid: GO:0016746\nname: acyltransferase activity\nnamespace: molecular_function\nalt_id: GO:0008415\ndef: \"Catalysis of the transfer of an acyl group from one compound (donor) to another (acceptor).\" [EC:2.3.-.-]\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsynonym: \"transferase activity, transferring acyl groups\" EXACT []\nxref: EC:2.3.-.-\nxref: Reactome:R-HSA-159431 \"Cytosolic chenodeoxycholoyl-CoA or choloyl-CoA are conjugated with glycine or taurine\"\nxref: Reactome:R-HSA-192312 \"Choloyl CoA reacts with glycine or taurine to form glycocholate or taurocholate\"\nxref: Reactome:R-HSA-193491 \"Chenodeoxycholoyl CoA reacts with glycine or taurine to form glycochenodeoxycholate or taurochenodeoxycholate\"\nxref: Reactome:R-HSA-8858298 \"HRASLS transfer acyl group from PC to PE to form NAPE\"\nis_a: GO:0016740 ! transferase activity\nproperty_value: skos:exactMatch EC:2.3.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016746",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 129716-129732",
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
  "excerpt": "[Term]\nid: GO:0061630\nname: ubiquitin protein ligase activity\nnamespace: molecular_function\nalt_id: GO:0090302\nalt_id: GO:0090622\nalt_id: GO:1904264\nalt_id: GO:1904822\ndef: \"Catalysis of the transfer of ubiquitin to a substrate protein via the reaction X-ubiquitin + S = X + S-ubiquitin, where X is either an E2 or E3 enzyme, the X-ubiquitin linkage is a thioester bond, and the S-ubiquitin linkage is an amide bond: an isopeptide bond between the C-terminal glycine of ubiquitin and the epsilon-amino group of lysine residues in the substrate or, in the linear extension of ubiquitin chains, a peptide bond the between the C-terminal glycine and N-terminal methionine of ubiquitin residues.\" [GOC:BioGRID, GOC:dph, GOC:mah, GOC:tb, PMID:22863777]\ncomment: This enzyme catalyzes a transferase reaction.\nsynonym: \"E3\" BROAD [GOC:dph]\nsynonym: \"ER-associated E3 ligase\" RELATED [PMID:24019521]\nsynonym: \"protein ubiquitination activity\" EXACT [GOC:dph]\nsynonym: \"ubiquitin ligase activity\" EXACT [GOC:dph]\nxref: EC:2.3.2.26\nxref: EC:2.3.2.27\nxref: EC:2.3.2.31\nxref: EC:2.3.2.33\nxref: EC:2.3.2.36\nxref: Reactome:R-HSA-1225956 \"Inefficient ubiquitination of ligand-responsive p-6Y-EGFR mutants by p-Y371-CBL\"\nxref: Reactome:R-HSA-1504190 \"DVL is ubiquitinated by CUL3:KLHL12:RBX1\"\nxref: Reactome:R-HSA-183036 \"Ubiquitination of stimulated EGFR (CBL:GRB2)\"\nxref: Reactome:R-HSA-201445 \"Ubiquitin-dependent degradation controls basal levels of R-Smad1/5/8\"\nxref: Reactome:R-HSA-3322429 \"XIAP monoubiquinates TLE\"\nxref: Reactome:R-HSA-3640861 \"RNF146 ubiquitinates ADP-ribosylated AXIN\"\nxref: Reactome:R-HSA-4608852 \"SMURF1/2 ubiquitinates PRICKLE1\"\nxref: Reactome:R-HSA-4641129 \"AXIN is ubiquitinated by SMURF2\"\nxref: Reactome:R-HSA-4641159 \"DVL1 is ubiquitinated by HECW1\"\nxref: Reactome:R-HSA-4641246 \"ZNRF3 autoubiquitinates to promote its internalization\"\nxref: Reactome:R-HSA-4641253 \"ZNRF3 ubiquitinates FZD to promote its downregulation\"\nxref: Reactome:R-HSA-5246693 \"APC is K63-polyubiquitinated\"\nxref: Reactome:R-HSA-5610737 \"NUMB:ITCH bind and ubiquitnate GLI1\"\nxref: Reactome:R-HSA-5632648 \"SMURF1/2 ubiquitinates PTCH1\"\nxref: Reactome:R-HSA-5635856 \"SPOP:CUL3:RBX1 ubiquitinates GLI2,3\"\nxref: Reactome:R-HSA-5635864 \"NUMB:ITCH ubiquitinates GLI1\"\nxref: Reactome:R-HSA-5654672 \"CBL ubiquitinates FRS2 and FGFR1\"\nxref: Reactome:R-HSA-5654677 \"CBL ubiquitinates FRS2 and FGFR2\"\nxref: Reactome:R-HSA-5654679 \"CBL ubiquitinates FRS2 and FGFR3\"\nxref: Reactome:R-HSA-5654684 \"CBL ubiquitinates FRS2 and FGFR4\"\nxref: Reactome:R-HSA-5658424 \"KBTBD7:CUL3:RBX1 ubiquitinates NF1\"\nxref: Reactome:R-HSA-5674022 \"BRAP autoubiquitinates\"\nxref: Reactome:R-HSA-5682858 \"RNF8 and RNF168 ubiquitinate H2AFX\"\nxref: Reactome:R-HSA-5684071 \"RNF4 ubiquitinates MDC1\"\nxref: Reactome:R-HSA-5687081 \"MAPK6 is ubiquitinated at the N-terminal\"\nxref: Reactome:R-HSA-5689111 \"PARK2 autoubiquitinates\"\nxref: Reactome:R-HSA-5690827 \"TNFAIP3 (A20) ubiquitinates RIPK1\"\nxref: Reactome:R-HSA-6781867 \"ERCC8:DDB1:CUL4:RBX1 ubiquitinates ERCC6 and RNA Pol II\"\nxref: Reactome:R-HSA-6782943 \"UV-DDB ubiquitinates XPC\"\nxref: Reactome:R-HSA-6785361 \"Monoubiquitination of FANCD2:FANCI\"\nxref: Reactome:R-HSA-6790487 \"RNF111 ubiquitinates SUMOylated XPC\"\nxref: Reactome:R-HSA-6798373 \"MDM2 ubiquitinates DYRK2\"\nxref: Reactome:R-HSA-6804253 \"MDM2 ubiquitinates JMY\"\nxref: Reactome:R-HSA-6804441 \"RNF34 or RFFL ubiquitinates phosphorylated TP53\"\nxref: Reactome:R-HSA-6804724 \"MDM2 ubiquitinates phosphorylated MDM4\"\nxref: Reactome:R-HSA-6804879 \"MDM2 ubiquitinates TP53\"\nxref: Reactome:R-HSA-6804942 \"MDM2 homodimers auto-ubiquitinate\"\nxref: Reactome:R-HSA-6807106 \"PTEN undergoes monoubiquitination\"\nxref: Reactome:R-HSA-6807134 \"NEDD4, WWP2, CHIP and XIAP polyubiquitinate PTEN\"\nxref: Reactome:R-HSA-68946 \"Phosphorylated Orc1 is ubiquitinated while still associated with chromatin\"\nxref: Reactome:R-HSA-69015 \"Cytoplasmic phosphorylated Cdc6 is ubiquitinated by the anaphase-promoting complex\"\nxref: Reactome:R-HSA-8848829 \"CBL autoubiquitinates\"\nxref: Reactome:R-HSA-8851011 \"TRIM27 polyubiquitinates PTEN\"\nxref: Reactome:R-HSA-8854041 \"SCF-FBXL7 ubiquitinates AURKA\"\nxref: Reactome:R-HSA-8854051 \"SCF-FBXL18 ubiquitinates FBXL7\"\nxref: Reactome:R-HSA-8854628 \"MYLIP dimer ubiquitinates VLDLR on Lys-839\"\nxref: Reactome:R-HSA-8866546 \"RNF5 and RNF185 ubiquitinate misfolded CFTR\"\nxref: Reactome:R-HSA-8866856 \"RNF5 and RNF185 ubiquitinate CFTR F508del\"\nxref: Reactome:R-HSA-8867288 \"OS9:SEL1:ERAD E3 ligase:DERL2 ubiquitinates unfolded protein:(GlcNAc)2 (Man)9-5\"\nxref: Reactome:R-HSA-8875183 \"CBL monoubiquitinates activated MET\"\nxref: Reactome:R-HSA-8875431 \"LRIG1 undergoes ubiquitination\"\nxref: Reactome:R-HSA-8876258 \"CBL monoubiquitinates InlB-bound MET\"\nxref: Reactome:R-HSA-8877003 \"CBLL1 ubiqutinates the InlA-bound CDH1 complex\"\nxref: Reactome:R-HSA-8938773 \"RNF144A polyubiquitinates PRKDC\"\nxref: Reactome:R-HSA-8938815 \"RNF152 polyubiquitinates RRAGA\"\nxref: Reactome:R-HSA-8939335 \"RNF181 polyubiquinates BCL10\"\nxref: Reactome:R-HSA-8939706 \"SCF(SKP2) polyubiquitinates RUNX2\"\nxref: Reactome:R-HSA-8942101 \"RNF20:RNF40 monoubiquitinates Histone H2B\"\nxref: Reactome:R-HSA-8943003 \"SHPRH polyubiquitinates monoubiquitinated PCNA\"\nxref: Reactome:R-HSA-8943040 \"HLTF polyubiquitinates monoubiquitinated PCNA\"\nxref: Reactome:R-HSA-8943080 \"TMEM129 polyubiquitinates HLA (MHC class I heavy chain) bound to cytomegalovirus US11\"\nxref: Reactome:R-HSA-8948775 \"MKRN1 polyubiquitinates PTEN\"\nxref: Reactome:R-HSA-8948832 \"RNF146 polyubiquitinates PARylated PTEN\"\nxref: Reactome:R-HSA-8952382 \"MDM2 polyubiquitinates RUNX3\"\nxref: Reactome:R-HSA-8952419 \"SMURFs ubiquitinate RUNX3\"\nxref: Reactome:R-HSA-8953946 \"PEX2:PEX10:PEX12 monoubiquitinates PEX5S,L at cysteine-11\"\nxref: Reactome:R-HSA-8956026 \"CUL9:RBX1 ubiquitinates BIRC5\"\nxref: Reactome:R-HSA-8956684 \"ITCH polyubiquitinates TP73\"\nxref: Reactome:R-HSA-9008076 \"WWP1 polyubiquitinates RUNX2\"\nxref: Reactome:R-HSA-9009308 \"STUB1 polyubiquitinates RUNX2\"\nxref: Reactome:R-HSA-9009403 \"SMURF1 polyubiquitinates RUNX2\"\nxref: Reactome:R-HSA-9011300 \"ZSWIM8 ubiquitinates ROBO3.1\"\nxref: Reactome:R-HSA-9021523 \"WWP2 ubiquitinates NOTCH3\"\nxref: Reactome:R-HSA-9033485 \"PEX2:PEX10:PEX12 monoubiquitinates PEX5L at cysteine-11\"\nxref: Reactome:R-HSA-934604 \"Phosphorylated SPRY2 is ubiquitinated by CBL\"\nxref: Reactome:R-HSA-936462 \"PIN1 mediated IRF3 degradation\"\nxref: Reactome:R-HSA-936475 \"Negative regulation of DDX58/IFIH1 signaling by RNF216\"\nxref: Reactome:R-HSA-9604629 \"FBXW7 promotes ubiquitination of p-NICD4\"\nxref: Reactome:R-HSA-9685195 \"SARS-CoV-1 9b recruits ITCH to MAVS\"\nxref: Reactome:R-HSA-9686920 \"PELI1 ubiquitinates RIPK3 at K363\"\nxref: Reactome:R-HSA-9686969 \"APC/C:Cdh1 polyubiquitinates SKP2\"\nxref: Reactome:R-HSA-9705738 \"SOCS1,3 ubiquitinates CSF3R in SOCS1,3:p-4Y-CSF3R:CSF3 dimer:LYN:p-Y-JAK1:p-JAK2:p-SYK:p-HCK:p-TYK2:CUL5:ELOB:ELOC:RNF7\"\nxref: Reactome:R-HSA-9706354 \"Ubiquitination of FLT3\"\nxref: Reactome:R-HSA-9706356 \"CBL mutants don't ubiquitinate FLT3\"\nxref: Reactome:R-HSA-9708517 \"FBXL17 ubiquitinates BACH1 (in BACH1:FBXL17:SCF (SKP2))\"\nxref: Reactome:R-HSA-9733316 \"p-Y-CBL autoubiquitinates and multiubiquitinates p-Y561-CSF1R in CSF1 dimer:p-Y561-CSF1R dimer:p-Y-CBL\"\nxref: Reactome:R-HSA-9755304 \"MUL1 ubiquitinates UBXN7\"\nxref: Reactome:R-HSA-9755505 \"KEAP1:NEDD8-CUL3:RBX1 complex ubiquitinates NFE2L2\"\nxref: Reactome:R-HSA-9759154 \"TRIM21 ubiquitinates SQSTM1\"\nxref: Reactome:R-HSA-9759172 \"KEAP1:CUL3:RBX1 ubiquitinates p-S349 SQSTM1 oligomer\"\nxref: Reactome:R-HSA-9762091 \"NFE2L2 is ubiquitinated by BTRC:SKP1:CUL1:RBX1\"\nxref: Reactome:R-HSA-9766645 \"CUL3:RBX1 ubiquitinates KEAP1\"\nxref: Reactome:R-HSA-990526 \"Recruitment of ITCH and K48 ubiquitination of MAVS\"\nxref: Reactome:R-HSA-9929490 \"CD274 ubiquitination by SPOP:CUL3:RBX1 complex\"\nxref: Reactome:R-HSA-9931298 \"Ubiquitination of CD274 by ERAD complex\"\nxref: Reactome:R-HSA-9931430 \"MIB2-mediated K63-ubiquitination of CD274\"\nxref: Reactome:R-HSA-9932510 \"BTRC:CUL1:SKP1:RBX1 (SCF-beta-TrCP1) ubiquitinylates phosphorylated PER1,2,3\"\nxref: Reactome:R-HSA-9932512 \"FBXL3:CUL1:SKP1:RBX1 ubiquitinylates phosphorylated CRY1,2\"\nxref: Reactome:R-HSA-9945766 \"NS3 is ubiquitinated\"\nxref: Reactome:R-HSA-9946390 \"NS1 dimer is ubiquitinated\"\nxref: Reactome:R-HSA-9948362 \"LTN1 K48 polyubiquitinates the nascent peptide in NEMF:60S ribosomal subunit:peptidyl-tRNA with nascent peptide\"\nxref: Reactome:R-HSA-9954737 \"RCHY1 K48 polyubiquitinates alanine-tailed nascent peptide\"\nis_a: GO:0004842 ! ubiquitin-protein transferase activity\nis_a: GO:0061659 ! ubiquitin-like protein ligase activity\nproperty_value: skos:narrowMatch EC:2.3.2.26\nproperty_value: skos:narrowMatch EC:2.3.2.27\nproperty_value: skos:narrowMatch EC:2.3.2.31\nproperty_value: skos:narrowMatch EC:2.3.2.33\nproperty_value: skos:narrowMatch EC:2.3.2.36\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0061630",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 358126-358254",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 41. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
