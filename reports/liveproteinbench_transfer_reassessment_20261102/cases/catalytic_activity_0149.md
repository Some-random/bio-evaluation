# catalytic_activity_0149: before and after transfer clarification

[All 1,328 cases](../README.md) · [Method](../METHOD.md) · [Summary](../SUMMARY.md) · [Exact reviewer user message](../inputs/catalytic_activity_0149.txt)

**Task:** `catalytic_activity`  
**Author key, unchanged:** **D** — 5-O-(ADP-D-ribosyl)-L-glutamyl-&#91;protein&#93; + H2O = L-glutamyl-&#91;protein&#93; + ADP-D-ribose + H(+)

| Round | Reviewer | Key support | Transfer / lookup | Output usability (canonical status) |
|---|---|---|---|---|
| before | GPT-6 Luna | supported | lookup-dependent | usable output (valid_review) |
| before | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |
| after | GPT-6 Luna | supported | reasoning-supported | usable output (valid_review) |
| after | Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported | usable output (valid_review) |

**Usable output means format-valid review, not reasoning-supported or biologically correct.** A usable output can classify the question as reasoning-supported, lookup-dependent or uncertain. An output error is a problem with the saved model response; it does not count a defective benchmark question or wrong key. Each saved review is retained in full below. Labels from output errors are displayed as saved and excluded from label statistics. The author key and reviewer evidence were visible to reviewers; this is a review of answerability and key support, not a benchmark-solving score.

## Complete original question

```text
[Protein Sequence]
MRTTLTGTASVLDTTLTRLIDDVIENGSSFLADDENLQHYKQHLSHLETASKIALLRECLCVRPPLPLLPEDLLQNVDSILTRVRQHKILTPIFSLSPSRLIKHGDLGATRIHLWRGDITTLTGVTAITNAANSQGLGCFQPTHRCIDNIIHAEAGPRLREECFQRMQARGKELEPGEVLVTEGHALFASSVMHTVGPQLKRGASPTETERRQLAKCYESILEALELLPSDEDGSKSIALCCISTGLFAFPADEAAEIAVSTVTSWLQKHPSTTITDVIFNTFTQSDTEFYSKLLGPSHTKSISPVENTPQGSLSLAREWLSSADAVLVTAGAGLSAAEGLDYHSRDLFKRNFPGCLKFGLTSLYSVFGFNDWPSEEHRWGYFFTHLNMVANWSNTPTYQILIPWLRNFGQDAFVRTSNADGLFLANGWPKEQLSTPQGSYGYLQCLNNCRVDAVVPSAPLVADAMPHIDKATQKLMDPSKIPLCRFCGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKKNLVILELGVGMNTPGVLRWPNEDLVMRSDGRVKLIRVGMGPEAMVPWEQEDEGLSTCVQGDIGRAIPLLLE

[Multiple Choices]
A. (2R,3R)-2,3-dihydroxy-3-methylpentanoate = (S)-3-methyl-2-oxopentanoate + H2O
B. deacetylipecoside + H2O = deacetylipecoside aglycone + D-glucose
C. dopamine + S-adenosyl-L-methionine = N-methyl-dopamine + S-adenosyl-L-homocysteine + H(+)
D. 5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)
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

## Four saved visible reviews

## Before: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The supplied sequence exactly matches the reviewed protein sequence, and its catalytic-activity annotation gives the reaction in choice D with ECO:0000269 evidence linked to a 2024 publication. The source also cites structural and mutagenesis work. This supports D for this protein, while distinguishing the evidence as an annotation tied to published experimental work rather than something established from the sequence alone.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

> The sequence may suggest a protein with ADP-ribose-related domains, but the input does not establish the specific substrate or hydrolysis of ADP-ribose from glutamylated protein. The precise reaction cannot be reliably selected from sequence inspection alone.


**Missing item-specific fact**

> The protein-specific catalytic activity: hydrolysis of 5-O-(ADP-D-ribosyl)-L-glutamyl-&#91;protein&#93;.


**Reason**

> Choosing D requires knowing this protein's experimentally characterized or database-annotated activity, which is absent from the question input; recognizing the sequence from an external record would be lookup or memorization, not reasoning from supplied evidence.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the listed reactions, D matches the supported catalytic activity; the other choices describe distinct reactions.


### Important caveats

- The reviewer-only source records an exact sequence match and an experimental-evidence code for the catalytic activity, but the primary paper was not independently reviewed here.
- The author’s exact source snapshot is unknown; the historical record checked also matches the sequence.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence may suggest a protein with ADP-ribose-related domains, but the input does not establish the specific substrate or hydrolysis of ADP-ribose from glutamylated protein. The precise reaction cannot be reliably selected from sequence inspection alone.",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "The protein-specific catalytic activity: hydrolysis of 5-O-(ADP-D-ribosyl)-L-glutamyl-[protein].",
    "reason": "Choosing D requires knowing this protein's experimentally characterized or database-annotated activity, which is absent from the question input; recognizing the sequence from an external record would be lookup or memorization, not reasoning from supplied evidence."
  },
  "case_id": "catalytic_activity_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed protein sequence, and its catalytic-activity annotation gives the reaction in choice D with ECO:0000269 evidence linked to a 2024 publication. The source also cites structural and mutagenesis work. This supports D for this protein, while distinguishing the evidence as an annotation tied to published experimental work rather than something established from the sequence alone."
  },
  "important_caveats": [
    "The reviewer-only source records an exact sequence match and an experimental-evidence code for the catalytic activity, but the primary paper was not independently reviewed here.",
    "The author’s exact source snapshot is unknown; the historical record checked also matches the sequence."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, D matches the supported catalytic activity; the other choices describe distinct reactions."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The supplied sequence exactly matches the reviewed protein sequence, and its catalytic-activity annotation gives the reaction in choice D with ECO:0000269 evidence linked to a 2024 publication. The source also cites structural and mutagenesis work. This supports D for this protein, while distinguishing the evidence as an annotation tied to published experimental work rather than something established from the sequence alone.",
    "evidence_ids": ["C5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "The sequence may suggest a protein with ADP-ribose-related domains, but the input does not establish the specific substrate or hydrolysis of ADP-ribose from glutamylated protein. The precise reaction cannot be reliably selected from sequence inspection alone.",
    "missing_item_specific_fact": "The protein-specific catalytic activity: hydrolysis of 5-O-(ADP-D-ribosyl)-L-glutamyl-[protein].",
    "reason": "Choosing D requires knowing this protein's experimentally characterized or database-annotated activity, which is absent from the question input; recognizing the sequence from an external record would be lookup or memorization, not reasoning from supplied evidence."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the listed reactions, D matches the supported catalytic activity; the other choices describe distinct reactions."
  },
  "important_caveats": [
    "The reviewer-only source records an exact sequence match and an experimental-evidence code for the catalytic activity, but the primary paper was not independently reviewed here.",
    "The author’s exact source snapshot is unknown; the historical record checked also matches the sequence."
  ]
}
```

