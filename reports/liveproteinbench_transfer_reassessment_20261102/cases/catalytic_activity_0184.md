# catalytic_activity_0184

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0184.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **D** — (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MATSSIRSRALGLSRRARFETTRLPFIGRRYKSDETLNRISSKITQPKSQGASQAMLYATGLTEEDMSKAQVGISSVWFEGNPCNMHLNDLSGIVRDSVLRAGLVPMRFNSVGVSDGISMGTAGMRYSLQSRELIADGIETVMNAQWYDANISLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDETERFDIIRNACPGKGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKNMLREEIKPRDVMTRQAFENAMIVVNVLGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYSIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIQPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEEKVVDLDVPTEELDARRKQWKAPPLRYQKGTLKKYCALVSDASHGCVTDGPI

[Multiple Choices]
A. 4-methylnorajmaline + S-adenosyl-L-methionine = 4-methylajmaline + S-adenosyl-L-homocysteine + H(+)
B. okaramine C + 2 reduced [NADPH--hemoprotein reductase] + 2 O2 = okaramine A + 2 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 2 H(+)
C. (19E)-geissoschizine + reduced [NADPH--hemoprotein reductase] + O2 = rhazimal + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
D. (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O
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

> The sequence-matched UniProt entry annotates this protein as a dihydroxy-acid dehydratase and gives the exact reaction in choice D. The catalytic-activity annotation is transferred by similarity from another UniProt entry (ECO:0000250), not evidence of direct experimental characterization of this exact protein.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a large IlvD-family dihydroxy-acid dehydratase. Transferable family knowledge connects these enzymes to dehydration of dihydroxy-acid substrates into ketoacids, as in choice D. That enzyme class and reaction type distinguish D from the specialized methyltransferase and oxidative alkaloid transformations in A–C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence meaningfully selects the only offered dihydroxy-acid dehydration reaction. The exact substrate specificity is not independently established from the input alone, but that does not undermine the distinction among these choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered alternatives, only D matches the expected reaction class for a dihydroxy-acid dehydratase.


### Important caveats

- The supplied database evidence supports the key but attributes the catalytic activity by similarity; it does not establish direct experimental measurement for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a large IlvD-family dihydroxy-acid dehydratase. Transferable family knowledge connects these enzymes to dehydration of dihydroxy-acid substrates into ketoacids, as in choice D. That enzyme class and reaction type distinguish D from the specialized methyltransferase and oxidative alkaloid transformations in A–C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence meaningfully selects the only offered dihydroxy-acid dehydration reaction. The exact substrate specificity is not independently established from the input alone, but that does not undermine the distinction among these choices."
  },
  "case_id": "catalytic_activity_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein as a dihydroxy-acid dehydratase and gives the exact reaction in choice D. The catalytic-activity annotation is transferred by similarity from another UniProt entry (ECO:0000250), not evidence of direct experimental characterization of this exact protein."
  },
  "important_caveats": [
    "The supplied database evidence supports the key but attributes the catalytic activity by similarity; it does not establish direct experimental measurement for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, only D matches the expected reaction class for a dihydroxy-acid dehydratase."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this protein as a dihydroxy-acid dehydratase and gives the exact reaction in choice D. The catalytic-activity annotation is transferred by similarity from another UniProt entry (ECO:0000250), not evidence of direct experimental characterization of this exact protein.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a large IlvD-family dihydroxy-acid dehydratase. Transferable family knowledge connects these enzymes to dehydration of dihydroxy-acid substrates into ketoacids, as in choice D. That enzyme class and reaction type distinguish D from the specialized methyltransferase and oxidative alkaloid transformations in A–C.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence meaningfully selects the only offered dihydroxy-acid dehydration reaction. The exact substrate specificity is not independently established from the input alone, but that does not undermine the distinction among these choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered alternatives, only D matches the expected reaction class for a dihydroxy-acid dehydratase."
  },
  "important_caveats": [
    "The supplied database evidence supports the key but attributes the catalytic activity by similarity; it does not establish direct experimental measurement for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A0F7TWW9 (sequence matched, 596 aa) annotates this protein as Dihydroxy-acid dehydratase pbrD (EC 4.2.1.9) with the exact catalytic reaction in option D: (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O. The EC assignment carries evidence code ECO:0000305 (by similarity) and the reaction annotation uses ECO:0000250 (inferred by similarity from Q0CPG9), with a PubMed reference (39511739) supporting the protein's role in aspterric acid biosynthesis. While the reaction annotation is similarity-based rather than direct experimental kinetics, it is the standard UniProt annotation and is consistent with the DHAD enzyme family assignment.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C7](#evidence-c7), [H2](#evidence-h2), [H4](#evidence-h4), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The supplied sequence contains multiple highly conserved DHAD (dihydroxy-acid dehydratase, EC 4.2.1.9) family motifs. The region 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDA' is a hallmark of the DHAD/IRCH superfamily active-site region found across bacteria, fungi, and plants. Additional DHAD-characteristic motifs include 'GSGITVTGKTMKENVASWPDFPADQD' and 'GKITGKEG' near the C-terminus. The overall length (~596 aa) is consistent with fungal DHADs. These motifs are transferable family-level knowledge: any model trained on protein families would recognize DHAD signatures. Option D (a dehydration reaction catalyzed by EC 4.2.1.9) is the only choice consistent with DHAD motifs. Options B and C require cytochrome P450 machinery (heme-binding motifs such as FGxGxRxCxG and reductase partners), which are entirely absent. Option A requires a SAM-dependent methyltransferase fold (VxGxG or GxGxG Rossmann-like motifs), also absent. Thus family motif recognition meaningfully and uniquely selects D over the three distractors.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the DHAD protein family from conserved sequence motifs (GAGLGQ, GDRIVIDA, GKITGKE) is well-established transferable knowledge. These motifs are shared across hundreds of characterized DHAD enzymes in multiple kingdoms. The absence of P450 heme motifs and SAM-binding motifs eliminates B, C, and A. A knowledgeable model can reach D through family-level inference without recalling the specific annotation of this Penicillium protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The DHAD motifs uniquely identify option D. The other three options require entirely different enzyme classes (P450 for B/C, methyltransferase for A) with no supporting sequence features in the input. No ambiguity among the offered choices.


### Important caveats

- The UniProt EC assignment and reaction annotation carry similarity-based evidence codes (ECO:0000250, ECO:0000305), not direct experimental kinetics for this specific protein, though the protein's biological role in aspterric acid biosynthesis is supported by PubMed 39511739.
- The protein is annotated as a mitochondrial precursor (N-terminal transit peptide), which is consistent with the DHAD assignment in fungi.
- DHAD also catalyzes the isoleucine-pathway reaction (option not offered here); the valine-pathway reaction in option D is the primary/first listed activity for EC 4.2.1.9.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The supplied sequence contains multiple highly conserved DHAD (dihydroxy-acid dehydratase, EC 4.2.1.9) family motifs. The region 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDA' is a hallmark of the DHAD/IRCH superfamily active-site region found across bacteria, fungi, and plants. Additional DHAD-characteristic motifs include 'GSGITVTGKTMKENVASWPDFPADQD' and 'GKITGKEG' near the C-terminus. The overall length (~596 aa) is consistent with fungal DHADs. These motifs are transferable family-level knowledge: any model trained on protein families would recognize DHAD signatures. Option D (a dehydration reaction catalyzed by EC 4.2.1.9) is the only choice consistent with DHAD motifs. Options B and C require cytochrome P450 machinery (heme-binding motifs such as FGxGxRxCxG and reductase partners), which are entirely absent. Option A requires a SAM-dependent methyltransferase fold (VxGxG or GxGxG Rossmann-like motifs), also absent. Thus family motif recognition meaningfully and uniquely selects D over the three distractors.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the DHAD protein family from conserved sequence motifs (GAGLGQ, GDRIVIDA, GKITGKE) is well-established transferable knowledge. These motifs are shared across hundreds of characterized DHAD enzymes in multiple kingdoms. The absence of P450 heme motifs and SAM-binding motifs eliminates B, C, and A. A knowledgeable model can reach D through family-level inference without recalling the specific annotation of this Penicillium protein."
  },
  "case_id": "catalytic_activity_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C7",
      "H2",
      "H4",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F7TWW9 (sequence matched, 596 aa) annotates this protein as Dihydroxy-acid dehydratase pbrD (EC 4.2.1.9) with the exact catalytic reaction in option D: (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O. The EC assignment carries evidence code ECO:0000305 (by similarity) and the reaction annotation uses ECO:0000250 (inferred by similarity from Q0CPG9), with a PubMed reference (39511739) supporting the protein's role in aspterric acid biosynthesis. While the reaction annotation is similarity-based rather than direct experimental kinetics, it is the standard UniProt annotation and is consistent with the DHAD enzyme family assignment."
  },
  "important_caveats": [
    "The UniProt EC assignment and reaction annotation carry similarity-based evidence codes (ECO:0000250, ECO:0000305), not direct experimental kinetics for this specific protein, though the protein's biological role in aspterric acid biosynthesis is supported by PubMed 39511739.",
    "The protein is annotated as a mitochondrial precursor (N-terminal transit peptide), which is consistent with the DHAD assignment in fungi.",
    "DHAD also catalyzes the isoleucine-pathway reaction (option not offered here); the valine-pathway reaction in option D is the primary/first listed activity for EC 4.2.1.9."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The DHAD motifs uniquely identify option D. The other three options require entirely different enzyme classes (P450 for B/C, methyltransferase for A) with no supporting sequence features in the input. No ambiguity among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A0F7TWW9 (sequence matched, 596 aa) annotates this protein as Dihydroxy-acid dehydratase pbrD (EC 4.2.1.9) with the exact catalytic reaction in option D: (2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O. The EC assignment carries evidence code ECO:0000305 (by similarity) and the reaction annotation uses ECO:0000250 (inferred by similarity from Q0CPG9), with a PubMed reference (39511739) supporting the protein's role in aspterric acid biosynthesis. While the reaction annotation is similarity-based rather than direct experimental kinetics, it is the standard UniProt annotation and is consistent with the DHAD enzyme family assignment.",
    "evidence_ids": ["C4", "C5", "C7", "H2", "H4", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The supplied sequence contains multiple highly conserved DHAD (dihydroxy-acid dehydratase, EC 4.2.1.9) family motifs. The region 'GAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDA' is a hallmark of the DHAD/IRCH superfamily active-site region found across bacteria, fungi, and plants. Additional DHAD-characteristic motifs include 'GSGITVTGKTMKENVASWPDFPADQD' and 'GKITGKEG' near the C-terminus. The overall length (~596 aa) is consistent with fungal DHADs. These motifs are transferable family-level knowledge: any model trained on protein families would recognize DHAD signatures. Option D (a dehydration reaction catalyzed by EC 4.2.1.9) is the only choice consistent with DHAD motifs. Options B and C require cytochrome P450 machinery (heme-binding motifs such as FGxGxRxCxG and reductase partners), which are entirely absent. Option A requires a SAM-dependent methyltransferase fold (VxGxG or GxGxG Rossmann-like motifs), also absent. Thus family motif recognition meaningfully and uniquely selects D over the three distractors.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the DHAD protein family from conserved sequence motifs (GAGLGQ, GDRIVIDA, GKITGKE) is well-established transferable knowledge. These motifs are shared across hundreds of characterized DHAD enzymes in multiple kingdoms. The absence of P450 heme motifs and SAM-binding motifs eliminates B, C, and A. A knowledgeable model can reach D through family-level inference without recalling the specific annotation of this Penicillium protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The DHAD motifs uniquely identify option D. The other three options require entirely different enzyme classes (P450 for B/C, methyltransferase for A) with no supporting sequence features in the input. No ambiguity among the offered choices."
  },
  "important_caveats": [
    "The UniProt EC assignment and reaction annotation carry similarity-based evidence codes (ECO:0000250, ECO:0000305), not direct experimental kinetics for this specific protein, though the protein's biological role in aspterric acid biosynthesis is supported by PubMed 39511739.",
    "The protein is annotated as a mitochondrial precursor (N-terminal transit peptide), which is consistent with the DHAD assignment in fungi.",
    "DHAD also catalyzes the isoleucine-pathway reaction (option not offered here); the valine-pathway reaction in option D is the primary/first listed activity for EC 4.2.1.9."
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
  "benchmark_sequence_length": 596,
  "benchmark_sequence_sha256": "c113b75f8644468658289da5480b81ecf252c20df4f27a6efbd96538aea1668e",
  "current_entry_audit": {
    "entryVersion": 31,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-04-09",
    "sequenceVersion": 2
  },
  "current_record_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 596,
  "current_source_sequence_sha256": "c113b75f8644468658289da5480b81ecf252c20df4f27a6efbd96538aea1668e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 30,
      "exact_sequence_comparison": "matched",
      "sequence_version": 2
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0F7TWW9",
  "selected_historical_entry_version": 30,
  "selected_historical_record_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "selected_historical_source_sequence_length": 596,
  "selected_historical_source_sequence_sha256": "c113b75f8644468658289da5480b81ecf252c20df4f27a6efbd96538aea1668e",
  "selected_historical_version": {
    "accession": "A0A0F7TWW9",
    "database": "Swiss-Prot",
    "entryVersion": 30,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_02/2026_02",
    "lastReleaseDate": "10-Jun-2026",
    "name": "PBRD_PENBI",
    "sequenceVersion": 2
  }
}
```

**Qualifications:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0F7TWW9\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":31,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-04-09\",\"sequenceVersion\":2}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Eurotiomycetes\",\"Eurotiomycetidae\",\"Eurotiales\",\"Aspergillaceae\",\"Penicillium\"],\"scientificName\":\"Penicillium brasilianum\",\"taxonId\":104259}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39511739\",\"source\":\"PubMed\"}],\"value\":\"Aspterric acid biosynthesis cluster protein D\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"39511739\",\"source\":\"PubMed\"}],\"value\":\"4.2.1.9\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39511739\",\"source\":\"PubMed\"}],\"value\":\"Dihydroxy-acid dehydratase pbrD, mitochondrial\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39511739\",\"source\":\"PubMed\"}],\"value\":\"DHAD astD\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0CPG9\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:24810\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0CPG9\",\"source\":\"UniProtKB\"}],\"name\":\"(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:24809\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:11851\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49072\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:27695\"}}],\"reaction\":{\"ecNumber\":\"4.2.1.9\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05791\",\"source\":\"UniProtKB\"}],\"name\":\"(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:27694\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:35146\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:49258\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Zhou Z.\",\"Zhang Y.\",\"Wu Q.\",\"Hou X.\",\"Zhang B.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39511739\"},{\"database\":\"DOI\",\"id\":\"10.1021/acs.jafc.4c08468\"}],\"citationType\":\"journal article\",\"firstPage\":\"25755\",\"id\":\"39511739\",\"journal\":\"J. Agric. Food Chem.\",\"lastPage\":\"25766\",\"publicationDate\":\"2024\",\"title\":\"Yeast synthesis and herbicidal activity evaluation of aspterric acid.\",\"volume\":\"72\"},\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-02T04:24:01.826200+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9c9db7d008b685b5073a404f2df8618925830622276ec1c773349e5fd3829400",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0F7TWW9.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H1",
  "excerpt": "ID   PBRD_PENBI              Reviewed;         596 AA.\nAC   A0A0F7TWW9;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   09-APR-2025, sequence version 2.\nDT   28-JAN-2026, entry version 30.\nDE   RecName: Full=Dihydroxy-acid dehydratase pbrD, mitochondrial {ECO:0000303|PubMed:39511739};\nDE            Short=DHAD astD {ECO:0000303|PubMed:39511739};\nDE            EC=4.2.1.9 {ECO:0000305|PubMed:39511739};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:39511739};\nDE   Flags: Precursor;\nGN   Name=pbrD {ECO:0000303|PubMed:39511739}; ORFNames=PMG11_09713;\nOS   Penicillium brasilianum.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Eurotiomycetes;\nOC   Eurotiomycetidae; Eurotiales; Aspergillaceae; Penicillium.\nOX   NCBI_TaxID=104259;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "url": "https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Dihydroxy-acid dehydratase pbrD, mitochondrial {ECO:0000303|PubMed:39511739};\nDE            Short=DHAD astD {ECO:0000303|PubMed:39511739};\nDE            EC=4.2.1.9 {ECO:0000305|PubMed:39511739};\nDE   AltName: Full=Aspterric acid biosynthesis cluster protein D {ECO:0000303|PubMed:39511739};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-10",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "url": "https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H3",
  "excerpt": "RN   [2]\nRP   FUNCTION.\nRX   PubMed=39511739; DOI=10.1021/acs.jafc.4c08468;\nRA   Zhou Z., Zhang Y., Wu Q., Hou X., Zhang B.;\nRT   \"Yeast synthesis and herbicidal activity evaluation of aspterric acid.\";\nRL   J. Agric. Food Chem. 72:25755-25766(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-29",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "url": "https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R)-2,3-dihydroxy-3-methylbutanoate = 3-methyl-2-oxobutanoate\nCC         + H2O; Xref=Rhea:RHEA:24809, ChEBI:CHEBI:11851, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:49072; EC=4.2.1.9;\nCC         Evidence={ECO:0000250|UniProtKB:Q0CPG9};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:24810;\nCC         Evidence={ECO:0000250|UniProtKB:Q0CPG9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-50",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "url": "https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=(2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-\nCC         oxopentanoate + H2O; Xref=Rhea:RHEA:27694, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:35146, ChEBI:CHEBI:49258; EC=4.2.1.9;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:27695;\nCC         Evidence={ECO:0000250|UniProtKB:P05791};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 51-57",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "url": "https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 184. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
