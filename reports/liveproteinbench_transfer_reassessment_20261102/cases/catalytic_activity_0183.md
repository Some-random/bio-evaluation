# catalytic_activity_0183

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0183.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **A** — beta-amyrin + 3 reduced &#91;NADPH--hemoprotein reductase&#93; + 3 O2 = oleanolate + 3 oxidized &#91;NADPH--hemoprotein reductase&#93; + 4 H2O + 4 H(+)

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | lookup-dependent |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MELFFICGLVLFSTLSLISLFLLHNHSSARGYRLPPGRMGWPFIGESYEFLANGWKGYPEKFIFSRLAKYKPNQVFKTSILGEKVAVMCGATCNKFLFSNEGKLVNAWWPNSVNKIFPSSTQTSSKEEAKKMRKLLPTFFKPEALQRYIPIMDEIAIRHMEDEWEGKSKIEVFPLAKRYTFWLACRLFLSIDDPVHVAKFADPFNDIASGIISIPIDLPGTPFNRGIKASNVVRQELKTIIKQRKLDLSDNKASPTQDILSHMLLTPDEDGRYMNELDIADKILGLLIGGHDTASAACTFVVKFLAELPHIYDGVYKEQMEIAKSKKEGERLNWEDIQKMKYSWNVACEVMRLAPPLQGAFREALSDFMYAGFQIPKGWKLYWSANSTHRNPECFPEPEKFDPARFDGSGPAPYTYVPFGGGPRMCPGKEYARLEILVFMHNIVKRFKWEKLIPDETIVVNPMPTPAKGLPVRLRPHSKPVTVSA

[Multiple Choices]
A. beta-amyrin + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = oleanolate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)
B. a 14alpha-hydroxymethyl steroid + reduced [NADPH--hemoprotein reductase] + O2 = a 14alpha-formyl steroid + oxidized [NADPH--hemoprotein reductase] + 2 H2O + H(+)
C. L-proline betaine + NADH + O2 + H(+) = N-methyl-L-proline + formaldehyde + NAD(+) + H2O
D. a 1,2-diacyl-sn-glycero-3-phosphocholine + H2O = a 1-acyl-sn-glycero-3-phosphocholine + a fatty acid + H(+)
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

> The sequence-matched UniProt annotation gives the exact beta-amyrin-to-oleanolate reaction in choice A and cites experimental evidence (ECO:0000269). The historical entry also records this reaction; the cited paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: lookup-dependent

**Discriminating biological argument**

Empty string, as saved.


**Missing item-specific fact**

> Whether this particular P450 oxidizes beta-amyrin to oleanolate rather than catalyzing the steroid oxidation in choice B.


**Reason**

> The hydrophobic N-terminus and conserved P450 heme-binding feature support a membrane-associated cytochrome P450, making choices A and B more plausible than the non-P450 alternatives. But both A and B describe P450-type oxidation, and these broad sequence features do not meaningfully distinguish their substrates or products. That distinction requires item-specific substrate-specificity evidence or a sufficiently informative homolog/family assignment.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The supplied sequence alone leaves uncertainty between the two P450-like reactions, but the sequence-matched catalytic-activity evidence supports A rather than identifying multiple defensible answers.


### Important caveats

