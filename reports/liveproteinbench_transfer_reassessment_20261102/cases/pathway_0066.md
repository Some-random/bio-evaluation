# pathway_0066

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0066.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Amino-acid degradation. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MQIKPPYLLFIGDATDKLSIKMAQSLADWRAELCVGELSVNGCTVSTGLNQCSICEAAKLGAKTFVLGFANSGGVLDKKWLPIISEAIENGMNIVSGLHDKLTNFDELVSLSQKHNTNLLDIRHPSTAFATGKGYKRKGKRLLTVGTDCSVGKMYTSLSLEKAMKEQNIDVDFRATGQCGILISGSGVAIDCVIADFISGAAESLSPDAEETHWDIIEGQGSLSHPAFAGVSLGLLHGSQPDALVICHALNRTHMRGLLHTSFPSIETTIELNIAAAKLTNPDVQVVGISVNTSSVSIEQGNEICERLSQTFGVPCVDPLRDGVDSIVANLC

[Multiple Choices]
A. Carbohydrate degradation
B. tetrahydrofolate interconversion. .
C. dTTP biosynthesis. .
D. Amino-acid degradation. .
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

> The exact sequence matches the source entry, which identifies the protein as D-glutamate N-acetyltransferase and annotates its pathway as amino-acid degradation. The catalytic-activity annotation cites experimental evidence; the pathway annotation is curator-assigned, so the two claims have different evidence status.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> The protein's specific enzymatic function or a reliably recognizable homolog/family assignment linking it to D-glutamate catabolism.


**Reason**

> The input is an enzyme-like sequence, but it provides no evident, distinctive sequence motif or context that identifies its substrate or pathway among these choices. Without a specific functional or family assignment, general knowledge does not meaningfully distinguish amino-acid degradation from the other offered pathways.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source annotation specifies amino-acid degradation, and no competing option is equally supported by the supplied evidence.


### Important caveats

