# active_site_0001

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/active_site_0001.txt)

**Task:** `active_site`  
**Expected answer:** **D** — Position 413 (Proton donor)

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
A. Position 1125 (Proton donor; for dehydratase activity)
B. Position 366 (For beta-ketoacyl synthase activity)
C. Position 274 (Nucleophile)
D. Position 413 (Proton donor)
```

<details>
<summary>Complete original system instructions</summary>

```text
You are an excellent scientist. Analyze the provided protein-related task carefully and choose the correct answer from the multiple-choice options.

The current task is about Enzyme Active Site Prediction, which is to identify the key amino acid residues that form the active site of an enzyme. The active site is the specific region on the enzyme where a substrate binds and the chemical reaction is catalyzed. Based on the full protein sequence provided, you must select the option that correctly lists the amino acid residues (by their type and position) that constitute the enzyme's catalytic center.. The inputs provided by the user for this task include:

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

> The sequence-matched UniProt annotation identifies position 413 as the proton donor, supporting D. This is a similarity-based annotation transferred from P05804 (ECO:0000250), not evidence of direct experimental validation for this exact protein.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence is consistent with a glycoside hydrolase, for which conserved catalytic acidic residues and their roles can be inferred from family-level patterns in related enzymes. That provides a credible basis to favor the offered proton-donor assignment at 413 over the nucleophile assignment at 274; the dehydratase and beta-ketoacyl synthase distractors do not fit that enzymatic context, and position 1125 is outside the 596-residue sequence.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> A family-level catalytic-residue pattern can meaningfully distinguish the offered choices without knowing this protein's recorded database answer. The exact positional assignment is still an inference, not something established solely by general chemistry.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied evidence supports D, and no second offered choice is comparably supported.


### Important caveats

