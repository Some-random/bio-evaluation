# GO_molecular_function_0023

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/GO_molecular_function_0023.txt)

**Task:** `GO_molecular_function`  
**Expected answer:** **D** — beta-glucuronidase activity

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MLFPKDTLTREIKDLSGIWRFKADPDNRGREEKWHHQPLQDTIPMPVPASYNDITQDAALRDHIGDVWYEQTFIVPRSWSGDRMMLWIGSACHHAVVWVNGVEVASHKGGFLPFEADITRVAVPGRENRVTIVVNNVLNWQTLPPGRIKTFDDEKHPEGYRVQEYFHDFFNYAGLHRPVKLYRTSGLFIQDITITTDVQGESGVVGYSIECSQPEGEVRVKLLDEDGKEAATGKGSSGTLQVENARLWKPLQAYLYTLHVELLDSYGQLADHYQLQVGIRTVKVEGTRFLINGERFYFKGFGKHEDSDIRGKGLDQAVNVKDFNLLKWINANSFRTSHYPYAEELLELADREGIVVIGEVPAVGFTFFNYNDKVYTPDQANEETLAHHHDVLSDLIARDKNHPSVVMWSLANEAATFQDEAVPYFRQLADTARRLDPQRPITIVQWPLPDKCKVAQFFDVICVNRYYSWYQDPGALELVEHQVEWELTNWYRNFGKPVIMTEYGADAIAGFHQDPPVMFTEEYQEELLTRYHNVFDRLDFVIGEHVWAFADFATKQGITRINGNKKGVFTRQRQPKAAARMLRSRWGEMGEYPEKL

[Multiple Choices]
A. tetraketide alpha-pyrone synthase activity
B. 3-oxoacyl-[acyl-carrier-protein] synthase activity
C. histone H3K9me/H3K9me2 demethylase activity
D. beta-glucuronidase activity
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

> The sequence matches the annotated protein, and the supplied experimental annotation reports beta-glucuronidase activity against an artificial beta-D-glucuronide substrate. This supports option D, though it does not establish that this is the protein's sole or primary physiological activity.

