# catalytic_activity_0046

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0046.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — L-aspartate + ATP = 4-phospho-L-aspartate + ADP

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSQSPTNVPRSYNSVLDLKLASPTNSASGATGGWIVQKFGGTSVGKFPENIVDNIVKVYSQTNRVAVVCSARSSQTKSEGTTSRLLRSADLAENDKDYQPLLNAIEEDHVTNAERIQSEEIKQELIKDTKQEIEHVRELLHACQIIGEISPRSLDSIMAVGEKLSCLFMTALMKDHGLNAVYINLQDVIPLSYDFQKGFDDSFYQFLSQEIGKRVLQCDKEREGEEDVIPVLTGYFGVVPGGLLNGVGRGYTDLCAALAAVALQADELQIWKEVDGIFTADPRKVPNARLLDSVTPEEAAELTYYGSEVIHPFTMEQVIRAKIPIRIKNVENPTGKGTIIYPDNIGRRGEATPPHPPAAFEQLAMSSLLQRKRSATAITAKQDIVVINIHSNKKTLSHGFLAHVFTTLDKYKLVVDLISTSEVHVSMALSIQSDQESQLKHALVDLRKMGTVDVTKKMTIVSLVGKQMVNFIGIAGNMFKVLADEKINIEMISQGANEINISAVINEKDTIRALKSIHAKLLEGGSAIGDSSAVDTRLEALKLS

[Multiple Choices]
A. 2 oxidized [4Fe-4S]-[ferredoxin] + taurine + H2O = aminoacetaldehyde + 2 reduced [4Fe-4S]-[ferredoxin] + sulfite + 3 H(+)
B. L-aspartate + ATP = 4-phospho-L-aspartate + ADP
C. (2R)-3-phosphoglycerate + ATP = (2R)-3-phospho-glyceroyl phosphate + ADP
D. 3 malonyl-CoA + acetyl-CoA + 2 S-adenosyl-L-methionine = 3,5-dimethylorsellinate + 2 S-adenosyl-L-homocysteine + 3 CO2 + 4 CoA
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

> The exact sequence matches the archived UniProt record annotated as aspartokinase, with the reaction in choice B. The annotation is explicitly based on similarity evidence from another UniProt protein (ECO:0000250), so it supports the key as a transferred annotation, not as independent experimental evidence for this exact protein.

