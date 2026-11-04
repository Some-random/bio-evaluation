# active_site_0082

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0082.txt)

**Task:** `active_site`  
**Expected answer:** **C** — Position 254 (Proton acceptor)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
METVQSSSSAELLRAQTHFSTQLFSFQNYASLKCALHLGIPDAIKQHGKPMNLSELTSALPIKPSKAPYIHRLMRMLVKAGYFAQENECFDLTPIGLLLLKDDPINIRALVLLELHPALLLPWIALSEWFQNDDATPFVTAHGKSFWDYTSRDPEFRKLFDEAMAGDSELISKVLVTEFKYVFEGLKSLVDVGGGNGTLARSIAKAFPNLKCTVFDLPEAVANEQGDGNLDFVAGDMFDRVPSADAILLKIVLHDWSDENCVKILKNCRKSIPVKDKGGKVIIIEGVVELEKNAGNEYAGLENLDMEMLVLYNSKERTKKEWAKLFSDAGFSDYKFIPALDSWCIIELTP

[Multiple Choices]
A. Position 280 (Proton acceptor)
B. Position 1134 (Proton donor; for dehydratase activity)
C. Position 254 (Proton acceptor)
D. Position 2475 (For beta-ketoacyl synthase 2 activity)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates position 254 as a proton acceptor, based on a PROSITE-ProRule computational annotation. This supports the key, though it is not direct experimental evidence for that residue's role.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 350-residue sequence has a glycine-rich region consistent with SAM binding in a small-molecule methyltransferase, and position 254 is histidine. In plant O-methyltransferase family patterns, a conserved histidine can act as the catalytic proton-accepting base. This makes option C a credible family-level inference; options B and D give positions beyond the sequence length.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable O-methyltransferase family knowledge and sequence features meaningfully favor the histidine at position 254 over the offered alternatives. This is a plausible inference, not a guarantee of the residue's experimentally measured role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence length rules out options B and D, while the family-level catalytic-base inference favors C over A.


### Important caveats

