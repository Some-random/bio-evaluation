# catalytic_activity_0125

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0125.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4&#x27;-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MTSHHSWYRYSINPFVLMGLVALFLAATANLTFFEKAMAVYPVSDNLGFIISMAVAVMGAMLLIVVLLSYRYVLKPVLILLLIMGAVTSYFTDTYGTVYDTTMLQNAMQTDQAESKDLMNLAFFVRIIGLGVLPSVLVAVAKVNYPTWGKGLIQRAMTWGVSLVLLLVPIGLFSSQYASFFRVHKPVRFYINPITPIYSVGKLASIEYKKATAPTDTIYHAKDAVQTTKPSERKPRLVVFVVGETARADHVQFNGYGRETFPQLAKVDGLANFSQVTSCGTSTAYSVPCMFSYLGQDDYDVDTAKYQENVLDTLDRLGVGILWRDNNSDSKGVMDKLPATQYFDYKSATNNTICNTNPYNECRDVGMLVGLDDYVSANNGKDMLIMLHQMGNHGPAYFKRYDEQFAKFTPVCEGNELAKCEHQSLINAYDNALLATDDFIAKSIDWLKTHEANYDVAMLYVSDHGESLGENGVYLHGMPNAFAPKEQRAVPAFFWSNNTTFKPTASDTVLTHDAITPTLLKLFDVTAGKVKDRAAFIQ

[Multiple Choices]
A. lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol
B. Random endo-hydrolysis of N-acetyl-beta-D-glucosaminide (1->4)-beta-linkages in chitin and chitodextrins.
C. spheroidene + 4 reduced [2Fe-2S]-[ferredoxin] + 2 O2 + 4 H(+) = spheroiden-2-one + 4 oxidized [2Fe-2S]-[ferredoxin] + 3 H2O
D. 4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-methionine = N-methyl-4-hydroxy-3,5-dimethoxyphenethylamine + S-adenosyl-L-homocysteine + H(+)
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

> The sequence exactly matches the cited UniProt record, whose catalytic-activity annotation gives the reaction in choice A and cites a paper addressing MCR-2 structure and function. This supports the key, though the excerpts do not independently show the underlying assay results.

