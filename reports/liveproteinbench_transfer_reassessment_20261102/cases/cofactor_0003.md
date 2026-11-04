# cofactor_0003

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/cofactor_0003.txt)

**Task:** `cofactor`  
**Expected answer:** **B** — &#91;2Fe-2S&#93; cluster

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
A. Co(2+)
B. [2Fe-2S] cluster
C. tungstopterin
D. Mo-bis(molybdopterin guanine dinucleotide)
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

> The sequence-matched UniProt record annotates a &#91;2Fe-2S&#93; cluster, but the evidence is transferred from related proteins (ECO:0000250), not direct experimental evidence for this exact protein. The record also annotates Mg(2+), which is not among the choices.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with the long-chain dihydroxy-acid dehydratase (IlvD/DHAD) family, including a likely mitochondrial targeting segment at its N-terminus. Family-level knowledge associates these enzymes with iron-sulfur cofactors; that provides a meaningful basis for choosing the &#91;2Fe-2S&#93; option over cobalt or the tungsten- and molybdenum-pterin cofactors associated with different enzyme families.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level inference from the sequence can distinguish the offered cofactor classes without knowing this exact protein's database annotation. The precise cluster assignment is not established experimentally by the supplied input, but the options and transferable DHAD-family knowledge support B.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Only B among the offered options matches the transferable iron-sulfur cofactor inference. The source also annotates Mg(2+), but that is not an offered choice.


### Important caveats

- The reviewer-only sequence-matched annotation supports B but is explicitly based on evidence transferred from related proteins, not direct experimental evidence for this protein.
- The protein record annotates Mg(2+) as an additional cofactor, so the singular wording does not capture every annotated cofactor.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with the long-chain dihydroxy-acid dehydratase (IlvD/DHAD) family, including a likely mitochondrial targeting segment at its N-terminus. Family-level knowledge associates these enzymes with iron-sulfur cofactors; that provides a meaningful basis for choosing the [2Fe-2S] option over cobalt or the tungsten- and molybdenum-pterin cofactors associated with different enzyme families.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can distinguish the offered cofactor classes without knowing this exact protein's database annotation. The precise cluster assignment is not established experimentally by the supplied input, but the options and transferable DHAD-family knowledge support B."
  },
  "case_id": "cofactor_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates a [2Fe-2S] cluster, but the evidence is transferred from related proteins (ECO:0000250), not direct experimental evidence for this exact protein. The record also annotates Mg(2+), which is not among the choices."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched annotation supports B but is explicitly based on evidence transferred from related proteins, not direct experimental evidence for this protein.",
    "The protein record annotates Mg(2+) as an additional cofactor, so the singular wording does not capture every annotated cofactor."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B among the offered options matches the transferable iron-sulfur cofactor inference. The source also annotates Mg(2+), but that is not an offered choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "cofactor_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record annotates a [2Fe-2S] cluster, but the evidence is transferred from related proteins (ECO:0000250), not direct experimental evidence for this exact protein. The record also annotates Mg(2+), which is not among the choices.",
    "evidence_ids": ["C5", "C6", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with the long-chain dihydroxy-acid dehydratase (IlvD/DHAD) family, including a likely mitochondrial targeting segment at its N-terminus. Family-level knowledge associates these enzymes with iron-sulfur cofactors; that provides a meaningful basis for choosing the [2Fe-2S] option over cobalt or the tungsten- and molybdenum-pterin cofactors associated with different enzyme families.",
    "missing_item_specific_fact": "",
    "reason": "A family-level inference from the sequence can distinguish the offered cofactor classes without knowing this exact protein's database annotation. The precise cluster assignment is not established experimentally by the supplied input, but the options and transferable DHAD-family knowledge support B."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Only B among the offered options matches the transferable iron-sulfur cofactor inference. The source also annotates Mg(2+), but that is not an offered choice."
  },
  "important_caveats": [
    "The reviewer-only sequence-matched annotation supports B but is explicitly based on evidence transferred from related proteins, not direct experimental evidence for this protein.",
    "The protein record annotates Mg(2+) as an additional cofactor, so the singular wording does not capture every annotated cofactor."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is annotated as dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) with a &#91;2Fe-2S&#93; cluster cofactor. The evidence code is ECO:0000250 (inferred by similarity to Q0CPG9/P39522), which is computational rather than direct experimental evidence for this exact protein. However, the &#91;2Fe-2S&#93; requirement for DHAD enzymes is well-established from multiple experimental studies on homologs (E. coli IlvD, yeast ILV3, plant DHADs). The sequence contains characteristic cysteine-rich motifs (GCDKNMPG, PGCSAK, RNACPGKGACGG, PGSSSCPADDPKK) consistent with &#91;2Fe-2S&#93; coordination. Mg(2+) is also listed as a cofactor but is not among the offered options.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C4](#evidence-c4), [H2](#evidence-h2).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~596 aa, mitochondrial targeting-like N-terminus, cysteine-rich central region with motifs GCDKNMPG, PGCSAK, RNACPGKGACGG, PGSSSCPADDPKK) is recognizable as a dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) family member. DHAD enzymes from E. coli (IlvD), yeast (ILV3), plants, and fungi are well-characterized to require a &#91;2Fe-2S&#93; cluster for catalysis. This is a highly conserved family-level feature. The other options correspond to entirely different enzyme classes: Co(2+) for B12-dependent mutases, tungstopterin for tungsten-dependent oxidoreductases (e.g., formate dehydrogenases), and Mo-bis(MGD) for molybdenum enzymes (e.g., nitrate reductase, DMSO reductase). None of these cofactors are associated with the DHAD fold or its catalytic mechanism (dehydratation via radical chemistry on a bound &#91;2Fe-2S&#93;). A model familiar with DHAD biochemistry from any homolog can confidently select B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Recognition of the DHAD family from sequence architecture and cysteine motifs, combined with well-established knowledge that DHAD enzymes require &#91;2Fe-2S&#93; (from E. coli IlvD, yeast ILV3, and many structural studies), provides a concrete transferable inference that clearly distinguishes option B from the three alternatives, which belong to unrelated enzyme classes.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent cofactors from entirely distinct enzyme classes. Only &#91;2Fe-2S&#93; is associated with DHAD. Mg(2+) is also a DHAD cofactor per the annotation but is not offered as a choice, so no ambiguity exists among the presented alternatives.