- The supplied reviewer evidence supports the position through a computational PROSITE-ProRule annotation, not a cited direct experiment on this residue.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 350-residue sequence has a glycine-rich region consistent with SAM binding in a small-molecule methyltransferase, and position 254 is histidine. In plant O-methyltransferase family patterns, a conserved histidine can act as the catalytic proton-accepting base. This makes option C a credible family-level inference; options B and D give positions beyond the sequence length.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable O-methyltransferase family knowledge and sequence features meaningfully favor the histidine at position 254 over the offered alternatives. This is a plausible inference, not a guarantee of the residue's experimentally measured role."
  },
  "case_id": "active_site_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 254 as a proton acceptor, based on a PROSITE-ProRule computational annotation. This supports the key, though it is not direct experimental evidence for that residue's role."
  },
  "important_caveats": [
    "The supplied reviewer evidence supports the position through a computational PROSITE-ProRule annotation, not a cited direct experiment on this residue."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence length rules out options B and D, while the family-level catalytic-base inference favors C over A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates position 254 as a proton acceptor, based on a PROSITE-ProRule computational annotation. This supports the key, though it is not direct experimental evidence for that residue's role.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 350-residue sequence has a glycine-rich region consistent with SAM binding in a small-molecule methyltransferase, and position 254 is histidine. In plant O-methyltransferase family patterns, a conserved histidine can act as the catalytic proton-accepting base. This makes option C a credible family-level inference; options B and D give positions beyond the sequence length.",
    "missing_item_specific_fact": "",
    "reason": "Transferable O-methyltransferase family knowledge and sequence features meaningfully favor the histidine at position 254 over the offered alternatives. This is a plausible inference, not a guarantee of the residue's experimentally measured role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence length rules out options B and D, while the family-level catalytic-base inference favors C over A."
  },
  "important_caveats": [
    "The supplied reviewer evidence supports the position through a computational PROSITE-ProRule annotation, not a cited direct experiment on this residue."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry E7FL15 (sequence matched, 350 AA) annotates an ACT_SITE at position 254 with description 'Proton acceptor' (evidence: ECO:0000255|PROSITE-ProRule:PRU01020, the SAM-dependent methyltransferase Type I pattern). The benchmark sequence matches the source. The annotation is computational (PROSITE-ProRule pattern match) rather than direct experimental mutagenesis on this exact protein, but the underlying biology (conserved catalytic His as proton acceptor in Type I SAM-dependent O-methyltransferases) is experimentally validated across many homologs. Position 254 in the sequence is indeed a Histidine (…AILLKIVL**H**DWSDEN…), consistent with the SAM-MT catalytic His.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three independent steps allow a knowledgeable model to select C without recalling this protein's UniProt record. (1) The supplied sequence is 350 residues; options B (position 1134) and D (position 2475) are immediately eliminated as impossible. (2) The sequence contains hallmark SAM-dependent methyltransferase motifs (e.g., 'VGGGNG' near residue 193, the Type I SAM-MT fold), so the model can assign the protein to the well-characterized Type I SAM-dependent O-methyltransferase family. (3) Across hundreds of experimentally characterized plant and microbial SAM-dependent O-methyltransferases (caffeic acid OMT, coniferyl aldehyde OMT, catechol OMT, etc.), the catalytic proton acceptor is a conserved Histidine acting as a general base to deprotonate the substrate hydroxyl for nucleophilic attack on SAM's methyl group. In the supplied sequence, residue 254 is H (in the context '…AILLKIVLHDW…', the structurally conserved catalytic-His position), whereas residue 280 is K (Lysine), which in this family is not the proton acceptor. The family-level mechanism thus cleanly distinguishes C (His-254) from A (Lys-280).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The inference relies on (a) counting sequence length to eliminate B and D, (b) recognizing SAM-MT family motifs in the input sequence, and (c) the well-established family-wide catalytic mechanism (His as proton acceptor) learned from many other O-methyltransferases. No fact unique to this exact protein's database record is needed to distinguish the four offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B and D are excluded by sequence length. Between A (K-280) and C (H-254), the SAM-MT catalytic-mechanism knowledge unambiguously favors the histidine as proton acceptor. Lysine at 280 is not a recognized catalytic base in this enzyme family. Only C is defensible.


### Important caveats

- The UniProt active-site annotation carries evidence code ECO:0000255 (PROSITE-ProRule pattern match), i.e., it is a computational/rule-based annotation rather than site-directed mutagenesis on this specific protein. The biological principle it encodes, however, is experimentally validated across the SAM-MT family.
- Options B and D reference positions (1134, 2475) far exceeding the 350-residue sequence, making them trivially eliminable; this lowers the effective difficulty to a two-way choice (A vs C).
- The PROSITE-ProRule PRU01020 pattern is broad and may flag the His in many SAM-MTs; for this particular OMT the assignment is consistent with the conserved catalytic-His position observed in structurally characterized homologs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three independent steps allow a knowledgeable model to select C without recalling this protein's UniProt record. (1) The supplied sequence is 350 residues; options B (position 1134) and D (position 2475) are immediately eliminated as impossible. (2) The sequence contains hallmark SAM-dependent methyltransferase motifs (e.g., 'VGGGNG' near residue 193, the Type I SAM-MT fold), so the model can assign the protein to the well-characterized Type I SAM-dependent O-methyltransferase family. (3) Across hundreds of experimentally characterized plant and microbial SAM-dependent O-methyltransferases (caffeic acid OMT, coniferyl aldehyde OMT, catechol OMT, etc.), the catalytic proton acceptor is a conserved Histidine acting as a general base to deprotonate the substrate hydroxyl for nucleophilic attack on SAM's methyl group. In the supplied sequence, residue 254 is H (in the context '…AILLKIVLHDW…', the structurally conserved catalytic-His position), whereas residue 280 is K (Lysine), which in this family is not the proton acceptor. The family-level mechanism thus cleanly distinguishes C (His-254) from A (Lys-280).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on (a) counting sequence length to eliminate B and D, (b) recognizing SAM-MT family motifs in the input sequence, and (c) the well-established family-wide catalytic mechanism (His as proton acceptor) learned from many other O-methyltransferases. No fact unique to this exact protein's database record is needed to distinguish the four offered choices."
  },
  "case_id": "active_site_0082",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry E7FL15 (sequence matched, 350 AA) annotates an ACT_SITE at position 254 with description 'Proton acceptor' (evidence: ECO:0000255|PROSITE-ProRule:PRU01020, the SAM-dependent methyltransferase Type I pattern). The benchmark sequence matches the source. The annotation is computational (PROSITE-ProRule pattern match) rather than direct experimental mutagenesis on this exact protein, but the underlying biology (conserved catalytic His as proton acceptor in Type I SAM-dependent O-methyltransferases) is experimentally validated across many homologs. Position 254 in the sequence is indeed a Histidine (…AILLKIVL**H**DWSDEN…), consistent with the SAM-MT catalytic His."
  },
  "important_caveats": [
    "The UniProt active-site annotation carries evidence code ECO:0000255 (PROSITE-ProRule pattern match), i.e., it is a computational/rule-based annotation rather than site-directed mutagenesis on this specific protein. The biological principle it encodes, however, is experimentally validated across the SAM-MT family.",
    "Options B and D reference positions (1134, 2475) far exceeding the 350-residue sequence, making them trivially eliminable; this lowers the effective difficulty to a two-way choice (A vs C).",
    "The PROSITE-ProRule PRU01020 pattern is broad and may flag the His in many SAM-MTs; for this particular OMT the assignment is consistent with the conserved catalytic-His position observed in structurally characterized homologs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and D are excluded by sequence length. Between A (K-280) and C (H-254), the SAM-MT catalytic-mechanism knowledge unambiguously favors the histidine as proton acceptor. Lysine at 280 is not a recognized catalytic base in this enzyme family. Only C is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0082",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry E7FL15 (sequence matched, 350 AA) annotates an ACT_SITE at position 254 with description 'Proton acceptor' (evidence: ECO:0000255|PROSITE-ProRule:PRU01020, the SAM-dependent methyltransferase Type I pattern). The benchmark sequence matches the source. The annotation is computational (PROSITE-ProRule pattern match) rather than direct experimental mutagenesis on this exact protein, but the underlying biology (conserved catalytic His as proton acceptor in Type I SAM-dependent O-methyltransferases) is experimentally validated across many homologs. Position 254 in the sequence is indeed a Histidine (…AILLKIVL**H**DWSDEN…), consistent with the SAM-MT catalytic His.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three independent steps allow a knowledgeable model to select C without recalling this protein's UniProt record. (1) The supplied sequence is 350 residues; options B (position 1134) and D (position 2475) are immediately eliminated as impossible. (2) The sequence contains hallmark SAM-dependent methyltransferase motifs (e.g., 'VGGGNG' near residue 193, the Type I SAM-MT fold), so the model can assign the protein to the well-characterized Type I SAM-dependent O-methyltransferase family. (3) Across hundreds of experimentally characterized plant and microbial SAM-dependent O-methyltransferases (caffeic acid OMT, coniferyl aldehyde OMT, catechol OMT, etc.), the catalytic proton acceptor is a conserved Histidine acting as a general base to deprotonate the substrate hydroxyl for nucleophilic attack on SAM's methyl group. In the supplied sequence, residue 254 is H (in the context '…AILLKIVLHDW…', the structurally conserved catalytic-His position), whereas residue 280 is K (Lysine), which in this family is not the proton acceptor. The family-level mechanism thus cleanly distinguishes C (His-254) from A (Lys-280).",
    "missing_item_specific_fact": "",
    "reason": "The inference relies on (a) counting sequence length to eliminate B and D, (b) recognizing SAM-MT family motifs in the input sequence, and (c) the well-established family-wide catalytic mechanism (His as proton acceptor) learned from many other O-methyltransferases. No fact unique to this exact protein's database record is needed to distinguish the four offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and D are excluded by sequence length. Between A (K-280) and C (H-254), the SAM-MT catalytic-mechanism knowledge unambiguously favors the histidine as proton acceptor. Lysine at 280 is not a recognized catalytic base in this enzyme family. Only C is defensible."
  },
  "important_caveats": [
    "The UniProt active-site annotation carries evidence code ECO:0000255 (PROSITE-ProRule pattern match), i.e., it is a computational/rule-based annotation rather than site-directed mutagenesis on this specific protein. The biological principle it encodes, however, is experimentally validated across the SAM-MT family.",
    "Options B and D reference positions (1134, 2475) far exceeding the 350-residue sequence, making them trivially eliminable; this lowers the effective difficulty to a two-way choice (A vs C).",
    "The PROSITE-ProRule PRU01020 pattern is broad and may flag the His in many SAM-MTs; for this particular OMT the assignment is consistent with the conserved catalytic-His position observed in structurally characterized homologs."
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
  "benchmark_sequence_length": 350,
  "benchmark_sequence_sha256": "06d60d20d59ec0d189d9e458b41043b823eff47106d90b331759a7a28b559f05",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2011-04-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 350,
  "current_source_sequence_sha256": "06d60d20d59ec0d189d9e458b41043b823eff47106d90b331759a7a28b559f05",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 51,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "E7FL15",
  "selected_historical_entry_version": 51,
  "selected_historical_record_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "selected_historical_source_sequence_length": 350,
  "selected_historical_source_sequence_sha256": "06d60d20d59ec0d189d9e458b41043b823eff47106d90b331759a7a28b559f05",
  "selected_historical_version": {
    "accession": "E7FL15",
    "database": "Swiss-Prot",
    "entryVersion": 51,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CIOMT_CARIP",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"E7FL15\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2011-04-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ipecac\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Rubiaceae\",\"Rubioideae\",\"Palicoureeae\",\"Carapichea\"],\"scientificName\":\"Carapichea ipecacuanha\",\"synonyms\":[\"Callicocca ipecacuanha\"],\"taxonId\":77880}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.395\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"7'-O-demethylcephaeline 7'-O-methyltransferase CiOMT\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"Cephaeline synthase CiOMT\"}]},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21228475\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAJ72588.1\",\"source\":\"EMBL\"}],\"value\":\"7'-O-demethylcephaeline/cephaeline O-methyltransferase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAJ72588.1\",\"source\":\"EMBL\"}],\"value\":\"7'OMT\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"CiOMT\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"2.1.1.396\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"Cephaeline 6'-O-methyltransferase CiOMT\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"21228475\",\"source\":\"PubMed\"}],\"value\":\"Emetine synthase CiOMT\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Proton acceptor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":254},\"start\":{\"modifier\":\"EXACT\",\"value\":254}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/1",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O24529\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":193},\"start\":{\"modifier\":\"EXACT\",\"value\":193}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O24529\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":216},\"start\":{\"modifier\":\"EXACT\",\"value\":216}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O24529\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":236},\"start\":{\"modifier\":\"EXACT\",\"value\":236}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O24529\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":237},\"start\":{\"modifier\":\"EXACT\",\"value\":237}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"O24529\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01020\",\"source\":\"PROSITE-ProRule\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:59789\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:59789\",\"name\":\"S-adenosyl-L-methionine\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":250},\"start\":{\"modifier\":\"EXACT\",\"value\":250}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/E7FL15.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"citation\":{\"authors\":[\"Cheong B.E.\",\"Takemura T.\",\"Yoshimatsu K.\",\"Sato F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"21228475\"},{\"database\":\"DOI\",\"id\":\"10.1271/bbb.100605\"}],\"citationType\":\"journal article\",\"firstPage\":\"107\",\"id\":\"21228475\",\"journal\":\"Biosci. Biotechnol. Biochem.\",\"lastPage\":\"113\",\"publicationDate\":\"2011\",\"title\":\"Molecular cloning of an O-methyltransferase from adventitious roots of Carapichea ipecacuanha.\",\"volume\":\"75\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAJ72588.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Root\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"ACTIVITY REGULATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:28:03.494312+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "609cf6cd020d9d7e0fa677f3e50015958090b4fcff0bd824c92b61563b40280a",
  "url": "https://rest.uniprot.org/uniprotkb/E7FL15.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H1",
  "excerpt": "ID   CIOMT_CARIP             Reviewed;         350 AA.\nAC   E7FL15;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-APR-2011, sequence version 1.\nDT   28-JAN-2026, entry version 51.\nDE   RecName: Full=Cephaeline 6'-O-methyltransferase CiOMT {ECO:0000303|PubMed:21228475};\nDE            Short=Emetine synthase CiOMT {ECO:0000303|PubMed:21228475};\nDE            EC=2.1.1.396 {ECO:0000269|PubMed:21228475};\nDE   AltName: Full=7'-O-demethylcephaeline 7'-O-methyltransferase CiOMT {ECO:0000303|PubMed:21228475};\nDE            Short=Cephaeline synthase CiOMT {ECO:0000303|PubMed:21228475};\nDE            EC=2.1.1.395 {ECO:0000269|PubMed:21228475};\nDE   AltName: Full=7'-O-demethylcephaeline/cephaeline O-methyltransferase {ECO:0000303|PubMed:21228475, ECO:0000312|EMBL:BAJ72588.1};\nDE            Short=7'OMT {ECO:0000312|EMBL:BAJ72588.1};\nDE            Short=CiOMT {ECO:0000303|PubMed:21228475};\nGN   Name=OMT {ECO:0000303|PubMed:21228475};\nOS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;\nOC   Carapichea.\nOX   NCBI_TaxID=77880;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-21",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAJ72588.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, AND ACTIVITY REGULATION.\nRC   TISSUE=Root;\nRX   PubMed=21228475; DOI=10.1271/bbb.100605;\nRA   Cheong B.E., Takemura T., Yoshimatsu K., Sato F.;\nRT   \"Molecular cloning of an O-methyltransferase from adventitious roots of\nRT   Carapichea ipecacuanha.\";\nRL   Biosci. Biotechnol. Biochem. 75:107-113(2011).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 22-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        254\nFT                   /note=\"Proton acceptor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H4",
  "excerpt": "FT   BINDING         193\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O24529,\nFT                   ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-118",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H5",
  "excerpt": "FT   BINDING         216\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O24529,\nFT                   ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-123",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H6",
  "excerpt": "FT   BINDING         236\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O24529,\nFT                   ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 124-128",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         237\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O24529,\nFT                   ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 129-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         250\nFT                   /ligand=\"S-adenosyl-L-methionine\"\nFT                   /ligand_id=\"ChEBI:CHEBI:59789\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:O24529,\nFT                   ECO:0000255|PROSITE-ProRule:PRU01020\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:05.930954+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 134-138",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "aff433f793df82273b03a21e91750cddc3849d13d8eed7c0543d7bb82fb2f13f",
  "url": "https://rest.uniprot.org/unisave/E7FL15?format=txt&versions=51"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 82. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
