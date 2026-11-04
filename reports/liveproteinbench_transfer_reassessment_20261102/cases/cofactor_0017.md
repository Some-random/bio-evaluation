# cofactor_0017

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0017.txt)

**Task:** `cofactor`  
**Expected answer:** **A** — FAD

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
A. FAD
B. [2Fe-2S] cluster
C. Fe cation
D. Na(+)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt record annotates FAD as the cofactor with experimental evidence; the cited structure was also determined in complex with FAD. This supports choice A for the supplied sequence.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a compact soluble oxidoreductase, and its glycine-rich segment (GTKIGLIG) is a plausible nucleotide/flavin-binding feature. Transferable knowledge of flavin-dependent oxidoreductases makes FAD a meaningful choice over the alternatives; the sequence has no conspicuous cysteine-rich motif supporting an iron-sulfur cluster, and sodium is not a usual catalytic cofactor for this kind of soluble enzyme.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> These sequence and family-level clues provide a probabilistic basis for distinguishing FAD among the offered choices, although they do not establish the exact cofactor experimentally.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence supports FAD as the most defensible offered choice; no alternative is comparably supported.


### Important caveats

- The reviewer-only evidence supports the key but was not available as input to the evaluated model.
- The sequence-based cofactor inference is probabilistic; the source record provides the target-specific experimental support.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a compact soluble oxidoreductase, and its glycine-rich segment (GTKIGLIG) is a plausible nucleotide/flavin-binding feature. Transferable knowledge of flavin-dependent oxidoreductases makes FAD a meaningful choice over the alternatives; the sequence has no conspicuous cysteine-rich motif supporting an iron-sulfur cluster, and sodium is not a usual catalytic cofactor for this kind of soluble enzyme.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "These sequence and family-level clues provide a probabilistic basis for distinguishing FAD among the offered choices, although they do not establish the exact cofactor experimentally."
  },
  "case_id": "cofactor_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates FAD as the cofactor with experimental evidence; the cited structure was also determined in complex with FAD. This supports choice A for the supplied sequence."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key but was not available as input to the evaluated model.",
    "The sequence-based cofactor inference is probabilistic; the source record provides the target-specific experimental support."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence supports FAD as the most defensible offered choice; no alternative is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates FAD as the cofactor with experimental evidence; the cited structure was also determined in complex with FAD. This supports choice A for the supplied sequence.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a compact soluble oxidoreductase, and its glycine-rich segment (GTKIGLIG) is a plausible nucleotide/flavin-binding feature. Transferable knowledge of flavin-dependent oxidoreductases makes FAD a meaningful choice over the alternatives; the sequence has no conspicuous cysteine-rich motif supporting an iron-sulfur cluster, and sodium is not a usual catalytic cofactor for this kind of soluble enzyme.",
    "missing_item_specific_fact": "",
    "reason": "These sequence and family-level clues provide a probabilistic basis for distinguishing FAD among the offered choices, although they do not establish the exact cofactor experimentally."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence supports FAD as the most defensible offered choice; no alternative is comparably supported."
  },
  "important_caveats": [
    "The reviewer-only evidence supports the key but was not available as input to the evaluated model.",
    "The sequence-based cofactor inference is probabilistic; the source record provides the target-specific experimental support."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A1E3M8P2) explicitly annotates FAD as the cofactor with direct experimental evidence (ECO:0000269, PubMed:34308084). The X-ray crystallography structure (PDB 7LRN) confirms the protein in complex with FAD. The protein is named 'Flavin-dependent siderophore-interacting protein' and the alternative name explicitly includes 'Flavin-dependent SIP.' The EC number 1.16.1.10 (ferric reductase) is consistent with FAD-dependent electron transfer.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple transferable arguments distinguish FAD from the other choices. (1) Process of elimination: &#91;2Fe-2S&#93; clusters require Cys-rich motifs (e.g., CxxCxxC...C patterns typical of ferredoxins); this 286-AA sequence lacks such Cys clusters. Fe cation cofactors typically involve His/Asp/Glu triads or tetrad clusters; no obvious canonical iron-binding motif is present. Na(+) is an extraordinarily rare catalytic cofactor and is essentially never the primary cofactor for an oxidoreductase. (2) Family-level knowledge: The sequence length (~286 AA), bacterial origin, and overall hydrophobic-core composition are consistent with the siderophore-interacting protein (SIP) family, which is a well-characterized class of FAD-dependent flavoproteins in microbiology literature. SIPs (e.g., IsdG-like proteins, BauF homologs) universally use FAD for ferric-reductase electron transfer. (3) The presence of a degenerate Rossmann-like motif (e.g., 'GKINTL' near position 30, 'GTKIGL' near position 120) is consistent with flavin-binding folds found in many FAD-dependent oxidoreductases. Together, these arguments meaningfully favor FAD over the three distractors.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question can be answered by combining process-of-elimination reasoning (absence of Cys clusters, absence of metal-binding motifs, implausibility of Na+) with family-level knowledge that SIPs are FAD-dependent flavoproteins. The sequence features (size, hydrophobic composition, degenerate Rossmann-like motifs) are consistent with FAD-dependent oxidoreductases broadly, and the SIP family association is well-established transferable knowledge from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The distractors are clearly eliminable: &#91;2Fe-2S&#93; requires Cys-rich motifs absent here; Fe cation lacks a matching binding motif; Na(+) is not a plausible catalytic cofactor for a reductase. FAD is the only biochemically reasonable choice.