</details>

## Before: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The protein sequence matches UniProt A0A559KX76 (ADRHT_FUSOC) exactly (SHA256 confirmed). The UniProt entry explicitly annotates the catalytic activity as '5-O-(ADP-D-ribosyl)-L-glutamyl-&#91;protein&#93; + H2O = L-glutamyl-&#91;protein&#93; + ADP-D-ribose + H(+)' with evidence code ECO:0000269 (inferred from direct assay), supported by a 2024 JBC paper (PMID 39270823) and X-ray crystallography at 2.22 Å in complex with Zn(2+). The reaction in option D matches the annotated reaction verbatim.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains recognizable macrodomain-fold motifs (e.g., the conserved 'GAGLSAA' β-strand region and 'CGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKK' segment), which are hallmarks of ADP-ribose-interacting proteins. Among the four options, only D involves ADP-ribose chemistry; the others describe a dihydroxy-acid dehydratase (A), a glycosidase (B), and a SAM-dependent methyltransferase (C), none of whose characteristic motifs (e.g., ilvD active-site residues, glycosidase catalytic Glu/Asp, COMT SAM-binding pocket) are present in this sequence. Recognizing the macrodomain fold and associating it with ADP-ribose metabolism is a legitimate general-biology inference that eliminates A, B, and C.


**Missing item-specific fact**

> Distinguishing the hydrolase (removal) activity from the transferase (addition) activity of this particular bifunctional macrodomain/SirTM protein cannot be resolved from sequence alone; however, since no option describes a transferase reaction, this distinction is not required to select D.


**Reason**

> A model with knowledge of the macrodomain fold and its association with ADP-ribose metabolism can eliminate the three non-ADP-ribose options through general biological reasoning. The reasoning does not require memorizing this specific Fusarium protein's database entry, though it does require recognizing a somewhat specialized fold motif.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The protein is annotated as bifunctional (hydrolase + probable transferase), but no option describes the transferase reaction. Option D is the only ADP-ribose-related reaction and matches the experimentally confirmed catalytic activity exactly. The other three options correspond to unrelated enzyme classes with no sequence support.


### Important caveats

