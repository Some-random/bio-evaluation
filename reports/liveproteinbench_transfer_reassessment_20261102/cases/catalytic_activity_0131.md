# catalytic_activity_0131

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0131.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate

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
A. a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol
B. (2S)-3-(4-methoxyphenyl)-2-[(3S)-3-(methylamino)-8-oxo-1-azaspiro[4.5]decan-1-yl]propanal = (1S,3S,6S,7S,8R)-7-hydroxy-6-[(4-methoxyphenyl)methyl]-3-(methylamino)-5-azatricyclo[6.3.1.0(1,5)]dodecan-9-one
C. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
D. an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate
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

> The sequence-matched UniProt annotation reports the reaction in choice D as the catalytic activity and assigns it EC 2.7.7.43, with experimental evidence cited. This directly supports the key for the supplied sequence.

Citations as saved: [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a P-loop-like GxxxxGKT motif (within GLAGAGKTT), suggestive of nucleotide binding. Among the options, D uniquely uses CTP to activate an N-acylneuraminate, forming a CMP-linked product and diphosphate—a nucleotide-transfer reaction. That makes D a credible choice over the hydrolysis, dehydration, and unusual cyclization alternatives, although the motif alone does not establish the exact substrate.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable sequence feature and the chemistry of the offered reactions meaningfully favor D without requiring knowledge of this exact protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only D describes CTP-dependent activation of an N-acylneuraminate; the other choices describe distinct transformations.


### Important caveats

- The nucleotide-binding motif is suggestive rather than proof of the specific reaction; the reviewer-only annotation provides direct support for the exact activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a P-loop-like GxxxxGKT motif (within GLAGAGKTT), suggestive of nucleotide binding. Among the options, D uniquely uses CTP to activate an N-acylneuraminate, forming a CMP-linked product and diphosphate—a nucleotide-transfer reaction. That makes D a credible choice over the hydrolysis, dehydration, and unusual cyclization alternatives, although the motif alone does not establish the exact substrate.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence feature and the chemistry of the offered reactions meaningfully favor D without requiring knowledge of this exact protein's annotation."
  },
  "case_id": "catalytic_activity_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports the reaction in choice D as the catalytic activity and assigns it EC 2.7.7.43, with experimental evidence cited. This directly supports the key for the supplied sequence."
  },
  "important_caveats": [
    "The nucleotide-binding motif is suggestive rather than proof of the specific reaction; the reviewer-only annotation provides direct support for the exact activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D describes CTP-dependent activation of an N-acylneuraminate; the other choices describe distinct transformations."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation reports the reaction in choice D as the catalytic activity and assigns it EC 2.7.7.43, with experimental evidence cited. This directly supports the key for the supplied sequence.",
    "evidence_ids": ["C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a P-loop-like GxxxxGKT motif (within GLAGAGKTT), suggestive of nucleotide binding. Among the options, D uniquely uses CTP to activate an N-acylneuraminate, forming a CMP-linked product and diphosphate—a nucleotide-transfer reaction. That makes D a credible choice over the hydrolysis, dehydration, and unusual cyclization alternatives, although the motif alone does not establish the exact substrate.",
    "missing_item_specific_fact": "",
    "reason": "A transferable sequence feature and the chemistry of the offered reactions meaningfully favor D without requiring knowledge of this exact protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only D describes CTP-dependent activation of an N-acylneuraminate; the other choices describe distinct transformations."
  },
  "important_caveats": [
    "The nucleotide-binding motif is suggestive rather than proof of the specific reaction; the reviewer-only annotation provides direct support for the exact activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DY07 (sequence SHA256 match confirmed) annotates this protein as N-acylneuraminate cytidylyltransferase (EC 2.7.7.43), with the catalytic activity explicitly stated as 'an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate.' This is supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024, Biochemistry 63:688-698). The expected answer D matches the annotated reaction verbatim.

Citations as saved: [C1](#evidence-c1), [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear Rossmann-fold nucleotide-binding motif 'GLAGAGKTT' (GxGxxG pattern), which is a hallmark of enzymes that bind nucleotide triphosphates such as CTP. Among the four offered reactions, only choice D involves a nucleotide substrate (CTP → CMP transfer + diphosphate release), consistent with a cytidylyltransferase. Choices A (glycosidase hydrolysis), B (a complex intramolecular cyclization/rearrangement), and C (a dehydratase reaction) do not involve nucleotide substrates and are mechanistically inconsistent with a P-loop nucleotide-binding fold. Additionally, the protein's size (~394 aa) and overall composition are consistent with the well-characterized CMP-Neu5Ac synthase family in bacterial sialic-acid biosynthesis, a transferase superfamily member. A knowledgeable model could use the P-loop motif to eliminate non-nucleotide-dependent reactions (A, C) and the unusual, highly specific nature of B (a single-step cyclization of a complex alkaloid-like substrate) to favor D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Rossmann-fold P-loop motif (GLAGAGKTT) provides a concrete, transferable sequence feature that meaningfully distinguishes the CTP-dependent nucleotidyl-transfer reaction (D) from the hydrolysis (A), cyclization (B), and dehydration (C) alternatives. This is a family-level inference based on conserved nucleotide-binding architecture shared across many transferase families, not a lookup of this protein's specific annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The nucleotide-binding motif strongly favors D over the other three choices. Choice B is a highly unusual single-step cyclization of a complex substrate with no obvious sequence-level support. Choices A and C describe reactions catalyzed by enzymes with entirely different structural folds (glycosidase TIM barrel or beta-propeller; iron-dependent dehydratase). No ambiguity among the offered alternatives is identified.


### Important caveats

- The Rossmann fold (GxGxxG) is found in many enzyme classes beyond cytidylyltransferases (e.g., dehydrogenases, synthetases), so the motif alone narrows but does not uniquely identify the enzyme. The argument relies on the combination of the motif with the reaction chemistry of the offered choices.
- The CMP-Neu5Ac synthase family is well-known in sialic-acid biosynthesis, but recognizing it from sequence alone without prior exposure to the family's characteristic features would be more challenging.
- The experimental evidence (PubMed:38382015) post-dates the typical training cutoff for many models, though the enzyme family and reaction are long-established in biochemistry.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold nucleotide-binding motif 'GLAGAGKTT' (GxGxxG pattern), which is a hallmark of enzymes that bind nucleotide triphosphates such as CTP. Among the four offered reactions, only choice D involves a nucleotide substrate (CTP → CMP transfer + diphosphate release), consistent with a cytidylyltransferase. Choices A (glycosidase hydrolysis), B (a complex intramolecular cyclization/rearrangement), and C (a dehydratase reaction) do not involve nucleotide substrates and are mechanistically inconsistent with a P-loop nucleotide-binding fold. Additionally, the protein's size (~394 aa) and overall composition are consistent with the well-characterized CMP-Neu5Ac synthase family in bacterial sialic-acid biosynthesis, a transferase superfamily member. A knowledgeable model could use the P-loop motif to eliminate non-nucleotide-dependent reactions (A, C) and the unusual, highly specific nature of B (a single-step cyclization of a complex alkaloid-like substrate) to favor D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold P-loop motif (GLAGAGKTT) provides a concrete, transferable sequence feature that meaningfully distinguishes the CTP-dependent nucleotidyl-transfer reaction (D) from the hydrolysis (A), cyclization (B), and dehydration (C) alternatives. This is a family-level inference based on conserved nucleotide-binding architecture shared across many transferase families, not a lookup of this protein's specific annotation."
  },
  "case_id": "catalytic_activity_0131",
  "expected_answer_check": {
    "evidence_ids": [
      "C1",
      "C4",
      "C5",
      "C7",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DY07 (sequence SHA256 match confirmed) annotates this protein as N-acylneuraminate cytidylyltransferase (EC 2.7.7.43), with the catalytic activity explicitly stated as 'an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate.' This is supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024, Biochemistry 63:688-698). The expected answer D matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The Rossmann fold (GxGxxG) is found in many enzyme classes beyond cytidylyltransferases (e.g., dehydrogenases, synthetases), so the motif alone narrows but does not uniquely identify the enzyme. The argument relies on the combination of the motif with the reaction chemistry of the offered choices.",
    "The CMP-Neu5Ac synthase family is well-known in sialic-acid biosynthesis, but recognizing it from sequence alone without prior exposure to the family's characteristic features would be more challenging.",
    "The experimental evidence (PubMed:38382015) post-dates the typical training cutoff for many models, though the enzyme family and reaction are long-established in biochemistry."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The nucleotide-binding motif strongly favors D over the other three choices. Choice B is a highly unusual single-step cyclization of a complex substrate with no obvious sequence-level support. Choices A and C describe reactions catalyzed by enzymes with entirely different structural folds (glycosidase TIM barrel or beta-propeller; iron-dependent dehydratase). No ambiguity among the offered alternatives is identified."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0131",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DY07 (sequence SHA256 match confirmed) annotates this protein as N-acylneuraminate cytidylyltransferase (EC 2.7.7.43), with the catalytic activity explicitly stated as 'an N-acylneuraminate + CTP = a CMP-N-acyl-beta-neuraminate + diphosphate.' This is supported by experimental evidence (ECO:0000269, PubMed:38382015, Ghosh & Raushel 2024, Biochemistry 63:688-698). The expected answer D matches the annotated reaction verbatim.",
    "evidence_ids": ["C1", "C4", "C5", "C7", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear Rossmann-fold nucleotide-binding motif 'GLAGAGKTT' (GxGxxG pattern), which is a hallmark of enzymes that bind nucleotide triphosphates such as CTP. Among the four offered reactions, only choice D involves a nucleotide substrate (CTP → CMP transfer + diphosphate release), consistent with a cytidylyltransferase. Choices A (glycosidase hydrolysis), B (a complex intramolecular cyclization/rearrangement), and C (a dehydratase reaction) do not involve nucleotide substrates and are mechanistically inconsistent with a P-loop nucleotide-binding fold. Additionally, the protein's size (~394 aa) and overall composition are consistent with the well-characterized CMP-Neu5Ac synthase family in bacterial sialic-acid biosynthesis, a transferase superfamily member. A knowledgeable model could use the P-loop motif to eliminate non-nucleotide-dependent reactions (A, C) and the unusual, highly specific nature of B (a single-step cyclization of a complex alkaloid-like substrate) to favor D.",
    "missing_item_specific_fact": "",
    "reason": "The Rossmann-fold P-loop motif (GLAGAGKTT) provides a concrete, transferable sequence feature that meaningfully distinguishes the CTP-dependent nucleotidyl-transfer reaction (D) from the hydrolysis (A), cyclization (B), and dehydration (C) alternatives. This is a family-level inference based on conserved nucleotide-binding architecture shared across many transferase families, not a lookup of this protein's specific annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The nucleotide-binding motif strongly favors D over the other three choices. Choice B is a highly unusual single-step cyclization of a complex substrate with no obvious sequence-level support. Choices A and C describe reactions catalyzed by enzymes with entirely different structural folds (glycosidase TIM barrel or beta-propeller; iron-dependent dehydratase). No ambiguity among the offered alternatives is identified."
  },
  "important_caveats": [
    "The Rossmann fold (GxGxxG) is found in many enzyme classes beyond cytidylyltransferases (e.g., dehydrogenases, synthetases), so the motif alone narrows but does not uniquely identify the enzyme. The argument relies on the combination of the motif with the reaction chemistry of the offered choices.",
    "The CMP-Neu5Ac synthase family is well-known in sialic-acid biosynthesis, but recognizing it from sequence alone without prior exposure to the family's characteristic features would be more challenging.",
    "The experimental evidence (PubMed:38382015) post-dates the typical training cutoff for many models, though the enzyme family and reaction are long-established in biochemistry."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 131. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