- The position-413 annotation is transferred by similarity from another protein; the supplied evidence does not establish direct experimental determination for this sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence is consistent with a glycoside hydrolase, for which conserved catalytic acidic residues and their roles can be inferred from family-level patterns in related enzymes. That provides a credible basis to favor the offered proton-donor assignment at 413 over the nucleophile assignment at 274; the dehydratase and beta-ketoacyl synthase distractors do not fit that enzymatic context, and position 1125 is outside the 596-residue sequence.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "A family-level catalytic-residue pattern can meaningfully distinguish the offered choices without knowing this protein's recorded database answer. The exact positional assignment is still an inference, not something established solely by general chemistry."
  },
  "case_id": "active_site_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 413 as the proton donor, supporting D. This is a similarity-based annotation transferred from P05804 (ECO:0000250), not evidence of direct experimental validation for this exact protein."
  },
  "important_caveats": [
    "The position-413 annotation is transferred by similarity from another protein; the supplied evidence does not establish direct experimental determination for this sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports D, and no second offered choice is comparably supported."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "active_site_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation identifies position 413 as the proton donor, supporting D. This is a similarity-based annotation transferred from P05804 (ECO:0000250), not evidence of direct experimental validation for this exact protein.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence is consistent with a glycoside hydrolase, for which conserved catalytic acidic residues and their roles can be inferred from family-level patterns in related enzymes. That provides a credible basis to favor the offered proton-donor assignment at 413 over the nucleophile assignment at 274; the dehydratase and beta-ketoacyl synthase distractors do not fit that enzymatic context, and position 1125 is outside the 596-residue sequence.",
    "missing_item_specific_fact": "",
    "reason": "A family-level catalytic-residue pattern can meaningfully distinguish the offered choices without knowing this protein's recorded database answer. The exact positional assignment is still an inference, not something established solely by general chemistry."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied evidence supports D, and no second offered choice is comparably supported."
  },
  "important_caveats": [
    "The position-413 annotation is transferred by similarity from another protein; the supplied evidence does not establish direct experimental determination for this sequence."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt annotation for A0A089LCJ8 (Beta-glucuronidase, EC 3.2.1.31) lists position 413 as an Active site with description 'Proton donor', transferred by similarity from E. coli beta-glucuronidase P05804 (ECO:0000250). The residue at position 413 in the supplied sequence is Glu (E), which is chemically consistent with a proton donor role in a retaining glycoside hydrolase. The annotation is computational transfer rather than direct experimental evidence for this specific protein, but the sequence context supports the assignment.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> A knowledgeable model can eliminate all three distractors and confirm D through the following transferable reasoning: (1) Option A cites position 1125, but the supplied sequence is only 596 residues, so this position does not exist — trivially eliminated. (2) Option B references 'beta-ketoacyl synthase activity,' an enzyme class involved in fatty acid biosynthesis (FabB/FabF), completely unrelated to the glycoside-hydrolase fold evident in this sequence; additionally, position 366 is Thr (T), not a catalytic residue for any known enzyme class — eliminated. (3) Option C designates position 274 as a 'Nucleophile.' Counting into the sequence, position 274 is Gln (Q). In every known glycoside hydrolase mechanism, the catalytic nucleophile is an acidic residue (Asp or Glu) capable of attacking the anomeric carbon of the sugar; Gln lacks the required carboxylate and cannot serve as a nucleophile — eliminated. (4) Option D designates position 413 as a 'Proton donor.' Position 413 is Glu (E), a carboxylic acid side chain that is a well-established proton donor in retaining glycosidases (e.g., the Asp/Glu proton donor in GH79 beta-glucuronidases such as E. coli GusB/P05804). This is fully consistent with the GH79/family catalytic mechanism. The model uses only sequence counting and general glycoside-hydrolase mechanistic knowledge (nucleophile must be Asp/Glu; proton donor is Asp/Glu), both learned from many other enzymes.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The question is answerable through sequence inspection (counting to the stated positions) combined with widely taught mechanistic principles of glycoside hydrolases (nucleophile identity, proton donor identity). No fact unique to this exact protein's database record is required; the reasoning relies on the amino acid identity at the queried positions and general enzyme-mechanism knowledge transferable from many other glycosidases.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Each distractor fails on a clear, independent criterion (out-of-range position, wrong enzyme class, wrong amino acid identity for the stated catalytic role). Only D survives all checks.


### Important caveats

- The UniProt annotation at position 413 carries evidence code ECO:0000250 (similarity transfer from P05804), not direct experimental validation for this Paenibacillus borealis protein. The assignment is a computational inference, though the Glu identity at 413 is mechanistically plausible.
- The model must correctly count to position 413 in a 596-residue sequence; miscounting by even a few residues could land on a different amino acid, but the surrounding sequence context (…WSLANEAATFQDE…) makes the Glu at 413 identifiable.
- The question asks for 'the enzyme's catalytic center' (singular focus on one residue), while the full active site also includes the nucleophile at position 502. The options present single residues, so the question is internally consistent.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "A knowledgeable model can eliminate all three distractors and confirm D through the following transferable reasoning: (1) Option A cites position 1125, but the supplied sequence is only 596 residues, so this position does not exist — trivially eliminated. (2) Option B references 'beta-ketoacyl synthase activity,' an enzyme class involved in fatty acid biosynthesis (FabB/FabF), completely unrelated to the glycoside-hydrolase fold evident in this sequence; additionally, position 366 is Thr (T), not a catalytic residue for any known enzyme class — eliminated. (3) Option C designates position 274 as a 'Nucleophile.' Counting into the sequence, position 274 is Gln (Q). In every known glycoside hydrolase mechanism, the catalytic nucleophile is an acidic residue (Asp or Glu) capable of attacking the anomeric carbon of the sugar; Gln lacks the required carboxylate and cannot serve as a nucleophile — eliminated. (4) Option D designates position 413 as a 'Proton donor.' Position 413 is Glu (E), a carboxylic acid side chain that is a well-established proton donor in retaining glycosidases (e.g., the Asp/Glu proton donor in GH79 beta-glucuronidases such as E. coli GusB/P05804). This is fully consistent with the GH79/family catalytic mechanism. The model uses only sequence counting and general glycoside-hydrolase mechanistic knowledge (nucleophile must be Asp/Glu; proton donor is Asp/Glu), both learned from many other enzymes.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through sequence inspection (counting to the stated positions) combined with widely taught mechanistic principles of glycoside hydrolases (nucleophile identity, proton donor identity). No fact unique to this exact protein's database record is required; the reasoning relies on the amino acid identity at the queried positions and general enzyme-mechanism knowledge transferable from many other glycosidases."
  },
  "case_id": "active_site_0001",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A089LCJ8 (Beta-glucuronidase, EC 3.2.1.31) lists position 413 as an Active site with description 'Proton donor', transferred by similarity from E. coli beta-glucuronidase P05804 (ECO:0000250). The residue at position 413 in the supplied sequence is Glu (E), which is chemically consistent with a proton donor role in a retaining glycoside hydrolase. The annotation is computational transfer rather than direct experimental evidence for this specific protein, but the sequence context supports the assignment."
  },
  "important_caveats": [
    "The UniProt annotation at position 413 carries evidence code ECO:0000250 (similarity transfer from P05804), not direct experimental validation for this Paenibacillus borealis protein. The assignment is a computational inference, though the Glu identity at 413 is mechanistically plausible.",
    "The model must correctly count to position 413 in a 596-residue sequence; miscounting by even a few residues could land on a different amino acid, but the surrounding sequence context (…WSLANEAATFQDE…) makes the Glu at 413 identifiable.",
    "The question asks for 'the enzyme's catalytic center' (singular focus on one residue), while the full active site also includes the nucleophile at position 502. The options present single residues, so the question is internally consistent."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor fails on a clear, independent criterion (out-of-range position, wrong enzyme class, wrong amino acid identity for the stated catalytic role). Only D survives all checks."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "active_site_0001",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt annotation for A0A089LCJ8 (Beta-glucuronidase, EC 3.2.1.31) lists position 413 as an Active site with description 'Proton donor', transferred by similarity from E. coli beta-glucuronidase P05804 (ECO:0000250). The residue at position 413 in the supplied sequence is Glu (E), which is chemically consistent with a proton donor role in a retaining glycoside hydrolase. The annotation is computational transfer rather than direct experimental evidence for this specific protein, but the sequence context supports the assignment.",
    "evidence_ids": ["C5", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "A knowledgeable model can eliminate all three distractors and confirm D through the following transferable reasoning: (1) Option A cites position 1125, but the supplied sequence is only 596 residues, so this position does not exist — trivially eliminated. (2) Option B references 'beta-ketoacyl synthase activity,' an enzyme class involved in fatty acid biosynthesis (FabB/FabF), completely unrelated to the glycoside-hydrolase fold evident in this sequence; additionally, position 366 is Thr (T), not a catalytic residue for any known enzyme class — eliminated. (3) Option C designates position 274 as a 'Nucleophile.' Counting into the sequence, position 274 is Gln (Q). In every known glycoside hydrolase mechanism, the catalytic nucleophile is an acidic residue (Asp or Glu) capable of attacking the anomeric carbon of the sugar; Gln lacks the required carboxylate and cannot serve as a nucleophile — eliminated. (4) Option D designates position 413 as a 'Proton donor.' Position 413 is Glu (E), a carboxylic acid side chain that is a well-established proton donor in retaining glycosidases (e.g., the Asp/Glu proton donor in GH79 beta-glucuronidases such as E. coli GusB/P05804). This is fully consistent with the GH79/family catalytic mechanism. The model uses only sequence counting and general glycoside-hydrolase mechanistic knowledge (nucleophile must be Asp/Glu; proton donor is Asp/Glu), both learned from many other enzymes.",
    "missing_item_specific_fact": "",
    "reason": "The question is answerable through sequence inspection (counting to the stated positions) combined with widely taught mechanistic principles of glycoside hydrolases (nucleophile identity, proton donor identity). No fact unique to this exact protein's database record is required; the reasoning relies on the amino acid identity at the queried positions and general enzyme-mechanism knowledge transferable from many other glycosidases."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Each distractor fails on a clear, independent criterion (out-of-range position, wrong enzyme class, wrong amino acid identity for the stated catalytic role). Only D survives all checks."
  },
  "important_caveats": [
    "The UniProt annotation at position 413 carries evidence code ECO:0000250 (similarity transfer from P05804), not direct experimental validation for this Paenibacillus borealis protein. The assignment is a computational inference, though the Glu identity at 413 is mechanistically plausible.",
    "The model must correctly count to position 413 in a 596-residue sequence; miscounting by even a few residues could land on a different amino acid, but the surrounding sequence context (…WSLANEAATFQDE…) makes the Glu at 413 identifiable.",
    "The question asks for 'the enzyme's catalytic center' (singular focus on one residue), while the full active site also includes the nucleophile at position 502. The options present single residues, so the question is internally consistent."
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
  "excerpt": "{\"description\":\"Proton donor\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05804\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":413},\"start\":{\"modifier\":\"EXACT\",\"value\":413}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/2",
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
  "excerpt": "{\"description\":\"Nucleophile\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05804\",\"source\":\"UniProtKB\"}],\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":502},\"start\":{\"modifier\":\"EXACT\",\"value\":502}},\"type\":\"Active site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/3",
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
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05804\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58720\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58720\",\"name\":\"D-glucuronate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":168},\"start\":{\"modifier\":\"EXACT\",\"value\":168}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/4",
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
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05804\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58720\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58720\",\"name\":\"D-glucuronate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":412},\"start\":{\"modifier\":\"EXACT\",\"value\":412}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/5",
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
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05804\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58720\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58720\",\"name\":\"D-glucuronate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":464},\"start\":{\"modifier\":\"EXACT\",\"value\":464}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/6",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence C10

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C10",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05804\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58720\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58720\",\"name\":\"D-glucuronate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":470},\"start\":{\"modifier\":\"EXACT\",\"value\":470}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/7",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence C11

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C11",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05804\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58720\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58720\",\"name\":\"D-glucuronate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":502},\"start\":{\"modifier\":\"EXACT\",\"value\":502}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/8",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence C12

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C12",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05804\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58720\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58720\",\"name\":\"D-glucuronate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":547},\"start\":{\"modifier\":\"EXACT\",\"value\":547}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/9",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence C13

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C13",
  "excerpt": "{\"description\":\"\",\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P05804\",\"source\":\"UniProtKB\"}],\"featureCrossReferences\":[{\"database\":\"ChEBI\",\"id\":\"CHEBI:58720\"}],\"ligand\":{\"id\":\"ChEBI:CHEBI:58720\",\"name\":\"D-glucuronate\"},\"location\":{\"end\":{\"modifier\":\"EXACT\",\"value\":566},\"start\":{\"modifier\":\"EXACT\",\"value\":566}},\"type\":\"Binding site\"}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/features/10",
  "retrieved_utc": "2026-11-01T06:24:37.179702+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "f005e61f4ce923f9d73b889125827288a188dc26d465df67272785f544bcb3a7",
  "url": "https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json"
}
```

### Evidence C14

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A089LCJ8.json)

```json
{
  "evidence_id": "C14",
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
  "excerpt": "FT   ACT_SITE        413\nFT                   /note=\"Proton donor\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P05804\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 108-110",
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
  "excerpt": "FT   ACT_SITE        502\nFT                   /note=\"Nucleophile\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P05804\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 111-113",
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
  "excerpt": "FT   BINDING         168\nFT                   /ligand=\"D-glucuronate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58720\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P05804\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 114-117",
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
  "excerpt": "FT   BINDING         412\nFT                   /ligand=\"D-glucuronate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58720\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P05804\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 118-121",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562",
  "url": "https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41"
}
```

### Evidence H7

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H7",
  "excerpt": "FT   BINDING         464\nFT                   /ligand=\"D-glucuronate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58720\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P05804\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 122-125",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562",
  "url": "https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41"
}
```

