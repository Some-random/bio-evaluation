# GO_molecular_function_0040

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0040.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **C** — 2 iron, 2 sulfur cluster binding

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MFNNFLNMYMCTLAEKLCKFKKNNFNNIHRNNNFYRDNNFYRDNNFYRDNNFYRDNNFYRDNNLYTNNNLYRDNNFYRDNNFYRDNNFYRDNNLYTNNNLYRDNNLYTNNNLYRDNNFYNITLRKFHFIQTISNNNFNFEIIKKYGDVINKIMFIHTQKKNKQERFMFNNKKYIKRKEYILNDLNEFISIIPHPEINNEITNNSNQKKNKDNKQNVLSTNQQIITNYNLNHKENVTSNLNFNNKEEDEKKLDKLLKKRNIKKRDIVTITEEAKEELKKIISINKKENNNNYNNMNTICSDNHNDMNTICNDKNILKLFFITKGCNGLTHSFNFISKKDIHKEDEIIYDDQNNILLVIDKNCILYVINTTLDYYKDDLTEKFIFKNPNITSICPCGTSFHFSKKK

[Multiple Choices]
A. RNA methyltransferase activity
B. protein heterodimerization activity
C. 2 iron, 2 sulfur cluster binding
D. guanyl-nucleotide exchange factor activity
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

> The sequence-matched UniProt record carries a 2Fe-2S cluster-binding GO annotation with IBA evidence. The record also reports experimental evidence that the protein binds and transfers Fe-S clusters, specifically &#91;4Fe-4S&#93;. That supports Fe-S-cluster binding generally, but does not experimentally establish the specific 2Fe-2S cluster type.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a Cys-containing region toward its C-terminus, alongside a long low-complexity N-terminal region. Transferable knowledge of Fe-S assembly proteins makes a cluster-binding function a credible inference from such a sequence pattern; none of the other options is suggested by an evident RNA methyltransferase catalytic domain or a recognizable nucleotide-exchange factor feature. This meaningfully favors C among the offered choices.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The inference need not identify the exact protein or establish which cluster type it binds. An Fe-S assembly/cluster-binding family-level inference distinguishes C from the listed alternatives, though it does not independently prove 2Fe-2S specificity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered option has comparably strong support from the sequence and transferable protein-family knowledge.


### Important caveats

