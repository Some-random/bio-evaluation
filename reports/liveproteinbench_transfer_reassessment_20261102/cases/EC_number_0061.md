# EC_number_0061

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0061.txt)

**Task:** `EC_number`  
**Expected answer:** **B** — 2.7.7.43

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVIAVIPARSGSKGIKNKNLVLLNNQPLIYYTIKAALNSKCISKVLVSSDSEEILSYAKSQNVDILKRPIELAQDDTTSDKVLLHALEFYKDYEDVIFLQPTSPLRTNIHIDEAFKIYKNSDANALISVTECDNKILKAFICDNKGDLKGICDDEYPFMPRQKLPKTYMSNGAIYILSIKDFLNKPSFLQSKTKYFLMNKISSLDIDNLEDLKQVENIQKMKGCVVWISGLAGAGKTTISSGLYKKLKEKYNNSVLLDGDELRKIFKHTGYTREERLESAKKISSLCSFLAKNDIIVICATISLFEEIYLLNRNTIENYFEVFVDCPMEELILRDQKGLYSGALKGEIKDVVGVDIKYAKPNAHYIIDNSSKTDLEKKINNLYNEVELFFNKER

[Multiple Choices]
A. 2.7.7.88
B. 2.7.7.43
C. 2.7.8.43
D. 4.2.1.9
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

> The sequence matches the annotated protein, and the cited catalytic-activity records assign it EC 2.7.7.43 for a CTP-dependent N-acylneuraminate cytidylyltransferase reaction. The annotations cite experimental evidence (ECO:0000269), rather than only computational inference.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a nucleotide-binding-like region, including the `WISGLAGAGKTT` motif, consistent with a nucleotide-dependent transferase. More importantly, transferable family-level sequence recognition can distinguish a bacterial CMP-neuraminic-acid synthetase/cytidylyltransferase from the other offered enzyme classes and functions, supporting B. The motif alone would not establish the acceptor substrate, so the inference depends on the broader sequence-family pattern.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides a credible basis for recognizing the relevant enzyme family and mapping that family to the offered EC choice. This is a probabilistic family inference, not proof from the short motif alone or reliance on the exact protein's database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives specify distinct reaction classes or enzyme functions; the sequence-family inference supports B, and the sequence-matched experimental annotation corroborates that choice.


### Important caveats

