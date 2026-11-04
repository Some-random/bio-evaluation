# pathway_0112

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0112.txt)

**Task:** `pathway`  
**Expected answer:** **A** — Secondary metabolite biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MKSPLKLYFLPYISPGHMIPLSEMARLFANQGHHVTIITTTSNATLLQKYTTATLSLHLIPLPTKEAGLPDGLENFISVNDLETAGKLYYALSLLQPVIEEFITSNPPDCIVSDMFYPWTADLASQLQVPRMVFHAACIFAMCMKESMRGPDAPHLKVSSDYELFEVKGLPDPVFMTRAQLPDYVRTPNGYTQLMEMWREAEKKSYGVMVNNFYELDPAYTEHYSKIMGHKVWNIGPAAQILHRGSGDKIERVHKAVVGENQCLSWLDTKEPNSVFYVCFGSAIRFPDDQLYEIASALESSGAQFIWAVLGKDSDNSDSNSDSEWLPAGFEEKMKETGRGMIIRGWAPQVLILDHPSVGGFMTHCGWNSTIEGVSAGVGMVTWPLYAEQFYNEKLITQVLKIGVEAGVEEWNLWVDVGRKLVKREKIEAAIRAVMGEAGVEMRRKAKELSVKAKKAVQDGGSSHRNLMALIEDLQRIRDDKMSKVAN

[Multiple Choices]
A. Secondary metabolite biosynthesis
B. Pyrimidine metabolism
C. protein glycosylation. .
D. LPS O-antigen biosynthesis. .
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

> The matched sequence is annotated as UDP-glucosyl transferase 73CC6, and its pathway annotation places it in secondary metabolite biosynthesis, specifically terpenoid biosynthesis. The annotation cites experimental evidence, though the supplied excerpts do not independently describe the experiments.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a plant family-1 UDP-dependent glycosyltransferase signature, including the conserved C-terminal PSPG-region motif (…HCGWNS…). Plant UGTs commonly transfer sugars to small-molecule acceptors, including specialized metabolites. This supports secondary-metabolite biosynthesis over protein glycosylation, LPS O-antigen biosynthesis, or pyrimidine metabolism among these choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable enzyme-family inference meaningfully distinguishes the broad pathway choice without requiring knowledge of this exact protein's recorded annotation. The family alone does not establish its precise substrate or pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The choices distinguish specialized-metabolite glycosylation from protein glycosylation and unrelated pathways; the sequence-family inference favors A.


### Important caveats

