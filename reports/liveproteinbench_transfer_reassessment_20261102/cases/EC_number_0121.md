# EC_number_0121

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0121.txt)

**Task:** `EC_number`  
**Expected answer:** **A** — 2.7.1.39

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MPARKYKIHVPCTSANIGPGFDVCGIALSLSLSLVVTIPSVSSGAEPLPKIIYTGLDSDNVPLSPYKNLLTRVALYVLRANGITTFPPGVTIEARNEIPFGRGLGSSGAAVIAGVLLGDLLGNLSLPKSRLLDFALMVERHPDNVTAALMGGFVGSYLRELSPEDMSAASIPLAEVLPEYPPDAGPDWGKSPPQPPHGIGHFVRFGWAKEIKAIAVSPRFELATAKARGVLPESYSRKDMIFNLQRLAVLTTALARSPPDPDLIYDAMGDRVHQPYRMTLIPGLPKILSTLTPTSHPGLLGICLSGAGPTILALATHNFEAIANEIERIFGDEQVLVDHKVLNIDEKGSWVEDITEA

[Multiple Choices]
A. 2.7.1.39
B. 2.7.1.52
C. 5.1.3.45
D. 1.1.1.1
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

> The sequence-matched UniProt record assigns EC 2.7.1.39 and specifies the homoserine-to-O-phosphohomoserine reaction. The annotation is supported by evidence transferred from a homolog (ECO:0000250), not by direct experimental evidence shown here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a eukaryotic THR1/homoserine-kinase family member: transferable recognition of the family’s sequence profile and conserved kinase features supports EC 2.7.1.39. This goes beyond identifying a generic kinase, which would not alone separate A from another kinase option; the homoserine-kinase family match distinguishes A from B and the non-kinase options C and D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition learned from related proteins provides a meaningful basis for selecting the homoserine kinase EC among these choices, without requiring the exact target’s database record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The family-level inference supports A; no other offered choice is comparably supported by the sequence.


### Important caveats

