# GO_biological_process_0003

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_biological_process_0003.txt)

**Task:** `GO_biological_process`  
**Expected answer:** **B** — alkaloid metabolic process

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MAGKSPEEQHPVKAYGWAATDSSGILSPFKFSRRATGDHDVRVKILYAGVCHSDLQSARNDMGCFTYPLVPGFETVGTATEVGSKVTKVKVGDKVAVGIMVGSCGKCDECVNDRECYCPEVITSYGRIDHDGTPTYGGFSSETVANEKFVFCFPEKLPMAAGAPLLNAGVSVYSAMRFYGLDKPGMHLGVVGLGGLGHLAVKFAKAFGVKVTVISTSTSKKGEAINDLGADAFLVSTDAEQMQAGSGTLDGILDTVPVVHPIEALLGLLKNHTKLVLVGATMGSFELPILPLGVGRKSVVSTIGGSTKETQEMLDFAAEHDITASVEIIPMDYVNTAMERIEKGDVRYRFVIDIGNTLTPPES

[Multiple Choices]
A. positive regulation of bone mineralization
B. alkaloid metabolic process
C. venom-mediated fibrinolysis
D. cellular response to topologically incorrect protein
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

> The matching-sequence UniProt entry describes the protein as an alcohol dehydrogenase involved in ajmaline-type alkaloid biosynthesis and cites experimental evidence for its function and pathway. The GO annotation itself is computationally assigned, but it agrees with that function annotation.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a soluble enzyme: it is a compact globular protein with conserved catalytic/cofactor-binding features, rather than an obvious secreted venom protein, mineralization regulator, or protein-quality-control sensor. Transferable knowledge that alcohol-dehydrogenase-like enzymes commonly catalyze metabolic reactions makes the metabolic-process option a credible choice among these alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence and choices support a probabilistic distinction for B without requiring recall of this exact protein's database record. The sequence alone does not establish alkaloid specificity, so this is a broad inference rather than a proof of the precise pathway.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> No other offered choice is comparably supported by the sequence's enzyme-like character and the alternatives provided.


### Important caveats

