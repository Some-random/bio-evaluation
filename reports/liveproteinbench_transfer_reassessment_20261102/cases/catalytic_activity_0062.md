# catalytic_activity_0062

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0062.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — a D-glucoside + &#91;(1-&gt;2)-beta-D-glucosyl&#93;(n) = a beta-D-glucosyl-(1-&gt;2)-D-glucoside + &#91;(1-&gt;2)-beta-D-glucosyl&#93;(n-1)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKPHNSEKYFVKNGQPHFLISGEVHYFRINPKLWRNHLQLLKQTGADTVSTYIPWDWHEIEEDDFDFEGKTHPARNLIRFIKLCKEENLDLIVKPGPYILAEYENQGLPSWLLKKLSKNAFALDENGNVISPDLVSYLSDEFLEYTFKWYDKVMPIISKHQKEHYGPITMMQLCNEIGVFQWLSGKSDYNPKVINLYKEFIIQRYKTIEKLNSVYSTNYNSFDDLKAPSGKIKLRSDYCAYFDFHLFFREYYNKYISILKNKIRSFGINIKLTHNIPGWIYGNASELPMLISTYSEIMKNHPDIIFGLDHIPEFVSFRNAHSDLACNKILEAMQPEAPVWAAEFQAGTREHHVKAYAKDLETFYIASLAHGIKGFNYYMFSQGINPEGKGFYGKTFYFQTALDAASNKLALYDSIKKVNRFIRKEQKDLLRTNVNSEICVGFYKPYFFTELISSQLLKEKKLNVEELGLYIDPRFLREEILFNGLLRGLQTLNYNYDVVDLENCDLKSLTAYKQLWITSAEFMDAETQNLLSEFVLNGGNLILYPAVPTLDNYLNRCEILKNNFGIEFITKDSSHKVSAFGIEDVFTAFSKKQIYNDTNSKPIAFTQENEICGIRKKIGKGELTILGFAFGYTSDEHLELIDKLVKLNKIKRELFVSDKDIQFVVRENNKSRYIFFLNYHNERKTFNYRKSSELKKKKSEEISIAPFSYKVIKENK

[Multiple Choices]
A. N-[(R)-4-phosphopantothenoyl]-L-cysteine + H(+) = (R)-4'-phosphopantetheine + CO2
B. (3S)-3-hydroxy-3-methylglutaryl-CoA = 3-methyl-(2E)-glutaconyl-CoA + H2O
C. nicotinate beta-D-ribonucleotide + ATP + H(+) = deamido-NAD(+) + diphosphate
D. a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1)
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

> The sequence-matched UniProt annotation assigns the reaction in D and cites experimental evidence (ECO:0000269) from a characterization study. The supplied evidence supports the key, though the primary paper was not independently reviewed here.

