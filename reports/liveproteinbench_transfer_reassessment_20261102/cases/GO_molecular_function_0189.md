# GO_molecular_function_0189

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0189.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — beta-glucosidase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MSSVLPTPVLPTPGKNINRGHFPDDFIFGAGTSSYQIEGAAREGGRGPSIWDTFTHTHPELIQDGSNGDTAVNSYNLYKEDIKIVKLMGLDAYRFSISWPRILPGGSINAGINQEGIKYYNNLIDELLANDIVPYVTLFHWDVPQALQDQYDGFLSDKIVDDFRDFAELCFWEFGDRVKNWITINEPQSYSDFFGVAYDTPPKAHALKASRLLVPTTVARPSKPARVFASTADPGTTTADQVYKVGHNLLLAHAAALKVYRDNFQDTQEGTFGMALVTQWMKPLNENNPADVEAASRAFDFKFGWFMQPLITGEYPKSMRQSLGPRLREFTRDQKKLLIGSYDYVGVNYYTATYVSSARPPNDNKAIFHTDGNFYTTDCKDGVLIGPLAGPAWLNIVPEGIYRCLQEIKAKYNNPVIYITENGVYEVNDTTKTLSEARVDTTRVDYLQDHLSYVLKARQQGVRVQGYFVWSLMDNWELRAGYTSRFGLIHVDYYNNFARYPKDSAIWFRNAFHKRLRIHVNKRPQEDDGAFDTPRKRLKK

[Multiple Choices]
A. ubiquitin-like protein transferase activity
B. 2-oxoglutarate-dependent dioxygenase activity
C. 2 iron, 2 sulfur cluster binding
D. beta-glucosidase activity
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

> The sequence-matched UniProt record reports beta-glucosidase activity and experimentally supported reactions releasing D-glucose from glucoside substrates. Its GO annotation is also beta-glucosidase activity.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the conserved GH1 glycoside-hydrolase motifs ITINEP and ITENG, consistent with a retaining glycosidase such as a beta-glucosidase. This family-level sequence evidence makes D substantially more plausible than ubiquitin-like transferase activity, 2-oxoglutarate-dependent dioxygenase activity, or 2Fe-2S cluster binding. The motifs support the enzyme family, though they do not alone establish its exact substrate specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Transferable knowledge of GH1 sequence motifs provides a concrete basis to distinguish the beta-glucosidase choice among these alternatives; the exact protein's recorded annotation is not necessary for that distinction.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The sequence-family inference favors D, and the supplied experimental annotation and reactions agree with that choice.


### Important caveats

