# pathway_0145

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0145.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAQEMRYFSTRGGKETLSFEDAVLTGLAPNGGLYIPTHIPALPKDWKTKWAGLSFPELSHEILSLFVPTSVIPSDDLQSIINTAYSSFRSPATTPIRQTGDNEYVLELWHGPTWAFKDVALQFLGELFRYFLERRNKDKTEDMEELTVVGATSGDTGSAAIYGLRSKPSITIFILYPDGRVSPIQEAQMATVPDANVYCVAVEDSDFDTCQSIVKTLFSDAQFNATHRLGAINSINWARILAQIVYYFSAYFQLPEEARKDGAKLQFVVPTGNFGDILAGWYAKKLGLPMEQLVVATNENDILERFFRTGRYEADDAVQQDQTAETAAVNGSSDGQQAVSAVKATHSPAMDILLSSNFERLLYYLALETNGTEGSDEEKRFKAQERLNDWMSTLKKDGKVDLGEDVRQAAGKDFWAERVSDGQTLEEIQKYYRREKYGPYVVDPHTAVGLTAQERSAKKASPDTTWITLSTAHPAKFSGAVELALSASEFPDFDFRRDVLPDELKKLEGLEKRVHRVKGEEGVRALIEKVKSASHEKVDAEEGRGSL

[Multiple Choices]
A. Metabolic intermediate biosynthesis
B. L-methionine biosynthesis via de novo pathway
C. Amino-acid biosynthesis
D. L-threonine from L-aspartate: step 2/5. .
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

> The sequence-matched UniProt annotation places the protein in amino-acid and L-threonine biosynthesis, supporting the broad choice C. The pathway annotation is linked to experimental evidence (ECO:0000269); the annotated reaction is step 5/5, not the step 2/5 specified in option D.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 547-aa sequence is consistent with the conserved sequence profile of a pyridoxal-phosphate-dependent threonine synthase family enzyme. Transferable knowledge of that enzyme family connects it to amino-acid biosynthesis, distinguishing C from the methionine-specific choice B and the incorrectly numbered threonine-pathway step in D. The sequence-based family assignment is an inference, not experimental confirmation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence provides a meaningful basis for the broad pathway choice among these alternatives; recalling an annotation for this exact protein is not necessary.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice A is too general to be a comparably specific pathway answer, while B names a different pathway and D specifies the wrong threonine-biosynthesis step.


### Important caveats

