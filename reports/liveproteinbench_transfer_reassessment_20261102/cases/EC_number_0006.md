# EC_number_0006

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0006.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.3.1.322

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | lookup-dependent |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MNITILSKETIKPLAPTPHHHKYYKVSLLDQFAPSSYMPFIFFYPNKFADRDAAGILTQLKESLSQILTIYYPLAGRVKDTVYVECNDEGVEFIEAQANGSLSDFLKQPDIAALNNFLPRNGNGLEKGCSISPVAIKATVFECSGIVLGVCIFHKVVDAAAAGEFLQSWAKIGRGSKETVELPNFTSASSLFPPRESLSSKFVRDFDNFFFQGSKSFMRRFVFDATAITTLRTKATSEKVPNPSRVEALMEFVVQHLSTAFKTAKSETPETLMITHPVNLRKRIEPPLPDSTFGNVIWLAFAFYDCDPSETKIKPGDVVERVREAFAALDKESISELETDDAFTSLSELLESVYTNEKIKIYRFTSTCNMGFYDVDFGWGKPVWVAHMGNMVDYRCKQQIVFMETGHMSKDIELWLAAEEDELSVLEKNAEFLAYATPNPTIWLDSDGTN

[Multiple Choices]
A. 2.3.1.312
B. 2.3.1.322
C. 2.4.2.12
D. 5.3.99.13
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

> The sequence-matched UniProt annotation assigns EC 2.3.1.322 and records the acetyl-CoA-dependent reaction forming akuammiline from rhazimol. The annotation cites experimental evidence (ECO:0000269); the historical entry also contains this assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The HXXXD and DFGWG motifs are characteristic of BAHD-family acyltransferases, supporting an acyltransferase interpretation and making the phosphoribosyltransferase and isomerase choices less plausible. But that family-level inference does not establish the specific substrate and product needed to distinguish the two 2.3.1 choices.


**Missing item-specific fact**

> The enzyme's experimentally established substrate/product specificity: acetylation of rhazimol to form akuammiline, rather than the reaction assigned to choice A.


**Reason**

> The sequence supports a broad enzyme-family inference, but the offered acyltransferase alternatives require distinguishing specific catalytic reactions. The sequence motifs alone do not establish that specificity; the relevant reaction measurement or exact-protein annotation is absent from the original input.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The EC alternatives represent distinct reaction classifications. The evidence supports the author's specific choice, even though the original sequence alone does not resolve the substrate-specific distinction.


### Important caveats

