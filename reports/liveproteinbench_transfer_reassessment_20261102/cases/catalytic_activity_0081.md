# catalytic_activity_0081

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0081.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **C** — L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)

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
A. O-phospho-L-seryl-[protein] + H2O = L-seryl-[protein] + phosphate
B. 3-O-beta-D-glucosyl-D-glucuronate + phosphate = aldehydo-D-glucuronate + alpha-D-glucose 1-phosphate
C. L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+)
D. dTMP + ATP = dTDP + ADP
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

> The matched-sequence UniProt annotation identifies the protein as homoserine kinase and assigns the reaction in choice C. The reaction assignment is transferred by similarity (ECO:0000250), so this supports the key as an annotation-based inference, not as direct experimental evidence for this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 357-residue sequence is consistent with a homoserine kinase in the GHMP kinase family. Transferable family recognition can distinguish this from the offered alternatives: homoserine kinase phosphorylates homoserine using ATP (C), whereas D is a different kinase reaction, A is a phosphatase reaction, and B is a phosphorylase reaction. In particular, the sequence length and lack of the characteristic Walker-A pattern expected for thymidylate kinase weigh against D. This is a family-level inference, not proof of the exact annotation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and reaction choices permit a meaningful family-level distinction for C without recalling this protein's database record. The inference is probabilistic; the reviewer-only annotation corroborates it but is not needed as the sole basis for answerability.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices describe distinct reaction types, and the sequence supports the homoserine-kinase interpretation rather than another offered reaction.


### Important caveats