- The UniProt entry was first published 2025-06-18; the historical Swiss-Prot record (version 22) was first released in January 2026. If the benchmark was constructed before that date, the annotation may not have been publicly available, though the sequence itself was.
- The transferase activity (EC 2.4.2.-) is annotated only by similarity (ECO:0000250, inferred from P0DN71), not experimentally confirmed. The hydrolase activity (EC 3.2.1.-) is experimentally confirmed (ECO:0000269).
- Recognition of the macrodomain fold from linear sequence is a specialized but legitimate biological skill; it is less universally taught than, e.g., Rossmann or Walker A motifs, so the reasoning argument, while valid, requires some domain-specific knowledge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains recognizable macrodomain-fold motifs (e.g., the conserved 'GAGLSAA' β-strand region and 'CGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKK' segment), which are hallmarks of ADP-ribose-interacting proteins. Among the four options, only D involves ADP-ribose chemistry; the others describe a dihydroxy-acid dehydratase (A), a glycosidase (B), and a SAM-dependent methyltransferase (C), none of whose characteristic motifs (e.g., ilvD active-site residues, glycosidase catalytic Glu/Asp, COMT SAM-binding pocket) are present in this sequence. Recognizing the macrodomain fold and associating it with ADP-ribose metabolism is a legitimate general-biology inference that eliminates A, B, and C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "Distinguishing the hydrolase (removal) activity from the transferase (addition) activity of this particular bifunctional macrodomain/SirTM protein cannot be resolved from sequence alone; however, since no option describes a transferase reaction, this distinction is not required to select D.",
    "reason": "A model with knowledge of the macrodomain fold and its association with ADP-ribose metabolism can eliminate the three non-ADP-ribose options through general biological reasoning. The reasoning does not require memorizing this specific Fusarium protein's database entry, though it does require recognizing a somewhat specialized fold motif."
  },
  "case_id": "catalytic_activity_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt A0A559KX76 (ADRHT_FUSOC) exactly (SHA256 confirmed). The UniProt entry explicitly annotates the catalytic activity as '5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)' with evidence code ECO:0000269 (inferred from direct assay), supported by a 2024 JBC paper (PMID 39270823) and X-ray crystallography at 2.22 Å in complex with Zn(2+). The reaction in option D matches the annotated reaction verbatim."
  },
  "important_caveats": [
    "The UniProt entry was first published 2025-06-18; the historical Swiss-Prot record (version 22) was first released in January 2026. If the benchmark was constructed before that date, the annotation may not have been publicly available, though the sequence itself was.",
    "The transferase activity (EC 2.4.2.-) is annotated only by similarity (ECO:0000250, inferred from P0DN71), not experimentally confirmed. The hydrolase activity (EC 3.2.1.-) is experimentally confirmed (ECO:0000269).",
    "Recognition of the macrodomain fold from linear sequence is a specialized but legitimate biological skill; it is less universally taught than, e.g., Rossmann or Walker A motifs, so the reasoning argument, while valid, requires some domain-specific knowledge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is annotated as bifunctional (hydrolase + probable transferase), but no option describes the transferase reaction. Option D is the only ADP-ribose-related reaction and matches the experimentally confirmed catalytic activity exactly. The other three options correspond to unrelated enzyme classes with no sequence support."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The protein sequence matches UniProt A0A559KX76 (ADRHT_FUSOC) exactly (SHA256 confirmed). The UniProt entry explicitly annotates the catalytic activity as '5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)' with evidence code ECO:0000269 (inferred from direct assay), supported by a 2024 JBC paper (PMID 39270823) and X-ray crystallography at 2.22 Å in complex with Zn(2+). The reaction in option D matches the annotated reaction verbatim.",
    "evidence_ids": ["C5", "H4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains recognizable macrodomain-fold motifs (e.g., the conserved 'GAGLSAA' β-strand region and 'CGSKMSICVRAGSWFNQAPYQEGEAQWKAWKSRVLREKK' segment), which are hallmarks of ADP-ribose-interacting proteins. Among the four options, only D involves ADP-ribose chemistry; the others describe a dihydroxy-acid dehydratase (A), a glycosidase (B), and a SAM-dependent methyltransferase (C), none of whose characteristic motifs (e.g., ilvD active-site residues, glycosidase catalytic Glu/Asp, COMT SAM-binding pocket) are present in this sequence. Recognizing the macrodomain fold and associating it with ADP-ribose metabolism is a legitimate general-biology inference that eliminates A, B, and C.",
    "missing_item_specific_fact": "Distinguishing the hydrolase (removal) activity from the transferase (addition) activity of this particular bifunctional macrodomain/SirTM protein cannot be resolved from sequence alone; however, since no option describes a transferase reaction, this distinction is not required to select D.",
    "reason": "A model with knowledge of the macrodomain fold and its association with ADP-ribose metabolism can eliminate the three non-ADP-ribose options through general biological reasoning. The reasoning does not require memorizing this specific Fusarium protein's database entry, though it does require recognizing a somewhat specialized fold motif."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The protein is annotated as bifunctional (hydrolase + probable transferase), but no option describes the transferase reaction. Option D is the only ADP-ribose-related reaction and matches the experimentally confirmed catalytic activity exactly. The other three options correspond to unrelated enzyme classes with no sequence support."
  },
  "important_caveats": [
    "The UniProt entry was first published 2025-06-18; the historical Swiss-Prot record (version 22) was first released in January 2026. If the benchmark was constructed before that date, the annotation may not have been publicly available, though the sequence itself was.",
    "The transferase activity (EC 2.4.2.-) is annotated only by similarity (ECO:0000250, inferred from P0DN71), not experimentally confirmed. The hydrolase activity (EC 3.2.1.-) is experimentally confirmed (ECO:0000269).",
    "Recognition of the macrodomain fold from linear sequence is a specialized but legitimate biological skill; it is less universally taught than, e.g., Rossmann or Walker A motifs, so the reasoning argument, while valid, requires some domain-specific knowledge."
  ]
}
```

</details>

## After: GPT-6 Luna

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The sequence-matched UniProt annotation gives choice D as the catalytic reaction and attributes it to experimental evidence (ECO:0000269); the historical record also associates the cited study with hydrolase function and catalytic activity. This supports the key, though the primary study was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The long sequence has a multidomain pattern with glycine-rich nucleotide-associated segments and a cysteine-rich region, consistent with transferable knowledge of ADP-ribose-processing enzyme families, including macrodomain/Sir2-like proteins. That family-level inference makes protein ADP-ribose removal (D) a meaningful fit, unlike the branched-chain ketoacid reaction, glycoside hydrolysis, or catechol methylation in A–C.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence provides a credible family-level route to distinguishing the ADP-ribose reaction from the other offered reaction types. It does not by itself establish every detail of D's substrate specificity, but the alternatives do not require that finer distinction to identify D as the supported choice.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Among the offered choices, D is the one consistent with an ADP-ribose-processing enzyme; the other reactions describe substantially different enzyme activities.


### Important caveats

- The experimental support is reported through the cited UniProt evidence annotation; the primary paper was not independently assessed.
- The sequence-based family inference supports the choice among these alternatives but is not, by itself, proof of the exact glutamyl-linked substrate.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The long sequence has a multidomain pattern with glycine-rich nucleotide-associated segments and a cysteine-rich region, consistent with transferable knowledge of ADP-ribose-processing enzyme families, including macrodomain/Sir2-like proteins. That family-level inference makes protein ADP-ribose removal (D) a meaningful fit, unlike the branched-chain ketoacid reaction, glycoside hydrolysis, or catechol methylation in A–C.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a credible family-level route to distinguishing the ADP-ribose reaction from the other offered reaction types. It does not by itself establish every detail of D's substrate specificity, but the alternatives do not require that finer distinction to identify D as the supported choice."
  },
  "case_id": "catalytic_activity_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation gives choice D as the catalytic reaction and attributes it to experimental evidence (ECO:0000269); the historical record also associates the cited study with hydrolase function and catalytic activity. This supports the key, though the primary study was not independently reviewed here."
  },
  "important_caveats": [
    "The experimental support is reported through the cited UniProt evidence annotation; the primary paper was not independently assessed.",
    "The sequence-based family inference supports the choice among these alternatives but is not, by itself, proof of the exact glutamyl-linked substrate."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, D is the one consistent with an ADP-ribose-processing enzyme; the other reactions describe substantially different enzyme activities."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation gives choice D as the catalytic reaction and attributes it to experimental evidence (ECO:0000269); the historical record also associates the cited study with hydrolase function and catalytic activity. This supports the key, though the primary study was not independently reviewed here.",
    "evidence_ids": ["C5", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The long sequence has a multidomain pattern with glycine-rich nucleotide-associated segments and a cysteine-rich region, consistent with transferable knowledge of ADP-ribose-processing enzyme families, including macrodomain/Sir2-like proteins. That family-level inference makes protein ADP-ribose removal (D) a meaningful fit, unlike the branched-chain ketoacid reaction, glycoside hydrolysis, or catechol methylation in A–C.",
    "missing_item_specific_fact": "",
    "reason": "The sequence provides a credible family-level route to distinguishing the ADP-ribose reaction from the other offered reaction types. It does not by itself establish every detail of D's substrate specificity, but the alternatives do not require that finer distinction to identify D as the supported choice."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Among the offered choices, D is the one consistent with an ADP-ribose-processing enzyme; the other reactions describe substantially different enzyme activities."
  },
  "important_caveats": [
    "The experimental support is reported through the cited UniProt evidence annotation; the primary paper was not independently assessed.",
    "The sequence-based family inference supports the choice among these alternatives but is not, by itself, proof of the exact glutamyl-linked substrate."
  ]
}
```