- The reviewer-only source evidence supports the key but was not part of the original model input.
- The sequence-based family recognition is probabilistic; the exact pathway step is not established from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 547-aa sequence is consistent with the conserved sequence profile of a pyridoxal-phosphate-dependent threonine synthase family enzyme. Transferable knowledge of that enzyme family connects it to amino-acid biosynthesis, distinguishing C from the methionine-specific choice B and the incorrectly numbered threonine-pathway step in D. The sequence-based family assignment is an inference, not experimental confirmation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence provides a meaningful basis for the broad pathway choice among these alternatives; recalling an annotation for this exact protein is not necessary."
  },
  "case_id": "pathway_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places the protein in amino-acid and L-threonine biosynthesis, supporting the broad choice C. The pathway annotation is linked to experimental evidence (ECO:0000269); the annotated reaction is step 5/5, not the step 2/5 specified in option D."
  },
  "important_caveats": [
    "The reviewer-only source evidence supports the key but was not part of the original model input.",
    "The sequence-based family recognition is probabilistic; the exact pathway step is not established from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A is too general to be a comparably specific pathway answer, while B names a different pathway and D specifies the wrong threonine-biosynthesis step."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation places the protein in amino-acid and L-threonine biosynthesis, supporting the broad choice C. The pathway annotation is linked to experimental evidence (ECO:0000269); the annotated reaction is step 5/5, not the step 2/5 specified in option D.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 547-aa sequence is consistent with the conserved sequence profile of a pyridoxal-phosphate-dependent threonine synthase family enzyme. Transferable knowledge of that enzyme family connects it to amino-acid biosynthesis, distinguishing C from the methionine-specific choice B and the incorrectly numbered threonine-pathway step in D. The sequence-based family assignment is an inference, not experimental confirmation.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence provides a meaningful basis for the broad pathway choice among these alternatives; recalling an annotation for this exact protein is not necessary."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice A is too general to be a comparably specific pathway answer, while B names a different pathway and D specifies the wrong threonine-biosynthesis step."
  },
  "important_caveats": [
    "The reviewer-only source evidence supports the key but was not part of the original model input.",
    "The sequence-based family recognition is probabilistic; the exact pathway step is not established from sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for this sequence (J9VI85, Threonine synthase, EC 4.2.3.1) states the pathway as 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 5/5.' Choice C ('Amino-acid biosynthesis') matches the top-level pathway category in this hierarchical annotation. The evidence is experimental (ECO:0000269, PubMed 18757810).

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains well-known PLP-dependent enzyme motifs: 'GATSGDTGSAAIYGL' (the conserved PLP-binding region of threonine synthase) and 'DPHTAVGL' near the C-terminus, which together identify this as a member of the threonine synthase (EC 4.2.3.1) family. From standard biochemistry knowledge, threonine synthase catalyzes the FINAL step (step 5/5) in the L-threonine-from-L-aspartate pathway, converting O-phospho-L-homoserine to L-threonine. Choice D specifies 'step 2/5,' which corresponds to aspartate semialdehyde dehydrogenase (EC 1.2.1.11), not threonine synthase. Therefore D is factually eliminated. Choices A (metabolic intermediate biosynthesis) and B (methionine biosynthesis) are clearly unrelated to a PLP-dependent serine/threonine-family enzyme. Choice C ('Amino-acid biosynthesis') is the correct broader pathway category encompassing threonine biosynthesis.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the threonine synthase family from conserved PLP-dependent enzyme sequence motifs, recall that threonine synthase is the terminal (5th) step in the aspartate-to-threonine pathway, and thereby eliminate D (which incorrectly states step 2/5). This leaves C as the correct pathway category. The inference relies on family-level sequence recognition and standard pathway biochemistry, not on recalling this exact protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choice D is eliminated by its incorrect step number (2/5 vs. the correct 5/5 for threonine synthase). Choices A and B are clearly unrelated to a PLP-dependent threonine synthase. Only C remains defensible.


### Important caveats

- The EC number assignment in UniProt is by similarity (ECO:0000250, transferred from P16120), but the pathway annotation is supported by experimental evidence (ECO:0000269, PubMed 18757810).
- The pathway hierarchy in UniProt means 'Amino-acid biosynthesis' (C) is the broadest level; a more specific annotation would be 'L-threonine from L-aspartate: step 5/5,' but that exact option is not offered (D misstates it as step 2/5).
- The sequence motifs used for family identification are well-established PLP-dependent enzyme signatures shared across the threonine synthase family in fungi and bacteria.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains well-known PLP-dependent enzyme motifs: 'GATSGDTGSAAIYGL' (the conserved PLP-binding region of threonine synthase) and 'DPHTAVGL' near the C-terminus, which together identify this as a member of the threonine synthase (EC 4.2.3.1) family. From standard biochemistry knowledge, threonine synthase catalyzes the FINAL step (step 5/5) in the L-threonine-from-L-aspartate pathway, converting O-phospho-L-homoserine to L-threonine. Choice D specifies 'step 2/5,' which corresponds to aspartate semialdehyde dehydrogenase (EC 1.2.1.11), not threonine synthase. Therefore D is factually eliminated. Choices A (metabolic intermediate biosynthesis) and B (methionine biosynthesis) are clearly unrelated to a PLP-dependent serine/threonine-family enzyme. Choice C ('Amino-acid biosynthesis') is the correct broader pathway category encompassing threonine biosynthesis.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the threonine synthase family from conserved PLP-dependent enzyme sequence motifs, recall that threonine synthase is the terminal (5th) step in the aspartate-to-threonine pathway, and thereby eliminate D (which incorrectly states step 2/5). This leaves C as the correct pathway category. The inference relies on family-level sequence recognition and standard pathway biochemistry, not on recalling this exact protein's database entry."
  },
  "case_id": "pathway_0145",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (J9VI85, Threonine synthase, EC 4.2.3.1) states the pathway as 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 5/5.' Choice C ('Amino-acid biosynthesis') matches the top-level pathway category in this hierarchical annotation. The evidence is experimental (ECO:0000269, PubMed 18757810)."
  },
  "important_caveats": [
    "The EC number assignment in UniProt is by similarity (ECO:0000250, transferred from P16120), but the pathway annotation is supported by experimental evidence (ECO:0000269, PubMed 18757810).",
    "The pathway hierarchy in UniProt means 'Amino-acid biosynthesis' (C) is the broadest level; a more specific annotation would be 'L-threonine from L-aspartate: step 5/5,' but that exact option is not offered (D misstates it as step 2/5).",
    "The sequence motifs used for family identification are well-established PLP-dependent enzyme signatures shared across the threonine synthase family in fungi and bacteria."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice D is eliminated by its incorrect step number (2/5 vs. the correct 5/5 for threonine synthase). Choices A and B are clearly unrelated to a PLP-dependent threonine synthase. Only C remains defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0145",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for this sequence (J9VI85, Threonine synthase, EC 4.2.3.1) states the pathway as 'Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 5/5.' Choice C ('Amino-acid biosynthesis') matches the top-level pathway category in this hierarchical annotation. The evidence is experimental (ECO:0000269, PubMed 18757810).",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains well-known PLP-dependent enzyme motifs: 'GATSGDTGSAAIYGL' (the conserved PLP-binding region of threonine synthase) and 'DPHTAVGL' near the C-terminus, which together identify this as a member of the threonine synthase (EC 4.2.3.1) family. From standard biochemistry knowledge, threonine synthase catalyzes the FINAL step (step 5/5) in the L-threonine-from-L-aspartate pathway, converting O-phospho-L-homoserine to L-threonine. Choice D specifies 'step 2/5,' which corresponds to aspartate semialdehyde dehydrogenase (EC 1.2.1.11), not threonine synthase. Therefore D is factually eliminated. Choices A (metabolic intermediate biosynthesis) and B (methionine biosynthesis) are clearly unrelated to a PLP-dependent serine/threonine-family enzyme. Choice C ('Amino-acid biosynthesis') is the correct broader pathway category encompassing threonine biosynthesis.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the threonine synthase family from conserved PLP-dependent enzyme sequence motifs, recall that threonine synthase is the terminal (5th) step in the aspartate-to-threonine pathway, and thereby eliminate D (which incorrectly states step 2/5). This leaves C as the correct pathway category. The inference relies on family-level sequence recognition and standard pathway biochemistry, not on recalling this exact protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choice D is eliminated by its incorrect step number (2/5 vs. the correct 5/5 for threonine synthase). Choices A and B are clearly unrelated to a PLP-dependent threonine synthase. Only C remains defensible."
  },
  "important_caveats": [
    "The EC number assignment in UniProt is by similarity (ECO:0000250, transferred from P16120), but the pathway annotation is supported by experimental evidence (ECO:0000269, PubMed 18757810).",
    "The pathway hierarchy in UniProt means 'Amino-acid biosynthesis' (C) is the broadest level; a more specific annotation would be 'L-threonine from L-aspartate: step 5/5,' but that exact option is not offered (D misstates it as step 2/5).",
    "The sequence motifs used for family identification are well-established PLP-dependent enzyme signatures shared across the threonine synthase family in fungi and bacteria."
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
  "benchmark_sequence_length": 547,
  "benchmark_sequence_sha256": "c29de6f54eb7b3652e0ebb99edcca36018a5532e49d71f579a4be901d48f70b5",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2012-11-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 547,
  "current_source_sequence_sha256": "c29de6f54eb7b3652e0ebb99edcca36018a5532e49d71f579a4be901d48f70b5",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 52,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VI85",
  "selected_historical_entry_version": 52,
  "selected_historical_record_sha256": "5954598a58390b1917faa545f6a402c14a6ff2f4f52694e1ab7713e9613c35f5",
  "selected_historical_source_sequence_length": 547,
  "selected_historical_source_sequence_sha256": "c29de6f54eb7b3652e0ebb99edcca36018a5532e49d71f579a4be901d48f70b5",
  "selected_historical_version": {
    "accession": "J9VI85",
    "database": "Swiss-Prot",
    "entryVersion": 52,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "THRC_CRYN9",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VI85\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:28:53.629626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f",
  "url": "https://rest.uniprot.org/uniprotkb/J9VI85.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2012-11-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:28:53.629626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f",
  "url": "https://rest.uniprot.org/uniprotkb/J9VI85.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"AFR93116.1\",\"source\":\"EMBL\"},{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:28:53.629626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f",
  "url": "https://rest.uniprot.org/uniprotkb/J9VI85.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P16120\",\"source\":\"UniProtKB\"}],\"value\":\"4.2.3.1\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Threonine synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"TS\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:28:53.629626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f",
  "url": "https://rest.uniprot.org/uniprotkb/J9VI85.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18757810\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine from L-aspartate: step 5/5\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:28:53.629626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f",
  "url": "https://rest.uniprot.org/uniprotkb/J9VI85.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VI85.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Kingsbury J.M.\",\"McCusker J.H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18757810\"},{\"database\":\"DOI\",\"id\":\"10.1099/mic.0.2008/019729-0\"}],\"citationType\":\"journal article\",\"firstPage\":\"2767\",\"id\":\"18757810\",\"journal\":\"Microbiology\",\"lastPage\":\"2775\",\"publicationDate\":\"2008\",\"title\":\"Threonine biosynthetic genes are essential in Cryptococcus neoformans.\",\"volume\":\"154\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ACC94295.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18757810\",\"source\":\"PubMed\"}],\"type\":\"STRAIN\",\"value\":\"H99 / ATCC 208821 / CBS 10515 / FGSC 9487\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:28:53.629626+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "056e7e3fc8935259cc82ae794bf1330a257055ae8fb1da4f8d48de3ca1faef9f",
  "url": "https://rest.uniprot.org/uniprotkb/J9VI85.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52)

```json
{
  "entry_version": 52,
  "evidence_id": "H1",
  "excerpt": "ID   THRC_CRYN9              Reviewed;         547 AA.\nAC   J9VI85; B2MW84;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-NOV-2012, sequence version 1.\nDT   28-JAN-2026, entry version 52.\nDE   RecName: Full=Threonine synthase {ECO:0000305};\nDE            Short=TS {ECO:0000305};\nDE            EC=4.2.3.1 {ECO:0000250|UniProtKB:P16120};\nGN   Name=THR4 {ECO:0000303|PubMed:18757810};\nGN   ORFNames=CNAG_03612 {ECO:0000312|EMBL:AFR93116.1};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|EMBL:AFR93116.1, ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.836361+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5954598a58390b1917faa545f6a402c14a6ff2f4f52694e1ab7713e9613c35f5",
  "url": "https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52)

```json
{
  "entry_version": 52,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ACC94295.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=H99 / ATCC 208821 / CBS 10515 / FGSC 9487\nRC   {ECO:0000303|PubMed:18757810};\nRX   PubMed=18757810; DOI=10.1099/mic.0.2008/019729-0;\nRA   Kingsbury J.M., McCusker J.H.;\nRT   \"Threonine biosynthetic genes are essential in Cryptococcus neoformans.\";\nRL   Microbiology 154:2767-2775(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.836361+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5954598a58390b1917faa545f6a402c14a6ff2f4f52694e1ab7713e9613c35f5",
  "url": "https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52)

```json
{
  "entry_version": 52,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-threonine biosynthesis; L-threonine\nCC       from L-aspartate: step 5/5. {ECO:0000269|PubMed:18757810}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:28:56.836361+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 57-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5954598a58390b1917faa545f6a402c14a6ff2f4f52694e1ab7713e9613c35f5",
  "url": "https://rest.uniprot.org/unisave/J9VI85?format=txt&versions=52"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 145. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
