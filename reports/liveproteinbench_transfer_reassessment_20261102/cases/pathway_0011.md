# pathway_0011

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0011.txt)

**Task:** `pathway`  
**Expected answer:** **B** — Amino-acid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MEVNQKWNWDTKPILVKCGGFSSQLAKNVTEKVDGDPLWGSRFDATNPEAVIQTHLDFLRNGADIILTNTYQSSVEGFVKYLGVTRERGVELIQKSVQLAKQAKEQYLSEIGSEAESALPLIMGSIGPYGAYLHDGSEYTGNYADKMSKEELRAWHKTRIEICLAAGVDGLALETLPCLMEAEAVTELVLDNFPDAKFWVSLQCMDEKHMASGENFAEAALSLWRLVQSRKAENRLLGIGLNCVNPLFVTPLLSSLTKVAGSDRIPLVVYSNRGEIYDVEQGDWTGTGEEVVKFVPEWIQLGVRIVGGCCRVYPTDVLAIRKYVDGLNIKP

[Multiple Choices]
A. coenzyme A biosynthesis
B. Amino-acid biosynthesis
C. 7,8-dihydrofolate from 2-amino-4-hydroxy-6-hydroxymethyl-7,8-dihydropteridine diphosphate and 4-aminobenzoate: step 1/2. .
D. L-threonine from L-aspartate: step 1/5. .
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

> The sequence-matched record annotates the protein as betaine-homocysteine S-methyltransferase and places it in de novo L-methionine biosynthesis, supporting the broader option “Amino-acid biosynthesis.” The pathway annotation is transferred by similarity, not evidence of direct experimental validation in this protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble betaine-homocysteine methyltransferase-family enzyme. Transferable knowledge of this enzyme family links methyl transfer from betaine to homocysteine with methionine production, an amino-acid biosynthesis route. That distinguishes B from coenzyme A biosynthesis, folate synthesis, and the specific threonine-from-aspartate step in D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family-level sequence recognition and the known reaction of related enzymes provide a meaningful basis for selecting the broad methionine/amino-acid pathway option; the exact target annotation is not needed to distinguish these alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The inferred methionine-biosynthesis function fits B; none of the other options describes that pathway.


### Important caveats