- The specific 2Fe-2S annotation is IBA (inference by biological aspect of ancestor), whereas the cited experimental function describes binding and transfer of &#91;4Fe-4S&#93; clusters.
- The sequence-based inference supports Fe-S cluster binding generally more strongly than it supports the exact cluster type.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a Cys-containing region toward its C-terminus, alongside a long low-complexity N-terminal region. Transferable knowledge of Fe-S assembly proteins makes a cluster-binding function a credible inference from such a sequence pattern; none of the other options is suggested by an evident RNA methyltransferase catalytic domain or a recognizable nucleotide-exchange factor feature. This meaningfully favors C among the offered choices.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The inference need not identify the exact protein or establish which cluster type it binds. An Fe-S assembly/cluster-binding family-level inference distinguishes C from the listed alternatives, though it does not independently prove 2Fe-2S specificity."
  },
  "case_id": "GO_molecular_function_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record carries a 2Fe-2S cluster-binding GO annotation with IBA evidence. The record also reports experimental evidence that the protein binds and transfers Fe-S clusters, specifically [4Fe-4S]. That supports Fe-S-cluster binding generally, but does not experimentally establish the specific 2Fe-2S cluster type."
  },
  "important_caveats": [
    "The specific 2Fe-2S annotation is IBA (inference by biological aspect of ancestor), whereas the cited experimental function describes binding and transfer of [4Fe-4S] clusters.",
    "The sequence-based inference supports Fe-S cluster binding generally more strongly than it supports the exact cluster type."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option has comparably strong support from the sequence and transferable protein-family knowledge."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record carries a 2Fe-2S cluster-binding GO annotation with IBA evidence. The record also reports experimental evidence that the protein binds and transfers Fe-S clusters, specifically [4Fe-4S]. That supports Fe-S-cluster binding generally, but does not experimentally establish the specific 2Fe-2S cluster type.",
    "evidence_ids": ["C5", "C6", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a Cys-containing region toward its C-terminus, alongside a long low-complexity N-terminal region. Transferable knowledge of Fe-S assembly proteins makes a cluster-binding function a credible inference from such a sequence pattern; none of the other options is suggested by an evident RNA methyltransferase catalytic domain or a recognizable nucleotide-exchange factor feature. This meaningfully favors C among the offered choices.",
    "missing_item_specific_fact": "",
    "reason": "The inference need not identify the exact protein or establish which cluster type it binds. An Fe-S assembly/cluster-binding family-level inference distinguishes C from the listed alternatives, though it does not independently prove 2Fe-2S specificity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered option has comparably strong support from the sequence and transferable protein-family knowledge."
  },
  "important_caveats": [
    "The specific 2Fe-2S annotation is IBA (inference by biological aspect of ancestor), whereas the cited experimental function describes binding and transfer of [4Fe-4S] clusters.",
    "The sequence-based inference supports Fe-S cluster binding generally more strongly than it supports the exact cluster type."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (O97297, IscA2_PLAF7) annotates GO:0051537 (2 iron, 2 sulfur cluster binding) with evidence code IBA:GO_Central. The protein's FUNCTION comment (supported by PubMed:34032321, ECO:0000269) states it 'Participates in iron-sulfur cluster formation (ISC) pathway for iron-sulfur (Fe-S) cluster biogenesis' and 'Can bind and transfer &#91;4Fe-4S&#93; clusters to target apo-proteins.' The 2Fe-2S annotation is via computational transfer (IBA), while experimental evidence specifically demonstrates 4Fe-4S binding. However, IscA-family proteins are broadly characterized as Fe-S cluster binding/delivery proteins, and the 2Fe-2S GO term is present in the record. The answer is supported by the database annotation, though the direct experimental evidence more precisely supports 4Fe-4S binding.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The C-terminal region of the sequence contains a Cys-Pro-Cys (CPC) motif: '...ITSICPCGTSFHFSKKK'. The CPC motif is a well-established, transferable signature for 2Fe-2S cluster coordination found across many Fe-S binding proteins (ferredoxins, IscA-family scaffolds, plant-type ferredoxins, etc.). Additionally, the overall architecture—a long N-terminal low-complexity, N/F/Y-rich region (characteristic of apicomplexan proteins) followed by a compact C-terminal functional domain enriched in cysteines—is consistent with Fe-S cluster delivery/scaffold proteins rather than enzymes. The sequence lacks any recognizable methyltransferase fold (no Rossmann-like βαβ dinucleotide-binding motif, no catalytic aspartate/glutamate in a SAM-binding pocket), lacks Sec7 or other GEF structural domains, and lacks obvious coiled-coil/leucine-zipper dimerization motifs. The CPC motif alone meaningfully distinguishes option C (Fe-S cluster binding) from options A (methyltransferase), B (heterodimerization), and D (GEF), because CPC is a canonical Fe-S ligand motif not associated with those other functions.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can recognize the CPC motif as a Fe-S cluster binding signature from general biochemistry and protein-family knowledge (IscA, ferredoxins, plant-type 2Fe-2S proteins). The absence of catalytic, GEF, or dimerization motifs further eliminates the distractors. This constitutes a concrete transferable inference from sequence features and family-level knowledge, not requiring memorization of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent fundamentally different molecular functions (catalytic methylation, protein-protein binding, metal-cluster coordination, nucleotide exchange). The CPC motif and absence of alternative functional signatures clearly single out option C. No other option is credibly supported by the sequence features.


### Important caveats

- The GO:0051537 annotation is via IBA:GO_Central (computational transfer), not direct experimental proof of 2Fe-2S binding specifically; the experimental evidence (PubMed:34032321) demonstrates 4Fe-4S binding/transfer.
- The protein also carries GO:0051539 (4Fe-4S cluster binding) via IEA:UniProtKB-KW, so the distinction between 2Fe-2S and 4Fe-4S is annotation-level rather than experimentally resolved for this specific protein.
- The N-terminal region is extremely N/F/Y-rich with repeated motifs, characteristic of Plasmodium falciparum low-complexity sequences; this is not diagnostic of function but is consistent with apicomplexan proteins.
- The reviewer-only evidence confirms the sequence matches UniProt O97297 (IscA2_PLAF7), but this identification was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The C-terminal region of the sequence contains a Cys-Pro-Cys (CPC) motif: '...ITSICPCGTSFHFSKKK'. The CPC motif is a well-established, transferable signature for 2Fe-2S cluster coordination found across many Fe-S binding proteins (ferredoxins, IscA-family scaffolds, plant-type ferredoxins, etc.). Additionally, the overall architecture—a long N-terminal low-complexity, N/F/Y-rich region (characteristic of apicomplexan proteins) followed by a compact C-terminal functional domain enriched in cysteines—is consistent with Fe-S cluster delivery/scaffold proteins rather than enzymes. The sequence lacks any recognizable methyltransferase fold (no Rossmann-like βαβ dinucleotide-binding motif, no catalytic aspartate/glutamate in a SAM-binding pocket), lacks Sec7 or other GEF structural domains, and lacks obvious coiled-coil/leucine-zipper dimerization motifs. The CPC motif alone meaningfully distinguishes option C (Fe-S cluster binding) from options A (methyltransferase), B (heterodimerization), and D (GEF), because CPC is a canonical Fe-S ligand motif not associated with those other functions.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the CPC motif as a Fe-S cluster binding signature from general biochemistry and protein-family knowledge (IscA, ferredoxins, plant-type 2Fe-2S proteins). The absence of catalytic, GEF, or dimerization motifs further eliminates the distractors. This constitutes a concrete transferable inference from sequence features and family-level knowledge, not requiring memorization of this specific protein's annotation."
  },
  "case_id": "GO_molecular_function_0040",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (O97297, IscA2_PLAF7) annotates GO:0051537 (2 iron, 2 sulfur cluster binding) with evidence code IBA:GO_Central. The protein's FUNCTION comment (supported by PubMed:34032321, ECO:0000269) states it 'Participates in iron-sulfur cluster formation (ISC) pathway for iron-sulfur (Fe-S) cluster biogenesis' and 'Can bind and transfer [4Fe-4S] clusters to target apo-proteins.' The 2Fe-2S annotation is via computational transfer (IBA), while experimental evidence specifically demonstrates 4Fe-4S binding. However, IscA-family proteins are broadly characterized as Fe-S cluster binding/delivery proteins, and the 2Fe-2S GO term is present in the record. The answer is supported by the database annotation, though the direct experimental evidence more precisely supports 4Fe-4S binding."
  },
  "important_caveats": [
    "The GO:0051537 annotation is via IBA:GO_Central (computational transfer), not direct experimental proof of 2Fe-2S binding specifically; the experimental evidence (PubMed:34032321) demonstrates 4Fe-4S binding/transfer.",
    "The protein also carries GO:0051539 (4Fe-4S cluster binding) via IEA:UniProtKB-KW, so the distinction between 2Fe-2S and 4Fe-4S is annotation-level rather than experimentally resolved for this specific protein.",
    "The N-terminal region is extremely N/F/Y-rich with repeated motifs, characteristic of Plasmodium falciparum low-complexity sequences; this is not diagnostic of function but is consistent with apicomplexan proteins.",
    "The reviewer-only evidence confirms the sequence matches UniProt O97297 (IscA2_PLAF7), but this identification was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular functions (catalytic methylation, protein-protein binding, metal-cluster coordination, nucleotide exchange). The CPC motif and absence of alternative functional signatures clearly single out option C. No other option is credibly supported by the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0040",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (O97297, IscA2_PLAF7) annotates GO:0051537 (2 iron, 2 sulfur cluster binding) with evidence code IBA:GO_Central. The protein's FUNCTION comment (supported by PubMed:34032321, ECO:0000269) states it 'Participates in iron-sulfur cluster formation (ISC) pathway for iron-sulfur (Fe-S) cluster biogenesis' and 'Can bind and transfer [4Fe-4S] clusters to target apo-proteins.' The 2Fe-2S annotation is via computational transfer (IBA), while experimental evidence specifically demonstrates 4Fe-4S binding. However, IscA-family proteins are broadly characterized as Fe-S cluster binding/delivery proteins, and the 2Fe-2S GO term is present in the record. The answer is supported by the database annotation, though the direct experimental evidence more precisely supports 4Fe-4S binding.",
    "evidence_ids": ["C5", "C6", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The C-terminal region of the sequence contains a Cys-Pro-Cys (CPC) motif: '...ITSICPCGTSFHFSKKK'. The CPC motif is a well-established, transferable signature for 2Fe-2S cluster coordination found across many Fe-S binding proteins (ferredoxins, IscA-family scaffolds, plant-type ferredoxins, etc.). Additionally, the overall architecture—a long N-terminal low-complexity, N/F/Y-rich region (characteristic of apicomplexan proteins) followed by a compact C-terminal functional domain enriched in cysteines—is consistent with Fe-S cluster delivery/scaffold proteins rather than enzymes. The sequence lacks any recognizable methyltransferase fold (no Rossmann-like βαβ dinucleotide-binding motif, no catalytic aspartate/glutamate in a SAM-binding pocket), lacks Sec7 or other GEF structural domains, and lacks obvious coiled-coil/leucine-zipper dimerization motifs. The CPC motif alone meaningfully distinguishes option C (Fe-S cluster binding) from options A (methyltransferase), B (heterodimerization), and D (GEF), because CPC is a canonical Fe-S ligand motif not associated with those other functions.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can recognize the CPC motif as a Fe-S cluster binding signature from general biochemistry and protein-family knowledge (IscA, ferredoxins, plant-type 2Fe-2S proteins). The absence of catalytic, GEF, or dimerization motifs further eliminates the distractors. This constitutes a concrete transferable inference from sequence features and family-level knowledge, not requiring memorization of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent fundamentally different molecular functions (catalytic methylation, protein-protein binding, metal-cluster coordination, nucleotide exchange). The CPC motif and absence of alternative functional signatures clearly single out option C. No other option is credibly supported by the sequence features."
  },
  "important_caveats": [
    "The GO:0051537 annotation is via IBA:GO_Central (computational transfer), not direct experimental proof of 2Fe-2S binding specifically; the experimental evidence (PubMed:34032321) demonstrates 4Fe-4S binding/transfer.",
    "The protein also carries GO:0051539 (4Fe-4S cluster binding) via IEA:UniProtKB-KW, so the distinction between 2Fe-2S and 4Fe-4S is annotation-level rather than experimentally resolved for this specific protein.",
    "The N-terminal region is extremely N/F/Y-rich with repeated motifs, characteristic of Plasmodium falciparum low-complexity sequences; this is not diagnostic of function but is consistent with apicomplexan proteins.",
    "The reviewer-only evidence confirms the sequence matches UniProt O97297 (IscA2_PLAF7), but this identification was not available to the evaluated model."
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
  "benchmark_sequence_length": 404,
  "benchmark_sequence_sha256": "1acf9cb41bfaea25908ce91d1c41f1ea1fac9268947da35d853e46258389584e",
  "current_entry_audit": {
    "entryVersion": 130,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "1999-05-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 404,
  "current_source_sequence_sha256": "1acf9cb41bfaea25908ce91d1c41f1ea1fac9268947da35d853e46258389584e",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 128,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "O97297",
  "selected_historical_entry_version": 128,
  "selected_historical_record_sha256": "f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633",
  "selected_historical_source_sequence_length": 404,
  "selected_historical_source_sequence_sha256": "1acf9cb41bfaea25908ce91d1c41f1ea1fac9268947da35d853e46258389584e",
  "selected_historical_version": {
    "accession": "O97297",
    "database": "Swiss-Prot",
    "entryVersion": 128,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ISCA2_PLAF7",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"O97297\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":130,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"1999-05-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"UP000001450\",\"source\":\"Proteomes\"}],\"lineage\":[\"Eukaryota\",\"Sar\",\"Alveolata\",\"Apicomplexa\",\"Aconoidasida\",\"Haemosporida\",\"Plasmodiidae\",\"Plasmodium\",\"Laverania\"],\"scientificName\":\"Plasmodium falciparum (isolate 3D7)\",\"taxonId\":36329}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Iron-sulfur assembly protein IscA2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"value\":\"PfIscA2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"34032321\",\"source\":\"PubMed\"}],\"value\":\"Participates in iron-sulfur cluster formation (ISC) pathway for iron-sulfur (Fe-S) cluster biogenesis (PubMed:34032321). Can bind and transfer [4Fe-4S] clusters to target apo-proteins (PubMed:34032321)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0051537\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:2 iron, 2 sulfur cluster binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IBA:GO_Central\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/18",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/O97297.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"citation\":{\"authors\":[\"Sadik M.\",\"Afsar M.\",\"Ramachandran R.\",\"Habib S.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"34032321\"},{\"database\":\"DOI\",\"id\":\"10.1111/mmi.14735\"}],\"citationType\":\"journal article\",\"firstPage\":\"606\",\"id\":\"34032321\",\"journal\":\"Mol. Microbiol.\",\"lastPage\":\"623\",\"publicationDate\":\"2021\",\"title\":\"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the Plasmodium falciparum mitochondrion.\",\"volume\":\"116\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"referenceNumber\":4,\"referencePositions\":[\"FUNCTION\",\"SUBUNIT\",\"SUBCELLULAR LOCATION\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-01T06:25:14.613954+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "9e07b2230ce28301f48911a9183e492a53b7d4a497fe4b6c29069aa554cb1ed5",
  "url": "https://rest.uniprot.org/uniprotkb/O97297.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)

```json
{
  "entry_version": 128,
  "evidence_id": "H1",
  "excerpt": "ID   ISCA2_PLAF7             Reviewed;         404 AA.\nAC   O97297;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-MAY-1999, sequence version 1.\nDT   28-JAN-2026, entry version 128.\nDE   RecName: Full=Iron-sulfur assembly protein IscA2 {ECO:0000305};\nDE            Short=PfIscA2 {ECO:0000303|PubMed:34032321};\nGN   Name=IscA2 {ECO:0000305};\nGN   ORFNames=PF3D7_0322500 {ECO:0000312|EMBL:CAB39044.1};\nOS   Plasmodium falciparum (isolate 3D7).\nOC   Eukaryota; Sar; Alveolata; Apicomplexa; Aconoidasida; Haemosporida;\nOC   Plasmodiidae; Plasmodium; Plasmodium (Laverania).\nOX   NCBI_TaxID=36329 {ECO:0000312|Proteomes:UP000001450};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.381564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-13",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633",
  "url": "https://rest.uniprot.org/unisave/O97297?format=txt&versions=128"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)

```json
{
  "entry_version": 128,
  "evidence_id": "H2",
  "excerpt": "RN   [4] {ECO:0000305}\nRP   FUNCTION, SUBUNIT, AND SUBCELLULAR LOCATION.\nRX   PubMed=34032321; DOI=10.1111/mmi.14735;\nRA   Sadik M., Afsar M., Ramachandran R., Habib S.;\nRT   \"[Fe-S] biogenesis and unusual assembly of the ISC scaffold complex in the\nRT   Plasmodium falciparum mitochondrion.\";\nRL   Mol. Microbiol. 116:606-623(2021).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.381564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 62-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633",
  "url": "https://rest.uniprot.org/unisave/O97297?format=txt&versions=128"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)

```json
{
  "entry_version": 128,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Participates in iron-sulfur cluster formation (ISC) pathway\nCC       for iron-sulfur (Fe-S) cluster biogenesis (PubMed:34032321). Can bind\nCC       and transfer [4Fe-4S] clusters to target apo-proteins\nCC       (PubMed:34032321). {ECO:0000269|PubMed:34032321}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.381564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 78-81",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633",
  "url": "https://rest.uniprot.org/unisave/O97297?format=txt&versions=128"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)

```json
{
  "entry_version": 128,
  "evidence_id": "H4",
  "excerpt": "DR   GO; GO:0051537; F:2 iron, 2 sulfur cluster binding; IBA:GO_Central.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.381564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-111",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633",
  "url": "https://rest.uniprot.org/unisave/O97297?format=txt&versions=128"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)

```json
{
  "entry_version": 128,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0051539; F:4 iron, 4 sulfur cluster binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.381564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 112-112",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633",
  "url": "https://rest.uniprot.org/unisave/O97297?format=txt&versions=128"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/O97297?format=txt&versions=128)

```json
{
  "entry_version": 128,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0046872; F:metal ion binding; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:16.381564+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 113-113",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "f66fa783bc1cfa4c7dea778172f820cf3d9b9708cee3f7b45ea0f320681d6633",
  "url": "https://rest.uniprot.org/unisave/O97297?format=txt&versions=128"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0005085\nname: guanyl-nucleotide exchange factor activity\nnamespace: molecular_function\nalt_id: GO:0005086\nalt_id: GO:0005087\nalt_id: GO:0005088\nalt_id: GO:0005089\nalt_id: GO:0005090\nalt_id: GO:0008321\nalt_id: GO:0008433\nalt_id: GO:0016219\nalt_id: GO:0016220\nalt_id: GO:0017034\nalt_id: GO:0017112\nalt_id: GO:0017132\nalt_id: GO:0019839\nalt_id: GO:0030676\ndef: \"Stimulates the exchange of GDP to GTP on a signaling GTPase, changing its conformation to its active form. Guanine nucleotide exchange factors (GEFs) act by stimulating the release of guanosine diphosphate (GDP) to allow binding of guanosine triphosphate (GTP), which is more abundant in the cell under normal cellular physiological conditions.\" [GOC:kd, GOC:mah, PMID:23303910, PMID:27218782]\nsubset: goslim_chembl\nsubset: goslim_drosophila\nsubset: goslim_yeast\nsynonym: \"ARF guanyl-nucleotide exchange factor activity\" NARROW []\nsynonym: \"cAMP-dependent guanyl-nucleotide exchange factor activity\" NARROW []\nsynonym: \"GDP-dissociation stimulator activity\" EXACT []\nsynonym: \"GDS\" EXACT []\nsynonym: \"GEF\" EXACT []\nsynonym: \"GNRP\" NARROW []\nsynonym: \"guanyl-nucleotide release factor activity\" EXACT []\nsynonym: \"guanyl-nucleotide releasing factor\" EXACT []\nsynonym: \"Rab guanyl-nucleotide exchange factor activity\" NARROW []\nsynonym: \"Rac guanyl-nucleotide exchange factor activity\" NARROW []\nsynonym: \"Ral guanyl-nucleotide exchange factor activity\" NARROW []\nsynonym: \"Ran guanyl-nucleotide exchange factor activity\" NARROW []\nsynonym: \"Rap guanyl-nucleotide exchange factor activity\" NARROW []\nsynonym: \"Ras guanyl-nucleotide exchange factor activity\" NARROW []\nsynonym: \"Rho guanine nucleotide exchange factor\" EXACT []\nsynonym: \"Rho guanyl-nucleotide exchange factor activity\" NARROW []\nsynonym: \"RhoGEF\" EXACT []\nsynonym: \"Sar guanyl-nucleotide exchange factor activity\" NARROW []\nxref: Reactome:R-HSA-109807 \"GRB2:SOS:p-Y427-SHC1 mediated nucleotide exchange of RAS\"\nxref: Reactome:R-HSA-109817 \"GRB2:SOS1:p-Y-IRS1,p-Y-IRS2 mediated nucleotide exchange of RAS\"\nxref: Reactome:R-HSA-114544 \"p115-RhoGEF activation of RHOA\"\nxref: Reactome:R-HSA-1168636 \"p-RasGRP1,3:DAG cause RAS to exchange GDP for GTP\"\nxref: Reactome:R-HSA-1225951 \"SOS-mediated nucleotide exchange of RAS (mediated by GRB2:SOS1 in complex with ligand-responsive p-6Y-EGFR mutants)\"\nxref: Reactome:R-HSA-1225957 \"SOS-mediated nucleotide exchange of RAS (mediated by GRB2:SOS1 in complex with phosphorylated SHC1 and ligand-responsive p-6Y-EGFR mutants)\"\nxref: Reactome:R-HSA-1250383 \"RAS guanyl-nucleotide exchange mediated by SOS1 in complex with GRB2 and p-Y349,350-SHC1:p-ERBB4\"\nxref: Reactome:R-HSA-1250463 \"RAS guanyl-nucleotide exchange mediated by SOS1 in complex with GRB2 and p-SHC1:Phosphorylated ERBB2 heterodimers\"\nxref: Reactome:R-HSA-1250498 \"RAS guanyl-nucleotide exchange mediated by SOS1 in complex with GRB2 and phosphorylated EGFR:ERBB2 heterodimers\"\nxref: Reactome:R-HSA-1306972 \"RAS guanyl nucleotide exchange mediated by SOS1 bound to GRB2 in complex with phosphorylated ERBB4:ERBB2 heterodimers\"\nxref: Reactome:R-HSA-1433415 \"Activation of RAC1\"\nxref: Reactome:R-HSA-1433471 \"Activation of RAS by p-KIT bound SOS1\"\nxref: Reactome:R-HSA-156913 \"Regeneration of eEF1A:GTP by eEF1B activity\"\nxref: Reactome:R-HSA-169904 \"C3G stimulates nucleotide exchange on Rap1\"\nxref: Reactome:R-HSA-170979 \"(Frs2)C3G stimulates nucleotide exchange on Rap1\"\nxref: Reactome:R-HSA-171026 \"Guanine nucleotide exchange on RAL\"\nxref: Reactome:R-HSA-177938 \"SOS1-mediated nucleotide exchange of RAS (EGF:EGFR:GRB2:SOS1)\"\nxref: Reactome:R-HSA-177945 \"SOS1-mediated nucleotide exchange of RAS (EGF:EGFR:SHC1:GRB2:SOS1)\"\nxref: Reactome:R-HSA-180687 \"Conversion of Ran-GDP to Ran-GTP\"\nxref: Reactome:R-HSA-186834 \"SOS-mediated nucleotide exchange on RAS (PDGF receptor:GRB2:SOS)\"\nxref: Reactome:R-HSA-187746 \"RIT/RIN are activated\"\nxref: Reactome:R-HSA-194518 \"RhoA is activated by nucleotide exchange and inhibits axonal growth\"\nxref: Reactome:R-HSA-2029445 \"An unknown GEF exchanges GTP for GDP on CDC42:GDP\"\nxref: Reactome:R-HSA-2029451 \"Activation of RAC1 by VAV\"\nxref: Reactome:R-HSA-2029467 \"Activation of RAC1 by CRKII:DOCK180:ELMO\"\nxref: Reactome:R-HSA-203977 \"SAR1 Activation And Membrane Binding\"\nxref: Reactome:R-HSA-205039 \"p75NTR indirectly activates RAC and Cdc42 via a guanyl-nucleotide exchange factor\"\nxref: Reactome:R-HSA-210977 \"Sos-mediated nucleotide exchange of Ras (Tie2 receptor:Grb2:Sos)\"\nxref: Reactome:R-HSA-2179407 \"SOS1-mediated nucleotide exchange of RAS (HB-EFG-initiated)\"\nxref: Reactome:R-HSA-2424476 \"Activation of RAC1 by VAV2/3\"\nxref: Reactome:R-HSA-2424477 \"SOS mediated nucleotide exchange of RAS (SHC)\"\nxref: Reactome:R-HSA-2485180 \"MII catalyses GDP/GTP exchange on Gt\"\nxref: Reactome:R-HSA-2730840 \"Activation of RAC1 by VAV\"\nxref: Reactome:R-HSA-350769 \"trans-Golgi Network Coat Activation\"\nxref: Reactome:R-HSA-354173 \"Activation of Rap1 by cytosolic GEFs\"\nxref: Reactome:R-HSA-379044 \"Liganded Gs-activating GPCR acts as a GEF for Gs\"\nxref: Reactome:R-HSA-379048 \"Liganded Gq/11-activating GPCRs act as GEFs for Gq/11\"\nxref: Reactome:R-HSA-380073 \"Liganded Gi-activating GPCR acts as a GEF for Gi\"\nxref: Reactome:R-HSA-381727 \"RAP1A exchanges GDP for GTP\"\nxref: Reactome:R-HSA-389348 \"Activation of Rac1 by pVav1\"\nxref: Reactome:R-HSA-389350 \"Activation of Cdc42 by pVav1\"\nxref: Reactome:R-HSA-392054 \"NCAM1:pFAK:Grb2:Sos-mediated nucleotide exchange of Ras\"\nxref: Reactome:R-HSA-392195 \"Gi activation by P2Y purinoceptor 12\"\nxref: Reactome:R-HSA-3928592 \"p190RhoGEF exchanges GTP for GDP on RHOA, activating it\"\nxref: Reactome:R-HSA-3928612 \"KALRN exchanges GTP for GDP on RAC1, activating it\"\nxref: Reactome:R-HSA-3928628 \"VAV exchanges GTP for GDP on RAC1, activating it\"\nxref: Reactome:R-HSA-3928632 \"ITSN1 exchanges GTP for GDP on CDC42, activating it\"\nxref: Reactome:R-HSA-3928633 \"bPIX exchanges GTP for GDP on RAC, activating it\"\nxref: Reactome:R-HSA-3928642 \"TIAM1 exchanges GTP for GDP on RAC1, activating it\"\nxref: Reactome:R-HSA-3928651 \"NGEF exchanges GTP for GDP on RHOA\"\nxref: Reactome:R-HSA-392870 \"Gs activation by prostacyclin receptor\"\nxref: Reactome:R-HSA-3965444 \"WNT:FZD complex promotes G-protein nucleotide exchange\"\nxref: Reactome:R-HSA-399938 \"Activation of Rac1 by FARP2\"\nxref: Reactome:R-HSA-399995 \"Muscarinic Acetylcholine Receptor M3 activates Gq\"\nxref: Reactome:R-HSA-400037 \"Gi,Go Heterotrimeric G-protein complex dissociates\"\nxref: Reactome:R-HSA-400092 \"Alpha-2A,alpha-2C Adrenergic Receptors activate Gi.Go heterotrimeric G proteins\"\nxref: Reactome:R-HSA-4093336 \"p-TIAM1 exchanges GTP for GDP on RAC1, activating it\"\nxref: Reactome:R-HSA-416530 \"FFAR1:FFAR1 ligands activate Gq\"\nxref: Reactome:R-HSA-416588 \"Activation of Rho by LARG and PDZ-RhoGEF\"\nxref: Reactome:R-HSA-418579 \"Gq activation by P2Y purinoceptor 1\"\nxref: Reactome:R-HSA-418850 \"Activation of Cdc42\"\nxref: Reactome:R-HSA-418856 \"Activation of Rac1\"\nxref: Reactome:R-HSA-419166 \"GEFs activate RhoA,B,C\"\nxref: Reactome:R-HSA-420883 \"Opsins act as GEFs for G alpha-t\"\nxref: Reactome:R-HSA-428535 \"Activation of RAC1 by SOS\"\nxref: Reactome:R-HSA-428750 \"Gq activation by TP receptor\"\nxref: Reactome:R-HSA-428917 \"G13 activation by TP receptor\"\nxref: Reactome:R-HSA-442273 \"VAV1 is a GEF for Rho/Rac family GTPases\"\nxref: Reactome:R-HSA-442291 \"VAV2 is a GEF for Rho/Rac family kinases\"\nxref: Reactome:R-HSA-442314 \"VAV3 is a GEF for Rho/Rac family kinases\"\nxref: Reactome:R-HSA-442732 \"NMDA-activated RASGRF1 activates RAS\"\nxref: Reactome:R-HSA-445064 \"Activation of Rac1 by VAV2\"\nxref: Reactome:R-HSA-5218829 \"VEGF induces CDC42 activation by unknown mechanism\"\nxref: Reactome:R-HSA-5218839 \"DOCK180:ELMO exchanges GTP for GDP, activating RAC1\"\nxref: Reactome:R-HSA-5218850 \"VAV exchanges GTP for GDP on RAC1, activating it\"\nxref: Reactome:R-HSA-5617816 \"RAB3IP stimulates nucleotide exchange on RAB8A\"\nxref: Reactome:R-HSA-5623508 \"GBF1 stimulates nucleotide exchange on ARF4\"\nxref: Reactome:R-HSA-5623521 \"RAB3IP stimulates nucleotide exchange on RAB8A\"\nxref: Reactome:R-HSA-5637806 \"SOS-mediated nucleotide exchange of RAS (mediated by GRB2:SOS1 in complex with p-EGFRvIII)\"\nxref: Reactome:R-HSA-5637808 \"SOS-mediated nucleotide exchange of RAS (mediated by GRB2:SOS1 in complex with phosphorylated SHC1 and p-EGFRvIII)\"\nxref: Reactome:R-HSA-5654392 \"Activated FGFR1:p-FRS:GRB2:SOS1 activates RAS nucleotide exchange\"\nxref: Reactome:R-HSA-5654402 \"Activated FGFR2:p-SHC1:GRB2:SOS1 activates RAS nucleotide exchange\"\nxref: Reactome:R-HSA-5654413 \"Activated FGFR3:p-FRS2:GRB2:SOS1 activates RAS nucleotide exchange\"\nxref: Reactome:R-HSA-5654426 \"Activated FGFR4:p-SHC1:GRB2:SOS1 activates RAS nucleotide exchange\"\nxref: Reactome:R-HSA-5654600 \"Activated FGFR1:p-SHC1:GRB2:SOS1 activates RAS nucleotide exchange\"\nxref: Reactome:R-HSA-5654618 \"Activated FGFR2:p-FRS2:GRB2:SOS1 activates RAS nucleotide exchange\"\nxref: Reactome:R-HSA-5654647 \"Activated FGFR3:p-SHC1:GRB2:SOS1 activates RAS nucleotide exchange\"\nxref: Reactome:R-HSA-5654663 \"Activated FGFR4:p-FRS2:GRB2:SOS1 activates RAS nucleotide exchange\"\nxref: Reactome:R-HSA-5655241 \"Activated FGFR2 mutants:p-FRS2:GRB2:SOS1 activates RAS nucleotide exchange\"\nxref: Reactome:R-HSA-5655277 \"Activated FGFR3 point, translocation and fusion mutants:p-FRS2:GRB2:SOS1 activates RAS nucleotide exchange\"\nxref: Reactome:R-HSA-5655326 \"Activated FGFR1 mutants:p-FRS2:GRB2:SOS1 activates RAS nucleotide exchange\"\nxref: Reactome:R-HSA-5655347 \"Activated FGFR4 mutants:p-FRS2:GRB2:SOS1 activates RAS nucleotide exchange\"\nxref: Reactome:R-HSA-5672965 \"RAS GEFs promote RAS nucleotide exchange\"\nxref: Reactome:R-HSA-5686071 \"GRB2-1:SOS1:p-Y-SHC mediated nucleotide exchange of RAS\"\nxref: Reactome:R-HSA-5686318 \"GRB2-1:SOS1:p-3Y-SHC1 mediated nucleotide exchange of RAS\"\nxref: Reactome:R-HSA-5694409 \"Nucleotide exchange on RAB1\"\nxref: Reactome:R-HSA-6807868 \"GBF1 stimulates ARF nucleotide exchange\"\nxref: Reactome:R-HSA-6811414 \"GBF1 stimulates nucleotide exchange on ARF\"\nxref: Reactome:R-HSA-6811418 \"ARFGAPs stimulate ARF GTPase activity at the Golgi membrane\"\nxref: Reactome:R-HSA-6811429 \"RIC1:RGP1 stimulates nucleotide RAB6 nucleotide exchange\"\nxref: Reactome:R-HSA-749453 \"Liganded Gz-activating GPCR acts as a GEF for Gz\"\nxref: Reactome:R-HSA-751029 \"Liganded G12/13-activating GPCR acts as a GEF for G12/13\"\nxref: Reactome:R-HSA-825631 \"Glucagon:GCGR mediates GTP-GDP exchange\"\nxref: Reactome:R-HSA-8848618 \"Activation of RAC1 by the PXN:CRK complex\"\nxref: Reactome:R-HSA-8850041 \"RAB3GAP1:RAB3GAP2 promotes nucleotide exchange on RAB18\"\nxref: Reactome:R-HSA-8851827 \"RAS guanyl nucleotide exchange by MET-bound GRB2:SOS1\"\nxref: Reactome:R-HSA-8851877 \"RAS guanyl nucleotide exchange by SOS1 associated with RANBP9 and MET\"\nxref: Reactome:R-HSA-8851899 \"RAS guanyl nucleotide exchange by SOS1 bound to GRB2, SCH1-2 and MET\"\nxref: Reactome:R-HSA-8875318 \"RAB3 GEFs exchange GTP for GDP on RAB3A\"\nxref: Reactome:R-HSA-8875320 \"RAB5 GEFs exchange GTP for GDP on RAB5\"\nxref: Reactome:R-HSA-8875568 \"RAPGEF1 activates RAP1\"\nxref: Reactome:R-HSA-8875591 \"DOCK7 activates RAC1\"\nxref: Reactome:R-HSA-8876188 \"DENND4s exchange GTP for GDP on RAB10\"\nxref: Reactome:R-HSA-8876190 \"RAB8 GEFs exchange GTP for GDP on RAB8\"\nxref: Reactome:R-HSA-8876191 \"RAB9 GEFs exchange GTP for GDP on RAB9\"\nxref: Reactome:R-HSA-8876193 \"RIC1-RGP1 exchanges GTP for GDP on RAB6\"\nxref: Reactome:R-HSA-8876454 \"DENND3 exchanges GTP for GDP on RAB12\"\nxref: Reactome:R-HSA-8876615 \"RAB13 GEFs exchange GTP for GDP on RAB13\"\nxref: Reactome:R-HSA-8876616 \"DENND6A,B exchange GTP for GDP on RAB14\"\nxref: Reactome:R-HSA-8876837 \"RAB21 GEFs exchange GTP for GDP on RAB21\"\nxref: Reactome:R-HSA-8877308 \"MADD exchanges GTP for GDP on RAB27\"\nxref: Reactome:R-HSA-8877311 \"RAB31 GEFs exchange GTP for GDP on RAB31\"\nxref: Reactome:R-HSA-8877451 \"MON1:CCZ1 exchanges GTP for GDP on RAB7\"\nxref: Reactome:R-HSA-8877475 \"TRAPPC complexes exchange GTP for GDP on RAB1\"\nxref: Reactome:R-HSA-8877612 \"DENND1s exchange GTP for GDP on RAB35\"\nxref: Reactome:R-HSA-8877760 \"HPS1:HPS4 exchange GTP for GDP on RAB32 and RAB38\"\nxref: Reactome:R-HSA-8877813 \"DENND5A,B exchange GTP for GDP on RAB39\"\nxref: Reactome:R-HSA-8877998 \"RAB3GAP1:RAB3GAP2 exchanges GTP for GDP on RAB18\"\nxref: Reactome:R-HSA-8964604 \"CDC42 in GNB/GNG:PAK1:ARHGEF6:CDC42 is activated\"\nxref: Reactome:R-HSA-8980691 \"RHOA GEFs activate RHOA\"\nxref: Reactome:R-HSA-8982637 \"Opsins binds G alpha-t\"\nxref: Reactome:R-HSA-8982640 \"G-alpha(t):G-beta-gamma:Opsins complex dissociates to active G-alpha(t)\"\nxref: Reactome:R-HSA-9013023 \"RHOB GEFs activate RHOB\"\nxref: Reactome:R-HSA-9013109 \"RHOC GEFs activate RHOC\"\nxref: Reactome:R-HSA-9013143 \"RAC1 GEFs activate RAC1\"\nxref: Reactome:R-HSA-9013159 \"CDC42 GEFs activate CDC42\"\nxref: Reactome:R-HSA-9013435 \"RHOD auto-activates\"\nxref: Reactome:R-HSA-9014296 \"RAC2 GEFs activate RAC2\"\nxref: Reactome:R-HSA-9014433 \"RHOG GEFs activate RHOG\"\nxref: Reactome:R-HSA-9017491 \"RHOJ GEFs activate RHOJ\"\nxref: Reactome:R-HSA-9018747 \"RHOQ GEFs activate RHOQ\"\nxref: Reactome:R-HSA-9018768 \"RHOU auto-activates\"\nxref: Reactome:R-HSA-9018804 \"RAC3 GEFs activate RAC3\"\nxref: Reactome:R-HSA-9018817 \"RHOT1 GEFs activate RHOT1\"\nxref: Reactome:R-HSA-9018825 \"RHOT2 GEFs activate RHOT2\"\nxref: Reactome:R-HSA-9026891 \"NTRK2 activates RAS signaling through SHC1\"\nxref: Reactome:R-HSA-9029158 \"EPO:phospho-EPOR:phospho-JAK2:LYN:IRS2:phospho-CRKL:RAPGEF1:GRB2-1:SOS1,phospho-VAV1 mediates exchange of GTP for GDP bound to RAS\"\nxref: Reactome:R-HSA-9032067 \"NTRK2 activates RAS signaling through FRS2\"\nxref: Reactome:R-HSA-9032798 \"DOCK3 activates RAC1\"\nxref: Reactome:R-HSA-9033292 \"NTRK2 and CDK5 promote activation of RAC1 by TIAM1\"\nxref: Reactome:R-HSA-9036301 \"ESTG stimulates GTP exchange on GPER:heterotrimeric G-protein s\"\nxref: Reactome:R-HSA-939265 \"Activation of Rap1 by membrane-associated GEFs\"\nxref: Reactome:R-HSA-9607304 \"SOS1-mediated nucleotide exchange of RAS downstream of FLT3\"\nxref: Reactome:R-HSA-9619803 \"p-S516-ARHGEF7 activates RAC1\"\nxref: Reactome:R-HSA-9624845 \"RCC1 stimulates GDP to GTP exchange on RAN\"\nxref: Reactome:R-HSA-9634418 \"RAS guanyl-nucleotide exchange mediated by SOS1 in complex with GRB2 and ERBB2 homodimer:p-SHC1\"\nxref: Reactome:R-HSA-9639286 \"RRAGC,D exchanges GTP for GDP\"\nxref: Reactome:R-HSA-9640167 \"RRAGA,B exchanges GDP for GTP\"\nxref: Reactome:R-HSA-9660824 \"ADORA2B (in Ade-Rib:ADORA2B:Heterotrimeric G-protein Gs) exchanges GDP for GTP on Gs\"\nxref: Reactome:R-HSA-9664991 \"RAS activation by SOS1 bound to phosphorylated heterodimers of ERBB2 KD mutants\"\nxref: Reactome:R-HSA-9665009 \"RAS activation by SOS1 bound to phosphorylated heterodimers of ERBB2 KD mutants and EGFR\"\nxref: Reactome:R-HSA-9665404 \"RAS guanyl nucleotide exchange mediated by the p-6Y- ERBB2 ECD mutants:EGF:p-6Y-EGFR:p-SHC1:GRB2:SOS1\"\nxref: Reactome:R-HSA-9665408 \"RAS activation by SOS1 bound to phosphorylated heterodimers of ERBB2 ECD mutants and EGFR through GRB2\"\nxref: Reactome:R-HSA-9665700 \"RAS activation by SOS1 bound to phosphorylated heterodimers of ERBB2 TMD/JMD mutants\"\nxref: Reactome:R-HSA-9665707 \"RAS activation by SOS1 bound to phosphorylated heterodimers of ERBB2 TMD/JMD mutants and EGFR\"\nxref: Reactome:R-HSA-9666428 \"DOCK180 exchanges GTP for GDP on RAC1:GDP\"\nxref: Reactome:R-HSA-9666430 \"p-VAV1,2,3 exchanges GTP for GDP on RAC1:GDP\"\nxref: Reactome:R-HSA-9670436 \"p-KIT mutants:GRB2:SOS catalyzes nucleotide exchange on RAS\"\nxref: Reactome:R-HSA-9672163 \"SOS-mediated nucleotide exchange on RAS downstream of PDGFRA extracellular domain dimers\"\nxref: Reactome:R-HSA-9672170 \"SOS-mediated nucleotide exchange of RAS downstream of mutant PDGFR receptors\"\nxref: Reactome:R-HSA-9680385 \"CSF1R-associated SOS1 mediates exchange of GTP for GDP bound to RAS\"\nxref: Reactome:R-HSA-9693111 \"RHOF auto-activates\"\nxref: Reactome:R-HSA-9695853 \"FLT3 mutants:GRB2:SOS1-mediated nucleotide exchange on RAS\"\nxref: Reactome:R-HSA-9703441 \"SOS1-mediated nucleotide exchange of RAS downstream of FLT3 fusion mutants\"\nxref: Reactome:R-HSA-9751201 \"p-VAV1,2,3 exchange 6TGTP for GDP on RAC1\"\nis_a: GO:0030695 ! GTPase regulator activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0005085",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 53422-53638",
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
  "excerpt": "[Term]\nid: GO:0008173\nname: RNA methyltransferase activity\nnamespace: molecular_function\ndef: \"Catalysis of the transfer of a methyl group from a donor to a nucleoside residue in an RNA molecule.\" [GOC:mah]\nxref: Reactome:R-HSA-191784 \"snRNA Cap hypermethylation\"\nis_a: GO:0008168 ! methyltransferase activity\nis_a: GO:0140098 ! catalytic activity, acting on RNA\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008173",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 80322-80330",
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
  "excerpt": "[Term]\nid: GO:0046982\nname: protein heterodimerization activity\nnamespace: molecular_function\ndef: \"Binding to a nonidentical protein to form a heterodimer.\" [GOC:ai]\nsubset: goslim_chembl\nis_a: GO:0046983 ! protein dimerization activity\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0046982",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 282546-282553",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

### Evidence GO4

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO4",
  "excerpt": "[Term]\nid: GO:0051537\nname: 2 iron, 2 sulfur cluster binding\nnamespace: molecular_function\ndef: \"Binding to a 2 iron, 2 sulfur (2Fe-2S) cluster; this cluster consists of two iron atoms, with two inorganic sulfur atoms found between the irons and acting as bridging ligands.\" [GOC:ai, PMID:15952888, Wikipedia:Iron-sulfur_cluster]\nsynonym: \"2 Fe 2 S cluster binding\" EXACT []\nsynonym: \"2 iron, 2 sulphur cluster binding\" EXACT []\nsynonym: \"2Fe-2S cluster binding\" EXACT []\nsynonym: \"diiron disulfide cluster binding\" EXACT []\nsynonym: \"diiron disulphide cluster binding\" EXACT []\nsynonym: \"iron-sulfur cluster 2Fe-2S binding\" EXACT []\nsynonym: \"iron-sulphur cluster 2Fe-2S binding\" EXACT []\nis_a: GO:0051536 ! iron-sulfur cluster binding\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0051537",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 327878-327891",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 40. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
