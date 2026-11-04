# EC_number_0097

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0097.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 1.16.1.10

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTKIAEKSKQEYGDLLKEKDHLQDMEQLEMTIVSIQTPYPSIVRIQGKINTLQPELWQAPNLAIRLIVSNPPEGQPISRVYTVRSFNPINAQIEIDFVKHEDLSPAMEWLNSAQVGTKIGLIGPRPHFIPNFTAKKHVVMFADDTAVPALYSILKQWELGISADIFIESFEKDIASQLPELEHVKIHSFHKEHHTSQKGLLLKAAFALEHYENITIWAACERNEARALRQFFLEDQQLNKNDVRIAGYWRDGVSSSELDKLRAQHYQEHIQQGKTLNEYDDLDLAN

[Multiple Choices]
A. 1.16.1.10
B. 1.14.19.80
C. 4.1.1.129
D. 3.6.1.5
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence matches the UniProt entry, which assigns EC 1.16.1.10 and reports catalytic activity for both NAD+ and NADP+ reactions with experimental evidence (ECO:0000269). This supports choice A for the supplied protein, though the underlying study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is a compact, apparently soluble enzyme rather than a membrane protein. Transferable knowledge of enzyme families makes the membrane-associated desaturase-like option B a poor fit; the decarboxylase option C and ATP-hydrolyzing option D also imply different catalytic classes. A soluble flavin-dependent oxidoreductase is a credible fit for A among these choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Sequence and family-level patterns provide a meaningful basis for distinguishing A from the listed alternatives. They do not by themselves establish the exact siderophore substrate or prove the complete EC assignment, but the question asks the model to choose among a small set of substantially different enzyme classes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice is comparably supported by the sequence-level inference.


### Important caveats

