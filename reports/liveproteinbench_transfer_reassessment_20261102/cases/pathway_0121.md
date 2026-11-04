# pathway_0121

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/pathway_0121.txt)

**Task:** `pathway`  
**Expected answer:** **C** — Alkaloid biosynthesis

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MGFAARPFHIVFSLFVLAGATQALIICPFDSIYQFGDSISDTGNYIRILPNGPAAAAANFPYGITFPGIPTGRFSDGRLIVDFIARVLGLPLLNPYLQQNASFKNGVNFAVGGATALNSSVLAAAGVQIPDIYLIPLSTQLNWFQTYLRSNCSSPTECSKKVQNSLFLIGNIGNNDVNYALPYRTIQEIEAYVPSIAKAVANATREIIRLGGRRIIVPGTFPFGCLPRNLYLFPNGDKDDLGCLRRLNDLSIYFNNLFQQALNSLRIEFPQAVIIYADYYNAFRFLLRNARALGFTSTLQSCCGIGGPYNFDLNRLCGFPGVPVCRNPREYIQWDGFHYTEAAHRHIVQYLIPDILKELKCS

[Multiple Choices]
A. L-histidine from 5-phospho-alpha-D-ribose 1-diphosphate: step 4/9. .
B. Purine metabolism
C. Alkaloid biosynthesis
D. polypeptide chain elongation. .
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

> The sequence-matched UniProt entry annotates the protein's pathway as alkaloid biosynthesis, specifically ajmaline biosynthesis, with experimental evidence linked to a publication. This supports choice C, though the primary study was not independently assessed here.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> Sequence features may support recognizing an enzyme and could help rule out a translation-related protein, but they do not establish that this enzyme acts in alkaloid rather than another metabolic pathway. No specific transferable pathway signature in the supplied sequence meaningfully identifies choice C over the metabolic alternatives.


**Missing item-specific fact**

> The exact protein's substrate or experimentally established role in ajmaline/alkaloid biosynthesis.


**Reason**

> The pathway assignment is supported by reviewer-only annotation, not supplied to the model. General enzyme or family recognition does not by itself determine the pathway-specific role needed to select among these choices.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The matched source annotation supports one offered pathway; the limited sequence-based answerability does not establish that another option is also correct.


### Important caveats