- Reviewer-only annotations support the key but were not available as original input.
- Family motifs support a glycoside-hydrolase inference but do not independently prove the protein's specific physiological substrates.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the conserved GH1 glycoside-hydrolase motifs ITINEP and ITENG, consistent with a retaining glycosidase such as a beta-glucosidase. This family-level sequence evidence makes D substantially more plausible than ubiquitin-like transferase activity, 2-oxoglutarate-dependent dioxygenase activity, or 2Fe-2S cluster binding. The motifs support the enzyme family, though they do not alone establish its exact substrate specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of GH1 sequence motifs provides a concrete basis to distinguish the beta-glucosidase choice among these alternatives; the exact protein's recorded annotation is not necessary for that distinction."
  },
  "case_id": "GO_molecular_function_0189",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6",
      "C7",
      "C8"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports beta-glucosidase activity and experimentally supported reactions releasing D-glucose from glucoside substrates. Its GO annotation is also beta-glucosidase activity."
  },
  "important_caveats": [
    "Reviewer-only annotations support the key but were not available as original input.",
    "Family motifs support a glycoside-hydrolase inference but do not independently prove the protein's specific physiological substrates."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-family inference favors D, and the supplied experimental annotation and reactions agree with that choice."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0189",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt record reports beta-glucosidase activity and experimentally supported reactions releasing D-glucose from glucoside substrates. Its GO annotation is also beta-glucosidase activity.",
    "evidence_ids": ["C5", "C6", "C7", "C8"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the conserved GH1 glycoside-hydrolase motifs ITINEP and ITENG, consistent with a retaining glycosidase such as a beta-glucosidase. This family-level sequence evidence makes D substantially more plausible than ubiquitin-like transferase activity, 2-oxoglutarate-dependent dioxygenase activity, or 2Fe-2S cluster binding. The motifs support the enzyme family, though they do not alone establish its exact substrate specificity.",
    "missing_item_specific_fact": "",
    "reason": "Transferable knowledge of GH1 sequence motifs provides a concrete basis to distinguish the beta-glucosidase choice among these alternatives; the exact protein's recorded annotation is not necessary for that distinction."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The sequence-family inference favors D, and the supplied experimental annotation and reactions agree with that choice."
  },
  "important_caveats": [
    "Reviewer-only annotations support the key but were not available as original input.",
    "Family motifs support a glycoside-hydrolase inference but do not independently prove the protein's specific physiological substrates."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry B6ZKN1 (sequence matched, 540 AA) is annotated as 'Ipecac alkaloid beta-glucosidase 9' with EC 3.2.1.-, GO:0008422 (beta-glucosidase activity) assigned via IDA (Inferred by Direct Assay) from experimental evidence (PubMed:18927081). The function comment confirms 'Beta-glucosidase catalyzing deglucosylation on N-deacetylisoipecoside and N-deacetylipecoside,' and catalytic activity reactions show hydrolysis releasing D-glucose. This is experimental evidence (ECO:0000269), not mere computational prediction.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [C8](#evidence-c8), [C9](#evidence-c9), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5), [H6](#evidence-h6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the NEP catalytic motif (visible as 'WITINEP' around residues ~170-176), which is a well-established, transferable sequence signature of Glycoside Hydrolase family 1 (GH1). This motif is shared across many characterized GH1 proteins (e.g., E. coli BgaA, plant beta-glucosidases like prunasinase, amygdalase, and numerous plant GH1 enzymes). The overall ~540-residue length and (β/α)8 TIM-barrel architecture are consistent with GH1. Among GH1 enzymes in plants (suggested by the N-terminal signal-peptide-like region and plant-typical sequence composition), beta-glucosidase is by far the predominant activity. The other options can be excluded by absence of their diagnostic motifs: (A) ubiquitin-like transferases require RING/U-box/HECT/RBR domains absent here; (B) 2-oxoglutarate-dependent dioxygenases require the HxD/E…H facial triad and a double-stranded β-helix fold, neither present; (C) 2Fe-2S cluster binding requires CxxC…CxxC cysteine-rich coordination motifs, absent in this sequence. Thus, the NEP motif plus plant context plus absence of alternative-domain signatures provides a credible transferable inference favoring D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The NEP motif is a family-level sequence signature learned from many GH1 proteins, not specific to this exact entry. Combined with the plant context and the clear absence of motifs required by options A, B, and C, a knowledgeable model can meaningfully distinguish D from the alternatives without knowing the recorded answer for this specific protein.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The NEP motif is specific to GH1 and does not overlap with the structural requirements of ubiquitin transferases, 2OG dioxygenases, or Fe-S cluster binding proteins. While GH1 contains a few non-glucosidase members, the plant context and overwhelming statistical prevalence of beta-glucosidase in plant GH1 make D the clear best choice among the four options.


### Important caveats

- The NEP motif identifies GH1 family membership but does not by itself guarantee beta-glucosidase specificity (GH1 also includes beta-galactosidases, beta-mannosidases, etc.); however, in plant GH1, beta-glucosidase is the dominant activity by a large margin.
- The reviewer-only evidence confirms experimental (IDA) annotation, but the evaluated model does not have access to this; the reasoning relies solely on sequence features and transferable family knowledge.
- The specific substrate (ipecac alkaloid glucosides) is unusual and would not be predictable from sequence alone, but the GO molecular function term 'beta-glucosidase activity' (GO:0008422) is correctly assigned based on the general catalytic mechanism (hydrolysis of terminal non-reducing beta-D-glucose residues).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the NEP catalytic motif (visible as 'WITINEP' around residues ~170-176), which is a well-established, transferable sequence signature of Glycoside Hydrolase family 1 (GH1). This motif is shared across many characterized GH1 proteins (e.g., E. coli BgaA, plant beta-glucosidases like prunasinase, amygdalase, and numerous plant GH1 enzymes). The overall ~540-residue length and (β/α)8 TIM-barrel architecture are consistent with GH1. Among GH1 enzymes in plants (suggested by the N-terminal signal-peptide-like region and plant-typical sequence composition), beta-glucosidase is by far the predominant activity. The other options can be excluded by absence of their diagnostic motifs: (A) ubiquitin-like transferases require RING/U-box/HECT/RBR domains absent here; (B) 2-oxoglutarate-dependent dioxygenases require the HxD/E…H facial triad and a double-stranded β-helix fold, neither present; (C) 2Fe-2S cluster binding requires CxxC…CxxC cysteine-rich coordination motifs, absent in this sequence. Thus, the NEP motif plus plant context plus absence of alternative-domain signatures provides a credible transferable inference favoring D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The NEP motif is a family-level sequence signature learned from many GH1 proteins, not specific to this exact entry. Combined with the plant context and the clear absence of motifs required by options A, B, and C, a knowledgeable model can meaningfully distinguish D from the alternatives without knowing the recorded answer for this specific protein."
  },
  "case_id": "GO_molecular_function_0189",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "C8",
      "C9",
      "H1",
      "H3",
      "H4",
      "H5",
      "H6"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry B6ZKN1 (sequence matched, 540 AA) is annotated as 'Ipecac alkaloid beta-glucosidase 9' with EC 3.2.1.-, GO:0008422 (beta-glucosidase activity) assigned via IDA (Inferred by Direct Assay) from experimental evidence (PubMed:18927081). The function comment confirms 'Beta-glucosidase catalyzing deglucosylation on N-deacetylisoipecoside and N-deacetylipecoside,' and catalytic activity reactions show hydrolysis releasing D-glucose. This is experimental evidence (ECO:0000269), not mere computational prediction."
  },
  "important_caveats": [
    "The NEP motif identifies GH1 family membership but does not by itself guarantee beta-glucosidase specificity (GH1 also includes beta-galactosidases, beta-mannosidases, etc.); however, in plant GH1, beta-glucosidase is the dominant activity by a large margin.",
    "The reviewer-only evidence confirms experimental (IDA) annotation, but the evaluated model does not have access to this; the reasoning relies solely on sequence features and transferable family knowledge.",
    "The specific substrate (ipecac alkaloid glucosides) is unusual and would not be predictable from sequence alone, but the GO molecular function term 'beta-glucosidase activity' (GO:0008422) is correctly assigned based on the general catalytic mechanism (hydrolysis of terminal non-reducing beta-D-glucose residues)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The NEP motif is specific to GH1 and does not overlap with the structural requirements of ubiquitin transferases, 2OG dioxygenases, or Fe-S cluster binding proteins. While GH1 contains a few non-glucosidase members, the plant context and overwhelming statistical prevalence of beta-glucosidase in plant GH1 make D the clear best choice among the four options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0189",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry B6ZKN1 (sequence matched, 540 AA) is annotated as 'Ipecac alkaloid beta-glucosidase 9' with EC 3.2.1.-, GO:0008422 (beta-glucosidase activity) assigned via IDA (Inferred by Direct Assay) from experimental evidence (PubMed:18927081). The function comment confirms 'Beta-glucosidase catalyzing deglucosylation on N-deacetylisoipecoside and N-deacetylipecoside,' and catalytic activity reactions show hydrolysis releasing D-glucose. This is experimental evidence (ECO:0000269), not mere computational prediction.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "C8", "C9", "H1", "H3", "H4", "H5", "H6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the NEP catalytic motif (visible as 'WITINEP' around residues ~170-176), which is a well-established, transferable sequence signature of Glycoside Hydrolase family 1 (GH1). This motif is shared across many characterized GH1 proteins (e.g., E. coli BgaA, plant beta-glucosidases like prunasinase, amygdalase, and numerous plant GH1 enzymes). The overall ~540-residue length and (β/α)8 TIM-barrel architecture are consistent with GH1. Among GH1 enzymes in plants (suggested by the N-terminal signal-peptide-like region and plant-typical sequence composition), beta-glucosidase is by far the predominant activity. The other options can be excluded by absence of their diagnostic motifs: (A) ubiquitin-like transferases require RING/U-box/HECT/RBR domains absent here; (B) 2-oxoglutarate-dependent dioxygenases require the HxD/E…H facial triad and a double-stranded β-helix fold, neither present; (C) 2Fe-2S cluster binding requires CxxC…CxxC cysteine-rich coordination motifs, absent in this sequence. Thus, the NEP motif plus plant context plus absence of alternative-domain signatures provides a credible transferable inference favoring D.",
    "missing_item_specific_fact": "",
    "reason": "The NEP motif is a family-level sequence signature learned from many GH1 proteins, not specific to this exact entry. Combined with the plant context and the clear absence of motifs required by options A, B, and C, a knowledgeable model can meaningfully distinguish D from the alternatives without knowing the recorded answer for this specific protein."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The NEP motif is specific to GH1 and does not overlap with the structural requirements of ubiquitin transferases, 2OG dioxygenases, or Fe-S cluster binding proteins. While GH1 contains a few non-glucosidase members, the plant context and overwhelming statistical prevalence of beta-glucosidase in plant GH1 make D the clear best choice among the four options."
  },
  "important_caveats": [
    "The NEP motif identifies GH1 family membership but does not by itself guarantee beta-glucosidase specificity (GH1 also includes beta-galactosidases, beta-mannosidases, etc.); however, in plant GH1, beta-glucosidase is the dominant activity by a large margin.",
    "The reviewer-only evidence confirms experimental (IDA) annotation, but the evaluated model does not have access to this; the reasoning relies solely on sequence features and transferable family knowledge.",
    "The specific substrate (ipecac alkaloid glucosides) is unusual and would not be predictable from sequence alone, but the GO molecular function term 'beta-glucosidase activity' (GO:0008422) is correctly assigned based on the general catalytic mechanism (hydrolysis of terminal non-reducing beta-D-glucose residues)."
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
  "benchmark_sequence_length": 540,
  "benchmark_sequence_sha256": "dde22a5d2821467a0cea322bb9996061c5a8b224e2f2f4700e01315256b12a92",
  "current_entry_audit": {
    "entryVersion": 46,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2009-02-10",
    "sequenceVersion": 1
  },
  "current_record_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 540,
  "current_source_sequence_sha256": "dde22a5d2821467a0cea322bb9996061c5a8b224e2f2f4700e01315256b12a92",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 44,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "B6ZKN1",
  "selected_historical_entry_version": 44,
  "selected_historical_record_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "selected_historical_source_sequence_length": 540,
  "selected_historical_source_sequence_sha256": "dde22a5d2821467a0cea322bb9996061c5a8b224e2f2f4700e01315256b12a92",
  "selected_historical_version": {
    "accession": "B6ZKN1",
    "database": "Swiss-Prot",
    "entryVersion": 44,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "GLU9_CARIP",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"B6ZKN1\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":46,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2009-02-10\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Ipecac\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"asterids\",\"lamiids\",\"Gentianales\",\"Rubiaceae\",\"Rubioideae\",\"Palicoureeae\",\"Carapichea\"],\"scientificName\":\"Carapichea ipecacuanha\",\"synonyms\":[\"Callicocca ipecacuanha\"],\"taxonId\":77880}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"Ipecac alkaloid beta-glucosidase 9\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"IpeGLU9\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"value\":\"Beta-glucosidase catalyzing deglucosylation on N-deacetylisoipecoside and N-deacetylipecoside\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:78764\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"name\":\"deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:78763\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:4167\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:229554\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:78888\"}}],\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"name\":\"deacetylisoipecoside + H2O = deacetylisoipecoside aglycone + D-glucose\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:78887\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:4167\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58091\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:229557\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/2",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000314\",\"id\":\"18927081\",\"source\":\"PubMed\"}],\"id\":\"GO:0008422\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:beta-glucosidase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"IDA:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/4",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/B6ZKN1.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Nomura T.\",\"Quesada A.L.\",\"Kutchan T.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"18927081\"},{\"database\":\"DOI\",\"id\":\"10.1074/jbc.m806953200\"}],\"citationType\":\"journal article\",\"firstPage\":\"34650\",\"id\":\"18927081\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"34659\",\"publicationDate\":\"2008\",\"title\":\"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis in Psychotria ipecacuanha.\",\"volume\":\"283\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"BAH02552.1\",\"source\":\"EMBL\"}],\"referenceComments\":[{\"type\":\"TISSUE\",\"value\":\"Root\"},{\"type\":\"TISSUE\",\"value\":\"Shoot\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"PATHWAY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-02T04:27:22.416766+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "533a8f1f084446cafdad81e51f750d9c73bd15fd90f73f21d0baa135fa93014f",
  "url": "https://rest.uniprot.org/uniprotkb/B6ZKN1.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H1",
  "excerpt": "ID   GLU9_CARIP              Reviewed;         540 AA.\nAC   B6ZKN1;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   10-FEB-2009, sequence version 1.\nDT   28-JAN-2026, entry version 44.\nDE   RecName: Full=Ipecac alkaloid beta-glucosidase 9 {ECO:0000303|PubMed:18927081};\nDE            Short=IpeGLU9 {ECO:0000303|PubMed:18927081};\nDE            EC=3.2.1.- {ECO:0000269|PubMed:18927081};\nGN   Name=GLU9 {ECO:0000303|PubMed:18927081};\nOS   Carapichea ipecacuanha (Ipecac) (Callicocca ipecacuanha).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   asterids; lamiids; Gentianales; Rubiaceae; Rubioideae; Palicoureeae;\nOC   Carapichea.\nOX   NCBI_TaxID=77880;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-15",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H2",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:BAH02552.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, AND PATHWAY.\nRC   TISSUE=Root, and Shoot;\nRX   PubMed=18927081; DOI=10.1074/jbc.m806953200;\nRA   Nomura T., Quesada A.L., Kutchan T.M.;\nRT   \"The new beta-D-glucosidase in terpenoid-isoquinoline alkaloid biosynthesis\nRT   in Psychotria ipecacuanha.\";\nRL   J. Biol. Chem. 283:34650-34659(2008).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 16-23",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Beta-glucosidase catalyzing deglucosylation on N-\nCC       deacetylisoipecoside and N-deacetylipecoside.\nCC       {ECO:0000269|PubMed:18927081}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 24-26",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=deacetylipecoside + H2O = deacetylipecoside aglycone + D-\nCC         glucose; Xref=Rhea:RHEA:78763, ChEBI:CHEBI:4167, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:58379, ChEBI:CHEBI:229554;\nCC         Evidence={ECO:0000269|PubMed:18927081};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:78764;\nCC         Evidence={ECO:0000269|PubMed:18927081};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 27-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H5",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=deacetylisoipecoside + H2O = deacetylisoipecoside aglycone +\nCC         D-glucose; Xref=Rhea:RHEA:78887, ChEBI:CHEBI:4167, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:58091, ChEBI:CHEBI:229557;\nCC         Evidence={ECO:0000269|PubMed:18927081};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:78888;\nCC         Evidence={ECO:0000269|PubMed:18927081};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-40",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44)

```json
{
  "entry_version": 44,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0008422; F:beta-glucosidase activity; IDA:UniProtKB.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-02T04:27:24.525722+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 53-53",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "e900cc5e5ccff52df88efc2616972e26828fb58ed3af99a3d212b589186fe0ff",
  "url": "https://rest.uniprot.org/unisave/B6ZKN1?format=txt&versions=44"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0008422\nname: beta-glucosidase activity\nnamespace: molecular_function\nalt_id: GO:0016983\ndef: \"Catalysis of the hydrolysis of terminal, non-reducing beta-D-glucose residues with release of beta-D-glucose.\" [EC:3.2.1.21, PMID:12594539]\nsynonym: \"amygdalase activity\" NARROW [EC:3.2.1.21]\nsynonym: \"amygdalinase\" NARROW [EC:3.2.1.21]\nsynonym: \"arbutinase activity\" NARROW []\nsynonym: \"aryl-beta-glucosidase activity\" RELATED [EC:3.2.1.21]\nsynonym: \"beta-1,6-glucosidase activity\" RELATED [EC:3.2.1.21]\nsynonym: \"beta-D-glucosidase activity\" EXACT [EC:3.2.1.21]\nsynonym: \"beta-D-glucoside glucohydrolase activity\" RELATED [EC:3.2.1.21]\nsynonym: \"beta-glucoside glucohydrolase activity\" EXACT [EC:3.2.1.21]\nsynonym: \"cellobiase activity\" NARROW [EC:3.2.1.21]\nsynonym: \"cytokine beta-glucosidase activity\" NARROW []\nsynonym: \"elaterase activity\" NARROW []\nsynonym: \"emulsin\" RELATED [EC:3.2.1.21]\nsynonym: \"gentiobiase activity\" NARROW []\nsynonym: \"gentobiase activity\" NARROW [EC:3.2.1.21]\nsynonym: \"limarase activity\" NARROW []\nsynonym: \"p-nitrophenyl beta-glucosidase activity\" NARROW []\nsynonym: \"primeverosidase activity\" NARROW []\nsynonym: \"quercetin 3'-O-beta-D-glucopyranoside hydrolase activity\" NARROW []\nsynonym: \"quercetin 4'-O-beta-D-glucopyranoside hydrolase activity\" NARROW []\nsynonym: \"salicilinase activity\" NARROW []\nxref: EC:3.2.1.21\nxref: MetaCyc:3.2.1.21-RXN\nxref: RHEA:69647\nxref: RHEA:69655\nis_a: GO:0015926 ! glucosidase activity\nproperty_value: skos:exactMatch EC:3.2.1.21\nproperty_value: skos:narrowMatch RHEA:69647\nproperty_value: skos:narrowMatch RHEA:69655\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0008422",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 83077-83111",
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
  "excerpt": "[Term]\nid: GO:0016706\nname: 2-oxoglutarate-dependent dioxygenase activity\nnamespace: molecular_function\nalt_id: GO:0010302\ndef: \"Catalysis of the reaction: A + 2-oxoglutarate + O2 = B + succinate + CO2. This is an oxidation-reduction (redox) reaction in which hydrogen or electrons are transferred from 2-oxoglutarate and one other donor, and one atom of oxygen is incorporated into each donor.\" [GOC:mah]\nsynonym: \"2-oxoglutarate dioxygenase activity\" EXACT []\nsynonym: \"oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, 2-oxoglutarate as one donor, and incorporation of one atom each of oxygen into both donors\" EXACT []\nxref: EC:1.14.11.-\nxref: Reactome:R-HSA-1234164 \"Cytosolic HIF1AN (FIH1) hydroxylates asparagine residues of Hypoxia-inducible Factor Alpha (HIF1A,HIF2A)\"\nxref: Reactome:R-HSA-6783455 \"TYW5 hydroxylates yW-72 yielding OHyW-72 at nucleotide 37 of tRNA(Phe)\"\nis_a: GO:0016705 ! oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen\nis_a: GO:0051213 ! dioxygenase activity\nproperty_value: skos:exactMatch EC:1.14.11.-\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0016706",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 129228-129242",
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
  "excerpt": "[Term]\nid: GO:0019787\nname: ubiquitin-like protein transferase activity\nnamespace: molecular_function\nalt_id: GO:0008639\nalt_id: GO:0008640\ndef: \"Catalysis of the transfer of a ubiquitin-like from one protein to another via the reaction X-ULP + Y = Y-ULP + X, where both X-ULP and Y-ULP are covalent linkages. ULP represents a ubiquitin-like protein.\" [GOC:mah, GOC:rn, PMID:10806345, PMID:10884686]\nsubset: goslim_drosophila\nsubset: goslim_pir\nsynonym: \"E2\" BROAD []\nsynonym: \"E3\" RELATED [GOC:dph]\nsynonym: \"small conjugating protein ligase activity\" NARROW [GOC:dph]\nsynonym: \"small conjugating protein transferase activity\" EXACT [GOC:dph]\nsynonym: \"small protein conjugating enzyme activity\" NARROW []\nsynonym: \"ubiquitin-like conjugating enzyme activity\" NARROW []\nsynonym: \"ubiquitin-like-protein ligase activity\" NARROW []\nxref: Reactome:R-HSA-5678490 \"ATG16L1 complex transfers LC3 from ATG3 to PE\"\nxref: Reactome:R-HSA-688137 \"RIP2 is K63 polyubiquitinated\"\nis_a: GO:0016755 ! aminoacyltransferase activity\nis_a: GO:0140096 ! catalytic activity, acting on a protein\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0019787",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 153098-153118",
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

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 189. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
