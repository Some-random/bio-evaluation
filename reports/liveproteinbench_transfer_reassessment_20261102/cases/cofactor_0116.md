# cofactor_0116

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0116.txt)

**Task:** `cofactor`  
**Expected answer:** **C** — FAD

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MYDVIVVGAGWCGLAAAKTYLQTCPTARLLVVDGDSSIGGTWSKERLYPHLVAEAHYGLFEFSDLPMRREGILPDGRIPSAAVHAYLTEYATKFGLLPRIRLNTWIEDIRQDPTAIGDDKAPYWTLQVAGSSQPLQARKLIIATGLTSEPRMPSFPGREDFEGHVLHSKMMGRADTGKLLNDPSIRHVVVYGGSKSAFDAVYLLLRAGKTVDWVIREGGGGPSIMTPLNILGQPSFRLNNSRVMSLFSPNPFEVAGERSWWQRVMHQRAGTFAQLLVVWFWRVLAYLLQRPWKYDYSVNGKQLKPILGLDSVLWSPATLGVMTHPTLWEDIHSGERVTIRRQNITALGQNKHVVLSNGDRITADMVVCATGWHARHSLFTPDEQLAVGLPSTSSFDPKSQAHWLNLQKAADEEILEEFPLLQNCPIALPPVRCEDDHHLYRFVAPSSGPLAQERLIAYVGFLRTTGAPIVYEAQSLWATAYLTGALHVPALEEREKEVARTNAWIRRRYICGRKVPFALFDFLPYVDMLYRDLGVNSRRKKNAVSE

[Multiple Choices]
A. FMN
B. pantetheine 4'-phosphate
C. FAD
D. cob(II)alamin
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Predicting Protein Cofactor, which is to identify the specific cofactor required for a given protein's catalytic activity. A cofactor is a non-protein chemical compound or metallic ion that is essential for an enzyme's function. Based on the provided protein sequence, you will need to determine which of the multiple-choice options is the correct cofactor.. The inputs provided by the user for this task include:

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

> The matched UniProt entry annotates the protein as an FAD-dependent monooxygenase and lists FAD as its cofactor. The cofactor annotation is computationally supported (ECO:0000305), so this supports the key as a database annotation but does not by itself establish experimental verification.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The N-terminal glycine-rich sequence motif is compatible with flavin binding, and monooxygenase family knowledge makes a flavin cofactor plausible. But that kind of motif does not reliably distinguish FAD from FMN, both offered choices; the other options are less consistent with this flavoprotein-like sequence.


**Missing item-specific fact**

> Whether this particular protein uses FAD rather than FMN, established by an applicable annotation, close-homolog evidence, or direct cofactor characterization.


**Reason**

