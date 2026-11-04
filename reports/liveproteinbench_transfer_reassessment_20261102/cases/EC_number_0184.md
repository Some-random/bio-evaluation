# EC_number_0184

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/EC_number_0184.txt)

**Task:** `EC_number`  
**Expected answer:** **C** — 3.2.1.31

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
A. 3.2.1.8
B. 6.3.2.35
C. 3.2.1.31
D. 1.14.15.9
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Commission (EC) Number Prediction, which is to predict the complete 4-digit Enzyme Commission (EC) number for a given protein. The EC number is a numerical classification that categorizes enzymes based on the chemical reactions they catalyze. You should select the most accurate EC number from the provided options based on the protein's sequence.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt entry assigns EC 3.2.1.31 and specifies the beta-D-glucuronoside hydrolysis reaction, citing experimental evidence (ECO:0000269). This supports choice C, though the underlying paper was not independently reviewed here.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 596-aa sequence has the length and apparent multidomain character expected of a GH2-like glycoside hydrolase. That family-level sequence/architecture inference favors beta-glucuronidase (EC 3.2.1.31, C) over the typically distinct xylanase glycosidase class (EC 3.2.1.8, A); the ligase and oxidoreductase options are still less compatible with a glycoside-hydrolase sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A transferable glycoside-hydrolase family inference provides a meaningful basis for distinguishing the offered choices. It is not a guarantee of substrate specificity, but the alternatives do not require exact-protein annotation lookup to make a reasoned selection.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The family-level inference favors C among the listed alternatives; no other option is comparably supported by the supplied sequence.


### Important caveats

