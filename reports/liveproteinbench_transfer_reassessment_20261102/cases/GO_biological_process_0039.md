# GO_biological_process_0039

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0039.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **D** — triterpenoid biosynthetic process

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MVLSRLDFPSDFIFGSGTSASQVEGAALEDGKTSTAFEGFLTRMSGNDLSKGVEGYYKYKEDVQLMVQTGLDAYRFSISWSRLIPGGKGPVNPKGLQYYNNFIDELIKNGIQPHVTLLHFDIPDTLMTAYNGLKGQEFVEDFTAFADVCFKEFGDRVLYWTTVNEANNFASLTLDEGNFMPSTEPYIRGHNIILAHASAVKLYREKYKKTQNGFIGLNLYASWYFPETDDEQDSIAAQRAIDFTIGWIMQPLIYGEYPETLKKQVGERLPTFTKEESTFVKNSFDFIGVNCYVGTAVKDDPDSCNSKNKTIITDMSAKLSPKGELGGAYMKGLLEYFKRDYGNPPIYIQENGYWTPRELGVNDASRIEYHTASLASMHDAMKNGANVKGYFQWSFLDLLEVFKYSYGLYHVDLEDPTRERRPKASANWYAEFLKGCATSNGNAKVETPL

[Multiple Choices]
A. mitophagy
B. response to insulin
C. response to bacterium
D. triterpenoid biosynthetic process
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Gene Ontology (GO) Biological Process Prediction, which is to predict the primary biological process a given protein participates in, as defined by the Gene Ontology (GO) 'Biological Process' branch. A biological process is a series of molecular events that accomplishes a larger biological program, such as cell division or signal transduction. Based on the provided protein sequence, you must select the option that best describes the overall biological objective to which the protein contributes.. The inputs provided by the user for this task include:

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