- The pathway annotation is curator-assigned; it should not be described as direct experimental evidence for pathway membership.
- The source sequence matches the benchmark sequence, but the author's exact source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's specific enzymatic function or a reliably recognizable homolog/family assignment linking it to D-glutamate catabolism.",
    "reason": "The input is an enzyme-like sequence, but it provides no evident, distinctive sequence motif or context that identifies its substrate or pathway among these choices. Without a specific functional or family assignment, general knowledge does not meaningfully distinguish amino-acid degradation from the other offered pathways."
  },
  "case_id": "pathway_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the source entry, which identifies the protein as D-glutamate N-acetyltransferase and annotates its pathway as amino-acid degradation. The catalytic-activity annotation cites experimental evidence; the pathway annotation is curator-assigned, so the two claims have different evidence status."
  },
  "important_caveats": [
    "The pathway annotation is curator-assigned; it should not be described as direct experimental evidence for pathway membership.",
    "The source sequence matches the benchmark sequence, but the author's exact source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source annotation specifies amino-acid degradation, and no competing option is equally supported by the supplied evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the source entry, which identifies the protein as D-glutamate N-acetyltransferase and annotates its pathway as amino-acid degradation. The catalytic-activity annotation cites experimental evidence; the pathway annotation is curator-assigned, so the two claims have different evidence status.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "The protein's specific enzymatic function or a reliably recognizable homolog/family assignment linking it to D-glutamate catabolism.",
    "reason": "The input is an enzyme-like sequence, but it provides no evident, distinctive sequence motif or context that identifies its substrate or pathway among these choices. Without a specific functional or family assignment, general knowledge does not meaningfully distinguish amino-acid degradation from the other offered pathways."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source annotation specifies amino-acid degradation, and no competing option is equally supported by the supplied evidence."
  },
  "important_caveats": [
    "The pathway annotation is curator-assigned; it should not be described as direct experimental evidence for pathway membership.",
    "The source sequence matches the benchmark sequence, but the author's exact source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXZ1 (sequence matched to the benchmark 332-AA sequence) is annotated as D-glutamate N-acetyltransferase (EC 2.3.1.312) with the explicit PATHWAY comment 'Amino-acid degradation' (evidence codes ECO:0000305, backed by experimental evidence ECO:0000269 from PubMed:36690779, a 2023 ISME J. paper on a novel D-glutamate catabolic pathway). The expected answer D is directly stated in the annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains motifs consistent with the GNAT (GCN5-related N-acetyltransferase) superfamily fold, including 'GSG' and 'GxG' patterns in the central region (e.g., 'GSGVAIDCVIADFISGAAES'), suggesting acetyltransferase (EC 2.x.x) activity. Among the four offered pathway choices, N-acetyltransferases are a well-known enzyme class in amino-acid catabolism (e.g., N-acetylation of amino acids as a catabolic entry step in many bacteria). The other three pathways involve fundamentally different enzyme classes: carbohydrate degradation relies on glycosidases, phosphorylases, and aldolases (hydrolases/lyases); tetrahydrofolate interconversion involves oxidoreductases (DHFR, MTHFD) and specific methyl/formyl transferases; dTTP biosynthesis involves nucleotide-specific kinases and ribonucleotide reductase. Recognizing acetyltransferase-like features and the general biological pattern that N-acetyltransferases participate in amino-acid degradation meaningfully distinguishes D from A, B, and C without needing the specific annotation of this exact protein.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GNAT-fold motif recognition is transferable structural/biochemical knowledge. The general association of N-acetyltransferases with amino-acid catabolism is a well-established biological pattern learned from many related proteins (e.g., amino-acid N-acetyltransferases in bacterial catabolic operons). The other three pathways are dominated by enzyme classes (hydrolases, oxidoreductases, nucleotide kinases) that are mechanistically and structurally distinct from acetyltransferases, providing a credible basis for elimination. The inference is probabilistic rather than certain, but it meaningfully distinguishes the offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four pathway choices involve clearly distinct enzyme classes. An acetyltransferase does not naturally fit carbohydrate degradation (hydrolases/lyases), tetrahydrofolate interconversion (oxidoreductases/specific transferases), or dTTP biosynthesis (nucleotide kinases). Only amino-acid degradation is a natural home for an N-acetyltransferase among the four options.


### Important caveats

- The protein is a novel enzyme (EC 2.3.1.312, first characterized in 2023). The GNAT-fold motif recognition from a 332-AA sequence (larger than typical ~200-AA GNAT enzymes) may be non-trivial and the sequence may contain additional domains beyond the catalytic GNAT core.
- The specific D-glutamate substrate specificity is novel and not predictable from sequence alone; however, the question asks about the pathway class (amino-acid degradation), not the specific substrate, so this does not undermine the pathway-level inference.
- The pathway annotation carries evidence code ECO:0000305 (curator inference) for the pathway label, though the underlying function and catalytic activity are supported by experimental evidence (ECO:0000269).
- The UniProt entry was first released in April 2025; the benchmark author's source snapshot date is unknown, so the annotation may or may not have been available at benchmark construction time.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains motifs consistent with the GNAT (GCN5-related N-acetyltransferase) superfamily fold, including 'GSG' and 'GxG' patterns in the central region (e.g., 'GSGVAIDCVIADFISGAAES'), suggesting acetyltransferase (EC 2.x.x) activity. Among the four offered pathway choices, N-acetyltransferases are a well-known enzyme class in amino-acid catabolism (e.g., N-acetylation of amino acids as a catabolic entry step in many bacteria). The other three pathways involve fundamentally different enzyme classes: carbohydrate degradation relies on glycosidases, phosphorylases, and aldolases (hydrolases/lyases); tetrahydrofolate interconversion involves oxidoreductases (DHFR, MTHFD) and specific methyl/formyl transferases; dTTP biosynthesis involves nucleotide-specific kinases and ribonucleotide reductase. Recognizing acetyltransferase-like features and the general biological pattern that N-acetyltransferases participate in amino-acid degradation meaningfully distinguishes D from A, B, and C without needing the specific annotation of this exact protein.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GNAT-fold motif recognition is transferable structural/biochemical knowledge. The general association of N-acetyltransferases with amino-acid catabolism is a well-established biological pattern learned from many related proteins (e.g., amino-acid N-acetyltransferases in bacterial catabolic operons). The other three pathways are dominated by enzyme classes (hydrolases, oxidoreductases, nucleotide kinases) that are mechanistically and structurally distinct from acetyltransferases, providing a credible basis for elimination. The inference is probabilistic rather than certain, but it meaningfully distinguishes the offered choices."
  },
  "case_id": "pathway_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ1 (sequence matched to the benchmark 332-AA sequence) is annotated as D-glutamate N-acetyltransferase (EC 2.3.1.312) with the explicit PATHWAY comment 'Amino-acid degradation' (evidence codes ECO:0000305, backed by experimental evidence ECO:0000269 from PubMed:36690779, a 2023 ISME J. paper on a novel D-glutamate catabolic pathway). The expected answer D is directly stated in the annotation."
  },
  "important_caveats": [
    "The protein is a novel enzyme (EC 2.3.1.312, first characterized in 2023). The GNAT-fold motif recognition from a 332-AA sequence (larger than typical ~200-AA GNAT enzymes) may be non-trivial and the sequence may contain additional domains beyond the catalytic GNAT core.",
    "The specific D-glutamate substrate specificity is novel and not predictable from sequence alone; however, the question asks about the pathway class (amino-acid degradation), not the specific substrate, so this does not undermine the pathway-level inference.",
    "The pathway annotation carries evidence code ECO:0000305 (curator inference) for the pathway label, though the underlying function and catalytic activity are supported by experimental evidence (ECO:0000269).",
    "The UniProt entry was first released in April 2025; the benchmark author's source snapshot date is unknown, so the annotation may or may not have been available at benchmark construction time."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four pathway choices involve clearly distinct enzyme classes. An acetyltransferase does not naturally fit carbohydrate degradation (hydrolases/lyases), tetrahydrofolate interconversion (oxidoreductases/specific transferases), or dTTP biosynthesis (nucleotide kinases). Only amino-acid degradation is a natural home for an N-acetyltransferase among the four options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ1 (sequence matched to the benchmark 332-AA sequence) is annotated as D-glutamate N-acetyltransferase (EC 2.3.1.312) with the explicit PATHWAY comment 'Amino-acid degradation' (evidence codes ECO:0000305, backed by experimental evidence ECO:0000269 from PubMed:36690779, a 2023 ISME J. paper on a novel D-glutamate catabolic pathway). The expected answer D is directly stated in the annotation.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains motifs consistent with the GNAT (GCN5-related N-acetyltransferase) superfamily fold, including 'GSG' and 'GxG' patterns in the central region (e.g., 'GSGVAIDCVIADFISGAAES'), suggesting acetyltransferase (EC 2.x.x) activity. Among the four offered pathway choices, N-acetyltransferases are a well-known enzyme class in amino-acid catabolism (e.g., N-acetylation of amino acids as a catabolic entry step in many bacteria). The other three pathways involve fundamentally different enzyme classes: carbohydrate degradation relies on glycosidases, phosphorylases, and aldolases (hydrolases/lyases); tetrahydrofolate interconversion involves oxidoreductases (DHFR, MTHFD) and specific methyl/formyl transferases; dTTP biosynthesis involves nucleotide-specific kinases and ribonucleotide reductase. Recognizing acetyltransferase-like features and the general biological pattern that N-acetyltransferases participate in amino-acid degradation meaningfully distinguishes D from A, B, and C without needing the specific annotation of this exact protein.",
    "missing_item_specific_fact": "",
    "reason": "The GNAT-fold motif recognition is transferable structural/biochemical knowledge. The general association of N-acetyltransferases with amino-acid catabolism is a well-established biological pattern learned from many related proteins (e.g., amino-acid N-acetyltransferases in bacterial catabolic operons). The other three pathways are dominated by enzyme classes (hydrolases, oxidoreductases, nucleotide kinases) that are mechanistically and structurally distinct from acetyltransferases, providing a credible basis for elimination. The inference is probabilistic rather than certain, but it meaningfully distinguishes the offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four pathway choices involve clearly distinct enzyme classes. An acetyltransferase does not naturally fit carbohydrate degradation (hydrolases/lyases), tetrahydrofolate interconversion (oxidoreductases/specific transferases), or dTTP biosynthesis (nucleotide kinases). Only amino-acid degradation is a natural home for an N-acetyltransferase among the four options."
  },
  "important_caveats": [
    "The protein is a novel enzyme (EC 2.3.1.312, first characterized in 2023). The GNAT-fold motif recognition from a 332-AA sequence (larger than typical ~200-AA GNAT enzymes) may be non-trivial and the sequence may contain additional domains beyond the catalytic GNAT core.",
    "The specific D-glutamate substrate specificity is novel and not predictable from sequence alone; however, the question asks about the pathway class (amino-acid degradation), not the specific substrate, so this does not undermine the pathway-level inference.",
    "The pathway annotation carries evidence code ECO:0000305 (curator inference) for the pathway label, though the underlying function and catalytic activity are supported by experimental evidence (ECO:0000269).",
    "The UniProt entry was first released in April 2025; the benchmark author's source snapshot date is unknown, so the annotation may or may not have been available at benchmark construction time."
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
  "benchmark_sequence_length": 332,
  "benchmark_sequence_sha256": "d233fd888471e43669f332aeb0b2fac44fb59ce5fab9d43f3919864cdb20c35d",
  "current_entry_audit": {
    "entryVersion": 5,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 1
  },
  "current_record_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 332,
  "current_source_sequence_sha256": "d233fd888471e43669f332aeb0b2fac44fb59ce5fab9d43f3919864cdb20c35d",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 3,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DXZ1",
  "selected_historical_entry_version": 3,
  "selected_historical_record_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "selected_historical_source_sequence_length": 332,
  "selected_historical_source_sequence_sha256": "d233fd888471e43669f332aeb0b2fac44fb59ce5fab9d43f3919864cdb20c35d",
  "selected_historical_version": {
    "accession": "P0DXZ1",
    "database": "Swiss-Prot",
    "entryVersion": 3,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DGCN_PSEAS",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXZ1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":5,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Alteromonadales\",\"Pseudoalteromonadaceae\",\"Pseudoalteromonas\"],\"scientificName\":\"Pseudoalteromonas sp\",\"taxonId\":53249}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.312\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"D-glutamate N-acetyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"value\":\"Amino-acid degradation\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Yu Y.\",\"Wang P.\",\"Cao H.Y.\",\"Teng Z.J.\",\"Zhu Y.\",\"Wang M.\",\"McMinn A.\",\"Chen Y.\",\"Xiang H.\",\"Zhang Y.Z.\",\"Chen X.L.\",\"Zhang Y.Q.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36690779\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41396-023-01364-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"537\",\"id\":\"36690779\",\"journal\":\"ISME J.\",\"lastPage\":\"548\",\"publicationDate\":\"2023\",\"title\":\"Novel D-glutamate catabolic pathway in marine Proteobacteria and halophilic archaea.\",\"volume\":\"17\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"CF6-2\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"INDUCTION\",\"DISRUPTION PHENOTYPE\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H1",
  "excerpt": "ID   DGCN_PSEAS              Reviewed;         332 AA.\nAC   P0DXZ1;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 1.\nDT   28-JAN-2026, entry version 3.\nDE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};\nGN   Name=dgcN {ECO:0000303|PubMed:36690779};\nOS   Pseudoalteromonas sp.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Alteromonadales; Pseudoalteromonadaceae; Pseudoalteromonas.\nOX   NCBI_TaxID=53249;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, INDUCTION,\nRP   AND DISRUPTION PHENOTYPE.\nRC   STRAIN=CF6-2;\nRX   PubMed=36690779; DOI=10.1038/s41396-023-01364-6;\nRA   Yu Y., Wang P., Cao H.Y., Teng Z.J., Zhu Y., Wang M., McMinn A., Chen Y.,\nRA   Xiang H., Zhang Y.Z., Chen X.L., Zhang Y.Q.;\nRT   \"Novel D-glutamate catabolic pathway in marine Proteobacteria and\nRT   halophilic archaea.\";\nRL   ISME J. 17:537-548(2023).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 13-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid degradation. {ECO:0000305|PubMed:36690779}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 48-48",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 66. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