- The nucleotide-binding-like motif is not specific to this substrate or EC number; family-level recognition from the full sequence is needed.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a nucleotide-binding-like region, including the `WISGLAGAGKTT` motif, consistent with a nucleotide-dependent transferase. More importantly, transferable family-level sequence recognition can distinguish a bacterial CMP-neuraminic-acid synthetase/cytidylyltransferase from the other offered enzyme classes and functions, supporting B. The motif alone would not establish the acceptor substrate, so the inference depends on the broader sequence-family pattern.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a credible basis for recognizing the relevant enzyme family and mapping that family to the offered EC choice. This is a probabilistic family inference, not proof from the short motif alone or reliance on the exact protein's database record."
  },
  "case_id": "EC_number_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and the cited catalytic-activity records assign it EC 2.7.7.43 for a CTP-dependent N-acylneuraminate cytidylyltransferase reaction. The annotations cite experimental evidence (ECO:0000269), rather than only computational inference."
  },
  "important_caveats": [
    "The nucleotide-binding-like motif is not specific to this substrate or EC number; family-level recognition from the full sequence is needed."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives specify distinct reaction classes or enzyme functions; the sequence-family inference supports B, and the sequence-matched experimental annotation corroborates that choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and the cited catalytic-activity records assign it EC 2.7.7.43 for a CTP-dependent N-acylneuraminate cytidylyltransferase reaction. The annotations cite experimental evidence (ECO:0000269), rather than only computational inference.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a nucleotide-binding-like region, including the `WISGLAGAGKTT` motif, consistent with a nucleotide-dependent transferase. More importantly, transferable family-level sequence recognition can distinguish a bacterial CMP-neuraminic-acid synthetase/cytidylyltransferase from the other offered enzyme classes and functions, supporting B. The motif alone would not establish the acceptor substrate, so the inference depends on the broader sequence-family pattern.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a credible basis for recognizing the relevant enzyme family and mapping that family to the offered EC choice. This is a probabilistic family inference, not proof from the short motif alone or reliance on the exact protein's database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives specify distinct reaction classes or enzyme functions; the sequence-family inference supports B, and the sequence-matched experimental annotation corroborates that choice."
  },
  "important_caveats": [
    "The nucleotide-binding-like motif is not specific to this substrate or EC number; family-level recognition from the full sequence is needed."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DY07 (NEUAC_CAMJ8) annotates this 394-aa protein as N-acylneuraminate cytidylyltransferase with EC 2.7.7.43, supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic activity (N-acylneuraminate + CTP → CMP-N-acyl-neuraminate + PPi) is experimentally confirmed. The sequence in the benchmark matches the source entry exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a canonical P-loop/Walker-A motif (GAGAGKTT, residues ~195-202), which is a hallmark of nucleotide-binding proteins, particularly CTP-binding nucleotidyltransferases. This strongly supports a 2.7.x transferase classification and eliminates D (4.2.1.9, a hydro-lyase/dehydratase with no nucleotide-binding requirement). The P-loop and overall ~394-aa architecture are inconsistent with 2.7.8.x (transferases transferring other groups, which typically lack P-loop CTP-binding motifs), eliminating C. Between A (2.7.7.88) and B (2.7.7.43): the CMP-Neu5Ac synthase (NeuA-type) family is one of the most widely distributed bacterial nucleotidyltransferase families, present in hundreds of bacterial genomes. Family-level recognition of the NeuA/CMP-Neu5Ac synthase architecture—including the P-loop for CTP binding, the characteristic ~350-400 aa length, and conserved sequence blocks shared across many bacterial homologs (E. coli NeuA, Pasteurella, Haemophilus, etc.)—provides a credible inference toward EC 2.7.7.43. EC 2.7.7.88 represents a different nucleotidyltransferase with a distinct substrate and mechanism, and the NeuA-family sequence signature does not match it. A model trained on protein family databases would recognize the NeuA-type fold and assign 2.7.7.43.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P-loop eliminates the lyase (D) and the 2.7.8.x subclass (C). Family-level recognition of the CMP-Neu5Ac synthase/NeuA nucleotidyltransferase family, which is extensively represented across bacterial proteomes, provides a credible transferable inference distinguishing 2.7.7.43 from 2.7.7.88. The argument relies on conserved motifs (P-loop for CTP binding), family architecture, and learned patterns from homologous proteins in other organisms, not on memorizing this specific protein's database entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> D (4.2.1.9) is clearly eliminated by the P-loop and transferase architecture. C (2.7.8.43) is eliminated because 2.7.8.x enzymes do not use CTP as a nucleotidyl donor in the manner indicated by the P-loop. The remaining distinction between A and B is resolved by NeuA-family recognition, making B the most defensible answer.


### Important caveats

- The exact identity of EC 2.7.7.88 was not independently verified; the reasoning assumes it represents a nucleotidyltransferase with a different substrate/family from CMP-Neu5Ac synthase.
- The P-loop motif (GAGAGKTT) is present but is a general nucleotide-binding feature; the stronger argument for B relies on broader NeuA-family sequence recognition rather than a single motif.
- The UniProt annotation carries experimental evidence (ECO:0000269), strengthening the key's reliability.
- The sequence was integrated into UniProt in June 2025; the benchmark's construction date relative to this annotation is unknown, though the reviewer-only source confirms the sequence matches.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a canonical P-loop/Walker-A motif (GAGAGKTT, residues ~195-202), which is a hallmark of nucleotide-binding proteins, particularly CTP-binding nucleotidyltransferases. This strongly supports a 2.7.x transferase classification and eliminates D (4.2.1.9, a hydro-lyase/dehydratase with no nucleotide-binding requirement). The P-loop and overall ~394-aa architecture are inconsistent with 2.7.8.x (transferases transferring other groups, which typically lack P-loop CTP-binding motifs), eliminating C. Between A (2.7.7.88) and B (2.7.7.43): the CMP-Neu5Ac synthase (NeuA-type) family is one of the most widely distributed bacterial nucleotidyltransferase families, present in hundreds of bacterial genomes. Family-level recognition of the NeuA/CMP-Neu5Ac synthase architecture—including the P-loop for CTP binding, the characteristic ~350-400 aa length, and conserved sequence blocks shared across many bacterial homologs (E. coli NeuA, Pasteurella, Haemophilus, etc.)—provides a credible inference toward EC 2.7.7.43. EC 2.7.7.88 represents a different nucleotidyltransferase with a distinct substrate and mechanism, and the NeuA-family sequence signature does not match it. A model trained on protein family databases would recognize the NeuA-type fold and assign 2.7.7.43.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P-loop eliminates the lyase (D) and the 2.7.8.x subclass (C). Family-level recognition of the CMP-Neu5Ac synthase/NeuA nucleotidyltransferase family, which is extensively represented across bacterial proteomes, provides a credible transferable inference distinguishing 2.7.7.43 from 2.7.7.88. The argument relies on conserved motifs (P-loop for CTP binding), family architecture, and learned patterns from homologous proteins in other organisms, not on memorizing this specific protein's database entry."
  },
  "case_id": "EC_number_0061",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H2",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DY07 (NEUAC_CAMJ8) annotates this 394-aa protein as N-acylneuraminate cytidylyltransferase with EC 2.7.7.43, supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic activity (N-acylneuraminate + CTP → CMP-N-acyl-neuraminate + PPi) is experimentally confirmed. The sequence in the benchmark matches the source entry exactly."
  },
  "important_caveats": [
    "The exact identity of EC 2.7.7.88 was not independently verified; the reasoning assumes it represents a nucleotidyltransferase with a different substrate/family from CMP-Neu5Ac synthase.",
    "The P-loop motif (GAGAGKTT) is present but is a general nucleotide-binding feature; the stronger argument for B relies on broader NeuA-family sequence recognition rather than a single motif.",
    "The UniProt annotation carries experimental evidence (ECO:0000269), strengthening the key's reliability.",
    "The sequence was integrated into UniProt in June 2025; the benchmark's construction date relative to this annotation is unknown, though the reviewer-only source confirms the sequence matches."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D (4.2.1.9) is clearly eliminated by the P-loop and transferase architecture. C (2.7.8.43) is eliminated because 2.7.8.x enzymes do not use CTP as a nucleotidyl donor in the manner indicated by the P-loop. The remaining distinction between A and B is resolved by NeuA-family recognition, making B the most defensible answer."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0061",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DY07 (NEUAC_CAMJ8) annotates this 394-aa protein as N-acylneuraminate cytidylyltransferase with EC 2.7.7.43, supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024). The catalytic activity (N-acylneuraminate + CTP → CMP-N-acyl-neuraminate + PPi) is experimentally confirmed. The sequence in the benchmark matches the source entry exactly.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H2", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a canonical P-loop/Walker-A motif (GAGAGKTT, residues ~195-202), which is a hallmark of nucleotide-binding proteins, particularly CTP-binding nucleotidyltransferases. This strongly supports a 2.7.x transferase classification and eliminates D (4.2.1.9, a hydro-lyase/dehydratase with no nucleotide-binding requirement). The P-loop and overall ~394-aa architecture are inconsistent with 2.7.8.x (transferases transferring other groups, which typically lack P-loop CTP-binding motifs), eliminating C. Between A (2.7.7.88) and B (2.7.7.43): the CMP-Neu5Ac synthase (NeuA-type) family is one of the most widely distributed bacterial nucleotidyltransferase families, present in hundreds of bacterial genomes. Family-level recognition of the NeuA/CMP-Neu5Ac synthase architecture—including the P-loop for CTP binding, the characteristic ~350-400 aa length, and conserved sequence blocks shared across many bacterial homologs (E. coli NeuA, Pasteurella, Haemophilus, etc.)—provides a credible inference toward EC 2.7.7.43. EC 2.7.7.88 represents a different nucleotidyltransferase with a distinct substrate and mechanism, and the NeuA-family sequence signature does not match it. A model trained on protein family databases would recognize the NeuA-type fold and assign 2.7.7.43.",
    "missing_item_specific_fact": "",
    "reason": "The P-loop eliminates the lyase (D) and the 2.7.8.x subclass (C). Family-level recognition of the CMP-Neu5Ac synthase/NeuA nucleotidyltransferase family, which is extensively represented across bacterial proteomes, provides a credible transferable inference distinguishing 2.7.7.43 from 2.7.7.88. The argument relies on conserved motifs (P-loop for CTP binding), family architecture, and learned patterns from homologous proteins in other organisms, not on memorizing this specific protein's database entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "D (4.2.1.9) is clearly eliminated by the P-loop and transferase architecture. C (2.7.8.43) is eliminated because 2.7.8.x enzymes do not use CTP as a nucleotidyl donor in the manner indicated by the P-loop. The remaining distinction between A and B is resolved by NeuA-family recognition, making B the most defensible answer."
  },
  "important_caveats": [
    "The exact identity of EC 2.7.7.88 was not independently verified; the reasoning assumes it represents a nucleotidyltransferase with a different substrate/family from CMP-Neu5Ac synthase.",
    "The P-loop motif (GAGAGKTT) is present but is a general nucleotide-binding feature; the stronger argument for B relies on broader NeuA-family sequence recognition rather than a single motif.",
    "The UniProt annotation carries experimental evidence (ECO:0000269), strengthening the key's reliability.",
    "The sequence was integrated into UniProt in June 2025; the benchmark's construction date relative to this annotation is unknown, though the reviewer-only source confirms the sequence matches."
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
  "benchmark_sequence_length": 394,
  "benchmark_sequence_sha256": "af09f26a5420425be58eeedbd38a5518b9f01e8f548d776db14ae23b9668a66c",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 394,
  "current_source_sequence_sha256": "af09f26a5420425be58eeedbd38a5518b9f01e8f548d776db14ae23b9668a66c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 2,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "P0DY07",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305",
  "selected_historical_source_sequence_length": 394,
  "selected_historical_source_sequence_sha256": "af09f26a5420425be58eeedbd38a5518b9f01e8f548d776db14ae23b9668a66c",
  "selected_historical_version": {
    "accession": "P0DY07",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "NEUAC_CAMJ8",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DY07\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:17.113205+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY07.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:17.113205+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY07.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Campylobacterota\",\"Epsilonproteobacteria\",\"Campylobacterales\",\"Campylobacteraceae\",\"Campylobacter\"],\"scientificName\":\"Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC 11828)\",\"taxonId\":407148}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:17.113205+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY07.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"CMP-N-acetylneuraminate synthase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"CMP-Neu5Ac synthase\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"value\":\"2.7.7.43\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"N-acylneuraminate cytidylyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:17.113205+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY07.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:11345\"}}],\"reaction\":{\"ecNumber\":\"2.7.7.43\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"name\":\"an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:11344\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:37563\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:60073\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:68671\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:17.113205+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY07.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:80844\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38382015\",\"source\":\"PubMed\"}],\"name\":\"N-acetylneuraminate + CTP = CMP-N-acetyl-beta-neuraminate + diphosphate\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:80843\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:33019\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35418\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:37563\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57812\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:25:17.113205+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY07.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DY07.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Ghosh M.K.\",\"Raushel F.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38382015\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.biochem.3c00664\"}],\"citationType\":\"journal article\",\"firstPage\":\"688\",\"id\":\"38382015\",\"journal\":\"Biochemistry\",\"lastPage\":\"698\",\"publicationDate\":\"2024\",\"title\":\"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter jejuni.\",\"volume\":\"63\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"81116 / NCTC 11828\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:25:17.113205+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "b50ed6bd92ec8842f4e9d1ae4d13d75caa73c77d62a5df6448b510c17ce7cfca",
  "url": "https://rest.uniprot.org/uniprotkb/P0DY07.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   NEUAC_CAMJ8             Reviewed;         394 AA.\nAC   P0DY07;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=N-acylneuraminate cytidylyltransferase {ECO:0000305};\nDE            EC=2.7.7.43 {ECO:0000269|PubMed:38382015};\nDE   AltName: Full=CMP-N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};\nDE            Short=CMP-Neu5Ac synthase {ECO:0000303|PubMed:38382015};\nGN   Name=HS6.5 {ECO:0000303|PubMed:38382015};\nGN   OrderedLocusNames=C8J_1333 {ECO:0000312|EMBL:ABV52931.1};\nOS   Campylobacter jejuni subsp. jejuni serotype O:6 (strain 81116 / NCTC\nOS   11828).\nOC   Bacteria; Pseudomonadati; Campylobacterota; Epsilonproteobacteria;\nOC   Campylobacterales; Campylobacteraceae; Campylobacter.\nOX   NCBI_TaxID=407148;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.379520+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305",
  "url": "https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=N-acylneuraminate cytidylyltransferase {ECO:0000305};\nDE            EC=2.7.7.43 {ECO:0000269|PubMed:38382015};\nDE   AltName: Full=CMP-N-acetylneuraminate synthase {ECO:0000303|PubMed:38382015};\nDE            Short=CMP-Neu5Ac synthase {ECO:0000303|PubMed:38382015};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.379520+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305",
  "url": "https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRC   STRAIN=81116 / NCTC 11828;\nRX   PubMed=38382015; DOI=10.1021/acs.biochem.3c00664;\nRA   Ghosh M.K., Raushel F.M.;\nRT   \"Biosynthesis of UDP-alpha-N-Acetyl-d-mannosaminuronic Acid and CMP-beta-N-\nRT   Acetyl-d-neuraminic Acid for the Capsular Polysaccharides of Campylobacter\nRT   jejuni.\";\nRL   Biochemistry 63:688-698(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.379520+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 26-34",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305",
  "url": "https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate +\nCC         diphosphate; Xref=Rhea:RHEA:11344, ChEBI:CHEBI:33019,\nCC         ChEBI:CHEBI:37563, ChEBI:CHEBI:60073, ChEBI:CHEBI:68671; EC=2.7.7.43;\nCC         Evidence={ECO:0000269|PubMed:38382015};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:11345;\nCC         Evidence={ECO:0000269|PubMed:38382015};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.379520+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305",
  "url": "https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=N-acetylneuraminate + CTP = CMP-N-acetyl-beta-neuraminate +\nCC         diphosphate; Xref=Rhea:RHEA:80843, ChEBI:CHEBI:33019,\nCC         ChEBI:CHEBI:35418, ChEBI:CHEBI:37563, ChEBI:CHEBI:57812;\nCC         Evidence={ECO:0000269|PubMed:38382015};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:80844;\nCC         Evidence={ECO:0000269|PubMed:38382015};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:24.379520+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "4fb8edfea54dbaf00ab1dbaeb2251b0f44292e2a8e79c4393f55f323eeaa2305",
  "url": "https://rest.uniprot.org/unisave/P0DY07?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 61. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