- The reviewer-only pathway annotation is supported by evidence transferred from a related protein, so it should not be presented as direct experimental evidence for this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble betaine-homocysteine methyltransferase-family enzyme. Transferable knowledge of this enzyme family links methyl transfer from betaine to homocysteine with methionine production, an amino-acid biosynthesis route. That distinguishes B from coenzyme A biosynthesis, folate synthesis, and the specific threonine-from-aspartate step in D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the known reaction of related enzymes provide a meaningful basis for selecting the broad methionine/amino-acid pathway option; the exact target annotation is not needed to distinguish these alternatives."
  },
  "case_id": "pathway_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record annotates the protein as betaine-homocysteine S-methyltransferase and places it in de novo L-methionine biosynthesis, supporting the broader option “Amino-acid biosynthesis.” The pathway annotation is transferred by similarity, not evidence of direct experimental validation in this protein."
  },
  "important_caveats": [
    "The reviewer-only pathway annotation is supported by evidence transferred from a related protein, so it should not be presented as direct experimental evidence for this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The inferred methionine-biosynthesis function fits B; none of the other options describes that pathway."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record annotates the protein as betaine-homocysteine S-methyltransferase and places it in de novo L-methionine biosynthesis, supporting the broader option “Amino-acid biosynthesis.” The pathway annotation is transferred by similarity, not evidence of direct experimental validation in this protein.",
    "evidence_ids": ["C4", "C5", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble betaine-homocysteine methyltransferase-family enzyme. Transferable knowledge of this enzyme family links methyl transfer from betaine to homocysteine with methionine production, an amino-acid biosynthesis route. That distinguishes B from coenzyme A biosynthesis, folate synthesis, and the specific threonine-from-aspartate step in D.",
    "missing_item_specific_fact": "",
    "reason": "Family-level sequence recognition and the known reaction of related enzymes provide a meaningful basis for selecting the broad methionine/amino-acid pathway option; the exact target annotation is not needed to distinguish these alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The inferred methionine-biosynthesis function fits B; none of the other options describes that pathway."
  },
  "important_caveats": [
    "The reviewer-only pathway annotation is supported by evidence transferred from a related protein, so it should not be presented as direct experimental evidence for this sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for Q9VJ31 (sequence matched) explicitly assigns the pathway 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway' (evidence C5, H2). The protein is annotated as Betaine-homocysteine S-methyltransferase (EC 2.1.1.5), a methyltransferase that converts homocysteine + betaine to methionine + dimethylglycine. This falls squarely under 'Amino-acid biosynthesis' as stated in choice B. The annotation evidence code is ECO:0000250 (similarity to Q93088, human BHMT), so it is a computational inference by homology rather than direct experimental evidence, but it is consistent and well-supported.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H1](#evidence-h1), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains multiple hallmark motifs of Class I SAM-dependent methyltransferases: a glycine-rich nucleotide-binding loop 'GIGPYGAY' (residues ~105-112), a second glycine-rich motif 'GGCCRVY' (~residues 305-311), and 'GIGLNCVN' (~residues 260-267). These are widely conserved across hundreds of characterized SAM-dependent methyltransferases and are readily recognizable to any model trained on protein sequence families. Among the four choices: (C) dihydropteroate synthase has a TIM-barrel fold with no methyltransferase motifs; (D) aspartate kinase is a kinase with P-loop and catalytic-lysine features, not methyltransferase motifs; (A) CoA biosynthesis involves pantothenate kinases, PPC synthetases/decarboxylases, and CoA synthetase—none are methyltransferases. Only (B) amino-acid biosynthesis (specifically methionine metabolism) routinely employs SAM-dependent methyltransferases (e.g., BHMT, methionine synthase). Thus, recognizing the methyltransferase fold and knowing which of the four listed pathways uses methyltransferases is sufficient to select B without knowing this specific protein's record.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The Class I methyltransferase motifs (GIGPYGAY, GGCCRVY, GIGLNCVN) are well-known sequence signatures shared across a large family of SAM-dependent methyltransferases. General biochemistry knowledge establishes that among the four offered pathways, only amino-acid (methionine) biosynthesis involves methyltransferases; the other three involve kinases, synthetases, or TIM-barrel enzymes. This provides a concrete, transferable inference that meaningfully distinguishes B from A, C, and D.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices describe mechanistically distinct enzyme classes (methyltransferase pathway, CoA-biosynthetic kinases/synthetases, TIM-barrel DHPS, aspartate kinase). The methyltransferase motifs in the sequence uniquely point to B. No other option is defensible given the fold recognition.


### Important caveats

- The UniProt pathway annotation carries evidence code ECO:0000250 (similarity to Q93088), meaning it is inferred by homology rather than direct experimental assay in Drosophila.
- BHMT is sometimes described as part of methionine 'recycling' or 'metabolism' rather than strictly 'de novo biosynthesis,' but the UniProt annotation explicitly places it under 'L-methionine biosynthesis via de novo pathway,' and among the given choices B is the only fitting category.
- The reviewer-only evidence identifies the protein as Q9VJ31 (BHMT_DROME); this accession was not provided to the evaluated model and does not affect the transferable-motif reasoning.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains multiple hallmark motifs of Class I SAM-dependent methyltransferases: a glycine-rich nucleotide-binding loop 'GIGPYGAY' (residues ~105-112), a second glycine-rich motif 'GGCCRVY' (~residues 305-311), and 'GIGLNCVN' (~residues 260-267). These are widely conserved across hundreds of characterized SAM-dependent methyltransferases and are readily recognizable to any model trained on protein sequence families. Among the four choices: (C) dihydropteroate synthase has a TIM-barrel fold with no methyltransferase motifs; (D) aspartate kinase is a kinase with P-loop and catalytic-lysine features, not methyltransferase motifs; (A) CoA biosynthesis involves pantothenate kinases, PPC synthetases/decarboxylases, and CoA synthetase—none are methyltransferases. Only (B) amino-acid biosynthesis (specifically methionine metabolism) routinely employs SAM-dependent methyltransferases (e.g., BHMT, methionine synthase). Thus, recognizing the methyltransferase fold and knowing which of the four listed pathways uses methyltransferases is sufficient to select B without knowing this specific protein's record.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The Class I methyltransferase motifs (GIGPYGAY, GGCCRVY, GIGLNCVN) are well-known sequence signatures shared across a large family of SAM-dependent methyltransferases. General biochemistry knowledge establishes that among the four offered pathways, only amino-acid (methionine) biosynthesis involves methyltransferases; the other three involve kinases, synthetases, or TIM-barrel enzymes. This provides a concrete, transferable inference that meaningfully distinguishes B from A, C, and D."
  },
  "case_id": "pathway_0011",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H1",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for Q9VJ31 (sequence matched) explicitly assigns the pathway 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway' (evidence C5, H2). The protein is annotated as Betaine-homocysteine S-methyltransferase (EC 2.1.1.5), a methyltransferase that converts homocysteine + betaine to methionine + dimethylglycine. This falls squarely under 'Amino-acid biosynthesis' as stated in choice B. The annotation evidence code is ECO:0000250 (similarity to Q93088, human BHMT), so it is a computational inference by homology rather than direct experimental evidence, but it is consistent and well-supported."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000250 (similarity to Q93088), meaning it is inferred by homology rather than direct experimental assay in Drosophila.",
    "BHMT is sometimes described as part of methionine 'recycling' or 'metabolism' rather than strictly 'de novo biosynthesis,' but the UniProt annotation explicitly places it under 'L-methionine biosynthesis via de novo pathway,' and among the given choices B is the only fitting category.",
    "The reviewer-only evidence identifies the protein as Q9VJ31 (BHMT_DROME); this accession was not provided to the evaluated model and does not affect the transferable-motif reasoning."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe mechanistically distinct enzyme classes (methyltransferase pathway, CoA-biosynthetic kinases/synthetases, TIM-barrel DHPS, aspartate kinase). The methyltransferase motifs in the sequence uniquely point to B. No other option is defensible given the fold recognition."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0011",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for Q9VJ31 (sequence matched) explicitly assigns the pathway 'Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway' (evidence C5, H2). The protein is annotated as Betaine-homocysteine S-methyltransferase (EC 2.1.1.5), a methyltransferase that converts homocysteine + betaine to methionine + dimethylglycine. This falls squarely under 'Amino-acid biosynthesis' as stated in choice B. The annotation evidence code is ECO:0000250 (similarity to Q93088, human BHMT), so it is a computational inference by homology rather than direct experimental evidence, but it is consistent and well-supported.",
    "evidence_ids": ["C4", "C5", "H1", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains multiple hallmark motifs of Class I SAM-dependent methyltransferases: a glycine-rich nucleotide-binding loop 'GIGPYGAY' (residues ~105-112), a second glycine-rich motif 'GGCCRVY' (~residues 305-311), and 'GIGLNCVN' (~residues 260-267). These are widely conserved across hundreds of characterized SAM-dependent methyltransferases and are readily recognizable to any model trained on protein sequence families. Among the four choices: (C) dihydropteroate synthase has a TIM-barrel fold with no methyltransferase motifs; (D) aspartate kinase is a kinase with P-loop and catalytic-lysine features, not methyltransferase motifs; (A) CoA biosynthesis involves pantothenate kinases, PPC synthetases/decarboxylases, and CoA synthetase—none are methyltransferases. Only (B) amino-acid biosynthesis (specifically methionine metabolism) routinely employs SAM-dependent methyltransferases (e.g., BHMT, methionine synthase). Thus, recognizing the methyltransferase fold and knowing which of the four listed pathways uses methyltransferases is sufficient to select B without knowing this specific protein's record.",
    "missing_item_specific_fact": "",
    "reason": "The Class I methyltransferase motifs (GIGPYGAY, GGCCRVY, GIGLNCVN) are well-known sequence signatures shared across a large family of SAM-dependent methyltransferases. General biochemistry knowledge establishes that among the four offered pathways, only amino-acid (methionine) biosynthesis involves methyltransferases; the other three involve kinases, synthetases, or TIM-barrel enzymes. This provides a concrete, transferable inference that meaningfully distinguishes B from A, C, and D."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe mechanistically distinct enzyme classes (methyltransferase pathway, CoA-biosynthetic kinases/synthetases, TIM-barrel DHPS, aspartate kinase). The methyltransferase motifs in the sequence uniquely point to B. No other option is defensible given the fold recognition."
  },
  "important_caveats": [
    "The UniProt pathway annotation carries evidence code ECO:0000250 (similarity to Q93088), meaning it is inferred by homology rather than direct experimental assay in Drosophila.",
    "BHMT is sometimes described as part of methionine 'recycling' or 'metabolism' rather than strictly 'de novo biosynthesis,' but the UniProt annotation explicitly places it under 'L-methionine biosynthesis via de novo pathway,' and among the given choices B is the only fitting category.",
    "The reviewer-only evidence identifies the protein as Q9VJ31 (BHMT_DROME); this accession was not provided to the evaluated model and does not affect the transferable-motif reasoning."
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
  "benchmark_sequence_length": 331,
  "benchmark_sequence_sha256": "6bd107edc9e34f66f2c22eae9672febecece9154557d102db3fa92c074ab48db",
  "current_entry_audit": {
    "entryVersion": 181,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2000-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 331,
  "current_source_sequence_sha256": "6bd107edc9e34f66f2c22eae9672febecece9154557d102db3fa92c074ab48db",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 179,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q9VJ31",
  "selected_historical_entry_version": 179,
  "selected_historical_record_sha256": "0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62",
  "selected_historical_source_sequence_length": 331,
  "selected_historical_source_sequence_sha256": "6bd107edc9e34f66f2c22eae9672febecece9154557d102db3fa92c074ab48db",
  "selected_historical_version": {
    "accession": "Q9VJ31",
    "database": "Swiss-Prot",
    "entryVersion": 179,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BHMT_DROME",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q9VJ31\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":181,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2000-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Fruit fly\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000803\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Metazoa\",\"Ecdysozoa\",\"Arthropoda\",\"Altocrustacea\",\"Allotriocarida\",\"Hexapoda\",\"Insecta\",\"Pterygota\",\"Neoptera\",\"Eumetabola\",\"Endopterygota\",\"Aparaglossata\",\"Panorpida\",\"Diptera\",\"Brachycera\",\"Muscomorpha\",\"Ephydroidea\",\"Drosophilidae\",\"Drosophila\",\"Sophophora\"],\"scientificName\":\"Drosophila melanogaster\",\"taxonId\":7227}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q93088\",\"source\":\"UniProtKB\"}],\"value\":\"2.1.1.5\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"FBgn0032727\",\"source\":\"FlyBase\"}],\"value\":\"Betaine-homocysteine S-methyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q9VJ31.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q93088\",\"source\":\"UniProtKB\"}],\"value\":\"Amino-acid biosynthesis; L-methionine biosynthesis via de novo pathway\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:33:22.549548+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d9e7ae75552fc6f8c0b82b0818c27c06ccc38e4edbafe213c0d1073bb6cc0f26",
  "url": "https://rest.uniprot.org/uniprotkb/Q9VJ31.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179)

```json
{
  "entry_version": 179,
  "evidence_id": "H1",
  "excerpt": "ID   BHMT_DROME              Reviewed;         331 AA.\nAC   Q9VJ31;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-2000, sequence version 1.\nDT   28-JAN-2026, entry version 179.\nDE   RecName: Full=Betaine-homocysteine S-methyltransferase {ECO:0000312|FlyBase:FBgn0032727};\nDE            EC=2.1.1.5 {ECO:0000250|UniProtKB:Q93088};\nGN   Name=Bhmt {ECO:0000312|FlyBase:FBgn0032727};\nGN   ORFNames=CG10623 {ECO:0000312|FlyBase:FBgn0032727};\nOS   Drosophila melanogaster (Fruit fly).\nOC   Eukaryota; Metazoa; Ecdysozoa; Arthropoda; Hexapoda; Insecta; Pterygota;\nOC   Neoptera; Endopterygota; Diptera; Brachycera; Muscomorpha; Ephydroidea;\nOC   Drosophilidae; Drosophila; Sophophora.\nOX   NCBI_TaxID=7227 {ECO:0000312|Proteomes:UP000000803};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:24.773902+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62",
  "url": "https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179)

```json
{
  "entry_version": 179,
  "evidence_id": "H2",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-methionine biosynthesis via de novo\nCC       pathway. {ECO:0000250|UniProtKB:Q93088}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:33:24.773902+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 119-120",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "0137a301084f29c9ad250967ed17fe809b86d9f9bf9482cf841c048eb041de62",
  "url": "https://rest.uniprot.org/unisave/Q9VJ31?format=txt&versions=179"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 11. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
