# active_site_0088

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0088.txt)

**Task:** `active_site`  
**Expected answer:** **A** — Position 127 (Nucleophile)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVSFKSLLLAASAFTAVLGRPFDSFDGPDVNITDADELLVRRQVTANSEGTHNGYFYSWWSDGGGQVTYTMGAGSRYSVTWKDTGNFVGGKGWNPGTGRTINYGGSFSPQGNGYLAVYGWTRNPLIEYYVVESYGTYNPGSGGQLKGTVTTDGGTYNVYVSTRTNQPSIDGTRTFQQYWSVRTSKRVGGAVTMQNHFNAWAQFGMNLGAHYYQIVATEGNGDFVGTEIWGLARGCRR

[Multiple Choices]
A. Position 127 (Nucleophile)
B. Position 266 (Proton acceptor)
C. Position 283 (For beta-ketoacyl synthase activity)
D. Position 10 (Proton donor)
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

> A historical UniProt entry whose sequence exactly matches the supplied sequence annotates residue 127 as the nucleophile. This is a PROSITE-ProRule computational annotation, not direct experimental confirmation; the same entry annotates residue 218 as the proton donor.

Citations as saved: [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a hydrophobic N-terminal signal peptide and a xylanase-like enzyme sequence with catalytic glutamate residues. Transferable glycoside-hydrolase knowledge supports a catalytic glutamate pair, with the earlier residue serving as the nucleophile and the later one as the proton donor. Residue 127 is glutamate; position 10 lies in the signal peptide, and positions 266 and 283 are beyond the 237-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level catalytic-residue patterns and the options meaningfully distinguish A without needing the exact protein's database record, although the precise role assignment is an inference rather than experimental proof from the input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only A gives an in-range catalytic-residue candidate consistent with the sequence and its xylanase-like pattern; B and C are out of range, and D falls in the N-terminal signal peptide.


### Important caveats

- The matching historical annotation is computationally assigned by PROSITE-ProRule, not shown here to be experimentally validated.
- The current UniProt sequence differs from the supplied sequence; the cited historical entry, rather than the current sequence record, is the exact match.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal signal peptide and a xylanase-like enzyme sequence with catalytic glutamate residues. Transferable glycoside-hydrolase knowledge supports a catalytic glutamate pair, with the earlier residue serving as the nucleophile and the later one as the proton donor. Residue 127 is glutamate; position 10 lies in the signal peptide, and positions 266 and 283 are beyond the 237-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level catalytic-residue patterns and the options meaningfully distinguish A without needing the exact protein's database record, although the precise role assignment is an inference rather than experimental proof from the input."
  },
  "case_id": "active_site_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "A historical UniProt entry whose sequence exactly matches the supplied sequence annotates residue 127 as the nucleophile. This is a PROSITE-ProRule computational annotation, not direct experimental confirmation; the same entry annotates residue 218 as the proton donor."
  },
  "important_caveats": [
    "The matching historical annotation is computationally assigned by PROSITE-ProRule, not shown here to be experimentally validated.",
    "The current UniProt sequence differs from the supplied sequence; the cited historical entry, rather than the current sequence record, is the exact match."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A gives an in-range catalytic-residue candidate consistent with the sequence and its xylanase-like pattern; B and C are out of range, and D falls in the N-terminal signal peptide."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "A historical UniProt entry whose sequence exactly matches the supplied sequence annotates residue 127 as the nucleophile. This is a PROSITE-ProRule computational annotation, not direct experimental confirmation; the same entry annotates residue 218 as the proton donor.",
    "evidence_ids": ["H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a hydrophobic N-terminal signal peptide and a xylanase-like enzyme sequence with catalytic glutamate residues. Transferable glycoside-hydrolase knowledge supports a catalytic glutamate pair, with the earlier residue serving as the nucleophile and the later one as the proton donor. Residue 127 is glutamate; position 10 lies in the signal peptide, and positions 266 and 283 are beyond the 237-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "Family-level catalytic-residue patterns and the options meaningfully distinguish A without needing the exact protein's database record, although the precise role assignment is an inference rather than experimental proof from the input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only A gives an in-range catalytic-residue candidate consistent with the sequence and its xylanase-like pattern; B and C are out of range, and D falls in the N-terminal signal peptide."
  },
  "important_caveats": [
    "The matching historical annotation is computationally assigned by PROSITE-ProRule, not shown here to be experimentally validated.",
    "The current UniProt sequence differs from the supplied sequence; the cited historical entry, rather than the current sequence record, is the exact match."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The historical UniProt entry G2X0L1 (entry version 60, sequence version 1, 237 AA) matches the benchmark sequence exactly (SHA-256 confirmed). The annotation at position 127 is 'ACT_SITE 127 /note="Nucleophile"' with evidence ECO:0000255|PROSITE-ProRule:PRU01097 (Glycosyl hydrolases family 11 signature). This is a computational/PROSITE-ProRule-based annotation, not direct experimental mutagenesis, but it is the canonical database annotation. Position 127 in the supplied sequence is Glutamic acid (E), consistent with the GH11 nucleophile role. The proton donor is annotated at position 218 (also Glu), not at position 10. Choices B (pos 266) and C (pos 283) reference positions beyond the 237-residue protein length.

Citations as saved: [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Three independent lines of reasoning eliminate the distractors and support A: (1) The protein is 237 residues long, so positions 266 (B) and 283 (C) are physically impossible — this is a trivial length check. (2) Position 10 in the sequence is Alanine (A), which cannot serve as a proton donor; catalytic proton donors in glycosidases are Glu or Asp residues. (3) The sequence contains characteristic glycosyl hydrolase family 11 (GH11) motifs (e.g., the 'GKGW' region near positions 88–91, 'GTVTTDGG' near 148–155, and the overall ~200-residue β-jelly-roll fold pattern), identifying this as a xylanase. GH11 enzymes use a retaining double-displacement mechanism with two conserved Glu residues: the nucleophile (first Glu, closer to N-terminus) and the proton donor (second Glu, closer to C-terminus). Position 127 is Glu (E) in a conserved context ('...LIEYYVVESYG...'), consistent with the GH11 nucleophile. Position 218 is also Glu, consistent with the proton donor. Among the offered choices, only A (Position 127, Nucleophile) matches both the amino acid identity and the mechanistic role expected for a GH11 xylanase.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can eliminate B and C by noting the protein is only 237 residues (positions 266 and 283 do not exist). It can eliminate D because position 10 is Alanine, not a catalytic residue. Recognizing GH11 sequence motifs and the conserved Glu nucleophile/proton donor pair from family-level knowledge distinguishes A as the correct answer without needing to recall this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices B and C are eliminated by protein length (237 residues; positions 266 and 283 are out of range). Choice D is eliminated because position 10 is Alanine, which cannot be a proton donor. Only choice A remains, with a Glu at position 127 consistent with the GH11 nucleophile.


### Important caveats

- The PROSITE-ProRule annotation (ECO:0000255) is a computational/similarity-based assignment, not direct experimental mutagenesis evidence for this specific protein. However, the GH11 nucleophile/proton donor Glu pair is well-established across the family.
- The current UniProt entry (sequence version 2, 250 AA) has a different sequence from the benchmark (237 AA); the historical version 1 (237 AA) matches exactly. The annotation positions apply to the matched historical sequence.
- The protein is a precursor (includes a signal peptide 'MVSFKSLLLAASAFTAVLGRPFDSF...'); the active-site numbering uses canonical entry coordinates on the full precursor sequence.
- The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning above relies only on sequence features, protein length, and transferable GH11 family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Three independent lines of reasoning eliminate the distractors and support A: (1) The protein is 237 residues long, so positions 266 (B) and 283 (C) are physically impossible — this is a trivial length check. (2) Position 10 in the sequence is Alanine (A), which cannot serve as a proton donor; catalytic proton donors in glycosidases are Glu or Asp residues. (3) The sequence contains characteristic glycosyl hydrolase family 11 (GH11) motifs (e.g., the 'GKGW' region near positions 88–91, 'GTVTTDGG' near 148–155, and the overall ~200-residue β-jelly-roll fold pattern), identifying this as a xylanase. GH11 enzymes use a retaining double-displacement mechanism with two conserved Glu residues: the nucleophile (first Glu, closer to N-terminus) and the proton donor (second Glu, closer to C-terminus). Position 127 is Glu (E) in a conserved context ('...LIEYYVVESYG...'), consistent with the GH11 nucleophile. Position 218 is also Glu, consistent with the proton donor. Among the offered choices, only A (Position 127, Nucleophile) matches both the amino acid identity and the mechanistic role expected for a GH11 xylanase.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B and C by noting the protein is only 237 residues (positions 266 and 283 do not exist). It can eliminate D because position 10 is Alanine, not a catalytic residue. Recognizing GH11 sequence motifs and the conserved Glu nucleophile/proton donor pair from family-level knowledge distinguishes A as the correct answer without needing to recall this specific protein's database entry."
  },
  "case_id": "active_site_0088",
  "expected_answer_check": {
    "evidence_ids": [
      "H1",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The historical UniProt entry G2X0L1 (entry version 60, sequence version 1, 237 AA) matches the benchmark sequence exactly (SHA-256 confirmed). The annotation at position 127 is 'ACT_SITE 127 /note=\"Nucleophile\"' with evidence ECO:0000255|PROSITE-ProRule:PRU01097 (Glycosyl hydrolases family 11 signature). This is a computational/PROSITE-ProRule-based annotation, not direct experimental mutagenesis, but it is the canonical database annotation. Position 127 in the supplied sequence is Glutamic acid (E), consistent with the GH11 nucleophile role. The proton donor is annotated at position 218 (also Glu), not at position 10. Choices B (pos 266) and C (pos 283) reference positions beyond the 237-residue protein length."
  },
  "important_caveats": [
    "The PROSITE-ProRule annotation (ECO:0000255) is a computational/similarity-based assignment, not direct experimental mutagenesis evidence for this specific protein. However, the GH11 nucleophile/proton donor Glu pair is well-established across the family.",
    "The current UniProt entry (sequence version 2, 250 AA) has a different sequence from the benchmark (237 AA); the historical version 1 (237 AA) matches exactly. The annotation positions apply to the matched historical sequence.",
    "The protein is a precursor (includes a signal peptide 'MVSFKSLLLAASAFTAVLGRPFDSF...'); the active-site numbering uses canonical entry coordinates on the full precursor sequence.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning above relies only on sequence features, protein length, and transferable GH11 family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B and C are eliminated by protein length (237 residues; positions 266 and 283 are out of range). Choice D is eliminated because position 10 is Alanine, which cannot be a proton donor. Only choice A remains, with a Glu at position 127 consistent with the GH11 nucleophile."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0088",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The historical UniProt entry G2X0L1 (entry version 60, sequence version 1, 237 AA) matches the benchmark sequence exactly (SHA-256 confirmed). The annotation at position 127 is 'ACT_SITE 127 /note=\"Nucleophile\"' with evidence ECO:0000255|PROSITE-ProRule:PRU01097 (Glycosyl hydrolases family 11 signature). This is a computational/PROSITE-ProRule-based annotation, not direct experimental mutagenesis, but it is the canonical database annotation. Position 127 in the supplied sequence is Glutamic acid (E), consistent with the GH11 nucleophile role. The proton donor is annotated at position 218 (also Glu), not at position 10. Choices B (pos 266) and C (pos 283) reference positions beyond the 237-residue protein length.",
    "evidence_ids": ["H1", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Three independent lines of reasoning eliminate the distractors and support A: (1) The protein is 237 residues long, so positions 266 (B) and 283 (C) are physically impossible — this is a trivial length check. (2) Position 10 in the sequence is Alanine (A), which cannot serve as a proton donor; catalytic proton donors in glycosidases are Glu or Asp residues. (3) The sequence contains characteristic glycosyl hydrolase family 11 (GH11) motifs (e.g., the 'GKGW' region near positions 88–91, 'GTVTTDGG' near 148–155, and the overall ~200-residue β-jelly-roll fold pattern), identifying this as a xylanase. GH11 enzymes use a retaining double-displacement mechanism with two conserved Glu residues: the nucleophile (first Glu, closer to N-terminus) and the proton donor (second Glu, closer to C-terminus). Position 127 is Glu (E) in a conserved context ('...LIEYYVVESYG...'), consistent with the GH11 nucleophile. Position 218 is also Glu, consistent with the proton donor. Among the offered choices, only A (Position 127, Nucleophile) matches both the amino acid identity and the mechanistic role expected for a GH11 xylanase.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can eliminate B and C by noting the protein is only 237 residues (positions 266 and 283 do not exist). It can eliminate D because position 10 is Alanine, not a catalytic residue. Recognizing GH11 sequence motifs and the conserved Glu nucleophile/proton donor pair from family-level knowledge distinguishes A as the correct answer without needing to recall this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices B and C are eliminated by protein length (237 residues; positions 266 and 283 are out of range). Choice D is eliminated because position 10 is Alanine, which cannot be a proton donor. Only choice A remains, with a Glu at position 127 consistent with the GH11 nucleophile."
  },
  "important_caveats": [
    "The PROSITE-ProRule annotation (ECO:0000255) is a computational/similarity-based assignment, not direct experimental mutagenesis evidence for this specific protein. However, the GH11 nucleophile/proton donor Glu pair is well-established across the family.",
    "The current UniProt entry (sequence version 2, 250 AA) has a different sequence from the benchmark (237 AA); the historical version 1 (237 AA) matches exactly. The annotation positions apply to the matched historical sequence.",
    "The protein is a precursor (includes a signal peptide 'MVSFKSLLLAASAFTAVLGRPFDSF...'); the active-site numbering uses canonical entry coordinates on the full precursor sequence.",
    "The reviewer-only accession and organism identity were not available to the evaluated model; the reasoning above relies only on sequence features, protein length, and transferable GH11 family knowledge."
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
  "benchmark_sequence_length": 237,
  "benchmark_sequence_sha256": "cfdd4b83b607c771888b0e9deb32dd898625aa384e94930782d11bae4f218452",
  "current_entry_audit": {
    "entryVersion": 62,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2026-06-10",
    "sequenceVersion": 2
  },
  "current_record_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "current_sequence_comparison": "mismatch",
  "current_source_sequence_length": 250,
  "current_source_sequence_sha256": "5530b30cec055de49b753bba02a39d9eca395ae75579bf67e16c02b7b3c232ce",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 60,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "G2X0L1",
  "selected_historical_entry_version": 60,
  "selected_historical_record_sha256": "fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a",
  "selected_historical_source_sequence_length": 237,
  "selected_historical_source_sequence_sha256": "cfdd4b83b607c771888b0e9deb32dd898625aa384e94930782d11bae4f218452",
  "selected_historical_version": {
    "accession": "G2X0L1",
    "database": "Swiss-Prot",
    "entryVersion": 60,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "EIX2_VERDV",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- The current UniProt sequence differs from the supplied sequence; applicability of current annotation excerpts is qualified by that mismatch.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"G2X0L1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":62,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2026-06-10\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Verticillium wilt\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Glomerellales\",\"Plectosphaerellaceae\",\"Verticillium\"],\"scientificName\":\"Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\",\"taxonId\":498257}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"value\":\"1,4-beta-D-xylan xylanohydrolase G\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18720841\",\"source\":\"PubMed\"}],\"value\":\"Endo-1,4-beta-xylanase G\"},\"shortNames\":[{\"value\":\"Xylanase G\"}]}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18720841\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.8\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33205907\",\"source\":\"PubMed\"}],\"value\":\"Ethylene-inducing xylanase 2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":127},\"start\":{\"modifier\":\"EXACT\",\"value\":127}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000255\",\"id\":\"PRU01097\",\"source\":\"PROSITE-ProRule\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":218},\"start\":{\"modifier\":\"EXACT\",\"value\":218}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang G.\",\"Rao B.\",\"Ye J.\",\"Ma L.\",\"Zhang X.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18720841\"}],\"citationType\":\"journal article\",\"firstPage\":\"765\",\"id\":\"18720841\",\"journal\":\"Wei Sheng Wu Xue Bao\",\"lastPage\":\"771\",\"publicationDate\":\"2008\",\"title\":\"Molecular cloning and heterologous expression of a new xylanase gene from Verticillium dahliae.\",\"volume\":\"48\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"SUBCELLULAR LOCATION\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/G2X0L1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Yin Z.\",\"Wang N.\",\"Pi L.\",\"Li L.\",\"Duan W.\",\"Wang X.\",\"Dou D.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33205907\"},{\"database\":\"DOI\",\"id\":\"10.1111/jipb.13031\"}],\"citationType\":\"journal article\",\"firstPage\":\"949\",\"id\":\"33205907\",\"journal\":\"J. Integr. Plant Biol.\",\"lastPage\":\"960\",\"publicationDate\":\"2021\",\"title\":\"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-like protein from Verticillium dahliae.\",\"volume\":\"63\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:06.423596+00:00",
  "sequence_comparison": "mismatch",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b6bf3dd61dab32b344f08d226c011b7c3f3936305e457046c933fe6555956510",
  "url": "https://rest.uniprot.org/uniprotkb/G2X0L1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)

```json
{
  "entry_version": 60,
  "evidence_id": "H1",
  "excerpt": "ID   EIX2_VERDV              Reviewed;         237 AA.\nAC   G2X0L1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-NOV-2011, sequence version 1.\nDT   28-JAN-2026, entry version 60.\nDE   RecName: Full=Ethylene-inducing xylanase 2 {ECO:0000303|PubMed:33205907};\nDE            Short=EIX2 {ECO:0000303|PubMed:33205907};\nDE            EC=3.2.1.8 {ECO:0000255|PROSITE-ProRule:PRU01097};\nDE   AltName: Full=Endo-1,4-beta-xylanase EIX2 {ECO:0000303|PubMed:33205907};\nDE   Flags: Precursor;\nGN   Name=EIX2 {ECO:0000303|PubMed:33205907}; ORFNames=VDAG_03790;\nOS   Verticillium dahliae (strain VdLs.17 / ATCC MYA-4575 / FGSC 10137)\nOS   (Verticillium wilt).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Glomerellales; Plectosphaerellaceae; Verticillium.\nOX   NCBI_TaxID=498257;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:04.256317+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a",
  "url": "https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)

```json
{
  "entry_version": 60,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=33205907; DOI=10.1111/jipb.13031;\nRA   Yin Z., Wang N., Pi L., Li L., Duan W., Wang X., Dou D.;\nRT   \"Nicotiana benthamiana LRR-RLP NbEIX2 mediates the perception of an EIX-\nRT   like protein from Verticillium dahliae.\";\nRL   J. Integr. Plant Biol. 63:949-960(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:04.256317+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 30-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a",
  "url": "https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)

```json
{
  "entry_version": 60,
  "evidence_id": "H3",
  "excerpt": "FT   ACT_SITE        127\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:04.256317+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 98-100",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a",
  "url": "https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60)

```json
{
  "entry_version": 60,
  "evidence_id": "H4",
  "excerpt": "FT   ACT_SITE        218\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000255|PROSITE-ProRule:PRU01097\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:04.256317+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 101-103",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fdadd4e4d52d68a34b5b3ac543b98fcb1301387253e8b3d7575373dd73f1aa2a",
  "url": "https://rest.uniprot.org/unisave/G2X0L1?format=txt&versions=60"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 88. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