> The sequence-matched record describes an experimentally supported role in triterpene saponin biosynthesis, specifically adding a sugar to a triterpene-derived substrate. The GO annotation also assigns triterpenoid biosynthetic process, supporting D. This is more than a computational family annotation, though the underlying experiment was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [C9](#evidence-c9).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence is compatible with a soluble glycosyl-hydrolase-like enzyme, which makes biosynthetic roles more plausible than mitophagy or insulin response. But that broad enzyme-family inference does not establish its substrate or distinguish triterpenoid biosynthesis from other possible roles, including a response to bacteria.


**Missing item-specific fact**

> The protein's particular substrate and role in a triterpene-saponin pathway, which are not specified by the sequence or original context.


**Reason**

> Selecting D over the plausible alternatives requires the target-specific functional assignment; recognizing a broad enzyme family does not meaningfully determine this pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence alone leaves the pathway unresolved, but no second option is independently established as a defensible annotation for this protein.


### Important caveats

- The reviewer-only source identifies the sequence and reports experimental support; this information was not available in the original input.
- The enzyme acts on a triterpene-derived saponin intermediate, so the process label describes its pathway context rather than implying that this enzyme builds the triterpene scaffold.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is compatible with a soluble glycosyl-hydrolase-like enzyme, which makes biosynthetic roles more plausible than mitophagy or insulin response. But that broad enzyme-family inference does not establish its substrate or distinguish triterpenoid biosynthesis from other possible roles, including a response to bacteria.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein's particular substrate and role in a triterpene-saponin pathway, which are not specified by the sequence or original context.",
    "reason": "Selecting D over the plausible alternatives requires the target-specific functional assignment; recognizing a broad enzyme family does not meaningfully determine this pathway."
  },
  "case_id": "GO_biological_process_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C9"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched record describes an experimentally supported role in triterpene saponin biosynthesis, specifically adding a sugar to a triterpene-derived substrate. The GO annotation also assigns triterpenoid biosynthetic process, supporting D. This is more than a computational family annotation, though the underlying experiment was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only source identifies the sequence and reports experimental support; this information was not available in the original input.",
    "The enzyme acts on a triterpene-derived saponin intermediate, so the process label describes its pathway context rather than implying that this enzyme builds the triterpene scaffold."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone leaves the pathway unresolved, but no second option is independently established as a defensible annotation for this protein."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched record describes an experimentally supported role in triterpene saponin biosynthesis, specifically adding a sugar to a triterpene-derived substrate. The GO annotation also assigns triterpenoid biosynthetic process, supporting D. This is more than a computational family annotation, though the underlying experiment was not independently reviewed here.",
    "evidence_ids": ["C5", "C9"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence is compatible with a soluble glycosyl-hydrolase-like enzyme, which makes biosynthetic roles more plausible than mitophagy or insulin response. But that broad enzyme-family inference does not establish its substrate or distinguish triterpenoid biosynthesis from other possible roles, including a response to bacteria.",
    "missing_item_specific_fact": "The protein's particular substrate and role in a triterpene-saponin pathway, which are not specified by the sequence or original context.",
    "reason": "Selecting D over the plausible alternatives requires the target-specific functional assignment; recognizing a broad enzyme family does not meaningfully determine this pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence alone leaves the pathway unresolved, but no second option is independently established as a defensible annotation for this protein."
  },
  "important_caveats": [
    "The reviewer-only source identifies the sequence and reports experimental support; this information was not available in the original input.",
    "The enzyme acts on a triterpene-derived saponin intermediate, so the process label describes its pathway context rather than implying that this enzyme builds the triterpene scaffold."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0AAW1I778, GH1_SAPOF) carries GO:0016104 (triterpenoid biosynthetic process) with IDA:UniProtKB evidence (C9/H7), and the FUNCTION comment (C5/H3) explicitly describes the protein as a component of the oleanane-type triterpene saponin biosynthetic pathway. The PATHWAY comment (C6/H4) confirms 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' The protein is a beta-glycosidase (EC 2.4.1.-) that elongates the C-28 sugar chain on triterpenoid saponin intermediates, which is correctly classified under triterpenoid biosynthetic process. Evidence code IDA indicates direct experimental support from PubMed:39043959.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C9](#evidence-c9), [C8](#evidence-c8), [H3](#evidence-h3), [H4](#evidence-h4), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable GH1 (glycosyl hydrolase family 1) motifs: a 'GSGT' region near the N-terminus, 'NEANN' around position ~150, and 'NACYVGT' around position ~300, all hallmarks of the GH1 (β/α)8 TIM-barrel fold. The N-terminal hydrophobic stretch ('MVLSRLDFPSDFIFGSGTSASQ') is consistent with a secretory signal peptide, placing the enzyme in the ER/Golgi secretory pathway. The amino-acid composition (high Ser/Thr/Gly, plant-typical bias) suggests a plant protein. From transferable knowledge of other plant proteins: (1) Mitophagy (A) involves mitochondrial membrane proteins (PINK1, Parkin, BNIP3) and is not a plant GH1 function. (2) Response to insulin (B) is an animal signaling pathway (receptor tyrosine kinases, PI3K/Akt); a plant secretory glycosidase does not fit. (3) Response to bacterium (C) is a stimulus-response GO term typically assigned to NLRs, PR proteins, or MAPK components, not to constitutive secretory glycosidases. (4) In plant specialized metabolism, particularly in Caryophyllales and other lineages rich in triterpenoid saponins, secretory GH1 enzymes are well-documented components of saponin/triterpenoid biosynthetic cascades (e.g., glycosidases trimming or modifying sugar chains on triterpenoid aglycones in Medicago, Panax, and related species). A constitutive secretory-pathway glycosidase in a plant is far more consistent with a biosynthetic role in secondary metabolism (D) than with a stimulus-triggered defense response (C). This family-level and pathway-context inference meaningfully distinguishes D from the other three options.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The GH1 family motifs, secretory signal peptide, and plant-like composition are extractable from the sequence. Transferable knowledge that plant secretory GH1 enzymes participate in triterpenoid/saponin biosynthetic pathways (learned from homologs in Medicago, Panax, etc.) and that 'response to bacterium' denotes stimulus-triggered signaling rather than constitutive biosynthesis provides a credible basis to select D. The argument is probabilistic but meaningfully discriminates among the four offered choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options A (mitophagy) and B (response to insulin) are clearly incompatible with a plant secretory GH1 enzyme. Option C (response to bacterium) is a stimulus-response term that does not match a constitutive secretory glycosidase. Only D (triterpenoid biosynthetic process) is consistent with the recognized family, subcellular localization, and plant specialized-metabolism context. No two options are equally defensible.


