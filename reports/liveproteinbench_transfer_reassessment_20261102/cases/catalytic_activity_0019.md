# catalytic_activity_0019

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0019.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — S-ubiquitinyl-&#91;E2 ubiquitin-conjugating enzyme&#93;-L-cysteine + &#91;acceptor protein&#93;-L-lysine = &#91;E2 ubiquitin-conjugating enzyme&#93;-L-cysteine + N(6)-ubiquitinyl-&#91;acceptor protein&#93;-L-lysine.

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPVILNFSSERVLSESELEALRHVGRVSQSEQLVVRGRTMRLHHISFMDSFSVEPVSGGLLDRLSARGHRLLAENLEIQLNRGHTFLQAFRLYMEQSRATPCTRQNVSSAIQNKINSHAFTVSHQDFSCHEQHLNCPITLCIPETGVFVRNAKNSEICSLYDHNALTELIRRNAPHPLSREPFVPEMIVSKDECHFNLIEQYFCILATQNICTRI

[Multiple Choices]
A. tyramine + reduced [NADPH--hemoprotein reductase] + O2 = dopamine + oxidized [NADPH--hemoprotein reductase] + H2O + H(+)
B. 3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-3,4-dihydroxy-5-methoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
C. D-aspartate + acetyl-CoA = N-acetyl-D-aspartate + CoA + H(+)
D. S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzymatic Reaction Prediction, which is to identify the specific chemical reaction catalyzed by a given enzyme. This involves understanding the enzyme's function based on its amino acid sequence and then selecting the correct transformation of substrates into products from a list of possible reactions.. The inputs provided by the user for this task include:

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

> The exact sequence matches the UniProt entry whose catalytic-activity annotation gives reaction D. That annotation cites experimental evidence (ECO:0000269), although the primary study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 215-aa sequence is consistent with the compact NleG/U-box E3 ubiquitin-ligase family. Transferable knowledge of this family supports a role in promoting transfer of ubiquitin from an E2-conjugated cysteine to a lysine on an acceptor protein, matching D. The other choices describe unrelated amine oxidation, methylation, and acetylation reactions.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level recognition and the general mechanism of E3 ubiquitin ligases provide a meaningful basis for distinguishing D without needing the exact protein's recorded annotation. This is a sequence-based inference, not proof of the specific protein's experimentally measured activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered reactions represent distinct enzyme activities, and the family-level inference supports D over the alternatives.


### Important caveats