- The experimental support comes from a UniProt annotation citing a study; that study was not independently examined.
- The exact reaction and EC number are more specific than can be established from the sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is a compact, apparently soluble enzyme rather than a membrane protein. Transferable knowledge of enzyme families makes the membrane-associated desaturase-like option B a poor fit; the decarboxylase option C and ATP-hydrolyzing option D also imply different catalytic classes. A soluble flavin-dependent oxidoreductase is a credible fit for A among these choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Sequence and family-level patterns provide a meaningful basis for distinguishing A from the listed alternatives. They do not by themselves establish the exact siderophore substrate or prove the complete EC assignment, but the question asks the model to choose among a small set of substantially different enzyme classes."
  },
  "case_id": "EC_number_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, which assigns EC 1.16.1.10 and reports catalytic activity for both NAD+ and NADP+ reactions with experimental evidence (ECO:0000269). This supports choice A for the supplied protein, though the underlying study was not independently reviewed here."
  },
  "important_caveats": [
    "The experimental support comes from a UniProt annotation citing a study; that study was not independently examined.",
    "The exact reaction and EC number are more specific than can be established from the sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence-level inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the UniProt entry, which assigns EC 1.16.1.10 and reports catalytic activity for both NAD+ and NADP+ reactions with experimental evidence (ECO:0000269). This supports choice A for the supplied protein, though the underlying study was not independently reviewed here.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is a compact, apparently soluble enzyme rather than a membrane protein. Transferable knowledge of enzyme families makes the membrane-associated desaturase-like option B a poor fit; the decarboxylase option C and ATP-hydrolyzing option D also imply different catalytic classes. A soluble flavin-dependent oxidoreductase is a credible fit for A among these choices.",
    "missing_item_specific_fact": "",
    "reason": "Sequence and family-level patterns provide a meaningful basis for distinguishing A from the listed alternatives. They do not by themselves establish the exact siderophore substrate or prove the complete EC assignment, but the question asks the model to choose among a small set of substantially different enzyme classes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence-level inference."
  },
  "important_caveats": [
    "The experimental support comes from a UniProt annotation citing a study; that study was not independently examined.",
    "The exact reaction and EC number are more specific than can be established from the sequence alone."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A1E3M8P2 (BAUF_ACIBA) annotates this 286-aa protein from Acinetobacter baumannii as Ferric acinetobactin reductase, EC 1.16.1.10, with experimental evidence code ECO:0000269 backed by PubMed:34308084 (X-ray crystallography at 2.85 Å in complex with FAD, plus biochemical characterization of catalytic activity). The catalytic reaction (2 Fe(II)-siderophore + NAD(P)+ + H+ → 2 Fe(III)-siderophore + NAD(P)H) is confirmed. The sequence matches exactly in both current and historical (v35) records.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four choices span four different EC classes (oxidoreductase-Fe, oxidoreductase-P450, lyase-decarboxylase, hydrolase-apyrase), enabling elimination-based reasoning. (1) EC 3.6.1.5 (apyrase/ATP diphosphohydrolase): Apyrases are typically 400–600 aa with Walker A (GxxxxGK&#91;T/S&#93;) and Walker B motifs; this 286-aa protein lacks these motifs, eliminating D. (2) EC 4.1.1.129 (decarboxylase): Carboxy-lyases of this class typically require PLP or divalent-metal binding motifs (e.g., the PLP-binding lysine or metal-coordinating His/Asp triads); no such features are evident, eliminating C. (3) EC 1.14.19.80 (cytochrome P450): P450s are 400–600 aa and carry the absolutely conserved heme-thiolate motif FxxGxxxCxG; no such motif is present, and the protein is far too small, eliminating B. (4) EC 1.16.1.10 (flavin-dependent siderophore-interacting protein): The 286-aa size is consistent with the flavin-dependent SIP family (~200–300 aa). Glycine-rich segments (e.g., 'GKINT', 'GPRPHFIP') are consistent with a Rossmann-like FAD-binding fold. Multiple His residues (HEDLSP, HKEHHTSQ, HYQEHIQQ) are consistent with the conserved His that stacks with the FAD isoalloxazine ring in characterized SIPs (e.g., Fes, Fiu). The absence of heme, PLP, and Walker motifs, combined with the small flavoprotein architecture, meaningfully distinguishes A from the other three choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The diverse EC-class alternatives allow a knowledgeable model to apply family-level structural and size constraints learned from other flavoproteins, P450s, apyrases, and decarboxylases to eliminate three choices and identify the flavin-dependent SIP oxidoreductase. The argument relies on transferable knowledge of protein-family signatures rather than memorization of this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices belong to distinct EC classes with well-established sequence/structural signatures. Size exclusion (286 aa vs. 400–600 aa for P450s and apyrases), absence of P450 heme-thiolate motif, absence of Walker A/B motifs, and absence of PLP/metal-binding decarboxylase features collectively leave only the flavoprotein oxidoreductase option defensible.


### Important caveats

- The FAD-binding motif in this sequence is not a perfect canonical GxGxxG Rossmann signature; it resembles the more variable flavin-binding motifs found in flavin-dependent SIPs specifically.
- The specific 4th digit (1.16.1.10 vs. other 1.16.x.x entries) would be harder to pin down from sequence alone, but the offered choices do not include competing 1.16.x.x alternatives, so the elimination logic suffices.
- The experimental evidence (PubMed:34308084, PDB 7LRN) confirms the annotation, but this evidence was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four choices span four different EC classes (oxidoreductase-Fe, oxidoreductase-P450, lyase-decarboxylase, hydrolase-apyrase), enabling elimination-based reasoning. (1) EC 3.6.1.5 (apyrase/ATP diphosphohydrolase): Apyrases are typically 400–600 aa with Walker A (GxxxxGK[T/S]) and Walker B motifs; this 286-aa protein lacks these motifs, eliminating D. (2) EC 4.1.1.129 (decarboxylase): Carboxy-lyases of this class typically require PLP or divalent-metal binding motifs (e.g., the PLP-binding lysine or metal-coordinating His/Asp triads); no such features are evident, eliminating C. (3) EC 1.14.19.80 (cytochrome P450): P450s are 400–600 aa and carry the absolutely conserved heme-thiolate motif FxxGxxxCxG; no such motif is present, and the protein is far too small, eliminating B. (4) EC 1.16.1.10 (flavin-dependent siderophore-interacting protein): The 286-aa size is consistent with the flavin-dependent SIP family (~200–300 aa). Glycine-rich segments (e.g., 'GKINT', 'GPRPHFIP') are consistent with a Rossmann-like FAD-binding fold. Multiple His residues (HEDLSP, HKEHHTSQ, HYQEHIQQ) are consistent with the conserved His that stacks with the FAD isoalloxazine ring in characterized SIPs (e.g., Fes, Fiu). The absence of heme, PLP, and Walker motifs, combined with the small flavoprotein architecture, meaningfully distinguishes A from the other three choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The diverse EC-class alternatives allow a knowledgeable model to apply family-level structural and size constraints learned from other flavoproteins, P450s, apyrases, and decarboxylases to eliminate three choices and identify the flavin-dependent SIP oxidoreductase. The argument relies on transferable knowledge of protein-family signatures rather than memorization of this specific entry's annotation."
  },
  "case_id": "EC_number_0097",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H2",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A1E3M8P2 (BAUF_ACIBA) annotates this 286-aa protein from Acinetobacter baumannii as Ferric acinetobactin reductase, EC 1.16.1.10, with experimental evidence code ECO:0000269 backed by PubMed:34308084 (X-ray crystallography at 2.85 Å in complex with FAD, plus biochemical characterization of catalytic activity). The catalytic reaction (2 Fe(II)-siderophore + NAD(P)+ + H+ → 2 Fe(III)-siderophore + NAD(P)H) is confirmed. The sequence matches exactly in both current and historical (v35) records."
  },
  "important_caveats": [
    "The FAD-binding motif in this sequence is not a perfect canonical GxGxxG Rossmann signature; it resembles the more variable flavin-binding motifs found in flavin-dependent SIPs specifically.",
    "The specific 4th digit (1.16.1.10 vs. other 1.16.x.x entries) would be harder to pin down from sequence alone, but the offered choices do not include competing 1.16.x.x alternatives, so the elimination logic suffices.",
    "The experimental evidence (PubMed:34308084, PDB 7LRN) confirms the annotation, but this evidence was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices belong to distinct EC classes with well-established sequence/structural signatures. Size exclusion (286 aa vs. 400–600 aa for P450s and apyrases), absence of P450 heme-thiolate motif, absence of Walker A/B motifs, and absence of PLP/metal-binding decarboxylase features collectively leave only the flavoprotein oxidoreductase option defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0097",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A1E3M8P2 (BAUF_ACIBA) annotates this 286-aa protein from Acinetobacter baumannii as Ferric acinetobactin reductase, EC 1.16.1.10, with experimental evidence code ECO:0000269 backed by PubMed:34308084 (X-ray crystallography at 2.85 Å in complex with FAD, plus biochemical characterization of catalytic activity). The catalytic reaction (2 Fe(II)-siderophore + NAD(P)+ + H+ → 2 Fe(III)-siderophore + NAD(P)H) is confirmed. The sequence matches exactly in both current and historical (v35) records.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H2", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four choices span four different EC classes (oxidoreductase-Fe, oxidoreductase-P450, lyase-decarboxylase, hydrolase-apyrase), enabling elimination-based reasoning. (1) EC 3.6.1.5 (apyrase/ATP diphosphohydrolase): Apyrases are typically 400–600 aa with Walker A (GxxxxGK[T/S]) and Walker B motifs; this 286-aa protein lacks these motifs, eliminating D. (2) EC 4.1.1.129 (decarboxylase): Carboxy-lyases of this class typically require PLP or divalent-metal binding motifs (e.g., the PLP-binding lysine or metal-coordinating His/Asp triads); no such features are evident, eliminating C. (3) EC 1.14.19.80 (cytochrome P450): P450s are 400–600 aa and carry the absolutely conserved heme-thiolate motif FxxGxxxCxG; no such motif is present, and the protein is far too small, eliminating B. (4) EC 1.16.1.10 (flavin-dependent siderophore-interacting protein): The 286-aa size is consistent with the flavin-dependent SIP family (~200–300 aa). Glycine-rich segments (e.g., 'GKINT', 'GPRPHFIP') are consistent with a Rossmann-like FAD-binding fold. Multiple His residues (HEDLSP, HKEHHTSQ, HYQEHIQQ) are consistent with the conserved His that stacks with the FAD isoalloxazine ring in characterized SIPs (e.g., Fes, Fiu). The absence of heme, PLP, and Walker motifs, combined with the small flavoprotein architecture, meaningfully distinguishes A from the other three choices.",
    "missing_item_specific_fact": "",
    "reason": "The diverse EC-class alternatives allow a knowledgeable model to apply family-level structural and size constraints learned from other flavoproteins, P450s, apyrases, and decarboxylases to eliminate three choices and identify the flavin-dependent SIP oxidoreductase. The argument relies on transferable knowledge of protein-family signatures rather than memorization of this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices belong to distinct EC classes with well-established sequence/structural signatures. Size exclusion (286 aa vs. 400–600 aa for P450s and apyrases), absence of P450 heme-thiolate motif, absence of Walker A/B motifs, and absence of PLP/metal-binding decarboxylase features collectively leave only the flavoprotein oxidoreductase option defensible."
  },
  "important_caveats": [
    "The FAD-binding motif in this sequence is not a perfect canonical GxGxxG Rossmann signature; it resembles the more variable flavin-binding motifs found in flavin-dependent SIPs specifically.",
    "The specific 4th digit (1.16.1.10 vs. other 1.16.x.x entries) would be harder to pin down from sequence alone, but the offered choices do not include competing 1.16.x.x alternatives, so the elimination logic suffices.",
    "The experimental evidence (PubMed:34308084, PDB 7LRN) confirms the annotation, but this evidence was not available to the evaluated model."
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
  "benchmark_sequence_length": 286,
  "benchmark_sequence_sha256": "69db519277a1b220b6f5ad165e8b2558cee0754be3f6745d9bf8c017a90dd9e3",
  "current_entry_audit": {
    "entryVersion": 37,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-01-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 286,
  "current_source_sequence_sha256": "69db519277a1b220b6f5ad165e8b2558cee0754be3f6745d9bf8c017a90dd9e3",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 35,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A1E3M8P2",
  "selected_historical_entry_version": 35,
  "selected_historical_record_sha256": "21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746",
  "selected_historical_source_sequence_length": 286,
  "selected_historical_source_sequence_sha256": "69db519277a1b220b6f5ad165e8b2558cee0754be3f6745d9bf8c017a90dd9e3",
  "selected_historical_version": {
    "accession": "A0A1E3M8P2",
    "database": "Swiss-Prot",
    "entryVersion": 35,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BAUF_ACIBA",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1E3M8P2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:33.445950+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":37,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-01-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:33.445950+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Moraxellales\",\"Moraxellaceae\",\"Acinetobacter\",\"Acinetobacter calcoaceticus/baumannii complex\"],\"scientificName\":\"Acinetobacter baumannii\",\"taxonId\":470}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:33.445950+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34308084\",\"source\":\"PubMed\"}],\"value\":\"Flavin-dependent siderophore-interacting protein\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34308084\",\"source\":\"PubMed\"}],\"value\":\"Flavin-dependent SIP\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34308084\",\"source\":\"PubMed\"}],\"value\":\"1.16.1.10\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Ferric acinetobactin reductase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:33.445950+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34308084\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:15063\"}}],\"reaction\":{\"ecNumber\":\"1.16.1.10\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34308084\",\"source\":\"PubMed\"}],\"name\":\"2 a Fe(II)-siderophore + NAD(+) + H(+) = 2 a Fe(III)-siderophore + NADH\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:15061\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11342\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11344\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29033\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29034\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57540\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57945\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:33.445950+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"right-to-left\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34308084\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:28797\"}}],\"reaction\":{\"ecNumber\":\"1.16.1.10\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34308084\",\"source\":\"PubMed\"}],\"name\":\"2 a Fe(II)-siderophore + NADP(+) + H(+) = 2 a Fe(III)-siderophore + NADPH\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:28795\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11342\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11344\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29033\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29034\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57783\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58349\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:33.445950+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Valentino H.\",\"Korasick D.A.\",\"Bohac T.J.\",\"Shapiro J.A.\",\"Wencewicz T.A.\",\"Tanner J.J.\",\"Sobrado P.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34308084\"},{\"database\":\"DOI\",\"id\":\"10.1021/acsomega.1c03047\"}],\"citationType\":\"journal article\",\"firstPage\":\"18537\",\"id\":\"34308084\",\"journal\":\"ACS Omega\",\"lastPage\":\"18547\",\"publicationDate\":\"2021\",\"title\":\"Structural and Biochemical Characterization of the Flavin-Dependent Siderophore-Interacting Protein from Acinetobacter baumannii.\",\"volume\":\"6\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"7LRN\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 17978 / DSM 105126 / CIP 53.77 / LMG 1025 / NCDC KC755 / 5377\"}],\"referenceNumber\":2,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.85 ANGSTROMS) IN COMPLEX WITH FAD\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"COFACTOR\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:33.445950+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "27262ada0697001eda3da1d3769c61657664eca5dc8977cc9c5dbaec21268418",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1E3M8P2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)

```json
{
  "entry_version": 35,
  "evidence_id": "H1",
  "excerpt": "ID   BAUF_ACIBA              Reviewed;         286 AA.\nAC   A0A1E3M8P2;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JAN-2017, sequence version 1.\nDT   28-JAN-2026, entry version 35.\nDE   RecName: Full=Ferric acinetobactin reductase {ECO:0000305};\nDE            EC=1.16.1.10 {ECO:0000269|PubMed:34308084};\nDE   AltName: Full=Flavin-dependent siderophore-interacting protein {ECO:0000303|PubMed:34308084};\nDE            Short=Flavin-dependent SIP {ECO:0000303|PubMed:34308084};\nGN   Name=bauF {ECO:0000303|PubMed:34308084};\nGN   ORFNames=AUO97_00860 {ECO:0000312|EMBL:APP29445.1};\nOS   Acinetobacter baumannii.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Moraxellales; Moraxellaceae; Acinetobacter;\nOC   Acinetobacter calcoaceticus/baumannii complex.\nOX   NCBI_TaxID=470;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:37.007835+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746",
  "url": "https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)

```json
{
  "entry_version": 35,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Ferric acinetobactin reductase {ECO:0000305};\nDE            EC=1.16.1.10 {ECO:0000269|PubMed:34308084};\nDE   AltName: Full=Flavin-dependent siderophore-interacting protein {ECO:0000303|PubMed:34308084};\nDE            Short=Flavin-dependent SIP {ECO:0000303|PubMed:34308084};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:37.007835+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746",
  "url": "https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)

```json
{
  "entry_version": 35,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0007744|PDB:7LRN}\nRP   X-RAY CRYSTALLOGRAPHY (2.85 ANGSTROMS) IN COMPLEX WITH FAD, FUNCTION,\nRP   CATALYTIC ACTIVITY, AND COFACTOR.\nRC   STRAIN=ATCC 17978 / DSM 105126 / CIP 53.77 / LMG 1025 / NCDC KC755 / 5377;\nRX   PubMed=34308084; DOI=10.1021/acsomega.1c03047;\nRA   Valentino H., Korasick D.A., Bohac T.J., Shapiro J.A., Wencewicz T.A.,\nRA   Tanner J.J., Sobrado P.;\nRT   \"Structural and Biochemical Characterization of the Flavin-Dependent\nRT   Siderophore-Interacting Protein from Acinetobacter baumannii.\";\nRL   ACS Omega 6:18537-18547(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:37.007835+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 22-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746",
  "url": "https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)

```json
{
  "entry_version": 35,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 a Fe(II)-siderophore + NAD(+) + H(+) = 2 a Fe(III)-\nCC         siderophore + NADH; Xref=Rhea:RHEA:15061, Rhea:RHEA-COMP:11342,\nCC         Rhea:RHEA-COMP:11344, ChEBI:CHEBI:15378, ChEBI:CHEBI:29033,\nCC         ChEBI:CHEBI:29034, ChEBI:CHEBI:57540, ChEBI:CHEBI:57945;\nCC         EC=1.16.1.10; Evidence={ECO:0000269|PubMed:34308084};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:15063;\nCC         Evidence={ECO:0000269|PubMed:34308084};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:37.007835+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746",
  "url": "https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35)

```json
{
  "entry_version": 35,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=2 a Fe(II)-siderophore + NADP(+) + H(+) = 2 a Fe(III)-\nCC         siderophore + NADPH; Xref=Rhea:RHEA:28795, Rhea:RHEA-COMP:11342,\nCC         Rhea:RHEA-COMP:11344, ChEBI:CHEBI:15378, ChEBI:CHEBI:29033,\nCC         ChEBI:CHEBI:29034, ChEBI:CHEBI:57783, ChEBI:CHEBI:58349;\nCC         EC=1.16.1.10; Evidence={ECO:0000269|PubMed:34308084};\nCC       PhysiologicalDirection=right-to-left; Xref=Rhea:RHEA:28797;\nCC         Evidence={ECO:0000269|PubMed:34308084};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:37.007835+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746",
  "url": "https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 97. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
