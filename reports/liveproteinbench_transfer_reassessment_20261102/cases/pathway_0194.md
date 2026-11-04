# pathway_0194

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0194.txt)

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
MATSSIRSRALGLSRRARFETTRLPFIGRRYKSDETLNRISSKITQPKSQGASQAMLYATGLTEEDMSKAQVGISSVWFEGNPCNMHLNDLSGIVRDSVLRAGLVPMRFNSVGVSDGISMGTAGMRYSLQSRELIADGIETVMNAQWYDANISLPGCDKNMPGVLMAMGRTNRPSIMVYGGSIKPGCSAKGQKLDLVSAFQSYGQFITGQIDETERFDIIRNACPGKGACGGMYTANTLATAIETMGMTVPGSSSCPADDPKKLVECENIGEVVKNMLREEIKPRDVMTRQAFENAMIVVNVLGGSTNAVLHLIAIADSVGIKLTIDDFQAVSDKTPFLADLKPSGKYLMNDLYSIGGTPALLKYLLKEGLIDGSGITVTGKTMKENVASWPDFPADQDIIQPLSNPIKPSGHLQILRGSLAPGGSVGKITGKEGLRFEGTAKCYDYEDAFIESLERGEIKKGEKTVVIIRYEGPKGGPGMPEMLKPSAAIMGAGLGQDVALLTDGRFSGGSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEEKVVDLDVPTEELDARRKQWKAPPLRYQKGTLKKYCALVSDASHGCVTDGPI

[Multiple Choices]
A. Glycolipid biosynthesis
B. Amino-acid biosynthesis
C. L-threonine from L-aspartate: step 4/5. .
D. Secondary metabolite biosynthesis. .
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

> The matched UniProt record assigns this protein to amino-acid biosynthesis, specifically branched-chain amino-acid pathways. The annotation is supported by transfer from a homolog (ECO:0000250), so it is computational/homology-based rather than direct experimental evidence for this exact protein.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the conserved dihydroxy-acid dehydratase (IlvD/DHAD) family. Knowledge transferred from this enzyme family connects it to branched-chain amino-acid biosynthesis, distinguishing broad option B from glycolipid biosynthesis, the specific threonine route in C, and secondary-metabolite biosynthesis in D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level sequence inference provides a meaningful basis for selecting B without needing the exact protein's database entry. It supports the pathway category, though it does not independently establish every aspect of this protein's in vivo role.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The alternatives distinguish amino-acid biosynthesis from unrelated pathway categories; the sequence-family inference favors B.


### Important caveats