- The reviewer-only source sequence matches the supplied sequence; its annotation cites experimental evidence, but the primary paper was not independently validated here.
- The organism and database annotation were not part of the original input and are not used as the basis for answerability.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 215-aa sequence is consistent with the compact NleG/U-box E3 ubiquitin-ligase family. Transferable knowledge of this family supports a role in promoting transfer of ubiquitin from an E2-conjugated cysteine to a lysine on an acceptor protein, matching D. The other choices describe unrelated amine oxidation, methylation, and acetylation reactions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the general mechanism of E3 ubiquitin ligases provide a meaningful basis for distinguishing D without needing the exact protein's recorded annotation. This is a sequence-based inference, not proof of the specific protein's experimentally measured activity."
  },
  "case_id": "catalytic_activity_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry whose catalytic-activity annotation gives reaction D. That annotation cites experimental evidence (ECO:0000269), although the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only source sequence matches the supplied sequence; its annotation cites experimental evidence, but the primary paper was not independently validated here.",
    "The organism and database annotation were not part of the original input and are not used as the basis for answerability."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions represent distinct enzyme activities, and the family-level inference supports D over the alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the UniProt entry whose catalytic-activity annotation gives reaction D. That annotation cites experimental evidence (ECO:0000269), although the primary study was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 215-aa sequence is consistent with the compact NleG/U-box E3 ubiquitin-ligase family. Transferable knowledge of this family supports a role in promoting transfer of ubiquitin from an E2-conjugated cysteine to a lysine on an acceptor protein, matching D. The other choices describe unrelated amine oxidation, methylation, and acetylation reactions.",
    "missing_item_specific_fact": "",
    "reason": "Family-level recognition and the general mechanism of E3 ubiquitin ligases provide a meaningful basis for distinguishing D without needing the exact protein's recorded annotation. This is a sequence-based inference, not proof of the specific protein's experimentally measured activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions represent distinct enzyme activities, and the family-level inference supports D over the alternatives."
  },
  "important_caveats": [
    "The reviewer-only source sequence matches the supplied sequence; its annotation cites experimental evidence, but the primary paper was not independently validated here.",
    "The organism and database annotation were not part of the original input and are not used as the basis for answerability."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry Q8XAN6 (NleG8, E. coli O157:H7) is annotated with EC 2.3.2.27 and the catalytic activity 'S-ubiquitinyl-&#91;E2 ubiquitin-conjugating enzyme&#93;-L-cysteine + &#91;acceptor protein&#93;-L-lysine = &#91;E2 ubiquitin-conjugating enzyme&#93;-L-cysteine + N(6)-ubiquitinyl-&#91;acceptor protein&#93;-L-lysine', matching choice D exactly. The evidence code ECO:0000269 (PubMed:36511702) indicates experimental support. The sequence match is confirmed (215 aa, SHA256 match).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of this 215-aa protein contains a cysteine-rich pattern: 'PITLCIPETG...CHFNLIEQYFCILATQNICTRI'. The 'CIP' motif (catalytic cysteine followed by proline) is a well-known family signature of RING/U-box E3 ubiquitin ligases, learned from homologs such as human U-box proteins (e.g., CHIP, PRP19) and bacterial NleG-type effectors. Multiple cysteines in the C-terminus (C-x-x-C spacing) are consistent with zinc-coordinating RING/U-box domains. In contrast, choice A (P450 tyramine hydroxylase) requires the canonical heme-binding FxxGxxxCxG motif, which is absent. Choice B (SAM-dependent methyltransferase) requires the VLDLGCGxGV motif or similar Rossmann-fold SAM-binding elements, absent here. Choice C (GNAT acetyltransferase) requires the R/QxxGxG acetyl-CoA binding motif, also absent. The combination of the CxxP catalytic motif and the C-terminal multi-cysteine zinc-binding pattern is a transferable family-level inference from other RING/U-box E3 ligases that meaningfully selects D over A, B, and C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the RING/U-box E3 ligase family from the C-terminal cysteine-rich architecture and the CIP catalytic motif, both well-documented across many E3 ligase homologs. The absence of P450, methyltransferase, and acetyltransferase signature motifs further eliminates alternatives A, B, and C. This constitutes a legitimate family-level inference from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices represent mechanistically distinct enzyme classes (P450 hydroxylase, methyltransferase, acetyltransferase, E3 ligase) with mutually exclusive structural signatures. The C-terminal CxxP motif and cysteine-rich zinc-binding pattern uniquely point to the E3 ligase class among the offered alternatives.


### Important caveats

- The specific identification as NleG8 (rather than any other RING/U-box E3 ligase) would require additional family-level knowledge, but the question only asks for the catalytic reaction type, which is determined by the RING/U-box fold features visible in the sequence.
- The experimental evidence (PubMed:36511702) for the EC assignment post-dates the original sequence deposition (2002); the sequence-based family inference is independent of this annotation.
- The CxxP motif here appears as 'CIP' (C-I-P) rather than the more canonical 'CxxP' with two intervening residues; however, 'CIP' is a documented variant within the RING/U-box superfamily.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of this 215-aa protein contains a cysteine-rich pattern: 'PITLCIPETG...CHFNLIEQYFCILATQNICTRI'. The 'CIP' motif (catalytic cysteine followed by proline) is a well-known family signature of RING/U-box E3 ubiquitin ligases, learned from homologs such as human U-box proteins (e.g., CHIP, PRP19) and bacterial NleG-type effectors. Multiple cysteines in the C-terminus (C-x-x-C spacing) are consistent with zinc-coordinating RING/U-box domains. In contrast, choice A (P450 tyramine hydroxylase) requires the canonical heme-binding FxxGxxxCxG motif, which is absent. Choice B (SAM-dependent methyltransferase) requires the VLDLGCGxGV motif or similar Rossmann-fold SAM-binding elements, absent here. Choice C (GNAT acetyltransferase) requires the R/QxxGxG acetyl-CoA binding motif, also absent. The combination of the CxxP catalytic motif and the C-terminal multi-cysteine zinc-binding pattern is a transferable family-level inference from other RING/U-box E3 ligases that meaningfully selects D over A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the RING/U-box E3 ligase family from the C-terminal cysteine-rich architecture and the CIP catalytic motif, both well-documented across many E3 ligase homologs. The absence of P450, methyltransferase, and acetyltransferase signature motifs further eliminates alternatives A, B, and C. This constitutes a legitimate family-level inference from other proteins."
  },
  "case_id": "catalytic_activity_0019",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry Q8XAN6 (NleG8, E. coli O157:H7) is annotated with EC 2.3.2.27 and the catalytic activity 'S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine', matching choice D exactly. The evidence code ECO:0000269 (PubMed:36511702) indicates experimental support. The sequence match is confirmed (215 aa, SHA256 match)."
  },
  "important_caveats": [
    "The specific identification as NleG8 (rather than any other RING/U-box E3 ligase) would require additional family-level knowledge, but the question only asks for the catalytic reaction type, which is determined by the RING/U-box fold features visible in the sequence.",
    "The experimental evidence (PubMed:36511702) for the EC assignment post-dates the original sequence deposition (2002); the sequence-based family inference is independent of this annotation.",
    "The CxxP motif here appears as 'CIP' (C-I-P) rather than the more canonical 'CxxP' with two intervening residues; however, 'CIP' is a documented variant within the RING/U-box superfamily."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct enzyme classes (P450 hydroxylase, methyltransferase, acetyltransferase, E3 ligase) with mutually exclusive structural signatures. The C-terminal CxxP motif and cysteine-rich zinc-binding pattern uniquely point to the E3 ligase class among the offered alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0019",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry Q8XAN6 (NleG8, E. coli O157:H7) is annotated with EC 2.3.2.27 and the catalytic activity 'S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine', matching choice D exactly. The evidence code ECO:0000269 (PubMed:36511702) indicates experimental support. The sequence match is confirmed (215 aa, SHA256 match).",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of this 215-aa protein contains a cysteine-rich pattern: 'PITLCIPETG...CHFNLIEQYFCILATQNICTRI'. The 'CIP' motif (catalytic cysteine followed by proline) is a well-known family signature of RING/U-box E3 ubiquitin ligases, learned from homologs such as human U-box proteins (e.g., CHIP, PRP19) and bacterial NleG-type effectors. Multiple cysteines in the C-terminus (C-x-x-C spacing) are consistent with zinc-coordinating RING/U-box domains. In contrast, choice A (P450 tyramine hydroxylase) requires the canonical heme-binding FxxGxxxCxG motif, which is absent. Choice B (SAM-dependent methyltransferase) requires the VLDLGCGxGV motif or similar Rossmann-fold SAM-binding elements, absent here. Choice C (GNAT acetyltransferase) requires the R/QxxGxG acetyl-CoA binding motif, also absent. The combination of the CxxP catalytic motif and the C-terminal multi-cysteine zinc-binding pattern is a transferable family-level inference from other RING/U-box E3 ligases that meaningfully selects D over A, B, and C.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the RING/U-box E3 ligase family from the C-terminal cysteine-rich architecture and the CIP catalytic motif, both well-documented across many E3 ligase homologs. The absence of P450, methyltransferase, and acetyltransferase signature motifs further eliminates alternatives A, B, and C. This constitutes a legitimate family-level inference from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices represent mechanistically distinct enzyme classes (P450 hydroxylase, methyltransferase, acetyltransferase, E3 ligase) with mutually exclusive structural signatures. The C-terminal CxxP motif and cysteine-rich zinc-binding pattern uniquely point to the E3 ligase class among the offered alternatives."
  },
  "important_caveats": [
    "The specific identification as NleG8 (rather than any other RING/U-box E3 ligase) would require additional family-level knowledge, but the question only asks for the catalytic reaction type, which is determined by the RING/U-box fold features visible in the sequence.",
    "The experimental evidence (PubMed:36511702) for the EC assignment post-dates the original sequence deposition (2002); the sequence-based family inference is independent of this annotation.",
    "The CxxP motif here appears as 'CIP' (C-I-P) rather than the more canonical 'CxxP' with two intervening residues; however, 'CIP' is a documented variant within the RING/U-box superfamily."
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
  "benchmark_sequence_length": 215,
  "benchmark_sequence_sha256": "ebd4800979a86f7074a5ae32983d282e50962a3735f30deb653b969a18f418ac",
  "current_entry_audit": {
    "entryVersion": 130,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-03-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 215,
  "current_source_sequence_sha256": "ebd4800979a86f7074a5ae32983d282e50962a3735f30deb653b969a18f418ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 129,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8XAN6",
  "selected_historical_entry_version": 129,
  "selected_historical_record_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "selected_historical_source_sequence_length": 215,
  "selected_historical_source_sequence_sha256": "ebd4800979a86f7074a5ae32983d282e50962a3735f30deb653b969a18f418ac",
  "selected_historical_version": {
    "accession": "Q8XAN6",
    "database": "Swiss-Prot",
    "entryVersion": 129,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "NLEG8_ECO57",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8XAN6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":130,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-03-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Escherichia\"],\"scientificName\":\"Escherichia coli O157:H7\",\"taxonId\":83334}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36511702\",\"source\":\"PubMed\"}],\"value\":\"2.3.2.27\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"E3 ubiquitin-protein ligase NleG\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.2.27\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36511702\",\"source\":\"PubMed\"}],\"name\":\"S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine + [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.\"}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8XAN6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Popov G.\",\"Fiebig-Comyn A.\",\"Syriste L.\",\"Little D.J.\",\"Skarina T.\",\"Stogios P.J.\",\"Birstonas S.\",\"Coombes B.K.\",\"Savchenko A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36511702\"},{\"database\":\"DOI\",\"id\":\"10.1128/iai.00505-22\"}],\"citationType\":\"journal article\",\"firstPage\":\"e0050522\",\"id\":\"36511702\",\"journal\":\"Infect. Immun.\",\"lastPage\":\"e0050522\",\"publicationDate\":\"2023\",\"title\":\"Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for Different Roles during Citrobacter rodentium Infection in Mice.\",\"volume\":\"91\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6XNJ\",\"source\":\"PDB\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.85 ANGSTROMS) OF 206-215 IN COMPLEX WITH HUMAN GOPC\",\"FUNCTION\",\"SUBUNIT\",\"INTERACTION WITH HOST GOPC\",\"SUBCELLULAR LOCATION\",\"DOMAIN\",\"MOTIF\",\"MUTAGENESIS OF ILE-138 AND 212-CYS--ILE-215\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:25.588356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "791e2a8b0c3d1f9c0bb073dd763d0e0b5f78854dc2060aca744568fc452d270b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8XAN6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H1",
  "excerpt": "ID   NLEG8_ECO57             Reviewed;         215 AA.\nAC   Q8XAN6; A0A0H3JIV3; A0A6M0JK84; Q7AEM3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAR-2002, sequence version 1.\nDT   28-JAN-2026, entry version 129.\nDE   RecName: Full=E3 ubiquitin-protein ligase NleG {ECO:0000305};\nDE            EC=2.3.2.27 {ECO:0000269|PubMed:36511702};\nGN   Name=nleG8 {ECO:0000303|PubMed:36511702};\nGN   Synonyms=nleG {ECO:0000312|EMBL:BAB35247.1};\nGN   ORFNames=ECs_1824 {ECO:0000312|EMBL:BAB35247.1};\nOS   Escherichia coli O157:H7.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Escherichia.\nOX   NCBI_TaxID=83334;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:42.292045+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "url": "https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=E3 ubiquitin-protein ligase NleG {ECO:0000305};\nDE            EC=2.3.2.27 {ECO:0000269|PubMed:36511702};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:42.292045+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "url": "https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:6XNJ}\nRP   X-RAY CRYSTALLOGRAPHY (1.85 ANGSTROMS) OF 206-215 IN COMPLEX WITH HUMAN\nRP   GOPC, FUNCTION, SUBUNIT, INTERACTION WITH HOST GOPC, SUBCELLULAR LOCATION,\nRP   DOMAIN, MOTIF, AND MUTAGENESIS OF ILE-138 AND 212-CYS--ILE-215.\nRX   PubMed=36511702; DOI=10.1128/iai.00505-22;\nRA   Popov G., Fiebig-Comyn A., Syriste L., Little D.J., Skarina T.,\nRA   Stogios P.J., Birstonas S., Coombes B.K., Savchenko A.;\nRT   \"Distinct Molecular Features of NleG Type 3 Secreted Effectors Allow for\nRT   Different Roles during Citrobacter rodentium Infection in Mice.\";\nRL   Infect. Immun. 91:e0050522-e0050522(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:42.292045+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-35",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "url": "https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129)

```json
{
  "entry_version": 129,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=S-ubiquitinyl-[E2 ubiquitin-conjugating enzyme]-L-cysteine +\nCC         [acceptor protein]-L-lysine = [E2 ubiquitin-conjugating enzyme]-L-\nCC         cysteine + N(6)-ubiquitinyl-[acceptor protein]-L-lysine.;\nCC         EC=2.3.2.27; Evidence={ECO:0000269|PubMed:36511702};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:42.292045+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6f2c88b76a2a840b2a82d844b183b53e16025dc00931c5f80d6e962d640caabe",
  "url": "https://rest.uniprot.org/unisave/Q8XAN6?format=txt&versions=129"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 19. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
