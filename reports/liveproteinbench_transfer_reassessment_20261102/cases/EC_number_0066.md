# EC_number_0066

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0066.txt)

**Task:** `EC_number`  
**Expected answer:** **D** — 2.7.4.9

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSAGKRGALIIFEGCDRSGKTTQSRLLVELLKSKGIPTLPMNFPERSSSIGQVINSYLTNSKDLPDEVIHLMFSANRWEHINQVKEKLLEGTTLVVDRYSFSGVAYSAAKGLDFDWCYAPERGLIKPDAVFYLRAPPNDLTHRGQYGKERYEKVEFQGRVAEVFNRICSKEGSYFHQFDARQSVEDLHAQIASITEELLPKVATRPLDTLS

[Multiple Choices]
A. 2.7.2.4
B. 2.4.1.391
C. 3.6.1.5
D. 2.7.4.9
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

> The sequence matches the annotated protein sequence. UniProt assigns EC 2.7.4.9 and reports the experimentally evidenced reaction dTMP + ATP = dTDP + ADP, which supports choice D. It also reports activity on dUMP, but that does not contradict the keyed EC assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 211-residue sequence has a P-loop-like nucleotide-binding motif (including the GxxxxGKTT pattern) and is consistent with the compact nucleoside-monophosphate-kinase family. That family-level inference makes a nucleotide kinase far more plausible than the glycosyltransferase (B) or ATP-hydrolysis option (C); the short sequence also contrasts with the much larger phosphoglycerate kinase typically represented by A. Among these choices, D, thymidylate kinase, is the meaningful fit. The motif alone does not establish dTMP as the substrate, so this is a transferable, probabilistic distinction rather than proof of the exact EC number.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and alternatives provide a credible family-level basis for distinguishing D from the offered choices. The inference does not rely on the reviewer-only identity or annotation of this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option is comparably supported by the sequence features and enzyme-family inference.


### Important caveats