### Important caveats

- The &#91;2Fe-2S&#93; annotation in UniProt is inferred by similarity (ECO:0000250), not experimentally verified for this exact Penicillium brasilianum protein. However, the family-level &#91;2Fe-2S&#93; requirement for DHAD is robustly supported by experimental data on multiple homologs.
- Mg(2+) is also annotated as a cofactor for this enzyme but is not among the answer choices, so it does not create ambiguity.
- The mitochondrial targeting sequence and overall domain architecture are consistent with mitochondrial DHAD, which is the form known to carry &#91;2Fe-2S&#93; (cytosolic DHAD in some organisms lacks the cluster).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~596 aa, mitochondrial targeting-like N-terminus, cysteine-rich central region with motifs GCDKNMPG, PGCSAK, RNACPGKGACGG, PGSSSCPADDPKK) is recognizable as a dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) family member. DHAD enzymes from E. coli (IlvD), yeast (ILV3), plants, and fungi are well-characterized to require a [2Fe-2S] cluster for catalysis. This is a highly conserved family-level feature. The other options correspond to entirely different enzyme classes: Co(2+) for B12-dependent mutases, tungstopterin for tungsten-dependent oxidoreductases (e.g., formate dehydrogenases), and Mo-bis(MGD) for molybdenum enzymes (e.g., nitrate reductase, DMSO reductase). None of these cofactors are associated with the DHAD fold or its catalytic mechanism (dehydratation via radical chemistry on a bound [2Fe-2S]). A model familiar with DHAD biochemistry from any homolog can confidently select B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the DHAD family from sequence architecture and cysteine motifs, combined with well-established knowledge that DHAD enzymes require [2Fe-2S] (from E. coli IlvD, yeast ILV3, and many structural studies), provides a concrete transferable inference that clearly distinguishes option B from the three alternatives, which belong to unrelated enzyme classes."
  },
  "case_id": "cofactor_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C4",
      "H2"
    ],
    "judgment": "supported",
    "reason": "The protein is annotated as dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) with a [2Fe-2S] cluster cofactor. The evidence code is ECO:0000250 (inferred by similarity to Q0CPG9/P39522), which is computational rather than direct experimental evidence for this exact protein. However, the [2Fe-2S] requirement for DHAD enzymes is well-established from multiple experimental studies on homologs (E. coli IlvD, yeast ILV3, plant DHADs). The sequence contains characteristic cysteine-rich motifs (GCDKNMPG, PGCSAK, RNACPGKGACGG, PGSSSCPADDPKK) consistent with [2Fe-2S] coordination. Mg(2+) is also listed as a cofactor but is not among the offered options."
  },
  "important_caveats": [
    "The [2Fe-2S] annotation in UniProt is inferred by similarity (ECO:0000250), not experimentally verified for this exact Penicillium brasilianum protein. However, the family-level [2Fe-2S] requirement for DHAD is robustly supported by experimental data on multiple homologs.",
    "Mg(2+) is also annotated as a cofactor for this enzyme but is not among the answer choices, so it does not create ambiguity.",
    "The mitochondrial targeting sequence and overall domain architecture are consistent with mitochondrial DHAD, which is the form known to carry [2Fe-2S] (cytosolic DHAD in some organisms lacks the cluster)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent cofactors from entirely distinct enzyme classes. Only [2Fe-2S] is associated with DHAD. Mg(2+) is also a DHAD cofactor per the annotation but is not offered as a choice, so no ambiguity exists among the presented alternatives."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "cofactor_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is annotated as dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) with a [2Fe-2S] cluster cofactor. The evidence code is ECO:0000250 (inferred by similarity to Q0CPG9/P39522), which is computational rather than direct experimental evidence for this exact protein. However, the [2Fe-2S] requirement for DHAD enzymes is well-established from multiple experimental studies on homologs (E. coli IlvD, yeast ILV3, plant DHADs). The sequence contains characteristic cysteine-rich motifs (GCDKNMPG, PGCSAK, RNACPGKGACGG, PGSSSCPADDPKK) consistent with [2Fe-2S] coordination. Mg(2+) is also listed as a cofactor but is not among the offered options.",
    "evidence_ids": ["C5", "H4", "C4", "H2"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~596 aa, mitochondrial targeting-like N-terminus, cysteine-rich central region with motifs GCDKNMPG, PGCSAK, RNACPGKGACGG, PGSSSCPADDPKK) is recognizable as a dihydroxy-acid dehydratase (DHAD, EC 4.2.1.9) family member. DHAD enzymes from E. coli (IlvD), yeast (ILV3), plants, and fungi are well-characterized to require a [2Fe-2S] cluster for catalysis. This is a highly conserved family-level feature. The other options correspond to entirely different enzyme classes: Co(2+) for B12-dependent mutases, tungstopterin for tungsten-dependent oxidoreductases (e.g., formate dehydrogenases), and Mo-bis(MGD) for molybdenum enzymes (e.g., nitrate reductase, DMSO reductase). None of these cofactors are associated with the DHAD fold or its catalytic mechanism (dehydratation via radical chemistry on a bound [2Fe-2S]). A model familiar with DHAD biochemistry from any homolog can confidently select B.",
    "missing_item_specific_fact": "",
    "reason": "Recognition of the DHAD family from sequence architecture and cysteine motifs, combined with well-established knowledge that DHAD enzymes require [2Fe-2S] (from E. coli IlvD, yeast ILV3, and many structural studies), provides a concrete transferable inference that clearly distinguishes option B from the three alternatives, which belong to unrelated enzyme classes."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent cofactors from entirely distinct enzyme classes. Only [2Fe-2S] is associated with DHAD. Mg(2+) is also a DHAD cofactor per the annotation but is not offered as a choice, so no ambiguity exists among the presented alternatives."
  },
  "important_caveats": [
    "The [2Fe-2S] annotation in UniProt is inferred by similarity (ECO:0000250), not experimentally verified for this exact Penicillium brasilianum protein. However, the family-level [2Fe-2S] requirement for DHAD is robustly supported by experimental data on multiple homologs.",
    "Mg(2+) is also annotated as a cofactor for this enzyme but is not among the answer choices, so it does not create ambiguity.",
    "The mitochondrial targeting sequence and overall domain architecture are consistent with mitochondrial DHAD, which is the form known to carry [2Fe-2S] (cytosolic DHAD in some organisms lacks the cluster)."
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
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:190135\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0CPG9\",\"source\":\"UniProtKB\"}],\"name\":\"[2Fe-2S] cluster\"}],\"commentType\":\"COFACTOR\",\"note\":{\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P39522\",\"source\":\"UniProtKB\"}],\"value\":\"Binds 1 [2Fe-2S] cluster per subunit.\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
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
  "excerpt": "{\"cofactors\":[{\"cofactorCrossReference\":{\"database\":\"ChEBI\",\"id\":\"CHEBI:18420\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"Q0CPG9\",\"source\":\"UniProtKB\"}],\"name\":\"Mg(2+)\"}],\"commentType\":\"COFACTOR\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/4",
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
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=[2Fe-2S] cluster; Xref=ChEBI:CHEBI:190135;\nCC         Evidence={ECO:0000250|UniProtKB:Q0CPG9};\nCC       Note=Binds 1 [2Fe-2S] cluster per subunit.\nCC       {ECO:0000250|UniProtKB:P39522};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 58-62",
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
  "excerpt": "CC   -!- COFACTOR:\nCC       Name=Mg(2+); Xref=ChEBI:CHEBI:18420;\nCC         Evidence={ECO:0000250|UniProtKB:Q0CPG9};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:04.510512+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 2,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 63-65",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "5c8dba2f186ec2f5c49e223d9e4d0a5408127c4f67b41ce2f7a9d3d700501ce5",
  "url": "https://rest.uniprot.org/unisave/A0A0F7TWW9?format=txt&versions=30"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/cofactor.json), zero-based source row 3. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