Citations as saved: [H4](#evidence-h4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 716-residue sequence is unusually long for the compact enzymes typically associated with the decarboxylation, dehydration, and nucleotide-transfer reactions in A–C. A large enzyme with substantial substrate-binding capacity is a plausible fit for transferring glucosyl units between a glucoside and a glucooligosaccharide, as in D. This is a transferable, probabilistic size-and-function inference, not a way to establish the beta-1,2 linkage specificity from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The alternatives differ substantially in reaction class, and the sequence length supplies a meaningful, if limited, clue favoring the glycosyl-transfer reaction. The exact linkage specificity is not independently apparent, but the choice need only be distinguished among these offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source annotation supports D; no other offered reaction is comparably supported by the supplied evidence.


### Important caveats

- The sequence-length inference is probabilistic and does not by itself prove the exact reaction or linkage specificity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 716-residue sequence is unusually long for the compact enzymes typically associated with the decarboxylation, dehydration, and nucleotide-transfer reactions in A–C. A large enzyme with substantial substrate-binding capacity is a plausible fit for transferring glucosyl units between a glucoside and a glucooligosaccharide, as in D. This is a transferable, probabilistic size-and-function inference, not a way to establish the beta-1,2 linkage specificity from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The alternatives differ substantially in reaction class, and the sequence length supplies a meaningful, if limited, clue favoring the glycosyl-transfer reaction. The exact linkage specificity is not independently apparent, but the choice need only be distinguished among these offered alternatives."
  },
  "case_id": "catalytic_activity_0062",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns the reaction in D and cites experimental evidence (ECO:0000269) from a characterization study. The supplied evidence supports the key, though the primary paper was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence-length inference is probabilistic and does not by itself prove the exact reaction or linkage specificity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source annotation supports D; no other offered reaction is comparably supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns the reaction in D and cites experimental evidence (ECO:0000269) from a characterization study. The supplied evidence supports the key, though the primary paper was not independently reviewed here.",
    "evidence_ids": ["H4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 716-residue sequence is unusually long for the compact enzymes typically associated with the decarboxylation, dehydration, and nucleotide-transfer reactions in A–C. A large enzyme with substantial substrate-binding capacity is a plausible fit for transferring glucosyl units between a glucoside and a glucooligosaccharide, as in D. This is a transferable, probabilistic size-and-function inference, not a way to establish the beta-1,2 linkage specificity from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "The alternatives differ substantially in reaction class, and the sequence length supplies a meaningful, if limited, clue favoring the glycosyl-transfer reaction. The exact linkage specificity is not independently apparent, but the choice need only be distinguished among these offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source annotation supports D; no other offered reaction is comparably supported by the supplied evidence."
  },
  "important_caveats": [
    "The sequence-length inference is probabilistic and does not by itself prove the exact reaction or linkage specificity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry I0AIT9 (sequence matched exactly, 716 aa) annotates this protein as Beta-1,2-glucosyltransferase (EC 2.4.1.391) with the exact reaction in Choice D, supported by experimental evidence (ECO:0000269|PubMed:35065074) including X-ray crystallography structures (PDB 7VKW-7VL6) in complexes with beta-D-glucose and sophorose. The catalytic activity comment (C5/H4) matches Choice D verbatim.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a PP-loop motif 'PPDIIFGLDHIPEF' (~residue 210) characteristic of the N-terminal Rossmann-like domain in GT-B fold glycosyltransferases (PPxxxD pattern). The C-terminal region shows 'GKGELTILGFAFGYTSDEHLELIDKLVKLNKIKRELFVSDKDIQF' with features consistent with the C-terminal acceptor-binding domain of GT-B proteins, including a GKGELTILG-like motif and a DxD-like 'SDKDIQ' pattern. The overall 716-aa length is consistent with a two-domain GT-B architecture (~2×300 aa). Among the four choices, only D is a transferase (EC 2.4.x.x); A is a lyase/decarboxylase (EC 4.1.1.36), B is a lyase/dehydratase (EC 4.2.1.122), and C is a ligase/synthetase (EC 6.3.1.5). Recognizing GT-B fold features allows a model to select D as the sole glycosyltransferase option without needing to resolve the exact beta-1,2 linkage specificity, since no other glycosyltransferase reaction is offered.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The PP-loop motif, two-domain GT-B architecture, and protein size provide transferable sequence-level evidence for glycosyltransferase activity. Since the four alternatives span four distinct EC classes (lyase, lyase, ligase, transferase), identifying the protein as a GT-B fold transferase is sufficient to select D without requiring knowledge of this specific protein's annotation. The beta-1,2 specificity is the only detail not derivable from sequence alone, but it is irrelevant because D is the only glycosyltransferase among the choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent four distinct EC enzyme classes (decarboxylase, dehydratase, NAD synthetase, glycosyltransferase). The sequence features point specifically toward a transferase, making D the uniquely defensible choice. No other option shares the transferase class or GT-B fold characteristics.


### Important caveats

- The protein is described as a 'novel' glycosyltransferase in the source paper, meaning it may not fit neatly into established GT families, but general GT-B fold motifs (PP-loop, two-domain architecture) are still recognizable.
- The specific beta-1,2 linkage and glucoside acceptor specificity cannot be determined from sequence motifs alone; the model relies on D being the only glycosyltransferase option rather than resolving linkage chemistry.
- PP motifs occur in other protein families; the argument depends on the broader context (two-domain architecture, C-terminal motifs, protein size) rather than the PP motif alone.
- The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269, X-ray crystallography), but this evidence was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a PP-loop motif 'PPDIIFGLDHIPEF' (~residue 210) characteristic of the N-terminal Rossmann-like domain in GT-B fold glycosyltransferases (PPxxxD pattern). The C-terminal region shows 'GKGELTILGFAFGYTSDEHLELIDKLVKLNKIKRELFVSDKDIQF' with features consistent with the C-terminal acceptor-binding domain of GT-B proteins, including a GKGELTILG-like motif and a DxD-like 'SDKDIQ' pattern. The overall 716-aa length is consistent with a two-domain GT-B architecture (~2×300 aa). Among the four choices, only D is a transferase (EC 2.4.x.x); A is a lyase/decarboxylase (EC 4.1.1.36), B is a lyase/dehydratase (EC 4.2.1.122), and C is a ligase/synthetase (EC 6.3.1.5). Recognizing GT-B fold features allows a model to select D as the sole glycosyltransferase option without needing to resolve the exact beta-1,2 linkage specificity, since no other glycosyltransferase reaction is offered.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The PP-loop motif, two-domain GT-B architecture, and protein size provide transferable sequence-level evidence for glycosyltransferase activity. Since the four alternatives span four distinct EC classes (lyase, lyase, ligase, transferase), identifying the protein as a GT-B fold transferase is sufficient to select D without requiring knowledge of this specific protein's annotation. The beta-1,2 specificity is the only detail not derivable from sequence alone, but it is irrelevant because D is the only glycosyltransferase among the choices."
  },
  "case_id": "catalytic_activity_0062",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry I0AIT9 (sequence matched exactly, 716 aa) annotates this protein as Beta-1,2-glucosyltransferase (EC 2.4.1.391) with the exact reaction in Choice D, supported by experimental evidence (ECO:0000269|PubMed:35065074) including X-ray crystallography structures (PDB 7VKW-7VL6) in complexes with beta-D-glucose and sophorose. The catalytic activity comment (C5/H4) matches Choice D verbatim."
  },
  "important_caveats": [
    "The protein is described as a 'novel' glycosyltransferase in the source paper, meaning it may not fit neatly into established GT families, but general GT-B fold motifs (PP-loop, two-domain architecture) are still recognizable.",
    "The specific beta-1,2 linkage and glucoside acceptor specificity cannot be determined from sequence motifs alone; the model relies on D being the only glycosyltransferase option rather than resolving linkage chemistry.",
    "PP motifs occur in other protein families; the argument depends on the broader context (two-domain architecture, C-terminal motifs, protein size) rather than the PP motif alone.",
    "The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269, X-ray crystallography), but this evidence was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four distinct EC enzyme classes (decarboxylase, dehydratase, NAD synthetase, glycosyltransferase). The sequence features point specifically toward a transferase, making D the uniquely defensible choice. No other option shares the transferase class or GT-B fold characteristics."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0062",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry I0AIT9 (sequence matched exactly, 716 aa) annotates this protein as Beta-1,2-glucosyltransferase (EC 2.4.1.391) with the exact reaction in Choice D, supported by experimental evidence (ECO:0000269|PubMed:35065074) including X-ray crystallography structures (PDB 7VKW-7VL6) in complexes with beta-D-glucose and sophorose. The catalytic activity comment (C5/H4) matches Choice D verbatim.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a PP-loop motif 'PPDIIFGLDHIPEF' (~residue 210) characteristic of the N-terminal Rossmann-like domain in GT-B fold glycosyltransferases (PPxxxD pattern). The C-terminal region shows 'GKGELTILGFAFGYTSDEHLELIDKLVKLNKIKRELFVSDKDIQF' with features consistent with the C-terminal acceptor-binding domain of GT-B proteins, including a GKGELTILG-like motif and a DxD-like 'SDKDIQ' pattern. The overall 716-aa length is consistent with a two-domain GT-B architecture (~2×300 aa). Among the four choices, only D is a transferase (EC 2.4.x.x); A is a lyase/decarboxylase (EC 4.1.1.36), B is a lyase/dehydratase (EC 4.2.1.122), and C is a ligase/synthetase (EC 6.3.1.5). Recognizing GT-B fold features allows a model to select D as the sole glycosyltransferase option without needing to resolve the exact beta-1,2 linkage specificity, since no other glycosyltransferase reaction is offered.",
    "missing_item_specific_fact": "",
    "reason": "The PP-loop motif, two-domain GT-B architecture, and protein size provide transferable sequence-level evidence for glycosyltransferase activity. Since the four alternatives span four distinct EC classes (lyase, lyase, ligase, transferase), identifying the protein as a GT-B fold transferase is sufficient to select D without requiring knowledge of this specific protein's annotation. The beta-1,2 specificity is the only detail not derivable from sequence alone, but it is irrelevant because D is the only glycosyltransferase among the choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four distinct EC enzyme classes (decarboxylase, dehydratase, NAD synthetase, glycosyltransferase). The sequence features point specifically toward a transferase, making D the uniquely defensible choice. No other option shares the transferase class or GT-B fold characteristics."
  },
  "important_caveats": [
    "The protein is described as a 'novel' glycosyltransferase in the source paper, meaning it may not fit neatly into established GT families, but general GT-B fold motifs (PP-loop, two-domain architecture) are still recognizable.",
    "The specific beta-1,2 linkage and glucoside acceptor specificity cannot be determined from sequence motifs alone; the model relies on D being the only glycosyltransferase option rather than resolving linkage chemistry.",
    "PP motifs occur in other protein families; the argument depends on the broader context (two-domain architecture, C-terminal motifs, protein size) rather than the PP motif alone.",
    "The reviewer evidence confirms the annotation is experimentally supported (ECO:0000269, X-ray crystallography), but this evidence was not available to the evaluated model."
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
  "benchmark_sequence_length": 716,
  "benchmark_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "current_entry_audit": {
    "entryVersion": 57,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-06-13",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 716,
  "current_source_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 55,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "I0AIT9",
  "selected_historical_entry_version": 55,
  "selected_historical_record_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "selected_historical_source_sequence_length": 716,
  "selected_historical_source_sequence_sha256": "494a006d1d004f1e295b0562188f842d9d56a09853f24865be22fafa2da2780f",
  "selected_historical_version": {
    "accession": "I0AIT9",
    "database": "Swiss-Prot",
    "entryVersion": 55,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "B12GT_IGNAJ",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"I0AIT9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":57,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-06-13\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Ignavibacteriota\",\"Ignavibacteria\",\"Ignavibacteriales\",\"Ignavibacteriaceae\",\"Ignavibacterium\"],\"scientificName\":\"Ignavibacterium album (strain DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16)\",\"taxonId\":945713}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"IaSGT\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.391\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"value\":\"Beta-1,2-glucosyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.4.1.391\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35065074\",\"source\":\"PubMed\"}],\"name\":\"a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:78691\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11881\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11882\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:27517\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35436\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:229541\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/I0AIT9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Kobayashi K.\",\"Shimizu H.\",\"Tanaka N.\",\"Kuramochi K.\",\"Nakai H.\",\"Nakajima M.\",\"Taguchi H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35065074\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2022.101606\"}],\"citationType\":\"journal article\",\"firstPage\":\"101606\",\"id\":\"35065074\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"101606\",\"publicationDate\":\"2022\",\"title\":\"Characterization and structural analyses of a novel glycosyltransferase acting on the beta-1,2-glucosidic linkages.\",\"volume\":\"298\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKW\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKX\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKY\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VKZ\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL0\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL1\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL2\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL3\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL4\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL5\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7VL6\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE; SOPHOROSE AND ALTERNATIVE SUBSTRATES\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"ACTIVE SITE\",\"MUTAGENESIS OF GLU-176 AND GLU-343\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:10.515356+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0141e863e485261dd884ecaf6bc9c67a2a0434afac2c92f95f4ffba2990aa032",
  "url": "https://rest.uniprot.org/uniprotkb/I0AIT9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H1",
  "excerpt": "ID   B12GT_IGNAJ             Reviewed;         716 AA.\nAC   I0AIT9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   13-JUN-2012, sequence version 1.\nDT   28-JAN-2026, entry version 55.\nDE   RecName: Full=Beta-1,2-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE            EC=2.4.1.391 {ECO:0000269|PubMed:35065074};\nDE   AltName: Full=Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE   AltName: Full=IaSGT {ECO:0000303|PubMed:35065074};\nGN   OrderedLocusNames=IALB_1185 {ECO:0000312|EMBL:AFH48896.1};\nOS   Ignavibacterium album (strain DSM 19864 / JCM 16511 / NBRC 101810 /\nOS   Mat9-16).\nOC   Bacteria; Pseudomonadati; Ignavibacteriota; Ignavibacteria;\nOC   Ignavibacteriales; Ignavibacteriaceae; Ignavibacterium.\nOX   NCBI_TaxID=945713;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Beta-1,2-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE            EC=2.4.1.391 {ECO:0000269|PubMed:35065074};\nDE   AltName: Full=Beta-1,2-glucooligosaccharide:D-glucoside beta-D-glucosyltransferase {ECO:0000303|PubMed:35065074};\nDE   AltName: Full=IaSGT {ECO:0000303|PubMed:35065074};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7VKW, ECO:0007744|PDB:7VKX, ECO:0007744|PDB:7VKY, ECO:0007744|PDB:7VKZ, ECO:0007744|PDB:7VL0, ECO:0007744|PDB:7VL1, ECO:0007744|PDB:7VL2, ECO:0007744|PDB:7VL3, ECO:0007744|PDB:7VL4, ECO:0007744|PDB:7VL5, ECO:0007744|PDB:7VL6}\nRP   X-RAY CRYSTALLOGRAPHY (1.56 ANGSTROMS) IN COMPLEXES WITH BETA-D-GLUCOSE;\nRP   SOPHOROSE AND ALTERNATIVE SUBSTRATES, FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF\nRP   GLU-176 AND GLU-343.\nRC   STRAIN=DSM 19864 / JCM 16511 / NBRC 101810 / Mat9-16;\nRX   PubMed=35065074; DOI=10.1016/j.jbc.2022.101606;\nRA   Kobayashi K., Shimizu H., Tanaka N., Kuramochi K., Nakai H., Nakajima M.,\nRA   Taguchi H.;\nRT   \"Characterization and structural analyses of a novel glycosyltransferase\nRT   acting on the beta-1,2-glucosidic linkages.\";\nRL   J. Biol. Chem. 298:101606-101606(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 25-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55)

```json
{
  "entry_version": 55,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a D-glucoside + [(1->2)-beta-D-glucosyl](n) = a beta-D-\nCC         glucosyl-(1->2)-D-glucoside + [(1->2)-beta-D-glucosyl](n-1);\nCC         Xref=Rhea:RHEA:78691, Rhea:RHEA-COMP:11881, Rhea:RHEA-COMP:11882,\nCC         ChEBI:CHEBI:27517, ChEBI:CHEBI:35436, ChEBI:CHEBI:229541;\nCC         EC=2.4.1.391; Evidence={ECO:0000269|PubMed:35065074};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:09.687306+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 46-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5021025e7fb0e4fabd17270f530d15eceb2dace998f43c4ec775fc10c6352a01",
  "url": "https://rest.uniprot.org/unisave/I0AIT9?format=txt&versions=55"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 62. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
