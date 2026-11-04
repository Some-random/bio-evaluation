# EC_number_0050

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0050.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 3.6.1.74

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATPKSFRDNLAEILKTHDFRTVELEFRLGFQAPGEFITNINKHVWTTAKEKLGTPAQELVMVDKYIRSTPGESSRYVVFPDGQGYWEHKKKVAKETTTGGKYGVRSAFSLERRENGKPPVSFRMQRTKYRTTFVKGPWKIDFTRVESIPATDRDCESTYEIEVELYDMFYLFEKELDIIIQEGNKLVQSIVM

[Multiple Choices]
A. 3.6.1.5
B. 3.6.1.74
C. 1.5.1.38
D. 1.1.1.138
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

> The sequence matches the annotated protein, and the supplied catalytic-activity evidence assigns it EC 3.6.1.74 for RNA 5′-end triphosphate hydrolysis. That evidence is linked to an experimental evidence code and a cited study, though the study itself was not independently reviewed here.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 193-residue sequence is a compact enzyme and lacks an obvious Rossmann-type cofactor-binding motif or a Walker A nucleotide-binding motif, making the oxidoreductase choices and an ATP-diphosphatase choice less fitting. Transferable knowledge of compact RNA-triphosphatase enzymes makes EC 3.6.1.74 a defensible best fit among these options. This is a probabilistic family-level inference, not a definitive assignment from sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The choices include substantially different enzyme classes, and sequence/family patterns provide a meaningful basis for preferring B without recalling this exact protein's record. The distinction from another phosphohydrolase is less certain than the distinction from the oxidoreductases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No second option is comparably supported by the supplied evidence; the expected EC number is experimentally supported for the matching sequence.


### Important caveats