- The database annotation cites experimental evidence, but the cited primary paper was not independently validated here.
- The exact author source snapshot is unknown.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "",
    "judgment": "lookup_or_memorization_dependent",
    "missing_item_specific_fact": "Whether this particular P450 oxidizes beta-amyrin to oleanolate rather than catalyzing the steroid oxidation in choice B.",
    "reason": "The hydrophobic N-terminus and conserved P450 heme-binding feature support a membrane-associated cytochrome P450, making choices A and B more plausible than the non-P450 alternatives. But both A and B describe P450-type oxidation, and these broad sequence features do not meaningfully distinguish their substrates or products. That distinction requires item-specific substrate-specificity evidence or a sufficiently informative homolog/family assignment."
  },
  "case_id": "catalytic_activity_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation gives the exact beta-amyrin-to-oleanolate reaction in choice A and cites experimental evidence (ECO:0000269). The historical entry also records this reaction; the cited paper was not independently reviewed here."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the cited primary paper was not independently validated here.",
    "The exact author source snapshot is unknown."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone leaves uncertainty between the two P450-like reactions, but the sequence-matched catalytic-activity evidence supports A rather than identifying multiple defensible answers."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt annotation gives the exact beta-amyrin-to-oleanolate reaction in choice A and cites experimental evidence (ECO:0000269). The historical entry also records this reaction; the cited paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "lookup_or_memorization_dependent",
    "discriminating_biological_argument": "",
    "missing_item_specific_fact": "Whether this particular P450 oxidizes beta-amyrin to oleanolate rather than catalyzing the steroid oxidation in choice B.",
    "reason": "The hydrophobic N-terminus and conserved P450 heme-binding feature support a membrane-associated cytochrome P450, making choices A and B more plausible than the non-P450 alternatives. But both A and B describe P450-type oxidation, and these broad sequence features do not meaningfully distinguish their substrates or products. That distinction requires item-specific substrate-specificity evidence or a sufficiently informative homolog/family assignment."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The supplied sequence alone leaves uncertainty between the two P450-like reactions, but the sequence-matched catalytic-activity evidence supports A rather than identifying multiple defensible answers."
  },
  "important_caveats": [
    "The database annotation cites experimental evidence, but the cited primary paper was not independently validated here.",
    "The exact author source snapshot is unknown."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> The UniProt entry A0AAW1NEA3 (sequence matched exactly, 485 aa) annotates this protein as Beta-amyrin 28-monooxygenase CYP716A378 (EC 1.14.14.126) with the catalytic reaction 'beta-amyrin + 3 reduced &#91;NADPH--hemoprotein reductase&#93; + 3 O2 = oleanolate + 3 oxidized &#91;NADPH--hemoprotein reductase&#93; + 4 H2O + 4 H(+)', matching option A verbatim. The annotation is backed by experimental evidence (ECO:0000269, PubMed:39043959, Nat. Chem. Biol. 2025).

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [H2](#evidence-h2), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The sequence contains the canonical P450 heme-binding motif (…VAVMCGATCNK…, with the conserved axial-ligand Cys) and the FxxGxxxCxG pattern, identifying it as a cytochrome P450 monooxygenase. This immediately eliminates C (NADH-dependent demethylase, no hemoprotein reductase) and D (phospholipase A2 hydrolysis, no cofactors). The N-terminal hydrophobic signal/transmembrane anchor and ~485 aa length are hallmarks of plant microsomal P450s. Among plant P450 families, the CYP716 family is the best-characterized clade of triterpene C-28 oxidases (converting beta-amyrin to oleanolic acid/oleanolate via three sequential oxidations). Sequence features visible here—the specific IFS/KRY motifs near the heme domain, the overall domain architecture, and the ~485 aa length—align with CYP716 family members (e.g., CYP716A1, CYP716A12 from Medicago, CYP716A17/18) rather than with steroid-oxidizing families such as CYP90 or CYP714, which tend to have different substrate-binding pocket compositions and slightly different N-terminal extensions. The CYP716–triterpene association is a well-established family-level regularity learned from numerous characterized homologs across Medicago, Glycyrrhiza, Panax, and other plants. Thus, recognizing the CYP716 family signature supports option A (triterpene oxidation) over option B (steroid oxidation).


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The P450 identity is directly readable from the heme-binding motif, eliminating C and D. The plant P450 context and CYP716 family-level sequence signatures (length, conserved motifs, substrate-pocket architecture) provide a credible transferable inference toward triterpene (beta-amyrin) oxidation rather than steroid oxidation, consistent with the well-documented CYP716 family function across many characterized homologs.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> Options C and D are clearly incompatible with a P450 enzyme. Between A and B, the CYP716 family signature and the triterpene-oxidation association provide a meaningful distinction favoring A, though the discrimination between CYP716 and steroid-oxidizing families from sequence alone is not absolute without alignment.


### Important caveats

- The CYP716 vs CYP72/CYP90 family assignment from raw sequence without BLAST alignment is a probabilistic family-level inference, not a certainty; however, the CYP716 family is among the most well-characterized plant P450 families, making the triterpene-oxidation inference reasonably robust.
- The UniProt annotation is experimental (ECO:0000269) from a 2025 Nat. Chem. Biol. paper; the protein was only integrated into Swiss-Prot in January 2026, so the original benchmark author may have sourced it from the pre-publication or EMBL record.
- Options C and D are strong distractors that are trivially eliminated by P450 cofactor requirements, which may make the effective choice between A and B the main challenge.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif (…VAVMCGATCNK…, with the conserved axial-ligand Cys) and the FxxGxxxCxG pattern, identifying it as a cytochrome P450 monooxygenase. This immediately eliminates C (NADH-dependent demethylase, no hemoprotein reductase) and D (phospholipase A2 hydrolysis, no cofactors). The N-terminal hydrophobic signal/transmembrane anchor and ~485 aa length are hallmarks of plant microsomal P450s. Among plant P450 families, the CYP716 family is the best-characterized clade of triterpene C-28 oxidases (converting beta-amyrin to oleanolic acid/oleanolate via three sequential oxidations). Sequence features visible here—the specific IFS/KRY motifs near the heme domain, the overall domain architecture, and the ~485 aa length—align with CYP716 family members (e.g., CYP716A1, CYP716A12 from Medicago, CYP716A17/18) rather than with steroid-oxidizing families such as CYP90 or CYP714, which tend to have different substrate-binding pocket compositions and slightly different N-terminal extensions. The CYP716–triterpene association is a well-established family-level regularity learned from numerous characterized homologs across Medicago, Glycyrrhiza, Panax, and other plants. Thus, recognizing the CYP716 family signature supports option A (triterpene oxidation) over option B (steroid oxidation).",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The P450 identity is directly readable from the heme-binding motif, eliminating C and D. The plant P450 context and CYP716 family-level sequence signatures (length, conserved motifs, substrate-pocket architecture) provide a credible transferable inference toward triterpene (beta-amyrin) oxidation rather than steroid oxidation, consistent with the well-documented CYP716 family function across many characterized homologs."
  },
  "case_id": "catalytic_activity_0183",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "H2",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1NEA3 (sequence matched exactly, 485 aa) annotates this protein as Beta-amyrin 28-monooxygenase CYP716A378 (EC 1.14.14.126) with the catalytic reaction 'beta-amyrin + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = oleanolate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)', matching option A verbatim. The annotation is backed by experimental evidence (ECO:0000269, PubMed:39043959, Nat. Chem. Biol. 2025)."
  },
  "important_caveats": [
    "The CYP716 vs CYP72/CYP90 family assignment from raw sequence without BLAST alignment is a probabilistic family-level inference, not a certainty; however, the CYP716 family is among the most well-characterized plant P450 families, making the triterpene-oxidation inference reasonably robust.",
    "The UniProt annotation is experimental (ECO:0000269) from a 2025 Nat. Chem. Biol. paper; the protein was only integrated into Swiss-Prot in January 2026, so the original benchmark author may have sourced it from the pre-publication or EMBL record.",
    "Options C and D are strong distractors that are trivially eliminated by P450 cofactor requirements, which may make the effective choice between A and B the main challenge."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incompatible with a P450 enzyme. Between A and B, the CYP716 family signature and the triterpene-oxidation association provide a meaningful distinction favoring A, though the discrimination between CYP716 and steroid-oxidizing families from sequence alone is not absolute without alignment."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0183",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The UniProt entry A0AAW1NEA3 (sequence matched exactly, 485 aa) annotates this protein as Beta-amyrin 28-monooxygenase CYP716A378 (EC 1.14.14.126) with the catalytic reaction 'beta-amyrin + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = oleanolate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)', matching option A verbatim. The annotation is backed by experimental evidence (ECO:0000269, PubMed:39043959, Nat. Chem. Biol. 2025).",
    "evidence_ids": ["C4", "C5", "H2", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The sequence contains the canonical P450 heme-binding motif (…VAVMCGATCNK…, with the conserved axial-ligand Cys) and the FxxGxxxCxG pattern, identifying it as a cytochrome P450 monooxygenase. This immediately eliminates C (NADH-dependent demethylase, no hemoprotein reductase) and D (phospholipase A2 hydrolysis, no cofactors). The N-terminal hydrophobic signal/transmembrane anchor and ~485 aa length are hallmarks of plant microsomal P450s. Among plant P450 families, the CYP716 family is the best-characterized clade of triterpene C-28 oxidases (converting beta-amyrin to oleanolic acid/oleanolate via three sequential oxidations). Sequence features visible here—the specific IFS/KRY motifs near the heme domain, the overall domain architecture, and the ~485 aa length—align with CYP716 family members (e.g., CYP716A1, CYP716A12 from Medicago, CYP716A17/18) rather than with steroid-oxidizing families such as CYP90 or CYP714, which tend to have different substrate-binding pocket compositions and slightly different N-terminal extensions. The CYP716–triterpene association is a well-established family-level regularity learned from numerous characterized homologs across Medicago, Glycyrrhiza, Panax, and other plants. Thus, recognizing the CYP716 family signature supports option A (triterpene oxidation) over option B (steroid oxidation).",
    "missing_item_specific_fact": "",
    "reason": "The P450 identity is directly readable from the heme-binding motif, eliminating C and D. The plant P450 context and CYP716 family-level sequence signatures (length, conserved motifs, substrate-pocket architecture) provide a credible transferable inference toward triterpene (beta-amyrin) oxidation rather than steroid oxidation, consistent with the well-documented CYP716 family function across many characterized homologs."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "Options C and D are clearly incompatible with a P450 enzyme. Between A and B, the CYP716 family signature and the triterpene-oxidation association provide a meaningful distinction favoring A, though the discrimination between CYP716 and steroid-oxidizing families from sequence alone is not absolute without alignment."
  },
  "important_caveats": [
    "The CYP716 vs CYP72/CYP90 family assignment from raw sequence without BLAST alignment is a probabilistic family-level inference, not a certainty; however, the CYP716 family is among the most well-characterized plant P450 families, making the triterpene-oxidation inference reasonably robust.",
    "The UniProt annotation is experimental (ECO:0000269) from a 2025 Nat. Chem. Biol. paper; the protein was only integrated into Swiss-Prot in January 2026, so the original benchmark author may have sourced it from the pre-publication or EMBL record.",
    "Options C and D are strong distractors that are trivially eliminated by P450 cofactor requirements, which may make the effective choice between A and B the main challenge."
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
  "benchmark_sequence_length": 485,
  "benchmark_sequence_sha256": "c4bff1f7e639d9ca658ce7a8d1b4bea128f38e1d86d04bfb0390444eed1c9e39",
  "current_entry_audit": {
    "entryVersion": 6,
    "firstPublicDate": "2025-06-18",
    "lastAnnotationUpdateDate": "2026-06-10",
    "lastSequenceUpdateDate": "2024-11-27",
    "sequenceVersion": 1
  },
  "current_record_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 485,
  "current_source_sequence_sha256": "c4bff1f7e639d9ca658ce7a8d1b4bea128f38e1d86d04bfb0390444eed1c9e39",
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
  "requested_accession": "A0AAW1NEA3",
  "selected_historical_entry_version": 5,
  "selected_historical_record_sha256": "8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5",
  "selected_historical_source_sequence_length": 485,
  "selected_historical_source_sequence_sha256": "c4bff1f7e639d9ca658ce7a8d1b4bea128f38e1d86d04bfb0390444eed1c9e39",
  "selected_historical_version": {
    "accession": "A0AAW1NEA3",
    "database": "Swiss-Prot",
    "entryVersion": 5,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "C7168_SAPOF",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"A0AAW1NEA3\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":6,\"firstPublicDate\":\"2025-06-18\",\"lastAnnotationUpdateDate\":\"2026-06-10\",\"lastSequenceUpdateDate\":\"2024-11-27\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"commonName\":\"Common soapwort\",\"lineage\":[\"Eukaryota\",\"Viridiplantae\",\"Streptophyta\",\"Embryophyta\",\"Tracheophyta\",\"Spermatophyta\",\"Magnoliopsida\",\"eudicotyledons\",\"Gunneridae\",\"Pentapetalae\",\"Caryophyllales\",\"Caryophyllaceae\",\"Caryophylleae\",\"Saponaria\"],\"scientificName\":\"Saponaria officinalis\",\"synonyms\":[\"Lychnis saponaria\"],\"taxonId\":3572}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"alternativeNames\":[{\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"Cytochrome P450 716A378\"},\"shortNames\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"SoCYP716A378\"}]}],\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"value\":\"1.14.14.126\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000305\"}],\"value\":\"Beta-amyrin 28-monooxygenase CYP716A378\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"physiologicalReactions\":[{\"directionType\":\"left-to-right\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"reactionCrossReference\":{\"database\":\"Rhea\",\"id\":\"RHEA:43069\"}}],\"reaction\":{\"ecNumber\":\"1.14.14.126\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39043959\",\"source\":\"PubMed\"}],\"name\":\"beta-amyrin + 3 reduced [NADPH--hemoprotein reductase] + 3 O2 = oleanolate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4 H(+)\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:43068\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11964\"},{\"database\":\"Rhea\",\"id\":\"RHEA-COMP:11965\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:10352\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15377\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15378\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:15379\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57618\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:58210\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:82828\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Jo S.\",\"El-Demerdash A.\",\"Owen C.\",\"Srivastava V.\",\"Wu D.\",\"Kikuchi S.\",\"Reed J.\",\"Hodgson H.\",\"Harkess A.\",\"Shu S.\",\"Plott C.\",\"Jenkins J.\",\"Williams M.\",\"Boston L.-B.\",\"Lacchini E.\",\"Qu T.\",\"Goossens A.\",\"Grimwood J.\",\"Schmutz J.\",\"Leebens-Mack J.\",\"Osbourn A.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39043959\"},{\"database\":\"DOI\",\"id\":\"10.1038/s41589-024-01681-7\"}],\"citationType\":\"journal article\",\"firstPage\":\"215\",\"id\":\"39043959\",\"journal\":\"Nat. Chem. Biol.\",\"lastPage\":\"226\",\"publicationDate\":\"2025\",\"title\":\"Unlocking saponin biosynthesis in soapwort.\",\"volume\":\"21\"},\"evidences\":[{\"evidenceCode\":\"ECO:0000312\",\"id\":\"WWM48148.1\",\"source\":\"EMBL\"}],\"referenceNumber\":1,\"referencePositions\":[\"NUCLEOTIDE SEQUENCE [MRNA]\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"TISSUE SPECIFICITY\",\"PATHWAY\",\"BIOTECHNOLOGY\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/0",
  "retrieved_utc": "2026-11-01T06:24:55.776537+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "3395db4e25f9768c60ce7cac240774ed32dd3f474abfda702e2c591ef35e9a76",
  "url": "https://rest.uniprot.org/uniprotkb/A0AAW1NEA3.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H1",
  "excerpt": "ID   C7168_SAPOF             Reviewed;         485 AA.\nAC   A0AAW1NEA3;\nDT   18-JUN-2025, integrated into UniProtKB/Swiss-Prot.\nDT   27-NOV-2024, sequence version 1.\nDT   28-JAN-2026, entry version 5.\nDE   RecName: Full=Beta-amyrin 28-monooxygenase CYP716A378 {ECO:0000305};\nDE            EC=1.14.14.126 {ECO:0000269|PubMed:39043959};\nDE   AltName: Full=Cytochrome P450 716A378 {ECO:0000303|PubMed:39043959};\nDE            Short=SoCYP716A378 {ECO:0000303|PubMed:39043959};\nGN   Name=CYP716A378 {ECO:0000303|PubMed:39043959};\nGN   Synonyms=Saoffv11003497m {ECO:0000303|PubMed:39043959};\nGN   ORFNames=RND81_01G137900 {ECO:0000312|EMBL:KAK9757076.1};\nOS   Saponaria officinalis (Common soapwort) (Lychnis saponaria).\nOC   Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;\nOC   Spermatophyta; Magnoliopsida; eudicotyledons; Gunneridae; Pentapetalae;\nOC   Caryophyllales; Caryophyllaceae; Caryophylleae; Saponaria.\nOX   NCBI_TaxID=3572;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:40.561544+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-17",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5",
  "url": "https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Beta-amyrin 28-monooxygenase CYP716A378 {ECO:0000305};\nDE            EC=1.14.14.126 {ECO:0000269|PubMed:39043959};\nDE   AltName: Full=Cytochrome P450 716A378 {ECO:0000303|PubMed:39043959};\nDE            Short=SoCYP716A378 {ECO:0000303|PubMed:39043959};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:40.561544+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-9",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5",
  "url": "https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H3",
  "excerpt": "RN   [1] {ECO:0000312|EMBL:WWM48148.1}\nRP   NUCLEOTIDE SEQUENCE [MRNA], FUNCTION, CATALYTIC ACTIVITY, TISSUE\nRP   SPECIFICITY, PATHWAY, AND BIOTECHNOLOGY.\nRX   PubMed=39043959; DOI=10.1038/s41589-024-01681-7;\nRA   Jo S., El-Demerdash A., Owen C., Srivastava V., Wu D., Kikuchi S., Reed J.,\nRA   Hodgson H., Harkess A., Shu S., Plott C., Jenkins J., Williams M.,\nRA   Boston L.-B., Lacchini E., Qu T., Goossens A., Grimwood J., Schmutz J.,\nRA   Leebens-Mack J., Osbourn A.;\nRT   \"Unlocking saponin biosynthesis in soapwort.\";\nRL   Nat. Chem. Biol. 21:215-226(2025).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:40.561544+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 18-27",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5",
  "url": "https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5)

```json
{
  "entry_version": 5,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=beta-amyrin + 3 reduced [NADPH--hemoprotein reductase] + 3 O2\nCC         = oleanolate + 3 oxidized [NADPH--hemoprotein reductase] + 4 H2O + 4\nCC         H(+); Xref=Rhea:RHEA:43068, Rhea:RHEA-COMP:11964, Rhea:RHEA-\nCC         COMP:11965, ChEBI:CHEBI:10352, ChEBI:CHEBI:15377, ChEBI:CHEBI:15378,\nCC         ChEBI:CHEBI:15379, ChEBI:CHEBI:57618, ChEBI:CHEBI:58210,\nCC         ChEBI:CHEBI:82828; EC=1.14.14.126;\nCC         Evidence={ECO:0000269|PubMed:39043959};\nCC       PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:43069;\nCC         Evidence={ECO:0000269|PubMed:39043959};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:27:40.561544+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 42-51",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "8601238c4d3910ff611c06a4f863e8c633074e9e3c66a978a480c31233a972f5",
  "url": "https://rest.uniprot.org/unisave/A0AAW1NEA3?format=txt&versions=5"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 183. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
