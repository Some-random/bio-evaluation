# catalytic_activity_0024

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0024.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)

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
A. (13S)-hydroperoxy-(9Z,11E,15Z)-octadecatrienoate = etherolenate + H2O
B. D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)
C. N-acetyl-D-glutamate = N-acetyl-L-glutamate
D. 2-hydroxyspheroidene + 2 reduced [2Fe-2S]-[ferredoxin] + O2 + 2 H(+) = 2,2-dihydroxyspheroidene + 2 oxidized [2Fe-2S]-[ferredoxin] + H2O
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

> The sequence-matched UniProt record reports the keyed D-glutamate acetyl-transfer reaction with experimental evidence cited to PubMed. This supports choice B for the supplied sequence; the other listed reactions are not this reaction.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> Whether this particular enzyme acetylates D-glutamate using acetyl-CoA or instead catalyzes racemization of N-acetyl-D-glutamate (the key distinction between B and C).


**Reason**

> Sequence length and apparent soluble-enzyme character make the membrane-associated carotenoid reaction and the much larger lipoxygenase-type reaction less plausible, but do not meaningfully distinguish acetyl transfer in B from racemization in C. The input gives no explicit family assignment or diagnostic feature that establishes which chemistry this enzyme performs; identifying the exact activity would require target-specific functional knowledge.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The source evidence supports B, and no other offered option is reported as the same reaction. Although the enzyme is also annotated for other substrates, those reactions are not among the choices.


### Important caveats

