# catalytic_activity_0136

[All questions](../README.md) · [Summary](../SUMMARY.md) · [Method](../METHOD.md) · [Exact reviewer input](../inputs/catalytic_activity_0136.txt)

**Task:** `catalytic_activity`  
**Expected answer:** **B** — L-histidine = D-histidine

| Reviewer | Expected-answer support | Reasoning versus lookup |
|---|---|---|
| GPT-6 Luna | supported | reasoning-supported |
| Qwen3.8-Flash-Next-NVFP4 | supported | reasoning-supported |

The reviewers assess the question and its expected answer. Their agreement is not expert confirmation. An unusable review is an output failure, not a finding that the question is wrong.

## Complete original question

```text
[Protein Sequence]
MDRKVQVLDFIKINPAGNITILIDNFDIYDKNIPKLSEEIMKETNLYAEQVGFIKDSHLQMMGGEFCGNASRAFASLLAFRDKDFSKQKNYNITCSGESKVLDVDVRNDGAKNKFLAKIKMPKFLSLEEINVDEYKLGLVRFSGINHFIFNIKENKETSFENIIDLVKKYLSNEEYSAFGIMFFDSDNLSMKPYVYVKEVGSGVYENSCASGTTALGYYLKKCKNLDRAKIVQPNGWLEYIIENDEMYIDGPVEIIAEGKIYIGK

[Multiple Choices]
A. glycyl-tRNA(Gly) + acetyl-CoA = N-acetylglycyl-tRNA(Gly) + CoA + H(+)
B. L-histidine = D-histidine
C. (9S)-hydroperoxy-(10E,12Z,15Z)-octadecatrienoate = colnelenate + H2O
D. benzoyl-CoA + L-lysyl-[protein] = N(6)-benzoyl-L-lysyl-[protein] + CoA + H(+)
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

> The sequence-matched UniProt entry annotates this reaction as L-histidine = D-histidine and cites experimental evidence (ECO:0000269). The archived record also contains the catalytic-activity annotation, though the underlying paper was not independently reviewed here.

Citations as saved: [C5](#evidence-c5), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The 265-residue sequence has two separated cysteines and no obvious canonical PLP-enzyme hallmark. A cofactor-independent racemase using cysteine acid/base chemistry is a plausible family-level inference; among these choices, B is the amino-acid stereoinversion reaction, whereas the others are distinct transferase or oxygenate-isomerization activities.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The sequence offers a transferable, though not definitive, cysteine-racemase hypothesis that meaningfully favors B over these alternatives. The cysteines alone are not diagnostic, so the inference is probabilistic rather than proof of this exact enzyme's activity.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The offered reactions describe distinct activities, and the sequence-based racemase inference favors only B.


### Important caveats

- The reviewer-only database annotation supports the key but was not part of the original model input.
- A pair of cysteines and lack of an obvious cofactor-binding hallmark do not independently establish racemase activity.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The 265-residue sequence has two separated cysteines and no obvious canonical PLP-enzyme hallmark. A cofactor-independent racemase using cysteine acid/base chemistry is a plausible family-level inference; among these choices, B is the amino-acid stereoinversion reaction, whereas the others are distinct transferase or oxygenate-isomerization activities.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a transferable, though not definitive, cysteine-racemase hypothesis that meaningfully favors B over these alternatives. The cysteines alone are not diagnostic, so the inference is probabilistic rather than proof of this exact enzyme's activity."
  },
  "case_id": "catalytic_activity_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C5",
      "H4"
    ],
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this reaction as L-histidine = D-histidine and cites experimental evidence (ECO:0000269). The archived record also contains the catalytic-activity annotation, though the underlying paper was not independently reviewed here."
  },
  "important_caveats": [
    "The reviewer-only database annotation supports the key but was not part of the original model input.",
    "A pair of cysteines and lack of an obvious cofactor-binding hallmark do not independently establish racemase activity."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions describe distinct activities, and the sequence-based racemase inference favors only B."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text
{
  "case_id": "catalytic_activity_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "The sequence-matched UniProt entry annotates this reaction as L-histidine = D-histidine and cites experimental evidence (ECO:0000269). The archived record also contains the catalytic-activity annotation, though the underlying paper was not independently reviewed here.",
    "evidence_ids": ["C5", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The 265-residue sequence has two separated cysteines and no obvious canonical PLP-enzyme hallmark. A cofactor-independent racemase using cysteine acid/base chemistry is a plausible family-level inference; among these choices, B is the amino-acid stereoinversion reaction, whereas the others are distinct transferase or oxygenate-isomerization activities.",
    "missing_item_specific_fact": "",
    "reason": "The sequence offers a transferable, though not definitive, cysteine-racemase hypothesis that meaningfully favors B over these alternatives. The cysteines alone are not diagnostic, so the inference is probabilistic rather than proof of this exact enzyme's activity."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The offered reactions describe distinct activities, and the sequence-based racemase inference favors only B."
  },
  "important_caveats": [
    "The reviewer-only database annotation supports the key but was not part of the original model input.",
    "A pair of cysteines and lack of an obvious cofactor-binding hallmark do not independently establish racemase activity."
  ]
}
```