</details>

## After: Qwen3.8-Flash-Next-NVFP4

**Output usability:** usable output: format-valid review.
**Canonical saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0A559KX76 explicitly annotates the catalytic activity as '5-O-(ADP-D-ribosyl)-L-glutamyl-&#91;protein&#93; + H2O = L-glutamyl-&#91;protein&#93; + ADP-D-ribose + H(+)' with ECO:0000269 (experimental evidence from PubMed:39270823) and PDB X-ray crystallography (8RSN, 2.22 Å, complex with Zn2+). The protein is named 'Protein-ADP-ribose hydrolase' (EC 3.2.1.-) as the macrodomain component of a bifunctional enzyme. The sequence matches the benchmark input exactly (597 aa, SHA-256 confirmed).

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4), [C6](#evidence-c6), [H3](#evidence-h3).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The N-terminal ~200 residues display hallmark macrodomain features: a GDL motif near the N-terminus ('GDLGATRIHLWRGDITTLTGVT'), a conserved GGL tripeptide ('AGAGLSAAEGLDYHSRDLFKRNFPGCLKFGL'), and the overall macrodomain fold architecture. Macrodomains are a well-characterized protein family (e.g., ARH3, MacroD1, MacroD2, bacterial macrodomains like those in Coxiella, Legionella, and viral macrodomains) whose defining function is binding and/or hydrolyzing ADP-ribose modifications on proteins. The C-terminal region contains a SirTM/Sir2-like ADP-ribosyltransferase domain ('VGMGPEAMVPWEQEDEGLSTCVQGDIGRAIPLLLE'), further confirming an ADP-ribose modification/removal theme. Among the four choices, only D involves ADP-ribose chemistry. Choice A (dihydroxy-acid dehydratase) requires a TIM-barrel fold with no relation to macrodomains. Choice B (glycosidase) requires glycosidase motifs absent here. Choice C (SAM-dependent methyltransferase) requires a Rossmann-like SAM-binding fold also absent. A model recognizing the macrodomain fold and its established association with ADP-ribose hydrolysis across many homologous proteins would confidently select D.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The macrodomain fold and its ADP-ribose hydrolase function are extensively documented across dozens of other macrodomain proteins (ARH3, MacroD1/2, viral macrodomains, bacterial macrodomains). The GDL and GGL motifs are recognizable sequence-level signatures. The SirTM domain at the C-terminus reinforces the ADP-ribose theme. None of the distractor options (DAD, glycosidase, methyltransferase) share any structural or mechanistic connection to macrodomains. Transferable family-level knowledge meaningfully distinguishes D from A, B, and C.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Although the UniProt entry annotates the protein as bifunctional (hydrolase + transferase), only the hydrolase reaction (D) is offered among the choices. The transferase direction (adding ADP-ribose to glutamate) is not presented as an alternative. The three distractors (A, B, C) are mechanistically and structurally unrelated to ADP-ribose chemistry or macrodomain proteins. No ambiguity exists among the offered options.


### Important caveats

- The entry is annotated as 'Probable' bifunctional enzyme; the transferase (SirTM) activity is by similarity (ECO:0000250 to P0DN71), while the hydrolase activity has direct experimental support (ECO:0000269, PubMed:39270823, PDB 8RSN).
- The macrodomain fold recognition from sequence alone requires familiarity with macrodomain consensus motifs (GDL, GGL); a model without this knowledge would struggle, but this is standard transferable protein-family knowledge.
- The entry was first public in 2025-06-18 and integrated into Swiss-Prot in 2026-01; the 2024 crystallographic paper (PubMed:39270823) is the primary experimental source.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The N-terminal ~200 residues display hallmark macrodomain features: a GDL motif near the N-terminus ('GDLGATRIHLWRGDITTLTGVT'), a conserved GGL tripeptide ('AGAGLSAAEGLDYHSRDLFKRNFPGCLKFGL'), and the overall macrodomain fold architecture. Macrodomains are a well-characterized protein family (e.g., ARH3, MacroD1, MacroD2, bacterial macrodomains like those in Coxiella, Legionella, and viral macrodomains) whose defining function is binding and/or hydrolyzing ADP-ribose modifications on proteins. The C-terminal region contains a SirTM/Sir2-like ADP-ribosyltransferase domain ('VGMGPEAMVPWEQEDEGLSTCVQGDIGRAIPLLLE'), further confirming an ADP-ribose modification/removal theme. Among the four choices, only D involves ADP-ribose chemistry. Choice A (dihydroxy-acid dehydratase) requires a TIM-barrel fold with no relation to macrodomains. Choice B (glycosidase) requires glycosidase motifs absent here. Choice C (SAM-dependent methyltransferase) requires a Rossmann-like SAM-binding fold also absent. A model recognizing the macrodomain fold and its established association with ADP-ribose hydrolysis across many homologous proteins would confidently select D.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The macrodomain fold and its ADP-ribose hydrolase function are extensively documented across dozens of other macrodomain proteins (ARH3, MacroD1/2, viral macrodomains, bacterial macrodomains). The GDL and GGL motifs are recognizable sequence-level signatures. The SirTM domain at the C-terminus reinforces the ADP-ribose theme. None of the distractor options (DAD, glycosidase, methyltransferase) share any structural or mechanistic connection to macrodomains. Transferable family-level knowledge meaningfully distinguishes D from A, B, and C."
  },
  "case_id": "catalytic_activity_0149",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4",
      "C6",
      "H3"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0A559KX76 explicitly annotates the catalytic activity as '5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)' with ECO:0000269 (experimental evidence from PubMed:39270823) and PDB X-ray crystallography (8RSN, 2.22 Å, complex with Zn2+). The protein is named 'Protein-ADP-ribose hydrolase' (EC 3.2.1.-) as the macrodomain component of a bifunctional enzyme. The sequence matches the benchmark input exactly (597 aa, SHA-256 confirmed)."
  },
  "important_caveats": [
    "The entry is annotated as 'Probable' bifunctional enzyme; the transferase (SirTM) activity is by similarity (ECO:0000250 to P0DN71), while the hydrolase activity has direct experimental support (ECO:0000269, PubMed:39270823, PDB 8RSN).",
    "The macrodomain fold recognition from sequence alone requires familiarity with macrodomain consensus motifs (GDL, GGL); a model without this knowledge would struggle, but this is standard transferable protein-family knowledge.",
    "The entry was first public in 2025-06-18 and integrated into Swiss-Prot in 2026-01; the 2024 crystallographic paper (PubMed:39270823) is the primary experimental source."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry annotates the protein as bifunctional (hydrolase + transferase), only the hydrolase reaction (D) is offered among the choices. The transferase direction (adding ADP-ribose to glutamate) is not presented as an alternative. The three distractors (A, B, C) are mechanistically and structurally unrelated to ADP-ribose chemistry or macrodomain proteins. No ambiguity exists among the offered options."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0149",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0A559KX76 explicitly annotates the catalytic activity as '5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)' with ECO:0000269 (experimental evidence from PubMed:39270823) and PDB X-ray crystallography (8RSN, 2.22 Å, complex with Zn2+). The protein is named 'Protein-ADP-ribose hydrolase' (EC 3.2.1.-) as the macrodomain component of a bifunctional enzyme. The sequence matches the benchmark input exactly (597 aa, SHA-256 confirmed).",
    "evidence_ids": ["C5", "H4", "C6", "H3"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The N-terminal ~200 residues display hallmark macrodomain features: a GDL motif near the N-terminus ('GDLGATRIHLWRGDITTLTGVT'), a conserved GGL tripeptide ('AGAGLSAAEGLDYHSRDLFKRNFPGCLKFGL'), and the overall macrodomain fold architecture. Macrodomains are a well-characterized protein family (e.g., ARH3, MacroD1, MacroD2, bacterial macrodomains like those in Coxiella, Legionella, and viral macrodomains) whose defining function is binding and/or hydrolyzing ADP-ribose modifications on proteins. The C-terminal region contains a SirTM/Sir2-like ADP-ribosyltransferase domain ('VGMGPEAMVPWEQEDEGLSTCVQGDIGRAIPLLLE'), further confirming an ADP-ribose modification/removal theme. Among the four choices, only D involves ADP-ribose chemistry. Choice A (dihydroxy-acid dehydratase) requires a TIM-barrel fold with no relation to macrodomains. Choice B (glycosidase) requires glycosidase motifs absent here. Choice C (SAM-dependent methyltransferase) requires a Rossmann-like SAM-binding fold also absent. A model recognizing the macrodomain fold and its established association with ADP-ribose hydrolysis across many homologous proteins would confidently select D.",
    "missing_item_specific_fact": "",
    "reason": "The macrodomain fold and its ADP-ribose hydrolase function are extensively documented across dozens of other macrodomain proteins (ARH3, MacroD1/2, viral macrodomains, bacterial macrodomains). The GDL and GGL motifs are recognizable sequence-level signatures. The SirTM domain at the C-terminus reinforces the ADP-ribose theme. None of the distractor options (DAD, glycosidase, methyltransferase) share any structural or mechanistic connection to macrodomains. Transferable family-level knowledge meaningfully distinguishes D from A, B, and C."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Although the UniProt entry annotates the protein as bifunctional (hydrolase + transferase), only the hydrolase reaction (D) is offered among the choices. The transferase direction (adding ADP-ribose to glutamate) is not presented as an alternative. The three distractors (A, B, C) are mechanistically and structurally unrelated to ADP-ribose chemistry or macrodomain proteins. No ambiguity exists among the offered options."
  },
  "important_caveats": [
    "The entry is annotated as 'Probable' bifunctional enzyme; the transferase (SirTM) activity is by similarity (ECO:0000250 to P0DN71), while the hydrolase activity has direct experimental support (ECO:0000269, PubMed:39270823, PDB 8RSN).",
    "The macrodomain fold recognition from sequence alone requires familiarity with macrodomain consensus motifs (GDL, GGL); a model without this knowledge would struggle, but this is standard transferable protein-family knowledge.",
    "The entry was first public in 2025-06-18 and integrated into Swiss-Prot in 2026-01; the 2024 crystallographic paper (PubMed:39270823) is the primary experimental source."
  ]
}
```

</details>

## Existing project source checks of the old Luna review only

These unchanged notes concern the earlier Luna claims. They do not validate either new review or the old Qwen review. No new scientific adjudication was performed.

## Project source-check notes

These project-authored, AI-assisted checks assess specific source claims. They are not expert adjudication and do not replace Luna’s saved review or the author key.

No additional case-specific project note was recorded. Citation membership checks do not establish that every scientific argument is correct.

## Complete reviewer-only evidence and qualifications

All excerpts supplied in the original and revised reviewer user message follow. This material was not available to the original evaluated model. Accession identity came from dataset image-path metadata. Source support and transferable discrimination are separate judgments.

**Applicability metadata, unchanged:**

```json
{
  "requested_accession": "A0A559KX76",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "benchmark_sequence_sha256": "fb7122de3adfadd42d80b188dae7090de1939670d22c33aa431753afa5349321",
  "benchmark_sequence_length": 597,
  "current_status": "retrieved",
  "current_sequence_comparison": "matched",
  "current_entry_audit": {
    "entryVersion": 24,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2019-10-16",
    "sequenceVersion": 1
  },
  "current_uniprot_release": "2026_03",
  "current_record_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "current_source_sequence_sha256": "fb7122de3adfadd42d80b188dae7090de1939670d22c33aa431753afa5349321",
  "current_source_sequence_length": 597,
  "historical_status": "retrieved",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "selected_historical_entry_version": 22,
  "selected_historical_version": {
    "accession": "A0A559KX76",
    "database": "Swiss-Prot",
    "entryVersion": 22,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "ADRHT_FUSOC",
    "sequenceVersion": 1
  },
  "selected_historical_record_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "selected_historical_source_sequence_sha256": "fb7122de3adfadd42d80b188dae7090de1939670d22c33aa431753afa5349321",
  "selected_historical_source_sequence_length": 597,
  "latest_at_cutoff_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 22,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "actual_author_source_snapshot": "unknown",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed."
}
```

**Qualifications, unchanged:**

- All evidence and source identity in this section are reviewer-only and were absent from the evaluated model input.
- UniProt annotations may be experimental, computational, or transferred by similarity; evidence codes and qualifiers are retained.
- The 2026-05-07 cutoff approximates the pinned repository date; the author data-construction date and exact source snapshot remain unknown.
- Selected source fields are excerpts; missing annotation is not evidence of falsehood. Primary papers were not comprehensively retrieved or independently validated.

### Evidence C1

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C1",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "json_pointer": "/primaryAccession",
  "excerpt": "\"A0A559KX76\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C2",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "json_pointer": "/entryAudit",
  "excerpt": "{\"entryVersion\":24,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2019-10-16\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C3",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "json_pointer": "/organism",
  "excerpt": "{\"lineage\":[\"Eukaryota\",\"Fungi\",\"Dikarya\",\"Ascomycota\",\"Pezizomycotina\",\"Sordariomycetes\",\"Hypocreomycetidae\",\"Hypocreales\",\"Nectriaceae\",\"Fusarium\",\"Fusarium oxysporum species complex\"],\"scientificName\":\"Fusarium oxysporum f. sp. cubense\",\"taxonId\":61366}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C4",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "json_pointer": "/proteinDescription",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"value\":\"Foc1Mfs1\"}},{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WZU87063.1\",\"source\":\"EMBL\"}],\"value\":\"Macrodomain-fused SirTM 1\"}}],\"includes\":[{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"value\":\"3.2.1.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Protein-ADP-ribose hydrolase\"}}},{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000250\",\"id\":\"P0DN71\",\"source\":\"UniProtKB\"}],\"value\":\"2.4.2.-\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Probable protein ADP-ribosyltransferase\"}}}],\"recommendedName\":{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C5",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "json_pointer": "/comments/1",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39270823\",\"source\":\"PubMed\"}],\"name\":\"5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-[protein] + ADP-D-ribose + H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:58248\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:10208\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:15089\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:29973\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57967\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142540\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0A559KX76.json)

```json
{
  "evidence_id": "C6",
  "source": "UniProtKB current entry",
  "url": "https://rest.uniprot.org/uniprotkb/A0A559KX76.json",
  "source_sha256": "52b8d79f7061ab8ceea42642d265f006efbce4efe152e77f8ff22f5e291de2e2",
  "retrieved_utc": "2026-11-02T04:25:25.184799+00:00",
  "json_pointer": "/references/1",
  "excerpt": "{\"citation\":{\"authors\":[\"Ariza A.\",\"Liu Q.\",\"Cowieson N.P.\",\"Ahel I.\",\"Filippov D.V.\",\"Rack J.G.M.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39270823\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107770\"}],\"citationType\":\"journal article\",\"firstPage\":\"107770\",\"id\":\"39270823\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107770\",\"publicationDate\":\"2024\",\"title\":\"Evolutionary and molecular basis of ADP-ribosylation reversal by zinc-dependent macrodomains.\",\"volume\":\"300\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"8RSN\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"race 1 / IMI 141109\"}],\"referenceNumber\":2,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [GENOMIC DNA]\",\"X-RAY CRYSTALLOGRAPHY (2.22 ANGSTROMS) IN COMPLEX WITH ZN(2+)\",\"FUNCTION AS AN HYDROLASE\",\"CATALYTIC ACTIVITY\",\"COFACTOR\",\"SUBUNIT\",\"MUTAGENESIS OF CYS-61 AND HIS-144\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "sequence_comparison": "matched"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "evidence_id": "H1",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "source_locator": "lines 1-21",
  "excerpt": "ID   ADRHT_FUSOC             Reviewed;         597 AA.\nAC   A0A559KX76;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   16-OCT-2019, sequence version 1.\nDT   28-JAN-2026, entry version 22.\nDE   RecName: Full=Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase {ECO:0000305};\nDE   AltName: Full=Foc1Mfs1 {ECO:0000303|PubMed:39270823};\nDE   AltName: Full=Macrodomain-fused SirTM 1 {ECO:0000312|EMBL:WZU87063.1};\nDE   Includes:\nDE     RecName: Full=Protein-ADP-ribose hydrolase {ECO:0000305};\nDE              EC=3.2.1.- {ECO:0000269|PubMed:39270823};\nDE   Includes:\nDE     RecName: Full=Probable protein ADP-ribosyltransferase {ECO:0000305};\nDE              EC=2.4.2.- {ECO:0000250|UniProtKB:P0DN71};\nGN   Name=mfs1 {ECO:0000312|EMBL:WZU87063.1};\nGN   ORFNames=Focb16_v015632 {ECO:0000312|EMBL:TVY64815.1};\nOS   Fusarium oxysporum f. sp. cubense.\nOC   Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina; Sordariomycetes;\nOC   Hypocreomycetidae; Hypocreales; Nectriaceae; Fusarium;\nOC   Fusarium oxysporum species complex.\nOX   NCBI_TaxID=61366;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 22,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "evidence_id": "H2",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "source_locator": "lines 6-14",
  "excerpt": "DE   RecName: Full=Probable bifunctional ADP-ribose hydrolase/ADP-ribosyltransferase {ECO:0000305};\nDE   AltName: Full=Foc1Mfs1 {ECO:0000303|PubMed:39270823};\nDE   AltName: Full=Macrodomain-fused SirTM 1 {ECO:0000312|EMBL:WZU87063.1};\nDE   Includes:\nDE     RecName: Full=Protein-ADP-ribose hydrolase {ECO:0000305};\nDE              EC=3.2.1.- {ECO:0000269|PubMed:39270823};\nDE   Includes:\nDE     RecName: Full=Probable protein ADP-ribosyltransferase {ECO:0000305};\nDE              EC=2.4.2.- {ECO:0000250|UniProtKB:P0DN71};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 22,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "evidence_id": "H3",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "source_locator": "lines 30-39",
  "excerpt": "RN   [2] {ECO:0007744|PDB:8RSN}\nRP   NUCLEOTIDE SEQUENCE [GENOMIC DNA], X-RAY CRYSTALLOGRAPHY (2.22 ANGSTROMS)\nRP   IN COMPLEX WITH ZN(2+), FUNCTION AS AN HYDROLASE, CATALYTIC ACTIVITY,\nRP   COFACTOR, SUBUNIT, AND MUTAGENESIS OF CYS-61 AND HIS-144.\nRC   STRAIN=race 1 / IMI 141109;\nRX   PubMed=39270823; DOI=10.1016/j.jbc.2024.107770;\nRA   Ariza A., Liu Q., Cowieson N.P., Ahel I., Filippov D.V., Rack J.G.M.;\nRT   \"Evolutionary and molecular basis of ADP-ribosylation reversal by zinc-\nRT   dependent macrodomains.\";\nRL   J. Biol. Chem. 300:107770-107770(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 22,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22)

```json
{
  "evidence_id": "H4",
  "source": "UniSave archived UniProt entry",
  "url": "https://rest.uniprot.org/unisave/A0A559KX76?format=txt&versions=22",
  "source_sha256": "ccc24bde8b49d7a5bb0c8ef22b62f586b11fd80f8a26f4fbd799761ee5448140",
  "retrieved_utc": "2026-11-02T04:25:28.054482+00:00",
  "source_locator": "lines 49-54",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=5-O-(ADP-D-ribosyl)-L-glutamyl-[protein] + H2O = L-glutamyl-\nCC         [protein] + ADP-D-ribose + H(+); Xref=Rhea:RHEA:58248, Rhea:RHEA-\nCC         COMP:10208, Rhea:RHEA-COMP:15089, ChEBI:CHEBI:15377,\nCC         ChEBI:CHEBI:15378, ChEBI:CHEBI:29973, ChEBI:CHEBI:57967,\nCC         ChEBI:CHEBI:142540; Evidence={ECO:0000269|PubMed:39270823};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "entry_version": 22,
  "sequence_version": 1,
  "sequence_comparison": "matched"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 149. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