- The supporting annotation is linked to experimental evidence, but the primary study was not independently reviewed here.
- Reviewer-only source records match the supplied sequence; the author's exact source snapshot is unknown. Those records support the key but are not original inputs for the answerability judgment.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular enzyme acetylates D-glutamate using acetyl-CoA or instead catalyzes racemization of N-acetyl-D-glutamate (the key distinction between B and C).",
    "reason": "Sequence length and apparent soluble-enzyme character make the membrane-associated carotenoid reaction and the much larger lipoxygenase-type reaction less plausible, but do not meaningfully distinguish acetyl transfer in B from racemization in C. The input gives no explicit family assignment or diagnostic feature that establishes which chemistry this enzyme performs; identifying the exact activity would require target-specific functional knowledge."
  },
  "case_id": "catalytic_activity_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports the keyed D-glutamate acetyl-transfer reaction with experimental evidence cited to PubMed. This supports choice B for the supplied sequence; the other listed reactions are not this reaction."
  },
  "important_caveats": [
    "The supporting annotation is linked to experimental evidence, but the primary study was not independently reviewed here.",
    "Reviewer-only source records match the supplied sequence; the author's exact source snapshot is unknown. Those records support the key but are not original inputs for the answerability judgment."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source evidence supports B, and no other offered option is reported as the same reaction. Although the enzyme is also annotated for other substrates, those reactions are not among the choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports the keyed D-glutamate acetyl-transfer reaction with experimental evidence cited to PubMed. This supports choice B for the supplied sequence; the other listed reactions are not this reaction.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "Whether this particular enzyme acetylates D-glutamate using acetyl-CoA or instead catalyzes racemization of N-acetyl-D-glutamate (the key distinction between B and C).",
    "reason": "Sequence length and apparent soluble-enzyme character make the membrane-associated carotenoid reaction and the much larger lipoxygenase-type reaction less plausible, but do not meaningfully distinguish acetyl transfer in B from racemization in C. The input gives no explicit family assignment or diagnostic feature that establishes which chemistry this enzyme performs; identifying the exact activity would require target-specific functional knowledge."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The source evidence supports B, and no other offered option is reported as the same reaction. Although the enzyme is also annotated for other substrates, those reactions are not among the choices."
  },
  "important_caveats": [
    "The supporting annotation is linked to experimental evidence, but the primary study was not independently reviewed here.",
    "Reviewer-only source records match the supplied sequence; the author's exact source snapshot is unknown. Those records support the key but are not original inputs for the answerability judgment."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXZ1 (sequence matched, 332 AA) annotates this protein as 'D-glutamate N-acetyltransferase' (EC 2.3.1.312) with experimental evidence (ECO:0000269, PubMed:36690779). The recorded catalytic activity reaction 'D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)' exactly matches choice B. The evidence is from a 2023 ISME Journal paper describing a novel D-glutamate catabolic pathway, with direct functional characterization.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C8](#evidence-c8), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable GNAT (GCN5-related N-acetyltransferase) fold features: the basic KR-rich segment 'GKGYKRKGKR' (~position 150) corresponds to the canonical GNAT motif B; 'GILISGSGVAID' resembles the motif A region involved in acetyl-CoA binding; and 'GSLGLLHGS' aligns with motif C/D hydrophobic regions. GNAT proteins are transferases (EC 2.x.x.x) that catalyze acetyl group transfer from acetyl-CoA. Among the four choices, only B is a transferase reaction. Option A (lipoxygenase, EC 1.13.11.x) is an oxidoreductase requiring a 700+ AA protein with a specific lipoxygenase domain—far too large for this 332 AA sequence. Option C (racemase, EC 5.1.1.x) would require PLP-binding motifs (conserved lysine in a specific context) absent here. Option D (carotenoid hydroxylase, EC 1.14.x.x) is a membrane-associated oxidoreductase with conserved His clusters for Fe coordination and ferredoxin interaction domains, not matching this soluble ~332 AA protein. Thus, recognizing the GNAT fold and the protein's small size allows a model to eliminate A, C, and D as belonging to entirely different enzyme classes, leaving B as the only transferase option.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GNAT fold motifs (motif A, B, C/D patterns) are well-established transferable knowledge from hundreds of characterized acetyltransferases. The enzyme-class distinction (transferase vs. oxidoreductase vs. isomerase) is sufficient to select B among the four offered alternatives without needing to know the exact substrate specificity of this particular protein. The protein's small size (332 AA) further excludes lipoxygenases, and the absence of PLP-binding or Fe-coordinating motifs excludes racemases and hydroxylases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent four distinct enzyme classes (oxidoreductase/lyase, transferase, isomerase, oxidoreductase). The GNAT fold features and protein size uniquely point to the transferase option B. No other option is defensible given the sequence characteristics.


### Important caveats

- The specific substrate (D-glutamate vs. D-aspartate vs. D-glutamine) is not determinable from sequence alone—the UniProt entry also records activity on D-aspartate and D-glutamine (C6, C7). However, this does not affect the answer since only one transferase option is offered.
- GNAT fold recognition from raw sequence is a probabilistic pattern-matching task; the motifs here are somewhat degenerate compared to textbook GNAT examples, but the KR-rich region and GILISGSG pattern are still identifiable by a trained model.
- The annotation is from a 2023 publication (PubMed:36690779) with direct experimental evidence, and the UniProt entry was first released in April 2025, so the author's source snapshot timing is relevant but the sequence match is confirmed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable GNAT (GCN5-related N-acetyltransferase) fold features: the basic KR-rich segment 'GKGYKRKGKR' (~position 150) corresponds to the canonical GNAT motif B; 'GILISGSGVAID' resembles the motif A region involved in acetyl-CoA binding; and 'GSLGLLHGS' aligns with motif C/D hydrophobic regions. GNAT proteins are transferases (EC 2.x.x.x) that catalyze acetyl group transfer from acetyl-CoA. Among the four choices, only B is a transferase reaction. Option A (lipoxygenase, EC 1.13.11.x) is an oxidoreductase requiring a 700+ AA protein with a specific lipoxygenase domain—far too large for this 332 AA sequence. Option C (racemase, EC 5.1.1.x) would require PLP-binding motifs (conserved lysine in a specific context) absent here. Option D (carotenoid hydroxylase, EC 1.14.x.x) is a membrane-associated oxidoreductase with conserved His clusters for Fe coordination and ferredoxin interaction domains, not matching this soluble ~332 AA protein. Thus, recognizing the GNAT fold and the protein's small size allows a model to eliminate A, C, and D as belonging to entirely different enzyme classes, leaving B as the only transferase option.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GNAT fold motifs (motif A, B, C/D patterns) are well-established transferable knowledge from hundreds of characterized acetyltransferases. The enzyme-class distinction (transferase vs. oxidoreductase vs. isomerase) is sufficient to select B among the four offered alternatives without needing to know the exact substrate specificity of this particular protein. The protein's small size (332 AA) further excludes lipoxygenases, and the absence of PLP-binding or Fe-coordinating motifs excludes racemases and hydroxylases."
  },
  "case_id": "catalytic_activity_0024",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C8",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ1 (sequence matched, 332 AA) annotates this protein as 'D-glutamate N-acetyltransferase' (EC 2.3.1.312) with experimental evidence (ECO:0000269, PubMed:36690779). The recorded catalytic activity reaction 'D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)' exactly matches choice B. The evidence is from a 2023 ISME Journal paper describing a novel D-glutamate catabolic pathway, with direct functional characterization."
  },
  "important_caveats": [
    "The specific substrate (D-glutamate vs. D-aspartate vs. D-glutamine) is not determinable from sequence alone—the UniProt entry also records activity on D-aspartate and D-glutamine (C6, C7). However, this does not affect the answer since only one transferase option is offered.",
    "GNAT fold recognition from raw sequence is a probabilistic pattern-matching task; the motifs here are somewhat degenerate compared to textbook GNAT examples, but the KR-rich region and GILISGSG pattern are still identifiable by a trained model.",
    "The annotation is from a 2023 publication (PubMed:36690779) with direct experimental evidence, and the UniProt entry was first released in April 2025, so the author's source snapshot timing is relevant but the sequence match is confirmed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four distinct enzyme classes (oxidoreductase/lyase, transferase, isomerase, oxidoreductase). The GNAT fold features and protein size uniquely point to the transferase option B. No other option is defensible given the sequence characteristics."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0024",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXZ1 (sequence matched, 332 AA) annotates this protein as 'D-glutamate N-acetyltransferase' (EC 2.3.1.312) with experimental evidence (ECO:0000269, PubMed:36690779). The recorded catalytic activity reaction 'D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)' exactly matches choice B. The evidence is from a 2023 ISME Journal paper describing a novel D-glutamate catabolic pathway, with direct functional characterization.",
    "evidence_ids": ["C4", "C5", "C8", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable GNAT (GCN5-related N-acetyltransferase) fold features: the basic KR-rich segment 'GKGYKRKGKR' (~position 150) corresponds to the canonical GNAT motif B; 'GILISGSGVAID' resembles the motif A region involved in acetyl-CoA binding; and 'GSLGLLHGS' aligns with motif C/D hydrophobic regions. GNAT proteins are transferases (EC 2.x.x.x) that catalyze acetyl group transfer from acetyl-CoA. Among the four choices, only B is a transferase reaction. Option A (lipoxygenase, EC 1.13.11.x) is an oxidoreductase requiring a 700+ AA protein with a specific lipoxygenase domain—far too large for this 332 AA sequence. Option C (racemase, EC 5.1.1.x) would require PLP-binding motifs (conserved lysine in a specific context) absent here. Option D (carotenoid hydroxylase, EC 1.14.x.x) is a membrane-associated oxidoreductase with conserved His clusters for Fe coordination and ferredoxin interaction domains, not matching this soluble ~332 AA protein. Thus, recognizing the GNAT fold and the protein's small size allows a model to eliminate A, C, and D as belonging to entirely different enzyme classes, leaving B as the only transferase option.",
    "missing_item_specific_fact": "",
    "reason": "The GNAT fold motifs (motif A, B, C/D patterns) are well-established transferable knowledge from hundreds of characterized acetyltransferases. The enzyme-class distinction (transferase vs. oxidoreductase vs. isomerase) is sufficient to select B among the four offered alternatives without needing to know the exact substrate specificity of this particular protein. The protein's small size (332 AA) further excludes lipoxygenases, and the absence of PLP-binding or Fe-coordinating motifs excludes racemases and hydroxylases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four distinct enzyme classes (oxidoreductase/lyase, transferase, isomerase, oxidoreductase). The GNAT fold features and protein size uniquely point to the transferase option B. No other option is defensible given the sequence characteristics."
  },
  "important_caveats": [
    "The specific substrate (D-glutamate vs. D-aspartate vs. D-glutamine) is not determinable from sequence alone—the UniProt entry also records activity on D-aspartate and D-glutamine (C6, C7). However, this does not affect the answer since only one transferase option is offered.",
    "GNAT fold recognition from raw sequence is a probabilistic pattern-matching task; the motifs here are somewhat degenerate compared to textbook GNAT examples, but the KR-rich region and GILISGSG pattern are still identifiable by a trained model.",
    "The annotation is from a 2023 publication (PubMed:36690779) with direct experimental evidence, and the UniProt entry was first released in April 2025, so the author's source snapshot timing is relevant but the sequence match is confirmed."
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:76496\"}}],\"reaction\":{\"ecNumber\":\"2.3.1.312\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"name\":\"D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:76495\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29986\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:195260\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
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
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.1.312\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"name\":\"D-aspartate + acetyl-CoA = N-acetyl-D-aspartate + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:76551\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29990\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:195274\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.3.1.312\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"36690779\",\"source\":\"PubMed\"}],\"name\":\"D-glutamine + acetyl-CoA = N-acetyl-D-glutamine + CoA + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:76547\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57287\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57288\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58000\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:143880\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:29:58.706491+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "aa2463d659dcce0272e4a1954d2f0e0ac1de2519b56334e15e5b9a8b29cffa17",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXZ1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXZ1.json)

```json
{
  "evidence_id": "C8",
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
  "excerpt": "DE   RecName: Full=D-glutamate N-acetyltransferase {ECO:0000305};\nDE            EC=2.3.1.312 {ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
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

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-glutamate + acetyl-CoA = N-acetyl-D-glutamate + CoA + H(+);\nCC         Xref=Rhea:RHEA:76495, ChEBI:CHEBI:15378, ChEBI:CHEBI:29986,\nCC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57288, ChEBI:CHEBI:195260;\nCC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:76496;\nCC         Evidence={ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-37",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-aspartate + acetyl-CoA = N-acetyl-D-aspartate + CoA + H(+);\nCC         Xref=Rhea:RHEA:76551, ChEBI:CHEBI:15378, ChEBI:CHEBI:29990,\nCC         ChEBI:CHEBI:57287, ChEBI:CHEBI:57288, ChEBI:CHEBI:195274;\nCC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 38-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3)

```json
{
  "entry_version": 3,
  "evidence_id": "H6",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=D-glutamine + acetyl-CoA = N-acetyl-D-glutamine + CoA + H(+);\nCC         Xref=Rhea:RHEA:76547, ChEBI:CHEBI:15378, ChEBI:CHEBI:57287,\nCC         ChEBI:CHEBI:57288, ChEBI:CHEBI:58000, ChEBI:CHEBI:143880;\nCC         EC=2.3.1.312; Evidence={ECO:0000269|PubMed:36690779};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:30:00.858326+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 43-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f028fea1879dfe3aaa57742281e0eecbec1a2030f44e9354a914347ae6b4be60",
  "url": "https://rest.uniprot.org/unisave/P0DXZ1?format=txt&versions=3"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 24. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
