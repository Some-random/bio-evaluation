# pathway_0076

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0076.txt)

**Task:** `pathway`  
**Expected answer:** **D** — Secondary metabolite biosynthesis. .

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNPPPSLLDKAAIVTGGSRGIGAAIAIELARRGAHVLITYNTASHKAQLVAEEIQKLGRKATVVQASSTDREGPNRIVQAAVSQYGRIDIIVNNAGMADDCLLQDLTHEFWDRIMDVNLRLPAFLVQAALQHLGPAPRIVNISSLAARAGYNATSVYAASKAALEGMTRAWATELGHRYNVTVNCVNPGPVDTDIMAVDENTDAEVVAYWNAKVKETPAAPRVGTPGDIAQIVAFLCEEGSRWCTGSVVNANGGLVTV

[Multiple Choices]
A. molybdopterin biosynthesis. .
B. L-methionine biosynthesis via de novo pathway. .
C. chorismate from D-erythrose 4-phosphate and phosphoenolpyruvate: step 7/7. .
D. Secondary metabolite biosynthesis. .
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

> The sequence-matched UniProt record annotates the pathway as secondary metabolite biosynthesis and links that annotation to a publication on FR901483 biosynthesis. This supports D, although the excerpts do not independently establish the paper's experimental details.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a likely short-chain dehydrogenase/reductase signature: an N-terminal Rossmann-like TGxxxGxG motif and a conserved-looking YxxxK motif. Such enzymes commonly perform redox tailoring in specialized-metabolite biosynthesis. That is a credible fit for broad option D, whereas chorismate synthase and the named molybdopterin and methionine pathway choices are more specific pathway enzymes and are not strongly suggested by this SDR-like sequence. This is a probabilistic family-level inference, not a substrate assignment.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable SDR-family knowledge gives a meaningful basis to favor the broad secondary-metabolite option over the three specific alternatives, though sequence motifs alone do not prove the enzyme's pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The broad secondary-metabolite choice is meaningfully favored over the specific primary-pathway alternatives; no second option is comparably supported by the sequence.


### Important caveats