- The experimental support is reported in a sequence-matched database annotation citing a publication; the publication itself was not independently examined.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 596-aa sequence has the length and apparent multidomain character expected of a GH2-like glycoside hydrolase. That family-level sequence/architecture inference favors beta-glucuronidase (EC 3.2.1.31, C) over the typically distinct xylanase glycosidase class (EC 3.2.1.8, A); the ligase and oxidoreductase options are still less compatible with a glycoside-hydrolase sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A transferable glycoside-hydrolase family inference provides a meaningful basis for distinguishing the offered choices. It is not a guarantee of substrate specificity, but the alternatives do not require exact-protein annotation lookup to make a reasoned selection."
  },
  "case_id": "EC_number_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.2.1.31 and specifies the beta-D-glucuronoside hydrolysis reaction, citing experimental evidence (ECO:0000269). This supports choice C, though the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The experimental support is reported in a sequence-matched database annotation citing a publication; the publication itself was not independently examined."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level inference favors C among the listed alternatives; no other option is comparably supported by the supplied sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "EC_number_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry assigns EC 3.2.1.31 and specifies the beta-D-glucuronoside hydrolysis reaction, citing experimental evidence (ECO:0000269). This supports choice C, though the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C4", "C5"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 596-aa sequence has the length and apparent multidomain character expected of a GH2-like glycoside hydrolase. That family-level sequence/architecture inference favors beta-glucuronidase (EC 3.2.1.31, C) over the typically distinct xylanase glycosidase class (EC 3.2.1.8, A); the ligase and oxidoreductase options are still less compatible with a glycoside-hydrolase sequence.",
    "missing_item_specific_fact": "",
    "reason": "A transferable glycoside-hydrolase family inference provides a meaningful basis for distinguishing the offered choices. It is not a guarantee of substrate specificity, but the alternatives do not require exact-protein annotation lookup to make a reasoned selection."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The family-level inference favors C among the listed alternatives; no other option is comparably supported by the supplied sequence."
  },
  "important_caveats": [
    "The experimental support is reported in a sequence-matched database annotation citing a publication; the publication itself was not independently examined."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry (A0A089LCJ8, BGLR_PAEBO) annotates this protein as Beta-glucuronidase with EC 3.2.1.31, supported by experimental evidence (ECO:0000269, PubMed:35947916). The catalytic activity is confirmed as 'a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol' (Rhea:RHEA:17633). The sequence match is exact (SHA256 identical) between the benchmark input and the source entry. The annotation is based on functional characterization (FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES) from the Isono et al. 2022 paper.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence (~596 aa) contains multiple tryptophan residues in patterns typical of glycoside-binding sites (WYEQ, WIGSACHHAVVWVNG, WYRNFGKPVIMTEYG), and the overall architecture is consistent with a glycoside hydrolase (EC 3.2.x.x), immediately eliminating B (EC 6.3.2.35, glutamine synthase, a ligase with distinct ATP-binding and glutamine synthetase motifs) and D (EC 1.14.15.9, peptidylglycine α-amidating monooxygenase, an oxidoreductase with copper-binding motifs). For the remaining A (3.2.1.8, endo-β-1,4-glucanase/cellulase) vs C (3.2.1.31, beta-glucuronidase): the ~596 aa length is most consistent with GH2 family proteins (e.g., E. coli GusA beta-glucuronidase is ~603 aa), whereas typical cellulase families (GH5 ~400-500 aa, GH9 ~700-800 aa) differ in size. The sequence contains conserved Glu-containing motifs (e.g., 'DDEKHPEGY') reminiscent of GH2 catalytic residues. GH2 beta-glucuronidases are a well-characterized family with distinctive TIM-barrel architecture and conserved catalytic Glu pairs, distinguishable from cellulase families by sequence-level family signatures learned from homologs. This provides a probabilistic but credible family-level inference favoring C over A.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> Elimination of B and D is straightforward from recognizing the sequence as a hydrolase. The A vs C distinction relies on family-level knowledge of glycoside hydrolase families (GH2 beta-glucuronidases vs GH5/GH9 cellulases), including sequence length patterns and conserved catalytic motifs transferable from well-characterized homologs. While the distinction is not airtight (the protein is actually GH94-related per the reference, making the EC assignment somewhat atypical for its family), the offered choices are distinguishable through family-level inference about GH2-like features versus cellulase-family features.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> B and D are clearly eliminated as the sequence shows glycoside hydrolase features. Between A and C, while both are glycoside hydrolases, the family-level features (length, motifs, architecture) more consistently align with GH2 beta-glucuronidase than with typical cellulase families. No other option is seriously defensible.


### Important caveats

- The reference paper (PubMed:35947916) describes this protein as a 'GH94 glycoside phosphorylase' acting on glucuronides, yet the EC annotation is 3.2.1.31 (a hydrolase EC, not a phosphorylase EC 2.4.x.x). The EC assignment reflects observed hydrolytic activity rather than strict family assignment, which is somewhat unusual and could confuse a model familiar with GH94 phosphorylases.
- The A vs C distinction (cellulase vs beta-glucuronidase) is genuinely challenging from sequence alone; the family-level argument is probabilistic rather than definitive.
- The UniProt annotation is Swiss-Prot reviewed with experimental evidence (ECO:0000269), providing strong support for the key.
- The sequence identity between benchmark input and source entry is exact (SHA256 match confirmed in both current and historical snapshots).

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence (~596 aa) contains multiple tryptophan residues in patterns typical of glycoside-binding sites (WYEQ, WIGSACHHAVVWVNG, WYRNFGKPVIMTEYG), and the overall architecture is consistent with a glycoside hydrolase (EC 3.2.x.x), immediately eliminating B (EC 6.3.2.35, glutamine synthase, a ligase with distinct ATP-binding and glutamine synthetase motifs) and D (EC 1.14.15.9, peptidylglycine α-amidating monooxygenase, an oxidoreductase with copper-binding motifs). For the remaining A (3.2.1.8, endo-β-1,4-glucanase/cellulase) vs C (3.2.1.31, beta-glucuronidase): the ~596 aa length is most consistent with GH2 family proteins (e.g., E. coli GusA beta-glucuronidase is ~603 aa), whereas typical cellulase families (GH5 ~400-500 aa, GH9 ~700-800 aa) differ in size. The sequence contains conserved Glu-containing motifs (e.g., 'DDEKHPEGY') reminiscent of GH2 catalytic residues. GH2 beta-glucuronidases are a well-characterized family with distinctive TIM-barrel architecture and conserved catalytic Glu pairs, distinguishable from cellulase families by sequence-level family signatures learned from homologs. This provides a probabilistic but credible family-level inference favoring C over A.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "Elimination of B and D is straightforward from recognizing the sequence as a hydrolase. The A vs C distinction relies on family-level knowledge of glycoside hydrolase families (GH2 beta-glucuronidases vs GH5/GH9 cellulases), including sequence length patterns and conserved catalytic motifs transferable from well-characterized homologs. While the distinction is not airtight (the protein is actually GH94-related per the reference, making the EC assignment somewhat atypical for its family), the offered choices are distinguishable through family-level inference about GH2-like features versus cellulase-family features."
  },
  "case_id": "EC_number_0184",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry (A0A089LCJ8, BGLR_PAEBO) annotates this protein as Beta-glucuronidase with EC 3.2.1.31, supported by experimental evidence (ECO:0000269, PubMed:35947916). The catalytic activity is confirmed as 'a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol' (Rhea:RHEA:17633). The sequence match is exact (SHA256 identical) between the benchmark input and the source entry. The annotation is based on functional characterization (FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES) from the Isono et al. 2022 paper."
  },
  "important_caveats": [
    "The reference paper (PubMed:35947916) describes this protein as a 'GH94 glycoside phosphorylase' acting on glucuronides, yet the EC annotation is 3.2.1.31 (a hydrolase EC, not a phosphorylase EC 2.4.x.x). The EC assignment reflects observed hydrolytic activity rather than strict family assignment, which is somewhat unusual and could confuse a model familiar with GH94 phosphorylases.",
    "The A vs C distinction (cellulase vs beta-glucuronidase) is genuinely challenging from sequence alone; the family-level argument is probabilistic rather than definitive.",
    "The UniProt annotation is Swiss-Prot reviewed with experimental evidence (ECO:0000269), providing strong support for the key.",
    "The sequence identity between benchmark input and source entry is exact (SHA256 match confirmed in both current and historical snapshots)."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and D are clearly eliminated as the sequence shows glycoside hydrolase features. Between A and C, while both are glycoside hydrolases, the family-level features (length, motifs, architecture) more consistently align with GH2 beta-glucuronidase than with typical cellulase families. No other option is seriously defensible."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "EC_number_0184",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry (A0A089LCJ8, BGLR_PAEBO) annotates this protein as Beta-glucuronidase with EC 3.2.1.31, supported by experimental evidence (ECO:0000269, PubMed:35947916). The catalytic activity is confirmed as 'a beta-D-glucuronoside + H2O = D-glucuronate + an alcohol' (Rhea:RHEA:17633). The sequence match is exact (SHA256 identical) between the benchmark input and the source entry. The annotation is based on functional characterization (FUNCTION, CATALYTIC ACTIVITY, BIOPHYSICOCHEMICAL PROPERTIES) from the Isono et al. 2022 paper.",
    "evidence_ids": ["C4", "C5", "C6", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence (~596 aa) contains multiple tryptophan residues in patterns typical of glycoside-binding sites (WYEQ, WIGSACHHAVVWVNG, WYRNFGKPVIMTEYG), and the overall architecture is consistent with a glycoside hydrolase (EC 3.2.x.x), immediately eliminating B (EC 6.3.2.35, glutamine synthase, a ligase with distinct ATP-binding and glutamine synthetase motifs) and D (EC 1.14.15.9, peptidylglycine α-amidating monooxygenase, an oxidoreductase with copper-binding motifs). For the remaining A (3.2.1.8, endo-β-1,4-glucanase/cellulase) vs C (3.2.1.31, beta-glucuronidase): the ~596 aa length is most consistent with GH2 family proteins (e.g., E. coli GusA beta-glucuronidase is ~603 aa), whereas typical cellulase families (GH5 ~400-500 aa, GH9 ~700-800 aa) differ in size. The sequence contains conserved Glu-containing motifs (e.g., 'DDEKHPEGY') reminiscent of GH2 catalytic residues. GH2 beta-glucuronidases are a well-characterized family with distinctive TIM-barrel architecture and conserved catalytic Glu pairs, distinguishable from cellulase families by sequence-level family signatures learned from homologs. This provides a probabilistic but credible family-level inference favoring C over A.",
    "missing_item_specific_fact": "",
    "reason": "Elimination of B and D is straightforward from recognizing the sequence as a hydrolase. The A vs C distinction relies on family-level knowledge of glycoside hydrolase families (GH2 beta-glucuronidases vs GH5/GH9 cellulases), including sequence length patterns and conserved catalytic motifs transferable from well-characterized homologs. While the distinction is not airtight (the protein is actually GH94-related per the reference, making the EC assignment somewhat atypical for its family), the offered choices are distinguishable through family-level inference about GH2-like features versus cellulase-family features."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "B and D are clearly eliminated as the sequence shows glycoside hydrolase features. Between A and C, while both are glycoside hydrolases, the family-level features (length, motifs, architecture) more consistently align with GH2 beta-glucuronidase than with typical cellulase families. No other option is seriously defensible."
  },
  "important_caveats": [
    "The reference paper (PubMed:35947916) describes this protein as a 'GH94 glycoside phosphorylase' acting on glucuronides, yet the EC annotation is 3.2.1.31 (a hydrolase EC, not a phosphorylase EC 2.4.x.x). The EC assignment reflects observed hydrolytic activity rather than strict family assignment, which is somewhat unusual and could confuse a model familiar with GH94 phosphorylases.",
    "The A vs C distinction (cellulase vs beta-glucuronidase) is genuinely challenging from sequence alone; the family-level argument is probabilistic rather than definitive.",
    "The UniProt annotation is Swiss-Prot reviewed with experimental evidence (ECO:0000269), providing strong support for the key.",
    "The sequence identity between benchmark input and source entry is exact (SHA256 match confirmed in both current and historical snapshots)."
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

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C6",
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
  "excerpt": "DE   RecName: Full=Beta-glucuronidase {ECO:0000303|PubMed:35947916};\nDE            EC=3.2.1.31 {ECO:0000269|PubMed:35947916};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
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

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/EC_number.json), zero-based source row 184. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