Citations as saved: [C5](#evidence-c5), [C6](#evidence-c6).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long, soluble bacterial enzyme sequence is consistent with a carbohydrate-active enzyme profile. Transferable family and sequence-pattern knowledge can favor the carbohydrate glycoside option D over the fatty-acid-condensation activities in A and B and the Fe(II)/2-oxoglutarate-dependent demethylase activity in C. This is a probabilistic distinction, not proof of beta-glucuronide specificity.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The choices contrast substantially different enzyme classes, so a transferable carbohydrate-enzyme inference can meaningfully favor D. Exact substrate activity and physiological importance would require protein-specific evidence, but those finer facts are not necessary to distinguish the offered alternatives.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied experimental evidence supports beta-glucuronidase activity; none of the other choices describes a comparable carbohydrate-directed activity.


### Important caveats

- The reported beta-glucuronidase activity is demonstrated with an artificial substrate; the physiological role is described as probable.
- The cited study title refers to a glycoside phosphorylase, so option D should not be interpreted as an exhaustive description of the protein's activities.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long, soluble bacterial enzyme sequence is consistent with a carbohydrate-active enzyme profile. Transferable family and sequence-pattern knowledge can favor the carbohydrate glycoside option D over the fatty-acid-condensation activities in A and B and the Fe(II)/2-oxoglutarate-dependent demethylase activity in C. This is a probabilistic distinction, not proof of beta-glucuronide specificity.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The choices contrast substantially different enzyme classes, so a transferable carbohydrate-enzyme inference can meaningfully favor D. Exact substrate activity and physiological importance would require protein-specific evidence, but those finer facts are not necessary to distinguish the offered alternatives."
  },
  "case_id": "GO_molecular_function_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "C6"
    ],
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and the supplied experimental annotation reports beta-glucuronidase activity against an artificial beta-D-glucuronide substrate. This supports option D, though it does not establish that this is the protein's sole or primary physiological activity."
  },
  "important_caveats": [
    "The reported beta-glucuronidase activity is demonstrated with an artificial substrate; the physiological role is described as probable.",
    "The cited study title refers to a glycoside phosphorylase, so option D should not be interpreted as an exhaustive description of the protein's activities."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied experimental evidence supports beta-glucuronidase activity; none of the other choices describes a comparable carbohydrate-directed activity."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "GO_molecular_function_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence matches the annotated protein, and the supplied experimental annotation reports beta-glucuronidase activity against an artificial beta-D-glucuronide substrate. This supports option D, though it does not establish that this is the protein's sole or primary physiological activity.",
    "evidence_ids": ["C5", "C6"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long, soluble bacterial enzyme sequence is consistent with a carbohydrate-active enzyme profile. Transferable family and sequence-pattern knowledge can favor the carbohydrate glycoside option D over the fatty-acid-condensation activities in A and B and the Fe(II)/2-oxoglutarate-dependent demethylase activity in C. This is a probabilistic distinction, not proof of beta-glucuronide specificity.",
    "missing_item_specific_fact": "",
    "reason": "The choices contrast substantially different enzyme classes, so a transferable carbohydrate-enzyme inference can meaningfully favor D. Exact substrate activity and physiological importance would require protein-specific evidence, but those finer facts are not necessary to distinguish the offered alternatives."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied experimental evidence supports beta-glucuronidase activity; none of the other choices describes a comparable carbohydrate-directed activity."
  },
  "important_caveats": [
    "The reported beta-glucuronidase activity is demonstrated with an artificial substrate; the physiological role is described as probable.",
    "The cited study title refers to a glycoside phosphorylase, so option D should not be interpreted as an exhaustive description of the protein's activities."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A089LCJ8 (BGLR_PAEBO) is annotated as Beta-glucuronidase (EC 3.2.1.31) with experimental evidence (ECO:0000269, PubMed:35947916). The GO annotation GO:0004566 (beta-glucuronidase activity) is assigned with evidence code EXP:UniProtKB. The catalytic activity (a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol) was experimentally confirmed using the substrate p-nitrophenyl-beta-D-glucuronide (PNPG). The sequence matches the benchmark input exactly (SHA256 confirmed). The author's expected answer D is fully supported by experimental evidence.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [C7](#evidence-c7), [H1](#evidence-h1), [H3](#evidence-h3), [H4](#evidence-h4), [H5](#evidence-h5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options represent radically different enzyme classes: (A) a type III polyketide synthase (plant/fungal, ~400 aa, Cys-His-His triad, specific PKS fold), (B) a 3-oxoacyl-ACP synthase (bacterial fatty acid biosynthesis, typically 280-400 aa, cysteine-protease-like fold with Cys-His-His catalytic triad), (C) a histone H3K9 demethylase (eukaryotic JmjC-domain 2-oxoglutarate-dependent dioxygenase with conserved His-X-Asp/His-X-His motifs for Fe(II) coordination), and (D) a beta-glucuronidase (glycoside hydrolase, GH79 family, ~500-600 aa, TIM-barrel fold with conserved 'GE' motifs and Asp/Glu catalytic residues). The 596-aa length is inconsistent with typical FabH/FabB/FabF (~300-380 aa) or JmjC domains (~200 aa). The sequence contains multiple 'GE' motifs (e.g., 'GEVPAVG', 'GEHVWAFADF') and 'DIT' patterns characteristic of GH79 beta-glucuronidases, along with a hydrophobic/aromatic residue distribution consistent with a TIM-barrel glycoside hydrolase fold. The absence of JmjC-domain His/Asp/Glu coordination motifs rules out C; the absence of type III PKS features and the bacterial-like sequence composition argues against A; the size and glycoside-hydrolase motifs argue against B. Family-level knowledge of GH79 motifs learned from other beta-glucuronidases provides a credible positive identification.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The four options are sufficiently divergent in enzyme class, size, fold, and catalytic mechanism that transferable knowledge about protein families (GH79 glycoside hydrolases, Fab synthases, JmjC dioxygenases, type III PKS) and general structural biology (TIM barrel vs. cysteine protease fold vs. JmjC fold) allows meaningful discrimination. The 'GE' motifs and overall length are recognizable GH79 signatures learned from other beta-glucuronidases, not from this specific protein's record.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options represent entirely different enzyme classes with distinct folds, sizes, and catalytic mechanisms. The 596-aa length, presence of GH79-conserved 'GE' motifs, and absence of JmjC/PKS/Fab-specific features make D the clearly most defensible choice. No other option is supported by the sequence features.


### Important caveats

- The reviewer evidence confirms the annotation is based on experimental characterization (PubMed:35947916), not merely computational prediction.
- The model does not receive organism information; however, the sequence composition and absence of eukaryotic-specific features (JmjC domain) are discernible from the sequence itself.
- The GH79 family motif recognition argument relies on transferable pattern knowledge from other GH79 beta-glucuronidases, which is permitted transfer knowledge.
- The UniProt entry was first publicly released in April 2025; the benchmark construction date is unknown, so the annotation timeline relative to the benchmark is uncertain but does not affect the scientific validity of the answer.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options represent radically different enzyme classes: (A) a type III polyketide synthase (plant/fungal, ~400 aa, Cys-His-His triad, specific PKS fold), (B) a 3-oxoacyl-ACP synthase (bacterial fatty acid biosynthesis, typically 280-400 aa, cysteine-protease-like fold with Cys-His-His catalytic triad), (C) a histone H3K9 demethylase (eukaryotic JmjC-domain 2-oxoglutarate-dependent dioxygenase with conserved His-X-Asp/His-X-His motifs for Fe(II) coordination), and (D) a beta-glucuronidase (glycoside hydrolase, GH79 family, ~500-600 aa, TIM-barrel fold with conserved 'GE' motifs and Asp/Glu catalytic residues). The 596-aa length is inconsistent with typical FabH/FabB/FabF (~300-380 aa) or JmjC domains (~200 aa). The sequence contains multiple 'GE' motifs (e.g., 'GEVPAVG', 'GEHVWAFADF') and 'DIT' patterns characteristic of GH79 beta-glucuronidases, along with a hydrophobic/aromatic residue distribution consistent with a TIM-barrel glycoside hydrolase fold. The absence of JmjC-domain His/Asp/Glu coordination motifs rules out C; the absence of type III PKS features and the bacterial-like sequence composition argues against A; the size and glycoside-hydrolase motifs argue against B. Family-level knowledge of GH79 motifs learned from other beta-glucuronidases provides a credible positive identification.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The four options are sufficiently divergent in enzyme class, size, fold, and catalytic mechanism that transferable knowledge about protein families (GH79 glycoside hydrolases, Fab synthases, JmjC dioxygenases, type III PKS) and general structural biology (TIM barrel vs. cysteine protease fold vs. JmjC fold) allows meaningful discrimination. The 'GE' motifs and overall length are recognizable GH79 signatures learned from other beta-glucuronidases, not from this specific protein's record."
  },
  "case_id": "GO_molecular_function_0023",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "C7",
      "H1",
      "H3",
      "H4",
      "H5"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A089LCJ8 (BGLR_PAEBO) is annotated as Beta-glucuronidase (EC 3.2.1.31) with experimental evidence (ECO:0000269, PubMed:35947916). The GO annotation GO:0004566 (beta-glucuronidase activity) is assigned with evidence code EXP:UniProtKB. The catalytic activity (a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol) was experimentally confirmed using the substrate p-nitrophenyl-beta-D-glucuronide (PNPG). The sequence matches the benchmark input exactly (SHA256 confirmed). The author's expected answer D is fully supported by experimental evidence."
  },
  "important_caveats": [
    "The reviewer evidence confirms the annotation is based on experimental characterization (PubMed:35947916), not merely computational prediction.",
    "The model does not receive organism information; however, the sequence composition and absence of eukaryotic-specific features (JmjC domain) are discernible from the sequence itself.",
    "The GH79 family motif recognition argument relies on transferable pattern knowledge from other GH79 beta-glucuronidases, which is permitted transfer knowledge.",
    "The UniProt entry was first publicly released in April 2025; the benchmark construction date is unknown, so the annotation timeline relative to the benchmark is uncertain but does not affect the scientific validity of the answer."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different enzyme classes with distinct folds, sizes, and catalytic mechanisms. The 596-aa length, presence of GH79-conserved 'GE' motifs, and absence of JmjC/PKS/Fab-specific features make D the clearly most defensible choice. No other option is supported by the sequence features."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "GO_molecular_function_0023",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A089LCJ8 (BGLR_PAEBO) is annotated as Beta-glucuronidase (EC 3.2.1.31) with experimental evidence (ECO:0000269, PubMed:35947916). The GO annotation GO:0004566 (beta-glucuronidase activity) is assigned with evidence code EXP:UniProtKB. The catalytic activity (a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol) was experimentally confirmed using the substrate p-nitrophenyl-beta-D-glucuronide (PNPG). The sequence matches the benchmark input exactly (SHA256 confirmed). The author's expected answer D is fully supported by experimental evidence.",
    "evidence_ids": ["C4", "C5", "C6", "C7", "H1", "H3", "H4", "H5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four options represent radically different enzyme classes: (A) a type III polyketide synthase (plant/fungal, ~400 aa, Cys-His-His triad, specific PKS fold), (B) a 3-oxoacyl-ACP synthase (bacterial fatty acid biosynthesis, typically 280-400 aa, cysteine-protease-like fold with Cys-His-His catalytic triad), (C) a histone H3K9 demethylase (eukaryotic JmjC-domain 2-oxoglutarate-dependent dioxygenase with conserved His-X-Asp/His-X-His motifs for Fe(II) coordination), and (D) a beta-glucuronidase (glycoside hydrolase, GH79 family, ~500-600 aa, TIM-barrel fold with conserved 'GE' motifs and Asp/Glu catalytic residues). The 596-aa length is inconsistent with typical FabH/FabB/FabF (~300-380 aa) or JmjC domains (~200 aa). The sequence contains multiple 'GE' motifs (e.g., 'GEVPAVG', 'GEHVWAFADF') and 'DIT' patterns characteristic of GH79 beta-glucuronidases, along with a hydrophobic/aromatic residue distribution consistent with a TIM-barrel glycoside hydrolase fold. The absence of JmjC-domain His/Asp/Glu coordination motifs rules out C; the absence of type III PKS features and the bacterial-like sequence composition argues against A; the size and glycoside-hydrolase motifs argue against B. Family-level knowledge of GH79 motifs learned from other beta-glucuronidases provides a credible positive identification.",
    "missing_item_specific_fact": "",
    "reason": "The four options are sufficiently divergent in enzyme class, size, fold, and catalytic mechanism that transferable knowledge about protein families (GH79 glycoside hydrolases, Fab synthases, JmjC dioxygenases, type III PKS) and general structural biology (TIM barrel vs. cysteine protease fold vs. JmjC fold) allows meaningful discrimination. The 'GE' motifs and overall length are recognizable GH79 signatures learned from other beta-glucuronidases, not from this specific protein's record."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options represent entirely different enzyme classes with distinct folds, sizes, and catalytic mechanisms. The 596-aa length, presence of GH79-conserved 'GE' motifs, and absence of JmjC/PKS/Fab-specific features make D the clearly most defensible choice. No other option is supported by the sequence features."
  },
  "important_caveats": [
    "The reviewer evidence confirms the annotation is based on experimental characterization (PubMed:35947916), not merely computational prediction.",
    "The model does not receive organism information; however, the sequence composition and absence of eukaryotic-specific features (JmjC domain) are discernible from the sequence itself.",
    "The GH79 family motif recognition argument relies on transferable pattern knowledge from other GH79 beta-glucuronidases, which is permitted transfer knowledge.",
    "The UniProt entry was first publicly released in April 2025; the benchmark construction date is unknown, so the annotation timeline relative to the benchmark is uncertain but does not affect the scientific validity of the answer."
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
  "benchmark_sequence_sha256": "92ddb41573a2c8ca97687a2ec29d37e183cbd01214b1e420a77dcd55150f4b9c",
  "current_entry_audit": {
    "entryVersion": 43,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2014-11-26",
    "sequenceVersion": 1
  },
  "current_record_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 596,
  "current_source_sequence_sha256": "92ddb41573a2c8ca97687a2ec29d37e183cbd01214b1e420a77dcd55150f4b9c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 41,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "A0A089LCJ8",
  "selected_historical_entry_version": 41,
  "selected_historical_record_sha256": "7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562",
  "selected_historical_source_sequence_length": 596,
  "selected_historical_source_sequence_sha256": "92ddb41573a2c8ca97687a2ec29d37e183cbd01214b1e420a77dcd55150f4b9c",
  "selected_historical_version": {
    "accession": "A0A089LCJ8",
    "database": "Swiss-Prot",
    "entryVersion": 41,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "BGLR_PAEBO",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0A089LCJ8\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":43,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2014-11-26\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Bacillati\",\"Bacillota\",\"Bacilli\",\"Caryophanales\",\"Paenibacillaceae\",\"Paenibacillus\"],\"scientificName\":\"Paenibacillus borealis\",\"taxonId\":160799}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.31\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"value\":\"Beta-glucuronidase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"FUNCTION\",\"texts\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"value\":\"Displays beta-glucuronidase activity with the artificial substrate p-nitrophenyl-beta-D-glucuronide (PNPG) (PubMed:35947916). Is probably involved in the metabolism of oligosaccharides containing the 3-O-beta-D-glucopyranosyl-beta-D-glucuronide structure released from bacterial and plant acidic carbohydrates (PubMed:35947916)\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/0",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"3.2.1.31\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"name\":\"a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:17633\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:30879\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58720\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:83411\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence C7

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C7",
  "excerpt": "{\"database\":\"GO\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"35947916\",\"source\":\"PubMed\"}],\"id\":\"GO:0004566\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:beta-glucuronidase activity\"},{\"key\":\"GoEvidenceType\",\"value\":\"EXP:UniProtKB\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/10",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence C8

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C8",
  "excerpt": "{\"database\":\"GO\",\"id\":\"GO:0030246\",\"properties\":[{\"key\":\"GoTerm\",\"value\":\"F:carbohydrate binding\"},{\"key\":\"GoEvidenceType\",\"value\":\"IEA:TreeGrafter\"}]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/uniProtKBCrossReferences/11",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence C9

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C9",
  "excerpt": "{\"citation\":{\"authors\":[\"Isono N.\",\"Mizutani E.\",\"Hayashida H.\",\"Katsuzaki H.\",\"Saburi W.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"35947916\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.bbrc.2022.07.098\"}],\"citationType\":\"journal article\",\"firstPage\":\"60\",\"id\":\"35947916\",\"journal\":\"Biochem. Biophys. Res. Commun.\",\"lastPage\":\"65\",\"publicationDate\":\"2022\",\"title\":\"Functional characterization of a novel GH94 glycoside phosphorylase, 3-O-beta-d-glucopyranosyl beta-d-glucuronide phosphorylase, and implication of the metabolic pathway of acidic carbohydrates in Paenibacillus borealis.\",\"volume\":\"625\"},\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"DSM 13188 / CCUG 43137 / CIP 107056 / KCTC 3805 / KK19\"}],\"referenceNumber\":2,\"referencePositions\":[\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"BIOPHYSICOCHEMICAL PROPERTIES\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/1",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H1",
  "excerpt": "ID   BGLR_PAEBO              Reviewed;         596 AA.\nAC   A0A089LCJ8;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   26-NOV-2014, sequence version 1.\nDT   28-JAN-2026, entry version 41.\nDE   RecName: Full=Beta-glucuronidase {ECO:0000303|PubMed:35947916};\nDE            EC=3.2.1.31 {ECO:0000269|PubMed:35947916};\nGN   ORFNames=PBOR_13360 {ECO:0000312|EMBL:AIQ57810.1};\nOS   Paenibacillus borealis.\nOC   Bacteria; Bacillati; Bacillota; Bacilli; Bacillales; Paenibacillaceae;\nOC   Paenibacillus.\nOX   NCBI_TaxID=160799;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-12",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562",
  "url": "https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H2",
  "excerpt": "RN   [2]\nRP   FUNCTION, CATALYTIC ACTIVITY, AND BIOPHYSICOCHEMICAL PROPERTIES.\nRC   STRAIN=DSM 13188 / CCUG 43137 / CIP 107056 / KCTC 3805 / KK19;\nRX   PubMed=35947916; DOI=10.1016/j.bbrc.2022.07.098;\nRA   Isono N., Mizutani E., Hayashida H., Katsuzaki H., Saburi W.;\nRT   \"Functional characterization of a novel GH94 glycoside phosphorylase, 3-O-\nRT   beta-d-glucopyranosyl beta-d-glucuronide phosphorylase, and implication of\nRT   the metabolic pathway of acidic carbohydrates in Paenibacillus borealis.\";\nRL   Biochem. Biophys. Res. Commun. 625:60-65(2022).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 19-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562",
  "url": "https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H3",
  "excerpt": "CC   -!- FUNCTION: Displays beta-glucuronidase activity with the artificial\nCC       substrate p-nitrophenyl-beta-D-glucuronide (PNPG) (PubMed:35947916). Is\nCC       probably involved in the metabolism of oligosaccharides containing the\nCC       3-O-beta-D-glucopyranosyl-beta-D-glucuronide structure released from\nCC       bacterial and plant acidic carbohydrates (PubMed:35947916).\nCC       {ECO:0000269|PubMed:35947916}.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 28-33",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562",
  "url": "https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol;\nCC         Xref=Rhea:RHEA:17633, ChEBI:CHEBI:15377, ChEBI:CHEBI:30879,\nCC         ChEBI:CHEBI:58720, ChEBI:CHEBI:83411; EC=3.2.1.31;\nCC         Evidence={ECO:0000269|PubMed:35947916};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 34-38",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562",
  "url": "https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41"
}
```

### Evidence H5

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H5",
  "excerpt": "DR   GO; GO:0004566; F:beta-glucuronidase activity; IEA:UniProtKB-EC.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 68-68",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562",
  "url": "https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41"
}
```

### Evidence H6

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H6",
  "excerpt": "DR   GO; GO:0030246; F:carbohydrate binding; IEA:TreeGrafter.\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 69-69",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562",
  "url": "https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41"
}
```

### Evidence GO1

[Gene Ontology current ontology](https://current.geneontology.org/ontology/go-basic.obo)

```json
{
  "evidence_id": "GO1",
  "excerpt": "[Term]\nid: GO:0004315\nname: 3-oxoacyl-[acyl-carrier-protein] synthase activity\nnamespace: molecular_function\nalt_id: GO:0033817\ndef: \"Catalysis of the reaction: acyl-[acyl-carrier protein] + malonyl-[acyl-carrier protein] = 3-oxoacyl-[acyl-carrier protein] + CO2 + [acyl-carrier protein].\" [RHEA:22836]\ncomment: Note that this activity is responsible for the chain-elongation step of dissociated (type II) fatty-acid biosynthesis, i.e. the addition of two C atoms to the fatty-acid chain. Can use fatty acyl thioesters of ACP (C2 to C16) as substrates, as well as fatty acyl thioesters of Co-A (C4 to C16).\nsynonym: \"3-ketoacyl-acyl carrier protein synthase activity\" RELATED [EC:2.3.1.41]\nsynonym: \"3-oxoacyl-[acyl-carrier protein] synthase activity\" EXACT []\nsynonym: \"3-oxoacyl-ACP synthase activity\" EXACT []\nsynonym: \"3-oxoacyl-acyl carrier protein synthase I activity\" NARROW [EC:2.3.1.179]\nsynonym: \"3-oxoacyl-acyl-carrier-protein synthase activity\" RELATED [EC:2.3.1.41]\nsynonym: \"acyl-acyl-carrier-protein:malonyl-acyl-carrier-protein C-acyltransferase (decarboxylating)\" RELATED [EC:2.3.1.41]\nsynonym: \"acyl-malonyl acyl carrier protein-condensing enzyme activity\" RELATED [EC:2.3.1.41]\nsynonym: \"acyl-malonyl(acyl-carrier-protein)-condensing enzyme activity\" RELATED [EC:2.3.1.41]\nsynonym: \"beta-ketoacyl acyl carrier protein synthase activity\" RELATED [EC:2.3.1.41]\nsynonym: \"beta-ketoacyl synthetase activity\" RELATED [EC:2.3.1.41]\nsynonym: \"beta-ketoacyl-[acyl carrier protein] synthase activity\" RELATED [EC:2.3.1.41]\nsynonym: \"beta-ketoacyl-ACP synthase I activity\" NARROW [EC:2.3.1.41]\nsynonym: \"beta-ketoacyl-ACP synthase II activity\" NARROW [EC:2.3.1.179]\nsynonym: \"beta-ketoacyl-ACP synthetase activity\" RELATED [EC:2.3.1.41]\nsynonym: \"beta-ketoacyl-acyl carrier protein synthase activity\" RELATED [EC:2.3.1.41]\nsynonym: \"beta-ketoacyl-acyl carrier protein synthetase activity\" RELATED [EC:2.3.1.41]\nsynonym: \"beta-ketoacyl-acyl-carrier-protein synthase I\" NARROW [EC:2.3.1.41]\nsynonym: \"beta-ketoacyl-acyl-carrier-protein synthase II activity\" NARROW []\nsynonym: \"beta-ketoacylsynthase activity\" RELATED [EC:2.3.1.41]\nsynonym: \"condensing enzyme activity\" BROAD [EC:2.3.1.41]\nsynonym: \"fatty acid condensing enzyme activity\" BROAD [EC:2.3.1.41]\nsynonym: \"ketoacyl-ACP synthase activity\" EXACT []\nxref: EC:2.3.1.179\nxref: EC:2.3.1.41\nxref: MetaCyc:2.3.1.179-RXN\nxref: MetaCyc:3-OXOACYL-ACP-SYNTH-RXN\nxref: RHEA:14565\nxref: RHEA:22836\nxref: RHEA:41800\nxref: RHEA:41820\nxref: RHEA:41836\nxref: RHEA:41852\nxref: RHEA:41868\nxref: RHEA:41884\nxref: RHEA:41900\nxref: RHEA:41916\nxref: RHEA:42248\nxref: RHEA:42252\nxref: RHEA:42260\nxref: RHEA:42268\nxref: RHEA:42272\nxref: RHEA:42276\nxref: RHEA:47824\nxref: RHEA:54924\nxref: RHEA:54940\nxref: RHEA:55040\nxref: RHEA:65308\nxref: RHEA:65312\nis_a: GO:0016747 ! acyltransferase activity, transferring groups other than amino-acyl groups\nproperty_value: skos:exactMatch EC:2.3.1.41\nproperty_value: skos:exactMatch MetaCyc:3-OXOACYL-ACP-SYNTH-RXN\nproperty_value: skos:exactMatch RHEA:22836\nproperty_value: skos:narrowMatch EC:2.3.1.179\nproperty_value: skos:narrowMatch MetaCyc:2.3.1.179-RXN\nproperty_value: skos:narrowMatch RHEA:14565\nproperty_value: skos:narrowMatch RHEA:41800\nproperty_value: skos:narrowMatch RHEA:41820\nproperty_value: skos:narrowMatch RHEA:41836\nproperty_value: skos:narrowMatch RHEA:41852\nproperty_value: skos:narrowMatch RHEA:41868\nproperty_value: skos:narrowMatch RHEA:41884\nproperty_value: skos:narrowMatch RHEA:41900\nproperty_value: skos:narrowMatch RHEA:41916\nproperty_value: skos:narrowMatch RHEA:42248\nproperty_value: skos:narrowMatch RHEA:42252\nproperty_value: skos:narrowMatch RHEA:42260\nproperty_value: skos:narrowMatch RHEA:42268\nproperty_value: skos:narrowMatch RHEA:42272\nproperty_value: skos:narrowMatch RHEA:42276\nproperty_value: skos:narrowMatch RHEA:47824\nproperty_value: skos:narrowMatch RHEA:54924\nproperty_value: skos:narrowMatch RHEA:54940\nproperty_value: skos:narrowMatch RHEA:55040\nproperty_value: skos:narrowMatch RHEA:65308\nproperty_value: skos:narrowMatch RHEA:65312\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004315",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 39629-39711",
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
  "excerpt": "[Term]\nid: GO:0004566\nname: beta-glucuronidase activity\nnamespace: molecular_function\ndef: \"Catalysis of the reaction: a beta-D-glucuronoside + H2O = an alcohol + D-glucuronate.\" [EC:3.2.1.31]\nsynonym: \"beta-D-glucuronoside glucuronosohydrolase activity\" RELATED [EC:3.2.1.31]\nsynonym: \"beta-glucuronide glucuronohydrolase activity\" RELATED [EC:3.2.1.31]\nsynonym: \"exo-beta-D-glucuronidase activity\" RELATED [EC:3.2.1.31]\nsynonym: \"glucuronidase activity\" RELATED [EC:3.2.1.31]\nsynonym: \"ketodase activity\" RELATED [EC:3.2.1.31]\nxref: EC:3.2.1.31\nxref: MetaCyc:BETA-GLUCURONID-RXN\nxref: Reactome:R-HSA-1678854 \"GUSB tetramer hydrolyses CS/HS precursor\"\nxref: Reactome:R-HSA-2162226 \"GUSB tetramer hydrolyzes GlcA-1,3-GlcNAc\"\nxref: Reactome:R-HSA-2162227 \"GUSB tetramer hydrolyses (HA)2\"\nxref: Reactome:R-HSA-2318373 \"Defective GUSB does not hydrolyse (HA)2\"\nxref: Reactome:R-HSA-9036068 \"Defective GUSB does not hydrolyse GlcA-1,3-GlcNAc\"\nxref: Reactome:R-HSA-9036070 \"Defective GUSB does not hydrolyse CS/HS precursor\"\nxref: RHEA:17633\nxref: RHEA:28326\nxref: RHEA:30475\nxref: RHEA:76111\nis_a: GO:0046574 ! glucuronidase activity\nproperty_value: skos:exactMatch EC:3.2.1.31\nproperty_value: skos:exactMatch RHEA:17633\nproperty_value: skos:narrowMatch RHEA:28326\nproperty_value: skos:narrowMatch RHEA:30475\nproperty_value: skos:narrowMatch RHEA:76111\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0004566",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 44488-44516",
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
  "excerpt": "[Term]\nid: GO:0090439\nname: tetraketide alpha-pyrone synthase activity\nnamespace: molecular_function\ndef: \"Catalyzes the reaction: 7-hydroxylauroyl-CoA + 3 malonyl-CoA + 2 H+ = 2-(8-hydroxy-2-oxotridecyl)-6-oxopyran-4-olate + 3 CO2 + 4 coenzyme A.\" [MetaCyc:RXN-16407, PMID:21193570]\nxref: MetaCyc:RXN-16407\nis_a: GO:0016747 ! acyltransferase activity, transferring groups other than amino-acyl groups\nproperty_value: skos:exactMatch MetaCyc:RXN-16407\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0090439",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 399100-399108",
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
  "excerpt": "[Term]\nid: GO:0140683\nname: histone H3K9me/H3K9me2 demethylase activity\nnamespace: molecular_function\ndef: \"Catalysis of the removal of a methyl group from a di or a monomethyl-lysine residue at position 9 of the histone H3 protein. This is a dioxygenase reaction that is dependent on Fe(II) and 2-oxoglutarate.\" [PMID:16603238]\ncomment: Comment: Note that the residue position corresponds to the canonical human H3 histone (UniProtKB:P84243); this residue is conserved across all eukaryotes. Residue 1 is the first residue following removal of the initiating Methionine (Met). Note that each histone is encoded by multiple genes, and sequences may vary across different genes within an organism.\nsynonym: \"histone H3-di/monomethyl-lysine-9 demethylase activity\" EXACT []\nsynonym: \"histone H3K9me demethylase activity\" BROAD []\nsynonym: \"histone H3K9me2 demethylase activity\" BROAD []\nxref: EC:1.14.11.65\nxref: RHEA:60188\nis_a: GO:0016706 ! 2-oxoglutarate-dependent dioxygenase activity\nis_a: GO:0032454 ! histone H3K9 demethylase activity\nproperty_value: skos:exactMatch EC:1.14.11.65\nproperty_value: skos:exactMatch RHEA:60188\n\n",
  "excerpt_format": "literal contiguous OBO lines",
  "go_id": "GO:0140683",
  "retrieved_utc": "2026-11-01T07:04:24.975173+00:00",
  "source": "Gene Ontology current ontology",
  "source_locator": "lines 442495-442510",
  "source_scope": "current ontology; exact historical benchmark ontology unknown",
  "source_sha256": "b08d45b268b8c24ccb2513dbbbc7d4df9f6521c099b413f79eb31e06e0fa3bcc",
  "url": "https://current.geneontology.org/ontology/go-basic.obo"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/GO_molecular_function.json), zero-based source row 23. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
