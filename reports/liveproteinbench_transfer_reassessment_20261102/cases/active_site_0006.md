# active_site_0006

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0006.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 115 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVCFSSLFVAASAIAVVFASPVDHEQLAKRQSTPSSQGTHDGYFYSWWTDGGAAATYTNLAGGEYSVSWSNGGNLVGGKGWNPGSARTITYSGTYNPNGNSYLAVYGWTRNPLVEYYVVENFGTYNPSSGATARGQVTHDGALYRLFESTRTNQPSIDGTATFQQYWAVRDVKRTGGTVNMATFFNAWTSAGMRLGTHNYQVVATEGYFSSGSARINVAGGGGSTPSPPSTPSPPTTPSPPPVTPPPSGGGSCAARWGQCGGSGWNGATCCSAGTCQAQNQWYSQCL

[Multiple Choices]
A. Position 58 (Proton donor)
B. Position 157 (Nucleophile; for glutaminase activity)
C. Position 113 (Glycyl thioester intermediate)
D. Position 115 (Nucleophile)
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

> The sequence-matched UniProt annotation identifies position 115 as the nucleophile, supporting D. This is a PROSITE-ProRule computational annotation, not direct experimental validation. The same annotation places the proton donor at position 206, not position 58.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has an N-terminal signal-peptide-like hydrophobic region and a catalytic domain consistent with a secreted fungal GH11 xylanase. In this family, conserved catalytic glutamates act as the nucleophile and proton donor. Position 115 is Glu, whereas position 58 is Thr; this favors D over A. The glutaminase and glycyl-thioester choices do not fit the xylanase family mechanism.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence and mechanism knowledge gives a concrete basis for selecting the nucleophile at 115 among these alternatives, without needing to recall this exact protein's annotation. It is a transferable inference, though not experimental proof.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives distinguish the nucleophile at 115 from an incorrectly located proton donor and mechanistically mismatched options; no second offered choice is comparably defensible.


### Important caveats