- The reviewer-only UniProt annotation links the EC assignment and catalytic activity to experimental evidence, but the primary study was not independently reviewed here.
- A P-loop-like motif supports nucleotide binding and kinase-family inference, but does not by itself specify thymidylate as the substrate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 211-residue sequence has a P-loop-like nucleotide-binding motif (including the GxxxxGKTT pattern) and is consistent with the compact nucleoside-monophosphate-kinase family. That family-level inference makes a nucleotide kinase far more plausible than the glycosyltransferase (B) or ATP-hydrolysis option (C); the short sequence also contrasts with the much larger phosphoglycerate kinase typically represented by A. Among these choices, D, thymidylate kinase, is the meaningful fit. The motif alone does not establish dTMP as the substrate, so this is a transferable, probabilistic distinction rather than proof of the exact EC number.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and alternatives provide a credible family-level basis for distinguishing D from the offered choices. The inference does not rely on the reviewer-only identity or annotation of this exact protein."
  },
  "case_id": "EC_number_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein sequence. UniProt assigns EC 2.7.4.9 and reports the experimentally evidenced reaction dTMP + ATP = dTDP + ADP, which supports choice D. It also reports activity on dUMP, but that does not contradict the keyed EC assignment."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation links the EC assignment and catalytic activity to experimental evidence, but the primary study was not independently reviewed here.",
    "A P-loop-like motif supports nucleotide binding and kinase-family inference, but does not by itself specify thymidylate as the substrate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence features and enzyme-family inference."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein sequence. UniProt assigns EC 2.7.4.9 and reports the experimentally evidenced reaction dTMP + ATP = dTDP + ADP, which supports choice D. It also reports activity on dUMP, but that does not contradict the keyed EC assignment.",
    "evidence_ids": ["C4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 211-residue sequence has a P-loop-like nucleotide-binding motif (including the GxxxxGKTT pattern) and is consistent with the compact nucleoside-monophosphate-kinase family. That family-level inference makes a nucleotide kinase far more plausible than the glycosyltransferase (B) or ATP-hydrolysis option (C); the short sequence also contrasts with the much larger phosphoglycerate kinase typically represented by A. Among these choices, D, thymidylate kinase, is the meaningful fit. The motif alone does not establish dTMP as the substrate, so this is a transferable, probabilistic distinction rather than proof of the exact EC number.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and alternatives provide a credible family-level basis for distinguishing D from the offered choices. The inference does not rely on the reviewer-only identity or annotation of this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option is comparably supported by the sequence features and enzyme-family inference."
  },
  "important_caveats": [
    "The reviewer-only UniProt annotation links the EC assignment and catalytic activity to experimental evidence, but the primary study was not independently reviewed here.",
    "A P-loop-like motif supports nucleotide binding and kinase-family inference, but does not by itself specify thymidylate as the substrate."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A1ZB29 (KTHY_DROME) is annotated with EC 2.7.4.9 (Thymidylate kinase) with experimental evidence (ECO:0000269, PubMed:38518117). The catalytic activity dTMP + ATP = dTDP + ADP is experimentally confirmed. The benchmark sequence (211 aa, SHA256 bf1ed8a3...) matches the source entry exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 211-residue sequence contains multiple well-conserved TMPK family motifs recognizable from homologs (E. coli TMPK, human TMPK, yeast TMPK): (1) a P-loop/Walker-A nucleotide-binding motif 'GCDRSGKTT' (residues ~8-16), nearly identical to the E. coli TMPK P-loop 'GCDRSGKT'; (2) a conserved 'DRY' arginine-finger motif in 'DRYSFSG' (~residue 90-96), characteristic of the NMP-binding domain in TMPKs; (3) an 'AP' motif in 'CYAPER' (~residue 130), part of the NMP-binding subdomain. The small size (~211 aa) is diagnostic of the TMPK/NMP-kinase fold. These features identify the protein as a phosphotransferase (eliminating C, a hydrolase, and B, a glycosyltransferase) and specifically a nucleoside-monophosphate kinase. Among the remaining kinase options, 2.7.2.4 (acetyl-CoA synthase, AMP-forming) is a large multi-domain enzyme (>600 aa) with entirely different motifs, while 2.7.4.9 (TMPK) matches the small size and the specific TMPK P-loop/DRY/AP motif combination. Thus family-level motif recognition distinguishes D from all alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P-loop 'GCDRSGKTT', the 'DRY' arginine finger, and the 'AP' NMP-binding motif are textbook conserved features of the TMPK family shared across E. coli, human, yeast, and Drosophila orthologs. A model trained on general protein-family knowledge can recognize these motifs in a 211-aa sequence and assign the protein to the TMPK family (EC 2.7.4.x), then use size and motif specificity to select 2.7.4.9 over the other choices. No target-specific database lookup is required.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence motifs (P-loop, DRY, AP) and protein size uniquely identify a TMPK-family NMP kinase. The other options represent entirely different enzyme classes (glycosyltransferase, hydrolase) or a much larger enzyme (acetyl-CoA synthase), none of which match the observed motifs or size.


### Important caveats

- The experimental EC assignment (ECO:0000269) is based on a 2024 characterization paper (PubMed:38518117) of Drosophila melanogaster TMPK; the protein also shows activity toward dUMP, but the primary EC assignment remains 2.7.4.9.
- The reviewer identified the source accession via dataset metadata not available to the evaluated model; the reasoning argument relies only on sequence motifs visible in the input and general TMPK-family knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 211-residue sequence contains multiple well-conserved TMPK family motifs recognizable from homologs (E. coli TMPK, human TMPK, yeast TMPK): (1) a P-loop/Walker-A nucleotide-binding motif 'GCDRSGKTT' (residues ~8-16), nearly identical to the E. coli TMPK P-loop 'GCDRSGKT'; (2) a conserved 'DRY' arginine-finger motif in 'DRYSFSG' (~residue 90-96), characteristic of the NMP-binding domain in TMPKs; (3) an 'AP' motif in 'CYAPER' (~residue 130), part of the NMP-binding subdomain. The small size (~211 aa) is diagnostic of the TMPK/NMP-kinase fold. These features identify the protein as a phosphotransferase (eliminating C, a hydrolase, and B, a glycosyltransferase) and specifically a nucleoside-monophosphate kinase. Among the remaining kinase options, 2.7.2.4 (acetyl-CoA synthase, AMP-forming) is a large multi-domain enzyme (>600 aa) with entirely different motifs, while 2.7.4.9 (TMPK) matches the small size and the specific TMPK P-loop/DRY/AP motif combination. Thus family-level motif recognition distinguishes D from all alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P-loop 'GCDRSGKTT', the 'DRY' arginine finger, and the 'AP' NMP-binding motif are textbook conserved features of the TMPK family shared across E. coli, human, yeast, and Drosophila orthologs. A model trained on general protein-family knowledge can recognize these motifs in a 211-aa sequence and assign the protein to the TMPK family (EC 2.7.4.x), then use size and motif specificity to select 2.7.4.9 over the other choices. No target-specific database lookup is required."
  },
  "case_id": "EC_number_0066",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A1ZB29 (KTHY_DROME) is annotated with EC 2.7.4.9 (Thymidylate kinase) with experimental evidence (ECO:0000269, PubMed:38518117). The catalytic activity dTMP + ATP = dTDP + ADP is experimentally confirmed. The benchmark sequence (211 aa, SHA256 bf1ed8a3...) matches the source entry exactly."
  },
  "important_caveats": [
    "The experimental EC assignment (ECO:0000269) is based on a 2024 characterization paper (PubMed:38518117) of Drosophila melanogaster TMPK; the protein also shows activity toward dUMP, but the primary EC assignment remains 2.7.4.9.",
    "The reviewer identified the source accession via dataset metadata not available to the evaluated model; the reasoning argument relies only on sequence motifs visible in the input and general TMPK-family knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence motifs (P-loop, DRY, AP) and protein size uniquely identify a TMPK-family NMP kinase. The other options represent entirely different enzyme classes (glycosyltransferase, hydrolase) or a much larger enzyme (acetyl-CoA synthase), none of which match the observed motifs or size."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0066",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A1ZB29 (KTHY_DROME) is annotated with EC 2.7.4.9 (Thymidylate kinase) with experimental evidence (ECO:0000269, PubMed:38518117). The catalytic activity dTMP + ATP = dTDP + ADP is experimentally confirmed. The benchmark sequence (211 aa, SHA256 bf1ed8a3...) matches the source entry exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 211-residue sequence contains multiple well-conserved TMPK family motifs recognizable from homologs (E. coli TMPK, human TMPK, yeast TMPK): (1) a P-loop/Walker-A nucleotide-binding motif 'GCDRSGKTT' (residues ~8-16), nearly identical to the E. coli TMPK P-loop 'GCDRSGKT'; (2) a conserved 'DRY' arginine-finger motif in 'DRYSFSG' (~residue 90-96), characteristic of the NMP-binding domain in TMPKs; (3) an 'AP' motif in 'CYAPER' (~residue 130), part of the NMP-binding subdomain. The small size (~211 aa) is diagnostic of the TMPK/NMP-kinase fold. These features identify the protein as a phosphotransferase (eliminating C, a hydrolase, and B, a glycosyltransferase) and specifically a nucleoside-monophosphate kinase. Among the remaining kinase options, 2.7.2.4 (acetyl-CoA synthase, AMP-forming) is a large multi-domain enzyme (>600 aa) with entirely different motifs, while 2.7.4.9 (TMPK) matches the small size and the specific TMPK P-loop/DRY/AP motif combination. Thus family-level motif recognition distinguishes D from all alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The P-loop 'GCDRSGKTT', the 'DRY' arginine finger, and the 'AP' NMP-binding motif are textbook conserved features of the TMPK family shared across E. coli, human, yeast, and Drosophila orthologs. A model trained on general protein-family knowledge can recognize these motifs in a 211-aa sequence and assign the protein to the TMPK family (EC 2.7.4.x), then use size and motif specificity to select 2.7.4.9 over the other choices. No target-specific database lookup is required."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence motifs (P-loop, DRY, AP) and protein size uniquely identify a TMPK-family NMP kinase. The other options represent entirely different enzyme classes (glycosyltransferase, hydrolase) or a much larger enzyme (acetyl-CoA synthase), none of which match the observed motifs or size."
  },
  "important_caveats": [
    "The experimental EC assignment (ECO:0000269) is based on a 2024 characterization paper (PubMed:38518117) of Drosophila melanogaster TMPK; the protein also shows activity toward dUMP, but the primary EC assignment remains 2.7.4.9.",
    "The reviewer identified the source accession via dataset metadata not available to the evaluated model; the reasoning argument relies only on sequence motifs visible in the input and general TMPK-family knowledge."
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
  "benchmark_sequence_length": 211,
  "benchmark_sequence_sha256": "bf1ed8a3fcd4c18e58888815bfd740519681fc01ccace8f65722bc742c0f0cdf",
  "current_entry_audit": {
    "entryVersion": 158,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2007-02-06",
    "sequenceVersion": 1
  },
  "current_record_sha256": "8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 211,
  "current_source_sequence_sha256": "bf1ed8a3fcd4c18e58888815bfd740519681fc01ccace8f65722bc742c0f0cdf",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 156,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A1ZB29",
  "selected_historical_entry_version": 156,
  "selected_historical_record_sha256": "bec1661b56942c96a37903d0045394314b809ce2713c1f5e399dfd08e81195a9",
  "selected_historical_source_sequence_length": 211,
  "selected_historical_source_sequence_sha256": "bf1ed8a3fcd4c18e58888815bfd740519681fc01ccace8f65722bc742c0f0cdf",
  "selected_historical_version": {
    "accession": "A1ZB29",
    "database": "Swiss-Prot",
    "entryVersion": 156,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "KTHY_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A1ZB29\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:47.024723+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7",
  "url": "https://rest.uniprot.org/uniprotkb/A1ZB29.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":158,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2007-02-06\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:47.024723+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7",
  "url": "https://rest.uniprot.org/uniprotkb/A1ZB29.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:47.024723+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7",
  "url": "https://rest.uniprot.org/uniprotkb/A1ZB29.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0034299\",\"source\":\"FlyBase\"}],\"value\":\"Deoxythymidylate kinase\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38518117\",\"source\":\"PubMed\"}],\"value\":\"2.7.4.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38518117\",\"source\":\"PubMed\"}],\"value\":\"Thymidylate kinase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38518117\",\"source\":\"PubMed\"}],\"value\":\"DmTMPK\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:47.024723+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7",
  "url": "https://rest.uniprot.org/uniprotkb/A1ZB29.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38518117\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:13518\"}}],\"reaction\":{\"ecNumber\":\"2.7.4.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38518117\",\"source\":\"PubMed\"}],\"name\":\"dTMP + ATP = dTDP + ADP\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:13517\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58369\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:63528\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:47.024723+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7",
  "url": "https://rest.uniprot.org/uniprotkb/A1ZB29.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38518117\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:30656\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38518117\",\"source\":\"PubMed\"}],\"name\":\"dUMP + ATP = dUDP + ADP\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:30655\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:60471\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:246422\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:26:47.024723+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7",
  "url": "https://rest.uniprot.org/uniprotkb/A1ZB29.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A1ZB29.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Hu Frisk J.\",\"Wang L.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38518117\"},{\"database\":\"DOI\",\"id\":\"10.1080/15257770.2024.2332410\"}],\"citationType\":\"journal article\",\"firstPage\":\"1\",\"id\":\"38518117\",\"journal\":\"Nucleosides Nucleotides Nucleic Acids\",\"lastPage\":\"9\",\"publicationDate\":\"2024\",\"title\":\"Molecular characterization of Drosophila melanogaster thymidylate kinase.\",\"volume\":\"43\"},\"referenceNumber\":6,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/5",
  "retrieved_utc": "2026-11-02T04:26:47.024723+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "8555e9f6519f5abfebd9fbac4f9f543b7c48facea7144c3741a9180f4122ceb7",
  "url": "https://rest.uniprot.org/uniprotkb/A1ZB29.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156)

```json
{
  "entry_version": 156,
  "evidence_id": "H1",
  "excerpt": "ID   KTHY_DROME              Reviewed;         211 AA.\nAC   A1ZB29; A0AP29; A0AP30; A0AP31; C0MJH3; Q8SZQ0;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   06-FEB-2007, sequence version 1.\nDT   28-JAN-2026, entry version 156.\nDE   RecName: Full=Thymidylate kinase {ECO:0000303|PubMed:38518117};\nDE            Short=DmTMPK {ECO:0000303|PubMed:38518117};\nDE            EC=2.7.4.9 {ECO:0000269|PubMed:38518117};\nDE   AltName: Full=Deoxythymidylate kinase {ECO:0000312|FlyBase:FBgn0034299};\nGN   Name=Dtymk {ECO:0000312|FlyBase:FBgn0034299};\nGN   Synonyms=TMPK {ECO:0000303|PubMed:38518117};\nGN   ORFNames=CG5757 {ECO:0000312|FlyBase:FBgn0034299};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.964915+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bec1661b56942c96a37903d0045394314b809ce2713c1f5e399dfd08e81195a9",
  "url": "https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156)

```json
{
  "entry_version": 156,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Thymidylate kinase {ECO:0000303|PubMed:38518117};\nDE            Short=DmTMPK {ECO:0000303|PubMed:38518117};\nDE            EC=2.7.4.9 {ECO:0000269|PubMed:38518117};\nDE   AltName: Full=Deoxythymidylate kinase {ECO:0000312|FlyBase:FBgn0034299};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.964915+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bec1661b56942c96a37903d0045394314b809ce2713c1f5e399dfd08e81195a9",
  "url": "https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156)

```json
{
  "entry_version": 156,
  "evidence_id": "H3",
  "excerpt": "RN   [6]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=38518117; DOI=10.1080/15257770.2024.2332410;\nRA   Hu Frisk J., Wang L.;\nRT   \"Molecular characterization of Drosophila melanogaster thymidylate\nRT   kinase.\";\nRL   Nucleosides Nucleotides Nucleic Acids 43:1-9(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.964915+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 99-105",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bec1661b56942c96a37903d0045394314b809ce2713c1f5e399dfd08e81195a9",
  "url": "https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156)

```json
{
  "entry_version": 156,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=dTMP + ATP = dTDP + ADP; Xref=Rhea:RHEA:13517,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:58369, ChEBI:CHEBI:63528,\nCC         ChEBI:CHEBI:456216; EC=2.7.4.9;\nCC         Evidence={ECO:0000269|PubMed:38518117};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13518;\nCC         Evidence={ECO:0000269|PubMed:38518117};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.964915+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-119",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bec1661b56942c96a37903d0045394314b809ce2713c1f5e399dfd08e81195a9",
  "url": "https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156)

```json
{
  "entry_version": 156,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=dUMP + ATP = dUDP + ADP; Xref=Rhea:RHEA:30655,\nCC         ChEBI:CHEBI:30616, ChEBI:CHEBI:60471, ChEBI:CHEBI:246422,\nCC         ChEBI:CHEBI:456216; Evidence={ECO:0000269|PubMed:38518117};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:30656;\nCC         Evidence={ECO:0000269|PubMed:38518117};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:49.964915+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 120-125",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "bec1661b56942c96a37903d0045394314b809ce2713c1f5e399dfd08e81195a9",
  "url": "https://rest.uniprot.org/unisave/A1ZB29?format=txt&versions=156"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 66. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