- The source annotation is linked to experimental evidence, but the cited primary study was not independently reviewed.
- The source identity and pathway annotation were reviewer-only information and should not be treated as original model inputs.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "Sequence features may support recognizing an enzyme and could help rule out a translation-related protein, but they do not establish that this enzyme acts in alkaloid rather than another metabolic pathway. No specific transferable pathway signature in the supplied sequence meaningfully identifies choice C over the metabolic alternatives.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The exact protein's substrate or experimentally established role in ajmaline/alkaloid biosynthesis.",
    "reason": "The pathway assignment is supported by reviewer-only annotation, not supplied to the model. General enzyme or family recognition does not by itself determine the pathway-specific role needed to select among these choices."
  },
  "case_id": "pathway_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the protein's pathway as alkaloid biosynthesis, specifically ajmaline biosynthesis, with experimental evidence linked to a publication. This supports choice C, though the primary study was not independently assessed here."
  },
  "important_caveats": [
    "The source annotation is linked to experimental evidence, but the cited primary study was not independently reviewed.",
    "The source identity and pathway annotation were reviewer-only information and should not be treated as original model inputs."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched source annotation supports one offered pathway; the limited sequence-based answerability does not establish that another option is also correct."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "pathway_0121",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates the protein's pathway as alkaloid biosynthesis, specifically ajmaline biosynthesis, with experimental evidence linked to a publication. This supports choice C, though the primary study was not independently assessed here.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "Sequence features may support recognizing an enzyme and could help rule out a translation-related protein, but they do not establish that this enzyme acts in alkaloid rather than another metabolic pathway. No specific transferable pathway signature in the supplied sequence meaningfully identifies choice C over the metabolic alternatives.",
    "missing_item_specific_fact": "The exact protein's substrate or experimentally established role in ajmaline/alkaloid biosynthesis.",
    "reason": "The pathway assignment is supported by reviewer-only annotation, not supplied to the model. General enzyme or family recognition does not by itself determine the pathway-specific role needed to select among these choices."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The matched source annotation supports one offered pathway; the limited sequence-based answerability does not establish that another option is also correct."
  },
  "important_caveats": [
    "The source annotation is linked to experimental evidence, but the cited primary study was not independently reviewed.",
    "The source identity and pathway annotation were reviewer-only information and should not be treated as original model inputs."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry P0DXJ5 (Acetylajmalan esterase 2, EC 3.1.1.80, from Rauvolfia serpentina) explicitly annotates the pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence (ECO:0000269, PubMed:38212296). The sequence matches exactly. The expected answer C ('Alkaloid biosynthesis') is directly confirmed by the database annotation.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence exhibits a clear N-terminal signal peptide (hydrophobic stretch MGFAARPFHIVFSLFVLAGATQALIICPFDSIYQFGDSISDTGNYIRILPNGPAAAAANFPYGITFPGIPTGRFSDGRLIVDFIARVLGLPLLNPYLQQNASFKNGVNFAVGGATALNSSVLAAAGVQIPDIYLIPLSTQLNWFQTYLRSNCSSPTECSKKVQNSLFLIGNIGNNDVNYALPYRTIQEIEAYVPSIAKAVANATREIIRLGG...), indicating secretory/ER localization. The C-terminal region contains motifs consistent with a carboxylesterase domain (GGRRIIVPGTFPFG...GCLRRLNDLSIYFNNLF...GFTSTLQSCCGIGGPYNFDLNRLCGFPGVPVCRNPREYIQWDGFHYTEAAHRHIVQYLIPDILKELKCS), suggesting hydrolytic modification of intermediates. Among the four offered choices: (D) polypeptide chain elongation requires ribosomal elongation factors (EF-Tu/EF-G) with GTPase domains and very different sequences; (A) histidine biosynthesis and (B) purine metabolism involve cytoplasmic enzymes (ATP phosphoribosyltransferase, IMP dehydrogenase, etc.) lacking signal peptides and esterase domains. A plant enzyme with a signal peptide and esterase activity that modifies metabolic intermediates is most consistent with secondary metabolite biosynthesis. Among the offered choices, alkaloid biosynthesis (C) is the only secondary metabolic pathway listed, and plant alkaloid biosynthesis (e.g., monoterpene indole alkaloids in Apocynaceae) commonly involves ER-localized modifying enzymes including esterases. This chain of inference—signal peptide + esterase domain + plant-like composition + elimination of core metabolic choices—meaningfully distinguishes C from A, B, and D using transferable knowledge of plant secondary metabolism enzyme localization and function.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The combination of a signal peptide, carboxylesterase-like domain, and plant-like sequence characteristics allows elimination of the three core-metabolic distractors (histidine biosynthesis, purine metabolism, polypeptide elongation) via general knowledge that these pathways involve cytoplasmic enzymes without secretory targeting. The remaining choice, alkaloid biosynthesis, is the only secondary metabolic pathway offered and is consistent with plant ER-localized modifying enzymes. This is a defensible probabilistic inference from sequence features and family-level knowledge, not requiring recall of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (histidine biosynthesis, purine metabolism, polypeptide chain elongation) describe core metabolic processes whose enzymes are well-characterized cytoplasmic proteins with distinct sequence families (GTPases for elongation factors, transferases/dehydrogenases for biosynthetic steps). None of these would carry a signal peptide or a carboxylesterase domain. Alkaloid biosynthesis is the only offered pathway consistent with a plant secretory esterase modifying intermediates.


### Important caveats

- The specific identification as 'alkaloid biosynthesis' rather than, say, terpenoid or flavonoid biosynthesis relies on knowing that Rauvolfia is a monoterpene indole alkaloid-producing plant and that esterases modify alkaloid intermediates. However, among the four offered choices, alkaloid biosynthesis is the only secondary metabolite pathway, so this specificity is not tested.
- The UniProt annotation is based on a 2024 Nat. Commun. paper (PubMed:38212296) with experimental evidence for function and pathway, lending strong support to the key.
- The protein was only integrated into UniProtKB/Swiss-Prot in June 2025; the benchmark author may have sourced it from the primary paper or a pre-publication database.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence exhibits a clear N-terminal signal peptide (hydrophobic stretch MGFAARPFHIVFSLFVLAGATQALIICPFDSIYQFGDSISDTGNYIRILPNGPAAAAANFPYGITFPGIPTGRFSDGRLIVDFIARVLGLPLLNPYLQQNASFKNGVNFAVGGATALNSSVLAAAGVQIPDIYLIPLSTQLNWFQTYLRSNCSSPTECSKKVQNSLFLIGNIGNNDVNYALPYRTIQEIEAYVPSIAKAVANATREIIRLGG...), indicating secretory/ER localization. The C-terminal region contains motifs consistent with a carboxylesterase domain (GGRRIIVPGTFPFG...GCLRRLNDLSIYFNNLF...GFTSTLQSCCGIGGPYNFDLNRLCGFPGVPVCRNPREYIQWDGFHYTEAAHRHIVQYLIPDILKELKCS), suggesting hydrolytic modification of intermediates. Among the four offered choices: (D) polypeptide chain elongation requires ribosomal elongation factors (EF-Tu/EF-G) with GTPase domains and very different sequences; (A) histidine biosynthesis and (B) purine metabolism involve cytoplasmic enzymes (ATP phosphoribosyltransferase, IMP dehydrogenase, etc.) lacking signal peptides and esterase domains. A plant enzyme with a signal peptide and esterase activity that modifies metabolic intermediates is most consistent with secondary metabolite biosynthesis. Among the offered choices, alkaloid biosynthesis (C) is the only secondary metabolic pathway listed, and plant alkaloid biosynthesis (e.g., monoterpene indole alkaloids in Apocynaceae) commonly involves ER-localized modifying enzymes including esterases. This chain of inference—signal peptide + esterase domain + plant-like composition + elimination of core metabolic choices—meaningfully distinguishes C from A, B, and D using transferable knowledge of plant secondary metabolism enzyme localization and function.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The combination of a signal peptide, carboxylesterase-like domain, and plant-like sequence characteristics allows elimination of the three core-metabolic distractors (histidine biosynthesis, purine metabolism, polypeptide elongation) via general knowledge that these pathways involve cytoplasmic enzymes without secretory targeting. The remaining choice, alkaloid biosynthesis, is the only secondary metabolic pathway offered and is consistent with plant ER-localized modifying enzymes. This is a defensible probabilistic inference from sequence features and family-level knowledge, not requiring recall of this specific protein's annotation."
  },
  "case_id": "pathway_0121",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ5 (Acetylajmalan esterase 2, EC 3.1.1.80, from Rauvolfia serpentina) explicitly annotates the pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence (ECO:0000269, PubMed:38212296). The sequence matches exactly. The expected answer C ('Alkaloid biosynthesis') is directly confirmed by the database annotation."
  },
  "important_caveats": [
    "The specific identification as 'alkaloid biosynthesis' rather than, say, terpenoid or flavonoid biosynthesis relies on knowing that Rauvolfia is a monoterpene indole alkaloid-producing plant and that esterases modify alkaloid intermediates. However, among the four offered choices, alkaloid biosynthesis is the only secondary metabolite pathway, so this specificity is not tested.",
    "The UniProt annotation is based on a 2024 Nat. Commun. paper (PubMed:38212296) with experimental evidence for function and pathway, lending strong support to the key.",
    "The protein was only integrated into UniProtKB/Swiss-Prot in June 2025; the benchmark author may have sourced it from the primary paper or a pre-publication database."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (histidine biosynthesis, purine metabolism, polypeptide chain elongation) describe core metabolic processes whose enzymes are well-characterized cytoplasmic proteins with distinct sequence families (GTPases for elongation factors, transferases/dehydrogenases for biosynthetic steps). None of these would carry a signal peptide or a carboxylesterase domain. Alkaloid biosynthesis is the only offered pathway consistent with a plant secretory esterase modifying intermediates."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "pathway_0121",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry P0DXJ5 (Acetylajmalan esterase 2, EC 3.1.1.80, from Rauvolfia serpentina) explicitly annotates the pathway as 'Alkaloid biosynthesis; ajmaline biosynthesis' with experimental evidence (ECO:0000269, PubMed:38212296). The sequence matches exactly. The expected answer C ('Alkaloid biosynthesis') is directly confirmed by the database annotation.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence exhibits a clear N-terminal signal peptide (hydrophobic stretch MGFAARPFHIVFSLFVLAGATQALIICPFDSIYQFGDSISDTGNYIRILPNGPAAAAANFPYGITFPGIPTGRFSDGRLIVDFIARVLGLPLLNPYLQQNASFKNGVNFAVGGATALNSSVLAAAGVQIPDIYLIPLSTQLNWFQTYLRSNCSSPTECSKKVQNSLFLIGNIGNNDVNYALPYRTIQEIEAYVPSIAKAVANATREIIRLGG...), indicating secretory/ER localization. The C-terminal region contains motifs consistent with a carboxylesterase domain (GGRRIIVPGTFPFG...GCLRRLNDLSIYFNNLF...GFTSTLQSCCGIGGPYNFDLNRLCGFPGVPVCRNPREYIQWDGFHYTEAAHRHIVQYLIPDILKELKCS), suggesting hydrolytic modification of intermediates. Among the four offered choices: (D) polypeptide chain elongation requires ribosomal elongation factors (EF-Tu/EF-G) with GTPase domains and very different sequences; (A) histidine biosynthesis and (B) purine metabolism involve cytoplasmic enzymes (ATP phosphoribosyltransferase, IMP dehydrogenase, etc.) lacking signal peptides and esterase domains. A plant enzyme with a signal peptide and esterase activity that modifies metabolic intermediates is most consistent with secondary metabolite biosynthesis. Among the offered choices, alkaloid biosynthesis (C) is the only secondary metabolic pathway listed, and plant alkaloid biosynthesis (e.g., monoterpene indole alkaloids in Apocynaceae) commonly involves ER-localized modifying enzymes including esterases. This chain of inference—signal peptide + esterase domain + plant-like composition + elimination of core metabolic choices—meaningfully distinguishes C from A, B, and D using transferable knowledge of plant secondary metabolism enzyme localization and function.",
    "missing_item_specific_fact": "",
    "reason": "The combination of a signal peptide, carboxylesterase-like domain, and plant-like sequence characteristics allows elimination of the three core-metabolic distractors (histidine biosynthesis, purine metabolism, polypeptide elongation) via general knowledge that these pathways involve cytoplasmic enzymes without secretory targeting. The remaining choice, alkaloid biosynthesis, is the only secondary metabolic pathway offered and is consistent with plant ER-localized modifying enzymes. This is a defensible probabilistic inference from sequence features and family-level knowledge, not requiring recall of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (histidine biosynthesis, purine metabolism, polypeptide chain elongation) describe core metabolic processes whose enzymes are well-characterized cytoplasmic proteins with distinct sequence families (GTPases for elongation factors, transferases/dehydrogenases for biosynthetic steps). None of these would carry a signal peptide or a carboxylesterase domain. Alkaloid biosynthesis is the only offered pathway consistent with a plant secretory esterase modifying intermediates."
  },
  "important_caveats": [
    "The specific identification as 'alkaloid biosynthesis' rather than, say, terpenoid or flavonoid biosynthesis relies on knowing that Rauvolfia is a monoterpene indole alkaloid-producing plant and that esterases modify alkaloid intermediates. However, among the four offered choices, alkaloid biosynthesis is the only secondary metabolite pathway, so this specificity is not tested.",
    "The UniProt annotation is based on a 2024 Nat. Commun. paper (PubMed:38212296) with experimental evidence for function and pathway, lending strong support to the key.",
    "The protein was only integrated into UniProtKB/Swiss-Prot in June 2025; the benchmark author may have sourced it from the primary paper or a pre-publication database."
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
  "benchmark_sequence_length": 362,
  "benchmark_sequence_sha256": "d8e428e5582a9f9deeaba106d2f89f040034c96a765f282c6106bf8a9dc8a981",
  "current_entry_audit": {
    "entryVersion": 4,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2025-06-18",
    "sequenceVersion": 1
  },
  "current_record_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 362,
  "current_source_sequence_sha256": "d8e428e5582a9f9deeaba106d2f89f040034c96a765f282c6106bf8a9dc8a981",
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
  "requested_accession": "P0DXJ5",
  "selected_historical_entry_version": 2,
  "selected_historical_record_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "selected_historical_source_sequence_length": 362,
  "selected_historical_source_sequence_sha256": "d8e428e5582a9f9deeaba106d2f89f040034c96a765f282c6106bf8a9dc8a981",
  "selected_historical_version": {
    "accession": "P0DXJ5",
    "database": "Swiss-Prot",
    "entryVersion": 2,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "AAE2_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"P0DXJ5\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":4,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2025-06-18\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"flag\":\"Precursor\",\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"3.1.1.80\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Acetylajmalan esterase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"RsAAE2\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis; ajmaline biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/3",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/P0DXJ5.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:29:33.413705+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "e74045ec75b84a761a8c28c824548a403267850c5218348997bbacf67e779d70",
  "url": "https://rest.uniprot.org/uniprotkb/P0DXJ5.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H1",
  "excerpt": "ID   AAE2_RAUSE              Reviewed;         362 AA.\nAC   P0DXJ5;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   18-JUN-2025, sequence version 1.\nDT   28-JAN-2026, entry version 2.\nDE   RecName: Full=Acetylajmalan esterase 2 {ECO:0000303|PubMed:38212296};\nDE            Short=RsAAE2 {ECO:0000303|PubMed:38212296};\nDE            EC=3.1.1.80 {ECO:0000269|PubMed:38212296};\nDE   Flags: Precursor;\nGN   Name=AAE2 {ECO:0000303|PubMed:38212296};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H2",
  "excerpt": "RN   [1]\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE\nRP   SPECIFICITY, AND BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 17-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2)

```json
{
  "entry_version": 2,
  "evidence_id": "H3",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.\nCC       {ECO:0000269|PubMed:38212296}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:29:35.241829+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 45-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "fd05ebf51e29b1b8ffb9eabf52681e84944476cb3e9a9d3ef689fd184b6b5e95",
  "url": "https://rest.uniprot.org/unisave/P0DXJ5?format=txt&versions=2"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/pathway.json), zero-based source row 121. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