### Evidence H8

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H8",
  "excerpt": "FT   BINDING         470\nFT                   /ligand=\"D-glucuronate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58720\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P05804\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 126-129",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562",
  "url": "https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41"
}
```

### Evidence H9

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H9",
  "excerpt": "FT   BINDING         502\nFT                   /ligand=\"D-glucuronate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58720\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P05804\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 130-133",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562",
  "url": "https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41"
}
```

### Evidence H10

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H10",
  "excerpt": "FT   BINDING         547\nFT                   /ligand=\"D-glucuronate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58720\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P05804\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 134-137",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562",
  "url": "https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41"
}
```

### Evidence H11

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41)

```json
{
  "entry_version": 41,
  "evidence_id": "H11",
  "excerpt": "FT   BINDING         566\nFT                   /ligand=\"D-glucuronate\"\nFT                   /ligand_id=\"ChEBI:CHEBI:58720\"\nFT                   /evidence=\"ECO:0000250|UniProtKB:P05804\"\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:15.466546+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 138-141",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "7fe98c6765fe88e6243f21f7805fad6fb6c1c7ac16afc1caaa13afb6d2025562",
  "url": "https://rest.uniprot.org/unisave/A0A089LCJ8?format=txt&versions=41"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/active_site.json), zero-based source row 1. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