Citations as saved: [H4](#evidence-h4), [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence has a prominent hydrophobic N-terminal region consistent with multiple membrane-spanning segments followed by a large non-membrane domain. That architecture is characteristic of membrane-associated phosphoethanolamine transferases such as the MCR family, which modify lipid A using phosphatidylethanolamine. This transferable family-level pattern makes choice A substantially more plausible than chitin hydrolysis, carotenoid oxidation, or small-molecule methylation.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The options contrast distinct enzyme families and reaction types. Sequence architecture plus transferable knowledge about MCR-like lipid-modifying enzymes meaningfully distinguishes A without needing the exact protein's database annotation, although sequence alone may not establish every substrate detail with certainty.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four choices describe substantially different enzyme activities, and the sequence pattern supports the lipid A-modifying activity in A.


### Important caveats

- The reviewer-only annotation is literature-linked database evidence, not a presentation of the primary experimental data.
- The family-level sequence inference supports the choice probabilistically; it is not by itself a complete biochemical demonstration of the precise reaction.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence has a prominent hydrophobic N-terminal region consistent with multiple membrane-spanning segments followed by a large non-membrane domain. That architecture is characteristic of membrane-associated phosphoethanolamine transferases such as the MCR family, which modify lipid A using phosphatidylethanolamine. This transferable family-level pattern makes choice A substantially more plausible than chitin hydrolysis, carotenoid oxidation, or small-molecule methylation.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The options contrast distinct enzyme families and reaction types. Sequence architecture plus transferable knowledge about MCR-like lipid-modifying enzymes meaningfully distinguishes A without needing the exact protein's database annotation, although sequence alone may not establish every substrate detail with certainty."
  },
  "case_id": "catalytic_activity_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "H4",
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited UniProt record, whose catalytic-activity annotation gives the reaction in choice A and cites a paper addressing MCR-2 structure and function. This supports the key, though the excerpts do not independently show the underlying assay results."
  },
  "important_caveats": [
    "The reviewer-only annotation is literature-linked database evidence, not a presentation of the primary experimental data.",
    "The family-level sequence inference supports the choice probabilistically; it is not by itself a complete biochemical demonstration of the precise reaction."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe substantially different enzyme activities, and the sequence pattern supports the lipid A-modifying activity in A."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence exactly matches the cited UniProt record, whose catalytic-activity annotation gives the reaction in choice A and cites a paper addressing MCR-2 structure and function. This supports the key, though the excerpts do not independently show the underlying assay results.",
    "evidence_ids": ["H4", "C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence has a prominent hydrophobic N-terminal region consistent with multiple membrane-spanning segments followed by a large non-membrane domain. That architecture is characteristic of membrane-associated phosphoethanolamine transferases such as the MCR family, which modify lipid A using phosphatidylethanolamine. This transferable family-level pattern makes choice A substantially more plausible than chitin hydrolysis, carotenoid oxidation, or small-molecule methylation.",
    "missing_item_specific_fact": "",
    "reason": "The options contrast distinct enzyme families and reaction types. Sequence architecture plus transferable knowledge about MCR-like lipid-modifying enzymes meaningfully distinguishes A without needing the exact protein's database annotation, although sequence alone may not establish every substrate detail with certainty."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four choices describe substantially different enzyme activities, and the sequence pattern supports the lipid A-modifying activity in A."
  },
  "important_caveats": [
    "The reviewer-only annotation is literature-linked database evidence, not a presentation of the primary experimental data.",
    "The family-level sequence inference supports the choice probabilistically; it is not by itself a complete biochemical demonstration of the precise reaction."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The reviewer evidence (C5, H4) from UniProt entry A0A1C3NEV1 (MCR-2, EC 2.7.8.43) records the exact catalytic reaction stated in Choice A: lipid A (E. coli) + 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + 1,2-diacyl-sn-glycerol. The sequence matches (538 AA, SHA256 identical). The annotation is backed by a crystal structure (PDB 6A7W) and a PubMed publication (30194678) reporting functional characterization, with evidence code ECO:0000305 (curator inference from experimental data).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 538-residue sequence exhibits a clear multi-transmembrane (TM) architecture: the N-terminal ~200 residues contain approximately 10 hydrophobic stretches characteristic of integral membrane proteins, followed by a cytoplasmic catalytic domain. This architecture immediately eliminates Choice B (chitinase: soluble glycosyl hydrolase, no TM segments), Choice C (spheroidene monooxygenase: soluble Rieske-type &#91;2Fe-2S&#93; oxygenase, ~300-400 AA, no multi-TM topology), and Choice D (catechol O-methyltransferase: small ~270 AA soluble SAM-dependent enzyme). Among the remaining alternatives, only Choice A describes a membrane-associated lipid-modification reaction. Furthermore, the cytoplasmic domain contains histidine-rich motifs (e.g., 'HQMGNHG', 'VSDHGESLGENGVYLHG') consistent with the Zn2+-binding catalytic motifs conserved across the MCR phosphoethanolamine transferase family (MCR-1 through MCR-10), a well-known group of plasmid-encoded colistin-resistance enzymes. The combination of (1) ~10 TM helices, (2) a cytoplasmic catalytic domain of appropriate length, and (3) His-rich metal-binding motifs in that domain provides a credible family-level inference pointing to a phosphoethanolamine transferase acting on lipid A, which matches Choice A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The multi-TM membrane architecture is directly observable from the sequence and is a strong discriminator against the three soluble-enzyme distractors (B, C, D). The cytoplasmic domain's His-rich motifs and overall topology are consistent with the well-characterized MCR phosphoethanolamine transferase family, allowing a knowledgeable model to infer the lipid A modification reaction without needing to recall the specific database entry for this exact protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The three distractors (chitinase, carotenoid oxygenase, SAM-methyltransferase) describe soluble enzymes with completely different architectures and cofactor requirements, making them clearly incompatible with the multi-TM sequence. No other offered choice is a plausible alternative given the sequence topology.


### Important caveats

- The MCR family recognition relies on the model's knowledge of this well-studied antimicrobial-resistance protein family; the specific catalytic reaction details (lipid A 4'-phosphoethanolamine transfer) are a family-level assignment rather than a de novo prediction from sequence alone.
- The UniProt annotation uses evidence code ECO:0000305 (curator inference from experimental data in PubMed 30194678 and PDB 6A7W), indicating the catalytic activity was established experimentally but the annotation itself is a curated statement.
- The reviewer-only evidence confirms the sequence-to-entry match; this identity was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 538-residue sequence exhibits a clear multi-transmembrane (TM) architecture: the N-terminal ~200 residues contain approximately 10 hydrophobic stretches characteristic of integral membrane proteins, followed by a cytoplasmic catalytic domain. This architecture immediately eliminates Choice B (chitinase: soluble glycosyl hydrolase, no TM segments), Choice C (spheroidene monooxygenase: soluble Rieske-type [2Fe-2S] oxygenase, ~300-400 AA, no multi-TM topology), and Choice D (catechol O-methyltransferase: small ~270 AA soluble SAM-dependent enzyme). Among the remaining alternatives, only Choice A describes a membrane-associated lipid-modification reaction. Furthermore, the cytoplasmic domain contains histidine-rich motifs (e.g., 'HQMGNHG', 'VSDHGESLGENGVYLHG') consistent with the Zn2+-binding catalytic motifs conserved across the MCR phosphoethanolamine transferase family (MCR-1 through MCR-10), a well-known group of plasmid-encoded colistin-resistance enzymes. The combination of (1) ~10 TM helices, (2) a cytoplasmic catalytic domain of appropriate length, and (3) His-rich metal-binding motifs in that domain provides a credible family-level inference pointing to a phosphoethanolamine transferase acting on lipid A, which matches Choice A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The multi-TM membrane architecture is directly observable from the sequence and is a strong discriminator against the three soluble-enzyme distractors (B, C, D). The cytoplasmic domain's His-rich motifs and overall topology are consistent with the well-characterized MCR phosphoethanolamine transferase family, allowing a knowledgeable model to infer the lipid A modification reaction without needing to recall the specific database entry for this exact protein."
  },
  "case_id": "catalytic_activity_0125",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The reviewer evidence (C5, H4) from UniProt entry A0A1C3NEV1 (MCR-2, EC 2.7.8.43) records the exact catalytic reaction stated in Choice A: lipid A (E. coli) + 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + 1,2-diacyl-sn-glycerol. The sequence matches (538 AA, SHA256 identical). The annotation is backed by a crystal structure (PDB 6A7W) and a PubMed publication (30194678) reporting functional characterization, with evidence code ECO:0000305 (curator inference from experimental data)."
  },
  "important_caveats": [
    "The MCR family recognition relies on the model's knowledge of this well-studied antimicrobial-resistance protein family; the specific catalytic reaction details (lipid A 4'-phosphoethanolamine transfer) are a family-level assignment rather than a de novo prediction from sequence alone.",
    "The UniProt annotation uses evidence code ECO:0000305 (curator inference from experimental data in PubMed 30194678 and PDB 6A7W), indicating the catalytic activity was established experimentally but the annotation itself is a curated statement.",
    "The reviewer-only evidence confirms the sequence-to-entry match; this identity was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (chitinase, carotenoid oxygenase, SAM-methyltransferase) describe soluble enzymes with completely different architectures and cofactor requirements, making them clearly incompatible with the multi-TM sequence. No other offered choice is a plausible alternative given the sequence topology."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0125",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The reviewer evidence (C5, H4) from UniProt entry A0A1C3NEV1 (MCR-2, EC 2.7.8.43) records the exact catalytic reaction stated in Choice A: lipid A (E. coli) + 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + 1,2-diacyl-sn-glycerol. The sequence matches (538 AA, SHA256 identical). The annotation is backed by a crystal structure (PDB 6A7W) and a PubMed publication (30194678) reporting functional characterization, with evidence code ECO:0000305 (curator inference from experimental data).",
    "evidence_ids": ["C5", "H4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 538-residue sequence exhibits a clear multi-transmembrane (TM) architecture: the N-terminal ~200 residues contain approximately 10 hydrophobic stretches characteristic of integral membrane proteins, followed by a cytoplasmic catalytic domain. This architecture immediately eliminates Choice B (chitinase: soluble glycosyl hydrolase, no TM segments), Choice C (spheroidene monooxygenase: soluble Rieske-type [2Fe-2S] oxygenase, ~300-400 AA, no multi-TM topology), and Choice D (catechol O-methyltransferase: small ~270 AA soluble SAM-dependent enzyme). Among the remaining alternatives, only Choice A describes a membrane-associated lipid-modification reaction. Furthermore, the cytoplasmic domain contains histidine-rich motifs (e.g., 'HQMGNHG', 'VSDHGESLGENGVYLHG') consistent with the Zn2+-binding catalytic motifs conserved across the MCR phosphoethanolamine transferase family (MCR-1 through MCR-10), a well-known group of plasmid-encoded colistin-resistance enzymes. The combination of (1) ~10 TM helices, (2) a cytoplasmic catalytic domain of appropriate length, and (3) His-rich metal-binding motifs in that domain provides a credible family-level inference pointing to a phosphoethanolamine transferase acting on lipid A, which matches Choice A.",
    "missing_item_specific_fact": "",
    "reason": "The multi-TM membrane architecture is directly observable from the sequence and is a strong discriminator against the three soluble-enzyme distractors (B, C, D). The cytoplasmic domain's His-rich motifs and overall topology are consistent with the well-characterized MCR phosphoethanolamine transferase family, allowing a knowledgeable model to infer the lipid A modification reaction without needing to recall the specific database entry for this exact protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The three distractors (chitinase, carotenoid oxygenase, SAM-methyltransferase) describe soluble enzymes with completely different architectures and cofactor requirements, making them clearly incompatible with the multi-TM sequence. No other offered choice is a plausible alternative given the sequence topology."
  },
  "important_caveats": [
    "The MCR family recognition relies on the model's knowledge of this well-studied antimicrobial-resistance protein family; the specific catalytic reaction details (lipid A 4'-phosphoethanolamine transfer) are a family-level assignment rather than a de novo prediction from sequence alone.",
    "The UniProt annotation uses evidence code ECO:0000305 (curator inference from experimental data in PubMed 30194678 and PDB 6A7W), indicating the catalytic activity was established experimentally but the annotation itself is a curated statement.",
    "The reviewer-only evidence confirms the sequence-to-entry match; this identity was not available to the evaluated model."
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
  "benchmark_sequence_length": 538,
  "benchmark_sequence_sha256": "ac11cd8f4c43b75871bc89c0dbaa1f186110d0c878b6152a899c2abf8270e1ac",
  "current_entry_audit": {
    "entryVersion": 40,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2016-11-02",
    "sequenceVersion": 1
  },
  "current_record_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 538,
  "current_source_sequence_sha256": "ac11cd8f4c43b75871bc89c0dbaa1f186110d0c878b6152a899c2abf8270e1ac",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 38,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A1C3NEV1",
  "selected_historical_entry_version": 38,
  "selected_historical_record_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "selected_historical_source_sequence_length": 538,
  "selected_historical_source_sequence_sha256": "ac11cd8f4c43b75871bc89c0dbaa1f186110d0c878b6152a899c2abf8270e1ac",
  "selected_historical_version": {
    "accession": "A0A1C3NEV1",
    "database": "Swiss-Prot",
    "entryVersion": 38,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "MCR2_ECOLX",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A1C3NEV1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":40,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2016-11-02\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"SBV31106.1\",\"source\":\"EMBL\"}],\"lineage\":[\"Bacteria\",\"Pseudomonadati\",\"Pseudomonadota\",\"Gammaproteobacteria\",\"Enterobacterales\",\"Enterobacteriaceae\",\"Escherichia\"],\"scientificName\":\"Escherichia coli\",\"taxonId\":562}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"A0A0R6L508\",\"source\":\"UniProtKB\"}],\"value\":\"Polymyxin resistance protein MCR-2\"}}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30194678\",\"source\":\"PubMed\"}],\"value\":\"2.7.8.43\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"30194678\",\"source\":\"PubMed\"},{\"evidenceCode\":\"ECO:0000303\",\"id\":\"Ref.1\",\"source\":\"Reference\"}],\"value\":\"Phosphatidylethanolamine transferase Mcr-2\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"2.7.8.43\",\"evidences\":[{\"evidenceCode\":\"ECO:0000305\",\"id\":\"30194678\",\"source\":\"PubMed\"}],\"name\":\"lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate) (E. coli) + a 1,2-diacyl-sn-glycerol\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:46900\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:17815\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:64612\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:87097\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:134257\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Wang X.\",\"Lu Q.\",\"Qi J.\",\"Chai Y.\",\"Wang Y.\",\"Gao G.F.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"30194678\"},{\"database\":\"DOI\",\"id\":\"10.1007/s11427-018-9363-4\"}],\"citationType\":\"journal article\",\"firstPage\":\"1432\",\"id\":\"30194678\",\"journal\":\"Sci. China Life Sci.\",\"lastPage\":\"1436\",\"publicationDate\":\"2018\",\"title\":\"Structural and functional insights into MCR-2 mediated colistin resistance.\",\"volume\":\"61\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"6A7W\",\"source\":\"PDB\"}],\"referenceComments\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WHI04997.1\",\"source\":\"EMBL\"}],\"type\":\"PLASMID\",\"value\":\"unnamed5\"}],\"referenceNumber\":4,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+)\",\"DISULFIDE BONDS\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"MUTAGENESIS OF PHE-91; TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283; LYS-331 AND HIS-476\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/3",
  "retrieved_utc": "2026-11-02T04:24:32.663314+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "919af10a00ec31395e30970b3152dc7099658836191b0b0da093f5ea34918d31",
  "url": "https://rest.uniprot.org/uniprotkb/A0A1C3NEV1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H1",
  "excerpt": "ID   MCR2_ECOLX              Reviewed;         538 AA.\nAC   A0A1C3NEV1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   02-NOV-2016, sequence version 1.\nDT   28-JAN-2026, entry version 38.\nDE   RecName: Full=Phosphatidylethanolamine transferase Mcr-2 {ECO:0000303|PubMed:30194678, ECO:0000303|Ref.1};\nDE            EC=2.7.8.43 {ECO:0000305|PubMed:30194678};\nDE   AltName: Full=Polymyxin resistance protein MCR-2 {ECO:0000250|UniProtKB:A0A0R6L508};\nGN   Name=mcr2 {ECO:0000305}; Synonyms=mcr-2 {ECO:0000312|EMBL:SBV31106.1};\nGN   ORFNames=QDW62_28200 {ECO:0000312|EMBL:WHI04997.1};\nOS   Escherichia coli.\nOG   Plasmid pKP37-BE {ECO:0000312|EMBL:SBV31106.1}, and\nOG   Plasmid unnamed5 {ECO:0000312|EMBL:WHI04997.1}.\nOC   Bacteria; Pseudomonadati; Pseudomonadota; Gammaproteobacteria;\nOC   Enterobacterales; Enterobacteriaceae; Escherichia.\nOX   NCBI_TaxID=562 {ECO:0000312|EMBL:SBV31106.1};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-16",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Phosphatidylethanolamine transferase Mcr-2 {ECO:0000303|PubMed:30194678, ECO:0000303|Ref.1};\nDE            EC=2.7.8.43 {ECO:0000305|PubMed:30194678};\nDE   AltName: Full=Polymyxin resistance protein MCR-2 {ECO:0000250|UniProtKB:A0A0R6L508};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-8",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H3",
  "excerpt": "RN   [4] {ECO:0007744|PDB:6A7W}\nRP   X-RAY CRYSTALLOGRAPHY (2.99 ANGSTROMS) OF 215-538 IN COMPLEX WITH ZN(2+),\nRP   DISULFIDE BONDS, FUNCTION, CATALYTIC ACTIVITY, AND MUTAGENESIS OF PHE-91;\nRP   TYR-99; MET-103; ASN-106; THR-110; GLU-114; SER-115; PHE-123; THR-283;\nRP   LYS-331 AND HIS-476.\nRC   PLASMID=unnamed5 {ECO:0000312|EMBL:WHI04997.1};\nRX   PubMed=30194678; DOI=10.1007/s11427-018-9363-4;\nRA   Wang X., Lu Q., Qi J., Chai Y., Wang Y., Gao G.F.;\nRT   \"Structural and functional insights into MCR-2 mediated colistin\nRT   resistance.\";\nRL   Sci. China Life Sci. 61:1432-1436(2018).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 44-54",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38)

```json
{
  "entry_version": 38,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=lipid A (E. coli) + a 1,2-diacyl-sn-glycero-3-\nCC         phosphoethanolamine + H(+) = lipid A 4'-(2-aminoethyl diphosphate)\nCC         (E. coli) + a 1,2-diacyl-sn-glycerol; Xref=Rhea:RHEA:46900,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:17815, ChEBI:CHEBI:64612,\nCC         ChEBI:CHEBI:87097, ChEBI:CHEBI:134257; EC=2.7.8.43;\nCC         Evidence={ECO:0000305|PubMed:30194678};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:24:35.172422+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 72-78",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "d75fc4c8bc738f05806f3af9945e4dc68a9d390599953db777a2ada2b9fa9923",
  "url": "https://rest.uniprot.org/unisave/A0A1C3NEV1?format=txt&versions=38"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 125. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