### Important caveats

- The Rossmann-like motifs in this sequence are degenerate and not canonical GxGxxG; family-level SIP knowledge strengthens the FAD assignment beyond what sequence motifs alone provide.
- The reviewer-only evidence confirms FAD experimentally (X-ray crystallography, PDB 7LRN), but this was not available to the evaluated model.
- The SIP family is well-known in microbiology, but a model without specific exposure to SIP literature would rely more heavily on the elimination argument.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple transferable arguments distinguish FAD from the other choices. (1) Process of elimination: [2Fe-2S] clusters require Cys-rich motifs (e.g., CxxCxxC...C patterns typical of ferredoxins); this 286-AA sequence lacks such Cys clusters. Fe cation cofactors typically involve His/Asp/Glu triads or tetrad clusters; no obvious canonical iron-binding motif is present. Na(+) is an extraordinarily rare catalytic cofactor and is essentially never the primary cofactor for an oxidoreductase. (2) Family-level knowledge: The sequence length (~286 AA), bacterial origin, and overall hydrophobic-core composition are consistent with the siderophore-interacting protein (SIP) family, which is a well-characterized class of FAD-dependent flavoproteins in microbiology literature. SIPs (e.g., IsdG-like proteins, BauF homologs) universally use FAD for ferric-reductase electron transfer. (3) The presence of a degenerate Rossmann-like motif (e.g., 'GKINTL' near position 30, 'GTKIGL' near position 120) is consistent with flavin-binding folds found in many FAD-dependent oxidoreductases. Together, these arguments meaningfully favor FAD over the three distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question can be answered by combining process-of-elimination reasoning (absence of Cys clusters, absence of metal-binding motifs, implausibility of Na+) with family-level knowledge that SIPs are FAD-dependent flavoproteins. The sequence features (size, hydrophobic composition, degenerate Rossmann-like motifs) are consistent with FAD-dependent oxidoreductases broadly, and the SIP family association is well-established transferable knowledge from other proteins."
  },
  "case_id": "cofactor_0017",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A1E3M8P2) explicitly annotates FAD as the cofactor with direct experimental evidence (ECO:0000269, PubMed:34308084). The X-ray crystallography structure (PDB 7LRN) confirms the protein in complex with FAD. The protein is named 'Flavin-dependent siderophore-interacting protein' and the alternative name explicitly includes 'Flavin-dependent SIP.' The EC number 1.16.1.10 (ferric reductase) is consistent with FAD-dependent electron transfer."
  },
  "important_caveats": [
    "The Rossmann-like motifs in this sequence are degenerate and not canonical GxGxxG; family-level SIP knowledge strengthens the FAD assignment beyond what sequence motifs alone provide.",
    "The reviewer-only evidence confirms FAD experimentally (X-ray crystallography, PDB 7LRN), but this was not available to the evaluated model.",
    "The SIP family is well-known in microbiology, but a model without specific exposure to SIP literature would rely more heavily on the elimination argument."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors are clearly eliminable: [2Fe-2S] requires Cys-rich motifs absent here; Fe cation lacks a matching binding motif; Na(+) is not a plausible catalytic cofactor for a reductase. FAD is the only biochemically reasonable choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0017",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A1E3M8P2) explicitly annotates FAD as the cofactor with direct experimental evidence (ECO:0000269, PubMed:34308084). The X-ray crystallography structure (PDB 7LRN) confirms the protein in complex with FAD. The protein is named 'Flavin-dependent siderophore-interacting protein' and the alternative name explicitly includes 'Flavin-dependent SIP.' The EC number 1.16.1.10 (ferric reductase) is consistent with FAD-dependent electron transfer.",
    "evidence_ids": ["C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple transferable arguments distinguish FAD from the other choices. (1) Process of elimination: [2Fe-2S] clusters require Cys-rich motifs (e.g., CxxCxxC...C patterns typical of ferredoxins); this 286-AA sequence lacks such Cys clusters. Fe cation cofactors typically involve His/Asp/Glu triads or tetrad clusters; no obvious canonical iron-binding motif is present. Na(+) is an extraordinarily rare catalytic cofactor and is essentially never the primary cofactor for an oxidoreductase. (2) Family-level knowledge: The sequence length (~286 AA), bacterial origin, and overall hydrophobic-core composition are consistent with the siderophore-interacting protein (SIP) family, which is a well-characterized class of FAD-dependent flavoproteins in microbiology literature. SIPs (e.g., IsdG-like proteins, BauF homologs) universally use FAD for ferric-reductase electron transfer. (3) The presence of a degenerate Rossmann-like motif (e.g., 'GKINTL' near position 30, 'GTKIGL' near position 120) is consistent with flavin-binding folds found in many FAD-dependent oxidoreductases. Together, these arguments meaningfully favor FAD over the three distractors.",
    "missing_item_specific_fact": "",
    "reason": "The question can be answered by combining process-of-elimination reasoning (absence of Cys clusters, absence of metal-binding motifs, implausibility of Na+) with family-level knowledge that SIPs are FAD-dependent flavoproteins. The sequence features (size, hydrophobic composition, degenerate Rossmann-like motifs) are consistent with FAD-dependent oxidoreductases broadly, and the SIP family association is well-established transferable knowledge from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The distractors are clearly eliminable: [2Fe-2S] requires Cys-rich motifs absent here; Fe cation lacks a matching binding motif; Na(+) is not a plausible catalytic cofactor for a reductase. FAD is the only biochemically reasonable choice."
  },
  "important_caveats": [
    "The Rossmann-like motifs in this sequence are degenerate and not canonical GxGxxG; family-level SIP knowledge strengthens the FAD assignment beyond what sequence motifs alone provide.",
    "The reviewer-only evidence confirms FAD experimentally (X-ray crystallography, PDB 7LRN), but this was not available to the evaluated model.",
    "The SIP family is well-known in microbiology, but a model without specific exposure to SIP literature would rely more heavily on the elimination argument."
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
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34308084\",\"source\":\"PubMed\"}],\"name\":\"FAD\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
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
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FAD; Xref=ChEBI:CHEBI:57692;\nCC         Evidence={ECO:0000269|PubMed:34308084};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:37.007835+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 59-61",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "21245d159df4b708ad492dd55bbbd986a27609a5d66677beffd60475a84e1746",
  "url": "https://rest.uniprot.org/unisave/A0A1E3M8P2?format=txt&versions=35"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 17. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
