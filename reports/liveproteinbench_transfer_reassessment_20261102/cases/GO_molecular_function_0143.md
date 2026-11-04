# GO_molecular_function_0143

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0143.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — transferase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSANTGKPARHYLISYPRTASNLLLKILALDSQPNFSSGGFDGGYFFMPADDILTDPRIRVRARSISDWTADERAQLKETFQACFEAQQRWLESAESQGQSVFVKEHTVFFADPTARSCLQFGPSATSEPAWTVEYAGGSTHSKLNITVLPDEFLLTWLPTFLIRHPALAFPSLYRTVIKREGKESAAADNFASLLTTVEWSRSLYDFYVQNRESLPCSPDQRLEWPIVLDADDIIAHPATVTLYCDKIGMDPRQLCFNWDQLKSEELSKIEPNQLAMRMSLYQSTGIDTSKSSRGINVDDEATKWRSEFGIAVADHIEKLVRGAMADYEYLRARRLRAD

[Multiple Choices]
A. UMP/dUMP kinase activity
B. protein binding involved in heterotypic cell-cell adhesion
C. transferase activity
D. glucose-6-phosphate isomerase activity
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Molecular Function Prediction, which is to predict the fundamental activity of a protein at the molecular level, as defined by the Gene Ontology (GO) 'Molecular Function' branch. This describes the elemental tasks a protein performs, such as catalysis, transport, or binding to specific molecules. Based on the protein's amino acid sequence, you are to select the option that best describes its primary molecular function.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies the protein as a sulfotransferase, which is a transferase. The broader choice C is therefore supported, though the annotation says the enzyme’s specific pathway role remains undetermined.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 340-aa sequence is consistent with a soluble enzyme and does not show the familiar P-loop nucleotide-binding motif expected for many kinases, making A less compelling. It is also substantially shorter than typical glucose-6-phosphate isomerases, weakening D; a cell-adhesion binding role is a poor fit for this enzyme-like sequence. Among these choices, the broad enzyme class C is the best-supported inference. This is a probabilistic inference from sequence and transferable enzyme-family patterns, not a definitive identification of a sulfotransferase from the sequence alone.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The offered alternatives are sufficiently distinct for sequence length, enzyme-like character, and transferable knowledge of common kinase motifs and isomerase families to favor C. No exact-protein annotation is necessary to make that distinction, although it would strengthen the conclusion.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives describe different functions, and the broad transferase option is the best fit among those offered.


### Important caveats