### Important caveats

- The protein is named 'Glycosyl hydrolase-like protein 1' with EC 2.4.1.-, indicating glycosidase/glycosyltransferase activity; its classification under 'triterpenoid biosynthetic process' reflects its pathway role (modifying sugar chains on triterpenoid intermediates) rather than a direct triterpenoid-synthesizing catalytic step.
- The GH1 family is very large; sequence recognition alone identifies the fold but not the specific substrate or pathway. The inference to triterpenoid biosynthesis relies on plant secretory-pathway context and knowledge of analogous enzymes in other plant species.
- The UniProt entry was first public on 2025-06-18; the benchmark author's source snapshot is unknown. The sequence match is confirmed across both current and historical (v5) records.
- GO:0016135 (saponin biosynthetic process) is also annotated with IDA evidence and is a more specific term; the question's option D uses the broader parent term GO:0016104, which is also directly annotated.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable GH1 (glycosyl hydrolase family 1) motifs: a 'GSGT' region near the N-terminus, 'NEANN' around position ~150, and 'NACYVGT' around position ~300, all hallmarks of the GH1 (β/α)8 TIM-barrel fold. The N-terminal hydrophobic stretch ('MVLSRLDFPSDFIFGSGTSASQ') is consistent with a secretory signal peptide, placing the enzyme in the ER/Golgi secretory pathway. The amino-acid composition (high Ser/Thr/Gly, plant-typical bias) suggests a plant protein. From transferable knowledge of other plant proteins: (1) Mitophagy (A) involves mitochondrial membrane proteins (PINK1, Parkin, BNIP3) and is not a plant GH1 function. (2) Response to insulin (B) is an animal signaling pathway (receptor tyrosine kinases, PI3K/Akt); a plant secretory glycosidase does not fit. (3) Response to bacterium (C) is a stimulus-response GO term typically assigned to NLRs, PR proteins, or MAPK components, not to constitutive secretory glycosidases. (4) In plant specialized metabolism, particularly in Caryophyllales and other lineages rich in triterpenoid saponins, secretory GH1 enzymes are well-documented components of saponin/triterpenoid biosynthetic cascades (e.g., glycosidases trimming or modifying sugar chains on triterpenoid aglycones in Medicago, Panax, and related species). A constitutive secretory-pathway glycosidase in a plant is far more consistent with a biosynthetic role in secondary metabolism (D) than with a stimulus-triggered defense response (C). This family-level and pathway-context inference meaningfully distinguishes D from the other three options.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The GH1 family motifs, secretory signal peptide, and plant-like composition are extractable from the sequence. Transferable knowledge that plant secretory GH1 enzymes participate in triterpenoid/saponin biosynthetic pathways (learned from homologs in Medicago, Panax, etc.) and that 'response to bacterium' denotes stimulus-triggered signaling rather than constitutive biosynthesis provides a credible basis to select D. The argument is probabilistic but meaningfully discriminates among the four offered choices."
  },
  "case_id": "GO_biological_process_0039",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C9",
      "C8",
      "H3",
      "H4",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0AAW1I778, GH1_SAPOF) carries GO:0016104 (triterpenoid biosynthetic process) with IDA:UniProtKB evidence (C9/H7), and the FUNCTION comment (C5/H3) explicitly describes the protein as a component of the oleanane-type triterpene saponin biosynthetic pathway. The PATHWAY comment (C6/H4) confirms 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' The protein is a beta-glycosidase (EC 2.4.1.-) that elongates the C-28 sugar chain on triterpenoid saponin intermediates, which is correctly classified under triterpenoid biosynthetic process. Evidence code IDA indicates direct experimental support from PubMed:39043959."
  },
  "important_caveats": [
    "The protein is named 'Glycosyl hydrolase-like protein 1' with EC 2.4.1.-, indicating glycosidase/glycosyltransferase activity; its classification under 'triterpenoid biosynthetic process' reflects its pathway role (modifying sugar chains on triterpenoid intermediates) rather than a direct triterpenoid-synthesizing catalytic step.",
    "The GH1 family is very large; sequence recognition alone identifies the fold but not the specific substrate or pathway. The inference to triterpenoid biosynthesis relies on plant secretory-pathway context and knowledge of analogous enzymes in other plant species.",
    "The UniProt entry was first public on 2025-06-18; the benchmark author's source snapshot is unknown. The sequence match is confirmed across both current and historical (v5) records.",
    "GO:0016135 (saponin biosynthetic process) is also annotated with IDA evidence and is a more specific term; the question's option D uses the broader parent term GO:0016104, which is also directly annotated."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (mitophagy) and B (response to insulin) are clearly incompatible with a plant secretory GH1 enzyme. Option C (response to bacterium) is a stimulus-response term that does not match a constitutive secretory glycosidase. Only D (triterpenoid biosynthetic process) is consistent with the recognized family, subcellular localization, and plant specialized-metabolism context. No two options are equally defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0039",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0AAW1I778, GH1_SAPOF) carries GO:0016104 (triterpenoid biosynthetic process) with IDA:UniProtKB evidence (C9/H7), and the FUNCTION comment (C5/H3) explicitly describes the protein as a component of the oleanane-type triterpene saponin biosynthetic pathway. The PATHWAY comment (C6/H4) confirms 'Secondary metabolite biosynthesis; terpenoid biosynthesis.' The protein is a beta-glycosidase (EC 2.4.1.-) that elongates the C-28 sugar chain on triterpenoid saponin intermediates, which is correctly classified under triterpenoid biosynthetic process. Evidence code IDA indicates direct experimental support from PubMed:39043959.",
    "evidence_ids": ["C5", "C6", "C9", "C8", "H3", "H4", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable GH1 (glycosyl hydrolase family 1) motifs: a 'GSGT' region near the N-terminus, 'NEANN' around position ~150, and 'NACYVGT' around position ~300, all hallmarks of the GH1 (β/α)8 TIM-barrel fold. The N-terminal hydrophobic stretch ('MVLSRLDFPSDFIFGSGTSASQ') is consistent with a secretory signal peptide, placing the enzyme in the ER/Golgi secretory pathway. The amino-acid composition (high Ser/Thr/Gly, plant-typical bias) suggests a plant protein. From transferable knowledge of other plant proteins: (1) Mitophagy (A) involves mitochondrial membrane proteins (PINK1, Parkin, BNIP3) and is not a plant GH1 function. (2) Response to insulin (B) is an animal signaling pathway (receptor tyrosine kinases, PI3K/Akt); a plant secretory glycosidase does not fit. (3) Response to bacterium (C) is a stimulus-response GO term typically assigned to NLRs, PR proteins, or MAPK components, not to constitutive secretory glycosidases. (4) In plant specialized metabolism, particularly in Caryophyllales and other lineages rich in triterpenoid saponins, secretory GH1 enzymes are well-documented components of saponin/triterpenoid biosynthetic cascades (e.g., glycosidases trimming or modifying sugar chains on triterpenoid aglycones in Medicago, Panax, and related species). A constitutive secretory-pathway glycosidase in a plant is far more consistent with a biosynthetic role in secondary metabolism (D) than with a stimulus-triggered defense response (C). This family-level and pathway-context inference meaningfully distinguishes D from the other three options.",
    "missing_item_specific_fact": "",
    "reason": "The GH1 family motifs, secretory signal peptide, and plant-like composition are extractable from the sequence. Transferable knowledge that plant secretory GH1 enzymes participate in triterpenoid/saponin biosynthetic pathways (learned from homologs in Medicago, Panax, etc.) and that 'response to bacterium' denotes stimulus-triggered signaling rather than constitutive biosynthesis provides a credible basis to select D. The argument is probabilistic but meaningfully discriminates among the four offered choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options A (mitophagy) and B (response to insulin) are clearly incompatible with a plant secretory GH1 enzyme. Option C (response to bacterium) is a stimulus-response term that does not match a constitutive secretory glycosidase. Only D (triterpenoid biosynthetic process) is consistent with the recognized family, subcellular localization, and plant specialized-metabolism context. No two options are equally defensible."
  },
  "important_caveats": [
    "The protein is named 'Glycosyl hydrolase-like protein 1' with EC 2.4.1.-, indicating glycosidase/glycosyltransferase activity; its classification under 'triterpenoid biosynthetic process' reflects its pathway role (modifying sugar chains on triterpenoid intermediates) rather than a direct triterpenoid-synthesizing catalytic step.",
    "The GH1 family is very large; sequence recognition alone identifies the fold but not the specific substrate or pathway. The inference to triterpenoid biosynthesis relies on plant secretory-pathway context and knowledge of analogous enzymes in other plant species.",
    "The UniProt entry was first public on 2025-06-18; the benchmark author's source snapshot is unknown. The sequence match is confirmed across both current and historical (v5) records.",
    "GO:0016135 (saponin biosynthetic process) is also annotated with IDA evidence and is a more specific term; the question's option D uses the broader parent term GO:0016104, which is also directly annotated."
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
  "benchmark_sequence_length": 449,
  "benchmark_sequence_sha256": "dbde96162e07c4bc2cf12569813f95c3ba7a3a98e55757ed498dcdc9af566214",
  "current_entry_audit": {
    "entryVersion": 7,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 449,
  "current_source_sequence_sha256": "dbde96162e07c4bc2cf12569813f95c3ba7a3a98e55757ed498dcdc9af566214",
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
  "requested_accession": "A0AAW1I778",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "c7ca0832007e22d89941a95ac8b35a4ce0c5a8531725045ef236385b2578847f",
  "selected_historical_source_sequence_length": 449,
  "selected_historical_source_sequence_sha256": "dbde96162e07c4bc2cf12569813f95c3ba7a3a98e55757ed498dcdc9af566214",
  "selected_historical_version": {
    "accession": "A0AAW1I778",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GH1_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1I778\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:26:30.134986+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1I778.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":7,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:26:30.134986+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1I778.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:26:30.134986+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1I778.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"2.4.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Glycosyl hydrolase-like protein 1\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoGH1\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:26:30.134986+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1I778.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Component of the oleanane-type triterpene saponins (e.g. saponarioside A and saponarioside B) biosynthetic pathway, leading to the production of natural products with detergent properties used as traditional sources of soap (PubMed:39043959). Beta-glycosidase that catalyzes the transfer of a modified glucose moiety to QA-triFRXX to produce QA-triF(Q)RXX via the elongation of the C-28 sugar chain with a D-quinovose (PubMed:39043959)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:26:30.134986+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1I778.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Secondary metabolite biosynthesis; terpenoid biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:26:30.134986+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1I778.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0005975\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:carbohydrate metabolic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:InterPro\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/9",
  "retrieved_utc": "2026-11-02T04:26:30.134986+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1I778.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"id\":\"GO:0016135\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:saponin biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-02T04:26:30.134986+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1I778.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"id\":\"GO:0016104\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:triterpenoid biosynthetic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-02T04:26:30.134986+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1I778.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1I778.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48151.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"SUBCELLULAR LOCATION\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:26:30.134986+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "d22cd9c7375b6893468cf4fe1337927b3c7c8e643c1da67a1d632f6b833638e0",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1I778.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   GH1_SAPOF               Reviewed;         449 AA.\nAC   A0AAW1I778;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=Glycosyl hydrolase-like protein 1 {ECO:0000303|PubMed:39043959};\nDE            Short=SoGH1 {ECO:0000303|PubMed:39043959};\nDE            EC=2.4.1.- {ECO:0000269|PubMed:39043959};\nGN   Name=GH1 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11054913m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_10G213900 {ECO:0000312|EMBL:KAK9684494.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:36.143043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c7ca0832007e22d89941a95ac8b35a4ce0c5a8531725045ef236385b2578847f",
  "url": "https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48151.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, SUBCELLULAR LOCATION, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:36.143043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c7ca0832007e22d89941a95ac8b35a4ce0c5a8531725045ef236385b2578847f",
  "url": "https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Component of the oleanane-type triterpene saponins (e.g.\nCC       saponarioside A and saponarioside B) biosynthetic pathway, leading to\nCC       the production of natural products with detergent properties used as\nCC       traditional sources of soap (PubMed:39043959). Beta-glycosidase that\nCC       catalyzes the transfer of a modified glucose moiety to QA-triFRXX to\nCC       produce QA-triF(Q)RXX via the elongation of the C-28 sugar chain with a\nCC       D-quinovose (PubMed:39043959). {ECO:0000269|PubMed:39043959}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:36.143043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c7ca0832007e22d89941a95ac8b35a4ce0c5a8531725045ef236385b2578847f",
  "url": "https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H4",
  "excerpt": "CC   -!- PATHWAY: Secondary metabolite biosynthesis; terpenoid biosynthesis.\nCC       {ECO:0000269|PubMed:39043959}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:36.143043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 41-42",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c7ca0832007e22d89941a95ac8b35a4ce0c5a8531725045ef236385b2578847f",
  "url": "https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0005975; P:carbohydrate metabolic process; IEA:InterPro.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:36.143043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 67-67",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c7ca0832007e22d89941a95ac8b35a4ce0c5a8531725045ef236385b2578847f",
  "url": "https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0016135; P:saponin biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:36.143043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c7ca0832007e22d89941a95ac8b35a4ce0c5a8531725045ef236385b2578847f",
  "url": "https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0016104; P:triterpenoid biosynthetic process; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:26:36.143043+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c7ca0832007e22d89941a95ac8b35a4ce0c5a8531725045ef236385b2578847f",
  "url": "https://rest.uniprot.org/unisave/A0AAW1I778?format=txt&versions=5"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0000423\nname: mitophagy\nnamespace: biological_process\ndef: \"The selective autophagy process in which a mitochondrion is degraded by macroautophagy.\" [PMID:15798367]\ncomment: Note that this terms refers to the macroautophagy process and is named by common usage. Be aware that there are a separate micromitophagy and mitophagy by induced vacuole formation processes.\nsynonym: \"macromitophagy\" EXACT []\nxref: Reactome:R-HSA-5205647 \"Mitophagy\"\nxref: Wikipedia:Mitophagy\nis_a: GO:0000422 ! autophagy of mitochondrion\nis_a: GO:0016236 ! macroautophagy\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0000423",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 4330-4341",
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
  "excerpt": "[Term]\nid: GO:0009617\nname: response to bacterium\nnamespace: biological_process\nalt_id: GO:0009618\nalt_id: GO:0009680\ndef: \"Any process that results in a change in state or activity of a cell or an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a stimulus from a bacterium.\" [GOC:hb]\nsynonym: \"response to bacteria\" EXACT []\nxref: Reactome:R-HSA-9824439 \"Bacterial Infection Pathways\"\nis_a: GO:0051707 ! response to other organism\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009617",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 97970-97980",
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
  "excerpt": "[Term]\nid: GO:0016104\nname: triterpenoid biosynthetic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways resulting in the formation of triterpenoid compounds, terpenoids with six isoprene units.\" [GOC:curators]\nsynonym: \"triterpene biosynthesis\" NARROW []\nsynonym: \"triterpene biosynthetic process\" NARROW []\nsynonym: \"triterpenoid anabolism\" EXACT []\nsynonym: \"triterpenoid biosynthesis\" EXACT []\nsynonym: \"triterpenoid formation\" EXACT []\nsynonym: \"triterpenoid synthesis\" EXACT []\nis_a: GO:0006722 ! triterpenoid metabolic process\nis_a: GO:0016114 ! terpenoid biosynthetic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016104",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 123487-123500",
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
  "excerpt": "[Term]\nid: GO:0032868\nname: response to insulin\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell or an organism (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of an insulin stimulus. Insulin is a polypeptide hormone produced by the islets of Langerhans of the pancreas in mammals, and by the homologous organs of other organisms.\" [GOC:mah, ISBN:0198506732]\nsynonym: \"response to insulin stimulus\" EXACT [GOC:dos]\nis_a: GO:0043434 ! response to peptide hormone\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0032868",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 191290-191297",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 39. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