- The reviewer evidence describes the matched protein as also named an aspterric-acid biosynthesis cluster protein, but that name alone does not establish a secondary-metabolite pathway as the best answer among these choices.
- The pathway annotation is homology-transferred, not direct experimental proof for this exact protein.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the conserved dihydroxy-acid dehydratase (IlvD/DHAD) family. Knowledge transferred from this enzyme family connects it to branched-chain amino-acid biosynthesis, distinguishing broad option B from glycolipid biosynthesis, the specific threonine route in C, and secondary-metabolite biosynthesis in D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for selecting B without needing the exact protein's database entry. It supports the pathway category, though it does not independently establish every aspect of this protein's in vivo role."
  },
  "case_id": "pathway_0194",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt record assigns this protein to amino-acid biosynthesis, specifically branched-chain amino-acid pathways. The annotation is supported by transfer from a homolog (ECO:0000250), so it is computational/homology-based rather than direct experimental evidence for this exact protein."
  },
  "important_caveats": [
    "The reviewer evidence describes the matched protein as also named an aspterric-acid biosynthesis cluster protein, but that name alone does not establish a secondary-metabolite pathway as the best answer among these choices.",
    "The pathway annotation is homology-transferred, not direct experimental proof for this exact protein."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives distinguish amino-acid biosynthesis from unrelated pathway categories; the sequence-family inference favors B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0194",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt record assigns this protein to amino-acid biosynthesis, specifically branched-chain amino-acid pathways. The annotation is supported by transfer from a homolog (ECO:0000250), so it is computational/homology-based rather than direct experimental evidence for this exact protein.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the conserved dihydroxy-acid dehydratase (IlvD/DHAD) family. Knowledge transferred from this enzyme family connects it to branched-chain amino-acid biosynthesis, distinguishing broad option B from glycolipid biosynthesis, the specific threonine route in C, and secondary-metabolite biosynthesis in D.",
    "missing_item_specific_fact": "",
    "reason": "A family-level sequence inference provides a meaningful basis for selecting B without needing the exact protein's database entry. It supports the pathway category, though it does not independently establish every aspect of this protein's in vivo role."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The alternatives distinguish amino-acid biosynthesis from unrelated pathway categories; the sequence-family inference favors B."
  },
  "important_caveats": [
    "The reviewer evidence describes the matched protein as also named an aspterric-acid biosynthesis cluster protein, but that name alone does not establish a secondary-metabolite pathway as the best answer among these choices.",
    "The pathway annotation is homology-transferred, not direct experimental proof for this exact protein."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A0F7TWW9) annotates this protein as Dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) with pathway comments explicitly stating 'Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4' and 'Amino-acid biosynthesis; L-valine biosynthesis; L-valine from pyruvate: step 3/4.' The EC number 4.2.1.9 (dihydroxy-acid dehydratase) is a well-characterized enzyme in branched-chain amino acid biosynthesis. While the protein is also named 'Aspterric acid biosynthesis cluster protein D' (a secondary metabolite context), its primary enzymatic function and UniProt pathway annotations are amino-acid biosynthesis, supporting choice B.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable motifs of the dihydroxy-acid dehydratase (DHAD) family, including the conserved 'GAGLGQDVALL' and 'GSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEEK' regions characteristic of the AHAS/DHAD superfamily catalytic domain. DHAD (EC 4.2.1.9) is a textbook enzyme in branched-chain amino acid biosynthesis (valine, isoleucine, leucine), converting 2,3-dihydroxy-3-methylbutanoate to 2-keto-3-methylvalerate and 2,3-dihydroxy-3-methylpentanoate to 2-keto-3-methylisovalerate. This family knowledge allows elimination of: (A) glycolipid biosynthesis — no DHAD involvement; (C) L-threonine from L-aspartate — threonine biosynthesis proceeds via homoserine/O-phosphohomoserine, not through dihydroxy-acid intermediates; (D) secondary metabolite biosynthesis — while the protein is in a secondary metabolite cluster, its enzymatic catalytic activity is DHAD, a primary metabolic enzyme. The DHAD-to-amino-acid-biosynthesis link is well-established across bacteria, fungi, and plants.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the DHAD/AHAS family from conserved sequence motifs is standard transferable knowledge. The DHAD family's role in branched-chain amino acid biosynthesis is textbook biochemistry learned from many homologs (E. coli IlvD, yeast ILV3, Arabidopsis AHAS/DHAD). This family-level inference meaningfully distinguishes B from A, C, and D without requiring knowledge of this specific Penicillium entry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "D"
]
```

> Choice D (Secondary metabolite biosynthesis) could be argued because the protein is explicitly named 'Aspterric acid biosynthesis cluster protein D' and aspterric acid is a secondary metabolite. However, the enzymatic function (DHAD, EC 4.2.1.9) is unambiguously in amino acid biosynthesis, and UniProt pathway annotations confirm this. The question asks for the pathway in which the protein 'functions,' which most naturally refers to its enzymatic activity rather than its genomic context. B remains the stronger answer, but D is a plausible distractor for someone focusing on the cluster context rather than the catalytic mechanism.


### Important caveats

- The pathway annotations carry evidence code ECO:0000250 (inferred by similarity from Q0CPG9), not direct experimental validation of this specific protein's pathway assignment.
- The EC number assignment (4.2.1.9) is based on ECO:0000305 (inferred by sequence similarity), though the 2024 paper (PubMed:39511739) provides functional context.
- The protein's dual identity as both a DHAD enzyme (amino acid biosynthesis) and a secondary metabolite cluster component creates a minor conceptual tension, but the enzymatic function clearly places it in amino acid biosynthesis.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable motifs of the dihydroxy-acid dehydratase (DHAD) family, including the conserved 'GAGLGQDVALL' and 'GSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEEK' regions characteristic of the AHAS/DHAD superfamily catalytic domain. DHAD (EC 4.2.1.9) is a textbook enzyme in branched-chain amino acid biosynthesis (valine, isoleucine, leucine), converting 2,3-dihydroxy-3-methylbutanoate to 2-keto-3-methylvalerate and 2,3-dihydroxy-3-methylpentanoate to 2-keto-3-methylisovalerate. This family knowledge allows elimination of: (A) glycolipid biosynthesis — no DHAD involvement; (C) L-threonine from L-aspartate — threonine biosynthesis proceeds via homoserine/O-phosphohomoserine, not through dihydroxy-acid intermediates; (D) secondary metabolite biosynthesis — while the protein is in a secondary metabolite cluster, its enzymatic catalytic activity is DHAD, a primary metabolic enzyme. The DHAD-to-amino-acid-biosynthesis link is well-established across bacteria, fungi, and plants.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the DHAD/AHAS family from conserved sequence motifs is standard transferable knowledge. The DHAD family's role in branched-chain amino acid biosynthesis is textbook biochemistry learned from many homologs (E. coli IlvD, yeast ILV3, Arabidopsis AHAS/DHAD). This family-level inference meaningfully distinguishes B from A, C, and D without requiring knowledge of this specific Penicillium entry."
  },
  "case_id": "pathway_0194",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0F7TWW9) annotates this protein as Dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) with pathway comments explicitly stating 'Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4' and 'Amino-acid biosynthesis; L-valine biosynthesis; L-valine from pyruvate: step 3/4.' The EC number 4.2.1.9 (dihydroxy-acid dehydratase) is a well-characterized enzyme in branched-chain amino acid biosynthesis. While the protein is also named 'Aspterric acid biosynthesis cluster protein D' (a secondary metabolite context), its primary enzymatic function and UniProt pathway annotations are amino-acid biosynthesis, supporting choice B."
  },
  "important_caveats": [
    "The pathway annotations carry evidence code ECO:0000250 (inferred by similarity from Q0CPG9), not direct experimental validation of this specific protein's pathway assignment.",
    "The EC number assignment (4.2.1.9) is based on ECO:0000305 (inferred by sequence similarity), though the 2024 paper (PubMed:39511739) provides functional context.",
    "The protein's dual identity as both a DHAD enzyme (amino acid biosynthesis) and a secondary metabolite cluster component creates a minor conceptual tension, but the enzymatic function clearly places it in amino acid biosynthesis."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "D"
    ],
    "reason": "Choice D (Secondary metabolite biosynthesis) could be argued because the protein is explicitly named 'Aspterric acid biosynthesis cluster protein D' and aspterric acid is a secondary metabolite. However, the enzymatic function (DHAD, EC 4.2.1.9) is unambiguously in amino acid biosynthesis, and UniProt pathway annotations confirm this. The question asks for the pathway in which the protein 'functions,' which most naturally refers to its enzymatic activity rather than its genomic context. B remains the stronger answer, but D is a plausible distractor for someone focusing on the cluster context rather than the catalytic mechanism."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0194",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A0F7TWW9) annotates this protein as Dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) with pathway comments explicitly stating 'Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4' and 'Amino-acid biosynthesis; L-valine biosynthesis; L-valine from pyruvate: step 3/4.' The EC number 4.2.1.9 (dihydroxy-acid dehydratase) is a well-characterized enzyme in branched-chain amino acid biosynthesis. While the protein is also named 'Aspterric acid biosynthesis cluster protein D' (a secondary metabolite context), its primary enzymatic function and UniProt pathway annotations are amino-acid biosynthesis, supporting choice B.",
    "evidence_ids": ["C4", "C5", "C6", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable motifs of the dihydroxy-acid dehydratase (DHAD) family, including the conserved 'GAGLGQDVALL' and 'GSHGFLIGHIVPEAMEGGPIALARDGDRIVIDAEEK' regions characteristic of the AHAS/DHAD superfamily catalytic domain. DHAD (EC 4.2.1.9) is a textbook enzyme in branched-chain amino acid biosynthesis (valine, isoleucine, leucine), converting 2,3-dihydroxy-3-methylbutanoate to 2-keto-3-methylvalerate and 2,3-dihydroxy-3-methylpentanoate to 2-keto-3-methylisovalerate. This family knowledge allows elimination of: (A) glycolipid biosynthesis — no DHAD involvement; (C) L-threonine from L-aspartate — threonine biosynthesis proceeds via homoserine/O-phosphohomoserine, not through dihydroxy-acid intermediates; (D) secondary metabolite biosynthesis — while the protein is in a secondary metabolite cluster, its enzymatic catalytic activity is DHAD, a primary metabolic enzyme. The DHAD-to-amino-acid-biosynthesis link is well-established across bacteria, fungi, and plants.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the DHAD/AHAS family from conserved sequence motifs is standard transferable knowledge. The DHAD family's role in branched-chain amino acid biosynthesis is textbook biochemistry learned from many homologs (E. coli IlvD, yeast ILV3, Arabidopsis AHAS/DHAD). This family-level inference meaningfully distinguishes B from A, C, and D without requiring knowledge of this specific Penicillium entry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["D"],
    "reason": "Choice D (Secondary metabolite biosynthesis) could be argued because the protein is explicitly named 'Aspterric acid biosynthesis cluster protein D' and aspterric acid is a secondary metabolite. However, the enzymatic function (DHAD, EC 4.2.1.9) is unambiguously in amino acid biosynthesis, and UniProt pathway annotations confirm this. The question asks for the pathway in which the protein 'functions,' which most naturally refers to its enzymatic activity rather than its genomic context. B remains the stronger answer, but D is a plausible distractor for someone focusing on the cluster context rather than the catalytic mechanism."
  },
  "important_caveats": [
    "The pathway annotations carry evidence code ECO:0000250 (inferred by similarity from Q0CPG9), not direct experimental validation of this specific protein's pathway assignment.",
    "The EC number assignment (4.2.1.9) is based on ECO:0000305 (inferred by sequence similarity), though the 2024 paper (PubMed:39511739) provides functional context.",
    "The protein's dual identity as both a DHAD enzyme (amino acid biosynthesis) and a secondary metabolite cluster component creates a minor conceptual tension, but the enzymatic function clearly places it in amino acid biosynthesis."
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
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0CPG9\",\"source\":\"UniProtKB\"}],\"value\":\"Amino-acid biosynthesis; L-isoleucine biosynthesis; L-isoleucine from 2-oxobutanoate: step 3/4\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/6",
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
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0CPG9\",\"source\":\"UniProtKB\"}],\"value\":\"Amino-acid biosynthesis; L-valine biosynthesis; L-valine from pyruvate: step 3/4\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/7",
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

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30)

```json
{
  "entry_version": 30,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-isoleucine biosynthesis; L-\nCC       isoleucine from 2-oxobutanoate: step 3/4.\nCC       {ECO:0000250|UniProtKB:Q0CPG9}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-71",
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
  "excerpt": "CC   -!- PATHWAY: Amino-acid biosynthesis; L-valine biosynthesis; L-valine from\nCC       pyruvate: step 3/4. {ECO:0000250|UniProtKB:Q0CPG9}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-73",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "url": "https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 194. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