> Transferable sequence and enzyme-family knowledge supports a flavin cofactor but does not meaningfully resolve the key distinction between FAD and FMN. The specific cofactor assignment therefore depends on information about this protein or sufficiently close homologs that is not supplied.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[
  "A",
  "C"
]
```

> From the sequence alone, the flavin-compatible motif does not distinguish FMN from FAD. The reviewer-only annotation resolves the choice as FAD, but that information was not an original input.


### Important caveats

- The source sequence matches the supplied sequence.
- The cited cofactor annotation is computationally supported; the supplied evidence does not establish direct experimental measurement of FAD binding.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal glycine-rich sequence motif is compatible with flavin binding, and monooxygenase family knowledge makes a flavin cofactor plausible. But that kind of motif does not reliably distinguish FAD from FMN, both offered choices; the other options are less consistent with this flavoprotein-like sequence.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular protein uses FAD rather than FMN, established by an applicable annotation, close-homolog evidence, or direct cofactor characterization.",
    "reason": "Transferable sequence and enzyme-family knowledge supports a flavin cofactor but does not meaningfully resolve the key distinction between FAD and FMN. The specific cofactor assignment therefore depends on information about this protein or sufficiently close homologs that is not supplied."
  },
  "case_id": "cofactor_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates the protein as an FAD-dependent monooxygenase and lists FAD as its cofactor. The cofactor annotation is computationally supported (ECO:0000305), so this supports the key as a database annotation but does not by itself establish experimental verification."
  },
  "important_caveats": [
    "The source sequence matches the supplied sequence.",
    "The cited cofactor annotation is computationally supported; the supplied evidence does not establish direct experimental measurement of FAD binding."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [
      "A",
      "C"
    ],
    "reason": "From the sequence alone, the flavin-compatible motif does not distinguish FMN from FAD. The reviewer-only annotation resolves the choice as FAD, but that information was not an original input."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matched UniProt entry annotates the protein as an FAD-dependent monooxygenase and lists FAD as its cofactor. The cofactor annotation is computationally supported (ECO:0000305), so this supports the key as a database annotation but does not by itself establish experimental verification.",
    "evidence_ids": ["C4", "C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The N-terminal glycine-rich sequence motif is compatible with flavin binding, and monooxygenase family knowledge makes a flavin cofactor plausible. But that kind of motif does not reliably distinguish FAD from FMN, both offered choices; the other options are less consistent with this flavoprotein-like sequence.",
    "missing_item_specific_fact": "Whether this particular protein uses FAD rather than FMN, established by an applicable annotation, close-homolog evidence, or direct cofactor characterization.",
    "reason": "Transferable sequence and enzyme-family knowledge supports a flavin cofactor but does not meaningfully resolve the key distinction between FAD and FMN. The specific cofactor assignment therefore depends on information about this protein or sufficiently close homologs that is not supplied."
  },
  "question_ambiguity": {
    "multiple_defensible_options": ["A", "C"],
    "reason": "From the sequence alone, the flavin-compatible motif does not distinguish FMN from FAD. The reviewer-only annotation resolves the choice as FAD, but that information was not an original input."
  },
  "important_caveats": [
    "The source sequence matches the supplied sequence.",
    "The cited cofactor annotation is computationally supported; the supplied evidence does not establish direct experimental measurement of FAD binding."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXV6 (sequence matched) is annotated as 'FAD-dependent monooxygenase' with an explicit COFACTOR annotation listing FAD (ChEBI:CHEBI:57692). The evidence code is ECO:0000305 (inferred from sequence or functional similarity), indicating computational/transfer annotation rather than direct experimental determination, but the annotation is unambiguous and consistent with the protein's classification as a member of the lanomycin biosynthesis cluster. The expected answer C (FAD) is directly supported by the database record.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains a clear N-terminal Rossmann-fold dinucleotide-binding motif 'VIVVGAGWCG' (GxGxxG pattern at ~positions 7-14), a hallmark of flavin-binding proteins. The protein is 546 residues, substantially larger than typical FMN-only oxidoreductases (~200-300 aa) and consistent with FAD-dependent monooxygenases that require two Rossmann-type domains to accommodate the larger FAD molecule (adenine + isoalloxazine). A second glycine-rich region 'GGSKSAF' (~position 270) and 'GGGGPSIMTPL' (~position 250) suggest additional FAD-binding contacts characteristic of FAD (not FMN). Pantetheine 4'-phosphate is eliminated: no ACP-like 'GGDS/GGDL' phosphopantetheine attachment motif is present, and the overall architecture is not that of an acyl-transfer enzyme. Cob(II)alamin is eliminated: no B12-binding domain motifs (e.g., RxxH, DxHxH, or the characteristic B12-binding β-propeller) are evident. The combination of (1) Rossmann-fold motifs, (2) large multi-domain size typical of FAD monooxygenases, (3) multiple glycine-rich FAD-contact regions, and (4) absence of features for the other three cofactors allows a knowledgeable model to select FAD over FMN, pantetheine 4'-phosphate, and cob(II)alamin using family-level knowledge of FAD-dependent monooxygenases.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides recognizable Rossmann-fold motifs, protein size, and domain architecture that are transferable features shared across the FAD-dependent monooxygenase superfamily. A model familiar with flavoprotein structural biology can distinguish FAD from FMN by size and multi-domain FAD-binding architecture, and can eliminate pantetheine 4'-phosphate and cob(II)alamin by absence of their characteristic binding motifs. This constitutes legitimate family-level inference from other proteins.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> While FMN and FAD are both flavins and share Rossmann-fold binding, the 546-residue size, multiple glycine-rich regions, and overall multi-domain architecture strongly favor FAD over FMN. Pantetheine 4'-phosphate and cob(II)alamin lack any supporting sequence features. No two options are genuinely ambiguous given the sequence evidence.


### Important caveats

- The UniProt annotation uses evidence code ECO:0000305 (inferred from sequence/functional similarity), so the FAD assignment is computational/transfer-based rather than directly experimentally determined for this specific protein.
- The protein was identified as part of the lanomycin biosynthesis gene cluster (ORF4) in Pyrenophora dematioidea; its exact catalytic role and cofactor dependence may not have been independently biochemically characterized beyond genomic context.
- The distinguishing argument between FAD and FMN relies on protein size and multi-domain architecture, which is a strong but not absolute discriminator; some FMN-dependent enzymes can be large if part of multi-domain complexes.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains a clear N-terminal Rossmann-fold dinucleotide-binding motif 'VIVVGAGWCG' (GxGxxG pattern at ~positions 7-14), a hallmark of flavin-binding proteins. The protein is 546 residues, substantially larger than typical FMN-only oxidoreductases (~200-300 aa) and consistent with FAD-dependent monooxygenases that require two Rossmann-type domains to accommodate the larger FAD molecule (adenine + isoalloxazine). A second glycine-rich region 'GGSKSAF' (~position 270) and 'GGGGPSIMTPL' (~position 250) suggest additional FAD-binding contacts characteristic of FAD (not FMN). Pantetheine 4'-phosphate is eliminated: no ACP-like 'GGDS/GGDL' phosphopantetheine attachment motif is present, and the overall architecture is not that of an acyl-transfer enzyme. Cob(II)alamin is eliminated: no B12-binding domain motifs (e.g., RxxH, DxHxH, or the characteristic B12-binding β-propeller) are evident. The combination of (1) Rossmann-fold motifs, (2) large multi-domain size typical of FAD monooxygenases, (3) multiple glycine-rich FAD-contact regions, and (4) absence of features for the other three cofactors allows a knowledgeable model to select FAD over FMN, pantetheine 4'-phosphate, and cob(II)alamin using family-level knowledge of FAD-dependent monooxygenases.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides recognizable Rossmann-fold motifs, protein size, and domain architecture that are transferable features shared across the FAD-dependent monooxygenase superfamily. A model familiar with flavoprotein structural biology can distinguish FAD from FMN by size and multi-domain FAD-binding architecture, and can eliminate pantetheine 4'-phosphate and cob(II)alamin by absence of their characteristic binding motifs. This constitutes legitimate family-level inference from other proteins."
  },
  "case_id": "cofactor_0116",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXV6 (sequence matched) is annotated as 'FAD-dependent monooxygenase' with an explicit COFACTOR annotation listing FAD (ChEBI:CHEBI:57692). The evidence code is ECO:0000305 (inferred from sequence or functional similarity), indicating computational/transfer annotation rather than direct experimental determination, but the annotation is unambiguous and consistent with the protein's classification as a member of the lanomycin biosynthesis cluster. The expected answer C (FAD) is directly supported by the database record."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred from sequence/functional similarity), so the FAD assignment is computational/transfer-based rather than directly experimentally determined for this specific protein.",
    "The protein was identified as part of the lanomycin biosynthesis gene cluster (ORF4) in Pyrenophora dematioidea; its exact catalytic role and cofactor dependence may not have been independently biochemically characterized beyond genomic context.",
    "The distinguishing argument between FAD and FMN relies on protein size and multi-domain architecture, which is a strong but not absolute discriminator; some FMN-dependent enzymes can be large if part of multi-domain complexes."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While FMN and FAD are both flavins and share Rossmann-fold binding, the 546-residue size, multiple glycine-rich regions, and overall multi-domain architecture strongly favor FAD over FMN. Pantetheine 4'-phosphate and cob(II)alamin lack any supporting sequence features. No two options are genuinely ambiguous given the sequence evidence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0116",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXV6 (sequence matched) is annotated as 'FAD-dependent monooxygenase' with an explicit COFACTOR annotation listing FAD (ChEBI:CHEBI:57692). The evidence code is ECO:0000305 (inferred from sequence or functional similarity), indicating computational/transfer annotation rather than direct experimental determination, but the annotation is unambiguous and consistent with the protein's classification as a member of the lanomycin biosynthesis cluster. The expected answer C (FAD) is directly supported by the database record.",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains a clear N-terminal Rossmann-fold dinucleotide-binding motif 'VIVVGAGWCG' (GxGxxG pattern at ~positions 7-14), a hallmark of flavin-binding proteins. The protein is 546 residues, substantially larger than typical FMN-only oxidoreductases (~200-300 aa) and consistent with FAD-dependent monooxygenases that require two Rossmann-type domains to accommodate the larger FAD molecule (adenine + isoalloxazine). A second glycine-rich region 'GGSKSAF' (~position 270) and 'GGGGPSIMTPL' (~position 250) suggest additional FAD-binding contacts characteristic of FAD (not FMN). Pantetheine 4'-phosphate is eliminated: no ACP-like 'GGDS/GGDL' phosphopantetheine attachment motif is present, and the overall architecture is not that of an acyl-transfer enzyme. Cob(II)alamin is eliminated: no B12-binding domain motifs (e.g., RxxH, DxHxH, or the characteristic B12-binding β-propeller) are evident. The combination of (1) Rossmann-fold motifs, (2) large multi-domain size typical of FAD monooxygenases, (3) multiple glycine-rich FAD-contact regions, and (4) absence of features for the other three cofactors allows a knowledgeable model to select FAD over FMN, pantetheine 4'-phosphate, and cob(II)alamin using family-level knowledge of FAD-dependent monooxygenases.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides recognizable Rossmann-fold motifs, protein size, and domain architecture that are transferable features shared across the FAD-dependent monooxygenase superfamily. A model familiar with flavoprotein structural biology can distinguish FAD from FMN by size and multi-domain FAD-binding architecture, and can eliminate pantetheine 4'-phosphate and cob(II)alamin by absence of their characteristic binding motifs. This constitutes legitimate family-level inference from other proteins."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "While FMN and FAD are both flavins and share Rossmann-fold binding, the 546-residue size, multiple glycine-rich regions, and overall multi-domain architecture strongly favor FAD over FMN. Pantetheine 4'-phosphate and cob(II)alamin lack any supporting sequence features. No two options are genuinely ambiguous given the sequence evidence."
  },
  "important_caveats": [
    "The UniProt annotation uses evidence code ECO:0000305 (inferred from sequence/functional similarity), so the FAD assignment is computational/transfer-based rather than directly experimentally determined for this specific protein.",
    "The protein was identified as part of the lanomycin biosynthesis gene cluster (ORF4) in Pyrenophora dematioidea; its exact catalytic role and cofactor dependence may not have been independently biochemically characterized beyond genomic context.",
    "The distinguishing argument between FAD and FMN relies on protein size and multi-domain architecture, which is a strong but not absolute discriminator; some FMN-dependent enzymes can be large if part of multi-domain complexes."
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
  "benchmark_sequence_length": 546,
  "benchmark_sequence_sha256": "7df1c302f7926e2d8ce67872cea5f1885a96c661666cec76e87fe2b497b1dc21",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-02-05",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-02-05",
    "sequenceVersion": 1
  },
  "current_record_sha256": "604f2ff191211f3fc9173924778cd268cd13201aacb65262a9cd48362829e340",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 546,
  "current_source_sequence_sha256": "7df1c302f7926e2d8ce67872cea5f1885a96c661666cec76e87fe2b497b1dc21",
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
  "requested_accession": "P0DXV6",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "1aa3327dc9591ccf3b323653d57490eeb83ea02899e48e37df4e6dc51b099591",
  "selected_historical_source_sequence_length": 546,
  "selected_historical_source_sequence_sha256": "7df1c302f7926e2d8ce67872cea5f1885a96c661666cec76e87fe2b497b1dc21",
  "selected_historical_version": {
    "accession": "P0DXV6",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2025_02/2025_02",
    "firstReleaseDate": "23-Apr-2025",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "LAN4_PYRDE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV6.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXV6\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:48.282490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "604f2ff191211f3fc9173924778cd268cd13201aacb65262a9cd48362829e340",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV6.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV6.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-02-05\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-02-05\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:48.282490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "604f2ff191211f3fc9173924778cd268cd13201aacb65262a9cd48362829e340",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV6.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV6.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Helminthosporium dematioideum\",\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Dothideomycetes\",\"Pleosporomycetidae\",\"Pleosporales\",\"Pleosporineae\",\"Pleosporaceae\",\"Pyrenophora\"],\"scientificName\":\"Pyrenophora dematioidea\",\"taxonId\":139229}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:48.282490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "604f2ff191211f3fc9173924778cd268cd13201aacb65262a9cd48362829e340",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV6.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV6.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"Lanomycin biosynthesis cluster protein 4\"}}],\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"1.-.-.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"33857369\",\"source\":\"PubMed\"}],\"value\":\"FAD-dependent monooxygenase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:48.282490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "604f2ff191211f3fc9173924778cd268cd13201aacb65262a9cd48362829e340",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV6.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV6.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:57692\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"name\":\"FAD\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:29:48.282490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "604f2ff191211f3fc9173924778cd268cd13201aacb65262a9cd48362829e340",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV6.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXV6.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Liu N.\",\"Abramyan E.D.\",\"Cheng W.\",\"Perlatti B.\",\"Harvey C.J.B.\",\"Bills G.F.\",\"Tang Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"33857369\"},{\"database\":\"DOI\",\"id\":\"10.1021/jacs.1c01516\"}],\"citationType\":\"journal article\",\"firstPage\":\"6043\",\"id\":\"33857369\",\"journal\":\"J. Am. Chem. Soc.\",\"lastPage\":\"6047\",\"publicationDate\":\"2021\",\"title\":\"Targeted genome mining reveals the biosynthetic gene clusters of natural product CYP51 inhibitors.\",\"volume\":\"143\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"TTI-1096\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"FUNCTION\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:48.282490+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "604f2ff191211f3fc9173924778cd268cd13201aacb65262a9cd48362829e340",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXV6.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV6?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   LAN4_PYRDE              Reviewed;         546 AA.\nAC   P0DXV6;\nDT   05-FEB-2025, integrated into UniProtKB/Swiss-Prot.\nDT   05-FEB-2025, sequence version 1.\nDT   09-APR-2025, entry version 2.\nDE   RecName: Full=FAD-dependent monooxygenase {ECO:0000303|PubMed:33857369};\nDE            EC=1.-.-.- {ECO:0000305|PubMed:33857369};\nDE   AltName: Full=Lanomycin biosynthesis cluster protein 4 {ECO:0000303|PubMed:33857369};\nDE   Flags: Precursor;\nGN   Name=ORF4 {ECO:0000303|PubMed:33857369};\nOS   Pyrenophora dematioidea (Helminthosporium dematioideum).\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Dothideomycetes;\nOC   Pleosporomycetidae; Pleosporales; Pleosporineae; Pleosporaceae;\nOC   Pyrenophora.\nOX   NCBI_TaxID=139229;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:50.838620+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1aa3327dc9591ccf3b323653d57490eeb83ea02899e48e37df4e6dc51b099591",
  "url": "https://rest.uniprot.org/unisave/P0DXV6?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV6?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=FAD-dependent monooxygenase {ECO:0000303|PubMed:33857369};\nDE            EC=1.-.-.- {ECO:0000305|PubMed:33857369};\nDE   AltName: Full=Lanomycin biosynthesis cluster protein 4 {ECO:0000303|PubMed:33857369};\nDE   Flags: Precursor;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:50.838620+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1aa3327dc9591ccf3b323653d57490eeb83ea02899e48e37df4e6dc51b099591",
  "url": "https://rest.uniprot.org/unisave/P0DXV6?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV6?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], FUNCTION, AND PATHWAY.\nRC   STRAIN=TTI-1096;\nRX   PubMed=33857369; DOI=10.1021/jacs.1c01516;\nRA   Liu N., Abramyan E.D., Cheng W., Perlatti B., Harvey C.J.B., Bills G.F.,\nRA   Tang Y.;\nRT   \"Targeted genome mining reveals the biosynthetic gene clusters of natural\nRT   product CYP51 inhibitors.\";\nRL   J. Am. Chem. Soc. 143:6043-6047(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:50.838620+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-24",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1aa3327dc9591ccf3b323653d57490eeb83ea02899e48e37df4e6dc51b099591",
  "url": "https://rest.uniprot.org/unisave/P0DXV6?format=txt&versions=2"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXV6?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H4",
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=FAD; Xref=ChEBI:CHEBI:57692; Evidence={ECO:0000305};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:50.838620+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 35-36",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "1aa3327dc9591ccf3b323653d57490eeb83ea02899e48e37df4e6dc51b099591",
  "url": "https://rest.uniprot.org/unisave/P0DXV6?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 116. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