- The sequence does not by itself establish the exact reaction with certainty.
- Reviewer-only organism and protein annotations were not treated as original model input.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 193-residue sequence is a compact enzyme and lacks an obvious Rossmann-type cofactor-binding motif or a Walker A nucleotide-binding motif, making the oxidoreductase choices and an ATP-diphosphatase choice less fitting. Transferable knowledge of compact RNA-triphosphatase enzymes makes EC 3.6.1.74 a defensible best fit among these options. This is a probabilistic family-level inference, not a definitive assignment from sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The choices include substantially different enzyme classes, and sequence/family patterns provide a meaningful basis for preferring B without recalling this exact protein's record. The distinction from another phosphohydrolase is less certain than the distinction from the oxidoreductases."
  },
  "case_id": "EC_number_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and the supplied catalytic-activity evidence assigns it EC 3.6.1.74 for RNA 5′-end triphosphate hydrolysis. That evidence is linked to an experimental evidence code and a cited study, though the study itself was not independently reviewed here."
  },
  "important_caveats": [
    "The sequence does not by itself establish the exact reaction with certainty.",
    "Reviewer-only organism and protein annotations were not treated as original model input."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second option is comparably supported by the supplied evidence; the expected EC number is experimentally supported for the matching sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and the supplied catalytic-activity evidence assigns it EC 3.6.1.74 for RNA 5′-end triphosphate hydrolysis. That evidence is linked to an experimental evidence code and a cited study, though the study itself was not independently reviewed here.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 193-residue sequence is a compact enzyme and lacks an obvious Rossmann-type cofactor-binding motif or a Walker A nucleotide-binding motif, making the oxidoreductase choices and an ATP-diphosphatase choice less fitting. Transferable knowledge of compact RNA-triphosphatase enzymes makes EC 3.6.1.74 a defensible best fit among these options. This is a probabilistic family-level inference, not a definitive assignment from sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "The choices include substantially different enzyme classes, and sequence/family patterns provide a meaningful basis for preferring B without recalling this exact protein's record. The distinction from another phosphohydrolase is less certain than the distinction from the oxidoreductases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No second option is comparably supported by the supplied evidence; the expected EC number is experimentally supported for the matching sequence."
  },
  "important_caveats": [
    "The sequence does not by itself establish the exact reaction with certainty.",
    "Reviewer-only organism and protein annotations were not treated as original model input."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence (C4, C5, H2, H4) confirms Q98500 (TPASE_PBCV1) is annotated as EC 3.6.1.74 (5'-RNA triphosphatase A449R) with experimental evidence (ECO:0000269, PubMed:11160672, Ho/Gong/Shuman 2001). The catalytic reaction is: a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end diphospho-ribonucleoside in mRNA + phosphate + H(+). The benchmark sequence (193 aa) matches the UniProt entry sequence exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 193-aa protein can be distinguished from the alternatives using general biochemical knowledge. EC 1.5.1.38 (DHFR) and EC 1.1.1.138 (3-hydroxyacyl-CoA dehydrogenase) require a Rossmann-fold NAD(P)-binding motif (GxGxxG) and are typically 150-300+ aa oxidoreductases; the sequence lacks any GxGxxG motif and has no structural hallmarks of a Rossmann fold. EC 3.6.1.5 (ATP diphosphohydrolase/apyrase) proteins are characteristically large multi-domain enzymes (typically 400-600+ aa) with Walker A/B motifs; a 193-aa protein is far too small. By elimination of the three clearly incompatible options, EC 3.6.1.74 (5'-RNA triphosphatase) remains. Positively, the small size, absence of cofactor-binding motifs, and phosphatase-type catalytic composition (EC 3.6 = acting on phosphoanhydride bonds) are consistent with a small metal-dependent phosphatase such as a 5'-RNA triphosphatase, a well-characterized class of small (~150-200 aa) viral and cellular enzymes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use general biochemical principles (Rossmann-fold requirement for oxidoreductases, size constraints on apyrases, phosphatase-superfamily size range) to eliminate options A, C, and D, leaving B. This is transferable knowledge from studying many enzyme families, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span two distinct EC classes (EC 1 = oxidoreductases vs EC 3 = hydrolases) and within EC 3.6.1.x the size and motif constraints clearly separate 3.6.1.5 from 3.6.1.74. No two options are equally defensible given the sequence features.


### Important caveats

- The elimination argument strongly rules out EC 1.5.1.38 and EC 1.1.1.138 (no Rossmann fold) and EC 3.6.1.5 (size too small for apyrase). The positive identification as specifically 3.6.1.74 rather than another small phosphatase relies on the fact that it is the only remaining option among the four choices.
- The experimental evidence (ECO:0000269) for the annotation comes from Ho, Gong, Shuman (2001), J. Virol. 75:1744-1750, characterizing the A449R triphosphatase activity of PBCV-1.
- The protein is from a large DNA virus (PBCV-1); viral capping enzymes are often small and structurally distinct from cellular counterparts, consistent with the observed sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 193-aa protein can be distinguished from the alternatives using general biochemical knowledge. EC 1.5.1.38 (DHFR) and EC 1.1.1.138 (3-hydroxyacyl-CoA dehydrogenase) require a Rossmann-fold NAD(P)-binding motif (GxGxxG) and are typically 150-300+ aa oxidoreductases; the sequence lacks any GxGxxG motif and has no structural hallmarks of a Rossmann fold. EC 3.6.1.5 (ATP diphosphohydrolase/apyrase) proteins are characteristically large multi-domain enzymes (typically 400-600+ aa) with Walker A/B motifs; a 193-aa protein is far too small. By elimination of the three clearly incompatible options, EC 3.6.1.74 (5'-RNA triphosphatase) remains. Positively, the small size, absence of cofactor-binding motifs, and phosphatase-type catalytic composition (EC 3.6 = acting on phosphoanhydride bonds) are consistent with a small metal-dependent phosphatase such as a 5'-RNA triphosphatase, a well-characterized class of small (~150-200 aa) viral and cellular enzymes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use general biochemical principles (Rossmann-fold requirement for oxidoreductases, size constraints on apyrases, phosphatase-superfamily size range) to eliminate options A, C, and D, leaving B. This is transferable knowledge from studying many enzyme families, not a lookup of this specific protein's annotation."
  },
  "case_id": "EC_number_0050",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence (C4, C5, H2, H4) confirms Q98500 (TPASE_PBCV1) is annotated as EC 3.6.1.74 (5'-RNA triphosphatase A449R) with experimental evidence (ECO:0000269, PubMed:11160672, Ho/Gong/Shuman 2001). The catalytic reaction is: a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end diphospho-ribonucleoside in mRNA + phosphate + H(+). The benchmark sequence (193 aa) matches the UniProt entry sequence exactly."
  },
  "important_caveats": [
    "The elimination argument strongly rules out EC 1.5.1.38 and EC 1.1.1.138 (no Rossmann fold) and EC 3.6.1.5 (size too small for apyrase). The positive identification as specifically 3.6.1.74 rather than another small phosphatase relies on the fact that it is the only remaining option among the four choices.",
    "The experimental evidence (ECO:0000269) for the annotation comes from Ho, Gong, Shuman (2001), J. Virol. 75:1744-1750, characterizing the A449R triphosphatase activity of PBCV-1.",
    "The protein is from a large DNA virus (PBCV-1); viral capping enzymes are often small and structurally distinct from cellular counterparts, consistent with the observed sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span two distinct EC classes (EC 1 = oxidoreductases vs EC 3 = hydrolases) and within EC 3.6.1.x the size and motif constraints clearly separate 3.6.1.5 from 3.6.1.74. No two options are equally defensible given the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0050",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence (C4, C5, H2, H4) confirms Q98500 (TPASE_PBCV1) is annotated as EC 3.6.1.74 (5'-RNA triphosphatase A449R) with experimental evidence (ECO:0000269, PubMed:11160672, Ho/Gong/Shuman 2001). The catalytic reaction is: a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end diphospho-ribonucleoside in mRNA + phosphate + H(+). The benchmark sequence (193 aa) matches the UniProt entry sequence exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 193-aa protein can be distinguished from the alternatives using general biochemical knowledge. EC 1.5.1.38 (DHFR) and EC 1.1.1.138 (3-hydroxyacyl-CoA dehydrogenase) require a Rossmann-fold NAD(P)-binding motif (GxGxxG) and are typically 150-300+ aa oxidoreductases; the sequence lacks any GxGxxG motif and has no structural hallmarks of a Rossmann fold. EC 3.6.1.5 (ATP diphosphohydrolase/apyrase) proteins are characteristically large multi-domain enzymes (typically 400-600+ aa) with Walker A/B motifs; a 193-aa protein is far too small. By elimination of the three clearly incompatible options, EC 3.6.1.74 (5'-RNA triphosphatase) remains. Positively, the small size, absence of cofactor-binding motifs, and phosphatase-type catalytic composition (EC 3.6 = acting on phosphoanhydride bonds) are consistent with a small metal-dependent phosphatase such as a 5'-RNA triphosphatase, a well-characterized class of small (~150-200 aa) viral and cellular enzymes.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use general biochemical principles (Rossmann-fold requirement for oxidoreductases, size constraints on apyrases, phosphatase-superfamily size range) to eliminate options A, C, and D, leaving B. This is transferable knowledge from studying many enzyme families, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span two distinct EC classes (EC 1 = oxidoreductases vs EC 3 = hydrolases) and within EC 3.6.1.x the size and motif constraints clearly separate 3.6.1.5 from 3.6.1.74. No two options are equally defensible given the sequence features."
  },
  "important_caveats": [
    "The elimination argument strongly rules out EC 1.5.1.38 and EC 1.1.1.138 (no Rossmann fold) and EC 3.6.1.5 (size too small for apyrase). The positive identification as specifically 3.6.1.74 rather than another small phosphatase relies on the fact that it is the only remaining option among the four choices.",
    "The experimental evidence (ECO:0000269) for the annotation comes from Ho, Gong, Shuman (2001), J. Virol. 75:1744-1750, characterizing the A449R triphosphatase activity of PBCV-1.",
    "The protein is from a large DNA virus (PBCV-1); viral capping enzymes are often small and structurally distinct from cellular counterparts, consistent with the observed sequence."
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
  "benchmark_sequence_length": 193,
  "benchmark_sequence_sha256": "2e3ef2dd5cc36f7f2ffcab76a32ce1bb6958f79ccde3e9c943bcd61f8649ed54",
  "current_entry_audit": {
    "entryVersion": 86,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1997-02-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 193,
  "current_source_sequence_sha256": "2e3ef2dd5cc36f7f2ffcab76a32ce1bb6958f79ccde3e9c943bcd61f8649ed54",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 85,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q98500",
  "selected_historical_entry_version": 85,
  "selected_historical_record_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "selected_historical_source_sequence_length": 193,
  "selected_historical_source_sequence_sha256": "2e3ef2dd5cc36f7f2ffcab76a32ce1bb6958f79ccde3e9c943bcd61f8649ed54",
  "selected_historical_version": {
    "accession": "Q98500",
    "database": "Swiss-Prot",
    "entryVersion": 85,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "TPASE_PBCV1",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q98500\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":86,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1997-02-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"PBCV-1\",\"lineage\":[\"Viruses\",\"Varidnaviria\",\"Bamfordvirae\",\"Nucleocytoviricota\",\"Megaviricetes\",\"Algavirales\",\"Phycodnaviridae\",\"Chlorovirus\",\"Chlorovirus vanettense\"],\"scientificName\":\"Paramecium bursaria Chlorella virus 1\",\"taxonId\":10506}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"value\":\"3.6.1.74\"}],\"fullName\":{\"value\":\"5'RNA triphosphatase A449R\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11160672\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:67005\"}}],\"reaction\":{\"ecNumber\":\"3.6.1.74\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"11160672\",\"source\":\"PubMed\"}],\"name\":\"a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end diphospho-ribonucleoside in mRNA + phosphate + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:67004\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:17164\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:17165\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:43474\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:167616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:167618\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q98500.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Ho C.K.\",\"Gong C.\",\"Shuman S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"11160672\"},{\"database\":\"DOI\",\"id\":\"10.1128/jvi.75.4.1744-1750.2001\"}],\"citationType\":\"journal article\",\"firstPage\":\"1744\",\"id\":\"11160672\",\"journal\":\"J. Virol.\",\"lastPage\":\"1750\",\"publicationDate\":\"2001\",\"title\":\"RNA triphosphatase component of the mRNA capping apparatus of Paramecium bursaria Chlorella virus 1.\",\"volume\":\"75\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CHARACTERIZATION OF TRIPHOSPHATASE ACTIVITY\",\"MUTAGENESIS OF GLU-26\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:32:37.911424+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "6c87eb1e93d56410573b8835a7e7ba07266a6e6668be9e06673d11fb8aae1750",
  "url": "https://rest.uniprot.org/uniprotkb/Q98500.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H1",
  "excerpt": "ID   TPASE_PBCV1             Reviewed;         193 AA.\nAC   Q98500;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-FEB-1997, sequence version 1.\nDT   28-JAN-2026, entry version 85.\nDE   RecName: Full=5'RNA triphosphatase A449R;\nDE            EC=3.6.1.74;\nGN   Name=A449R;\nOS   Paramecium bursaria Chlorella virus 1 (PBCV-1).\nOC   Viruses; Varidnaviria; Bamfordvirae; Nucleocytoviricota; Megaviricetes;\nOC   Algavirales; Phycodnaviridae; Chlorovirus; Chlorovirus vanettense.\nOX   NCBI_TaxID=10506;\nOH   NCBI_TaxID=3071; Chlorella.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=5'RNA triphosphatase A449R;\nDE            EC=3.6.1.74;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CHARACTERIZATION OF TRIPHOSPHATASE ACTIVITY, AND MUTAGENESIS OF\nRP   GLU-26.\nRX   PubMed=11160672; DOI=10.1128/jvi.75.4.1744-1750.2001;\nRA   Ho C.K., Gong C., Shuman S.;\nRT   \"RNA triphosphatase component of the mRNA capping apparatus of Paramecium\nRT   bursaria Chlorella virus 1.\";\nRL   J. Virol. 75:1744-1750(2001).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 21-28",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85)

```json
{
  "entry_version": 85,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a 5'-end triphospho-ribonucleoside in mRNA + H2O = a 5'-end\nCC         diphospho-ribonucleoside in mRNA + phosphate + H(+);\nCC         Xref=Rhea:RHEA:67004, Rhea:RHEA-COMP:17164, Rhea:RHEA-COMP:17165,\nCC         ChEBI:CHEBI:15377, ChEBI:CHEBI:15378, ChEBI:CHEBI:43474,\nCC         ChEBI:CHEBI:167616, ChEBI:CHEBI:167618; EC=3.6.1.74;\nCC         Evidence={ECO:0000269|PubMed:11160672};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:67005;\nCC         Evidence={ECO:0000269|PubMed:11160672};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:32:39.788206+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "18b726813fb89600400cf082d676e2e28e85ff6e785c91979666e63f364070dd",
  "url": "https://rest.uniprot.org/unisave/Q98500?format=txt&versions=85"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 50. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