- The exact role in ajmaline biosynthesis is not inferable with certainty from the sequence alone.
- The GO annotation cited here is electronically inferred; the separate function and pathway annotations cite experimental evidence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme: it is a compact globular protein with conserved catalytic/cofactor-binding features, rather than an obvious secreted venom protein, mineralization regulator, or protein-quality-control sensor. Transferable knowledge that alcohol-dehydrogenase-like enzymes commonly catalyze metabolic reactions makes the metabolic-process option a credible choice among these alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices support a probabilistic distinction for B without requiring recall of this exact protein's database record. The sequence alone does not establish alkaloid specificity, so this is a broad inference rather than a proof of the precise pathway."
  },
  "case_id": "GO_biological_process_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H5",
      "H6",
      "H7"
    ],
    "judgment": "supported",
    "reason": "The matching-sequence UniProt entry describes the protein as an alcohol dehydrogenase involved in ajmaline-type alkaloid biosynthesis and cites experimental evidence for its function and pathway. The GO annotation itself is computationally assigned, but it agrees with that function annotation."
  },
  "important_caveats": [
    "The exact role in ajmaline biosynthesis is not inferable with certainty from the sequence alone.",
    "The GO annotation cited here is electronically inferred; the separate function and pathway annotations cite experimental evidence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence's enzyme-like character and the alternatives provided."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_biological_process_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The matching-sequence UniProt entry describes the protein as an alcohol dehydrogenase involved in ajmaline-type alkaloid biosynthesis and cites experimental evidence for its function and pathway. The GO annotation itself is computationally assigned, but it agrees with that function annotation.",
    "evidence_ids": ["C5", "C6", "C7", "H5", "H6", "H7"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a soluble enzyme: it is a compact globular protein with conserved catalytic/cofactor-binding features, rather than an obvious secreted venom protein, mineralization regulator, or protein-quality-control sensor. Transferable knowledge that alcohol-dehydrogenase-like enzymes commonly catalyze metabolic reactions makes the metabolic-process option a credible choice among these alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The sequence and choices support a probabilistic distinction for B without requiring recall of this exact protein's database record. The sequence alone does not establish alkaloid specificity, so this is a broad inference rather than a proof of the precise pathway."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "No other offered choice is comparably supported by the sequence's enzyme-like character and the alternatives provided."
  },
  "important_caveats": [
    "The exact role in ajmaline biosynthesis is not inferable with certainty from the sequence alone.",
    "The GO annotation cited here is electronically inferred; the separate function and pathway annotations cite experimental evidence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The protein is 1,2-Dihydrovomilenine reductase (RsDHVR) from Rauvolfia serpentina, an alcohol dehydrogenase experimentally demonstrated (ECO:0000269, PubMed:12391554, 26715562, 38212296) to catalyze a step in ajmaline-type monoterpenoid indole alkaloid biosynthesis. The UniProt PATHWAY comment reads 'Alkaloid biosynthesis; ajmaline biosynthesis' (C6, H6), and the GO term GO:0009820 'alkaloid metabolic process' is directly annotated (C7, H7). Although the GO evidence code is IEA (electronic), the underlying experimental evidence for the alkaloid biosynthesis pathway is robust. The answer B is scientifically supported.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H5](#evidence-h5), [H6](#evidence-h6), [H7](#evidence-h7), [GO1](#evidence-go1).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 363-aa sequence contains motifs diagnostic of the alcohol dehydrogenase (ADH) superfamily, including a putative Rossmann-fold NAD-binding region (GAGV...GLGGLGHLAV pattern) and a zinc-binding/catalytic region (GATMGSFELPILPLGVGRKSVVSTIGGSTK). The overall architecture and absence of signal peptides, transmembrane segments, or animal-specific features indicate a plant cytosolic enzyme. Among the four options: (A) 'positive regulation of bone mineralization' is an exclusively animal process—no plant protein participates in bone mineralization; (C) 'venom-mediated fibrinolysis' is restricted to animal venom proteases (snake, spider, etc.)—a plant ADH cannot be a venom component; (D) 'cellular response to topologically incorrect protein' describes the unfolded/misfolded protein stress response (chaperones, ERAD, ubiquitin-proteasome)—an ADH enzyme is not a component of this pathway. Only (B) 'alkaloid metabolic process' is a metabolic process compatible with a plant enzyme. Plant ADH/CAD-like enzymes are well-known to participate in secondary metabolism including alkaloid biosynthesis (e.g., CAD-like enzymes in Rauvolfia, Catharanthus). Thus, recognizing the protein as a plant ADH-family enzyme and eliminating the three clearly incompatible animal/stress-response options leads uniquely to B.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A knowledgeable model can identify the ADH superfamily fold from sequence motifs, infer a plant origin from sequence context, and eliminate the three distractors that are categorically incompatible with a plant enzyme (bone mineralization is animal-only; venom fibrinolysis requires a venom protease; misfolded-protein response involves chaperones/proteasome, not a metabolic enzyme). The remaining option, alkaloid metabolic process, is the only one consistent with a plant secondary-metabolic enzyme. This is a concrete, transferable inference using family knowledge and biological domain constraints, not a lookup of this specific protein's annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors are categorically incompatible with a plant enzyme: bone mineralization (A) is animal-specific, venom-mediated fibrinolysis (C) requires a venom protease, and the misfolded-protein response (D) is a stress-response pathway not involving metabolic enzymes. Only B is a metabolic process plausible for a plant ADH. No ambiguity exists among the offered choices.


### Important caveats

- The GO annotation evidence code for this protein is IEA (Inferred from Electronic Annotation via UniProtKB-ARBA), but the underlying pathway evidence (alkaloid biosynthesis) is experimentally supported (ECO:0000269) in three independent publications.
- The specific identification as 'alkaloid' metabolism (rather than, e.g., lignin or terpenoid biosynthesis) relies on the plant CAD-like subfamily being recruited for secondary metabolism, which is a learned pattern from multiple plant species, not derivable from the sequence alone without family-level knowledge.
- The reviewer-only evidence confirms the UniProt accession A0A0U3S9Q3 and Swiss-Prot entry DHVOR_RAUSE, but this identity was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 363-aa sequence contains motifs diagnostic of the alcohol dehydrogenase (ADH) superfamily, including a putative Rossmann-fold NAD-binding region (GAGV...GLGGLGHLAV pattern) and a zinc-binding/catalytic region (GATMGSFELPILPLGVGRKSVVSTIGGSTK). The overall architecture and absence of signal peptides, transmembrane segments, or animal-specific features indicate a plant cytosolic enzyme. Among the four options: (A) 'positive regulation of bone mineralization' is an exclusively animal process—no plant protein participates in bone mineralization; (C) 'venom-mediated fibrinolysis' is restricted to animal venom proteases (snake, spider, etc.)—a plant ADH cannot be a venom component; (D) 'cellular response to topologically incorrect protein' describes the unfolded/misfolded protein stress response (chaperones, ERAD, ubiquitin-proteasome)—an ADH enzyme is not a component of this pathway. Only (B) 'alkaloid metabolic process' is a metabolic process compatible with a plant enzyme. Plant ADH/CAD-like enzymes are well-known to participate in secondary metabolism including alkaloid biosynthesis (e.g., CAD-like enzymes in Rauvolfia, Catharanthus). Thus, recognizing the protein as a plant ADH-family enzyme and eliminating the three clearly incompatible animal/stress-response options leads uniquely to B.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the ADH superfamily fold from sequence motifs, infer a plant origin from sequence context, and eliminate the three distractors that are categorically incompatible with a plant enzyme (bone mineralization is animal-only; venom fibrinolysis requires a venom protease; misfolded-protein response involves chaperones/proteasome, not a metabolic enzyme). The remaining option, alkaloid metabolic process, is the only one consistent with a plant secondary-metabolic enzyme. This is a concrete, transferable inference using family knowledge and biological domain constraints, not a lookup of this specific protein's annotation."
  },
  "case_id": "GO_biological_process_0003",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "H5",
      "H6",
      "H7",
      "GO1"
    ],
    "judgment": "supported",
    "reason": "The protein is 1,2-Dihydrovomilenine reductase (RsDHVR) from Rauvolfia serpentina, an alcohol dehydrogenase experimentally demonstrated (ECO:0000269, PubMed:12391554, 26715562, 38212296) to catalyze a step in ajmaline-type monoterpenoid indole alkaloid biosynthesis. The UniProt PATHWAY comment reads 'Alkaloid biosynthesis; ajmaline biosynthesis' (C6, H6), and the GO term GO:0009820 'alkaloid metabolic process' is directly annotated (C7, H7). Although the GO evidence code is IEA (electronic), the underlying experimental evidence for the alkaloid biosynthesis pathway is robust. The answer B is scientifically supported."
  },
  "important_caveats": [
    "The GO annotation evidence code for this protein is IEA (Inferred from Electronic Annotation via UniProtKB-ARBA), but the underlying pathway evidence (alkaloid biosynthesis) is experimentally supported (ECO:0000269) in three independent publications.",
    "The specific identification as 'alkaloid' metabolism (rather than, e.g., lignin or terpenoid biosynthesis) relies on the plant CAD-like subfamily being recruited for secondary metabolism, which is a learned pattern from multiple plant species, not derivable from the sequence alone without family-level knowledge.",
    "The reviewer-only evidence confirms the UniProt accession A0A0U3S9Q3 and Swiss-Prot entry DHVOR_RAUSE, but this identity was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are categorically incompatible with a plant enzyme: bone mineralization (A) is animal-specific, venom-mediated fibrinolysis (C) requires a venom protease, and the misfolded-protein response (D) is a stress-response pathway not involving metabolic enzymes. Only B is a metabolic process plausible for a plant ADH. No ambiguity exists among the offered choices."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_biological_process_0003",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein is 1,2-Dihydrovomilenine reductase (RsDHVR) from Rauvolfia serpentina, an alcohol dehydrogenase experimentally demonstrated (ECO:0000269, PubMed:12391554, 26715562, 38212296) to catalyze a step in ajmaline-type monoterpenoid indole alkaloid biosynthesis. The UniProt PATHWAY comment reads 'Alkaloid biosynthesis; ajmaline biosynthesis' (C6, H6), and the GO term GO:0009820 'alkaloid metabolic process' is directly annotated (C7, H7). Although the GO evidence code is IEA (electronic), the underlying experimental evidence for the alkaloid biosynthesis pathway is robust. The answer B is scientifically supported.",
    "evidence_ids": ["C5", "C6", "C7", "H5", "H6", "H7", "GO1"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 363-aa sequence contains motifs diagnostic of the alcohol dehydrogenase (ADH) superfamily, including a putative Rossmann-fold NAD-binding region (GAGV...GLGGLGHLAV pattern) and a zinc-binding/catalytic region (GATMGSFELPILPLGVGRKSVVSTIGGSTK). The overall architecture and absence of signal peptides, transmembrane segments, or animal-specific features indicate a plant cytosolic enzyme. Among the four options: (A) 'positive regulation of bone mineralization' is an exclusively animal process—no plant protein participates in bone mineralization; (C) 'venom-mediated fibrinolysis' is restricted to animal venom proteases (snake, spider, etc.)—a plant ADH cannot be a venom component; (D) 'cellular response to topologically incorrect protein' describes the unfolded/misfolded protein stress response (chaperones, ERAD, ubiquitin-proteasome)—an ADH enzyme is not a component of this pathway. Only (B) 'alkaloid metabolic process' is a metabolic process compatible with a plant enzyme. Plant ADH/CAD-like enzymes are well-known to participate in secondary metabolism including alkaloid biosynthesis (e.g., CAD-like enzymes in Rauvolfia, Catharanthus). Thus, recognizing the protein as a plant ADH-family enzyme and eliminating the three clearly incompatible animal/stress-response options leads uniquely to B.",
    "missing_item_specific_fact": "",
    "reason": "A knowledgeable model can identify the ADH superfamily fold from sequence motifs, infer a plant origin from sequence context, and eliminate the three distractors that are categorically incompatible with a plant enzyme (bone mineralization is animal-only; venom fibrinolysis requires a venom protease; misfolded-protein response involves chaperones/proteasome, not a metabolic enzyme). The remaining option, alkaloid metabolic process, is the only one consistent with a plant secondary-metabolic enzyme. This is a concrete, transferable inference using family knowledge and biological domain constraints, not a lookup of this specific protein's annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors are categorically incompatible with a plant enzyme: bone mineralization (A) is animal-specific, venom-mediated fibrinolysis (C) requires a venom protease, and the misfolded-protein response (D) is a stress-response pathway not involving metabolic enzymes. Only B is a metabolic process plausible for a plant ADH. No ambiguity exists among the offered choices."
  },
  "important_caveats": [
    "The GO annotation evidence code for this protein is IEA (Inferred from Electronic Annotation via UniProtKB-ARBA), but the underlying pathway evidence (alkaloid biosynthesis) is experimentally supported (ECO:0000269) in three independent publications.",
    "The specific identification as 'alkaloid' metabolism (rather than, e.g., lignin or terpenoid biosynthesis) relies on the plant CAD-like subfamily being recruited for secondary metabolism, which is a learned pattern from multiple plant species, not derivable from the sequence alone without family-level knowledge.",
    "The reviewer-only evidence confirms the UniProt accession A0A0U3S9Q3 and Swiss-Prot entry DHVOR_RAUSE, but this identity was not available to the evaluated model."
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
  "benchmark_sequence_length": 363,
  "benchmark_sequence_sha256": "9941adf9dcda8a9a678cb7bae23ca23f59278208d6b5e98e8fa474f1a99f1441",
  "current_entry_audit": {
    "entryVersion": 34,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-03-16",
    "sequenceVersion": 1
  },
  "current_record_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 363,
  "current_source_sequence_sha256": "9941adf9dcda8a9a678cb7bae23ca23f59278208d6b5e98e8fa474f1a99f1441",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 32,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A0U3S9Q3",
  "selected_historical_entry_version": 32,
  "selected_historical_record_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "selected_historical_source_sequence_length": 363,
  "selected_historical_source_sequence_sha256": "9941adf9dcda8a9a678cb7bae23ca23f59278208d6b5e98e8fa474f1a99f1441",
  "selected_historical_version": {
    "accession": "A0A0U3S9Q3",
    "database": "Swiss-Prot",
    "entryVersion": 32,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "DHVOR_RAUSE",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A0U3S9Q3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":34,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-03-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Serpentine wood\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Apocynaceae\",\"Rauvolfioideae\",\"Vinceae\",\"Rauvolfiinae\",\"Rauvolfia\"],\"scientificName\":\"Rauvolfia serpentina\",\"synonyms\":[\"Ophioxylon serpentinum\"],\"taxonId\":4060}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Protein RR4\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsRR4\"}]},{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"1.5.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"Vomilenine reductase 2\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsVR2\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12391554\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"1.3.1.73\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"1,2-Dihydrovomilenine reductase\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"26715562\",\"source\":\"PubMed\"}],\"value\":\"RsDHVR\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12391554\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Alcohol dehydrogenase involved in the biosynthesis of ajmaline-type monoterpenoid indole alkaloids (MIAs) natural products, important plant-derived pharmaceuticals used in the therapy of heart disorders (PubMed:26715562, PubMed:38212296). Catalyzes the conversion of 1,2-dihydrovomilenine to 17-O-acetylnorajmaline, an intermediate chemical in the biosynthesis of ajmaline (PubMed:12391554, PubMed:26715562, PubMed:38212296). Also able, with a lower efficiency, to convert vomilenine into 19,20-dihydrovomilenine (PubMed:26715562, PubMed:38212296)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"PATHWAY\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"12391554\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"26715562\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000269\",\"id\":\"38212296\",\"source\":\"PubMed\"}],\"value\":\"Alkaloid biosynthesis; ajmaline biosynthesis\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/5",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0009820\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"P:alkaloid metabolic process\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:UniProtKB-ARBA\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/12",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"citation\":{\"authors\":[\"Geissler M.\",\"Burghard M.\",\"Volk J.\",\"Staniek A.\",\"Warzecha H.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"26715562\"},{\"database\":\"DOI\",\"id\":\"10.1007/s00425-015-2446-6\"}],\"citationType\":\"journal article\",\"firstPage\":\"813\",\"id\":\"26715562\",\"journal\":\"Planta\",\"lastPage\":\"824\",\"publicationDate\":\"2016\",\"title\":\"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\",\"volume\":\"243\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"ALW82981.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 1)\",\"PROTEIN SEQUENCE OF 5-13 AND 298-308\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Guo J.\",\"Gao D.\",\"Lian J.\",\"Qu Y.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"38212296\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41467-024-44797-z\"}],\"citationType\":\"journal article\",\"firstPage\":\"457\",\"id\":\"38212296\",\"journal\":\"Nat. Commun.\",\"lastPage\":\"457\",\"publicationDate\":\"2024\",\"title\":\"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\",\"volume\":\"15\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WKU61918.1\",\"source\":\"EMBL\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 2)\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\",\"TISSUE SPECIFICITY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"citation\":{\"authors\":[\"Gao S.\",\"von Schumann G.\",\"Stoeckigt J.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"12391554\"},{\"database\":\"DOI\",\"id\":\"10.1055/s-2002-34935\"}],\"citationType\":\"journal article\",\"firstPage\":\"906\",\"id\":\"12391554\",\"journal\":\"Planta Med.\",\"lastPage\":\"911\",\"publicationDate\":\"2002\",\"title\":\"A newly-detected reductase from Rauvolfia closes a gap in the biosynthesis of the antiarrhythmic alkaloid ajmaline.\",\"volume\":\"68\"},\"referenceNumber\":3,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:24:41.228210+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "ee30accdc431e8b63f4d222bad60253967328240f6c83fd47b2627281e1afe10",
  "url": "https://rest.uniprot.org/uniprotkb/A0A0U3S9Q3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H1",
  "excerpt": "ID   DHVOR_RAUSE             Reviewed;         363 AA.\nAC   A0A0U3S9Q3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-MAR-2016, sequence version 1.\nDT   28-JAN-2026, entry version 32.\nDE   RecName: Full=1,2-Dihydrovomilenine reductase {ECO:0000303|PubMed:26715562};\nDE            Short=RsDHVR {ECO:0000303|PubMed:26715562};\nDE            EC=1.3.1.73 {ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:38212296};\nDE   AltName: Full=Protein RR4 {ECO:0000303|PubMed:26715562};\nDE            Short=RsRR4 {ECO:0000303|PubMed:26715562};\nDE   AltName: Full=Vomilenine reductase 2 {ECO:0000303|PubMed:26715562};\nDE            Short=RsVR2 {ECO:0000303|PubMed:26715562};\nDE            EC=1.5.1.- {ECO:0000269|PubMed:26715562, ECO:0000269|PubMed:38212296};\nGN   Name=DHVR {ECO:0000303|PubMed:26715562};\nGN   Synonyms=RR4 {ECO:0000303|PubMed:26715562},\nGN   VR2 {ECO:0000303|PubMed:26715562};\nOS   Rauvolfia serpentina (Serpentine wood) (Ophioxylon serpentinum).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Apocynaceae; Rauvolfioideae; Vinceae;\nOC   Rauvolfiinae; Rauvolfia.\nOX   NCBI_TaxID=4060;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-22",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:ALW82981.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 1), PROTEIN SEQUENCE OF 5-13 AND\nRP   298-308, FUNCTION, CATALYTIC ACTIVITY, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOPHYSICOCHEMICAL PROPERTIES.\nRX   PubMed=26715562; DOI=10.1007/s00425-015-2446-6;\nRA   Geissler M., Burghard M., Volk J., Staniek A., Warzecha H.;\nRT   \"A novel cinnamyl alcohol dehydrogenase (CAD)-like reductase contributes to\nRT   the structural diversity of monoterpenoid indole alkaloids in Rauvolfia.\";\nRL   Planta 243:813-824(2016).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 23-31",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H3",
  "excerpt": "RN   [2] {ECO:0000312|EMBL:WKU61918.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA] (ISOFORM 2), FUNCTION, CATALYTIC ACTIVITY,\nRP   BIOPHYSICOCHEMICAL PROPERTIES, PATHWAY, TISSUE SPECIFICITY, AND\nRP   BIOTECHNOLOGY.\nRX   PubMed=38212296; DOI=10.1038/s41467-024-44797-z;\nRA   Guo J., Gao D., Lian J., Qu Y.;\nRT   \"De novo biosynthesis of antiarrhythmic alkaloid ajmaline.\";\nRL   Nat. Commun. 15:457-457(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 32-39",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H4",
  "excerpt": "RN   [3]\nRP   FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES, AND PATHWAY.\nRX   PubMed=12391554; DOI=10.1055/s-2002-34935;\nRA   Gao S., von Schumann G., Stoeckigt J.;\nRT   \"A newly-detected reductase from Rauvolfia closes a gap in the biosynthesis\nRT   of the antiarrhythmic alkaloid ajmaline.\";\nRL   Planta Med. 68:906-911(2002).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 40-46",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H5",
  "excerpt": "CC   -!- FUNCTION: Alcohol dehydrogenase involved in the biosynthesis of\nCC       ajmaline-type monoterpenoid indole alkaloids (MIAs) natural products,\nCC       important plant-derived pharmaceuticals used in the therapy of heart\nCC       disorders (PubMed:26715562, PubMed:38212296). Catalyzes the conversion\nCC       of 1,2-dihydrovomilenine to 17-O-acetylnorajmaline, an intermediate\nCC       chemical in the biosynthesis of ajmaline (PubMed:12391554,\nCC       PubMed:26715562, PubMed:38212296). Also able, with a lower efficiency,\nCC       to convert vomilenine into 19,20-dihydrovomilenine (PubMed:26715562,\nCC       PubMed:38212296). {ECO:0000269|PubMed:12391554,\nCC       ECO:0000269|PubMed:26715562, ECO:0000269|PubMed:38212296}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 47-56",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H6",
  "excerpt": "CC   -!- PATHWAY: Alkaloid biosynthesis; ajmaline biosynthesis.\nCC       {ECO:0000269|PubMed:12391554, ECO:0000269|PubMed:26715562,\nCC       ECO:0000269|PubMed:38212296}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 89-91",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32)