- The pathway annotation is linked to a publication, but the supplied excerpts do not include the paper's experimental results.
- An SDR-like motif indicates enzyme family, not a unique substrate or pathway.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a likely short-chain dehydrogenase/reductase signature: an N-terminal Rossmann-like TGxxxGxG motif and a conserved-looking YxxxK motif. Such enzymes commonly perform redox tailoring in specialized-metabolite biosynthesis. That is a credible fit for broad option D, whereas chorismate synthase and the named molybdopterin and methionine pathway choices are more specific pathway enzymes and are not strongly suggested by this SDR-like sequence. This is a probabilistic family-level inference, not a substrate assignment.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable SDR-family knowledge gives a meaningful basis to favor the broad secondary-metabolite option over the three specific alternatives, though sequence motifs alone do not prove the enzyme's pathway."
  },
  "case_id": "pathway_0076",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the pathway as secondary metabolite biosynthesis and links that annotation to a publication on FR901483 biosynthesis. This supports D, although the excerpts do not independently establish the paper's experimental details."
  },
  "important_caveats": [
    "The pathway annotation is linked to a publication, but the supplied excerpts do not include the paper's experimental results.",
    "An SDR-like motif indicates enzyme family, not a unique substrate or pathway."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broad secondary-metabolite choice is meaningfully favored over the specific primary-pathway alternatives; no second option is comparably supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates the pathway as secondary metabolite biosynthesis and links that annotation to a publication on FR901483 biosynthesis. This supports D, although the excerpts do not independently establish the paper's experimental details.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a likely short-chain dehydrogenase/reductase signature: an N-terminal Rossmann-like TGxxxGxG motif and a conserved-looking YxxxK motif. Such enzymes commonly perform redox tailoring in specialized-metabolite biosynthesis. That is a credible fit for broad option D, whereas chorismate synthase and the named molybdopterin and methionine pathway choices are more specific pathway enzymes and are not strongly suggested by this SDR-like sequence. This is a probabilistic family-level inference, not a substrate assignment.",
    "missing_item_specific_fact": "",
    "reason": "Transferable SDR-family knowledge gives a meaningful basis to favor the broad secondary-metabolite option over the three specific alternatives, though sequence motifs alone do not prove the enzyme's pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The broad secondary-metabolite choice is meaningfully favored over the specific primary-pathway alternatives; no second option is comparably supported by the sequence."
  },
  "important_caveats": [
    "The pathway annotation is linked to a publication, but the supplied excerpts do not include the paper's experimental results.",
    "An SDR-like motif indicates enzyme family, not a unique substrate or pathway."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A7T8F1N2, FRZI_CLASX) explicitly annotates the PATHWAY as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269, PubMed:33372776). The protein is FrzI, a short-chain dehydrogenase/reductase in the FR901483 biosynthesis cluster. FR901483 is an immunosuppressant secondary metabolite. The sequence matches the benchmark input exactly. Evidence C5 and H3 confirm the pathway annotation.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [C4](#evidence-c4), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains unmistakable short-chain dehydrogenase/reductase (SDR) family hallmarks: a Rossmann-fold NAD(P)-binding motif 'GGSRGIGAAIA' (GxGxxG pattern), a catalytic Ser in the 'TSS' region, and a C-terminal Tyr-Lys catalytic dyad ('YNT…K'). SDRs are among the most abundant enzyme classes in fungal secondary metabolite biosynthesis gene clusters (e.g., aflatoxin, fumonisin, lovastatin clusters all contain multiple SDR tailoring enzymes). By contrast, the other three options involve highly specific, well-characterized enzyme types that are NOT SDRs: (A) molybdopterin biosynthesis uses MoaD/MoeB-type transferases and MoaA radical SAM enzymes; (B) de novo methionine biosynthesis uses homoserine O-succinyltransferase (MetA), cystathionine gamma-synthase (MetB), and methionine synthase (MetE/MetH); (C) chorismate step 7 is chorismate synthase (AroC), a flavin-dependent enzyme. None of these are SDRs. A knowledgeable model recognizing the SDR fold and knowing that SDRs are ubiquitous in secondary metabolite clusters but absent from the specific enzyme rosters of molybdopterin, methionine, or chorismate pathways can confidently select D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The SDR family identification from the sequence is unambiguous (Rossmann fold, NAD-binding GxGxxG, catalytic tetrad). The strong statistical and mechanistic association of SDRs with secondary metabolite biosynthesis in fungi, combined with the clear mismatch of SDRs to the specific enzyme types required by options A, B, and C, provides a concrete transferable inference that meaningfully distinguishes D from the alternatives without needing to know this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The SDR identification is clear from the sequence motifs, and the elimination of A, B, and C is straightforward because those pathways require specific non-SDR enzyme types. D is the only option consistent with an SDR, and SDRs are overwhelmingly associated with secondary metabolite biosynthesis in fungal gene clusters. No ambiguity among the offered choices.


### Important caveats

- SDRs also participate in primary metabolism (e.g., alcohol dehydrogenases, steroid dehydrogenases), but none of the other three options correspond to primary metabolic SDR pathways, so the elimination logic still holds.
- The UniProt annotation is backed by experimental evidence (ECO:0000269) from the 2021 JACS paper on FR901483 biosynthesis, lending strong support to the pathway assignment.
- The organism (Cladobotryum sp., a fungus) is not provided in the model input, but the fungal SDR-in-secondary-metabolite-cluster pattern is sufficiently general to support the inference from sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains unmistakable short-chain dehydrogenase/reductase (SDR) family hallmarks: a Rossmann-fold NAD(P)-binding motif 'GGSRGIGAAIA' (GxGxxG pattern), a catalytic Ser in the 'TSS' region, and a C-terminal Tyr-Lys catalytic dyad ('YNT…K'). SDRs are among the most abundant enzyme classes in fungal secondary metabolite biosynthesis gene clusters (e.g., aflatoxin, fumonisin, lovastatin clusters all contain multiple SDR tailoring enzymes). By contrast, the other three options involve highly specific, well-characterized enzyme types that are NOT SDRs: (A) molybdopterin biosynthesis uses MoaD/MoeB-type transferases and MoaA radical SAM enzymes; (B) de novo methionine biosynthesis uses homoserine O-succinyltransferase (MetA), cystathionine gamma-synthase (MetB), and methionine synthase (MetE/MetH); (C) chorismate step 7 is chorismate synthase (AroC), a flavin-dependent enzyme. None of these are SDRs. A knowledgeable model recognizing the SDR fold and knowing that SDRs are ubiquitous in secondary metabolite clusters but absent from the specific enzyme rosters of molybdopterin, methionine, or chorismate pathways can confidently select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The SDR family identification from the sequence is unambiguous (Rossmann fold, NAD-binding GxGxxG, catalytic tetrad). The strong statistical and mechanistic association of SDRs with secondary metabolite biosynthesis in fungi, combined with the clear mismatch of SDRs to the specific enzyme types required by options A, B, and C, provides a concrete transferable inference that meaningfully distinguishes D from the alternatives without needing to know this exact protein's annotation."
  },
  "case_id": "pathway_0076",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "C4",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8F1N2, FRZI_CLASX) explicitly annotates the PATHWAY as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269, PubMed:33372776). The protein is FrzI, a short-chain dehydrogenase/reductase in the FR901483 biosynthesis cluster. FR901483 is an immunosuppressant secondary metabolite. The sequence matches the benchmark input exactly. Evidence C5 and H3 confirm the pathway annotation."
  },
  "important_caveats": [
    "SDRs also participate in primary metabolism (e.g., alcohol dehydrogenases, steroid dehydrogenases), but none of the other three options correspond to primary metabolic SDR pathways, so the elimination logic still holds.",
    "The UniProt annotation is backed by experimental evidence (ECO:0000269) from the 2021 JACS paper on FR901483 biosynthesis, lending strong support to the pathway assignment.",
    "The organism (Cladobotryum sp., a fungus) is not provided in the model input, but the fungal SDR-in-secondary-metabolite-cluster pattern is sufficiently general to support the inference from sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The SDR identification is clear from the sequence motifs, and the elimination of A, B, and C is straightforward because those pathways require specific non-SDR enzyme types. D is the only option consistent with an SDR, and SDRs are overwhelmingly associated with secondary metabolite biosynthesis in fungal gene clusters. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0076",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A7T8F1N2, FRZI_CLASX) explicitly annotates the PATHWAY as 'Secondary metabolite biosynthesis' with experimental evidence (ECO:0000269, PubMed:33372776). The protein is FrzI, a short-chain dehydrogenase/reductase in the FR901483 biosynthesis cluster. FR901483 is an immunosuppressant secondary metabolite. The sequence matches the benchmark input exactly. Evidence C5 and H3 confirm the pathway annotation.",
    "evidence_ids": ["C5", "H3", "C4", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains unmistakable short-chain dehydrogenase/reductase (SDR) family hallmarks: a Rossmann-fold NAD(P)-binding motif 'GGSRGIGAAIA' (GxGxxG pattern), a catalytic Ser in the 'TSS' region, and a C-terminal Tyr-Lys catalytic dyad ('YNT…K'). SDRs are among the most abundant enzyme classes in fungal secondary metabolite biosynthesis gene clusters (e.g., aflatoxin, fumonisin, lovastatin clusters all contain multiple SDR tailoring enzymes). By contrast, the other three options involve highly specific, well-characterized enzyme types that are NOT SDRs: (A) molybdopterin biosynthesis uses MoaD/MoeB-type transferases and MoaA radical SAM enzymes; (B) de novo methionine biosynthesis uses homoserine O-succinyltransferase (MetA), cystathionine gamma-synthase (MetB), and methionine synthase (MetE/MetH); (C) chorismate step 7 is chorismate synthase (AroC), a flavin-dependent enzyme. None of these are SDRs. A knowledgeable model recognizing the SDR fold and knowing that SDRs are ubiquitous in secondary metabolite clusters but absent from the specific enzyme rosters of molybdopterin, methionine, or chorismate pathways can confidently select D.",
    "missing_item_specific_fact": "",
    "reason": "The SDR family identification from the sequence is unambiguous (Rossmann fold, NAD-binding GxGxxG, catalytic tetrad). The strong statistical and mechanistic association of SDRs with secondary metabolite biosynthesis in fungi, combined with the clear mismatch of SDRs to the specific enzyme types required by options A, B, and C, provides a concrete transferable inference that meaningfully distinguishes D from the alternatives without needing to know this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The SDR identification is clear from the sequence motifs, and the elimination of A, B, and C is straightforward because those pathways require specific non-SDR enzyme types. D is the only option consistent with an SDR, and SDRs are overwhelmingly associated with secondary metabolite biosynthesis in fungal gene clusters. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "SDRs also participate in primary metabolism (e.g., alcohol dehydrogenases, steroid dehydrogenases), but none of the other three options correspond to primary metabolic SDR pathways, so the elimination logic still holds.",
    "The UniProt annotation is backed by experimental evidence (ECO:0000269) from the 2021 JACS paper on FR901483 biosynthesis, lending strong support to the pathway assignment.",
    "The organism (Cladobotryum sp., a fungus) is not provided in the model input, but the fungal SDR-in-secondary-metabolite-cluster pattern is sufficiently general to support the inference from sequence alone."
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
  "benchmark_sequence_length": 258,
  "benchmark_sequence_sha256": "900848c2f83044ac5f5a81d57e8b7d27cd6bc66d8b0cdb266bed700cbb1522de",
  "current_entry_audit": {
    "entryVersion": 18,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2021-06-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 258,
  "current_source_sequence_sha256": "900848c2f83044ac5f5a81d57e8b7d27cd6bc66d8b0cdb266bed700cbb1522de",
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
  "requested_accession": "A0A7T8F1N2",
  "selected_historical_entry_version": 16,
  "selected_historical_record_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "selected_historical_source_sequence_length": 258,
  "selected_historical_source_sequence_sha256": "900848c2f83044ac5f5a81d57e8b7d27cd6bc66d8b0cdb266bed700cbb1522de",
  "selected_historical_version": {
    "accession": "A0A7T8F1N2",
    "database": "Swiss-Prot",
    "entryVersion": 16,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "FRZI_CLASX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A7T8F1N2\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":18,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2021-06-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Hypocreaceae\",\"Cladobotryum\"],\"scientificName\":\"Cladobotryum sp\",\"taxonId\":2040732}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"FR901483 biosynthesis clusters protein I\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"1.1.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Short-chain dehydrogenase/reductase FrzI\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"33372776\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhang Z.\",\"Tamura Y.\",\"Tang M.\",\"Qiao T.\",\"Sato M.\",\"Otsu Y.\",\"Sasamura S.\",\"Taniguchi M.\",\"Watanabe K.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33372776\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.0c12352\"}],\"citationType\":\"journal article\",\"firstPage\":\"132\",\"id\":\"33372776\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"136\",\"publicationDate\":\"2021\",\"title\":\"Biosynthesis of the Immunosuppressant (-)-FR901483.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"11231\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:50.517832+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "a48d33ae046ca7d2880e19af31acc95da30a7d81466d9e58266bba934f1fdd76",
  "url": "https://rest.uniprot.org/uniprotkb/A0A7T8F1N2.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H1",
  "excerpt": "ID   FRZI_CLASX              Reviewed;         258 AA.\nAC   A0A7T8F1N2;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-JUN-2021, sequence version 1.\nDT   28-JAN-2026, entry version 16.\nDE   RecName: Full=Short-chain dehydrogenase/reductase FrzI {ECO:0000303|PubMed:33372776};\nDE            EC=1.1.1.- {ECO:0000269|PubMed:33372776};\nDE   AltName: Full=FR901483 biosynthesis clusters protein I {ECO:0000303|PubMed:33372776};\nGN   Name=FrzI {ECO:0000303|PubMed:33372776};\nOS   Cladobotryum sp.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Hypocreaceae; Cladobotryum.\nOX   NCBI_TaxID=2040732;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, CATALYTIC ACTIVITY, AND\nRP   PATHWAY.\nRC   STRAIN=11231;\nRX   PubMed=33372776; DOI=10.1021/jacs.0c12352;\nRA   Zhang Z., Tamura Y., Tang M., Qiao T., Sato M., Otsu Y., Sasamura S.,\nRA   Taniguchi M., Watanabe K., Tang Y.;\nRT   \"Biosynthesis of the Immunosuppressant (-)-FR901483.\";\nRL   J. Am. Chem. Soc. 143:132-136(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 14-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16)

```json
{
  "entry_version": 16,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis.\nCC       {ECO:0000269|PubMed:33372776}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:54.316010+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-64",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ea33ab978987653ceb1106c71afcee5b805fc9a5d38cccf91ee029364fdb1198",
  "url": "https://rest.uniprot.org/unisave/A0A7T8F1N2?format=txt&versions=16"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 76. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