- The reviewer-only source annotation supports the key but was not available to the evaluated model.
- The sequence suggests a UGT family, but exact pathway assignment and substrate specificity require protein-specific evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a plant family-1 UDP-dependent glycosyltransferase signature, including the conserved C-terminal PSPG-region motif (…HCGWNS…). Plant UGTs commonly transfer sugars to small-molecule acceptors, including specialized metabolites. This supports secondary-metabolite biosynthesis over protein glycosylation, LPS O-antigen biosynthesis, or pyrimidine metabolism among these choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable enzyme-family inference meaningfully distinguishes the broad pathway choice without requiring knowledge of this exact protein's recorded annotation. The family alone does not establish its precise substrate or pathway."
  },
  "case_id": "pathway_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The matched sequence is annotated as UDP-glucosyl transferase 73CC6, and its pathway annotation places it in secondary metabolite biosynthesis, specifically terpenoid biosynthesis. The annotation cites experimental evidence, though the supplied excerpts do not independently describe the experiments."
  },
  "important_caveats": [
    "The reviewer-only source annotation supports the key but was not available to the evaluated model.",
    "The sequence suggests a UGT family, but exact pathway assignment and substrate specificity require protein-specific evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish specialized-metabolite glycosylation from protein glycosylation and unrelated pathways; the sequence-family inference favors A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched sequence is annotated as UDP-glucosyl transferase 73CC6, and its pathway annotation places it in secondary metabolite biosynthesis, specifically terpenoid biosynthesis. The annotation cites experimental evidence, though the supplied excerpts do not independently describe the experiments.",
    "evidence_ids": ["C4", "C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a plant family-1 UDP-dependent glycosyltransferase signature, including the conserved C-terminal PSPG-region motif (…HCGWNS…). Plant UGTs commonly transfer sugars to small-molecule acceptors, including specialized metabolites. This supports secondary-metabolite biosynthesis over protein glycosylation, LPS O-antigen biosynthesis, or pyrimidine metabolism among these choices.",
    "missing_item_specific_fact": "",
    "reason": "A transferable enzyme-family inference meaningfully distinguishes the broad pathway choice without requiring knowledge of this exact protein's recorded annotation. The family alone does not establish its precise substrate or pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The choices distinguish specialized-metabolite glycosylation from protein glycosylation and unrelated pathways; the sequence-family inference favors A."
  },
  "important_caveats": [
    "The reviewer-only source annotation supports the key but was not available to the evaluated model.",
    "The sequence suggests a UGT family, but exact pathway assignment and substrate specificity require protein-specific evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1J9R8 (GT736_SAPOF) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is UDP-glucosyl transferase 73CC6 (SoUGT73CC6) from Saponaria officinalis, characterized in the paper 'Unlocking saponin biosynthesis in soapwort' (Nat. Chem. Biol. 2025). Saponins are triterpenoid secondary metabolites, confirming the pathway assignment. The sequence matches the benchmark input exactly.

Citations as saved: [C5](#evidence-c5), [C4](#evidence-c4), [C6](#evidence-c6), [H3](#evidence-h3), [H1](#evidence-h1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the sequence contains the PSPG (Plant Secondary Product Glycosyltransferase) box motif, identifiable by the conserved 'HCGWNST' and surrounding residues (…FMTHCGWNSTIEGVSAGVGMVTWPLYAEQFYNEKLITQVLKIGVEAGVEEWNLWVDVGRKLVKREKIEAAIRAVMGEAGVEMRRKAKELSVKAKKAVQDGGSSHRNLMALIEDLQRIRDDKMSKVAN). This motif is the defining signature of the plant UGT (GT1) superfamily. From extensive knowledge of other plant UGTs (UGT73, UGT74, UGT78, UGT85, UGT91 families), a knowledgeable model recognizes that plant UGTs overwhelmingly function in secondary metabolite biosynthesis—glycosylating small molecules such as flavonoids, triterpenoids, alkaloids, and phenylpropanoids—rather than in protein glycosylation, pyrimidine metabolism, or LPS biosynthesis. Specifically: (1) Protein glycosylation (C) is performed by oligosaccharyltransferases and Golgi glycosyltransferases with entirely different folds and no PSPG box; (2) Pyrimidine metabolism (B) enzymes (dihydroorotate dehydrogenase, thymidylate synthase, etc.) share no structural or motif similarity; (3) LPS O-antigen biosynthesis (D) is a bacterial process using GT4/GT29-family glycosyltransferases with different motifs and no PSPG signature. The PSPG motif thus provides a concrete, transferable family-level feature that meaningfully distinguishes option A from all other choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the PSPG motif is a well-established, transferable feature of the plant UGT family learned from dozens of characterized plant UGTs. The overwhelming empirical pattern is that plant UGTs modify secondary metabolites, not proteins or primary metabolites. This family-level inference, combined with the absence of features diagnostic of pyrimidine enzymes or bacterial LPS biosynthetic machinery, provides a credible and concrete basis for selecting A over B, C, and D without needing to know the specific annotation of this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While option C (protein glycosylation) is a superficially tempting distractor because the protein is a glycosyltransferase, the PSPG motif specifically identifies it as a small-molecule glycosyltransferase of the plant UGT family, which is well distinguished from protein glycosylation machinery. Options B and D are clearly unrelated. No ambiguity remains among the offered choices given the PSPG motif recognition.


### Important caveats

- The PSPG motif identification relies on recognizing conserved sequence patterns; a model unfamiliar with the PSPG box might confuse this glycosyltransferase with a protein glycosylation enzyme (option C).
- The UniProt annotation is based on experimental characterization (ECO:0000269) from a 2025 Nat. Chem. Biol. paper, so the pathway assignment is experimentally supported, not merely inferred by homology.
- The reviewer-only evidence confirms the sequence match and annotation, but the evaluated model had access only to the raw sequence and the four pathway choices.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the sequence contains the PSPG (Plant Secondary Product Glycosyltransferase) box motif, identifiable by the conserved 'HCGWNST' and surrounding residues (…FMTHCGWNSTIEGVSAGVGMVTWPLYAEQFYNEKLITQVLKIGVEAGVEEWNLWVDVGRKLVKREKIEAAIRAVMGEAGVEMRRKAKELSVKAKKAVQDGGSSHRNLMALIEDLQRIRDDKMSKVAN). This motif is the defining signature of the plant UGT (GT1) superfamily. From extensive knowledge of other plant UGTs (UGT73, UGT74, UGT78, UGT85, UGT91 families), a knowledgeable model recognizes that plant UGTs overwhelmingly function in secondary metabolite biosynthesis—glycosylating small molecules such as flavonoids, triterpenoids, alkaloids, and phenylpropanoids—rather than in protein glycosylation, pyrimidine metabolism, or LPS biosynthesis. Specifically: (1) Protein glycosylation (C) is performed by oligosaccharyltransferases and Golgi glycosyltransferases with entirely different folds and no PSPG box; (2) Pyrimidine metabolism (B) enzymes (dihydroorotate dehydrogenase, thymidylate synthase, etc.) share no structural or motif similarity; (3) LPS O-antigen biosynthesis (D) is a bacterial process using GT4/GT29-family glycosyltransferases with different motifs and no PSPG signature. The PSPG motif thus provides a concrete, transferable family-level feature that meaningfully distinguishes option A from all other choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the PSPG motif is a well-established, transferable feature of the plant UGT family learned from dozens of characterized plant UGTs. The overwhelming empirical pattern is that plant UGTs modify secondary metabolites, not proteins or primary metabolites. This family-level inference, combined with the absence of features diagnostic of pyrimidine enzymes or bacterial LPS biosynthetic machinery, provides a credible and concrete basis for selecting A over B, C, and D without needing to know the specific annotation of this exact protein."
  },
  "case_id": "pathway_0112",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C4",
      "C6",
      "H3",
      "H1"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1J9R8 (GT736_SAPOF) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is UDP-glucosyl transferase 73CC6 (SoUGT73CC6) from Saponaria officinalis, characterized in the paper 'Unlocking saponin biosynthesis in soapwort' (Nat. Chem. Biol. 2025). Saponins are triterpenoid secondary metabolites, confirming the pathway assignment. The sequence matches the benchmark input exactly."
  },
  "important_caveats": [
    "The PSPG motif identification relies on recognizing conserved sequence patterns; a model unfamiliar with the PSPG box might confuse this glycosyltransferase with a protein glycosylation enzyme (option C).",
    "The UniProt annotation is based on experimental characterization (ECO:0000269) from a 2025 Nat. Chem. Biol. paper, so the pathway assignment is experimentally supported, not merely inferred by homology.",
    "The reviewer-only evidence confirms the sequence match and annotation, but the evaluated model had access only to the raw sequence and the four pathway choices."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While option C (protein glycosylation) is a superficially tempting distractor because the protein is a glycosyltransferase, the PSPG motif specifically identifies it as a small-molecule glycosyltransferase of the plant UGT family, which is well distinguished from protein glycosylation machinery. Options B and D are clearly unrelated. No ambiguity remains among the offered choices given the PSPG motif recognition."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0112",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1J9R8 (GT736_SAPOF) explicitly annotates the pathway as 'Secondary metabolite biosynthesis; terpenoid biosynthesis' with experimental evidence (ECO:0000269, PubMed:39043959). The protein is UDP-glucosyl transferase 73CC6 (SoUGT73CC6) from Saponaria officinalis, characterized in the paper 'Unlocking saponin biosynthesis in soapwort' (Nat. Chem. Biol. 2025). Saponins are triterpenoid secondary metabolites, confirming the pathway assignment. The sequence matches the benchmark input exactly.",
    "evidence_ids": ["C5", "C4", "C6", "H3", "H1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the sequence contains the PSPG (Plant Secondary Product Glycosyltransferase) box motif, identifiable by the conserved 'HCGWNST' and surrounding residues (…FMTHCGWNSTIEGVSAGVGMVTWPLYAEQFYNEKLITQVLKIGVEAGVEEWNLWVDVGRKLVKREKIEAAIRAVMGEAGVEMRRKAKELSVKAKKAVQDGGSSHRNLMALIEDLQRIRDDKMSKVAN). This motif is the defining signature of the plant UGT (GT1) superfamily. From extensive knowledge of other plant UGTs (UGT73, UGT74, UGT78, UGT85, UGT91 families), a knowledgeable model recognizes that plant UGTs overwhelmingly function in secondary metabolite biosynthesis—glycosylating small molecules such as flavonoids, triterpenoids, alkaloids, and phenylpropanoids—rather than in protein glycosylation, pyrimidine metabolism, or LPS biosynthesis. Specifically: (1) Protein glycosylation (C) is performed by oligosaccharyltransferases and Golgi glycosyltransferases with entirely different folds and no PSPG box; (2) Pyrimidine metabolism (B) enzymes (dihydroorotate dehydrogenase, thymidylate synthase, etc.) share no structural or motif similarity; (3) LPS O-antigen biosynthesis (D) is a bacterial process using GT4/GT29-family glycosyltransferases with different motifs and no PSPG signature. The PSPG motif thus provides a concrete, transferable family-level feature that meaningfully distinguishes option A from all other choices.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the PSPG motif is a well-established, transferable feature of the plant UGT family learned from dozens of characterized plant UGTs. The overwhelming empirical pattern is that plant UGTs modify secondary metabolites, not proteins or primary metabolites. This family-level inference, combined with the absence of features diagnostic of pyrimidine enzymes or bacterial LPS biosynthetic machinery, provides a credible and concrete basis for selecting A over B, C, and D without needing to know the specific annotation of this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While option C (protein glycosylation) is a superficially tempting distractor because the protein is a glycosyltransferase, the PSPG motif specifically identifies it as a small-molecule glycosyltransferase of the plant UGT family, which is well distinguished from protein glycosylation machinery. Options B and D are clearly unrelated. No ambiguity remains among the offered choices given the PSPG motif recognition."
  },
  "important_caveats": [
    "The PSPG motif identification relies on recognizing conserved sequence patterns; a model unfamiliar with the PSPG box might confuse this glycosyltransferase with a protein glycosylation enzyme (option C).",
    "The UniProt annotation is based on experimental characterization (ECO:0000269) from a 2025 Nat. Chem. Biol. paper, so the pathway assignment is experimentally supported, not merely inferred by homology.",
    "The reviewer-only evidence confirms the sequence match and annotation, but the evaluated model had access only to the raw sequence and the four pathway choices."
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
  "benchmark_sequence_length": 487,
  "benchmark_sequence_sha256": "b1b45ba99c50f4295f6244b8dfb1a6f33e09e922612161af815842f67ed015d4",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 487,
  "current_source_sequence_sha256": "b1b45ba99c50f4295f6244b8dfb1a6f33e09e922612161af815842f67ed015d4",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 5,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0AAW1J9R8",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "9a59059b7ffd1f6c1fad31864cf878dfa9b156b29abca47f100f1fefa03ca58c",
  "selected_historical_source_sequence_length": 487,
  "selected_historical_source_sequence_sha256": "b1b45ba99c50f4295f6244b8dfb1a6f33e09e922612161af815842f67ed015d4",
  "selected_historical_version": {
    "accession": "A0AAW1J9R8",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GT736_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1J9R8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:55.561717+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:55.561717+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:55.561717+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"UDP-glucosyl transferase 73CC6\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoUGT73CC6\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:55.561717+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-01T06:24:55.561717+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48156.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:55.561717+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d6756a6f7b434de420aa07cff6a4074c9de628376f0e1ebcc553a7107eb687ff",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1J9R8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J9R8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   GT736_SAPOF             Reviewed;         487 AA.\nAC   A0AAW1J9R8;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=UDP-glucosyl transferase 73CC6 {ECO:0000303|PubMed:39043959};\nDE            Short=SoUGT73CC6 {ECO:0000303|PubMed:39043959};\nDE            EC=2.4.1.- {ECO:0000269|PubMed:39043959};\nGN   Name=UGT73CC6 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11041839m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_08G118300 {ECO:0000312|EMBL:KAK9698621.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:40.480726+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a59059b7ffd1f6c1fad31864cf878dfa9b156b29abca47f100f1fefa03ca58c",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J9R8?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J9R8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48156.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:40.480726+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a59059b7ffd1f6c1fad31864cf878dfa9b156b29abca47f100f1fefa03ca58c",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J9R8?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1J9R8?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\nCC       {ECO:0000269|PubMed:39043959}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:40.480726+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 50-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "9a59059b7ffd1f6c1fad31864cf878dfa9b156b29abca47f100f1fefa03ca58c",
  "url": "https://rest.uniprot.org/unisave/A0AAW1J9R8?format=txt&versions=5"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 112. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