- The supplied source annotation assigns the reaction by similarity to another protein; direct experimental validation for this exact sequence is not established by the excerpts.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 357-residue sequence is consistent with a homoserine kinase in the GHMP kinase family. Transferable family recognition can distinguish this from the offered alternatives: homoserine kinase phosphorylates homoserine using ATP (C), whereas D is a different kinase reaction, A is a phosphatase reaction, and B is a phosphorylase reaction. In particular, the sequence length and lack of the characteristic Walker-A pattern expected for thymidylate kinase weigh against D. This is a family-level inference, not proof of the exact annotation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and reaction choices permit a meaningful family-level distinction for C without recalling this protein's database record. The inference is probabilistic; the reviewer-only annotation corroborates it but is not needed as the sole basis for answerability."
  },
  "case_id": "catalytic_activity_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies the protein as homoserine kinase and assigns the reaction in choice C. The reaction assignment is transferred by similarity (ECO:0000250), so this supports the key as an annotation-based inference, not as direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The supplied source annotation assigns the reaction by similarity to another protein; direct experimental validation for this exact sequence is not established by the excerpts."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe distinct reaction types, and the sequence supports the homoserine-kinase interpretation rather than another offered reaction."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched-sequence UniProt annotation identifies the protein as homoserine kinase and assigns the reaction in choice C. The reaction assignment is transferred by similarity (ECO:0000250), so this supports the key as an annotation-based inference, not as direct experimental evidence for this exact protein.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 357-residue sequence is consistent with a homoserine kinase in the GHMP kinase family. Transferable family recognition can distinguish this from the offered alternatives: homoserine kinase phosphorylates homoserine using ATP (C), whereas D is a different kinase reaction, A is a phosphatase reaction, and B is a phosphorylase reaction. In particular, the sequence length and lack of the characteristic Walker-A pattern expected for thymidylate kinase weigh against D. This is a family-level inference, not proof of the exact annotation.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and reaction choices permit a meaningful family-level distinction for C without recalling this protein's database record. The inference is probabilistic; the reviewer-only annotation corroborates it but is not needed as the sole basis for answerability."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe distinct reaction types, and the sequence supports the homoserine-kinase interpretation rather than another offered reaction."
  },
  "important_caveats": [
    "The supplied source annotation assigns the reaction by similarity to another protein; direct experimental validation for this exact sequence is not established by the excerpts."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt entry J9VU26 (KHSE_CRYN9, Cryptococcus neoformans) annotates this protein as Homoserine kinase (EC 2.7.1.39) with catalytic activity L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+). The annotation evidence code is ECO:0000250 (inferred by similarity to P17423), so the reaction assignment is computational rather than directly measured on this protein. However, the gene name THR1, the threonine-biosynthesis pathway context, and the 2008 Kingsbury & McCusker study on threonine biosynthetic genes in C. neoformans provide functional support. The sequence (357 AA) matches the benchmark sequence exactly.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> Multiple transferable features distinguish choice C from the alternatives. (1) The N-terminal ~35 residues (MPARKYKIHVPCTSANIGPGFDVCGIALSLSLSLVVTIPSVSSGAE) exhibit hallmarks of a mitochondrial targeting presequence (positively charged N-terminus, hydroxyl-rich and amphipathic hydrophobic core). In fungi, the threonine biosynthesis pathway (homoserine dehydrogenase → homoserine kinase → threonine synthase) is mitochondrial, a well-established fact from S. cerevisiae and other fungi. (2) The protein length (~357 AA) is consistent with homoserine kinase (~300–360 AA) and far too large for thymidylate kinase (~130–160 AA), eliminating D. (3) The sequence contains motifs consistent with the GHMP kinase superfamily (e.g., the glycine-rich region 'GLGSSGAAVIAGVLLGDLLGN' and the catalytic-domain architecture 'GIGHFVRFGWAKEIKAIAVSPRFELATAKARGVLPESYSRKDMIFNLQRLAVLTTALARS…'), which includes homoserine kinase but excludes phosphatases (A) and phosphorylases (B). (4) Thymidylate kinase belongs to the P-loop NTPase fold (Walker A: GXXXXGK&#91;T/S&#93;), which is absent here, further ruling out D. Combining mitochondrial localization, GHMP-kinase family recognition, and size constraints, a knowledgeable model can credibly select C over A, B, and D without recalling this specific UniProt record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The mitochondrial targeting sequence, GHMP-kinase family motifs, and protein-length constraint are all observable in the original input and connect to well-established transferable knowledge about fungal amino-acid metabolism and kinase superfamilies. These features meaningfully separate C from the three distractors.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Choices A (phosphatase) and B (phosphorylase) are entirely different enzyme classes with no kinase-like motifs. Choice D (thymidylate kinase) is excluded by the ~357-aa length, absence of a Walker A P-loop, and mitochondrial targeting sequence. Only C is consistent with all observable features.


### Important caveats

- The UniProt annotation for the catalytic reaction carries evidence code ECO:0000250 (inferred by similarity to P17423), meaning the exact reaction was not directly assayed on this C. neoformans protein; it is a similarity-based transfer.
- The mitochondrial targeting sequence is a computational prediction from the N-terminal region; while strongly suggestive, it is not experimentally confirmed in the supplied evidence.
- The gene name THR1 and the Kingsbury & McCusker (2008) pathway study provide independent functional context but were not given to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Multiple transferable features distinguish choice C from the alternatives. (1) The N-terminal ~35 residues (MPARKYKIHVPCTSANIGPGFDVCGIALSLSLSLVVTIPSVSSGAE) exhibit hallmarks of a mitochondrial targeting presequence (positively charged N-terminus, hydroxyl-rich and amphipathic hydrophobic core). In fungi, the threonine biosynthesis pathway (homoserine dehydrogenase → homoserine kinase → threonine synthase) is mitochondrial, a well-established fact from S. cerevisiae and other fungi. (2) The protein length (~357 AA) is consistent with homoserine kinase (~300–360 AA) and far too large for thymidylate kinase (~130–160 AA), eliminating D. (3) The sequence contains motifs consistent with the GHMP kinase superfamily (e.g., the glycine-rich region 'GLGSSGAAVIAGVLLGDLLGN' and the catalytic-domain architecture 'GIGHFVRFGWAKEIKAIAVSPRFELATAKARGVLPESYSRKDMIFNLQRLAVLTTALARS…'), which includes homoserine kinase but excludes phosphatases (A) and phosphorylases (B). (4) Thymidylate kinase belongs to the P-loop NTPase fold (Walker A: GXXXXGK[T/S]), which is absent here, further ruling out D. Combining mitochondrial localization, GHMP-kinase family recognition, and size constraints, a knowledgeable model can credibly select C over A, B, and D without recalling this specific UniProt record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The mitochondrial targeting sequence, GHMP-kinase family motifs, and protein-length constraint are all observable in the original input and connect to well-established transferable knowledge about fungal amino-acid metabolism and kinase superfamilies. These features meaningfully separate C from the three distractors."
  },
  "case_id": "catalytic_activity_0081",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt entry J9VU26 (KHSE_CRYN9, Cryptococcus neoformans) annotates this protein as Homoserine kinase (EC 2.7.1.39) with catalytic activity L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+). The annotation evidence code is ECO:0000250 (inferred by similarity to P17423), so the reaction assignment is computational rather than directly measured on this protein. However, the gene name THR1, the threonine-biosynthesis pathway context, and the 2008 Kingsbury & McCusker study on threonine biosynthetic genes in C. neoformans provide functional support. The sequence (357 AA) matches the benchmark sequence exactly."
  },
  "important_caveats": [
    "The UniProt annotation for the catalytic reaction carries evidence code ECO:0000250 (inferred by similarity to P17423), meaning the exact reaction was not directly assayed on this C. neoformans protein; it is a similarity-based transfer.",
    "The mitochondrial targeting sequence is a computational prediction from the N-terminal region; while strongly suggestive, it is not experimentally confirmed in the supplied evidence.",
    "The gene name THR1 and the Kingsbury & McCusker (2008) pathway study provide independent functional context but were not given to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A (phosphatase) and B (phosphorylase) are entirely different enzyme classes with no kinase-like motifs. Choice D (thymidylate kinase) is excluded by the ~357-aa length, absence of a Walker A P-loop, and mitochondrial targeting sequence. Only C is consistent with all observable features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0081",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt entry J9VU26 (KHSE_CRYN9, Cryptococcus neoformans) annotates this protein as Homoserine kinase (EC 2.7.1.39) with catalytic activity L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+). The annotation evidence code is ECO:0000250 (inferred by similarity to P17423), so the reaction assignment is computational rather than directly measured on this protein. However, the gene name THR1, the threonine-biosynthesis pathway context, and the 2008 Kingsbury & McCusker study on threonine biosynthetic genes in C. neoformans provide functional support. The sequence (357 AA) matches the benchmark sequence exactly.",
    "evidence_ids": ["C4", "C5", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "Multiple transferable features distinguish choice C from the alternatives. (1) The N-terminal ~35 residues (MPARKYKIHVPCTSANIGPGFDVCGIALSLSLSLVVTIPSVSSGAE) exhibit hallmarks of a mitochondrial targeting presequence (positively charged N-terminus, hydroxyl-rich and amphipathic hydrophobic core). In fungi, the threonine biosynthesis pathway (homoserine dehydrogenase → homoserine kinase → threonine synthase) is mitochondrial, a well-established fact from S. cerevisiae and other fungi. (2) The protein length (~357 AA) is consistent with homoserine kinase (~300–360 AA) and far too large for thymidylate kinase (~130–160 AA), eliminating D. (3) The sequence contains motifs consistent with the GHMP kinase superfamily (e.g., the glycine-rich region 'GLGSSGAAVIAGVLLGDLLGN' and the catalytic-domain architecture 'GIGHFVRFGWAKEIKAIAVSPRFELATAKARGVLPESYSRKDMIFNLQRLAVLTTALARS…'), which includes homoserine kinase but excludes phosphatases (A) and phosphorylases (B). (4) Thymidylate kinase belongs to the P-loop NTPase fold (Walker A: GXXXXGK[T/S]), which is absent here, further ruling out D. Combining mitochondrial localization, GHMP-kinase family recognition, and size constraints, a knowledgeable model can credibly select C over A, B, and D without recalling this specific UniProt record.",
    "missing_item_specific_fact": "",
    "reason": "The mitochondrial targeting sequence, GHMP-kinase family motifs, and protein-length constraint are all observable in the original input and connect to well-established transferable knowledge about fungal amino-acid metabolism and kinase superfamilies. These features meaningfully separate C from the three distractors."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Choices A (phosphatase) and B (phosphorylase) are entirely different enzyme classes with no kinase-like motifs. Choice D (thymidylate kinase) is excluded by the ~357-aa length, absence of a Walker A P-loop, and mitochondrial targeting sequence. Only C is consistent with all observable features."
  },
  "important_caveats": [
    "The UniProt annotation for the catalytic reaction carries evidence code ECO:0000250 (inferred by similarity to P17423), meaning the exact reaction was not directly assayed on this C. neoformans protein; it is a similarity-based transfer.",
    "The mitochondrial targeting sequence is a computational prediction from the N-terminal region; while strongly suggestive, it is not experimentally confirmed in the supplied evidence.",
    "The gene name THR1 and the Kingsbury & McCusker (2008) pathway study provide independent functional context but were not given to the evaluated model."
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 81. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
