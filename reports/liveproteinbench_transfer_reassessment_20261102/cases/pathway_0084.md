# pathway_0084

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0084.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Lipid metabolism. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MRYAVVTGVSSGIGKAICEKFLAKGLYVFGSVRKKEDAKYFEEKYPNTFHTLVFDTTDYPAVDKAVEEIHKVVGKKGLSVLVNNAGVAKYGPIQHVPIEELRQQYEVNVFASVYLTQKLLWLLGASKEAKWQGKVIQISSTAGVMTRPMLGPYSSSKHAVEAIYDALRRELMIYGVEVVLIEPGPIKTEIWGKAKSGGNPYKDTDYGEIFAQLDKAVDEIEKIGLPVEAVAGKAWEAFVAKKPKARYVVAPKKLMFKAAMYLIPDRMLDKIFYKDLKKLTQES

[Multiple Choices]
A. L-threonine from L-aspartate: step 4/5. .
B. Amino-acid degradation
C. Lipid metabolism. .
D. capsule polysaccharide biosynthesis. .
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Protein Pathway Prediction, which is to predict the primary metabolic or signaling pathway in which a given protein functions. Biological pathways are series of chemical reactions occurring within a cell that are essential for life. Based on the protein's amino acid sequence, you should identify the most relevant pathway from the given options.. The inputs provided by the user for this task include:

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

> The exact sequence matches a UniProt entry annotated as NADPH-dependent 3-dehydrocapnine reductase, with the pathway listed as lipid metabolism. The pathway annotation cites the capnine-biosynthesis study, while the pathway label itself is curator-assigned rather than direct proof of every aspect of pathway placement.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein's substrate and role as a 3-dehydrocapnine reductase, or a sufficiently close, functionally characterized homolog that establishes that role.


**Reason**

> The N-terminal glycine-rich sequence is consistent with a dinucleotide-binding oxidoreductase, but that broad feature does not meaningfully distinguish lipid metabolism from the offered amino-acid or polysaccharide pathways. Choosing among them requires substrate specificity or a family-level functional match not established by the input sequence alone.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied source evidence supports C for this protein. Insufficient sequence evidence for an unaided inference does not by itself make another option equally defensible.


### Important caveats