- The supplied database active-site annotation is computationally assigned by PROSITE-ProRule; the cited excerpts do not establish direct experimental validation.
- A xylanase catalytic center includes more than the single residue named in D; the options ask for one residue and role.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has an N-terminal signal-peptide-like hydrophobic region and a catalytic domain consistent with a secreted fungal GH11 xylanase. In this family, conserved catalytic glutamates act as the nucleophile and proton donor. Position 115 is Glu, whereas position 58 is Thr; this favors D over A. The glutaminase and glycyl-thioester choices do not fit the xylanase family mechanism.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and mechanism knowledge gives a concrete basis for selecting the nucleophile at 115 among these alternatives, without needing to recall this exact protein's annotation. It is a transferable inference, though not experimental proof."
  },
  "case_id": "active_site_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 115 as the nucleophile, supporting D. This is a PROSITE-ProRule computational annotation, not direct experimental validation. The same annotation places the proton donor at position 206, not position 58."
  },
  "important_caveats": [
    "The supplied database active-site annotation is computationally assigned by PROSITE-ProRule; the cited excerpts do not establish direct experimental validation.",
    "A xylanase catalytic center includes more than the single residue named in D; the options ask for one residue and role."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives distinguish the nucleophile at 115 from an incorrectly located proton donor and mechanistically mismatched options; no second offered choice is comparably defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 115 as the nucleophile, supporting D. This is a PROSITE-ProRule computational annotation, not direct experimental validation. The same annotation places the proton donor at position 206, not position 58.",
    "evidence_ids": ["C5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has an N-terminal signal-peptide-like hydrophobic region and a catalytic domain consistent with a secreted fungal GH11 xylanase. In this family, conserved catalytic glutamates act as the nucleophile and proton donor. Position 115 is Glu, whereas position 58 is Thr; this favors D over A. The glutaminase and glycyl-thioester choices do not fit the xylanase family mechanism.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence and mechanism knowledge gives a concrete basis for selecting the nucleophile at 115 among these alternatives, without needing to recall this exact protein's annotation. It is a transferable inference, though not experimental proof."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives distinguish the nucleophile at 115 from an incorrectly located proton donor and mechanistically mismatched options; no second offered choice is comparably defensible."
  },
  "important_caveats": [
    "The supplied database active-site annotation is computationally assigned by PROSITE-ProRule; the cited excerpts do not establish direct experimental validation.",
    "A xylanase catalytic center includes more than the single residue named in D; the options ask for one residue and role."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0G4KL96 (EIX3, Endo-1,4-beta-xylanase, EC 3.2.1.8) annotates position 115 as 'Nucleophile' (Active site) with evidence ECO:0000255|PROSITE-ProRule:PRU01097, which is the Glycosyl hydrolases family 10 active site rule. The sequence at position 115 is Glutamic acid (E), consistent with the canonical nucleophilic glutamate in GH10 xylanases. The annotation is computational/curated (PROSITE-ProRule) rather than direct experimental mutagenesis, but the GH10 catalytic mechanism (Glu nucleophile, Glu proton donor) is well-established across the family.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the hallmark GH10 xylanase motif 'WWTDGG' (~positions 47-52) and the overall architecture (multiple aromatic residues, 'NGG' patterns, ~287 aa) identifies it as a Glycoside Hydrolase family 10 endo-xylanase. In GH10 enzymes, the catalytic nucleophile is a conserved Glutamic acid and the proton donor is another conserved Glu. Checking the amino acid at each offered position: Position 58 = Thr (cannot be a proton donor in glycosidases; those are Asp/Glu); Position 157 = Ile (cannot be a nucleophile; also 'glutaminase activity' is irrelevant to a xylanase); Position 113 = Leu (cannot form a 'glycyl thioester intermediate'—that is a ubiquitin-activating enzyme (E1) mechanism, not glycosidase chemistry); Position 115 = Glu (the canonical nucleophile residue in GH10). Thus, basic amino-acid chemistry and family-level mechanism knowledge (GH10 nucleophile = Glu) eliminate A, B, and C, leaving D as the only chemically plausible catalytic residue.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can (1) recognize the GH10 family from the WWTDGG motif and sequence architecture, (2) recall that GH10 nucleophiles are Glu, (3) check the amino acid identity at each offered position, and (4) eliminate options with chemically impossible residues (Thr as proton donor, Ile as nucleophile, Leu forming a thioester). The distinction among choices is made by amino acid identity and general glycosidase mechanism, not by recalling a specific database annotation for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only option D lists a chemically appropriate catalytic residue (Glu at position 115) for a GH10 xylanase nucleophile. The other three options assign impossible roles to non-catalytic amino acids (Thr, Ile, Leu) or invoke an unrelated enzyme mechanism (glycyl thioester for E1 enzymes, glutaminase activity).


### Important caveats

- The UniProt annotation for position 115 is based on PROSITE-ProRule (ECO:0000255), a computational/family-level rule, not direct site-directed mutagenesis on this specific EIX3 protein.
- The proton donor is annotated at position 206 (also Glu), which is not offered as an option, so the question only tests nucleophile identification.
- The reviewer-only evidence (accession, organism, UniProt annotations) was not available to the evaluated model; the reasoning above relies only on sequence-derived family recognition and general biochemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the hallmark GH10 xylanase motif 'WWTDGG' (~positions 47-52) and the overall architecture (multiple aromatic residues, 'NGG' patterns, ~287 aa) identifies it as a Glycoside Hydrolase family 10 endo-xylanase. In GH10 enzymes, the catalytic nucleophile is a conserved Glutamic acid and the proton donor is another conserved Glu. Checking the amino acid at each offered position: Position 58 = Thr (cannot be a proton donor in glycosidases; those are Asp/Glu); Position 157 = Ile (cannot be a nucleophile; also 'glutaminase activity' is irrelevant to a xylanase); Position 113 = Leu (cannot form a 'glycyl thioester intermediate'—that is a ubiquitin-activating enzyme (E1) mechanism, not glycosidase chemistry); Position 115 = Glu (the canonical nucleophile residue in GH10). Thus, basic amino-acid chemistry and family-level mechanism knowledge (GH10 nucleophile = Glu) eliminate A, B, and C, leaving D as the only chemically plausible catalytic residue.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) recognize the GH10 family from the WWTDGG motif and sequence architecture, (2) recall that GH10 nucleophiles are Glu, (3) check the amino acid identity at each offered position, and (4) eliminate options with chemically impossible residues (Thr as proton donor, Ile as nucleophile, Leu forming a thioester). The distinction among choices is made by amino acid identity and general glycosidase mechanism, not by recalling a specific database annotation for this exact protein."
  },
  "case_id": "active_site_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0G4KL96 (EIX3, Endo-1,4-beta-xylanase, EC 3.2.1.8) annotates position 115 as 'Nucleophile' (Active site) with evidence ECO:0000255|PROSITE-ProRule:PRU01097, which is the Glycosyl hydrolases family 10 active site rule. The sequence at position 115 is Glutamic acid (E), consistent with the canonical nucleophilic glutamate in GH10 xylanases. The annotation is computational/curated (PROSITE-ProRule) rather than direct experimental mutagenesis, but the GH10 catalytic mechanism (Glu nucleophile, Glu proton donor) is well-established across the family."
  },
  "important_caveats": [
    "The UniProt annotation for position 115 is based on PROSITE-ProRule (ECO:0000255), a computational/family-level rule, not direct site-directed mutagenesis on this specific EIX3 protein.",
    "The proton donor is annotated at position 206 (also Glu), which is not offered as an option, so the question only tests nucleophile identification.",
    "The reviewer-only evidence (accession, organism, UniProt annotations) was not available to the evaluated model; the reasoning above relies only on sequence-derived family recognition and general biochemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D lists a chemically appropriate catalytic residue (Glu at position 115) for a GH10 xylanase nucleophile. The other three options assign impossible roles to non-catalytic amino acids (Thr, Ile, Leu) or invoke an unrelated enzyme mechanism (glycyl thioester for E1 enzymes, glutaminase activity)."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0G4KL96 (EIX3, Endo-1,4-beta-xylanase, EC 3.2.1.8) annotates position 115 as 'Nucleophile' (Active site) with evidence ECO:0000255|PROSITE-ProRule:PRU01097, which is the Glycosyl hydrolases family 10 active site rule. The sequence at position 115 is Glutamic acid (E), consistent with the canonical nucleophilic glutamate in GH10 xylanases. The annotation is computational/curated (PROSITE-ProRule) rather than direct experimental mutagenesis, but the GH10 catalytic mechanism (Glu nucleophile, Glu proton donor) is well-established across the family.",
    "evidence_ids": ["C5", "H3", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the hallmark GH10 xylanase motif 'WWTDGG' (~positions 47-52) and the overall architecture (multiple aromatic residues, 'NGG' patterns, ~287 aa) identifies it as a Glycoside Hydrolase family 10 endo-xylanase. In GH10 enzymes, the catalytic nucleophile is a conserved Glutamic acid and the proton donor is another conserved Glu. Checking the amino acid at each offered position: Position 58 = Thr (cannot be a proton donor in glycosidases; those are Asp/Glu); Position 157 = Ile (cannot be a nucleophile; also 'glutaminase activity' is irrelevant to a xylanase); Position 113 = Leu (cannot form a 'glycyl thioester intermediate'—that is a ubiquitin-activating enzyme (E1) mechanism, not glycosidase chemistry); Position 115 = Glu (the canonical nucleophile residue in GH10). Thus, basic amino-acid chemistry and family-level mechanism knowledge (GH10 nucleophile = Glu) eliminate A, B, and C, leaving D as the only chemically plausible catalytic residue.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can (1) recognize the GH10 family from the WWTDGG motif and sequence architecture, (2) recall that GH10 nucleophiles are Glu, (3) check the amino acid identity at each offered position, and (4) eliminate options with chemically impossible residues (Thr as proton donor, Ile as nucleophile, Leu forming a thioester). The distinction among choices is made by amino acid identity and general glycosidase mechanism, not by recalling a specific database annotation for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only option D lists a chemically appropriate catalytic residue (Glu at position 115) for a GH10 xylanase nucleophile. The other three options assign impossible roles to non-catalytic amino acids (Thr, Ile, Leu) or invoke an unrelated enzyme mechanism (glycyl thioester for E1 enzymes, glutaminase activity)."
  },
  "important_caveats": [
    "The UniProt annotation for position 115 is based on PROSITE-ProRule (ECO:0000255), a computational/family-level rule, not direct site-directed mutagenesis on this specific EIX3 protein.",
    "The proton donor is annotated at position 206 (also Glu), which is not offered as an option, so the question only tests nucleophile identification.",
    "The reviewer-only evidence (accession, organism, UniProt annotations) was not available to the evaluated model; the reasoning above relies only on sequence-derived family recognition and general biochemistry."
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
  "benchmark_sequence_length": 287,
  "benchmark_sequence_sha256": "15441327e40b4a507f2d749497c8c4cbcbed343d618fb80e7789fe007d17270c",
  "current_entry_audit": {
    "entryVersion": 37,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2015-09-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 287,
  "current_source_sequence_sha256": "15441327e40b4a507f2d749497c8c4cbcbed343d618fb80e7789fe007d17270c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 36,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0G4KL96",
  "selected_historical_entry_version": 36,
  "selected_historical_record_sha256": "3e9ce979511ebc6beb41036187cb06c1d4ba05ea05f31964b342d98537c3251b",
  "selected_historical_source_sequence_length": 287,
  "selected_historical_source_sequence_sha256": "15441327e40b4a507f2d749497c8c4cbcbed343d618fb80e7789fe007d17270c",
  "selected_historical_version": {
    "accession": "A0A0G4KL96",
    "database": "Swiss-Prot",
    "entryVersion": 36,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX3_VERLO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0G4KL96\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:05.640284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":37,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2015-09-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:05.640284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Verticillium dahliae var. longisporum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Glomerellales\",\"Plectosphaerellaceae\",\"Verticillium\"],\"scientificName\":\"Verticillium longisporum\",\"taxonId\":100787}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:05.640284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase EIX3\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 3\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"EIX3\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:05.640284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":115},\"start\":{\"modifier\":\"EXACT\",\"value\":115}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-02T04:24:05.640284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":206},\"start\":{\"modifier\":\"EXACT\",\"value\":206}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-02T04:24:05.640284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-02T04:24:05.640284+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee5462ea538a6639e4bb2c2732a6d0e1f62813e984780d98433324fcf5b40c9b",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0G4KL96.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H1",
  "excerpt": "ID   EIX3_VERLO              Reviewed;         287 AA.\nAC   A0A0G4KL96;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-SEP-2015, sequence version 1.\nDT   28-JAN-2026, entry version 36.\nDE   RecName: Full=Ethylene-inducing xylanase 3 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX3 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX3 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX3 {ECO:0000303|PubMed:33205907}; ORFNames=BN1708_002170;\nOS   Verticillium longisporum (Verticillium dahliae var. longisporum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.\nOX   NCBI_TaxID=100787;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:07.694004+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e9ce979511ebc6beb41036187cb06c1d4ba05ea05f31964b342d98537c3251b",
  "url": "https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H2",
  "excerpt": "RN   [3]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:07.694004+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 29-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e9ce979511ebc6beb41036187cb06c1d4ba05ea05f31964b342d98537c3251b",
  "url": "https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        115\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:07.694004+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 104-106",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e9ce979511ebc6beb41036187cb06c1d4ba05ea05f31964b342d98537c3251b",
  "url": "https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36)

```json
{
  "entry_version": 36,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        206\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:07.694004+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 107-109",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "3e9ce979511ebc6beb41036187cb06c1d4ba05ea05f31964b342d98537c3251b",
  "url": "https://rest.uniprot.org/unisave/A0A0G4KL96?format=txt&versions=36"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 6. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