- The reviewer-only annotation supports the key but was not part of the original input.
- The sequence-based discrimination is strongest against the named alternatives; it does not independently establish the enzyme’s precise substrate or pathway role.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 340-aa sequence is consistent with a soluble enzyme and does not show the familiar P-loop nucleotide-binding motif expected for many kinases, making A less compelling. It is also substantially shorter than typical glucose-6-phosphate isomerases, weakening D; a cell-adhesion binding role is a poor fit for this enzyme-like sequence. Among these choices, the broad enzyme class C is the best-supported inference. This is a probabilistic inference from sequence and transferable enzyme-family patterns, not a definitive identification of a sulfotransferase from the sequence alone.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The offered alternatives are sufficiently distinct for sequence length, enzyme-like character, and transferable knowledge of common kinase motifs and isomerase families to favor C. No exact-protein annotation is necessary to make that distinction, although it would strengthen the conclusion."
  },
  "case_id": "GO_molecular_function_0143",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as a sulfotransferase, which is a transferase. The broader choice C is therefore supported, though the annotation says the enzyme’s specific pathway role remains undetermined."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not part of the original input.",
    "The sequence-based discrimination is strongest against the named alternatives; it does not independently establish the enzyme’s precise substrate or pathway role."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe different functions, and the broad transferase option is the best fit among those offered."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0143",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies the protein as a sulfotransferase, which is a transferase. The broader choice C is therefore supported, though the annotation says the enzyme’s specific pathway role remains undetermined.",
    "evidence_ids": ["C4", "C5", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 340-aa sequence is consistent with a soluble enzyme and does not show the familiar P-loop nucleotide-binding motif expected for many kinases, making A less compelling. It is also substantially shorter than typical glucose-6-phosphate isomerases, weakening D; a cell-adhesion binding role is a poor fit for this enzyme-like sequence. Among these choices, the broad enzyme class C is the best-supported inference. This is a probabilistic inference from sequence and transferable enzyme-family patterns, not a definitive identification of a sulfotransferase from the sequence alone.",
    "missing_item_specific_fact": "",
    "reason": "The offered alternatives are sufficiently distinct for sequence length, enzyme-like character, and transferable knowledge of common kinase motifs and isomerase families to favor C. No exact-protein annotation is necessary to make that distinction, although it would strengthen the conclusion."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives describe different functions, and the broad transferase option is the best fit among those offered."
  },
  "important_caveats": [
    "The reviewer-only annotation supports the key but was not part of the original input.",
    "The sequence-based discrimination is strongest against the named alternatives; it does not independently establish the enzyme’s precise substrate or pathway role."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A455ZLR3) annotates this protein as 'Sulfotransferase ppzF' with EC 2.8.2.- and GO:0016740 (transferase activity). EC 2.8.2.- is a subclass of EC class 2 (transferases), and the GO term definition states 'Transferase is the systematic name for any enzyme of EC class 2.' The evidence codes include IEA (inferred from electronic annotation via keyword) and ECO:0000250 (by similarity to Q4H424), with some experimental pathway context from PubMed 30452111 and 38578094. The entry notes 'The role of ppzF within the pathway has still to be determined,' so the sulfotransferase assignment is primarily computational/inferred rather than directly demonstrated for this specific protein, but the EC class 2 assignment and the 'Sulfotransferase' recommended name support the broad 'transferase activity' annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4), [H5](#evidence-h5), [GO2](#evidence-go2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 340-aa sequence is consistent with the sulfotransferase protein family (~300-350 aa, characteristic fold with PAPS-binding motifs). Regions such as 'GFDGGYFFMPADD' near the N-terminus and 'GMDPRQLCFNWDQLKSEELSKIEPNQLAMRMSLYQSTGIDTSKSSRGINVDDEATKWRSEFGIAVADHIEKLVRGAMADYEYLRARRLRAD' in the C-terminal half show patterns consistent with the conserved sulfotransferase fold and PAPS-binding architecture seen across the well-characterized sulfotransferase superfamily. Recognizing this family (transferable knowledge from hundreds of characterized sulfotransferases in animals, plants, fungi, and bacteria) leads to the inference that the protein catalyzes group transfer (sulfuryl transfer from PAPS), placing it in EC class 2 = transferase activity. The other options can be excluded: (D) glucose-6-phosphate isomerase is a ~550-aa TIM-barrel glycolytic enzyme with a very different sequence architecture; (B) heterotypic cell-cell adhesion binding requires Ig, cadherin, or integrin-type domains absent here; (A) UMP/dUMP kinase requires a P-loop nucleotide-binding motif (GXXXXGK&#91;T/S&#93;) and is typically ~250 aa, neither of which matches this sequence. Thus, family-level recognition of the sulfotransferase fold plus the known fact that all sulfotransferases are transferases (EC class 2) provides a concrete, transferable basis for selecting C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A model with knowledge of the sulfotransferase protein family (its size, fold, PAPS-binding motifs, and classification as EC class 2 transferases) can recognize the sequence features and rule out the other three options by their absent characteristic domains/motifs. This is standard family-level inference from other proteins, not memorization of this specific entry's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options are well-distinguished by sequence features. Option C (transferase activity, EC class 2) is the broad category encompassing sulfotransferases. Option A (UMP/dUMP kinase) is a specific nucleotide kinase with P-loop motifs absent here. Option B (heterotypic adhesion) requires adhesion domains not present. Option D (GPI) requires a TIM-barrel fold and ~550 aa length inconsistent with this 340-aa protein. No two options are simultaneously defensible for this sequence.


### Important caveats

- The sulfotransferase assignment for ppzF is primarily computational (IEA, by similarity to Q4H424) and the UniProt entry explicitly states 'The role of ppzF within the pathway has still to be determined.' The EC 2.8.2.- assignment uses ECO:0000305 (inferred by sequence similarity).
- Option C 'transferase activity' (GO:0016740) is an extremely broad parent term. If the protein were any EC class 2 enzyme (kinase, methyltransferase, glycosyltransferase, etc.), C would also be technically correct. The question's validity relies on the other three options being specifically wrong for this sequence.
- The reviewer-only evidence identifies the protein as A0A455ZLR3 (Metarhizium majus, strain ARSEF 297), but this accession and organism identity were not provided to the evaluated model; the model must work from the raw sequence alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 340-aa sequence is consistent with the sulfotransferase protein family (~300-350 aa, characteristic fold with PAPS-binding motifs). Regions such as 'GFDGGYFFMPADD' near the N-terminus and 'GMDPRQLCFNWDQLKSEELSKIEPNQLAMRMSLYQSTGIDTSKSSRGINVDDEATKWRSEFGIAVADHIEKLVRGAMADYEYLRARRLRAD' in the C-terminal half show patterns consistent with the conserved sulfotransferase fold and PAPS-binding architecture seen across the well-characterized sulfotransferase superfamily. Recognizing this family (transferable knowledge from hundreds of characterized sulfotransferases in animals, plants, fungi, and bacteria) leads to the inference that the protein catalyzes group transfer (sulfuryl transfer from PAPS), placing it in EC class 2 = transferase activity. The other options can be excluded: (D) glucose-6-phosphate isomerase is a ~550-aa TIM-barrel glycolytic enzyme with a very different sequence architecture; (B) heterotypic cell-cell adhesion binding requires Ig, cadherin, or integrin-type domains absent here; (A) UMP/dUMP kinase requires a P-loop nucleotide-binding motif (GXXXXGK[T/S]) and is typically ~250 aa, neither of which matches this sequence. Thus, family-level recognition of the sulfotransferase fold plus the known fact that all sulfotransferases are transferases (EC class 2) provides a concrete, transferable basis for selecting C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the sulfotransferase protein family (its size, fold, PAPS-binding motifs, and classification as EC class 2 transferases) can recognize the sequence features and rule out the other three options by their absent characteristic domains/motifs. This is standard family-level inference from other proteins, not memorization of this specific entry's annotation."
  },
  "case_id": "GO_molecular_function_0143",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4",
      "H5",
      "GO2"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A455ZLR3) annotates this protein as 'Sulfotransferase ppzF' with EC 2.8.2.- and GO:0016740 (transferase activity). EC 2.8.2.- is a subclass of EC class 2 (transferases), and the GO term definition states 'Transferase is the systematic name for any enzyme of EC class 2.' The evidence codes include IEA (inferred from electronic annotation via keyword) and ECO:0000250 (by similarity to Q4H424), with some experimental pathway context from PubMed 30452111 and 38578094. The entry notes 'The role of ppzF within the pathway has still to be determined,' so the sulfotransferase assignment is primarily computational/inferred rather than directly demonstrated for this specific protein, but the EC class 2 assignment and the 'Sulfotransferase' recommended name support the broad 'transferase activity' annotation."
  },
  "important_caveats": [
    "The sulfotransferase assignment for ppzF is primarily computational (IEA, by similarity to Q4H424) and the UniProt entry explicitly states 'The role of ppzF within the pathway has still to be determined.' The EC 2.8.2.- assignment uses ECO:0000305 (inferred by sequence similarity).",
    "Option C 'transferase activity' (GO:0016740) is an extremely broad parent term. If the protein were any EC class 2 enzyme (kinase, methyltransferase, glycosyltransferase, etc.), C would also be technically correct. The question's validity relies on the other three options being specifically wrong for this sequence.",
    "The reviewer-only evidence identifies the protein as A0A455ZLR3 (Metarhizium majus, strain ARSEF 297), but this accession and organism identity were not provided to the evaluated model; the model must work from the raw sequence alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-distinguished by sequence features. Option C (transferase activity, EC class 2) is the broad category encompassing sulfotransferases. Option A (UMP/dUMP kinase) is a specific nucleotide kinase with P-loop motifs absent here. Option B (heterotypic adhesion) requires adhesion domains not present. Option D (GPI) requires a TIM-barrel fold and ~550 aa length inconsistent with this 340-aa protein. No two options are simultaneously defensible for this sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0143",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A455ZLR3) annotates this protein as 'Sulfotransferase ppzF' with EC 2.8.2.- and GO:0016740 (transferase activity). EC 2.8.2.- is a subclass of EC class 2 (transferases), and the GO term definition states 'Transferase is the systematic name for any enzyme of EC class 2.' The evidence codes include IEA (inferred from electronic annotation via keyword) and ECO:0000250 (by similarity to Q4H424), with some experimental pathway context from PubMed 30452111 and 38578094. The entry notes 'The role of ppzF within the pathway has still to be determined,' so the sulfotransferase assignment is primarily computational/inferred rather than directly demonstrated for this specific protein, but the EC class 2 assignment and the 'Sulfotransferase' recommended name support the broad 'transferase activity' annotation.",
    "evidence_ids": ["C4", "C5", "H4", "H5", "GO2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 340-aa sequence is consistent with the sulfotransferase protein family (~300-350 aa, characteristic fold with PAPS-binding motifs). Regions such as 'GFDGGYFFMPADD' near the N-terminus and 'GMDPRQLCFNWDQLKSEELSKIEPNQLAMRMSLYQSTGIDTSKSSRGINVDDEATKWRSEFGIAVADHIEKLVRGAMADYEYLRARRLRAD' in the C-terminal half show patterns consistent with the conserved sulfotransferase fold and PAPS-binding architecture seen across the well-characterized sulfotransferase superfamily. Recognizing this family (transferable knowledge from hundreds of characterized sulfotransferases in animals, plants, fungi, and bacteria) leads to the inference that the protein catalyzes group transfer (sulfuryl transfer from PAPS), placing it in EC class 2 = transferase activity. The other options can be excluded: (D) glucose-6-phosphate isomerase is a ~550-aa TIM-barrel glycolytic enzyme with a very different sequence architecture; (B) heterotypic cell-cell adhesion binding requires Ig, cadherin, or integrin-type domains absent here; (A) UMP/dUMP kinase requires a P-loop nucleotide-binding motif (GXXXXGK[T/S]) and is typically ~250 aa, neither of which matches this sequence. Thus, family-level recognition of the sulfotransferase fold plus the known fact that all sulfotransferases are transferases (EC class 2) provides a concrete, transferable basis for selecting C.",
    "missing_item_specific_fact": "",
    "reason": "A model with knowledge of the sulfotransferase protein family (its size, fold, PAPS-binding motifs, and classification as EC class 2 transferases) can recognize the sequence features and rule out the other three options by their absent characteristic domains/motifs. This is standard family-level inference from other proteins, not memorization of this specific entry's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options are well-distinguished by sequence features. Option C (transferase activity, EC class 2) is the broad category encompassing sulfotransferases. Option A (UMP/dUMP kinase) is a specific nucleotide kinase with P-loop motifs absent here. Option B (heterotypic adhesion) requires adhesion domains not present. Option D (GPI) requires a TIM-barrel fold and ~550 aa length inconsistent with this 340-aa protein. No two options are simultaneously defensible for this sequence."
  },
  "important_caveats": [
    "The sulfotransferase assignment for ppzF is primarily computational (IEA, by similarity to Q4H424) and the UniProt entry explicitly states 'The role of ppzF within the pathway has still to be determined.' The EC 2.8.2.- assignment uses ECO:0000305 (inferred by sequence similarity).",
    "Option C 'transferase activity' (GO:0016740) is an extremely broad parent term. If the protein were any EC class 2 enzyme (kinase, methyltransferase, glycosyltransferase, etc.), C would also be technically correct. The question's validity relies on the other three options being specifically wrong for this sequence.",
    "The reviewer-only evidence identifies the protein as A0A455ZLR3 (Metarhizium majus, strain ARSEF 297), but this accession and organism identity were not provided to the evaluated model; the model must work from the raw sequence alone."
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
  "benchmark_sequence_length": 340,
  "benchmark_sequence_sha256": "e316590a6f1ebb768b4cd2ae53d0b5fb1deefd8c6c5ffb22c77db65f75c3048a",
  "current_entry_audit": {
    "entryVersion": 11,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-06-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 340,
  "current_source_sequence_sha256": "e316590a6f1ebb768b4cd2ae53d0b5fb1deefd8c6c5ffb22c77db65f75c3048a",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 10,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A455ZLR3",
  "selected_historical_entry_version": 10,
  "selected_historical_record_sha256": "ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d",
  "selected_historical_source_sequence_length": 340,
  "selected_historical_source_sequence_sha256": "e316590a6f1ebb768b4cd2ae53d0b5fb1deefd8c6c5ffb22c77db65f75c3048a",
  "selected_historical_version": {
    "accession": "A0A455ZLR3",
    "database": "Swiss-Prot",
    "entryVersion": 10,
    "firstRelease": "2025_02/2025_02",
    "firstReleaseDate": "23-Apr-2025",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PPZF_METMF",
    "sequenceVersion": 1
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.
- Ontology names and EXACT synonyms match options mechanically; no answer-support judgment is made.
- Only is_a and part_of edges are used in supplied graph paths; all qualifiers and obsolete/replaced_by tags remain in literal source blocks.
- The ontology is newer than the benchmark repository commit; the exact author ontology snapshot is unknown.
- No matching term or path does not establish that an option is false.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A455ZLR3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:25:16.946847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":11,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-06-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:25:16.946847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Clavicipitaceae\",\"Metarhizium\",\"Metarhizium majus\"],\"scientificName\":\"Metarhizium majus (strain ARSEF 297)\",\"taxonId\":1276143}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:25:16.946847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Pyrrolopyrazine biosynthesis cluster protein F\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"2.8.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30452111\",\"source\":\"PubMed\"}],\"value\":\"Sulfotransferase ppzF\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:25:16.946847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q4H424\",\"source\":\"UniProtKB\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"30452111\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38578094\",\"source\":\"PubMed\"}],\"value\":\"Sulfotransferase; part of the gene cluster that mediates the biosynthesis of pyrrolopyrazines, secondary metabolites showing insecticidal activity (PubMed:30452111, PubMed:38578094). The role of ppzF within the pathway has still to be determined (PubMed:38578094). The single multifunctional NRPS ppzA is sufficient to produce peramine via condensation of 1-pyrroline-5-carboxylate and arginine, N-methylation of the alpha-amino group of arginine and reduction of the thioester and the cyclization to form an iminium ion resulting in release from the peptide synthetase. Deprotonation of this intermediate and oxidation of the pyrroline ring would give rise to peramine (By similarity). In Epichloe species that produce only peramine, the peramine synthetase gene is not localized in a gene cluster, in contrast to Metarhizium species that contain additional pyrrolopyrazine biosynthesis genes. The 2-oxoglutarate-Fe(II) type oxidoreductase ppzC hydroxylates peramine to yield the newly identified compound 8-hydroxyperamine whereas ppzD converts L-proline into trans-4-hydroxy-L-proline, a precursor of peramine biosynthesis (PubMed:38578094)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:25:16.946847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Berry D.\",\"Mace W.\",\"Rehner S.A.\",\"Grage K.\",\"Dijkwel P.P.\",\"Young C.A.\",\"Scott B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30452111\"},{\"database\":\"DOI\",\"id\":\"10.1111/1462-2920.14483\"}],\"citationType\":\"journal article\",\"firstPage\":\"928\",\"id\":\"30452111\",\"journal\":\"Environ. Microbiol.\",\"lastPage\":\"939\",\"publicationDate\":\"2019\",\"title\":\"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\",\"volume\":\"21\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ARSEF 297\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:25:16.946847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Rothchild K.W.\",\"Hagar M.\",\"Berry D.\",\"Ryan K.S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38578094\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.4c01419\"}],\"citationType\":\"journal article\",\"firstPage\":\"10263\",\"id\":\"38578094\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"10267\",\"publicationDate\":\"2024\",\"title\":\"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\",\"volume\":\"146\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:25:16.946847+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "4f03679da2666fc918baa51a3273afd0d45dc9c660388a0fe8eed237cb3a398d",
  "url": "https://rest.uniprot.org/uniprotkb/A0A455ZLR3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H1",
  "excerpt": "ID   PPZF_METMF              Reviewed;         340 AA.\nAC   A0A455ZLR3;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-JUN-2019, sequence version 1.\nDT   09-APR-2025, entry version 10.\nDE   RecName: Full=Sulfotransferase ppzF {ECO:0000303|PubMed:30452111};\nDE            EC=2.8.2.- {ECO:0000305|PubMed:30452111};\nDE   AltName: Full=Pyrrolopyrazine biosynthesis cluster protein F {ECO:0000303|PubMed:30452111};\nGN   Name=ppzF {ECO:0000303|PubMed:30452111};\nOS   Metarhizium majus (strain ARSEF 297).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Clavicipitaceae; Metarhizium;\nOC   Metarhizium majus.\nOX   NCBI_TaxID=1276143;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:19.015576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=ARSEF 297;\nRX   PubMed=30452111; DOI=10.1111/1462-2920.14483;\nRA   Berry D., Mace W., Rehner S.A., Grage K., Dijkwel P.P., Young C.A.,\nRA   Scott B.;\nRT   \"Orthologous peramine and pyrrolopyrazine-producing biosynthetic gene\nRT   clusters in Metarhizium rileyi, Metarhizium majus and Cladonia grayi.\";\nRL   Environ. Microbiol. 21:928-939(2019).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:19.015576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 15-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION, AND PATHWAY.\nRX   PubMed=38578094; DOI=10.1021/jacs.4c01419;\nRA   Rothchild K.W., Hagar M., Berry D., Ryan K.S.;\nRT   \"Two Iron(II), alpha-Ketoglutarate-Dependent Enzymes Encoded by the PPZ\nRT   Gene Cluster of Metarhizium majus Enable Production of 8-Hydroxyperamine.\";\nRL   J. Am. Chem. Soc. 146:10263-10267(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:19.015576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-30",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H4",
  "excerpt": "CC   -!- FUNCTION: Sulfotransferase; part of the gene cluster that mediates the\nCC       biosynthesis of pyrrolopyrazines, secondary metabolites showing\nCC       insecticidal activity (PubMed:30452111, PubMed:38578094). The role of\nCC       ppzF within the pathway has still to be determined (PubMed:38578094).\nCC       The single multifunctional NRPS ppzA is sufficient to produce peramine\nCC       via condensation of 1-pyrroline-5-carboxylate and arginine, N-\nCC       methylation of the alpha-amino group of arginine and reduction of the\nCC       thioester and the cyclization to form an iminium ion resulting in\nCC       release from the peptide synthetase. Deprotonation of this intermediate\nCC       and oxidation of the pyrroline ring would give rise to peramine (By\nCC       similarity). In Epichloe species that produce only peramine, the\nCC       peramine synthetase gene is not localized in a gene cluster, in\nCC       contrast to Metarhizium species that contain additional pyrrolopyrazine\nCC       biosynthesis genes. The 2-oxoglutarate-Fe(II) type oxidoreductase ppzC\nCC       hydroxylates peramine to yield the newly identified compound 8-\nCC       hydroxyperamine whereas ppzD converts L-proline into trans-4-hydroxy-L-\nCC       proline, a precursor of peramine biosynthesis (PubMed:38578094).\nCC       {ECO:0000250|UniProtKB:Q4H424, ECO:0000269|PubMed:30452111,\nCC       ECO:0000269|PubMed:38578094}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:19.015576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 31-49",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10)

```json
{
  "entry_version": 10,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0016740; F:transferase activity; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:25:19.015576+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "ddc350505f9daf759d0d04d56b92ba49afb5a19348f35aee2a744b896e240a4d",
  "url": "https://rest.uniprot.org/unisave/A0A455ZLR3?format=txt&versions=10"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004347\nname: glucose-6-phosphate isomerase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: alpha-D-glucose 6-phosphate = beta-D-fructose 6-phosphate.\" [RHEA:11816]\nsynonym: \"D-glucose-6-phosphate aldose-ketose-isomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"D-glucose-6-phosphate ketol-isomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"glucose phosphate isomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"hexose monophosphate isomerase activity\" BROAD [EC:5.3.1.9]\nsynonym: \"hexose phosphate isomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"hexosephosphate isomerase activity\" BROAD [EC:5.3.1.9]\nsynonym: \"oxoisomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"phosphoglucoisomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"phosphoglucose isomerase activity\" RELATED [EC:5.3.1.9]\nsynonym: \"phosphohexoisomerase activity\" BROAD [EC:5.3.1.9]\nsynonym: \"phosphohexomutase activity\" BROAD [EC:5.3.1.9]\nsynonym: \"phosphohexose isomerase activity\" BROAD [EC:5.3.1.9]\nsynonym: \"phosphosaccharomutase activity\" BROAD [EC:5.3.1.9]\nxref: EC:5.3.1.9\nxref: MetaCyc:PGLUCISOM-RXN\nxref: Reactome:R-HSA-70471 \"GPI dimer isomerizes G6P\"\nxref: Reactome:R-HSA-70475 \"GPI dimer isomerizes Fru(6)P to G6P\"\nxref: RHEA:11816\nis_a: GO:0016861 ! intramolecular oxidoreductase activity, interconverting aldoses and ketoses\nproperty_value: skos:exactMatch EC:5.3.1.9\nproperty_value: skos:exactMatch MetaCyc:PGLUCISOM-RXN\nproperty_value: skos:exactMatch RHEA:11816\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004347",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 40334-40361",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO2

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO2",
  "excerpt": "[Term]\nid: GO:0016740\nname: transferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a group, e.g. a methyl group, glycosyl group, acyl group, phosphorus-containing, or other groups, from one compound (generally regarded as the donor) to another compound (generally regarded as the acceptor). Transferase is the systematic name for any enzyme of EC class 2.\" [EC:2.-.-.-]\nsubset: goslim_candida\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_generic\nsubset: goslim_metagenomics\nsubset: goslim_mouse\nsubset: goslim_pir\nsubset: goslim_plant\nsubset: goslim_prokaryote\nsubset: goslim_yeast\nxref: EC:2.-.-.-\nxref: Reactome:R-HSA-1483089 \"PE is converted to PS by PTDSS2\"\nxref: Reactome:R-HSA-1483186 \"PC is converted to PS by PTDSS1\"\nxref: Reactome:R-HSA-5333607 \"GSSeH combines with bGalNAc derivative to form GSSebGalNac\"\nxref: Reactome:R-HSA-5668414 \"TRAF2 ubiquitinates cIAP1,2 in cIAP1,2:TRAF1:TRAF2:TRAF3:NIK\"\nxref: Reactome:R-HSA-8868783 \"TSR3 transfers aminocarboxypropyl group from S-adenosylmethionine to N(1)-methylpseudouridine-1248 of 18SE rRNA yielding N(1)-methyl-N(3)-aminocarboxypropylpseudouridine-1248\"\nis_a: GO:0003824 ! catalytic activity\nproperty_value: skos:exactMatch EC:2.-.-.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016740",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 129652-129675",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO3

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO3",
  "excerpt": "[Term]\nid: GO:0086080\nname: protein binding involved in heterotypic cell-cell adhesion\nnamespace: molecular_function\ndef: \"Binding to a protein or protein complex contributing to the adhesion of two different types of cells.\" [GOC:BHF, GOC:mtg_cardiac_conduct_nov11]\nis_a: GO:0098632 ! cell-cell adhesion mediator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0086080",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 394815-394821",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 143. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