Citations as saved: [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the aspartokinase family: a knowledgeable model can use family-level sequence homology and conserved kinase features to identify an enzyme acting in aspartate metabolism. That distinguishes the aspartate phosphorylation in B from the unrelated taurine oxidation in A and polyketide synthesis in D, and from the distinct phosphoglycerate kinase reaction in C. This is a transferable family inference, not a claim that the sequence alone proves the precise reaction experimentally.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Family recognition and homolog-based inference provide a meaningful basis for choosing B among these alternatives. The exact protein's database annotation is not necessary to make that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The options describe distinct reactions, and the aspartokinase-family inference specifically favors B.


### Important caveats

- The reviewer-only record matches the supplied sequence, but its catalytic-activity annotation is transferred by similarity rather than shown here to be experimentally measured for this exact protein.
- The original input provides no organism or protein name; the transferable inference rests on the sequence and family-level knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the aspartokinase family: a knowledgeable model can use family-level sequence homology and conserved kinase features to identify an enzyme acting in aspartate metabolism. That distinguishes the aspartate phosphorylation in B from the unrelated taurine oxidation in A and polyketide synthesis in D, and from the distinct phosphoglycerate kinase reaction in C. This is a transferable family inference, not a claim that the sequence alone proves the precise reaction experimentally.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and homolog-based inference provide a meaningful basis for choosing B among these alternatives. The exact protein's database annotation is not necessary to make that distinction."
  },
  "case_id": "catalytic_activity_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The exact sequence matches the archived UniProt record annotated as aspartokinase, with the reaction in choice B. The annotation is explicitly based on similarity evidence from another UniProt protein (ECO:0000250), so it supports the key as a transferred annotation, not as independent experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence, but its catalytic-activity annotation is transferred by similarity rather than shown here to be experimentally measured for this exact protein.",
    "The original input provides no organism or protein name; the transferable inference rests on the sequence and family-level knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the aspartokinase-family inference specifically favors B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The exact sequence matches the archived UniProt record annotated as aspartokinase, with the reaction in choice B. The annotation is explicitly based on similarity evidence from another UniProt protein (ECO:0000250), so it supports the key as a transferred annotation, not as independent experimental evidence for this exact protein.",
    "evidence_ids": ["H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the aspartokinase family: a knowledgeable model can use family-level sequence homology and conserved kinase features to identify an enzyme acting in aspartate metabolism. That distinguishes the aspartate phosphorylation in B from the unrelated taurine oxidation in A and polyketide synthesis in D, and from the distinct phosphoglycerate kinase reaction in C. This is a transferable family inference, not a claim that the sequence alone proves the precise reaction experimentally.",
    "missing_item_specific_fact": "",
    "reason": "Family recognition and homolog-based inference provide a meaningful basis for choosing B among these alternatives. The exact protein's database annotation is not necessary to make that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The options describe distinct reactions, and the aspartokinase-family inference specifically favors B."
  },
  "important_caveats": [
    "The reviewer-only record matches the supplied sequence, but its catalytic-activity annotation is transferred by similarity rather than shown here to be experimentally measured for this exact protein.",
    "The original input provides no organism or protein name; the transferable inference rests on the sequence and family-level knowledge."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation (both current entry version 41 and archived version 39) identifies this 544-aa sequence as Aspartokinase (EC 2.7.2.4) with the exact catalytic reaction 'L-aspartate + ATP = 4-phospho-L-aspartate + ADP' (RHEA:23776), matching option B verbatim. The sequence SHA256 matches the benchmark input exactly. The annotation evidence code is ECO:0000250 (inferred by similarity from P10869, the S. cerevisiae aspartokinase), so the assignment is a well-supported computational transfer rather than direct experimental characterization of this specific Candida albicans protein, but it is consistent with the sequence family and the reaction is well-established for the family.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical 'GGLLNGVGRGY' motif (a GGG/GxGxG variant) embedded in a two-domain architecture characteristic of the amino acid kinase (AAK) superfamily. This motif is a well-known, transferable sequence signature shared across amino acid kinases (aspartokinase, N-acetylglutamate kinase, glutamate 5-kinase, carbamate kinase). Among the four offered choices, only option B (aspartokinase, EC 2.7.2.4) belongs to the AAK superfamily. Option A (taurine dioxygenase) is a radical-SAM enzyme with a completely different fold; option C (phosphoglycerate kinase) is a P-loop NTPase with a distinct Rossmann-like fold and typically ~417 aa; option D (polyketide synthase) involves a large multi-domain PKS architecture. Recognizing the GGG motif and the ~544-aa two-domain AAK architecture eliminates A, C, and D, leaving B as the only AAK-family option. The specific aspartokinase assignment within the AAK family is further supported by the C-terminal domain sequence pattern (e.g., 'GKGTIIYPDNIGRRGEATPPHPPAAFEQLAMSSLLQRKRSATAITAKQDIVVINIHSNKKTLSHGFLAHVFTTLDKYKLVVDLISTSEVHVSMALSIQSDQESQLKHALVDLRKMGTVDVTKKMTIVSLVGKQMVNFIGIAGNMFKVLADEKINIEMISQGANEINISAVINEKDTIRALKSIHAKLLEGGSAIGDSSAVDTRLEALKLS') which aligns with aspartokinase-specific residues rather than NAGK or Glu5K subfamilies.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GGG motif and AAK-family architecture are well-established, transferable sequence features. A model familiar with protein families can identify the AAK superfamily from the GGG motif and then select the only AAK option among the four choices. The discrimination does not require knowing the specific UniProt accession or database entry for this exact Candida albicans protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent four structurally and mechanistically distinct enzyme families (radical-SAM, amino acid kinase, P-loop NTPase, polyketide synthase). The GGG motif uniquely identifies the AAK superfamily, and only option B belongs to that superfamily. No other option is defensible for a sequence bearing this motif.


### Important caveats

- The UniProt annotation for this protein uses evidence code ECO:0000250 (inferred by similarity from P10869), meaning the aspartokinase assignment is a computational transfer, not direct experimental characterization of this exact Candida albicans protein.
- The GGG motif is shared across the AAK superfamily; distinguishing aspartokinase from other AAK members (NAGK, Glu5K, carbamate kinase) relies on broader sequence context and domain architecture, which is consistent here but is a pattern-matching inference rather than a single-residue proof.
- The identity of the protein as Candida albicans HOM3/aspartokinase was inferred by the reviewer from dataset metadata and is not available to the evaluated model; the model must rely on sequence features alone.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical 'GGLLNGVGRGY' motif (a GGG/GxGxG variant) embedded in a two-domain architecture characteristic of the amino acid kinase (AAK) superfamily. This motif is a well-known, transferable sequence signature shared across amino acid kinases (aspartokinase, N-acetylglutamate kinase, glutamate 5-kinase, carbamate kinase). Among the four offered choices, only option B (aspartokinase, EC 2.7.2.4) belongs to the AAK superfamily. Option A (taurine dioxygenase) is a radical-SAM enzyme with a completely different fold; option C (phosphoglycerate kinase) is a P-loop NTPase with a distinct Rossmann-like fold and typically ~417 aa; option D (polyketide synthase) involves a large multi-domain PKS architecture. Recognizing the GGG motif and the ~544-aa two-domain AAK architecture eliminates A, C, and D, leaving B as the only AAK-family option. The specific aspartokinase assignment within the AAK family is further supported by the C-terminal domain sequence pattern (e.g., 'GKGTIIYPDNIGRRGEATPPHPPAAFEQLAMSSLLQRKRSATAITAKQDIVVINIHSNKKTLSHGFLAHVFTTLDKYKLVVDLISTSEVHVSMALSIQSDQESQLKHALVDLRKMGTVDVTKKMTIVSLVGKQMVNFIGIAGNMFKVLADEKINIEMISQGANEINISAVINEKDTIRALKSIHAKLLEGGSAIGDSSAVDTRLEALKLS') which aligns with aspartokinase-specific residues rather than NAGK or Glu5K subfamilies.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GGG motif and AAK-family architecture are well-established, transferable sequence features. A model familiar with protein families can identify the AAK superfamily from the GGG motif and then select the only AAK option among the four choices. The discrimination does not require knowing the specific UniProt accession or database entry for this exact Candida albicans protein."
  },
  "case_id": "catalytic_activity_0046",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation (both current entry version 41 and archived version 39) identifies this 544-aa sequence as Aspartokinase (EC 2.7.2.4) with the exact catalytic reaction 'L-aspartate + ATP = 4-phospho-L-aspartate + ADP' (RHEA:23776), matching option B verbatim. The sequence SHA256 matches the benchmark input exactly. The annotation evidence code is ECO:0000250 (inferred by similarity from P10869, the S. cerevisiae aspartokinase), so the assignment is a well-supported computational transfer rather than direct experimental characterization of this specific Candida albicans protein, but it is consistent with the sequence family and the reaction is well-established for the family."
  },
  "important_caveats": [
    "The UniProt annotation for this protein uses evidence code ECO:0000250 (inferred by similarity from P10869), meaning the aspartokinase assignment is a computational transfer, not direct experimental characterization of this exact Candida albicans protein.",
    "The GGG motif is shared across the AAK superfamily; distinguishing aspartokinase from other AAK members (NAGK, Glu5K, carbamate kinase) relies on broader sequence context and domain architecture, which is consistent here but is a pattern-matching inference rather than a single-residue proof.",
    "The identity of the protein as Candida albicans HOM3/aspartokinase was inferred by the reviewer from dataset metadata and is not available to the evaluated model; the model must rely on sequence features alone."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four structurally and mechanistically distinct enzyme families (radical-SAM, amino acid kinase, P-loop NTPase, polyketide synthase). The GGG motif uniquely identifies the AAK superfamily, and only option B belongs to that superfamily. No other option is defensible for a sequence bearing this motif."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0046",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation (both current entry version 41 and archived version 39) identifies this 544-aa sequence as Aspartokinase (EC 2.7.2.4) with the exact catalytic reaction 'L-aspartate + ATP = 4-phospho-L-aspartate + ADP' (RHEA:23776), matching option B verbatim. The sequence SHA256 matches the benchmark input exactly. The annotation evidence code is ECO:0000250 (inferred by similarity from P10869, the S. cerevisiae aspartokinase), so the assignment is a well-supported computational transfer rather than direct experimental characterization of this specific Candida albicans protein, but it is consistent with the sequence family and the reaction is well-established for the family.",
    "evidence_ids": ["C4", "C5", "H2", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical 'GGLLNGVGRGY' motif (a GGG/GxGxG variant) embedded in a two-domain architecture characteristic of the amino acid kinase (AAK) superfamily. This motif is a well-known, transferable sequence signature shared across amino acid kinases (aspartokinase, N-acetylglutamate kinase, glutamate 5-kinase, carbamate kinase). Among the four offered choices, only option B (aspartokinase, EC 2.7.2.4) belongs to the AAK superfamily. Option A (taurine dioxygenase) is a radical-SAM enzyme with a completely different fold; option C (phosphoglycerate kinase) is a P-loop NTPase with a distinct Rossmann-like fold and typically ~417 aa; option D (polyketide synthase) involves a large multi-domain PKS architecture. Recognizing the GGG motif and the ~544-aa two-domain AAK architecture eliminates A, C, and D, leaving B as the only AAK-family option. The specific aspartokinase assignment within the AAK family is further supported by the C-terminal domain sequence pattern (e.g., 'GKGTIIYPDNIGRRGEATPPHPPAAFEQLAMSSLLQRKRSATAITAKQDIVVINIHSNKKTLSHGFLAHVFTTLDKYKLVVDLISTSEVHVSMALSIQSDQESQLKHALVDLRKMGTVDVTKKMTIVSLVGKQMVNFIGIAGNMFKVLADEKINIEMISQGANEINISAVINEKDTIRALKSIHAKLLEGGSAIGDSSAVDTRLEALKLS') which aligns with aspartokinase-specific residues rather than NAGK or Glu5K subfamilies.",
    "missing_item_specific_fact": "",
    "reason": "The GGG motif and AAK-family architecture are well-established, transferable sequence features. A model familiar with protein families can identify the AAK superfamily from the GGG motif and then select the only AAK option among the four choices. The discrimination does not require knowing the specific UniProt accession or database entry for this exact Candida albicans protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent four structurally and mechanistically distinct enzyme families (radical-SAM, amino acid kinase, P-loop NTPase, polyketide synthase). The GGG motif uniquely identifies the AAK superfamily, and only option B belongs to that superfamily. No other option is defensible for a sequence bearing this motif."
  },
  "important_caveats": [
    "The UniProt annotation for this protein uses evidence code ECO:0000250 (inferred by similarity from P10869), meaning the aspartokinase assignment is a computational transfer, not direct experimental characterization of this exact Candida albicans protein.",
    "The GGG motif is shared across the AAK superfamily; distinguishing aspartokinase from other AAK members (NAGK, Glu5K, carbamate kinase) relies on broader sequence context and domain architecture, which is consistent here but is a pattern-matching inference rather than a single-residue proof.",
    "The identity of the protein as Candida albicans HOM3/aspartokinase was inferred by the reviewer from dataset metadata and is not available to the evaluated model; the model must rely on sequence features alone."
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
  "benchmark_sequence_length": 544,
  "benchmark_sequence_sha256": "a70e31c973f256dd8bc7aaccfa7ecf4ba1619ab22a51f5845f097e63766efe67",
  "current_entry_audit": {
    "entryVersion": 41,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2017-01-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 544,
  "current_source_sequence_sha256": "a70e31c973f256dd8bc7aaccfa7ecf4ba1619ab22a51f5845f097e63766efe67",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 39,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A1D8PMB8",
  "selected_historical_entry_version": 39,
  "selected_historical_record_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "selected_historical_source_sequence_length": 544,
  "selected_historical_source_sequence_sha256": "a70e31c973f256dd8bc7aaccfa7ecf4ba1619ab22a51f5845f097e63766efe67",
  "selected_historical_version": {
    "accession": "A0A1D8PMB8",
    "database": "Swiss-Prot",
    "entryVersion": 39,
    "firstRelease": "2025_03/2025_03",
    "firstReleaseDate": "18-Jun-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AK_CANAL",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1D8PMB8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":41,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2017-01-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Yeast\",\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000000559\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Saccharomycotina\",\"Pichiomycetes\",\"Debaryomycetaceae\",\"Candida/Lodderomyces clade\",\"Candida\"],\"scientificName\":\"Candida albicans (strain SC5314 / ATCC MYA-2876)\",\"taxonId\":237561}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"value\":\"2.7.2.4\"}],\"fullName\":{\"value\":\"Aspartokinase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:23777\"}}],\"reaction\":{\"ecNumber\":\"2.7.2.4\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P10869\",\"source\":\"UniProtKB\"}],\"name\":\"L-aspartate + ATP = 4-phospho-L-aspartate + ADP\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:23776\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29991\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30616\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57535\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:456216\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:32.794689+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "7c688e4eaabc3e4781e5ade84edef7517de0ae1c9eaf84cba6bd0311b17eacc2",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1D8PMB8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H1",
  "excerpt": "ID   AK_CANAL                Reviewed;         544 AA.\nAC   A0A1D8PMB8;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JAN-2017, sequence version 1.\nDT   18-JUN-2025, entry version 39.\nDE   RecName: Full=Aspartokinase;\nDE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};\nGN   Name=HOM3 {ECO:0000312|CGD:CAL0000181037};\nGN   OrderedLocusNames=CAALFM_C405540WA {ECO:0000312|EMBL:AOW29286.1},\nGN   orf19.8820 {ECO:0000312|CGD:CAL0000181037};\nOS   Candida albicans (strain SC5314 / ATCC MYA-2876) (Yeast).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Saccharomycotina; Pichiomycetes;\nOC   Debaryomycetaceae; Candida/Lodderomyces clade; Candida.\nOX   NCBI_TaxID=237561 {ECO:0000312|Proteomes:UP000000559};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Aspartokinase;\nDE            EC=2.7.2.4 {ECO:0000250|UniProtKB:P10869};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39)

```json
{
  "entry_version": 39,
  "evidence_id": "H3",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-aspartate + ATP = 4-phospho-L-aspartate + ADP;\nCC         Xref=Rhea:RHEA:23776, ChEBI:CHEBI:29991, ChEBI:CHEBI:30616,\nCC         ChEBI:CHEBI:57535, ChEBI:CHEBI:456216; EC=2.7.2.4;\nCC         Evidence={ECO:0000250|UniProtKB:P10869};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:23777;\nCC         Evidence={ECO:0000250|UniProtKB:P10869};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.627360+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "25e1c2e406fb09fd648127e1e60780d1244490e7b9ae80cba023db5b2b691f93",
  "url": "https://rest.uniprot.org/unisave/A0A1D8PMB8?format=txt&versions=39"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 46. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