- The cited UniProt evidence is experimental-coded and sequence-matched, but the primary paper was not independently reviewed here.
- Reviewer-only source identity and annotations were not part of the original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The HXXXD and DFGWG motifs are characteristic of BAHD-family acyltransferases, supporting an acyltransferase interpretation and making the phosphoribosyltransferase and isomerase choices less plausible. But that family-level inference does not establish the specific substrate and product needed to distinguish the two 2.3.1 choices.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The enzyme's experimentally established substrate/product specificity: acetylation of rhazimol to form akuammiline, rather than the reaction assigned to choice A.",
    "reason": "The sequence supports a broad enzyme-family inference, but the offered acyltransferase alternatives require distinguishing specific catalytic reactions. The sequence motifs alone do not establish that specificity; the relevant reaction measurement or exact-protein annotation is absent from the original input."
  },
  "case_id": "EC_number_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.3.1.322 and records the acetyl-CoA-dependent reaction forming akuammiline from rhazimol. The annotation cites experimental evidence (ECO:0000269); the historical entry also contains this assignment."
  },
  "important_caveats": [
    "The cited UniProt evidence is experimental-coded and sequence-matched, but the primary paper was not independently reviewed here.",
    "Reviewer-only source identity and annotations were not part of the original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EC alternatives represent distinct reaction classifications. The evidence supports the author's specific choice, even though the original sequence alone does not resolve the substrate-specific distinction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation assigns EC 2.3.1.322 and records the acetyl-CoA-dependent reaction forming akuammiline from rhazimol. The annotation cites experimental evidence (ECO:0000269); the historical entry also contains this assignment.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The HXXXD and DFGWG motifs are characteristic of BAHD-family acyltransferases, supporting an acyltransferase interpretation and making the phosphoribosyltransferase and isomerase choices less plausible. But that family-level inference does not establish the specific substrate and product needed to distinguish the two 2.3.1 choices.",
    "missing_item_specific_fact": "The enzyme's experimentally established substrate/product specificity: acetylation of rhazimol to form akuammiline, rather than the reaction assigned to choice A.",
    "reason": "The sequence supports a broad enzyme-family inference, but the offered acyltransferase alternatives require distinguishing specific catalytic reactions. The sequence motifs alone do not establish that specificity; the relevant reaction measurement or exact-protein annotation is absent from the original input."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The EC alternatives represent distinct reaction classifications. The evidence supports the author's specific choice, even though the original sequence alone does not resolve the substrate-specific distinction."
  },
  "important_caveats": [
    "The cited UniProt evidence is experimental-coded and sequence-matched, but the primary paper was not independently reviewed here.",
    "Reviewer-only source identity and annotations were not part of the original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A9E7LUL3 (sequence matched, 450 AA) annotates this protein as Akuammiline synthase 2 with EC 2.3.1.322, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction is rhazimol + acetyl-CoA = akuammiline + CoA + H(+). The sequence in the question matches the source entry exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence contains the DFGWG motif (visible near the C-terminus: 'DFGWGKPVWVAHMGNMVDYRCKQQIVFMETGHMSKDIELWLAAEEDELSVLEKNAEFLAYATPNPTIWLDSDGTN'), which is a hallmark of the BAHD acyltransferase superfamily. This allows elimination of option C (2.4.2.12, a glycosyltransferase) and option D (5.3.99.13, an isomerase) on family grounds. However, both remaining options A (2.3.1.312) and B (2.3.1.322) are acyltransferases within the same 2.3.1 subclass. Distinguishing between them requires knowing the specific substrate (rhazimol for 2.3.1.322) and product (akuammiline), which was determined experimentally (in vitro enzymatic assays in Wang et al. 2022). No obvious sequence motif or family-level subfamily feature in the provided 450-aa sequence distinguishes a rhazimol acetyltransferase from whatever substrate 2.3.1.312 acts upon, since BAHD acyltransferases with different substrate specificities often share high overall sequence identity and differ only at a few active-site positions not identifiable without structural or mutagenesis data.


**Missing item-specific fact**

> The specific substrate/product identity of this enzyme (rhazimol → akuammiline acetylation) was established by in vitro enzymatic characterization (PubMed:36349266). Without this experimental fact or knowledge of the exact EC number assignment for this protein, a model cannot distinguish 2.3.1.312 from 2.3.1.322 based on sequence features alone.


**Reason**

> While BAHD family recognition (via DFGWG motif) credibly eliminates C and D, the critical A-vs-B distinction between two 2.3.1.x acyltransferase EC numbers differing only in the last digit requires knowledge of this enzyme's specific catalytic reaction, which is an experimentally determined fact about this exact protein not inferable from general BAHD-family sequence patterns.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "B"
]
```

> Both A (2.3.1.312) and B (2.3.1.322) are acyltransferases in the same subclass. Without the specific experimental substrate data, a knowledgeable model could plausibly select either as a BAHD acyltransferase EC number. The distinction is not resolvable from sequence features alone.


### Important caveats

- The EC numbers 2.3.1.312 and 2.3.1.322 are very close in the EC hierarchy; the last-digit distinction reflects specific substrate assignment rather than a major mechanistic or structural class difference.
- The DFGWG motif is clearly present in the sequence, supporting BAHD family assignment and elimination of C and D.
- The organism (Alstonia scholaris) and pathway context (indole alkaloid biosynthesis) are not provided in the model input and cannot be inferred from the sequence alone.
- The annotation evidence code ECO:0000269 indicates direct experimental evidence (in vitro assay), not computational prediction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the DFGWG motif (visible near the C-terminus: 'DFGWGKPVWVAHMGNMVDYRCKQQIVFMETGHMSKDIELWLAAEEDELSVLEKNAEFLAYATPNPTIWLDSDGTN'), which is a hallmark of the BAHD acyltransferase superfamily. This allows elimination of option C (2.4.2.12, a glycosyltransferase) and option D (5.3.99.13, an isomerase) on family grounds. However, both remaining options A (2.3.1.312) and B (2.3.1.322) are acyltransferases within the same 2.3.1 subclass. Distinguishing between them requires knowing the specific substrate (rhazimol for 2.3.1.322) and product (akuammiline), which was determined experimentally (in vitro enzymatic assays in Wang et al. 2022). No obvious sequence motif or family-level subfamily feature in the provided 450-aa sequence distinguishes a rhazimol acetyltransferase from whatever substrate 2.3.1.312 acts upon, since BAHD acyltransferases with different substrate specificities often share high overall sequence identity and differ only at a few active-site positions not identifiable without structural or mutagenesis data.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The specific substrate/product identity of this enzyme (rhazimol → akuammiline acetylation) was established by in vitro enzymatic characterization (PubMed:36349266). Without this experimental fact or knowledge of the exact EC number assignment for this protein, a model cannot distinguish 2.3.1.312 from 2.3.1.322 based on sequence features alone.",
    "reason": "While BAHD family recognition (via DFGWG motif) credibly eliminates C and D, the critical A-vs-B distinction between two 2.3.1.x acyltransferase EC numbers differing only in the last digit requires knowledge of this enzyme's specific catalytic reaction, which is an experimentally determined fact about this exact protein not inferable from general BAHD-family sequence patterns."
  },
  "case_id": "EC_number_0006",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7LUL3 (sequence matched, 450 AA) annotates this protein as Akuammiline synthase 2 with EC 2.3.1.322, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction is rhazimol + acetyl-CoA = akuammiline + CoA + H(+). The sequence in the question matches the source entry exactly."
  },
  "important_caveats": [
    "The EC numbers 2.3.1.312 and 2.3.1.322 are very close in the EC hierarchy; the last-digit distinction reflects specific substrate assignment rather than a major mechanistic or structural class difference.",
    "The DFGWG motif is clearly present in the sequence, supporting BAHD family assignment and elimination of C and D.",
    "The organism (Alstonia scholaris) and pathway context (indole alkaloid biosynthesis) are not provided in the model input and cannot be inferred from the sequence alone.",
    "The annotation evidence code ECO:0000269 indicates direct experimental evidence (in vitro assay), not computational prediction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "B"
    ],
    "reason": "Both A (2.3.1.312) and B (2.3.1.322) are acyltransferases in the same subclass. Without the specific experimental substrate data, a knowledgeable model could plausibly select either as a BAHD acyltransferase EC number. The distinction is not resolvable from sequence features alone."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0006",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A9E7LUL3 (sequence matched, 450 AA) annotates this protein as Akuammiline synthase 2 with EC 2.3.1.322, supported by experimental evidence (ECO:0000269, PubMed:36349266). The catalytic reaction is rhazimol + acetyl-CoA = akuammiline + CoA + H(+). The sequence in the question matches the source entry exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence contains the DFGWG motif (visible near the C-terminus: 'DFGWGKPVWVAHMGNMVDYRCKQQIVFMETGHMSKDIELWLAAEEDELSVLEKNAEFLAYATPNPTIWLDSDGTN'), which is a hallmark of the BAHD acyltransferase superfamily. This allows elimination of option C (2.4.2.12, a glycosyltransferase) and option D (5.3.99.13, an isomerase) on family grounds. However, both remaining options A (2.3.1.312) and B (2.3.1.322) are acyltransferases within the same 2.3.1 subclass. Distinguishing between them requires knowing the specific substrate (rhazimol for 2.3.1.322) and product (akuammiline), which was determined experimentally (in vitro enzymatic assays in Wang et al. 2022). No obvious sequence motif or family-level subfamily feature in the provided 450-aa sequence distinguishes a rhazimol acetyltransferase from whatever substrate 2.3.1.312 acts upon, since BAHD acyltransferases with different substrate specificities often share high overall sequence identity and differ only at a few active-site positions not identifiable without structural or mutagenesis data.",
    "missing_item_specific_fact": "The specific substrate/product identity of this enzyme (rhazimol → akuammiline acetylation) was established by in vitro enzymatic characterization (PubMed:36349266). Without this experimental fact or knowledge of the exact EC number assignment for this protein, a model cannot distinguish 2.3.1.312 from 2.3.1.322 based on sequence features alone.",
    "reason": "While BAHD family recognition (via DFGWG motif) credibly eliminates C and D, the critical A-vs-B distinction between two 2.3.1.x acyltransferase EC numbers differing only in the last digit requires knowledge of this enzyme's specific catalytic reaction, which is an experimentally determined fact about this exact protein not inferable from general BAHD-family sequence patterns."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "B"],
    "reason": "Both A (2.3.1.312) and B (2.3.1.322) are acyltransferases in the same subclass. Without the specific experimental substrate data, a knowledgeable model could plausibly select either as a BAHD acyltransferase EC number. The distinction is not resolvable from sequence features alone."
  },
  "important_caveats": [
    "The EC numbers 2.3.1.312 and 2.3.1.322 are very close in the EC hierarchy; the last-digit distinction reflects specific substrate assignment rather than a major mechanistic or structural class difference.",
    "The DFGWG motif is clearly present in the sequence, supporting BAHD family assignment and elimination of C and D.",
    "The organism (Alstonia scholaris) and pathway context (indole alkaloid biosynthesis) are not provided in the model input and cannot be inferred from the sequence alone.",
    "The annotation evidence code ECO:0000269 indicates direct experimental evidence (in vitro assay), not computational prediction."
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
  "benchmark_sequence_length": 450,
  "benchmark_sequence_sha256": "62b3b72d1750fd9e23b46592068241b00c5ab48c8d92e89e25f8a38bb6497f71",
  "current_entry_audit": {
    "entryVersion": 15,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2023-05-03",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 450,
  "current_source_sequence_sha256": "62b3b72d1750fd9e23b46592068241b00c5ab48c8d92e89e25f8a38bb6497f71",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 13,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A9E7LUL3",
  "selected_historical_entry_version": 13,
  "selected_historical_record_sha256": "00a2ac636344439c8ae2680b8cbb49e3d24815db40f5db2b4288e120c98e1379",
  "selected_historical_source_sequence_length": 450,
  "selected_historical_source_sequence_sha256": "62b3b72d1750fd9e23b46592068241b00c5ab48c8d92e89e25f8a38bb6497f71",
  "selected_historical_version": {
    "accession": "A0A9E7LUL3",
    "database": "Swiss-Prot",
    "entryVersion": 13,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AKS2_ALSSC",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A9E7LUL3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:09.156747+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":15,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2023-05-03\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:09.156747+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Dogbane\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Alstonieae\",\"Alstonia\"],\"scientificName\":\"Alstonia scholaris\",\"synonyms\":[\"Echites scholaris\"],\"taxonId\":52822}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:09.156747+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"2.3.1.322\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"Akuammiline synthase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"value\":\"AsAKS2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:09.156747+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:79624\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.322\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36349266\",\"source\":\"PubMed\"}],\"name\":\"rhazimol + acetyl-CoA = akuammiline + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:79623\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:141879\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:230474\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:09.156747+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang Z.\",\"Xiao Y.\",\"Wu S.\",\"Chen J.\",\"Li A.\",\"Tatsis E.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"36349266\"},{\"database\":\"DOI\",\"id\":\"10.1039/d2sc03612f\"}],\"citationType\":\"journal article\",\"firstPage\":\"12389\",\"id\":\"36349266\",\"journal\":\"Chem. Sci.\",\"lastPage\":\"12395\",\"publicationDate\":\"2022\",\"title\":\"Deciphering and reprogramming the cyclization regioselectivity in bifurcation of indole alkaloid biosynthesis.\",\"volume\":\"13\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"URS65388.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:09.156747+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6d6c7e768e23601860f9dd4d1c638f99277782f49c413631010a3b801d3d53d4",
  "url": "https://rest.uniprot.org/uniprotkb/A0A9E7LUL3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H1",
  "excerpt": "ID   AKS2_ALSSC              Reviewed;         450 AA.\nAC   A0A9E7LUL3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   03-MAY-2023, sequence version 1.\nDT   28-JAN-2026, entry version 13.\nDE   RecName: Full=Akuammiline synthase 2 {ECO:0000303|PubMed:36349266};\nDE            Short=AsAKS2 {ECO:0000303|PubMed:36349266};\nDE            EC=2.3.1.322 {ECO:0000269|PubMed:36349266};\nGN   Name=AKS2 {ECO:0000303|PubMed:36349266};\nGN   Synonyms=BAHD5 {ECO:0000303|PubMed:36349266};\nOS   Alstonia scholaris (Dogbane) (Echites scholaris).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Alstonieae;\nOC   Alstonia.\nOX   NCBI_TaxID=52822;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.133287+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "00a2ac636344439c8ae2680b8cbb49e3d24815db40f5db2b4288e120c98e1379",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Akuammiline synthase 2 {ECO:0000303|PubMed:36349266};\nDE            Short=AsAKS2 {ECO:0000303|PubMed:36349266};\nDE            EC=2.3.1.322 {ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.133287+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "00a2ac636344439c8ae2680b8cbb49e3d24815db40f5db2b4288e120c98e1379",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:URS65388.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=36349266; DOI=10.1039/d2sc03612f;\nRA   Wang Z., Xiao Y., Wu S., Chen J., Li A., Tatsis E.C.;\nRT   \"Deciphering and reprogramming the cyclization regioselectivity in\nRT   bifurcation of indole alkaloid biosynthesis.\";\nRL   Chem. Sci. 13:12389-12395(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.133287+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "00a2ac636344439c8ae2680b8cbb49e3d24815db40f5db2b4288e120c98e1379",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13)

```json
{
  "entry_version": 13,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=rhazimol + acetyl-CoA = akuammiline + CoA + H(+);\nCC         Xref=Rhea:RHEA:79623, ChEBI:CHEBI:15378, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:57288, ChEBI:CHEBI:141879, ChEBI:CHEBI:230474;\nCC         EC=2.3.1.322; Evidence={ECO:0000269|PubMed:36349266};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:79624;\nCC         Evidence={ECO:0000269|PubMed:36349266};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:14.133287+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "00a2ac636344439c8ae2680b8cbb49e3d24815db40f5db2b4288e120c98e1379",
  "url": "https://rest.uniprot.org/unisave/A0A9E7LUL3?format=txt&versions=13"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 6. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