- The source sequence matches the supplied sequence, including in the historical record; the author's exact source snapshot is unknown.
- The pathway label is an annotation with ECO:0000305 evidence. The cited paper is associated with the function and catalytic activity annotations, but was not independently reviewed here.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's substrate and role as a 3-dehydrocapnine reductase, or a sufficiently close, functionally characterized homolog that establishes that role.",
    "reason": "The N-terminal glycine-rich sequence is consistent with a dinucleotide-binding oxidoreductase, but that broad feature does not meaningfully distinguish lipid metabolism from the offered amino-acid or polysaccharide pathways. Choosing among them requires substrate specificity or a family-level functional match not established by the input sequence alone."
  },
  "case_id": "pathway_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as NADPH-dependent 3-dehydrocapnine reductase, with the pathway listed as lipid metabolism. The pathway annotation cites the capnine-biosynthesis study, while the pathway label itself is curator-assigned rather than direct proof of every aspect of pathway placement."
  },
  "important_caveats": [
    "The source sequence matches the supplied sequence, including in the historical record; the author's exact source snapshot is unknown.",
    "The pathway label is an annotation with ECO:0000305 evidence. The cited paper is associated with the function and catalytic activity annotations, but was not independently reviewed here."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied source evidence supports C for this protein. Insufficient sequence evidence for an unaided inference does not by itself make another option equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches a UniProt entry annotated as NADPH-dependent 3-dehydrocapnine reductase, with the pathway listed as lipid metabolism. The pathway annotation cites the capnine-biosynthesis study, while the pathway label itself is curator-assigned rather than direct proof of every aspect of pathway placement.",
    "evidence_ids": ["C4", "C5", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein's substrate and role as a 3-dehydrocapnine reductase, or a sufficiently close, functionally characterized homolog that establishes that role.",
    "reason": "The N-terminal glycine-rich sequence is consistent with a dinucleotide-binding oxidoreductase, but that broad feature does not meaningfully distinguish lipid metabolism from the offered amino-acid or polysaccharide pathways. Choosing among them requires substrate specificity or a family-level functional match not established by the input sequence alone."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied source evidence supports C for this protein. Insufficient sequence evidence for an unaided inference does not by itself make another option equally defensible."
  },
  "important_caveats": [
    "The source sequence matches the supplied sequence, including in the historical record; the author's exact source snapshot is unknown.",
    "The pathway label is an annotation with ECO:0000305 evidence. The cited paper is associated with the function and catalytic activity annotations, but was not independently reviewed here."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A3R5XUE6) annotates this 283-aa protein as 'NADPH-dependent 3-dehydrocapnine reductase' (CapC, EC 1.1.1.-) with the pathway comment 'Lipid metabolism' backed by ECO:0000305 from PubMed:35414181 (Liu et al., Biochemistry 2022, 'Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine'). Capnine is a sulfonolipid, and its biosynthetic pathway is correctly classified under lipid metabolism. The sequence in the question matches the UniProt entry exactly (283 aa, SHA-256 match confirmed in both current and historical snapshots).

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C6](#evidence-c6), [H3](#evidence-h3), [H2](#evidence-h2).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal Rossmann-fold motif (VVTGVSSGIG) and the NNAG motif at ~position 110 clearly identify this as a short-chain dehydrogenase/reductase (SDR). This identification eliminates option D (capsule polysaccharide biosynthesis, which involves glycosyltransferases, not dehydrogenases). The small size (~283 aa) and absence of a C-terminal ACT regulatory domain make option A (homoserine dehydrogenase, step 4/5 of threonine biosynthesis, typically ~370-400 aa with an ACT domain) unlikely. However, the SDR superfamily exceeds 100,000 members and is represented in virtually every metabolic pathway, including both amino-acid degradation and lipid metabolism. Distinguishing option B (amino-acid degradation) from option C (lipid metabolism) requires knowledge of this protein's specific SDR subfamily and substrate (sulfonolipid capnine), which cannot be reliably inferred from the conserved SDR catalytic motifs alone. General SDR knowledge does not provide a meaningful basis to prefer lipid metabolism over amino-acid degradation for a generic SDR sequence.


**Missing item-specific fact**

> The specific SDR subfamily assignment and substrate identity (3-dehydrocapnine / sulfonolipid capnine) that distinguishes this protein's role in lipid biosynthesis from the many SDRs involved in amino-acid degradation. This is a target-specific annotation from PubMed:35414181 and is not derivable from conserved SDR sequence motifs.


**Reason**

> While SDR family recognition (Rossmann + NNAG motifs) eliminates D and the small size disfavors A, the critical B-vs-C distinction requires knowing this protein's specific substrate and subfamily. The SDR superfamily is too large and diverse for general family-level knowledge to assign a pathway between amino-acid degradation and lipid metabolism. The correct assignment depends on the specific experimental characterization of capnine biosynthesis (PubMed:35414181), which is a fact about this exact protein rather than a transferable pattern.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options B and C are both broad metabolic categories, and without the specific annotation a model might plausibly select either. However, only C is factually correct for this protein (sulfonolipid capnine biosynthesis is a lipid pathway). B is a plausible distractor but not a defensible correct answer for this specific protein. No two options are equally defensible as correct.


### Important caveats

- The pathway annotation 'Lipid metabolism' carries evidence code ECO:0000305 (inferred by curator from PubMed:35414181), meaning it is a curator-assigned broad category rather than a direct experimental pathway measurement. The underlying paper experimentally characterized the capnine biosynthetic pathway.
- The EC number is listed as '1.1.1.-' (incomplete), reflecting that the full EC assignment was not finalized at the time of annotation.
- The SDR identification from sequence is robust (Rossmann + NNAG motifs), but SDR subfamily-to-pathway mapping is inherently uncertain without structural or biochemical data.
- The organism (Ornithobacterium rhinotracheale, a Bacteroidota/Flavobacteriales member) and the sulfonolipid capnine pathway are not provided in the original input; the model must rely solely on the sequence and general knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal Rossmann-fold motif (VVTGVSSGIG) and the NNAG motif at ~position 110 clearly identify this as a short-chain dehydrogenase/reductase (SDR). This identification eliminates option D (capsule polysaccharide biosynthesis, which involves glycosyltransferases, not dehydrogenases). The small size (~283 aa) and absence of a C-terminal ACT regulatory domain make option A (homoserine dehydrogenase, step 4/5 of threonine biosynthesis, typically ~370-400 aa with an ACT domain) unlikely. However, the SDR superfamily exceeds 100,000 members and is represented in virtually every metabolic pathway, including both amino-acid degradation and lipid metabolism. Distinguishing option B (amino-acid degradation) from option C (lipid metabolism) requires knowledge of this protein's specific SDR subfamily and substrate (sulfonolipid capnine), which cannot be reliably inferred from the conserved SDR catalytic motifs alone. General SDR knowledge does not provide a meaningful basis to prefer lipid metabolism over amino-acid degradation for a generic SDR sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific SDR subfamily assignment and substrate identity (3-dehydrocapnine / sulfonolipid capnine) that distinguishes this protein's role in lipid biosynthesis from the many SDRs involved in amino-acid degradation. This is a target-specific annotation from PubMed:35414181 and is not derivable from conserved SDR sequence motifs.",
    "reason": "While SDR family recognition (Rossmann + NNAG motifs) eliminates D and the small size disfavors A, the critical B-vs-C distinction requires knowing this protein's specific substrate and subfamily. The SDR superfamily is too large and diverse for general family-level knowledge to assign a pathway between amino-acid degradation and lipid metabolism. The correct assignment depends on the specific experimental characterization of capnine biosynthesis (PubMed:35414181), which is a fact about this exact protein rather than a transferable pattern."
  },
  "case_id": "pathway_0084",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C6",
      "H3",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A3R5XUE6) annotates this 283-aa protein as 'NADPH-dependent 3-dehydrocapnine reductase' (CapC, EC 1.1.1.-) with the pathway comment 'Lipid metabolism' backed by ECO:0000305 from PubMed:35414181 (Liu et al., Biochemistry 2022, 'Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine'). Capnine is a sulfonolipid, and its biosynthetic pathway is correctly classified under lipid metabolism. The sequence in the question matches the UniProt entry exactly (283 aa, SHA-256 match confirmed in both current and historical snapshots)."
  },
  "important_caveats": [
    "The pathway annotation 'Lipid metabolism' carries evidence code ECO:0000305 (inferred by curator from PubMed:35414181), meaning it is a curator-assigned broad category rather than a direct experimental pathway measurement. The underlying paper experimentally characterized the capnine biosynthetic pathway.",
    "The EC number is listed as '1.1.1.-' (incomplete), reflecting that the full EC assignment was not finalized at the time of annotation.",
    "The SDR identification from sequence is robust (Rossmann + NNAG motifs), but SDR subfamily-to-pathway mapping is inherently uncertain without structural or biochemical data.",
    "The organism (Ornithobacterium rhinotracheale, a Bacteroidota/Flavobacteriales member) and the sulfonolipid capnine pathway are not provided in the original input; the model must rely solely on the sequence and general knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are both broad metabolic categories, and without the specific annotation a model might plausibly select either. However, only C is factually correct for this protein (sulfonolipid capnine biosynthesis is a lipid pathway). B is a plausible distractor but not a defensible correct answer for this specific protein. No two options are equally defensible as correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0084",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A3R5XUE6) annotates this 283-aa protein as 'NADPH-dependent 3-dehydrocapnine reductase' (CapC, EC 1.1.1.-) with the pathway comment 'Lipid metabolism' backed by ECO:0000305 from PubMed:35414181 (Liu et al., Biochemistry 2022, 'Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine'). Capnine is a sulfonolipid, and its biosynthetic pathway is correctly classified under lipid metabolism. The sequence in the question matches the UniProt entry exactly (283 aa, SHA-256 match confirmed in both current and historical snapshots).",
    "evidence_ids": ["C5", "C4", "C6", "H3", "H2"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal Rossmann-fold motif (VVTGVSSGIG) and the NNAG motif at ~position 110 clearly identify this as a short-chain dehydrogenase/reductase (SDR). This identification eliminates option D (capsule polysaccharide biosynthesis, which involves glycosyltransferases, not dehydrogenases). The small size (~283 aa) and absence of a C-terminal ACT regulatory domain make option A (homoserine dehydrogenase, step 4/5 of threonine biosynthesis, typically ~370-400 aa with an ACT domain) unlikely. However, the SDR superfamily exceeds 100,000 members and is represented in virtually every metabolic pathway, including both amino-acid degradation and lipid metabolism. Distinguishing option B (amino-acid degradation) from option C (lipid metabolism) requires knowledge of this protein's specific SDR subfamily and substrate (sulfonolipid capnine), which cannot be reliably inferred from the conserved SDR catalytic motifs alone. General SDR knowledge does not provide a meaningful basis to prefer lipid metabolism over amino-acid degradation for a generic SDR sequence.",
    "missing_item_specific_fact": "The specific SDR subfamily assignment and substrate identity (3-dehydrocapnine / sulfonolipid capnine) that distinguishes this protein's role in lipid biosynthesis from the many SDRs involved in amino-acid degradation. This is a target-specific annotation from PubMed:35414181 and is not derivable from conserved SDR sequence motifs.",
    "reason": "While SDR family recognition (Rossmann + NNAG motifs) eliminates D and the small size disfavors A, the critical B-vs-C distinction requires knowing this protein's specific substrate and subfamily. The SDR superfamily is too large and diverse for general family-level knowledge to assign a pathway between amino-acid degradation and lipid metabolism. The correct assignment depends on the specific experimental characterization of capnine biosynthesis (PubMed:35414181), which is a fact about this exact protein rather than a transferable pattern."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options B and C are both broad metabolic categories, and without the specific annotation a model might plausibly select either. However, only C is factually correct for this protein (sulfonolipid capnine biosynthesis is a lipid pathway). B is a plausible distractor but not a defensible correct answer for this specific protein. No two options are equally defensible as correct."
  },
  "important_caveats": [
    "The pathway annotation 'Lipid metabolism' carries evidence code ECO:0000305 (inferred by curator from PubMed:35414181), meaning it is a curator-assigned broad category rather than a direct experimental pathway measurement. The underlying paper experimentally characterized the capnine biosynthetic pathway.",
    "The EC number is listed as '1.1.1.-' (incomplete), reflecting that the full EC assignment was not finalized at the time of annotation.",
    "The SDR identification from sequence is robust (Rossmann + NNAG motifs), but SDR subfamily-to-pathway mapping is inherently uncertain without structural or biochemical data.",
    "The organism (Ornithobacterium rhinotracheale, a Bacteroidota/Flavobacteriales member) and the sulfonolipid capnine pathway are not provided in the original input; the model must rely solely on the sequence and general knowledge."
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
  "benchmark_sequence_length": 283,
  "benchmark_sequence_sha256": "c34636190c93b708ede11afe25d8f3e950d83ee164fe4651dffd58c7eb032d36",
  "current_entry_audit": {
    "entryVersion": 18,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-04-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 283,
  "current_source_sequence_sha256": "c34636190c93b708ede11afe25d8f3e950d83ee164fe4651dffd58c7eb032d36",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 16,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A3R5XUE6",
  "selected_historical_entry_version": 16,
  "selected_historical_record_sha256": "6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434",
  "selected_historical_source_sequence_length": 283,
  "selected_historical_source_sequence_sha256": "c34636190c93b708ede11afe25d8f3e950d83ee164fe4651dffd58c7eb032d36",
  "selected_historical_version": {
    "accession": "A0A3R5XUE6",
    "database": "Swiss-Prot",
    "entryVersion": 16,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "CAPC_ORNRH",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A3R5XUE6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":18,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-04-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Bacteroidota\",\"Flavobacteriia\",\"Flavobacteriales\",\"Weeksellaceae\",\"Ornithobacterium\"],\"scientificName\":\"Ornithobacterium rhinotracheale\",\"taxonId\":28251}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"NADPH-dependent 3-dehydrocapnine reductase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"35414181\",\"source\":\"PubMed\"}],\"value\":\"Lipid metabolism\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu Y.\",\"Wei Y.\",\"Teh T.M.\",\"Liu D.\",\"Zhou Y.\",\"Zhao S.\",\"Ang E.L.\",\"Zhao H.\",\"Zhang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35414181\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.2c00102\"}],\"citationType\":\"journal article\",\"firstPage\":\"2861\",\"id\":\"35414181\",\"journal\":\"Biochemistry\",\"lastPage\":\"2869\",\"publicationDate\":\"2022\",\"title\":\"Identification and Characterization of the Biosynthetic Pathway of the Sulfonolipid Capnine.\",\"volume\":\"61\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:46.269818+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "eeb98d69cf0b99fa39b7fc118681807f2518aa1d8a1eb2df8e1e31569d47b1c6",
  "url": "https://rest.uniprot.org/uniprotkb/A0A3R5XUE6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H1",
  "excerpt": "ID   CAPC_ORNRH              Reviewed;         283 AA.\nAC   A0A3R5XUE6;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-APR-2019, sequence version 1.\nDT   28-JAN-2026, entry version 16.\nDE   RecName: Full=NADPH-dependent 3-dehydrocapnine reductase {ECO:0000303|PubMed:35414181};\nDE            EC=1.1.1.- {ECO:0000269|PubMed:35414181};\nGN   Name=capC {ECO:0000303|PubMed:35414181};\nGN   ORFNames=EQP59_04780 {ECO:0000312|EMBL:QAR30703.1};\nOS   Ornithobacterium rhinotracheale.\nOC   Bacteria; Pseudomonadati; Bacteroidota; Flavobacteriia; Flavobacteriales;\nOC   Weeksellaceae; Ornithobacterium.\nOX   NCBI_TaxID=28251;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:30.826829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434",
  "url": "https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND CATALYTIC ACTIVITY.\nRX   PubMed=35414181; DOI=10.1021/acs.biochem.2c00102;\nRA   Liu Y., Wei Y., Teh T.M., Liu D., Zhou Y., Zhao S., Ang E.L., Zhao H.,\nRA   Zhang Y.;\nRT   \"Identification and Characterization of the Biosynthetic Pathway of the\nRT   Sulfonolipid Capnine.\";\nRL   Biochemistry 61:2861-2869(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:30.826829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434",
  "url": "https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Lipid metabolism. {ECO:0000305|PubMed:35414181}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:30.826829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-41",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "6775a10db7332809ed4375188f70ceb1072cc82dbd87c32150e6341b3a85c434",
  "url": "https://rest.uniprot.org/unisave/A0A3R5XUE6?format=txt&versions=16"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 84. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