</details>

## Qwen3.8-Flash-Next-NVFP4

**Saved status:** `valid_review`.

### Expected-answer support: supported

> UniProt Q8RI81 (HISR_FUSNN) is annotated as Histidine racemase (EC 5.1.1.24) with catalytic activity 'L-histidine = D-histidine', supported by experimental evidence (ECO:0000269, PubMed:39424140, 2024 JBC paper with X-ray crystallography of mutants Ser-67 and Ser-209, plus mutagenesis of Cys-67 and Cys-209). The benchmark sequence matches the UniProt sequence exactly (265 aa, SHA256 match confirmed). The annotation is experimentally validated, not merely computational.

Citations as saved: [C4](#evidence-c4), [C5](#evidence-c5), [C6](#evidence-c6), [H1](#evidence-h1), [H2](#evidence-h2), [H3](#evidence-h3), [H4](#evidence-h4).

### Reasoning versus lookup: reasoning-supported

**Discriminating biological argument**

> The four options represent very different enzyme classes. (1) Option C (lipoxygenase-type hydroperoxide dehydrase) is strongly disfavored: lipoxygenases and related lipid-peroxidation enzymes are typically 500-800+ aa with a conserved iron-binding domain (His-rich motif); this 265-aa protein is far too small. (2) Options A and D are acyltransferases (GNAT-fold or related); the sequence lacks recognizable GNAT acyltransferase motifs (e.g., the conserved Q/RxxGxG/A motif for CoA binding) and lacks the characteristic β-sheet/α-helix GNAT fold signature. (3) Option B (cofactor-independent amino acid racemase) is consistent with: the small size (265 aa, typical of bacterial amino acid racemases), the absence of a PLP-binding motif (ruling out PLP-dependent racemases but consistent with cofactor-independent ones), and the presence of two strategically positioned Cys residues (C67 in 'FCGNASRAF' and C209 in 'GSGVYENSCA') that match the catalytic dyad pattern seen in cofactor-independent racemases (e.g., cysteine racemase, aspartate racemase use Cys-based chemistry). A knowledgeable model can eliminate C by size, weaken A/D by absence of transferase motifs, and positively support B via Cys-residue chemistry and small-bacterial-racemase profile. This is probabilistic but meaningfully distinguishes B from the alternatives.


**Missing item-specific fact**

Empty string, as saved.


**Reason**

> The model can use general enzyme-class knowledge (size constraints for lipoxygenases, absence of GNAT motifs for transferases, Cys-based cofactor-independent racemase chemistry) to meaningfully favor B over A, C, and D. The inference is probabilistic and not a certainty proof, but it provides a concrete, transferable basis for distinguishing the offered alternatives without requiring recall of this specific protein's database annotation.


### Question ambiguity

**Multiple defensible options, exactly as saved:**

```json
[]
```

> The four options span four distinct enzyme classes (tRNA acetyltransferase, amino acid racemase, lipid hydroperoxide lyase, protein acyltransferase). Size eliminates C definitively; motif absence disfavors A and D; Cys-residue chemistry and small size support B. No two options are genuinely indistinguishable given the sequence.


### Important caveats

- This enzyme was only characterized experimentally in 2024 (PubMed:39424140) and annotated in UniProt in April 2025; before that, the sequence had no known function. A model trained on pre-2024 data would not have seen this annotation.
- The Cys-67/Cys-209 catalytic dyad identification is specific to this enzyme per the 2024 paper; a model would need to recognize the general Cys-racemase pattern rather than this specific pair.
- The elimination of A and D relies on absence of motifs rather than positive exclusion; some tRNA-modifying or protein-modifying enzymes lack canonical motifs, making the argument probabilistic rather than definitive.
- The reviewer evidence confirms sequence identity and experimental annotation but was not available to the evaluated model.

<details>
<summary>Complete saved parsed visible review</summary>

```json
{
  "answerability_check": {
    "discriminating_biological_argument": "The four options represent very different enzyme classes. (1) Option C (lipoxygenase-type hydroperoxide dehydrase) is strongly disfavored: lipoxygenases and related lipid-peroxidation enzymes are typically 500-800+ aa with a conserved iron-binding domain (His-rich motif); this 265-aa protein is far too small. (2) Options A and D are acyltransferases (GNAT-fold or related); the sequence lacks recognizable GNAT acyltransferase motifs (e.g., the conserved Q/RxxGxG/A motif for CoA binding) and lacks the characteristic β-sheet/α-helix GNAT fold signature. (3) Option B (cofactor-independent amino acid racemase) is consistent with: the small size (265 aa, typical of bacterial amino acid racemases), the absence of a PLP-binding motif (ruling out PLP-dependent racemases but consistent with cofactor-independent ones), and the presence of two strategically positioned Cys residues (C67 in 'FCGNASRAF' and C209 in 'GSGVYENSCA') that match the catalytic dyad pattern seen in cofactor-independent racemases (e.g., cysteine racemase, aspartate racemase use Cys-based chemistry). A knowledgeable model can eliminate C by size, weaken A/D by absence of transferase motifs, and positively support B via Cys-residue chemistry and small-bacterial-racemase profile. This is probabilistic but meaningfully distinguishes B from the alternatives.",
    "judgment": "reasoning_supported",
    "missing_item_specific_fact": "",
    "reason": "The model can use general enzyme-class knowledge (size constraints for lipoxygenases, absence of GNAT motifs for transferases, Cys-based cofactor-independent racemase chemistry) to meaningfully favor B over A, C, and D. The inference is probabilistic and not a certainty proof, but it provides a concrete, transferable basis for distinguishing the offered alternatives without requiring recall of this specific protein's database annotation."
  },
  "case_id": "catalytic_activity_0136",
  "expected_answer_check": {
    "evidence_ids": [
      "C4",
      "C5",
      "C6",
      "H1",
      "H2",
      "H3",
      "H4"
    ],
    "judgment": "supported",
    "reason": "UniProt Q8RI81 (HISR_FUSNN) is annotated as Histidine racemase (EC 5.1.1.24) with catalytic activity 'L-histidine = D-histidine', supported by experimental evidence (ECO:0000269, PubMed:39424140, 2024 JBC paper with X-ray crystallography of mutants Ser-67 and Ser-209, plus mutagenesis of Cys-67 and Cys-209). The benchmark sequence matches the UniProt sequence exactly (265 aa, SHA256 match confirmed). The annotation is experimentally validated, not merely computational."
  },
  "important_caveats": [
    "This enzyme was only characterized experimentally in 2024 (PubMed:39424140) and annotated in UniProt in April 2025; before that, the sequence had no known function. A model trained on pre-2024 data would not have seen this annotation.",
    "The Cys-67/Cys-209 catalytic dyad identification is specific to this enzyme per the 2024 paper; a model would need to recognize the general Cys-racemase pattern rather than this specific pair.",
    "The elimination of A and D relies on absence of motifs rather than positive exclusion; some tRNA-modifying or protein-modifying enzymes lack canonical motifs, making the argument probabilistic rather than definitive.",
    "The reviewer evidence confirms sequence identity and experimental annotation but was not available to the evaluated model."
  ],
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct enzyme classes (tRNA acetyltransferase, amino acid racemase, lipid hydroperoxide lyase, protein acyltransferase). Size eliminates C definitively; motif absence disfavors A and D; Cys-residue chemistry and small size support B. No two options are genuinely indistinguishable given the sequence."
  }
}
```

</details>

<details>
<summary>Exact saved visible final text</summary>

```text


{
  "case_id": "catalytic_activity_0136",
  "expected_answer_check": {
    "judgment": "supported",
    "reason": "UniProt Q8RI81 (HISR_FUSNN) is annotated as Histidine racemase (EC 5.1.1.24) with catalytic activity 'L-histidine = D-histidine', supported by experimental evidence (ECO:0000269, PubMed:39424140, 2024 JBC paper with X-ray crystallography of mutants Ser-67 and Ser-209, plus mutagenesis of Cys-67 and Cys-209). The benchmark sequence matches the UniProt sequence exactly (265 aa, SHA256 match confirmed). The annotation is experimentally validated, not merely computational.",
    "evidence_ids": ["C4", "C5", "C6", "H1", "H2", "H3", "H4"]
  },
  "answerability_check": {
    "judgment": "reasoning_supported",
    "discriminating_biological_argument": "The four options represent very different enzyme classes. (1) Option C (lipoxygenase-type hydroperoxide dehydrase) is strongly disfavored: lipoxygenases and related lipid-peroxidation enzymes are typically 500-800+ aa with a conserved iron-binding domain (His-rich motif); this 265-aa protein is far too small. (2) Options A and D are acyltransferases (GNAT-fold or related); the sequence lacks recognizable GNAT acyltransferase motifs (e.g., the conserved Q/RxxGxG/A motif for CoA binding) and lacks the characteristic β-sheet/α-helix GNAT fold signature. (3) Option B (cofactor-independent amino acid racemase) is consistent with: the small size (265 aa, typical of bacterial amino acid racemases), the absence of a PLP-binding motif (ruling out PLP-dependent racemases but consistent with cofactor-independent ones), and the presence of two strategically positioned Cys residues (C67 in 'FCGNASRAF' and C209 in 'GSGVYENSCA') that match the catalytic dyad pattern seen in cofactor-independent racemases (e.g., cysteine racemase, aspartate racemase use Cys-based chemistry). A knowledgeable model can eliminate C by size, weaken A/D by absence of transferase motifs, and positively support B via Cys-residue chemistry and small-bacterial-racemase profile. This is probabilistic but meaningfully distinguishes B from the alternatives.",
    "missing_item_specific_fact": "",
    "reason": "The model can use general enzyme-class knowledge (size constraints for lipoxygenases, absence of GNAT motifs for transferases, Cys-based cofactor-independent racemase chemistry) to meaningfully favor B over A, C, and D. The inference is probabilistic and not a certainty proof, but it provides a concrete, transferable basis for distinguishing the offered alternatives without requiring recall of this specific protein's database annotation."
  },
  "question_ambiguity": {
    "multiple_defensible_options": [],
    "reason": "The four options span four distinct enzyme classes (tRNA acetyltransferase, amino acid racemase, lipid hydroperoxide lyase, protein acyltransferase). Size eliminates C definitively; motif absence disfavors A and D; Cys-residue chemistry and small size support B. No two options are genuinely indistinguishable given the sequence."
  },
  "important_caveats": [
    "This enzyme was only characterized experimentally in 2024 (PubMed:39424140) and annotated in UniProt in April 2025; before that, the sequence had no known function. A model trained on pre-2024 data would not have seen this annotation.",
    "The Cys-67/Cys-209 catalytic dyad identification is specific to this enzyme per the 2024 paper; a model would need to recognize the general Cys-racemase pattern rather than this specific pair.",
    "The elimination of A and D relies on absence of motifs rather than positive exclusion; some tRNA-modifying or protein-modifying enzymes lack canonical motifs, making the argument probabilistic rather than definitive.",
    "The reviewer evidence confirms sequence identity and experimental annotation but was not available to the evaluated model."
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
  "benchmark_sequence_length": 265,
  "benchmark_sequence_sha256": "366955426ff1f55c671654b2e899936080724ffe2dc1099a5aecf063554e039c",
  "current_entry_audit": {
    "entryVersion": 81,
    "firstPublicDate": "2025-04-09",
    "lastAnnotationUpdateDate": "2026-09-02",
    "lastSequenceUpdateDate": "2002-06-01",
    "sequenceVersion": 1
  },
  "current_record_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "current_sequence_comparison": "matched",
  "current_source_sequence_length": 265,
  "current_source_sequence_sha256": "366955426ff1f55c671654b2e899936080724ffe2dc1099a5aecf063554e039c",
  "current_status": "retrieved",
  "current_uniprot_release": "2026_03",
  "historical_cutoff_date": "2026-05-07",
  "historical_sequence_comparison": "matched",
  "historical_sequence_versions_checked": [
    {
      "entry_version": 79,
      "exact_sequence_comparison": "matched",
      "sequence_version": 1
    }
  ],
  "historical_status": "retrieved",
  "identity_origin": "reviewer-only accession inferred mechanically from original dataset image-path metadata; this accession/metadata was absent from evaluated model input",
  "latest_at_cutoff_sequence_comparison": "matched",
  "numbering": "Canonical entry coordinates; construct or isoform numbering is not assumed.",
  "requested_accession": "Q8RI81",
  "selected_historical_entry_version": 79,
  "selected_historical_record_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "selected_historical_source_sequence_length": 265,
  "selected_historical_source_sequence_sha256": "366955426ff1f55c671654b2e899936080724ffe2dc1099a5aecf063554e039c",
  "selected_historical_version": {
    "accession": "Q8RI81",
    "database": "Swiss-Prot",
    "entryVersion": 79,
    "firstRelease": "2026_01/2026_01",
    "firstReleaseDate": "28-Jan-2026",
    "lastRelease": "2026_01/2026_01",
    "lastReleaseDate": "28-Jan-2026",
    "name": "HISR_FUSNN",
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

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C1",
  "excerpt": "\"Q8RI81\"",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/primaryAccession",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C2

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C2",
  "excerpt": "{\"entryVersion\":81,\"firstPublicDate\":\"2025-04-09\",\"lastAnnotationUpdateDate\":\"2026-09-02\",\"lastSequenceUpdateDate\":\"2002-06-01\",\"sequenceVersion\":1}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/entryAudit",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C3

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C3",
  "excerpt": "{\"lineage\":[\"Bacteria\",\"Fusobacteriati\",\"Fusobacteriota\",\"Fusobacteriia\",\"Fusobacteriales\",\"Fusobacteriaceae\",\"Fusobacterium\"],\"scientificName\":\"Fusobacterium nucleatum subsp. nucleatum (strain ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355)\",\"taxonId\":190304}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/organism",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C4

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C4",
  "excerpt": "{\"recommendedName\":{\"ecNumbers\":[{\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"value\":\"5.1.1.24\"}],\"fullName\":{\"evidences\":[{\"evidenceCode\":\"ECO:0000303\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"value\":\"Histidine racemase\"}}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/proteinDescription",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C5

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C5",
  "excerpt": "{\"commentType\":\"CATALYTIC ACTIVITY\",\"reaction\":{\"ecNumber\":\"5.1.1.24\",\"evidences\":[{\"evidenceCode\":\"ECO:0000269\",\"id\":\"39424140\",\"source\":\"PubMed\"}],\"name\":\"L-histidine = D-histidine\",\"reactionCrossReferences\":[{\"database\":\"Rhea\",\"id\":\"RHEA:59188\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:57595\"},{\"database\":\"ChEBI\",\"id\":\"CHEBI:142967\"}]}}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/comments/1",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence C6

[UniProtKB current entry](https://rest.uniprot.org/uniprotkb/Q8RI81.json)

```json
{
  "evidence_id": "C6",
  "excerpt": "{\"citation\":{\"authors\":[\"Lamer T.\",\"Chen P.\",\"Venter M.J.\",\"van Belkum M.J.\",\"Wijewardane A.\",\"Wu C.\",\"Lemieux M.J.\",\"Vederas J.C.\"],\"citationCrossReferences\":[{\"database\":\"PubMed\",\"id\":\"39424140\"},{\"database\":\"DOI\",\"id\":\"10.1016/j.jbc.2024.107896\"}],\"citationType\":\"journal article\",\"firstPage\":\"107896\",\"id\":\"39424140\",\"journal\":\"J. Biol. Chem.\",\"lastPage\":\"107896\",\"publicationDate\":\"2024\",\"title\":\"Discovery, characterization, and structure of a cofactor-independent histidine racemase from the oral pathogen Fusobacterium nucleatum.\",\"volume\":\"300\"},\"evidences\":[{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9CR1\",\"source\":\"PDB\"},{\"evidenceCode\":\"ECO:0007744\",\"id\":\"9CR6\",\"source\":\"PDB\"}],\"referenceComments\":[{\"type\":\"STRAIN\",\"value\":\"ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355\"}],\"referenceNumber\":3,\"referencePositions\":[\"X-RAY CRYSTALLOGRAPHY (2.5 ANGSTROMS) OF MUTANTS SER-67 AND SER-209\",\"FUNCTION\",\"CATALYTIC ACTIVITY\",\"ACTIVITY REGULATION\",\"BIOPHYSICOCHEMICAL PROPERTIES\",\"SUBUNIT\",\"ACTIVE SITE\",\"MUTAGENESIS OF CYS-67 AND CYS-209\"]}",
  "excerpt_format": "canonical JSON value at JSON pointer",
  "json_pointer": "/references/2",
  "retrieved_utc": "2026-11-01T06:25:25.407556+00:00",
  "sequence_comparison": "matched",
  "source": "UniProtKB current entry",
  "source_scope": "current snapshot; actual author source snapshot unknown",
  "source_sha256": "0b210dc9bf403c4b7aabdf6972f59e66a6825c5dadefc8b002828f6d21b33d6b",
  "url": "https://rest.uniprot.org/uniprotkb/Q8RI81.json"
}
```

### Evidence H1

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)

```json
{
  "entry_version": 79,
  "evidence_id": "H1",
  "excerpt": "ID   HISR_FUSNN              Reviewed;         265 AA.\nAC   Q8RI81;\nDT   09-APR-2025, integrated into UniProtKB/Swiss-Prot.\nDT   01-JUN-2002, sequence version 1.\nDT   28-JAN-2026, entry version 79.\nDE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};\nDE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};\nGN   Name=hisR {ECO:0000303|PubMed:39424140};\nGN   OrderedLocusNames=FN1732 {ECO:0000312|EMBL:AAL93847.1};\nOS   Fusobacterium nucleatum subsp. nucleatum (strain ATCC 25586 / DSM 15643 /\nOS   BCRC 10681 / CIP 101130 / JCM 8532 / KCTC 2640 / LMG 13131 / VPI 4355).\nOC   Bacteria; Fusobacteriati; Fusobacteriota; Fusobacteriia; Fusobacteriales;\nOC   Fusobacteriaceae; Fusobacterium.\nOX   NCBI_TaxID=190304;\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.693468+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 1-14",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "url": "https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79"
}
```

### Evidence H2

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)

```json
{
  "entry_version": 79,
  "evidence_id": "H2",
  "excerpt": "DE   RecName: Full=Histidine racemase {ECO:0000303|PubMed:39424140};\nDE            EC=5.1.1.24 {ECO:0000269|PubMed:39424140};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.693468+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 6-7",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "url": "https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79"
}
```

### Evidence H3

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)

```json
{
  "entry_version": 79,
  "evidence_id": "H3",
  "excerpt": "RN   [3] {ECO:0007744|PDB:9CR1, ECO:0007744|PDB:9CR6}\nRP   X-RAY CRYSTALLOGRAPHY (2.5 ANGSTROMS) OF MUTANTS SER-67 AND SER-209,\nRP   FUNCTION, CATALYTIC ACTIVITY, ACTIVITY REGULATION, BIOPHYSICOCHEMICAL\nRP   PROPERTIES, SUBUNIT, ACTIVE SITE, AND MUTAGENESIS OF CYS-67 AND CYS-209.\nRC   STRAIN=ATCC 25586 / DSM 15643 / BCRC 10681 / CIP 101130 / JCM 8532 / KCTC\nRC   2640 / LMG 13131 / VPI 4355;\nRX   PubMed=39424140; DOI=10.1016/j.jbc.2024.107896;\nRA   Lamer T., Chen P., Venter M.J., van Belkum M.J., Wijewardane A., Wu C.,\nRA   Lemieux M.J., Vederas J.C.;\nRT   \"Discovery, characterization, and structure of a cofactor-independent\nRT   histidine racemase from the oral pathogen Fusobacterium nucleatum.\";\nRL   J. Biol. Chem. 300:107896-107896(2024).\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.693468+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 36-47",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "url": "https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79"
}
```

### Evidence H4

[UniSave archived UniProt entry](https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79)

```json
{
  "entry_version": 79,
  "evidence_id": "H4",
  "excerpt": "CC   -!- CATALYTIC ACTIVITY:\nCC       Reaction=L-histidine = D-histidine; Xref=Rhea:RHEA:59188,\nCC         ChEBI:CHEBI:57595, ChEBI:CHEBI:142967; EC=5.1.1.24;\nCC         Evidence={ECO:0000269|PubMed:39424140};\n",
  "excerpt_format": "literal contiguous UniProt flat-file lines",
  "retrieved_utc": "2026-11-01T06:28:41.693468+00:00",
  "sequence_comparison": "matched",
  "sequence_version": 1,
  "source": "UniSave archived UniProt entry",
  "source_locator": "lines 55-58",
  "source_scope": "record released no later than 2026-05-07; actual author source snapshot unknown",
  "source_sha256": "c6b9df06883840dd205917d83d0a4b738a80a6e8becaecd06bbb78bb24df9da2",
  "url": "https://rest.uniprot.org/unisave/Q8RI81?format=txt&versions=79"
}
```

---

Original question/key: [pinned source](https://github.com/Rongdingyi/LiveProteinBench/blob/8b9710932511f816651fc1a7e8a1bc85c3c77767/dataset/QA/catalytic_activity.json), zero-based source row 136. © 2026 LiveProteinBench contributors; [CC BY 4.0](https://huggingface.co/datasets/LiveProteinBench/LiveProteinBench/blob/8428f64e33d53330f7745376d9c45de2d2c37eaf/LICENSE). [Source credits](../THIRD_PARTY_NOTICES.md).