- Reviewer evidence confirms an exact sequence match, but the EC annotation is similarity-transferred rather than independently demonstrated by experimental evidence in the supplied excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a eukaryotic THR1/homoserine-kinase family member: transferable recognition of the family’s sequence profile and conserved kinase features supports EC 2.7.1.39. This goes beyond identifying a generic kinase, which would not alone separate A from another kinase option; the homoserine-kinase family match distinguishes A from B and the non-kinase options C and D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition learned from related proteins provides a meaningful basis for selecting the homoserine kinase EC among these choices, without requiring the exact target’s database record."
  },
  "case_id": "EC_number_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.7.1.39 and specifies the homoserine-to-O-phosphohomoserine reaction. The annotation is supported by evidence transferred from a homolog (ECO:0000250), not by direct experimental evidence shown here."
  },
  "important_caveats": [
    "Reviewer evidence confirms an exact sequence match, but the EC annotation is similarity-transferred rather than independently demonstrated by experimental evidence in the supplied excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level inference supports A; no other offered choice is comparably supported by the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0121",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record assigns EC 2.7.1.39 and specifies the homoserine-to-O-phosphohomoserine reaction. The annotation is supported by evidence transferred from a homolog (ECO:0000250), not by direct experimental evidence shown here.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a eukaryotic THR1/homoserine-kinase family member: transferable recognition of the family’s sequence profile and conserved kinase features supports EC 2.7.1.39. This goes beyond identifying a generic kinase, which would not alone separate A from another kinase option; the homoserine-kinase family match distinguishes A from B and the non-kinase options C and D.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition learned from related proteins provides a meaningful basis for selecting the homoserine kinase EC among these choices, without requiring the exact target’s database record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level inference supports A; no other offered choice is comparably supported by the sequence."
  },
  "important_caveats": [
    "Reviewer evidence confirms an exact sequence match, but the EC annotation is similarity-transferred rather than independently demonstrated by experimental evidence in the supplied excerpts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry J9VU26 (KHSE_CRYN9) annotates this protein as Homoserine kinase with EC 2.7.1.39. The annotation is present in both the current record (entry version 53) and the historical Swiss-Prot record (entry version 51). The evidence code is ECO:0000250 (inferred by similarity from UniProtKB:P17423, the S. cerevisiae homoserine kinase), so this is a computational/similarity-based annotation rather than direct experimental characterization of this exact protein. The catalytic activity (L-homoserine + ATP = O-phospho-L-homoserine + ADP + H+) is consistent with EC 2.7.1.39. The sequence matches the benchmark input exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Several transferable features distinguish the answer. (1) Sequence length: the protein is 357 aa, consistent with GHMP kinase family members (~300-400 aa) but too short for pyruvate kinase (EC 2.7.1.52), which is typically 500-600 aa with a TIM-barrel fold. (2) GHMP kinase motifs: the sequence contains 'GIGHFVRFG' and glycine-rich regions (e.g., 'GAGPTILALATHNFEAIANEIERIFGDEQ') consistent with the GHMP kinase superfamily (Galactokinase, Homoserine kinase, Mevalonate kinase, Phosphomevalonate kinase), which is the family containing homoserine kinase. Pyruvate kinase has a completely different fold and sequence signature. (3) Elimination of other classes: EC 1.1.1.1 (alcohol dehydrogenase) requires a Rossmann fold with GxGxxG motif and zinc-binding residues, absent here. EC 5.1.3.45 is an isomerase, a fundamentally different enzyme class with no kinase-like motifs. (4) Among the two kinase options, the GHMP kinase motif pattern and the ~357 aa size point to homoserine kinase (2.7.1.39) rather than pyruvate kinase (2.7.1.52). While the exact substrate specificity (homoserine vs mevalonate vs galactose) within GHMP kinases is harder to determine from sequence alone, those alternatives are not among the offered choices, so the distinction among the four options is achievable through family recognition and elimination.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can use sequence length, GHMP kinase family motif recognition, and elimination of non-kinase and wrong-fold kinase options to arrive at 2.7.1.39. This relies on well-established family-level knowledge of the GHMP kinase superfamily and general structural biology of pyruvate kinase and alcohol dehydrogenase, which are transferable across proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span three different enzyme classes (kinase, isomerase, oxidoreductase) and within kinases two very different families (GHMP kinase vs pyruvate kinase/TIM barrel). The sequence features and length clearly favor GHMP kinase over pyruvate kinase, and the kinase activity rules out the isomerase and oxidoreductase options. No other option is defensible.


### Important caveats

- The EC annotation for this protein is inferred by similarity (ECO:0000250) from S. cerevisiae homoserine kinase (P17423), not from direct experimental characterization of the Cryptococcus neoformans protein.
- Within the GHMP kinase superfamily, distinguishing homoserine kinase from mevalonate kinase or phosphomevalonate kinase by sequence alone can be challenging; however, those alternatives are not among the offered choices, so this does not affect the answerability among the given options.
- The annotation evidence code ECO:0000305 on the recommended name indicates the name was assigned based on the entry's own evidence, while the EC number itself carries ECO:0000250 (similarity to P17423).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Several transferable features distinguish the answer. (1) Sequence length: the protein is 357 aa, consistent with GHMP kinase family members (~300-400 aa) but too short for pyruvate kinase (EC 2.7.1.52), which is typically 500-600 aa with a TIM-barrel fold. (2) GHMP kinase motifs: the sequence contains 'GIGHFVRFG' and glycine-rich regions (e.g., 'GAGPTILALATHNFEAIANEIERIFGDEQ') consistent with the GHMP kinase superfamily (Galactokinase, Homoserine kinase, Mevalonate kinase, Phosphomevalonate kinase), which is the family containing homoserine kinase. Pyruvate kinase has a completely different fold and sequence signature. (3) Elimination of other classes: EC 1.1.1.1 (alcohol dehydrogenase) requires a Rossmann fold with GxGxxG motif and zinc-binding residues, absent here. EC 5.1.3.45 is an isomerase, a fundamentally different enzyme class with no kinase-like motifs. (4) Among the two kinase options, the GHMP kinase motif pattern and the ~357 aa size point to homoserine kinase (2.7.1.39) rather than pyruvate kinase (2.7.1.52). While the exact substrate specificity (homoserine vs mevalonate vs galactose) within GHMP kinases is harder to determine from sequence alone, those alternatives are not among the offered choices, so the distinction among the four options is achievable through family recognition and elimination.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use sequence length, GHMP kinase family motif recognition, and elimination of non-kinase and wrong-fold kinase options to arrive at 2.7.1.39. This relies on well-established family-level knowledge of the GHMP kinase superfamily and general structural biology of pyruvate kinase and alcohol dehydrogenase, which are transferable across proteins."
  },
  "case_id": "EC_number_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry J9VU26 (KHSE_CRYN9) annotates this protein as Homoserine kinase with EC 2.7.1.39. The annotation is present in both the current record (entry version 53) and the historical Swiss-Prot record (entry version 51). The evidence code is ECO:0000250 (inferred by similarity from UniProtKB:P17423, the S. cerevisiae homoserine kinase), so this is a computational/similarity-based annotation rather than direct experimental characterization of this exact protein. The catalytic activity (L-homoserine + ATP = O-phospho-L-homoserine + ADP + H+) is consistent with EC 2.7.1.39. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The EC annotation for this protein is inferred by similarity (ECO:0000250) from S. cerevisiae homoserine kinase (P17423), not from direct experimental characterization of the Cryptococcus neoformans protein.",
    "Within the GHMP kinase superfamily, distinguishing homoserine kinase from mevalonate kinase or phosphomevalonate kinase by sequence alone can be challenging; however, those alternatives are not among the offered choices, so this does not affect the answerability among the given options.",
    "The annotation evidence code ECO:0000305 on the recommended name indicates the name was assigned based on the entry's own evidence, while the EC number itself carries ECO:0000250 (similarity to P17423)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different enzyme classes (kinase, isomerase, oxidoreductase) and within kinases two very different families (GHMP kinase vs pyruvate kinase/TIM barrel). The sequence features and length clearly favor GHMP kinase over pyruvate kinase, and the kinase activity rules out the isomerase and oxidoreductase options. No other option is defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0121",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry J9VU26 (KHSE_CRYN9) annotates this protein as Homoserine kinase with EC 2.7.1.39. The annotation is present in both the current record (entry version 53) and the historical Swiss-Prot record (entry version 51). The evidence code is ECO:0000250 (inferred by similarity from UniProtKB:P17423, the S. cerevisiae homoserine kinase), so this is a computational/similarity-based annotation rather than direct experimental characterization of this exact protein. The catalytic activity (L-homoserine + ATP = O-phospho-L-homoserine + ADP + H+) is consistent with EC 2.7.1.39. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Several transferable features distinguish the answer. (1) Sequence length: the protein is 357 aa, consistent with GHMP kinase family members (~300-400 aa) but too short for pyruvate kinase (EC 2.7.1.52), which is typically 500-600 aa with a TIM-barrel fold. (2) GHMP kinase motifs: the sequence contains 'GIGHFVRFG' and glycine-rich regions (e.g., 'GAGPTILALATHNFEAIANEIERIFGDEQ') consistent with the GHMP kinase superfamily (Galactokinase, Homoserine kinase, Mevalonate kinase, Phosphomevalonate kinase), which is the family containing homoserine kinase. Pyruvate kinase has a completely different fold and sequence signature. (3) Elimination of other classes: EC 1.1.1.1 (alcohol dehydrogenase) requires a Rossmann fold with GxGxxG motif and zinc-binding residues, absent here. EC 5.1.3.45 is an isomerase, a fundamentally different enzyme class with no kinase-like motifs. (4) Among the two kinase options, the GHMP kinase motif pattern and the ~357 aa size point to homoserine kinase (2.7.1.39) rather than pyruvate kinase (2.7.1.52). While the exact substrate specificity (homoserine vs mevalonate vs galactose) within GHMP kinases is harder to determine from sequence alone, those alternatives are not among the offered choices, so the distinction among the four options is achievable through family recognition and elimination.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can use sequence length, GHMP kinase family motif recognition, and elimination of non-kinase and wrong-fold kinase options to arrive at 2.7.1.39. This relies on well-established family-level knowledge of the GHMP kinase superfamily and general structural biology of pyruvate kinase and alcohol dehydrogenase, which are transferable across proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span three different enzyme classes (kinase, isomerase, oxidoreductase) and within kinases two very different families (GHMP kinase vs pyruvate kinase/TIM barrel). The sequence features and length clearly favor GHMP kinase over pyruvate kinase, and the kinase activity rules out the isomerase and oxidoreductase options. No other option is defensible."
  },
  "important_caveats": [
    "The EC annotation for this protein is inferred by similarity (ECO:0000250) from S. cerevisiae homoserine kinase (P17423), not from direct experimental characterization of the Cryptococcus neoformans protein.",
    "Within the GHMP kinase superfamily, distinguishing homoserine kinase from mevalonate kinase or phosphomevalonate kinase by sequence alone can be challenging; however, those alternatives are not among the offered choices, so this does not affect the answerability among the given options.",
    "The annotation evidence code ECO:0000305 on the recommended name indicates the name was assigned based on the entry's own evidence, while the EC number itself carries ECO:0000250 (similarity to P17423)."
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
  "benchmark_sequence_length": 357,
  "benchmark_sequence_sha256": "0d5b6ca56754f8b7a34530cb0993479508f4e035318ede70547b7393e120e776",
  "current_entry_audit": {
    "entryVersion": 53,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2012-11-28",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 357,
  "current_source_sequence_sha256": "0d5b6ca56754f8b7a34530cb0993479508f4e035318ede70547b7393e120e776",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 51,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "J9VU26",
  "selected_historical_entry_version": 51,
  "selected_historical_record_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "selected_historical_source_sequence_length": 357,
  "selected_historical_source_sequence_sha256": "0d5b6ca56754f8b7a34530cb0993479508f4e035318ede70547b7393e120e776",
  "selected_historical_version": {
    "accession": "J9VU26",
    "database": "Swiss-Prot",
    "entryVersion": 51,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "KHSE_CRYN9",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"J9VU26\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":53,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2012-11-28\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Cryptococcus neoformans var. grubii serotype A\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000010091\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Basidiomycota\",\"Agaricomycotina\",\"Tremellomycetes\",\"Tremellales\",\"Cryptococcaceae\",\"Cryptococcus\",\"Cryptococcus neoformans species complex\"],\"scientificName\":\"Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\",\"taxonId\":235443}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17423\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.1.39\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Homoserine kinase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"HK\"},{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"HSK\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/J9VU26.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17423\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:13986\"}}],\"reaction\":{\"ecNumber\":\"2.7.1.39\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P17423\",\"source\":\"UniProtKB\"}],\"name\":\"L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:13985\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57476\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57590\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:11.100039+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0e9afaf34be107a1ef4697a7739b7135416509845602d34b04e02d7fb3acefe1",
  "url": "https://rest.uniprot.org/uniprotkb/J9VU26.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H1",
  "excerpt": "ID   KHSE_CRYN9              Reviewed;         357 AA.\nAC   J9VU26; B2MVI2;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   28-NOV-2012, sequence version 1.\nDT   28-JAN-2026, entry version 51.\nDE   RecName: Full=Homoserine kinase {ECO:0000305};\nDE            Short=HK {ECO:0000305};\nDE            Short=HSK {ECO:0000305};\nDE            EC=2.7.1.39 {ECO:0000250|UniProtKB:P17423};\nGN   Name=THR1 {ECO:0000303|PubMed:18757810};\nGN   ORFNames=CNAG_04156 {ECO:0000312|EMBL:AFR96886.1};\nOS   Cryptococcus neoformans (strain H99 / ATCC 208821 / CBS 10515 / FGSC 9487)\nOS   (Cryptococcus neoformans var. grubii serotype A).\nOC   Eukaryota; Fungi; Dikarya; Basidiomycota; Agaricomycotina; Tremellomycetes;\nOC   Tremellales; Cryptococcaceae; Cryptococcus;\nOC   Cryptococcus neoformans species complex.\nOX   NCBI_TaxID=235443 {ECO:0000312|Proteomes:UP000010091};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.320227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "url": "https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Homoserine kinase {ECO:0000305};\nDE            Short=HK {ECO:0000305};\nDE            Short=HSK {ECO:0000305};\nDE            EC=2.7.1.39 {ECO:0000250|UniProtKB:P17423};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.320227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "url": "https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ACC85591.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, PATHWAY, AND DISRUPTION PHENOTYPE.\nRX   PubMed=18757810; DOI=10.1099/mic.0.2008/019729-0;\nRA   Kingsbury J.M., McCusker J.H.;\nRT   \"Threonine biosynthetic genes are essential in Cryptococcus neoformans.\";\nRL   Microbiology 154:2767-2775(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.320227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "url": "https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51)

```json
{
  "entry_version": 51,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+);\nCC         Xref=Rhea:RHEA:13985, ChEBI:CHEBI:15378, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:57476, ChEBI:CHEBI:57590, ChEBI:CHEBI:456216;\nCC         EC=2.7.1.39; Evidence={ECO:0000250|UniProtKB:P17423};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:13986;\nCC         Evidence={ECO:0000250|UniProtKB:P17423};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:15.320227+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fc5fc0e459f5fad429e5682de28d956b045a7721e17c0769394b8a51086bfc87",
  "url": "https://rest.uniprot.org/unisave/J9VU26?format=txt&versions=51"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 121. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