```json
{
  "entry_version": 32,
  "evidence_id": "H7",
  "excerpt": "DR   GO; GO:0009820; P:alkaloid metabolic process; IEA:UniProtKB-KW.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:20.990872+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-130",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d736edca11739beb62ca2d5765f93a0db6fdd42ef122f9711acacccadcaabc22",
  "url": "https://rest.uniprot.org/unisave/A0A0U3S9Q3?format=txt&versions=32"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0009820\nname: alkaloid metabolic process\nnamespace: biological_process\ndef: \"The chemical reactions and pathways involving alkaloids, nitrogen containing natural products which are not otherwise classified as peptides, nonprotein amino acids, amines, cyanogenic glycosides, glucosinolates, cofactors, phytohormones or primary metabolites (such as purine or pyrimidine bases).\" [GOC:lr, ISBN:0122146743]\nsubset: goslim_chembl\nsynonym: \"alkaloid metabolism\" EXACT []\nis_a: GO:0008152 ! metabolic process\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0009820",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 99940-99948",
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
  "excerpt": "[Term]\nid: GO:0030501\nname: positive regulation of bone mineralization\nnamespace: biological_process\ndef: \"Any process that activates or increases the frequency, rate or extent of bone mineralization.\" [GOC:curators]\nsynonym: \"activation of bone mineralization\" NARROW []\nsynonym: \"stimulation of bone mineralization\" NARROW []\nsynonym: \"up regulation of bone mineralization\" EXACT []\nsynonym: \"up-regulation of bone mineralization\" EXACT []\nsynonym: \"upregulation of bone mineralization\" EXACT []\nis_a: GO:0030500 ! regulation of bone mineralization\nis_a: GO:0045778 ! positive regulation of ossification\nis_a: GO:0070169 ! positive regulation of biomineral tissue development\nrelationship: positively_regulates GO:0030282 ! bone mineralization\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0030501",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 166673-166687",
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
  "excerpt": "[Term]\nid: GO:0035967\nname: cellular response to topologically incorrect protein\nnamespace: biological_process\ndef: \"Any process that results in a change in state or activity of a cell (in terms of movement, secretion, enzyme production, gene expression, etc.) as a result of a protein that is not folded in its correct three-dimensional structure.\" [GOC:bf]\nsynonym: \"cellular response to misfolded or unfolded protein\" RELATED [GOC:bf]\nis_a: GO:0033554 ! cellular response to stress\nis_a: GO:0035966 ! response to topologically incorrect protein\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0035967",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 223090-223098",
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
  "excerpt": "[Term]\nid: GO:0044484\nname: venom-mediated fibrinolysis\nnamespace: biological_process\ndef: \"A process in which an organism causes fibrinolysis in another organism via the action of a venom. Fibrinolysis is a process that solubilizes fibrin in the blood, chiefly by the proteolytic action of plasmin.\" [GOC:fj, GOC:jl, PMID:17433397, PMID:17544404]\nsynonym: \"envenomation resulting in fibrinolysis\" EXACT []\nsynonym: \"envenomation resulting in fibrinolysis in another organism\" EXACT []\nsynonym: \"envenomation resulting in fibrinolysis in other organism\" EXACT []\nis_a: GO:0044483 ! venom-mediated perturbation of hemostasis\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0044484",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 257660-257669",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_biological_process.json), zero-based source row 3. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
